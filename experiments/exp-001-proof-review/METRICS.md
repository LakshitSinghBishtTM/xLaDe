# Metrics — EXP-001: Enforced Proof Review

## Enforcement Strength
- Policy enforced via Lean code
- Violations cause build failure
- No reliance on IDE plugins

## Scope
- Affects only files within the experiment directory
- No impact on kernel or upstream Lean

## Friction Introduced
- Requires adding a single marker (`@reviewed`)
- No changes to proof content or structure

## Reversibility
- Enforcement can be disabled by removing the experiment-specific
  lakefile or policy invocation
- No persistent state introduced

## Observed Outcome (Initial)
- Unreviewed proofs are reliably detected
- Reviewed proofs compile without modification

## Limitations
- Review marker is syntactic and not semantic
- No notion of reviewer identity or review depth
