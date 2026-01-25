# xLaDe Metrics

This directory defines the **metrics layer** of the xLaDe ecosystem.

Metrics in xLaDe are used to **observe, evaluate, and compare ecosystem-level
experiments**, rather than to benchmark Lean’s kernel or proof performance
directly.

They provide structured ways to reason about the impact of tooling, workflows,
policies, and user-facing changes explored through xLaDe experiments.

---

## Purpose of Metrics

The metrics framework is designed to answer questions such as:

- How does an experiment affect developer experience?
- Are errors becoming easier to understand or diagnose?
- Does a policy reduce friction or increase clarity?
- How do different workflows compare qualitatively?

Metrics are intended to support **analysis and reflection**, not enforcement.

---

## Scope and Philosophy

Metrics in xLaDe follow these principles:

- **Non-invasive**  
  Metrics do not alter Lean core or proof semantics.

- **Ecosystem-focused**  
  Metrics evaluate workflows, tooling, and user interaction patterns rather
  than kernel-level performance.

- **Non-fatal**  
  Missing or incomplete metrics never block experiments or execution.

- **Extensible**  
  New metrics can be introduced incrementally as experiments evolve.

---

## Directory Structure

The metrics directory may contain:

```text
metrics/
  README.md
  summary.md
  <metric-definition>.md
````

Metric definitions are intentionally lightweight and descriptive at this stage.
They may later be accompanied by structured data or automated collection tools.

---

## Relationship to Experiments

Metrics are tightly coupled to experiments but remain conceptually separate:

* **Experiments** propose and execute ideas
* **Metrics** observe and evaluate outcomes

An experiment may reference one or more metrics, but metrics themselves do not
encode experimental logic.

This separation allows metrics to remain stable even as experiments evolve.

---

## Current Status

At the current stage of xLaDe:

* Metrics are primarily **descriptive and qualitative**
* Collection and aggregation mechanisms are minimal or stubbed
* The emphasis is on defining *what should be measured*, not *how fast* or
  *how completely* it is measured

This is intentional and reflects the research-driven nature of the project.

---

## Future Directions

Planned extensions to the metrics layer include:

* Structured metric schemas
* Aggregation and comparison across experiment runs
* CLI-based reporting and summaries
* Export formats for research and evaluation

These extensions will be introduced without changing the existing CLI
interfaces.

---

## Research Status

All metrics should be considered **experimental**.

They are meant to guide discussion, evaluation, and iteration rather than serve
as definitive performance indicators.

Community contributions and suggestions for new metrics are welcome.
