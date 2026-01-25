# xLaDe Roadmap

xLaDe is developed in **explicit stages**, with a clear separation between
ecosystem orchestration, execution backends, and user-facing tooling.

This staged approach enables experimentation without destabilizing Lean core
or existing workflows.

---

## Stage 1 — Ecosystem Orchestration (Current)

✔ Implemented in v1

- CLI-based orchestration tool (`xlade`)
- Project initialization and runtime state management
- Experiment discovery and execution coordination
- Non-fatal policy checking framework
- Metrics discovery and reporting interfaces
- Environment diagnostics (`xlade doctor`)
- Lean 4 core isolation via submodules

At this stage, experiment execution and analysis backends are intentionally
minimal or stubbed. The emphasis is on **structure, interfaces, and
reproducibility**, rather than performance or completeness.

---

## Stage 2 — Execution and Analysis (Planned)

- Concrete execution engines for selected experiments
- Lean invocation and controlled result capture
- Structured metrics aggregation and reporting
- Policy enforcement driven by experiment outcomes
- Performance and usability evaluation

This stage will replace internal stubs while keeping the CLI interface stable.

---

## Stage 3 — Human-Centered Tooling (Future)

- Humanized and contextual error explanations
- Guided onboarding and learning modes
- IDE and GUI-based interfaces built on top of the CLI
- Visual representations of proofs and theorems
- Integration with educational workflows

---

## Stage 4 — Ecosystem Expansion (Long-Term)

- AI and machine learning integration for assisted reasoning
- Community-driven collaboration tools
- Support for lightweight and mobile environments
- Interoperability with other proof assistants
- Proposals for upstream Lean language and tooling improvements

---

## Notes

- The roadmap is intentionally **flexible** and research-driven.
- Community feedback and experimental results will guide prioritization.
