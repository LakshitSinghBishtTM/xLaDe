# xLaDe Modes

xLaDe modes define **alternative ways of running Lean within the xLaDe ecosystem**.

A mode represents a **development context** that influences how experiments, policies, and tooling are orchestrated — without modifying Lean’s kernel, compiler, or core semantics.
Modes exist to support different user intents, from learning to active research to conservative validation.

---

## What Modes Are (and Are Not)

### Modes **ARE**
- High-level ecosystem configurations
- A way to express **intent** (learning, experimentation, validation)
- A mechanism to:
  - enable or disable experiments
  - adjust policy enforcement
  - change warning and error behavior
  - Explicit and reversible

### Modes **ARE NOT**
- Forks of Lean
- Language-level feature toggles
- Performance profiles
- Changes to proof semantics or kernel behavior

Modes operate strictly at the **orchestration and policy layer**.

---

## Available Modes

xLaDe currently supports three modes:

### `onboarding`
**Learning-oriented, minimal enforcement**

- Builds only curated or minimal examples
- Avoids strict policy enforcement
- Emits helpful, human-readable messages
- Optimized for exploration and first-time use

**Intended for:**
- New Lean users
- First-time xLaDe contributors
- Educational and teaching contexts

**Stability:**  
Low — convenience is prioritized over guarantees.

---

### `experimental`
**Active ecosystem experimentation**

- Enables selected ecosystem experiments
- Policies may emit warnings or fail builds
- Behavior may change frequently
- No backward compatibility guarantees

**Intended for:**
- Researchers
- Tooling developers
- Contributors testing new workflows

**Stability:**  
Unstable — experimentation takes precedence.

---

### `stable`
**Conservative, policy-driven usage**

- Disables all ecosystem experiments
- Enforces strict repository policies
- Prioritizes reproducibility and predictability
- Minimizes behavioral changes over time

**Intended for:**
- Long-term contributors
- Validation and review
- Downstream or reference usage

**Stability:**  
High — behavior changes are minimized.

---

## Mode Selection

The active mode is set globally via:

```bash
xlade mode <onboarding|experimental|stable>
````

The selected mode is stored in:

```text
~/.xlade/mode
```

Modes can be changed at any time and do not require rebuilding Lean or modifying
project source files.

---

## Experiments and Modes

Ecosystem experiments are **selectively enabled** depending on the active mode.

By default:

* **Experimental mode** enables experiments
* **Stable mode** disables all experiments
* **Onboarding mode** disables all experiments

The set of enabled experiments for Experimental Mode is declared explicitly
(e.g. via `enabled-experiments.md`) and serves as a single source of truth.

---

## Design Rationale

The mode system allows xLaDe to:

* support diverse user goals without fragmentation
* isolate experimental behavior from stable workflows
* make expectations explicit and reviewable
* evolve tooling safely without destabilizing Lean usage

Modes provide **clarity and control**, not hidden behavior.

---

## Summary

xLaDe modes define **how the ecosystem behaves**, not how Lean works.

They:

* communicate intent,
* control experiment activation,
* shape policy enforcement,
* and preserve kernel immutability.

This design enables disciplined ecosystem experimentation while maintaining clear boundaries and predictable behavior.
