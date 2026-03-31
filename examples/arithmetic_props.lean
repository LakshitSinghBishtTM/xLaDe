-- Basic arithmetic properties

theorem add_comm_example (a b : Nat) : a + b = b + a := by
  exact Nat.add_comm a b

theorem add_assoc_example (a b c : Nat) :
  (a + b) + c = a + (b + c) := by
  exact Nat.add_assoc a b c

theorem mul_one_example (n : Nat) : n * 1 = n := by
  exact Nat.mul_one n

#check add_comm_example
#check add_assoc_example