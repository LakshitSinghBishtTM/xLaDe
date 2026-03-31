-- Simple pattern matching examples

def isZero (n : Nat) : Bool :=
  match n with
  | 0 => true
  | _ => false

def predSafe (n : Nat) : Nat :=
  match n with
  | 0 => 0
  | k + 1 => k

#eval isZero 0
#eval isZero 7

#eval predSafe 0
#eval predSafe 5