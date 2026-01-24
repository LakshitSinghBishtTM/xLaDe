# xLaDe Scripts

This directory contains shell scripts that orchestrate Lean usage
across the xLaDe repository.

Scripts may:
- enforce repository policies
- run experiments
- validate structural constraints

Scripts must not modify the Lean kernel or source semantics.

## Policy Enforcement

Scripts in this directory may enforce repository-wide policies,
such as kernel immutability and experiment isolation.

These checks are intended to be used locally or in CI.
****
