# xLaDe Overview

**xLaDe** is an experimental ecosystem framework built around **Lean 4**,
designed to enable controlled experimentation with tooling, developer
experience, and ecosystem-level ideas **without modifying Lean core**.

Rather than being a theorem library or a replacement for Lean, xLaDe acts as an
**orchestration layer**. It provides a structured way to run ecosystem
experiments, apply policies, collect metrics, and evolve user-facing ideas in a
reproducible and reviewable manner.

At its current stage, xLaDe is delivered as a **command-line application**
(`xlade`). This CLI-first approach establishes stable interfaces on top of which
richer execution engines, IDE integrations, and GUI-based tooling can be
developed in later stages.

---

## Project Vision

xLaDe aims to support a modern, flexible, and extensible Lean 4 ecosystem that
prioritizes **human-centered formal reasoning** and experimental innovation.

The long-term vision includes enabling users to:

- Write **human-readable proofs** supported by improved tactics  
- Receive **humanized error explanations** and corrective guidance  
- Experiment with **IDE and GUI-based tooling** for Lean 4  
- Explore **visual representations** of theorems and proofs  
- Integrate **AI and machine learning** for assisted theorem proving  
- Foster **community-driven collaboration and learning**  
- Support execution on **lightweight and mobile devices**  
- Enable **interoperability** with other proof assistants  
- Inform future **Lean language and tooling improvements**

xLaDe does not attempt to replace Lean or compete with its core development.
Instead, it provides a structured environment in which such ideas can be tested,
evaluated, and iterated upon before being proposed upstream.

---

## Current Status

xLaDe is in an **early but functional experimental stage**.

The repository currently provides:

- A **CLI application (`xlade`)** for ecosystem orchestration  
- Project-local and global **runtime state management**  
- Structured discovery and execution of **ecosystem experiments**  
- A non-fatal **policy checking framework**  
- Metrics discovery and reporting interfaces  
- Environment diagnostics and tooling checks  
- An immutable **Lean 4 core submodule** used as a reference baseline  
- Documentation, contribution guidelines, and a defined roadmap  

At this stage, several execution backends and analyses are intentionally
**stubbed or lightweight**. The focus is on establishing stable interfaces,
clear separation of concerns, and reproducible experimentation rather than
performance or completeness.

---

## Getting Involved

Contributions are welcome at all stages of the project. Interested contributors
can participate by:

- Proposing ideas or improvements via GitHub issues  
- Submitting pull requests for experiments, tooling, or documentation  
- Engaging in discussions around tactics, tooling, AI integration, and user
  experience  

For contribution guidelines, see [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## Roadmap

A detailed roadmap describing current, planned, and long-term development
stages is available in [`docs/roadmap.md`](./docs/roadmap.md).
