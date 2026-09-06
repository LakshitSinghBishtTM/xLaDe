# End-to-End Trace

This document is a **narrative execution trace** of a complete xLaDe session
from a fresh clone to running all three active experiments and reviewing results.

This is not a tutorial. It shows exactly what happens at each step — commands,
output, and state changes — so you know what to expect before you run anything.

For installation help, see [`INSTALL.md`](INSTALL.md).
For a command reference, see [`CLI_DEMO.md`](CLI_DEMO.md).

---

## Scenario

A researcher wants to evaluate xLaDe's three active experiments:

- **exp-001-proof-review** — Enforced Proof Review (requires Lake)
- **exp-002-kernel-boundary** — Kernel Boundary Violation Detection
- **exp-003-doc-coverage** — Documentation Coverage Check

The goal is to run all three, understand what each does, and inspect the
results. The machine has Python 3.12 and git, but Lean is not yet installed.

---

## Step 1 — Clone the Repository

```sh
git clone --recurse-submodules https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
```

The `--recurse-submodules` flag initialises `lean-core/` automatically.
Without it, `lean-core/` will be an empty directory and `xlade doctor`
will report it as missing.

---

## Step 2 — Install the CLI

```sh
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

After this, `xlade` is available as a command directly — no need to use
`./bin/xlade`.

---

## Step 3 — Check the Environment

```sh
xlade doctor
```

Output on a machine without Lean installed:

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
  workspace         [warn]   not initialised
                             Run: xlade init
  ----------------------------------------------------------------------------------------------------
  3 issues found. Fix above and re-run xlade doctor.
```

The researcher notes that exp-001-proof-review will be skipped without Lake,
but exp-002-kernel-boundary and exp-003-doc-coverage are script-based and
will run fine. They proceed.

---

## Step 4 — Initialise the Workspace

```sh
xlade init
```

```
  Workspace initialised.

  Created  .xlade/experiments.lock
  Created  .xlade/last-run

  Next:  xlade mode experimental
```

This creates `.xlade/` in the current directory. No Lean files are touched.

Running it again is safe:

```sh
xlade init
```

```
  [warn]  Workspace already initialised in this directory.
          Location: .xlade/
```

---

## Step 5 — Set the Mode

```sh
xlade mode experimental
```

```
  Mode set: experimental
  ----------------------------------------------------------------------------------------------------
  1. Experiments enabled
  2. Policies emit warnings
  3. No stability guarantees
  4. Intended for researchers and contributors
```

This writes `experimental` to `~/.xlade/mode`. Experiments with
`allowed_modes = ["experimental"]` will now be eligible to run.

---

## Step 6 — Discover Experiments

```sh
xlade list experiments
```

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

All three are active and allowed in experimental mode. The experiment name
shown is the directory name — this is what you pass to `xlade run`.

---

## Step 7 — Run exp-002-kernel-boundary

Starting with exp-002 since it has no Lean dependency.

```sh
xlade run exp-002-kernel-boundary
```

```
  Running experiment: exp-002-kernel-boundary
  Mode:      experimental
  Toolchain: leanprover/lean4:stable
  Timestamp: 2026-06-06 14:10:03
  ----------------------------------------------------------------------------------------------------
  [ok]     Kernel untouched.
  ----------------------------------------------------------------------------------------------------
  Status: success
```

exp-002-kernel-boundary runs `scripts/experiments/check-kernel.sh`, which checks whether
any files under `lean-core/` have been modified relative to `origin/main`. On
a clean clone, nothing is modified, so it passes.

---

## Step 8 — Run exp-003-doc-coverage

```sh
xlade run exp-003-doc-coverage
```

```
  Running experiment: exp-003-doc-coverage
  Mode:      experimental
  Toolchain: leanprover/lean4:stable
  Timestamp: 2026-06-06 14:10:41
  ----------------------------------------------------------------------------------------------------
  xLaDe Doc Coverage Check
  -------------------------
  [ok]     experiment: experiments/exp-001-proof-review/
  [ok]     experiment: experiments/exp-002-kernel-boundary/
  [ok]     experiment: experiments/exp-003-doc-coverage/
  [ok]     mode: modes/experimental/
  [ok]     mode: modes/onboarding/
  [ok]     mode: modes/stable/
  [ok]     policies/ has 4 documentation file(s)
  -------------------------
  [pass]   All documentation checks passed.
  ----------------------------------------------------------------------------------------------------
  Status: success
```

exp-003-doc-coverage runs `scripts/experiments/check-doc-coverage.sh`, which verifies
that every experiment and mode directory has a `README.md`, and that
`policies/` contains at least one `.md` file.

---

## Step 9 — Run exp-001-proof-review

exp-001-proof-review requires Lake. On this machine it is not installed.

```sh
xlade run exp-001-proof-review
```

```
  Running experiment: exp-001-proof-review
  Mode:      experimental
  Toolchain: leanprover/lean4:stable
  Timestamp: 2026-06-06 14:11:15
  ----------------------------------------------------------------------------------------------------
  [skip]  lake not found -- cannot run lean-policy experiment.
          Install Lean 4 and Lake via elan:
          curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
  ----------------------------------------------------------------------------------------------------
  Status: skipped
```

The experiment is recorded as `skipped` — not failed. The distinction
matters: `skipped` means the environment prevented execution, not that
the experiment logic failed. Once Lake is installed, re-running
exp-001-proof-review will execute the proof review policy for real.

---

## Step 10 — Review Status

```sh
xlade status
```

```
  xLaDe Status
  ----------------------------------------------------------------------------------------------------
  Workspace   initialised
  Mode        experimental
  Last run    exp-001-proof-review
  ----------------------------------------------------------------------------------------------------
  Runs        3  (success: 2, skipped: 1)

  Recent:
    exp-001-proof-review                    2026-06-06 14:11:15  skipped
    exp-003-doc-coverage                    2026-06-06 14:10:41  success
    exp-002-kernel-boundary                 2026-06-06 14:10:03  success
```

---

## Step 11 — Review Metrics

```sh
xlade metrics
```

```
  xLaDe Metrics  (3 run(s))
  ----------------------------------------------------------------------------------------------------
  Experiment               Mode          Timestamp            Status
  ----------------------------------------------------------------------------------------------------
  exp-002-kernel-boundary  experimental  2026-06-06 14:10:03  success
  exp-003-doc-coverage     experimental  2026-06-06 14:10:41  success
  exp-001-proof-review     experimental  2026-06-06 14:11:15  skipped
```

The full run history is stored in `.xlade/metrics.json` and survives
across sessions.

---

## Step 12 — Install Lean and Re-run exp-001-proof-review

The researcher installs elan and the Lean toolchain:

```sh
curl https://elan.lean-lang.org/elan-init.sh -sSf | sh
source ~/.elan/env
elan toolchain install leanprover/lean4:stable
```

Verify Lake is now available:

```sh
xlade doctor
```

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

Re-run exp-001-proof-review:

```sh
xlade run exp-001-proof-review
```

```
  Running experiment: exp-001-proof-review
  Mode:      experimental
  Toolchain: leanprover/lean4:stable
  Timestamp: 2026-06-06 15:30:22
  ----------------------------------------------------------------------------------------------------
  Executing Lake script: enforceReview
  xLaDe: enforcing proof review policy
  [ok]     Proofs/Reviewed.lean is reviewed
  ----------------------------------------------------------------------------------------------------
  Status: success
```

exp-001-proof-review runs `lake script run enforceReview` inside the
experiment directory. It reads `Proofs/Reviewed.lean`, confirms the
`@reviewed` marker is present, and passes.

---

## Step 13 — Reset the Workspace

To reset all xLaDe project-local state:

```sh
rm -rf .xlade
```

This removes the workspace directory, run history, and metrics. It does
not touch Lean source files, the kernel, or any experiment code.

To reinitialise from scratch:

```sh
xlade init
```

> **Note:** `rm -rf .xlade` only removes the xLaDe state directory.
> Do not confuse it with `rm -rf /` — that removes the entire filesystem,
> the OS, and everything else. One is a cleanup step. The other is a
> disaster. They look similar. They are not.

---

## Summary

| Step                      | Command                               | Outcome                                    |
|---------------------------|---------------------------------------|--------------------------------------------|
| Environment check         | `xlade doctor`                        | 3 issues identified, actionable hints given |
| Workspace setup           | `xlade init`                          | `.xlade/` created                          |
| Mode selection            | `xlade mode experimental`             | Experiments enabled                        |
| Discovery                 | `xlade list experiments`              | 3 experiments found                        |
| exp-002-kernel-boundary   | `xlade run exp-002-kernel-boundary`   | [ok] success — kernel boundary intact      |
| exp-003-doc-coverage      | `xlade run exp-003-doc-coverage`      | [pass] success — all docs present          |
| exp-001-proof-review      | `xlade run exp-001-proof-review`      | [skip] skipped — lake not found            |
| exp-001 (with Lake)       | `xlade run exp-001-proof-review`      | [ok] success — proof review enforced       |
| Results                   | `xlade status` / `xlade metrics`      | Full run history visible                   |
| Cleanup                   | `rm -rf .xlade`                       | State reset, Lean untouched                |

xLaDe orchestrates experiments, records state explicitly, and remains
fully reversible at every step.