# EXP-002: Kernel Boundary Violation Detection

## Question
Can xLaDe automatically detect violations of its kernel
non-modification policy?

## Hypothesis
Repository-level checks can enforce architectural boundaries
without modifying Lean itself.

## Enforcement Mechanism
- Script-based detection of changes to `lean-core/`

## Scope
Applies to all experiments and contributions.

## Mode Integration
Enabled only in Experimental Mode.

## Status
active
