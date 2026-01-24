import Lake
open Lake DSL

script enforceReview do
  IO.println "xLaDe: enforcing proof review policy"
  requireReviewed "Proofs/Reviewed.lean"
