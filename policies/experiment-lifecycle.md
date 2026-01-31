# Experiment Lifecycle Policy

This document defines the **lifecycle model** followed by all xLaDe experiments.

The lifecycle exists to ensure that ecosystem experiments remain:
- explicit,
- reviewable,
- reversible,
- and historically traceable.

Experiments are treated as **research artifacts**, not permanent features.

---

## Lifecycle States

Every xLaDe experiment must be in exactly one of the following states.

### 1. Draft

**Purpose:**  
Exploration and proposal.

**Characteristics:**
- Experiment is under development or discussion
- Enforcement may be incomplete or absent
- Not enabled by default in any mode

**Typical use:**
- Prototyping an idea
- Gathering feedback
- Clarifying scope and risks

---

### 2. Active

**Purpose:**  
Controlled evaluation.

**Characteristics:**
- Experiment has a defined:
  - enforcement mechanism
  - scope
  - reversibility plan
  - exit criteria
- May be enabled in **Experimental Mode**
- Subject to observation and metrics

**Typical use:**
- Testing ecosystem hypotheses
- Evaluating workflow or policy impact

---

### 3. Abandoned

**Purpose:**  
Historical record.

**Characteristics:**
- Experiment is no longer active
- Not enabled in any mode
- Documentation is preserved

**Rationale:**
- Prevents loss of design context
- Allows future researchers to understand:
  - what was tried
  - why it failed or was retired

---

### 4. Promoted

**Purpose:**  
Stabilization or upstreaming.

**Characteristics:**
- Experiment has demonstrated value
- Core ideas may be:
  - generalized into policies
  - integrated into tooling
  - proposed upstream
- The experiment itself may be retired or frozen

Promotion does **not** imply modification of the Lean kernel.

---

## Required Experiment Documentation

Every experiment must document:

- **Enforcement Mechanism**  
  How the experiment is applied (Lean code, scripts, CI, etc.)

- **Scope**  
  Which files, directories, or workflows are affected

- **Reversibility**  
  How the experiment can be disabled or removed

- **Exit Criteria**  
  Conditions under which the experiment is:
  - promoted
  - abandoned
  - revised

---

## Enforcement of the Lifecycle

The experiment lifecycle is enforced **primarily through documentation and review**.

At the current stage:
- Lifecycle state is declared explicitly by the experiment
- CI does not automatically enforce state transitions
- Human review ensures consistency and correctness

This reflects xLaDe’s research-first and non-invasive philosophy.

---

## Relationship to Modes

- **Experimental Mode**  
  May enable experiments in the **Active** state

- **Stable and Onboarding Modes**  
  Must not enable Draft, Active, or Abandoned experiments

Lifecycle state and mode selection are **orthogonal but coordinated**.

---

## Summary

The experiment lifecycle policy ensures that ecosystem experimentation in xLaDe
remains:

- disciplined,
- reversible,
- transparent,
- and historically grounded.

By making experiment status explicit, xLaDe avoids both premature stabilization and silent abandonment of ideas.
