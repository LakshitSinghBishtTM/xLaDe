# xLaDe Policies

Policies define constraints and rules governing the xLaDe repository.

Policies may be enforced by:
- scripts
- CI checks
- Lean-based validation

Policies exist to protect kernel integrity, ensure reproducibility,
and support disciplined experimentation.

## Automated Enforcement

Selected policies are enforced automatically via CI workflows
under `.github/workflows/`.

Violations cause pull requests or pushes to fail.
