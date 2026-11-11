# EXP-002: Kernel Boundary Violation Detection

> **Deprecated.** The `lean-core` submodule was removed from xLaDe, so this experiment no longer checks anything.
> Running it only prints a deprecation notice. The original check is kept, commented out, in
> `scripts/experiments/check-kernel.sh` for historical reference.

## Question
Can xLaDe automatically detect violations of its kernel
non-modification policy?

## Hypothesis
Repository-level checks can enforce architectural boundaries
without modifying Lean itself.

## Enforcement Mechanism
- Script-based detection of `lean-core` revision changes and local edits
- Fails when it cannot verify a Git baseline

## Scope
Applies to all experiments and contributions.

## Mode Integration
Enabled only in Experimental Mode.

## Status
abandoned (deprecated)
