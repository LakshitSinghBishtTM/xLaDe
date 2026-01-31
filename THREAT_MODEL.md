# Threat Model

This document describes what xLaDe **does and does not attempt to protect against**.

---

## Assets

xLaDe aims to protect:

- Lean kernel integrity
- Semantic stability
- Reproducibility of experiments
- Trust in upstream compatibility

---

## In-Scope Threats

xLaDe explicitly addresses:

- Accidental kernel modification
- Silent semantic divergence
- Unreviewed workflow changes
- Irreversible ecosystem experiments

---

## Out-of-Scope Threats

xLaDe does NOT attempt to protect against:

- Malicious contributors
- Supply-chain attacks
- Compiler exploits
- Performance regressions
- User error outside xLaDe workflows

---

## Trust Assumptions

- Lean core is trusted as-is
- Contributors follow documented processes
- CI enforcement is authoritative

---

## Summary

xLaDe’s threat model is **narrow and intentional**.

It focuses on protecting architectural boundaries rather than providing comprehensive security guarantees.
