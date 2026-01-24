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
