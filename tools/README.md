# xLaDe Tools

This directory contains **optional helper tools** used by xLaDe experiments, scripts, or developer workflows.
Tools provide **convenience and exploratory functionality**, but are never required for using Lean itself or for the correctness of xLaDe’s core design.

---

## What Tools Are (and Are Not)

### Tools **ARE**
- Optional helper utilities
- Used to:
  - improve developer experience
  - prototype ideas
  - support experiments or scripts
- Explicit, inspectable, and replaceable
- Designed to be added or removed without affecting core behavior

### Tools **ARE NOT**
- Part of the minimal xLaDe core
- Required for Lean compilation or proof checking
- Sources of semantic guarantees
- Stable or long-term commitments

No tool in this directory is relied upon for correctness.

---

## Design Principles

Tools in this directory follow these principles:

- **Non-essential**  
  Removing a tool must not break xLaDe or Lean usage.

- **Replaceable**  
  Tools may be rewritten, replaced, or discarded as experiments evolve.

- **Non-invasive**  
  Tools must not modify:
  - the Lean kernel
  - Lean source semantics
  - trusted compiler behavior

- **Experimental**  
  Tools may be incomplete, heuristic, or exploratory.

---

## Relationship to Experiments and Scripts

- Experiments may optionally invoke tools
- Scripts may use tools as helpers
- Neither experiments nor scripts may *depend* on tools for correctness

This ensures that tools enhance experimentation without becoming hidden
dependencies.

---

## Examples

Typical tools may include:
- error explanation helpers
- diagnostics wrappers
- experimental UX improvements
- analysis or reporting helpers

All such tools remain **outside the minimal core guarantees** of xLaDe.

---

## Summary

xLaDe tools exist to **support exploration, not enforce structure**.

They:
- improve ergonomics,
- enable rapid experimentation,
- and remain safely removable.

This separation preserves xLaDe’s minimal, research-first architecture.
