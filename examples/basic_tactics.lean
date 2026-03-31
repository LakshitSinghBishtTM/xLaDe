-- Simple use of tactics

theorem zero_add_example (n : Nat) : 0 + n = n := by
  simp

theorem add_zero_example (n : Nat) : n + 0 = n := by
  simp

theorem add_self_eq_double (n : Nat) : n + n = 2 * n := by
  simp

#check zero_add_example
#check add_self_eq_double