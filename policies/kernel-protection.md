# Kernel Protection Policy

This policy defines the **non-negotiable boundary** between the Lean kernel and all ecosystem-level experimentation conducted within xLaDe.
The Lean kernel and core sources are treated as **immutable infrastructure**.
xLaDe does not modify, extend, or replace Lean’s trusted computing base.

---

## Policy Statement

The following rules apply at all times:

- The `lean-core/` submodule **must not be modified directly**
- All ecosystem experiments **must operate outside the Lean kernel**
- Structural, workflow, documentation, tooling, and policy experiments
  **are permitted**
- No experiment may:
  - alter kernel semantics
  - change type checking or elaboration behavior
  - introduce kernel-level patches

Lean core is included **only as a reference baseline**, not as a target of experimentation.

---

## Rationale

This policy exists to ensure:

- **Semantic Stability**  
  Experimental results must not depend on altered core semantics.

- **Reproducibility**  
  Experiments must be repeatable across environments using standard Lean.

- **Upstream Compatibility**  
  Ideas developed in xLaDe can be discussed or proposed upstream without
  requiring kernel divergence.

By enforcing kernel immutability, xLaDe ensures that all observed effects are
attributable to **ecosystem design choices**, not language modification.

---

## Scope

This policy applies to:

- all experiments
- all modes
- all contributors
- all branches and pull requests

There are **no exceptions** based on mode, experiment status, or contributor role.

---

## Enforcement

This policy is enforced automatically via:

- repository scripts
- CI checks

### Enforcement Behavior
- Direct modifications to `lean-core/` are detected
- Violations cause:
  - build failure, or
  - pull request rejection

Enforcement is **deterministic and reproducible**.

---

## Reversibility

This policy can be disabled **only** by:

- removing the enforcement scripts and CI checks

No Lean source files need to be rewritten to change enforcement behavior.

This reflects xLaDe’s commitment to **reversible governance**, even for strict
policies.

---

## Relationship to Experiments

Kernel protection itself may be treated as an **ecosystem experiment** (e.g. EXP-002).

In such cases:
- the policy remains conceptually stable
- enforcement mechanisms may evolve
- violations remain explicitly detectable

At no point does experimentation permit kernel modification.

---

## Summary

The kernel protection policy establishes a **hard architectural boundary**
within xLaDe.

It ensures that:
- Lean’s trusted core remains untouched,
- ecosystem experimentation remains safe,
- and research conclusions remain valid and transferable.

This policy is foundational to xLaDe’s research-first and non-invasive design
philosophy.
