# xLaDe Scripts

This directory contains **auxiliary scripts** used to orchestrate Lean-related workflows across the xLaDe repository.
Scripts operate at the **repository and ecosystem level**, not at the language or kernel level.
They exist to support policy enforcement, experiment coordination, and structural validation.

---

## What Scripts Are (and Are Not)

### Scripts **ARE**
- Repository-level helpers for:
  - enforcing policies
  - running or coordinating experiments
  - validating structural constraints
- Usable both:
  - locally by contributors
  - automatically in CI environments
- Explicit, inspectable, and replaceable

### Scripts **ARE NOT**
- Modifications to Lean core or kernel
- Changes to Lean semantics or proof behavior
- Required for normal Lean usage outside xLaDe
- Hidden or implicit enforcement mechanisms

Scripts must never alter Lean source code or trusted semantics.

---

## Common Script Responsibilities

Scripts in this directory may perform tasks such as:

- enforcing repository-wide policies
- detecting kernel boundary violations
- validating experiment isolation
- checking repository structure invariants
- coordinating experiment-related workflows

All behavior must be **deterministic and reproducible**.

---

## Policy Enforcement

Some scripts are used to enforce **repository-wide policies**, including but not
limited to:

- kernel immutability
- experiment isolation
- structural invariants

### Enforcement Contexts

Scripts may be invoked:

- manually by contributors
- automatically as part of CI workflows
- during pre-merge or validation checks

Violations detected by scripts may result in:
- warnings (in permissive contexts), or
- failures (in strict or CI contexts)

The enforcement level depends on the active mode and CI configuration.

---

## Design Constraints

All scripts must adhere to the following constraints:

- **Non-invasive**  
  Scripts must not modify Lean kernel sources or semantics.

- **Transparent**  
  Script behavior should be clear from inspection.

- **Reversible**  
  Removing a script or CI hook must disable enforcement without side effects.

These constraints reflect xLaDe’s research-first and safety-oriented design.

---

## Summary

xLaDe scripts provide a **lightweight enforcement and orchestration layer** around Lean usage.

They:
- support disciplined ecosystem experimentation,
- protect architectural boundaries,
- and integrate cleanly with CI workflows,

while keeping Lean’s trusted core untouched.
