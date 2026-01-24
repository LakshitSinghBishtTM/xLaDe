# Kernel Protection Policy

The Lean kernel and core sources are treated as immutable within xLaDe.

## Policy
- The `lean-core/` submodule must not be modified directly.
- All ecosystem experiments must operate outside the kernel.
- Structural, workflow, and tooling experiments are permitted.

## Rationale
This policy ensures:
- semantic stability
- reproducibility
- compatibility with upstream Lean

## Enforcement
This policy is enforced by repository scripts and CI checks.
Violations cause build or merge failure.
