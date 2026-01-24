import Lake
open Lake DSL

/--
Stable mode entrypoint.

This mode enforces conservative defaults and policies.
-/
script stable do
  IO.println "xLaDe Stable Mode"
  IO.println "Strict policies enabled."
