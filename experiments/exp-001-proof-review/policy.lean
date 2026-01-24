import Lean

open Lean

def requireReviewed (path : System.FilePath) : IO Unit := do
  let contents ← IO.FS.readFile path
  if contents.contains "@reviewed" then
    IO.println s!"✔ {path} is reviewed"
  else
    throw <| IO.userError s!"✘ {path} is missing @reviewed tag"
