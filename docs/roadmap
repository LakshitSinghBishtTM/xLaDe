# xLaDe Research Roadmap

This document describes the **long-term research vision** for xLaDe.

Unlike [`roadmap.md`](roadmap.md), which covers engineering releases with
specific version numbers and monthly targets, this document has no version
numbers and no deadlines. These are research directions — some may take
years, some may never happen, and some may lead somewhere unexpected.

The goal of writing this down is not to make promises. It is to be honest
about where xLaDe is trying to go over a 5–10 year horizon, and to give
contributors and researchers a sense of the bigger picture.

---

## 1. Reproducible Experiment Environments

**The problem:** Lean 4 evolves fast. An experiment that runs today may
not run next year. This is the core motivation behind xLaDe and the first
long-term research direction.

**The vision:** Given any xLaDe experiment — even one written three years
ago — `xlade run` should be able to reconstruct the exact environment it
was written in (Lean toolchain version, dependencies, build configuration)
and execute it correctly. No manual setup. No guessing. The metadata
recorded at write time is sufficient to reproduce the execution at any
point in the future.

**What needs to happen:**
- Full compatibility metadata in `experiment.toml`
- Automated toolchain switching via elan based on experiment metadata
- Compatibility matrix tracking which experiments run on which Lean versions
- Archive format for retired experiments — nothing deleted, everything
  traceable and re-runnable

This is the most technically grounded research direction and the one most
likely to produce results that are useful beyond xLaDe itself.

---

## 2. Human-Readable Proof Workflows

**The problem:** Lean proofs are not readable by people who haven't spent
months learning Lean syntax and type theory. This limits who can review,
understand, and build on formal proofs — even people who understand the
underlying mathematics.

**The vision:** xLaDe experiments that translate Lean proofs into
human-readable explanations. Not summaries — actual step-by-step
derivations in plain language that a mathematician unfamiliar with Lean
could follow and verify.

**What this could look like:**

```sh
xlade translate exp-001-proof-review
```

Produces a human-readable document explaining what the proof does, what
each tactic step accomplishes, and what the result means — without
requiring the reader to know Lean.

**Why this matters:** Formal verification is only useful if people can
trust the proofs. Trust requires readability. Right now, only a small
community can read Lean proofs. Expanding that community requires better
translation tooling.

---

## 3. AI Integration

**The problem:** Debugging Lean proofs is hard. Error messages are often
cryptic. Finding the right tactic is often trial and error. This creates
friction that discourages people from using formal verification even when
they should.

**The vision:** xLaDe as an orchestration layer for AI-assisted proof
work. Not replacing the proof assistant, but sitting alongside it —
reading experiment output, diagnosing failures, suggesting fixes, and
explaining what went wrong in plain language.

**What this could look like:**

```sh
xlade run claude
xlade claude "check exp-001 and tell me what's wrong"
xlade translate exp-004
```

The AI integration would read the experiment state, the `metrics.json`
run history, the Lean output, and the source files — and respond with
actionable guidance. The `LeanResult` dataclass already captures the
structured output needed to feed into an AI tool effectively.

**Important constraint:** AI integration in xLaDe would never modify
proofs automatically. The role of AI here is diagnostic and explanatory,
not generative. A proof is either correct or it is not — that determination
stays with the Lean kernel, not a language model.

---

## 4. Multi-Prover Support

**The problem:** xLaDe is built around Lean 4, but the ecosystem problems
it addresses — backward compatibility, kernel drift, reproducibility — are
not unique to Lean. Coq, Isabelle, Agda, and F* face versions of the same
problems.

**The vision:** xLaDe as a prover-agnostic ecosystem framework. An
experiment could specify which prover it uses:

```toml
prover = "coq"
toolchain = "8.19.0"
type = "coq-policy"
entry = "scripts/check.v"
```

And `xlade run` would dispatch accordingly.

**Cross-prover experiments** become possible — the same theorem proved in
Lean, Coq, and Isabelle, with xLaDe tracking execution, metrics, and
environment metadata for all three. That is publishable research on proof
assistant ergonomics and ecosystem maturity.

**Realistic timeline:**
- Coq — feasible earlier, opam is well-behaved, `coqc` is a normal CLI tool
- Isabelle — harder, non-standard session/heap model, later
- Agda, F* — closer to Lean in behaviour, probably easier than Isabelle

---

## 5. Community Infrastructure

**The problem:** xLaDe currently has no community space. Issues and pull
requests on GitHub work for contributions but not for open-ended research
discussion, questions, or collaboration.

**The vision:** A forum or discussion space — likely hosted on the onion
site — where researchers, students, and contributors can discuss
experiments, share findings, propose ideas, and collaborate across
institutions without depending on centralized platforms.

**Why the onion site:** Consistent with xLaDe's minimal-trust distribution
philosophy. A forum that lives on GitHub Discussions is controlled by
GitHub. A forum on the onion site is controlled by the project. For a
research tool that explicitly documents its trust model and threat model,
this matters.

---

## 6. IDE and GUI Tooling

**The problem:** The CLI is the right foundation but not the right surface
for all users. Researchers who are not comfortable with the terminal are
excluded from using xLaDe, even if the underlying ideas are relevant to
their work.

**The vision:** GUI tooling built on top of the stable CLI — not replacing
it, but wrapping it. A VS Code extension that runs `xlade doctor` on
project open and shows results inline. A web interface for browsing
experiment history. A visual dashboard for `xlade metrics`.

The CLI-first design makes this possible without rewriting anything — the
GUI layer just calls CLI commands and formats the output.

---

## 7. Lean Language and Tooling Proposals

**The problem:** Good ideas developed in xLaDe have nowhere to go unless
they can be proposed upstream in a form the Lean core team will take
seriously.

**The vision:** xLaDe as a pipeline for upstream proposals. Experiments
that succeed and prove their value in xLaDe become documented proposals
for Lean itself — with evidence, metrics, and a track record of working
in practice. Not speculative feature requests, but validated ideas backed
by experimental data.

This is the intended end state for the most successful xLaDe experiments.
An experiment is not promoted until it has run, been evaluated, and
demonstrated clear value. By the time it reaches the Lean core team, it
is no longer a proposal — it is a report.

---

## Notes

This document will be updated as the project evolves. Some of these
directions will prove more tractable than others. Some will lead somewhere
unexpected. That is the nature of research.

The engineering roadmap for the next release cycle is in
[`roadmap.md`](roadmap.md). This document is for the longer view.

xLaDe is estimated to reach general usability around v4.5 at the current
release cadence — approximately three years from v1.5.0. The directions
described here are the ones that will define what "usable" means by then.