# Research Scope of xLaDe

## 1. Purpose of This Document

This document clarifies the **research scope, intent, and boundaries** of the xLaDe project. It is written to prevent ambiguity regarding what the project *does* and *does not* attempt to achieve.

xLaDe is a **research artifact**, not a production-ready software platform.

---

## 2. What xLaDe *Is*

xLaDe is an **experimental ecosystem framework built around Lean 4**, designed to explore research questions related to:

* Human-oriented proof development workflows
* Tooling and automation around formal proofs
* Evaluation and metrics for proof construction
* Governance, policies, and lifecycle management in proof ecosystems
* Experimental modes of interaction with proof assistants

The project focuses on **meta-level concerns** surrounding proof assistants rather than extending mathematical libraries or modifying the Lean kernel.

---

## 3. What xLaDe *Is Not*

xLaDe explicitly **does not**:

* Modify the Lean 4 kernel, compiler, or trusted code base
* Claim performance or correctness improvements over Lean itself
* Replace existing Lean tooling or standard workflows
* Serve as a production-grade or community-supported platform
* Act as a fork of Lean 4

Lean 4 is treated strictly as an **external dependency**, not as a component developed within this research.

---

## 4. Relationship to Lean 4

Lean 4 is included in this repository **only as a Git submodule**. This design choice is intentional and reflects the research philosophy of the project:

* Lean 4 remains an independently developed proof assistant
* xLaDe operates as an **overlay ecosystem** that interacts with Lean through standard interfaces
* No changes are made to Lean’s trusted computing base

This separation ensures that all experimental results and observations are attributable to ecosystem-level design decisions rather than core system modifications.

---

## 5. Research-Oriented Components

The repository is structured to mirror research concerns rather than product features:

* `experiments/` — exploratory prototypes and controlled experiments
* `metrics/` — mechanisms for observing and evaluating proof development
* `modes/` — alternative operational or interaction modes
* `policies/` — governance, contribution, and lifecycle rules
* `tools/` — auxiliary scripts supporting experimentation and analysis

These components collectively support investigation into **how proof assistants are used**, not merely *how proofs are written*.

---

## 6. Scope Limitations

The following are **out of scope** for this research:

* Large-scale formalization of mathematical theories
* Benchmarking against industrial proof workloads
* Long-term maintenance or backward compatibility guarantees
* Community governance beyond illustrative examples

Such topics are intentionally excluded to maintain focus within the constraints.

---

## 7. Intended Audience

xLaDe is intended for:

* Researchers studying proof assistants and formal methods
* Students exploring experimental tooling around Lean 4

It is **not intended** for general end users or industrial deployment as of now.

---

## 9. Summary

xLaDe is a **research-driven, exploratory ecosystem framework** that investigates how proof assistants like Lean 4 can be supported by better tooling, evaluation methods, and governance structures.

Its value lies in **insight and experimentation**, not in production readiness or adoption metrics.
