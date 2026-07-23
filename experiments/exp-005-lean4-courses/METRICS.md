# Metrics — EXP-005: Lean4 Courses

## Enforcement Strength

- Script-based via `lake build`
- Pass/fail determined by exit code
- No semantic analysis beyond Lean type checking
- 33 targets compiled

## Scope

- External project only (`lean4-courses/` submodule)
- No impact on xLaDe core or Lean kernel
- No upstream project modifications

## Friction Introduced

- Requires Lake installed via elan
- Submodule must be populated
- No friction on xLaDe core workflows

## Reversibility

- Fully reversible — remove experiment directory and submodule reference
- No persistent state outside `.xlade/metrics.json`

---

## First Run — 2026-06-08

| Field                    | Value                               |
|--------------------------|-------------------------------------|
| Status                   | success                             |
| Timestamp                | 2026-06-08 16:51:50                 |
| Toolchain used           | leanprover/lean4:v4.30.0            |
| Toolchain pinned by repo | leanprover/lean4:v4.29.0            |
| Toolchain mismatch       | yes — minor version                 |
| Build jobs               | 4                                   |
| Direct dependencies      | none                                |
| Mathlib                  | absent                              |
| Command                  | xlade run exp-005-lean4-courses     |

---

## Successful Run

(venv) [ajay@mac xLaDe]$ xlade run exp-005-lean4-courses

  Running experiment:  exp-005-lean4-courses
  Mode:                experimental
  Toolchain:           leanprover/lean4:v4.29.0
  Timestamp:           2026-07-23 08:22:31
  ----------------------------------------------------------------------------------------------------
  xLaDe EXP-005: Lean4 Courses
  ----------------------------------------------------------------------------------------------------
  [info]   Project: experiments/exp-005-lean4-courses/lean4-courses
  [info]   Running: lake build
  ----------------------------------------------------------------------------------------------------
  ℹ [2/4] Built Examples (247ms)
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
  ℹ [3/4] Built Solutions (335ms)
  info: 0000-startup/Solutions.lean:17:0: rfl : double 5 = double 5
  info: 0000-startup/Solutions.lean:29:0: true
  info: 0000-startup/Solutions.lean:30:0: false
  info: 0000-startup/Solutions.lean:42:0: 1024
  info: 0000-startup/Solutions.lean:48:0: "olleh"
  info: 0000-startup/Solutions.lean:57:0: 55
  Build completed successfully (4 jobs).
  ----------------------------------------------------------------------------------------------------
  [pass]   lake build succeeded. 32 modules compiled.
  ----------------------------------------------------------------------------------------------------
  Status: success

## Open Questions

These are the research questions EXP-005 raises for future runs:

1. At what future version does it first break, if any?
2. Do the Exercises.lean files (with `sorry`) compile cleanly?

---

## Limitations

- Only tests compilation, not proof strategy or exercise correctness
- Requires full Lean toolchain — skips cleanly without Lake