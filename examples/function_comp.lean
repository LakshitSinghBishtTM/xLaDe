-- Function composition and simple reasoning

def inc (n : Nat) : Nat := n + 1
def double (n : Nat) : Nat := n * 2

def inc_then_double (n : Nat) : Nat :=
  double (inc n)

#eval inc 3
#eval double 3
#eval inc_then_double 3

theorem inc_nonzero (n : Nat) : inc n ≠ 0 := by
  intro h
  cases n <;> simp [inc] at h