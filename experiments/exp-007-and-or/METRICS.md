# Metrics — EXP-7: AND/OR Proof Smoke Test

## Enforcement Strength

- Script-based via `lake env lean <file>`, run independently per file
- Pass/fail determined by exit code, per file, then combined (both must
  pass)
- No semantic analysis beyond Lean's type checker

## Scope

- Two specific files only, in a self-contained project
- No impact on xLaDe core or Lean kernel
- No external project involved

## Friction Introduced

- Requires Lake installed via elan (same as every other experiment)
- Requires `lake exe cache get` to succeed once (Mathlib dependency,
  same category of friction as EXP-006, but a much smaller project on
  top of it)
- No submodule to populate -- this is the lowest-friction experiment so
  far to set up, since the project already exists locally

## Reversibility

- Fully reversible -- remove the experiment directory
- No persistent state outside `.xlade/metrics.json`

---

## Manual Verification (outside xLaDe)

Before this experiment existed: `lake env lean true_statement.lean` and
`lake env lean false_statement.lean`, run directly from the project
directory. Both exited cleanly, no errors.

## First Successful Run

(venv) [ajay@mac xLaDe]$ xlade run exp-007-and-or

  Running experiment:  exp-007-and-or
  Mode:                experimental
  Toolchain:           leanprover/lean4:v4.32.2
  Timestamp:           2026-08-07 07:03:35
  ----------------------------------------------------------------------------------------------------
  xLaDe EXP-7: And OR Proof
  ----------------------------------------------------------------------------------------------------
  [info]   Project: experiments/exp-007-and-or/proof
  Current branch: HEAD
  Using cache from origin: (some leanprover-community/mathlib4)
  No files to download
  Already decompressed 8639 file(s)
  ----------------------------------------------------------------------------------------------------
  -- true_statement.lean --
    
  [pass]  true_statement.lean
  -- false_statement.lean --
    
  [pass]  false_statement.lean
  ----------------------------------------------------------------------------------------------------
  [pass]   both files type-checked.
  ----------------------------------------------------------------------------------------------------
  Status: success

---
