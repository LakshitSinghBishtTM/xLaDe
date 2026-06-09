# xLaDe Demo Session

This is a real terminal session. No editing, no cleanup, no idealised
output. This is what xLaDe looks like when you run it.

Recorded on 2026-06-09. xLaDe v1.6.0. Python 3.14.5. Linux x86_64.

---

## Environment Check

(venv) [ajay@mac xLaDe]$ xlade doctor

  xLaDe Doctor
  ----------------------------------------------------------------------------------------------------
  elan              [ok]     found
  lake              [ok]     found
  lean-core         [error]  submodule not populated
                             Run: git submodule update --init --recursive
  lean-toolchain    [ok]     present  (leanprover/lean4:stable)
  workspace         [ok]     initialised
  ----------------------------------------------------------------------------------------------------
  1 issue found. Fix above and re-run xlade doctor.

## List Experiments

(venv) [ajay@mac xLaDe]$ xlade list experiments

  Experiments  (5 found)
  ----------------------------------------------------------------------------------------------------
  Experiment               Status    Type              Modes
  ----------------------------------------------------------------------------------------------------
  exp-001-proof-review     active    lean-policy       experimental
  exp-002-kernel-boundary  active    script-policy     experimental
  exp-003-doc-coverage     active    script-policy     experimental
  exp-004-project-proof-1  active    script-policy     experimental
  exp-005-lean4-courses    active    script-policy     experimental

  Run with: xlade run <experiment-id>

---

## Running Experiments

(venv) [ajay@mac xLaDe]$ xlade run exp-002-kernel-boundary

  Running experiment:  exp-002-kernel-boundary
  Mode:                experimental
  Toolchain:           leanprover/lean4:stable
  Timestamp:           2026-06-09 07:15:34
  ----------------------------------------------------------------------------------------------------
  [ok]     Kernel untouched.
  ----------------------------------------------------------------------------------------------------
  Status: success

(venv) [ajay@mac xLaDe]$ xlade run exp-005-lean4-courses

  Running experiment:  exp-005-lean4-courses
  Mode:                experimental
  Toolchain:           leanprover/lean4:v4.30.0
  Timestamp:           2026-06-09 07:15:46
  ----------------------------------------------------------------------------------------------------
  xLaDe EXP-005: Lean4 Courses
  ----------------------------------------------------------------------------------------------------
  [info]   Project: experiments/exp-005-lean4-courses/lean4-courses
  [info]   Running: lake build
  ----------------------------------------------------------------------------------------------------
  ℹ [2/4] Replayed Solutions
  info: 0000-startup/Solutions.lean:17:0: rfl : double 5 = double 5
  info: 0000-startup/Solutions.lean:29:0: true
  info: 0000-startup/Solutions.lean:30:0: false
  info: 0000-startup/Solutions.lean:42:0: 1024
  info: 0000-startup/Solutions.lean:48:0: "olleh"
  info: 0000-startup/Solutions.lean:57:0: 55
  ℹ [3/4] Replayed Examples
  info: 0000-startup/Examples.lean:11:0: 42 : Nat
  info: 0000-startup/Examples.lean:12:0: "hello" : String
  info: 0000-startup/Examples.lean:13:0: Bool.true : Bool
  info: 0000-startup/Examples.lean:15:0: 5
  info: 0000-startup/Examples.lean:16:0: "hello world"
  info: 0000-startup/Examples.lean:19:0: "Hello, Lean 4!"
  info: 0000-startup/Examples.lean:24:0: 10
  info: 0000-startup/Examples.lean:57:0: def Course0000Examples.double : Nat → Nat :=
  fun n => 2 * n
  info: 0000-startup/Examples.lean:63:0: 'Course0000Examples.two_eq' does not depend on any axioms
  info: 0000-startup/Examples.lean:76:0: 3628800
  Build completed successfully (4 jobs).
  ----------------------------------------------------------------------------------------------------
  [pass]   lake build succeeded. 32 modules compiled.
  ----------------------------------------------------------------------------------------------------
  Status: success

---

## Status and Metrics

(venv) [ajay@mac xLaDe]$ xlade status

  xLaDe Status
  ----------------------------------------------------------------------------------------------------
  Workspace   initialised
  Mode        experimental
  Last run    exp-005-lean4-courses
  ----------------------------------------------------------------------------------------------------
  Runs        22  (success: 22)

  Recent:
    exp-002-kernel-boundary                 2026-06-08 16:58:07  success
    exp-001-proof-review                    2026-06-08 16:58:11  success
    exp-005-lean4-courses                   2026-06-08 17:27:08  success
    exp-002-kernel-boundary                 2026-06-09 07:15:34  success
    exp-005-lean4-courses                   2026-06-09 07:15:46  success

(venv) [ajay@mac xLaDe]$ xlade metrics

  xLaDe Metrics  (22 run(s))
  ----------------------------------------------------------------------------------------------------
  Experiment               Mode          Timestamp            Status
  ----------------------------------------------------------------------------------------------------
  exp-001-proof-review     experimental  2026-06-08 09:12:00  success
  exp-001-proof-review     experimental  2026-06-08 09:13:42  success
  exp-001-proof-review     experimental  2026-06-08 09:14:21  success
  exp-001-proof-review     experimental  2026-06-08 09:17:29  success
  exp-001-proof-review     experimental  2026-06-08 10:56:48  success
  exp-002-kernel-boundary  experimental  2026-06-08 10:57:24  success
  exp-003-doc-coverage     experimental  2026-06-08 10:57:42  success
  exp-004-project-proof-1  experimental  2026-06-08 10:57:54  success
  exp-001-proof-review     experimental  2026-06-08 10:58:19  success
  exp-001-proof-review     experimental  2026-06-08 10:58:39  success
  exp-002-kernel-boundary  experimental  2026-06-08 10:59:20  success
  exp-003-doc-coverage     experimental  2026-06-08 10:59:31  success
  exp-004-project-proof-1  experimental  2026-06-08 10:59:40  success
  exp-005-lean4-courses    experimental  2026-06-08 16:51:50  success
  exp-004-project-proof-1  experimental  2026-06-08 16:56:26  success
  exp-005-lean4-courses    experimental  2026-06-08 16:56:57  success
  exp-003-doc-coverage     experimental  2026-06-08 16:58:00  success
  exp-002-kernel-boundary  experimental  2026-06-08 16:58:07  success
  exp-001-proof-review     experimental  2026-06-08 16:58:11  success
  exp-005-lean4-courses    experimental  2026-06-08 17:27:08  success
  exp-002-kernel-boundary  experimental  2026-06-09 07:15:34  success
  exp-005-lean4-courses    experimental  2026-06-09 07:15:46  success

---

## What This Shows

Five experiments total. Two of them wrapped external Lean 4 repositories
with no code connection to xLaDe. All runs recorded automatically
in `.xlade/metrics.json` with full environment metadata.

The audit trail is real. The builds are real. The external projects
knew nothing about xLaDe.