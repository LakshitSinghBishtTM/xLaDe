# EXP-004: Project Proof 1

## Research Question

Can xLaDe wrap and execute an external Lean 4 project as an experiment,
using the project as a git submodule and recording full environment metadata?

---

## Hypothesis

An external Lean 4 repository can be integrated into xLaDe as a submodule,
executed via `lake build`, and produce reproducible results with full
metadata recorded — without modifying the project source or the Lean kernel.

---

## Project

**Repository:** https://github.com/LakshitSinghBishtTM/exp-004-project-proof-1

**Submodule path:** `experiments/exp-004-project-proof-1/exp-004-project-proof-1/`

A minimal Lean 4 proof repository containing basic arithmetic and logic
theorems. No external dependencies beyond the Lean toolchain.

**Proofs included:**
- `add_comm_test` — commutativity of addition
- `add_assoc_test` — associativity of addition
- `zero_add_test` — zero as left identity
- `imp_trans_test` — transitivity of implication
- `and_comm_test` — commutativity of conjunction

---

## Enforcement Mechanism

- Script-based: `scripts/experiments/run-exp-004.sh`
- Runs `lake build` inside the project submodule directory
- Exit code determines pass/fail

---

## Success Criteria

`compilation` — `lake build` exits 0 with all proofs checked.

Failure is any non-zero exit from `lake build`.

---

## Scope

- `experiments/exp-004-project-proof-1/project/` — the external project
- No modifications to xLaDe core, Lean kernel, or project source

---

## Non-Goals

- Does not test proof correctness beyond what Lean's type checker enforces
- Does not test performance or elaboration time
- Does not modify the external project in any way

---

## Reversibility

Remove the experiment directory and submodule entry from `.gitmodules`.
No xLaDe core files are affected.

---

## Exit Criteria

- **Promoted** if xLaDe can reliably build and record metadata for external
  projects, informing the reproducibility framework
- **Abandoned** if the submodule approach proves unworkable for external projects

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
