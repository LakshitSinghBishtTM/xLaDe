# EXP-001: Enforced Proof Review

## Question
Can a Lean repository enforce proof review conventions without modifying
the Lean kernel or relying on IDE plugins?

## Hypothesis
A lightweight, build-time policy can enforce review discipline while
remaining reversible and non-invasive.

## Enforcement Mechanism
- Lean-based policy checks
- Build failure on violation

## Success Criteria
- Unreviewed proofs cause build failure
- Reviewed proofs pass without modification to Lean core

## Status
active

## Reversibility
This experiment can be disabled by removing the enforcement call
from the experiment-specific lakefile.

No Lean kernel or upstream code is modified.

## Exit Criteria
- If the policy proves useful, it may be generalized.
- If it causes friction, the experiment will be archived.

## Mode Integration

This experiment is enabled only in **Experimental Mode**.

- Onboarding Mode: disabled
- Stable Mode: disabled
- Experimental Mode: enabled
