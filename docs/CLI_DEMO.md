# xLaDe CLI Demo

xLaDe is used entirely through the `xlade` command-line interface. This
document covers every command, what it does, and what to expect from it.

For installation instructions, see [`INSTALL.md`](../INSTALL.md).  
For a narrative walkthrough, see [`END_TO_END_TRACE.md`](END_TO_END_TRACE.md).

---

## What the CLI Is (and Is Not)

The `xlade` CLI is an **ecosystem orchestration tool**. It manages workspace
state, selects modes, discovers experiments, and executes them. It does not
replace `lean` or `lake` — it coordinates them.

| The CLI IS                                  | The CLI IS NOT                         |
|---------------------------------------------|----------------------------------------|
| An orchestration layer for experiments      | A replacement for `lean` or `lake`     |
| A workspace and state manager               | A proof executor or elaboration engine |
| A stable interface over evolving components | A production-ready build system        |
| A diagnostics tool for your environment     | A GUI or IDE integration               |

---

## Prerequisites

Before using xLaDe, ensure your environment is set up correctly:

```sh
xlade doctor
```

All items should show `[ok]` before running experiments. See [`INSTALL.md`](../INSTALL.md)
for setup instructions if anything is missing.

---

## Command Reference

### `xlade init`

Initialises an xLaDe workspace in the current directory.

```sh
xlade init
```

Creates a `.xlade/` directory containing:

- `experiments.lock` — tracks experiment state
- `last-run` — records the most recently executed experiment
- `metrics.json` — written on every experiment run (created on first run)

Safe to run multiple times. If the workspace already exists, it reports
so and exits cleanly. Does not modify any Lean source files or dependencies.

**Example output (first run):**

```
  Workspace initialised.

  Created  .xlade/experiments.lock
  Created  .xlade/last-run

  Next:  xlade mode experimental
```

**Example output (already initialised):**

```
  [warn]  Workspace already initialised in this directory.
          Location: .xlade/
```

---

### `xlade mode`

Sets the active ecosystem mode. Modes control which experiments are enabled
and how strictly policies are enforced.

```sh
xlade mode experimental
xlade mode stable
xlade mode onboarding
```

The selected mode is stored in `~/.xlade/mode` and applies globally across
all xLaDe projects on the machine.

| Mode           | Experiments | Enforcement | Intended for              |
|----------------|-------------|-------------|---------------------------|
| `experimental` | Enabled     | Warnings    | Researchers, contributors |
| `stable`       | Disabled    | Strict      | Validation, long-term use |
| `onboarding`   | Disabled    | Minimal     | New users, learning       |

Experiments marked `allowed_modes = ["experimental"]` will only run when
experimental mode is active.

**Example output:**

```
  Mode set: experimental
  ----------------------------------------------------------------------------------------------------
  1. Experiments enabled
  2. Policies emit warnings
  3. No stability guarantees
  4. Intended for researchers and contributors
```

---

### `xlade list experiments`

Discovers and lists all available experiments in the `experiments/` directory.

```sh
xlade list experiments
```

Reads each experiment's `experiment.toml` and displays its directory name
(which is the ID used with `xlade run`), status, type, and allowed modes.

**Example output:**

```
  Experiments  (7 found)
  ----------------------------------------------------------------------------------------------------
  Experiment               Status    Type              Modes
  ----------------------------------------------------------------------------------------------------
  exp-001-proof-review     active    lean-policy       experimental
  exp-002-kernel-boundary  active    script-policy     experimental
  exp-003-doc-coverage     active    script-policy     experimental

  Run with: xlade run <experiment-id>
```

Returns a clear message if the `experiments/` directory is missing or
contains no valid experiments.

---

### `xlade run`

Runs an experiment by ID. The ID is the directory name under `experiments/`.

```sh
xlade run exp-002-kernel-boundary
```

Before executing, `xlade run` validates:

- The workspace is initialised (`.xlade/` exists)
- The experiment directory and `experiment.toml` exist
- The current mode is in the experiment's `allowed_modes`

On success it dispatches based on the experiment type:

- `script-policy` — executes the entry shell script via bash
- `lean-policy` — invokes `lake script run` in the experiment directory
  (requires Lake; reports `skipped` with install instructions if not found)

After every run, regardless of outcome, xlade writes a structured record
to `.xlade/metrics.json` with the experiment ID, mode, timestamp, and
status (`success`, `failed`, `skipped`, or `simulated`).

**Example output (exp-002-kernel-boundary, success):**

```
  Running experiment: exp-002-kernel-boundary
  Mode:      experimental
  Toolchain: leanprover/lean4:stable
  Timestamp: 2026-06-06 14:22:05
  ----------------------------------------------------------------------------------------------------
  [ok]     Kernel untouched.
  ----------------------------------------------------------------------------------------------------
  Status: success
```

**Example output (exp-001-proof-review, lake not installed):**

```
  Running experiment: exp-001-proof-review
  Mode:      experimental
  Toolchain: leanprover/lean4:stable
  Timestamp: 2026-06-06 14:22:10
  ----------------------------------------------------------------------------------------------------
  [skip]  lake not found -- cannot run lean-policy experiment.
          Install Lean 4 and Lake via elan:
          curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
  ----------------------------------------------------------------------------------------------------
  Status: skipped
```

---

### `xlade status`

Shows the current workspace state and a summary of past experiment runs.

```sh
xlade status
```

Reads from `~/.xlade/mode` and `.xlade/metrics.json`.

**Example output:**

```
  xLaDe Status
  ----------------------------------------------------------------------------------------------------
  Workspace   initialised
  Mode        experimental
  Last run    exp-002-kernel-boundary
  ----------------------------------------------------------------------------------------------------
  Runs        3  (success: 2, failed: 1)

  Recent:
    exp-002-kernel-boundary                 2026-06-06 14:22:05  success
    exp-003-doc-coverage                    2026-06-06 13:10:42  failed
    exp-002-kernel-boundary                 2026-06-05 09:05:17  success
```

---

### `xlade metrics`

Displays the full run history from `.xlade/metrics.json`.

```sh
xlade metrics
```

**Example output:**

```
  xLaDe Metrics  (3 run(s))
  ----------------------------------------------------------------------------------------------------
  Experiment               Mode          Timestamp            Status
  ----------------------------------------------------------------------------------------------------
  exp-002-kernel-boundary  experimental  2026-06-06 14:22:05  success
  exp-003-doc-coverage     experimental  2026-06-06 13:10:42  failed
  exp-002-kernel-boundary  experimental  2026-06-05 09:05:17  success
```

---

### `xlade check`

Runs a quick structural check of the current project.

```sh
xlade check
```

Verifies that:

- The workspace is initialised
- The `experiments/` directory exists

Reports any issues found. Does not execute experiments or modify state.

**Example output (issues found):**

```
  xLaDe Check
  ----------------------------------------------------------------------------------------------------
  workspace     [error]  not initialised
                         run: xlade init
  experiments   [error]  directory not found
                         expected experiments/ in project root
  ----------------------------------------------------------------------------------------------------
  2 issue(s) found.
```

**Example output (clean):**

```
  xLaDe Check
  ----------------------------------------------------------------------------------------------------
  workspace     [ok]
  experiments   [ok]
  ----------------------------------------------------------------------------------------------------
  All checks passed.
```

---

### `xlade doctor`

Checks the environment for required tools and configuration.

```sh
xlade doctor
```

Checks for:

- **elan** — the Lean version manager
- **lake** — the Lean build tool
- **lean-core submodule** — present and initialised
- **lean-toolchain** — file present with toolchain pinned
- **workspace** — `.xlade/` initialised in current directory

For each missing item, `xlade doctor` prints the exact command needed to
fix it. Ends with a pass/fail summary.

**Example output (all clear):**

```
  xLaDe Doctor
  ----------------------------------------------------------------------------------------------------
  elan              [ok]     found
  lake              [ok]     found
  lean-core         [ok]     submodule present
  lean-toolchain    [ok]     present  (leanprover/lean4:stable)
  workspace         [ok]     initialised
  ----------------------------------------------------------------------------------------------------
  All checks passed.
```

**Example output (issues found):**

```
  xLaDe Doctor
  ----------------------------------------------------------------------------------------------------
  elan              [error]  not found
                             Install: curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
                             Then restart your shell and re-run xlade doctor.
  lake              [error]  not found
                             Install elan first, then:
                             elan toolchain install leanprover/lean4:stable
  lean-core         [error]  submodule empty
                             Run: git submodule update --init --recursive
  lean-toolchain    [ok]     present  (leanprover/lean4:stable)
  workspace         [ok]     initialised
  ----------------------------------------------------------------------------------------------------
  3 issues found. Fix above and re-run xlade doctor.
```

---

## Typical Workflow

A standard session from a fresh clone looks like this:

```sh
# 1. Check the environment first
xlade doctor

# 2. Initialise the workspace
xlade init

# 3. Set the mode
xlade mode experimental

# 4. See what experiments are available
xlade list experiments

# 5. Run an experiment
xlade run exp-002-kernel-boundary

# 6. Review the results
xlade status
xlade metrics
```

---

## Design Philosophy

The xLaDe CLI is designed to be:

- **Explicit** — every state change is visible and recorded
- **Non-invasive** — Lean core is never touched
- **Interface-stable** — commands remain consistent as execution backends evolve
- **Research-honest** — limitations are reported clearly, not hidden

When something cannot run (missing tool, wrong mode, missing file), xLaDe
tells you exactly why and what to do about it. It never silently skips
steps or produces misleading output.