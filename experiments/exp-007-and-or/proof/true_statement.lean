import Mathlib

example (a b c : ℤ) (h : a < c ∧ c < b) : a < c ∧ c < b := h

example (a b c : ℤ) (h : a < c ∧ c < b) : a < b := by
  exact lt_trans h.1 h.2