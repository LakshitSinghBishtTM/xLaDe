# xLaDe Runtime State

This document describes how xLaDe manages runtime state across user
environments and individual projects.

xLaDe separates state into **global state** (user-level mode selection)
and **project-local state** (workspace, experiment history, and metrics).
This separation is intentional — it supports reproducibility, isolation,
and clarity across multiple projects on the same machine.

No runtime state affects Lean's kernel, semantics, or proof behaviour.

---

## Design Principles

xLaDe runtime state is designed to be:

- **Explicit** — all state is stored in visible, human-readable files
- **Non-invasive** — no Lean source files or build outputs are modified
- **Minimal** — only what is needed for orchestration is recorded
- **Recoverable** — deleting state resets behaviour without breaking anything

---

## Global State — `~/.xlade/`

Global state lives in the user's home directory and applies across all
xLaDe projects on the machine.

```
~/.xlade/
└── mode
```

### `mode`

Stores the currently active xLaDe mode. Set via:

```sh
xlade mode experimental
xlade mode stable
xlade mode onboarding
```

Valid values: `experimental`, `stable`, `onboarding`.

This file controls which experiments are eligible to run. Experiments
declare their `allowed_modes` in `experiment.toml` — if the current mode
is not in that list, `xlade run` refuses to execute the experiment.

This file does not alter Lean itself in any way.

---

## Project-Local State — `.xlade/`

Project-local state lives inside the project directory and is created by:

```sh
xlade init
```

```
.xlade/
├── experiments.lock
├── last-run
└── metrics.json
```

### `experiments.lock`

Records experiment activation state. Human-readable and manually
inspectable. Supports reproducibility by tracking which experiments
are active in this workspace.

### `last-run`

Contains the ID of the most recently executed experiment. Written by
`xlade run` on every execution. Read by `xlade status` to display the
last run. Contains `none` on a freshly initialised workspace.

### `metrics.json`

The primary runtime artifact. A structured JSON array appended on every
`xlade run` call, regardless of whether the experiment succeeded, failed,
or was skipped.

Each record contains:

```json
{
  "experiment_id": "exp-002-kernel-boundary",
  "experiment_name": "Kernel Boundary Violation Detection",
  "type": "script-policy",
  "mode": "experimental",
  "lean_toolchain": "leanprover/lean4:stable",
  "timestamp": "2026-05-26 14:10:03",
  "status": "success"
}
```

Status values:

| Value       | Meaning                                               |
|-------------|-------------------------------------------------------|
| `success`   | Experiment ran and passed                             |
| `failed`    | Experiment ran and failed                             |
| `skipped`   | Environment prevented execution (e.g. lake not found) |
| `simulated` | No entry point defined, execution was conceptual      |

`metrics.json` is read by `xlade status` (summary view) and
`xlade metrics` (full history table). If the file is missing, both
commands report no runs recorded. If the file is corrupted, both
commands report it clearly and exit cleanly without crashing.

---

## Lifecycle and Cleanup

**Reset project-local state:**

```sh
rm -rf .xlade
xlade init
```

**Reset global state:**

```sh
rm -rf ~/.xlade
```

Neither operation affects:
- Lean source files
- proof artifacts
- build outputs
- experiment definitions

This makes experimentation fully safe and reversible.

---

## State and Reproducibility

The combination of `lean_toolchain` recorded in each `metrics.json` entry
and the `experiment.toml` metadata for each experiment forms the foundation
of xLaDe's reproducibility model. Every run is associated with the exact
environment it executed in — mode, toolchain version, and timestamp.

This is the first step toward the longer-term goal of reconstructing
historical experiment environments on demand. See
[`REPRODUCIBILITY_AND_COMPATIBILITY.md`](REPRODUCIBILITY_AND_COMPATIBILITY.md)
for the full plan.

---

## Summary

| Location                  | Contents                    | Created by   |
|---------------------------|-----------------------------|--------------|
| `~/.xlade/mode`           | Active mode                 | `xlade mode` |
| `.xlade/experiments.lock` | Experiment activation state | `xlade init` |
| `.xlade/last-run`         | Last executed experiment ID | `xlade run`  |
| `.xlade/metrics.json`     | Full structured run history | `xlade run`  |