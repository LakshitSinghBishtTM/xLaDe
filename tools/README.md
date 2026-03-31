# xLaDe Tools

This directory contains optional helper tools used by xLaDe experiments, scripts, or developer workflows.
Tools provide convenience and exploratory functionality, but are never required for using Lean itself or for the correctness of xLaDe’s core design.

---

## What Tools Are (and Are Not)

### Tools ARE

- Optional helper utilities
- Used to:
  - improve developer experience
  - prototype ideas
  - support experiments or scripts
- Explicit, inspectable, and replaceable
- Designed to be added or removed without affecting core behavior

### Tools ARE NOT

- Part of the minimal xLaDe core
- Required for Lean compilation or proof checking
- Sources of semantic guarantees
- Stable or long-term commitments

---

## Design Principles

- Non-essential 
  Removing a tool must not break xLaDe or Lean usage.

- Replaceable
  Tools may be rewritten, replaced, or discarded as experiments evolve.

- Non-invasive
  Tools must not modify:
  - the Lean kernel
  - Lean source semantics
  - trusted compiler behavior

- Experimental
  Tools may be incomplete or exploratory.

---

## Relationship to Experiments and Scripts

- Experiments may optionally invoke tools
- Scripts may use tools as helpers
- Neither experiments nor scripts may depend on tools for correctness

---

## Examples

Typical tools may include:
- error explanation helpers
- diagnostics wrappers
- experimental UX improvements
- analysis or reporting helpers

All such tools remain outside the minimal core guarantees of xLaDe.