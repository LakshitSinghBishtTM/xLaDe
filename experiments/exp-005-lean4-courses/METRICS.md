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
- Toolchain override required if v4.29.0 not locally available
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
| Build time               | ~650ms (Solutions 321ms + Examples 324ms) |
| Build jobs               | 4                                   |
| Direct dependencies      | none                                |
| Mathlib                  | absent                              |
| Command                  | xlade run exp-005-lean4-courses     |

---

## Open Questions

These are the research questions EXP-005 raises for future runs:

1. Does it build on `v4.29.0` as originally pinned?
2. Does it build on `leanprover/lean4:stable`?
3. At what future version does it first break, if any?
4. Do the Exercises.lean files (with `sorry`) compile cleanly?

Systematic toolchain compatibility testing is planned for v1.8.0.

---

## Limitations

- Only tests compilation, not proof strategy or exercise correctness
- Submodule pinned to a specific commit — upstream changes require
  manual update
- First run used a different toolchain than the project pins
- Requires full Lean toolchain — skips cleanly without Lake