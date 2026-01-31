# EXP-001: Enforced Proof Review

## Research Question

Can a Lean repository enforce **proof review conventions** without modifying the Lean kernel or relying on IDE plugins?

---

## Hypothesis

A **lightweight, build-time policy** can enforce proof review discipline while remaining:

- non-invasive,
- reversible,
- and compatible with upstream Lean.

---

## Motivation

Large Lean codebases often rely on informal social conventions for proof review. This experiment investigates whether **explicit, enforceable conventions** can be introduced at the ecosystem level without:

- altering Lean semantics,
- requiring editor-specific tooling,
- or fragmenting workflows.

---

## Enforcement Mechanism

This experiment enforces review discipline using:

- **Lean-based policy checks**
- **Build-time enforcement**

### Enforcement Behavior

- Proofs that do not satisfy the review convention cause a **build failure**
- Proofs that satisfy the convention pass **without modification to Lean core**
- Enforcement is deterministic and reproducible

No IDE plugins or patched toolchains are required.

---

## Success Criteria

The experiment is considered successful if:

- Unreviewed proofs reliably cause build failure
- Reviewed proofs pass without kernel modification
- Enforcement remains lightweight and understandable
- Contributors can disable enforcement cleanly

---

## Scope

This experiment applies only to:

- proofs within the experiment’s declared scope
- repositories where the experiment is explicitly enabled

It does **not** affect:
- Lean kernel behavior
- elaboration or type checking semantics
- external repositories

---

## Reversibility

This experiment is fully reversible.

To disable enforcement:
- remove the experiment-specific enforcement call from its `lakefile`

No Lean kernel code, compiler behavior, or upstream sources are modified.

Disabling the experiment restores baseline Lean behavior immediately.

---

## Lifecycle Status

**Status:** Active

This experiment is currently under evaluation and subject to revision or retirement based on observed impact and feedback.

---

## Exit Criteria

The experiment will be evaluated according to the following outcomes:

- **Promotion**  
  If the policy proves useful and low-friction, it may be generalized into a reusable policy or tooling pattern.

- **Abandonment**  
  If enforcement causes undue friction or limited value, the experiment will be archived and preserved for historical reference.

---

## Mode Integration

This experiment is enabled **only** in Experimental Mode.

| Mode           | Status   |
|----------------|----------|
| Onboarding     | Disabled |
| Stable         | Disabled |
| Experimental   | Enabled  |

Mode selection controls whether the experiment is active; it does not affect Lean semantics.

---

## Relationship to Kernel Protection

This experiment complies fully with the **Kernel Protection Policy**:

- ❌ No kernel modification
- ❌ No semantic changes
- ❌ No patched toolchains
- ✅ Ecosystem-level enforcement only

All observed effects are attributable to policy enforcement, not language modification.

---

## Summary

EXP-001 evaluates whether **proof review discipline** can be enforced as an ecosystem policy rather than a social convention.

It provides a concrete test case for xLaDe’s core claim that meaningful workflow constraints can be introduced *around* Lean without touching its trusted core.
