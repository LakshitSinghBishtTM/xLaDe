import Lake
open Lake DSL

package «exp-001-proof-review» where

script enforceReview do
  IO.println "xLaDe: enforcing proof review policy"
  let path : System.FilePath := "Proofs/Reviewed.lean"
  let contents ← IO.FS.readFile path
  if contents.contains "@reviewed" then
    IO.println s!"[ok]   {path} is reviewed"
    return 0
  else
    IO.eprintln s!"[error]  {path} is missing @reviewed tag"
    return 1