# Changelog

All notable changes to xLaDe are documented in this file.

This project follows semantic versioning where possible.
Early releases are experimental.

---

## [1.0.0] — 2025-12-31

### Highlights
- Initial public release of xLaDe.
- Established xLaDe as an experimental Lean 4 ecosystem framework.

### Added
- Core repository structure (`docs/`, `examples/`, etc.).
- Formal project documentation and README.
- Forked and integrated the official Lean 4 Theorem Prover as a submodule.
- Contribution guidelines and initial contributor list.
- GitHub project essentials:
  - issue templates
  - pull request templates
  - badges
  - `.gitignore`

### Notes
This release represents the foundational structure of xLaDe.
It is experimental and not intended for production use.

## [1.1.0] — 2026-01-24

### Highlights
- Transition from conceptual framework to enforceable ecosystem platform.
- Formalized experiments, modes, policies, and metrics as stable components.

### Added
- Experiment lifecycle and template.
- EXP-001: Enforced Proof Review (Lean-based policy).
- EXP-002: Kernel Boundary Violation Detection (CI-enforced).
- Build modes: onboarding, experimental, stable.
- Metrics framework for ecosystem-level evaluation.
- Repository-wide kernel protection via CI.
- Public-facing documentation for contributors and users.

### Changed
- README updated to reflect xLaDe as an executable ecosystem platform.
- Contribution workflow reoriented around experiments.

### Notes
This release stabilizes the xLaDe ecosystem framework.
All features remain experimental, but their structure and enforcement
mechanisms are considered stable.

## [1.2.0] — 2026-02-20

### Highlights
- License transitioned to **GNU General Public License v3.0 (GPL-3.0)**.
- Repository finalized as the reference version for the xLaDe research paper.

### Added
- Expanded architectural documentation and rationale.
- Clearer separation between trusted infrastructure and experimental layers.
- Additional governance and status documentation.
- Improved contributor-facing guidance.

### Changed
- README rewritten to reflect research-oriented scope and limitations.
- Documentation reorganized for clarity and traceability.
- Experiment layouts and metadata made more consistent.
- Policies and modes aligned with documented architecture.

### Notes
This release consolidates xLaDe’s structure and documentation.
It does not introduce new experiments or tooling features.
All components remain experimental, but architectural intent and
repository organization are considered stable for reference and citation.