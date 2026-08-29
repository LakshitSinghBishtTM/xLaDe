-- A simple logical implication proof

theorem implies_self (p : Prop) : p → p := by
  intro hp
  exact hp
