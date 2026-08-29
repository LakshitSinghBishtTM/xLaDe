# Getting Started with xLaDe

This document walks you through your first xLaDe session from scratch.
Every command is explained. No prior xLaDe knowledge required.

For installation, see [`INSTALL.md`](../../docs/INSTALL.md) first.

---

## Step 1 — Check Your Environment

Before anything else, run the diagnostics:

```sh
xlade doctor
```

This checks for elan, lake, lean-core, lean-toolchain, and workspace
state. Every failing check prints the exact command to fix it. Fix
everything showing `[error]` before continuing.

A fully working environment looks like:
elan              [ok]     found
lake              [ok]     found
lean-core         [ok]     submodule present
lean-toolchain    [ok]     present  (leanprover/lean4:stable)
workspace         [warn]   not initialised
Run: xlade init

The workspace warning is expected because you haven't initialised yet.

---

## Step 2 — Initialise the Workspace

```sh
xlade init
```

This creates a `.xlade/` directory in the current folder containing:
- `experiments.lock` — tracks experiment state
- `last-run` — records the most recently run experiment
- `metrics.json` — created on first run, records all run history

Safe to run multiple times. If already initialised, it says so and
exits cleanly.

---

## Step 3 — Set a Mode

```sh
xlade mode experimental
```

Modes control which experiments are enabled and how strictly policies
are enforced. For research and development, use `experimental`. The
mode is stored globally in `~/.xlade/mode`.

---

## Step 4 — See What's Available

```sh
xlade list experiments
```

Shows every experiment in the `experiments/` directory with its status,
type, and allowed modes. The directory name is the ID you pass to
`xlade run`.

---

## Step 5 — Run Your First Experiment

Start with EXP-002. It has no Lean dependency and runs on any machine
with bash:

```sh
xlade run exp-002-kernel-boundary
```

This checks whether `lean-core/` has been modified. On a clean clone
it always passes. It demonstrates the core architectural constraint:
the Lean kernel is immutable.

---

## Step 6 — Run a Real External Project

```sh
xlade run exp-005-lean4-courses
```

This runs `lake build` inside a 32-module Lean 4 course repository
that has no knowledge of xLaDe. Watch Lean compile real code. The
result is recorded automatically.

---

## Step 7 — Review Results

```sh
xlade status
```

Shows workspace state, current mode, last run, and a summary of all
runs with success and failure counts.

```sh
xlade metrics
```

Shows the full run history as a table. Every entry has an experiment
ID, mode, timestamp, and status. This is stored in
`.xlade/metrics.json` and survives across sessions.

---

## Step 8 — Quick Structural Check

```sh
xlade check
```

Verifies the workspace is initialised and the `experiments/` directory
exists. Useful after cloning or before running experiments.

---

## What You Just Did

You ran a complete xLaDe session:
- Diagnosed the environment
- Initialised a workspace
- Selected a mode
- Discovered experiments
- Ran a kernel boundary check
- Built a real external Lean 4 project
- Reviewed a structured audit trail

All of this without touching the Lean kernel, without modifying any
external project, and without any hidden state.

---

## Next Steps

- Read [`docs/CLI_DEMO.md`](../../docs/CLI_DEMO.md) for the full
  command reference
- Read [`docs/WHY_xLaDe.md`](../../docs/WHY_xLaDe.md) for the
  research motivation
- Read [`experiments/README.md`](../../experiments/README.md) to
  understand the experiment framework
- Open an issue if you want to propose a new experiment