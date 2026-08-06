# Metrics — EXP-006: Lean Companion to Analysis I

## Enforcement Strength

- Script-based via the project's own `build.sh` (`lake exe cache get` +
  `lake build`)
- Pass/fail determined by exit code
- No semantic analysis beyond Lean type checking
- Whole-repository build -- not scoped to individual targets

## Scope

- External project only (`analysis/` submodule)
- No impact on xLaDe core or Lean kernel
- No upstream project modifications

## Friction Introduced

- Requires Lake installed via elan
- Submodule must be populated
- New, compared to EXP-004/EXP-005: requires `lake exe cache get` to
  succeed before `lake build` -- without it, Mathlib would need to
  compile from source instead of fetching prebuilt `.olean` files, which
  is a categorically longer build
- New: meaningful disk space for the Mathlib cache, and meaningful
  bandwidth for the initial fetch -- worth timing on first run, since
  exp-005's README documented ~454 KB/s as a real connection speed on
  this machine
- No friction on xLaDe core workflows

## Reversibility

- Fully reversible -- remove experiment directory and submodule reference
- No persistent state outside `.xlade/metrics.json`

---

## First Run

(venv) [ajay@mac xLaDe]$ xlade run exp-006-teorth-analysis

  Running experiment:  exp-006-teorth-analysis
  Mode:                experimental
  Toolchain:           leanprover/lean4:v4.29.0-rc8
  Timestamp:           2026-08-05 07:00:51
  ----------------------------------------------------------------------------------------------------
  xLaDe EXP-006: Lean Companion to Analysis I
  ----------------------------------------------------------------------------------------------------
  [info]   Project: experiments/exp-006-teorth-analysis/analysis
  [info]   Running: ./build.sh (lake exe cache get && lake build)
  ----------------------------------------------------------------------------------------------------
  ⚠ [8/21] Replayed Cache.Hashing
  warning: Cache/Hashing.lean:12:10: Ambiguous namespace `IO`: this `open` refers to all of 
  `_root_.Cache.IO`, `_root_.Lean.IO`, while `_root_.IO` is silently not opened because the `open` 
  occurs inside `namespace Cache.Hashing`. Specify the namespace unambiguously, e.g. 
  `_root_.Cache.IO`. The warning can sometimes also be addressed by moving the `open` outside of the 
  surrounding `namespace`.
  
  Note: This linter can be disabled with `set_option linter.ambiguousOpen false`
  Dependency Mathlib uses a different lean-toolchain
    Project uses leanprover/lean4:v4.33.0-rc2
    Mathlib uses leanprover/lean4:v4.29.0-rc8
  
  The cache will not work unless your project's toolchain matches Mathlib's toolchain
  This can be achieved by copying the contents of the file `.lake/packages/mathlib/lean-toolchain`
  into the `lean-toolchain` file at the root directory of your project
  You can use `cp .lake/packages/mathlib/lean-toolchain ./lean-toolchain`
  ----------------------------------------------------------------------------------------------------
  [fail]   build.sh failed.
  ----------------------------------------------------------------------------------------------------
  Status: failed

---

## Successful Run

(venv) [ajay@mac xLaDe]$ xlade run exp-006-teorth-analysis

  Running experiment:  exp-006-teorth-analysis
  Mode:                experimental
  Toolchain:           leanprover/lean4:v4.29.0-rc8
  Timestamp:           2026-08-06 06:14:26
  ----------------------------------------------------------------------------------------------------
  xLaDe EXP-006: Lean Companion to Analysis I
  ----------------------------------------------------------------------------------------------------
  [info]   Project: experiments/exp-006-teorth-analysis/analysis
  [info]   Running: ./build.sh (lake exe cache get && lake build)
  ----------------------------------------------------------------------------------------------------
  info: verso: checking out revision 'b6a5bacc221b260a67d474a2436b89d067ae5f7d'
  info: MD4Lean: checking out revision '6a3fb240133bcb7e1a066fdc784b3fdc304e3fc5'
  info: subverso: checking out revision '52b9dfbd2658408e37ae6e8b72601ddeaaa25a0c'
  ✔ [3/21] Built Cache.Init (302ms)
  ✔ [4/21] Built Batteries.Data.String.Basic (447ms)
  ✔ [5/21] Built Cache.Lean (481ms)
  ✔ [6/21] Built Batteries.Data.String.Basic:c.o (227ms)
  ✔ [7/21] Built Cache.Init:c.o (325ms)
  ✔ [8/21] Built Cache.Lean:c.o (296ms)
  ✔ [9/21] Built Batteries.Data.Array.Match (1.3s)
  ✔ [10/21] Built Batteries.Data.String.Matcher (527ms)
  ✔ [11/21] Built Batteries.Data.Array.Match:c.o (566ms)
  ✔ [12/21] Built Batteries.Data.String.Matcher:c.o (395ms)
  ✔ [13/21] Built Cache.IO (2.1s)
  ✔ [14/21] Built Cache.Hashing (532ms)
  ✔ [15/21] Built Cache.Hashing:c.o (469ms)
  ✔ [16/21] Built Cache.IO:c.o (1.5s)
  ✔ [17/21] Built Cache.Requests (1.7s)
  ✔ [18/21] Built Cache.Main (649ms)
  ✔ [19/21] Built Cache.Main:c.o (566ms)
  ✔ [20/21] Built Cache.Requests:c.o (2.3s)
  ✔ [21/21] Built cache:exe (1.5s)
  Fetching ProofWidgets cloud release... done!
  Current branch: HEAD
  Using cache (Azure) from origin: leanprover-community/mathlib4
  Attempting to download 8192 file(s) from leanprover-community/mathlib4 cache
Downloaded: 8192 file(s) [attempted 8192/8192 = 100%, 189 KB/s], Decompressed: 8180
  Decompressed 8192 file(s)
  Already decompressed 8192 file(s)
  ℹ [3499/3580] Built Analysis.Tools.ExistsUnique (10s)
  info: Analysis/Tools/ExistsUnique.lean:11:0: existsUnique_of_exists_of_unique.{u_1} {α : Sort u_1} 
  {p : α → Prop} (hex : ∃ x, p x)
    (hunique : ∀ (y₁ y₂ : α), p y₁ → p y₂ → y₁ = y₂) : ∃! x, p x
  info: Analysis/Tools/ExistsUnique.lean:12:0: ExistsUnique.exists.{u_1} {α : Sort u_1} {p : α → 
  Prop} : (∃! x, p x) → ∃ x, p x
  info: Analysis/Tools/ExistsUnique.lean:13:0: ExistsUnique.unique.{u_1} {α : Sort u_1} {p : α → 
  Prop} (h : ∃! x, p x) {y₁ y₂ : α} (py₁ : p y₁) (py₂ : p y₂) : y₁ = y₂
  info: Analysis/Tools/ExistsUnique.lean:14:0: ExistsUnique.intro.{u_1} {α : Sort u_1} {p : α → Prop} 
  (w : α) (h₁ : p w) (h₂ : ∀ (y : α), p y → y = w) : ∃! x, p x
  info: Analysis/Tools/ExistsUnique.lean:50:0: 'ExistsUnique.iff_subsingleton_nonempty' depends on 
  axioms: [propext]
  ✔ [3500/3580] Built Analysis.Section_10_3 (10s)
  ℹ [3501/3580] Built Analysis.Section_2_1 (12s)
  info: Analysis/Section_2_1.lean:46:0: 0 : Nat
  info: Analysis/Section_2_1.lean:50:0: fun n ↦ n++ : Nat → Nat
  info: Analysis/Section_2_1.lean:61:0: 1 : Nat
  info: Analysis/Section_2_1.lean:64:0: 2 : Nat
  info: Analysis/Section_2_1.lean:68:0: 3 : Nat
  ✔ [3502/3580] Built Analysis.Section_9_2 (12s)
  ✔ [3503/3580] Built Analysis.Section_9_10 (15s)
  ✔ [3504/3580] Built Analysis.Section_4_3 (19s)
  ℹ [3505/3580] Built Analysis.Section_10_1 (19s)
  info: Analysis/Section_10_1.lean:53:0: DifferentiableWithinAt.hasDerivWithinAt.{u, v} {𝕜 : Type u} 
  [NontriviallyNormedField 𝕜] {F : Type v}
    [NormedAddCommGroup F] [NormedSpace 𝕜 F] {f : 𝕜 → F} {x : 𝕜} {s : Set 𝕜} (h : 
  DifferentiableWithinAt 𝕜 f s x) :
    HasDerivWithinAt f (derivWithin f s x) s x
  info: Analysis/Section_10_1.lean:126:0: DifferentiableOn.eq_1.{u_1, u_2, u_3} (𝕜 : Type u_1) 
  [NontriviallyNormedField 𝕜] {E : Type u_2} [AddCommGroup E]
    [Module 𝕜 E] [TopologicalSpace E] {F : Type u_3} [AddCommGroup F] [Module 𝕜 F] [TopologicalSpace 
  F] (f : E → F)
    (s : Set E) : DifferentiableOn 𝕜 f s = ∀ x ∈ s, DifferentiableWithinAt 𝕜 f s x
  ℹ [3506/3580] Built Analysis.Appendix_A_1 (21s)
  info: Analysis/Appendix_A_1.lean:15:0: 2 + 2 = 4 : Prop
  info: Analysis/Appendix_A_1.lean:16:0: 2 + 2 = 5 : Prop
  info: Analysis/Appendix_A_1.lean:39:0: 2 + 3 * 5 : ℕ
  info: Analysis/Appendix_A_1.lean:42:0: 2 + 3 * 5 = 17 : Prop
  info: Analysis/Appendix_A_1.lean:44:0: Prime (30 + 5) : Prop
  info: Analysis/Appendix_A_1.lean:46:0: 30 + 5 ≤ 42 - 7 : Prop
  info: Analysis/Appendix_A_1.lean:108:0: Xor' (a b : Prop) : Prop
  ✔ [3507/3580] Built Analysis.Section_4_1 (22s)
  ✔ [3508/3580] Built Analysis.Section_4_2 (22s)
  ✔ [3509/3580] Built Analysis.Appendix_A_5 (13s)
  ℹ [3510/3581] Built Analysis.Appendix_A_2 (16s)
  info: Analysis/Appendix_A_2.lean:37:0: _root_.not_imp {a b : Prop} : ¬(a → b) ↔ a ∧ ¬b
  ℹ [3511/3594] Built Analysis.Appendix_A_4 (16s)
  info: Analysis/Appendix_A_4.lean:14:0: x = x : Prop
  info: Analysis/Appendix_A_4.lean:15:0: x = y : Prop
  info: Analysis/Appendix_A_4.lean:25:0: x + 3 : ℝ
  info: Analysis/Appendix_A_4.lean:26:0: x + 3 = 5 : Prop
  ℹ [4072/4160] Built Analysis.Appendix_A_7 (13s)
  info: Analysis/Appendix_A_7.lean:29:0: Eq.refl.{u_1} {α : Sort u_1} (a : α) : a = a
  info: Analysis/Appendix_A_7.lean:35:0: Eq.symm.{u} {α : Sort u} {a b : α} (h : a = b) : b = a
  info: Analysis/Appendix_A_7.lean:41:0: Eq.trans.{u} {α : Sort u} {a b c : α} (h₁ : a = b) (h₂ : b = 
  c) : a = c
  info: Analysis/Appendix_A_7.lean:47:0: congrArg.{u, v} {α : Sort u} {β : Sort v} {a₁ a₂ : α} (f : α 
  → β) (h : a₁ = a₂) : f a₁ = f a₂
  info: Analysis/Appendix_A_7.lean:91:0: Quot.mk make_twelve_equal_two 2 : Quot make_twelve_equal_two
  info: Analysis/Appendix_A_7.lean:92:0: Quot.mk make_twelve_equal_two 12 : Quot make_twelve_equal_two
  ✔ [4202/4303] Built Analysis.Section_7_2 (33s)
  ✔ [4270/4359] Built Analysis.Appendix_A_3 (22s)
  ✔ [4734/4820] Built Analysis.Appendix_A_6 (19s)
  ℹ [4797/4867] Built Analysis.Section_3_1 (35s)
  info: Analysis/Section_3_1.lean:146:0: Chapter3.SetTheory.Set.ext_iff.{u_1, u_2} [SetTheory] {X Y : 
  Set} : X = Y ↔ ∀ (x : Object), x ∈ X ↔ x ∈ Y
  ✔ [4923/5001] Built Analysis.Misc.FiniteChoice (14s)
  ✔ [6408/6501] Built Analysis.Misc.Probability (20s)
  ✔ [7806/7890] Built Analysis.Section_3_2 (14s)
  ✔ [8228/8310] Built Analysis.Section_3_epilogue (26s)
  ✔ [8230/8310] Built Analysis.Misc.NatBitwise (10s)
  ℹ [8231/8310] Built Analysis.Section_4_4 (63s)
  info: Analysis/Section_4_4.lean:61:0: even_iff_exists_two_mul.{u_2} {α : Type u_2} [Semiring α] {a 
  : α} : Even a ↔ ∃ b, a = 2 * b
  info: Analysis/Section_4_4.lean:62:0: odd_iff_exists_bit1.{u_2} {α : Type u_2} [Semiring α] {a : α} 
  : Odd a ↔ ∃ b, a = 2 * b + 1
  info: Analysis/Section_4_4.lean:70:0: Nat.rec.{u} {motive : ℕ → Sort u} (zero : motive Nat.zero) 
  (succ : (n : ℕ) → motive n → motive n.succ) (t : ℕ) :
    motive t
  ✔ [8232/8310] Built Analysis.Misc.UnitsSystem (45s)
  ✔ [8233/8310] Built Analysis.Misc.Combinatorics (18s)
  ⚠ [8234/8310] Built Analysis.Misc.«Real-EReal-ENNReal» (19s)
  warning: Analysis/Misc/Real-EReal-ENNReal.lean:294:51: unused variable `hg_sum`
  
  Note: This linter can be disabled with `set_option linter.unusedVariables false`
  ✔ [8235/8310] Built Analysis.Section_8_1 (72s)
  ℹ [8236/8310] Built Analysis.Section_3_3 (41s)
  info: Analysis/Section_3_3.lean:58:0: Chapter3.Function.mk.{u_1, u_2} [SetTheory] {X Y : Set} (P : 
  X.toSubtype → Y.toSubtype → Prop)
    (unique : ∀ (x : X.toSubtype), ∃! y, P x y) : Function X Y
  ✔ [8237/8310] Built Analysis.Misc.UnitsSystemExamples (9.8s)
  ℹ [8238/8310] Built Analysis.MeasureTheory.Notation (28s)
  info: Analysis/MeasureTheory/Notation.lean:60:0: top_add.{u_2} {α : Type u_2} 
  [LinearOrderedAddCommMonoidWithTop α] (a : α) : ⊤ + a = ⊤
  info: Analysis/MeasureTheory/Notation.lean:61:0: add_top.{u_2} {α : Type u_2} 
  [LinearOrderedAddCommMonoidWithTop α] (a : α) : a + ⊤ = ⊤
  info: Analysis/MeasureTheory/Notation.lean:62:0: ENNReal.top_mul {a : ENNReal} (h : a ≠ 0) : ⊤ * a 
  = ⊤
  info: Analysis/MeasureTheory/Notation.lean:63:0: ENNReal.mul_top {a : ENNReal} (h : a ≠ 0) : a * ⊤ 
  = ⊤
  info: Analysis/MeasureTheory/Notation.lean:64:0: lt_top_iff_ne_top.{u} {α : Type u} [PartialOrder 
  α] [OrderTop α] {a : α} : a < ⊤ ↔ a ≠ ⊤
  info: Analysis/MeasureTheory/Notation.lean:182:0: ENNReal.tendsto_nat_tsum (f : ℕ → ENNReal) : 
  Tendsto (fun n ↦ ∑ i ∈ Finset.range n, f i) atTop (nhds (∑' (n : ℕ), f n))
  info: Analysis/MeasureTheory/Notation.lean:184:0: ENNReal.tsum_eq_iSup_sum.{u_1} {α : Type u_1} {f 
  : α → ENNReal} : ∑' (a : α), f a = ⨆ s, ∑ a ∈ s, f a
  info: Analysis/MeasureTheory/Notation.lean:186:0: Equiv.tsum_eq.{u_1, u_2, u_3} {α : Type u_1} {β : 
  Type u_2} {γ : Type u_3} [AddCommMonoid α] [TopologicalSpace α]
    (e : γ ≃ β) (f : β → α) : ∑' (c : γ), f (e c) = ∑' (b : β), f b
  info: Analysis/MeasureTheory/Notation.lean:233:0: ENNReal.tsum_comm.{u_1, u_2} {α : Type u_1} {β : 
  Type u_2} {f : α → β → ENNReal} :
    ∑' (a : α) (b : β), f a b = ∑' (b : β) (a : α), f a b
  ✔ [8239/8310] Built Analysis.Misc.SI (14s)
  ℹ [8240/8310] Built Analysis.Section_2_2 (56s)
  info: Analysis/Section_2_2.lean:62:0: fun n m ↦ n + m : Nat → Nat → Nat
  info: Analysis/Section_2_2.lean:173:0: existsUnique_of_exists_of_unique.{u_1} {α : Sort u_1} {p : α 
  → Prop} (hex : ∃ x, p x)
    (hunique : ∀ (y₁ y₂ : α), p y₁ → p y₂ → y₁ = y₂) : ∃! x, p x
  ℹ [8241/8310] Built Analysis.Appendix_B_1 (66s)
  info: Analysis/Appendix_B_1.lean:63:0: 0 : Digit
  info: Analysis/Appendix_B_1.lean:64:0: 1 : Digit
  info: Analysis/Appendix_B_1.lean:65:0: 2 : Digit
  info: Analysis/Appendix_B_1.lean:66:0: 3 : Digit
  info: Analysis/Appendix_B_1.lean:67:0: 4 : Digit
  info: Analysis/Appendix_B_1.lean:68:0: 5 : Digit
  info: Analysis/Appendix_B_1.lean:69:0: 6 : Digit
  info: Analysis/Appendix_B_1.lean:70:0: 7 : Digit
  info: Analysis/Appendix_B_1.lean:71:0: 8 : Digit
  info: Analysis/Appendix_B_1.lean:72:0: 9 : Digit
  info: Analysis/Appendix_B_1.lean:113:0: PosintDecimal.mk' 3 [1, 4] ⋯ : PosintDecimal
  info: Analysis/Appendix_B_1.lean:116:0: PosintDecimal.mk' 3 [] ⋯ : PosintDecimal
  info: Analysis/Appendix_B_1.lean:119:0: PosintDecimal.mk' 1 [0] ⋯ : PosintDecimal
  ✔ [8242/8310] Built Analysis.Section_3_4 (54s)
  ✔ [8243/8310] Built Analysis.Section_2_3 (8.0s)
  ℹ [8244/8310] Built Analysis.Misc.SIExamples (11s)
  info: Analysis/Misc/SIExamples.lean:13:0: F = m * a : Prop
  info: Analysis/Misc/SIExamples.lean:14:0: p = m * v : Prop
  info: Analysis/Misc/SIExamples.lean:15:0: h = v * t - g * t**2 / 2 : Prop
  info: Analysis/Misc/SIExamples.lean:16:0: E = m * c**2 : Prop
  info: Analysis/Misc/SIExamples.lean:17:0: E = m * v**2 / 2 + m * g * h : Prop
  ✔ [8245/8310] Built Analysis.Section_2_epilogue (7.9s)
  ℹ [8246/8310] Built Analysis.Section_11_1 (106s)
  info: Analysis/Section_11_1.lean:64:0: Set.ordConnected_def.{u_1} {α : Type u_1} [Preorder α] {s : 
  Set α} :
    s.OrdConnected ↔ ∀ ⦃x : α⦄, x ∈ s → ∀ ⦃y : α⦄, y ∈ s → Set.Icc x y ⊆ s
  info: Analysis/Section_11_1.lean:208:0: Chapter11.Partition.mk {I : BoundedInterval} (intervals : 
  Finset BoundedInterval)
    (exists_unique : ∀ x ∈ I, ∃! J, J ∈ intervals ∧ x ∈ J) (contains : ∀ J ∈ intervals, J ⊆ I) : 
  Partition I
  ℹ [8247/8310] Built Analysis.Appendix_B_2 (23s)
  info: Analysis/Appendix_B_2.lean:21:0: AppendixB.NNRealDecimal.mk (intPart : ℕ) (fracPart : ℕ → 
  Digit) : NNRealDecimal
  ✔ [8248/8310] Built Analysis.Misc.erdos_379 (46s)
  ✔ [8249/8310] Built Analysis.Misc.erdos_987 (51s)
  ✔ [8250/8310] Built Analysis.Section_11_2 (8.0s)
  ℹ [8251/8310] Built Analysis.Section_7_1 (121s)
  info: Analysis/Section_7_1.lean:41:0: Finset.mem_Icc.{u_1} {α : Type u_1} [Preorder α] 
  [LocallyFiniteOrder α] {a b x : α} : x ∈ Icc a b ↔ a ≤ x ∧ x ≤ b
  info: Analysis/Section_7_1.lean:96:0: Finset.sum_congr.{u_1, u_4} {ι : Type u_1} {M : Type u_4} {s₁ 
  s₂ : Finset ι} [AddCommMonoid M] {f g : ι → M}
    (h : s₁ = s₂) : (∀ x ∈ s₂, f x = g x) → s₁.sum f = s₂.sum g
  info: Analysis/Section_7_1.lean:294:0: Nat.factorial_zero : Nat.factorial 0 = 1
  info: Analysis/Section_7_1.lean:295:0: Nat.factorial_succ (n : ℕ) : (n + 1).factorial = (n + 1) * 
  n.factorial
  ℹ [8252/8310] Built Analysis.Section_5_1 (96s)
  info: Analysis/Section_5_1.lean:56:0: ↑fun x ↦ ↑x ^ 2 : Sequence
  ℹ [8253/8310] Built Analysis.Section_3_5 (34s)
  info: Analysis/Section_3_5.lean:45:0: Chapter3.OrderedPair.ext.{u_1, u_2} {inst✝ : SetTheory} {x y 
  : OrderedPair} (fst : x.fst = y.fst)
    (snd : x.snd = y.snd) : x = y
  ✔ [8254/8310] Built Analysis.Misc.erdos_707 (63s)
  ✔ [8255/8310] Built Analysis.Section_5_2 (6.4s)
  ✔ [8256/8310] Built Analysis.Misc.erdos_613 (67s)
  ✔ [8257/8310] Built Analysis.Section_3_6 (29s)
  ✔ [8258/8310] Built Analysis.Section_5_3 (25s)
  ✔ [8259/8310] Built Analysis.Section_5_4 (23s)
  ✔ [8260/8310] Built Analysis.Section_5_5 (20s)
  ✔ [8261/8310] Built Analysis.Section_5_6 (6.4s)
  ℹ [8262/8310] Built Analysis.Section_5_epilogue (2.3s)
  info: Analysis/Section_5_epilogue.lean:197:0: Real.mk_le {f g : CauSeq ℚ abs} : Real.mk f ≤ Real.mk 
  g ↔ f ≤ g
  info: Analysis/Section_5_epilogue.lean:198:0: Real.mk_le_of_forall_le {f : CauSeq ℚ abs} {x : ℝ} (h 
  : ∃ i, ∀ j ≥ i, ↑(↑f j) ≤ x) : Real.mk f ≤ x
  info: Analysis/Section_5_epilogue.lean:199:0: Real.mk_const {x : ℚ} : Real.mk (CauSeq.const abs x) 
  = ↑x
  ℹ [8263/8310] Built Analysis.Section_6_2 (4.2s)
  info: Analysis/Section_6_2.lean:44:0: EReal.neg_top : -⊤ = ⊥
  info: Analysis/Section_6_2.lean:45:0: EReal.neg_bot : -⊥ = ⊤
  info: Analysis/Section_6_2.lean:55:0: EReal.coe_lt_coe_iff {x y : ℝ} : ↑x < ↑y ↔ x < y
  info: Analysis/Section_6_2.lean:75:0: instCompleteLinearOrderEReal : CompleteLinearOrder EReal
  info: Analysis/Section_6_2.lean:176:0: isLUB_iff_sSup_eq.{u_1} {α : Type u_1} 
  [CompleteSemilatticeSup α] {s : Set α} {a : α} : IsLUB s a ↔ sSup s = a
  info: Analysis/Section_6_2.lean:177:0: isGLB_iff_sInf_eq.{u_1} {α : Type u_1} 
  [CompleteSemilatticeInf α] {s : Set α} {a : α} : IsGLB s a ↔ sInf s = a
  ℹ [8264/8310] Built Analysis.Section_6_1 (6.3s)
  info: Analysis/Section_6_1.lean:24:0: Real.dist_eq (x y : ℝ) : dist x y = |x - y|
  ✔ [8265/8310] Built Analysis.Section_6_3 (2.6s)
  ✔ [8266/8310] Built Analysis.Section_6_4 (5.5s)
  ✔ [8267/8310] Built Analysis.Section_6_5 (17s)
  ℹ [8268/8310] Built Analysis.Section_9_1 (19s)
  info: Analysis/Section_9_1.lean:25:0: Set.Icc_def.{u_1} {α : Type u_1} [Preorder α] (a b : α) : {x 
  | a ≤ x ∧ x ≤ b} = Set.Icc a b
  info: Analysis/Section_9_1.lean:26:0: Set.Ico_def.{u_1} {α : Type u_1} [Preorder α] (a b : α) : {x 
  | a ≤ x ∧ x < b} = Set.Ico a b
  info: Analysis/Section_9_1.lean:27:0: Set.Ioc_def.{u_1} {α : Type u_1} [Preorder α] (a b : α) : {x 
  | a < x ∧ x ≤ b} = Set.Ioc a b
  info: Analysis/Section_9_1.lean:28:0: Set.Ioo_def.{u_1} {α : Type u_1} [Preorder α] (a b : α) : {x 
  | a < x ∧ x < b} = Set.Ioo a b
  info: Analysis/Section_9_1.lean:29:0: Set.Ici_def.{u_1} {α : Type u_1} [Preorder α] (b : α) : {x | 
  b ≤ x} = Set.Ici b
  info: Analysis/Section_9_1.lean:30:0: Set.Ioi_def.{u_1} {α : Type u_1} [Preorder α] (a : α) : {x | 
  a < x} = Set.Ioi a
  info: Analysis/Section_9_1.lean:31:0: Set.Iic_def.{u_1} {α : Type u_1} [Preorder α] (b : α) : {x | 
  x ≤ b} = Set.Iic b
  info: Analysis/Section_9_1.lean:32:0: Set.Iio_def.{u_1} {α : Type u_1} [Preorder α] (a : α) : {x | 
  x < a} = Set.Iio a
  info: Analysis/Section_9_1.lean:34:0: EReal.image_coe_Icc (x y : ℝ) : Real.toEReal '' Set.Icc x y = 
  Set.Icc ↑x ↑y
  info: Analysis/Section_9_1.lean:35:0: EReal.image_coe_Ico (x y : ℝ) : Real.toEReal '' Set.Ico x y = 
  Set.Ico ↑x ↑y
  info: Analysis/Section_9_1.lean:36:0: EReal.image_coe_Ioc (x y : ℝ) : Real.toEReal '' Set.Ioc x y = 
  Set.Ioc ↑x ↑y
  info: Analysis/Section_9_1.lean:37:0: EReal.image_coe_Ioo (x y : ℝ) : Real.toEReal '' Set.Ioo x y = 
  Set.Ioo ↑x ↑y
  info: Analysis/Section_9_1.lean:38:0: EReal.image_coe_Ici (x : ℝ) : Real.toEReal '' Set.Ici x = 
  Set.Ico ↑x ⊤
  info: Analysis/Section_9_1.lean:39:0: EReal.image_coe_Ioi (x : ℝ) : Real.toEReal '' Set.Ioi x = 
  Set.Ioo ↑x ⊤
  info: Analysis/Section_9_1.lean:40:0: EReal.image_coe_Iic (x : ℝ) : Real.toEReal '' Set.Iic x = 
  Set.Ioc ⊥ ↑x
  info: Analysis/Section_9_1.lean:41:0: EReal.image_coe_Iio (x : ℝ) : Real.toEReal '' Set.Iio x = 
  Set.Ioo ⊥ ↑x
  ✔ [8269/8310] Built Analysis.Section_6_6 (4.0s)
  ✔ [8270/8310] Built Analysis.Section_9_3 (14s)
  ✔ [8271/8310] Built Analysis.Section_6_7 (15s)
  ℹ [8272/8310] Built Analysis.Section_9_4 (4.3s)
  info: Analysis/Section_9_4.lean:28:0: ContinuousOn.eq_1.{u_1, u_2} {X : Type u_1} {Y : Type u_2} 
  [TopologicalSpace X] [TopologicalSpace Y] (f : X → Y)
    (s : Set X) : ContinuousOn f s = ∀ x ∈ s, ContinuousWithinAt f s x
  info: Analysis/Section_9_4.lean:29:0: continuousOn_univ.{u_1, u_2} {α : Type u_1} {β : Type u_2} 
  [TopologicalSpace α] [TopologicalSpace β] {f : α → β} :
    ContinuousOn f Set.univ ↔ Continuous f
  info: Analysis/Section_9_4.lean:30:0: continuousWithinAt_univ.{u_1, u_2} {α : Type u_1} {β : Type 
  u_2} [TopologicalSpace α] [TopologicalSpace β] (f : α → β)
    (x : α) : ContinuousWithinAt f Set.univ x ↔ ContinuousAt f x
  ✔ [8273/8310] Built Analysis.Section_6_epilogue (10s)
  ✔ [8274/8310] Built Analysis.Section_9_5 (9.3s)
  ✔ [8275/8310] Built Analysis.Section_9_7 (14s)
  ✔ [8276/8310] Built Analysis.Section_10_4 (19s)
  ℹ [8277/8310] Built Analysis.Section_9_6 (24s)
  info: Analysis/Section_9_6.lean:77:0: isMaxOn_iff.{u, v} {α : Type u} {β : Type v} [Preorder β] {f 
  : α → β} {s : Set α} {a : α} :
    IsMaxOn f s a ↔ ∀ x ∈ s, f x ≤ f a
  info: Analysis/Section_9_6.lean:78:0: isMinOn_iff.{u, v} {α : Type u} {β : Type v} [Preorder β] {f 
  : α → β} {s : Set α} {a : α} :
    IsMinOn f s a ↔ ∀ x ∈ s, f a ≤ f x
  ℹ [8278/8310] Built Analysis.Section_9_8 (6.3s)
  info: Analysis/Section_9_8.lean:55:0: nontrivial_iff.{u_1} {α : Type u_1} : Nontrivial α ↔ ∃ x y, x 
  ≠ y
  ✔ [8279/8310] Built Analysis.Section_10_2 (7.4s)
  ℹ [8280/8310] Built Analysis.MeasureTheory.Section_1_1_1 (57s)
  info: Analysis/MeasureTheory/Section_1_1_1.lean:293:0: exists_lt_of_lt_csSup.{u_1} {α : Type u_1} 
  [ConditionallyCompleteLinearOrder α] {s : Set α} {b : α} (hs : s.Nonempty)
    (hb : b < sSup s) : ∃ a ∈ s, b < a
  info: Analysis/MeasureTheory/Section_1_1_1.lean:298:0: exists_lt_of_csInf_lt.{u_1} {α : Type u_1} 
  [ConditionallyCompleteLinearOrder α] {s : Set α} {b : α} (hs : s.Nonempty)
    (hb : sInf s < b) : ∃ a ∈ s, a < b
  ✔ [8281/8310] Built Analysis.Section_7_3 (31s)
  ✔ [8282/8310] Built Analysis.Section_11_3 (21s)
  ✔ [8283/8310] Built Analysis.Section_9_9 (31s)
  ⚠ [8284/8310] Built Analysis.MeasureTheory.Section_1_1_2 (20s)
  warning: Analysis/MeasureTheory/Section_1_1_2.lean:146:24: unused variable `hAE`
  
  Note: This linter can be disabled with `set_option linter.unusedVariables false`
  warning: Analysis/MeasureTheory/Section_1_1_2.lean:168:24: unused variable `hAE`
  
  Note: This linter can be disabled with `set_option linter.unusedVariables false`
  ⚠ [8285/8310] Built Analysis.Section_10_5 (28s)
  warning: Analysis/Section_10_5.lean:33:49: unused variable `hab`
  
  Note: This linter can be disabled with `set_option linter.unusedVariables false`
  ✔ [8286/8310] Built Analysis.Section_7_4 (29s)
  ✔ [8287/8310] Built Analysis.MeasureTheory.Section_1_1_3 (17s)
  ✔ [8288/8310] Built Analysis.Section_7_5 (13s)
  ✔ [8289/8310] Built Analysis.MeasureTheory.Section_1_2_0 (18s)
  ✔ [8290/8310] Built Analysis.Section_11_4 (51s)
  ✔ [8291/8310] Built Analysis.Section_8_2 (29s)
  ✔ [8292/8310] Built Analysis.Section_11_7 (14s)
  ✔ [8293/8310] Built Analysis.Section_8_4 (14s)
  ✔ [8294/8310] Built Analysis.Section_8_3 (14s)
  ✔ [8295/8310] Built Analysis.MeasureTheory.Section_1_2_1 (71s)
  ✔ [8296/8310] Built Analysis.Section_11_5 (82s)
  ✔ [8297/8310] Built Analysis.MeasureTheory.Section_1_2_2 (11s)
  ℹ [8298/8310] Built Analysis.Section_8_5 (68s)
  info: Analysis/Section_8_5.lean:60:0: inferInstance : LinearOrder ℕ
  info: Analysis/Section_8_5.lean:61:0: inferInstance : LinearOrder ℚ
  info: Analysis/Section_8_5.lean:62:0: inferInstance : LinearOrder ℝ
  info: Analysis/Section_8_5.lean:63:0: inferInstance : LinearOrder EReal
  ✔ [8299/8310] Built Analysis.MeasureTheory.Section_1_2_3 (6.2s)
  ✔ [8300/8310] Built Analysis.MeasureTheory.Section_1_3_1 (10s)
  ✔ [8301/8310] Built Analysis.Section_11_6 (33s)
  ✔ [8302/8310] Built Analysis.Section_11_8 (9.2s)
  ✔ [8303/8310] Built Analysis.MeasureTheory.Section_1_3_2 (32s)
  ✔ [8304/8310] Built Analysis.MeasureTheory.Section_1_3_3 (4.0s)
  ✔ [8305/8310] Built Analysis.MeasureTheory.Section_1_3_4 (9.0s)
  ✔ [8306/8310] Built Analysis.Section_11_9 (27s)
  ✔ [8307/8310] Built Analysis.MeasureTheory.Section_1_3_5 (9.0s)
  ✔ [8308/8310] Built Analysis.Section_11_10 (21s)
  ✔ [8309/8310] Built Analysis (3.6s)
  Build completed successfully (8310 jobs).
  ----------------------------------------------------------------------------------------------------
  [pass]   build.sh succeeded.
  ----------------------------------------------------------------------------------------------------
  ----------------------------------------------------------------------------------------------------
  Status: success