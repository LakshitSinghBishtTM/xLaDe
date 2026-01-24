# Metrics — EXP-002: Kernel Boundary Violation Detection

## Enforcement Strength
- Policy enforced via repository scripts and CI
- Kernel modifications are automatically rejected

## Scope
- Applies globally to the repository
- Independent of Lean build configuration

## Friction Introduced
- No impact on normal development
- Only affects attempts to modify `lean-core/`

## Reversibility
- Enforcement can be disabled by removing the CI check
- No code changes required

## Observed Outcome (Initial)
- Kernel boundary violations are detectable at commit time
- Architectural boundaries are made explicit and enforceable

## Limitations
- Relies on repository structure consistency
- Does not prevent indirect semantic influence
