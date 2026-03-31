-- Combination of definitions, theorems, and evaluation

def double (n : Nat) : Nat :=
  n + n

def square (n : Nat) : Nat :=
  n * n

theorem double_zero : double 0 = 0 := by
  simp [double]

theorem square_one : square 1 = 1 := by
  simp [square]

#eval double 5
#eval square 4