import Mathlib

example : ¬ (∀ a b c : ℤ, (a < c ∨ c < b) → (a < c ∧ c < b)) := by
  intro h
  have hh := h (5 : ℤ) (0 : ℤ) (10 : ℤ) (Or.inl (by norm_num))
  norm_num at hh