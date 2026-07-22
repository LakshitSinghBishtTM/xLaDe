# xLaDe Architecture

## 1. Purpose of This Document

This document describes the **architectural intent and current structure** of
the xLaDe repository. It is intended for contributors and researchers who want
to understand how the project is organised, where boundaries lie, and how
components relate to each other.

xLaDe is an experimental project. This document reflects the current state
accurately rather than describing an aspirational design.

---

## 2. Architectural Philosophy

xLaDe is guided by three core principles:

**Non-invasive experimentation.**
Experiments must not modify Lean's trusted kernel or core semantics. All
observable effects must be attributable to ecosystem-level design decisions,
not language modification.

**Explicit architectural boundaries.**
The repository clearly distinguishes between components that are fixed
(the Lean kernel) and components that may evolve (experiments, tooling,
policies, CLI). This boundary is enforced by CI, not just documented.

**Minimal core with demand-driven growth.**
New abstractions are introduced only in response to concrete use cases.
The architecture stays lean — pun intended.

---

## 3. Repository Structure

```
xLaDe/
├── .github/
│   └── workflows/          CI — tests, kernel protection, mirrors
├── bin/
│   └── xlade               CLI entrypoint (calls xlade.cli.main)
├── docs/                   Design rationale and usage documentation
├── examples/               Minimal Lean 4 examples
├── experiments/            Ecosystem experiments (each is a directory)
│   ├── exp-001-proof-review/
│   ├── exp-002-kernel-boundary/
│   └── exp-003-doc-coverage/
├── lean-core/              Lean 4 source (git submodule, immutable)
├── metrics/                Research artifact files (qualitative .md)
├── modes/
│   ├── experimental/
│   ├── onboarding/
│   └── stable/
├── policies/               Repository governance documents
├── scripts/                Policy enforcement shell scripts
├── security/               Threat model, trust model, security policy
├── tests/                  83-test pytest suite
│   ├── conftest.py
│   ├── test_check.py
│   ├── test_doctor.py
│   ├── test_exp003.py
│   ├── test_init.py
│   ├── test_lean_core.py
│   ├── test_list_experiments.py
│   ├── test_metrics.py
│   ├── test_mode.py
│   ├── test_run.py
│   ├── test_run_execution.py
│   └── test_status.py
├── tools/                  Optional helper utilities
├── xlade/                  Python CLI package
│   ├── cli/
│   │   ├── check.py
│   │   ├── doctor.py
│   │   ├── init.py
│   │   ├── list_experiments.py
│   │   ├── main.py
│   │   ├── metrics.py
│   │   ├── mode.py
│   │   ├── run.py
│   │   └── status.py
│   └── core/
│       ├── errors.py
│       └── lean.py         Subprocess wrapper — LeanResult, run_lake_script, etc.
├── lakefile.lean           Root Lake configuration
├── lake-manifest.json      Locked dependency graph
├── lean-toolchain          Pinned Lean compiler version
├── pyproject.toml          Python packaging
└── VERSION                 Current version string
```

---

## 4. Architectural Boundaries

### 4.1 Stable Components — Do Not Modify

**Lean kernel and core semantics.**
The `lean-core/` submodule is immutable. It is included as a reference
baseline only. No experiment, mode, or tool may modify it.

**Core compiler behaviour.**
Changes to elaboration, type checking, or evaluation semantics are out of
scope for xLaDe entirely.

CI enforces kernel immutability on every pull request. Any modification to
`lean-core/` is detected and the build fails.

### 4.2 Experimental Components — Safe to Modify

Everything outside `lean-core/` is an experimental component:

- Repository layout and organisation
- CLI behaviour and commands
- Experiment definitions and scripts
- Policy enforcement mechanisms
- Metrics and evaluation artifacts
- Documentation

These are the primary focus of xLaDe. Changes here are expected to be
reversible and well-documented.

---

## 5. The Python CLI Layer — `xlade/`

The CLI is a pure Python package installed via `pip install -e .`. It
provides all user-facing commands and orchestrates experiment execution.

```
xlade/
├── cli/        One module per command (init, run, status, doctor, ...)
└── core/
    ├── errors.py   Shared error formatting
    └── lean.py     All subprocess calls to lake and lean
```

### `xlade/core/lean.py`

This module is the single point of contact between the Python CLI and the
Lean toolchain. All `subprocess` calls to `lake` and `lean` go through here.

It exposes:

- `LeanResult` — dataclass with `success`, `returncode`, `stdout`, `stderr`,
  `command` fields. Supports `bool()` directly (`if result:`).
- `run_lake_script(script_name, cwd, passthrough)` — runs `lake script run`
- `run_lake_build(cwd, passthrough)` — runs `lake build`
- `run_lean_file(path, passthrough)` — runs `lean <file>`
- `run_script(entry, cwd, passthrough)` — runs `bash <script>`
- `lean_version()` / `lake_version()` — version queries

All functions check for the binary first and return a failed `LeanResult`
with a human-readable message if it is not found. Exceptions from subprocess
are caught internally. Callers never handle raw subprocess errors.

`passthrough=True` streams output to the terminal live (default for
experiment runs). `passthrough=False` captures stdout/stderr and returns
them in the result (default for version queries and diagnostics).

### `xlade/cli/run.py`

Orchestrates experiment execution. Reads `experiment.toml`, validates
workspace and mode, dispatches to `xlade/core/lean.py` based on experiment
type, writes a structured record to `.xlade/metrics.json` on every run
regardless of outcome.

Experiment types currently supported:

| Type             | Execution                                             |
|------------------|-------------------------------------------------------|
| `script-policy`  | `lean.run_script(entry)` via bash                     |
| `lean-policy`    | `lean.run_lake_script("enforceReview", cwd=exp_path)` |

---

## 6. Experiments

Each experiment is a self-contained directory under `experiments/`. The
directory name is the experiment ID used in CLI commands.

```
experiments/exp-002-kernel-boundary/
├── experiment.toml     Metadata — id, type, status, allowed_modes, entry
├── README.md           Research question, hypothesis, enforcement, exit criteria
├── METRICS.md          Evaluation observations
└── policy.md           Policy description (for documentation experiments)
```

`experiment.toml` drives execution:

```toml
id = "exp-002-kernel-boundary"
name = "Kernel Boundary Violation Detection"
type = "script-policy"
status = "active"
allowed_modes = ["experimental"]
lean_toolchain = "leanprover/lean4:stable"
entry = "scripts/experiments/check-kernel.sh"
```

The `entry` field is relative to the repository root for `script-policy`
experiments and relative to the experiment directory for `lean-policy`
experiments.

---

## 7. Runtime State

xLaDe maintains two state locations:

**Global state** — `~/.xlade/`
- `mode` — active mode (`experimental`, `stable`, `onboarding`)

**Project-local state** — `.xlade/` (created by `xlade init`)
- `experiments.lock` — experiment activation state
- `last-run` — ID of the most recently executed experiment
- `metrics.json` — structured run history, appended on every `xlade run`

Deleting `.xlade/` resets project state completely. No Lean files are
affected. See [`RUNTIME_STATE.md`](RUNTIME_STATE.md) for full details.

---

## 8. CI Workflows

| Workflow                | Trigger                       | Purpose                                     |
|-------------------------|-------------------------------|---------------------------------------------|
| `tests.yml`             | push to main, PRs             | Runs full pytest suite                      |
| `kernel-protection.yml` | push to main, PRs             | Kernel protection check                     |
| `mirror.yml`            | push, create, delete          | Syncs to GitLab, Codeberg, Bitbucket, Gitea |
| `sourceforge.yml`       | push to main, manual dispatch | Syncs protected main to Sourceforge         |
| `ci.yml`                | push to main, PRs             | CI workflow                                 |
| `cd.yml`                | push with tag                 | CD workflow                                 |
---

## 9. Current Status and Limitations

As of current version, xLaDe is a functional experimental platform. It is not
production software. Specific limitations are documented in
[`LIMITATIONS.md`](../LIMITATIONS.md).

Key facts about the current state:

- EXP-001 executes when Lake is installed, skips cleanly otherwise
- EXP-002 and EXP-003 execute on any machine with bash
- The test suite does not require a Lean installation to run
- No IDE integrations, no GUI, no scheduler

---

## 10. Future Evolution

The architecture is designed to grow incrementally. Planned directions
include a `prover` field in `experiment.toml` to support Coq and Isabelle
alongside Lean, a structured output format for AI tool integration, and
expanded environment reproducibility tooling. See
[`roadmap.md`](roadmap.md) for the detailed release plan.

Growth remains demand-driven. Complexity is added only when a concrete
use case requires it.
