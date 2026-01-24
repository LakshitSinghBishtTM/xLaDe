## Why xLaDe?

Lean has developed a strong and rapidly growing ecosystem for formalization and verification, supported by an active community, mature libraries, and robust tooling. Most Lean-based projects naturally focus on **formal content**: proving theorems, verifying algorithms, and extending libraries such as mathlib.

However, **ecosystem-level experimentation** involving workflows, governance, repository structure, and contributor practices—often lacks a **safe, explicit, and well-documented space**. Such experiments are difficult to conduct directly in upstream repositories, where stability, backward compatibility, and community coordination are critical concerns.

xLaDe exists to address this gap.

xLaDe provides:

- **Isolation for ecosystem experiments**  
  A controlled environment where ideas about workflows, policies, tooling, and organization can be explored without risking disruption to upstream Lean repositories or established community practices.

- **Explicit architectural boundaries**  
  Clear separation between what must remain stable (e.g., the Lean kernel) and what is safe to experiment with (e.g., repository layout, governance mechanisms, development workflows). These boundaries are documented and, where possible, enforced.

- **A reproducible experimentation platform**  
  By pinning toolchains and dependencies, xLaDe ensures that experiments can be repeated, reviewed, and discussed meaningfully over time, rather than existing as one-off prototypes.

- **A place to test ideas before upstreaming**  
  xLaDe allows ideas to mature through iteration and community feedback before they are proposed for inclusion in upstream projects, reducing friction and improving the quality of proposals.

- **Transparency and documentation of design decisions**  
  Experiments in xLaDe are treated as first-class artifacts, with documented motivation, scope, limitations, and evaluation criteria. This makes it easier to understand not only *what* was tried, but *why* and *with what effect*.

In short, xLaDe is not about replacing Lean or redefining its foundations.  
It is about **creating a disciplined, open laboratory** for exploring how Lean-based development itself can evolve.
