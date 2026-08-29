# EXP-7: AND/OR Proof Test

`true_statement.lean`'s hypothesis is an `∧` conjunction throughout, 
and `false_statement.lean` disproves a claim that mixes `∨` (hypothesis) 
with `∧` (conclusion) showing "a<c ∨ c<b" does not imply "a<c ∧ c<b".

---

## Hypothesis

Two hand-written Lean/Mathlib proofs, run through xLaDe via the exact
method already verified manually (`lake env lean <file>`), report
success/failure that matches what manual verification already showed:
both pass, cleanly.

---

## Project

**Type:** Self-contained (`lake new proof math`) -- no external
repository, no submodule
**Location:** `experiments/exp-007-and-or/proof/`
**Toolchain:** `leanprover/lean4:v4.32.2`
**Dependencies:** Mathlib

## Enforcement Mechanism

- Script-based: `scripts/experiments/run-exp-007.sh`
- Runs `lake exe cache get` once (Mathlib's prebuilt cache), then
  `lake env lean <file>` on each of the two files independently
- **Not** `lake build`: `lakefile.toml` declares `lean_lib "Proof"`,
  which by Lake's convention expects a root `Proof.lean` or a `Proof/`
  source tree. These two files sit at the project root under their own
  names instead, outside that target -- `lake build` wouldn't
  necessarily exercise them at all. `lake env lean <file>` is exactly
  the method already used to verify both manually, so the entry script
  mirrors that rather than assuming a build path that was never tested.
- Both files must type-check for the experiment to pass; either one
  failing is an overall failure

---

## Success Criteria

`both true_statement.lean and false_statement.lean type-check via lake
env lean` -- both exit 0.

Failure: either file exits non-zero.

---

## Scope

- `experiments/exp-007-and-or/proof/` only
- No modification to xLaDe core, no external project, no Lean kernel
  involvement

---

## Non-Goals

- Does not test anything beyond these two specific files
- Does not exercise the `Proof` lean_lib target or `lake build`
- Does not test proof strategy quality, only that each file type-checks

---

## Reversibility

Fully reversible -- remove the experiment directory. No submodule, no
`.gitmodules` entry, nothing else to clean up.

---

## Mode Integration

| Mode         | Status   |
|--------------|----------|
| Onboarding   | Disabled |
| Stable       | Disabled |
| Experimental | Enabled  |

---

## Status

Active
