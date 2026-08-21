# Known Limitations

This document describes the current limitations of xLaDe. These are
honest statements about what the project cannot do right now — not
apologies, but useful information for anyone deciding whether xLaDe
fits their needs.

Some limitations are intentional design trade-offs. Some are deferred
work. All of them are acknowledged.

---

## Execution Limitations

**EXP-001 requires Lake.**
The Enforced Proof Review experiment uses `lake script run` and cannot
execute without a full Lean 4 + Lake installation via elan. On machines
without Lake, it reports `skipped` cleanly. EXP-002 and EXP-003 run on
any machine with bash.

**No parallel experiment execution.**
Experiments run sequentially. There is no scheduler, no queue, and no
support for running multiple experiments simultaneously.

**No experiment dependencies.**
Experiments cannot declare dependencies on other experiments. There is
no way to say "run EXP-001 before EXP-002" automatically.

**No incremental execution.**
Every `xlade run` executes the full experiment from scratch. There is
no caching or incremental build support.

---

## Compatibility Limitations

**No automated toolchain switching.**
xLaDe records the required Lean toolchain in `experiment.toml` but does
not yet automatically switch to it before running. If the installed Lean
version differs from what an experiment requires, the user must switch
manually via elan. Automated switching is planned for a future release.

**No compatibility warnings.**
`xlade check` does not yet detect Lean version mismatches between the
installed toolchain and what an experiment was validated against.
Compatibility tracking is planned for future versions.

**No backward compatibility guarantees.**
xLaDe itself makes no guarantees about backward compatibility between
versions. This is an experimental research tool — breaking changes may
occur at any release.

---

## Metrics Limitations

**Metrics are structural, not semantic.**
`metrics.json` records what ran, when, in what mode, and whether it
succeeded. It does not record proof content, tactic counts, elaboration
time, or any semantic information about the Lean proof itself.

**No aggregation or comparison tooling.**
There is no built-in way to compare metrics across experiments or across
runs of the same experiment over time. The JSON is human-readable and
can be processed externally.

**No dashboards.**
`xlade metrics` displays a table in the terminal. There is no web
interface, no visualisation, and no export to external monitoring tools.

---

## Experiment Limitations

**Three active experiments.**
As of v1.5.0, xLaDe has three active experiments. The experiment
framework is designed for more, but the current set is intentionally
small while the foundation stabilises.

**Experiments are policy-focused.**
Current experiments test structural and workflow policies — kernel
protection, proof review discipline, documentation coverage. There are
no performance benchmarks, no semantic proof analysis experiments, and
no cross-version comparison experiments yet.

**No experiment versioning.**
Experiments do not have internal version numbers. If an experiment
changes significantly, there is no mechanism to distinguish the old
version from the new one in the run history.

---

## Tooling Limitations

**No IDE integrations.**
There are no plugins for VS Code, Emacs, or any other editor. xLaDe
is a CLI tool only.

**No GUI.**
There is no graphical interface. All interaction is through the terminal.

**No multi-prover support.**
xLaDe currently supports Lean 4 only. Support for Coq, Isabelle, and
other proof assistants is a long-term research direction, not a near-term
feature.

**No AI integration.**
There is no language model integration of any kind. AI-assisted proof
diagnosis and translation are long-term research directions described in
[`research_roadmap.md`](docs/research_roadmap.md).

---

## Usage Limitations

**Not production grade.**
xLaDe is an experimental research tool. It is not suitable for
production use, critical infrastructure, or any context where stability
and reliability are required.

**No stability guarantees.**
Interfaces, file formats, and behaviour may change between releases
without notice. The `metrics.json` schema, `experiment.toml` fields,
and CLI output format are all subject to change.

**No support SLA.**
There is no guaranteed response time for issues or pull requests.
This is a research project maintained by a small team.

---

## What Is Not a Limitation

For clarity — the following are **intentional design decisions**, not
limitations:

- The Lean kernel is immutable — this is the core architectural constraint
- Experiments do not modify Lean semantics — this is by design
- The CLI has no hidden behaviour — explicit over convenient
- `xlade run` always writes to `metrics.json` — this is required for
  reproducibility

These will not change.