# Threat Model

This document describes what xLaDe does and does not attempt to protect against.

---

## Scope

- Lean kernel integrity
- Semantic stability
- Reproducibility of experiments
- Trust in upstream compatibility

---

## In-Scope Threats

- Accidental kernel modification
- Silent semantic divergence
- Unreviewed workflow changes
- Irreversible ecosystem experiments

---

## Out-of-Scope Threats

- Malicious contributors
- Supply-chain attacks
- Compiler exploits
- Performance regressions
- User error outside xLaDe workflows

---

## Trust Assumptions

- Trusted lean core
- Contributors follow documented processes
- CI enforcement is authoritative
