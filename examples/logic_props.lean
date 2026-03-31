-- Basic logical reasoning

theorem and_comm (p q : Prop) : p ∧ q → q ∧ p := by
  intro h
  exact And.intro h.right h.left

theorem imp_trans (p q r : Prop) :
  (p → q) → (q → r) → (p → r) := by
  intro hpq hqr hp
  exact hqr (hpq hp)

#check and_comm
#check imp_trans