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
- License changed to GNU General Public License v3.0 (GPL-3.0).
- Documentation changes

### Added
- Expanded architectural documentation and rationale.
- Clearer separation between trusted infrastructure and experimental layers.
- Additional governance and status documentation.
- Improved contributor-facing guidance.

### Changed
- README rewritten to reflect scope and limitations.
- Documentation reorganized for clarity and traceability.
- Experiment layouts and metadata made more consistent.
- Policies and modes aligned with documented architecture.

### Notes
This release consolidates xLaDe’s structure and documentation.
It does not introduce new experiments or tooling features.
All components remain experimental.

## [1.3.0] — 2026-03-31

### Highlights
- Made a functioning official site of xLaDe available at "http://xladeajfgkh32qgq5sj2mtmho3te5pivto7lav44dsbov6uduciz6hqd.onion/"
- Added project on gitlab at "https://gitlab.com/lakshitsinghbishttm/xLaDe". Both github and gitlab versions will be synced.

### Added
- Rationale behind choosing an onion site for xLaDe.
- New examples of lean to try in xlade.
- Dedicated security folder.

### Changed
- Docs to focus on the xlade functioning, limitations, contributions and readme.

### Notes
This monthly release focuses mainly on organisation and official site of xLaDe and its integration with github repo instead of major code changes. xLaDe still is in its experimental stage.

## [1.4.0] — 2026-04-27

### Highlights
- Added metadata for each experiment to support backward compatibility in future (ongoing long term idea)
- Modified cli tool to run experiments

### Added
- Mirrors to support decentralisation and reduce redundancy
- Structured tools module
- Docs explaining roadmap regarding backward compatibility

### Notes
This monthly release makes cli tool execute experiments, but the testing of xlade cli hasn't been done properly, so problems may occur.