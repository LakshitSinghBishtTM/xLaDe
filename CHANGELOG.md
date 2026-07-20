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
- Added project on GitLab at "https://gitlab.com/lakshitsinghbishttm/xLaDe". Both GitHub and GitLab versions will be synced.

### Added
- Rationale behind choosing an onion site for xLaDe.
- New examples of Lean to try in xLaDe.
- Dedicated security folder.

### Changed
- Docs to focus on the xLaDe functioning, limitations, contributions and README.

### Notes
This monthly release focuses mainly on organization and official site of xLaDe and its integration with GitHub repo instead of major code changes. xLaDe still is in its experimental stage.

## [1.4.0] — 2026-04-27

### Highlights
- Added metadata for each experiment to support backward compatibility in the future (ongoing long-term idea)
- Modified CLI tool to run experiments

### Added
- Mirrors to support decentralization and reduce redundancy
- Structured tools module
- Docs explaining roadmap regarding backward compatibility

### Notes
This monthly release makes the CLI tool execute experiments, but the testing of the xLaDe CLI hasn't been done properly, so problems may occur.

## [1.5.0] — 2026-05-26

### Highlights
- CLI becomes real and xlade is now a properly installable Python package
- 50-test pytest suite added, all passing on Python 3.14
- EXP-002 and EXP-003 now execute for real instead of simulating
- metrics.json written on every run, read by xlade metrics and xlade status

### Added
- tests/ directory with 50 tests across 8 modules (test_init, test_mode,
  test_run, test_run_execution, test_doctor, test_check,
  test_list_experiments, test_metrics, test_status, test_exp003)
- pyproject.toml — proper Python packaging, xlade installs via pip
- tests/conftest.py with fixture isolation (tmp_project, initialized_project,
  fake_home, experiments_dir)
- _write_metrics() in run.py — appends structured JSON record on every run
- _execute() in run.py — dispatches script-policy experiments to bash,
  lean-policy experiments to lake with graceful fallback if lake not found
- xlade metrics — aligned run history table with status symbols
- xlade status — run summary with success/fail counts and recent runs
- EXP-003: Documentation Coverage Check — scripts/check-doc-coverage.sh
- experiments/exp-001-proof-review/Proofs/Reviewed.lean
- ROADMAP.md — v1.5.0 through v2.0.0 release plan
- docs/AI_use.md — AI usage policy for contributors

### Changed
- run.py now writes metrics.json on every run with experiment_id, mode,
  lean_toolchain, timestamp, status
- run.py now executes script-policy experiments via subprocess
- run.py lean-policy branch: runs lake script enforceReview if lake present,
  records skipped if lake not found
- xlade/cli/errors.py now re-exports from xlade/core/errors.py
- xlade metrics reads from .xlade/metrics.json not just metrics/ directory
- xlade status shows full run summary from .xlade/metrics.json
- CODE_OF_CONDUCT.md contact method filled in
- .gitignore cleaned up and expanded
- modes/experimental/enabled-experiments.md updated to include EXP-003

### Notes
- EXP-001 execution remains skipped without Lake installed — requires
  Lean 4 toolchain (addressed in v1.6.0)
- CLI is functional and tested but still experimental
- 50/50 tests passing on Python 3.14

## [1.6.0] — 2026-06-01

### Highlights
- CLI output completely overhauled — consistent [tag] style, 100-char separators, 2-space indent
- 83-test suite, all passing on Python 3.11–3.14 and verified on FreeBSD and Android aarch64 (Termux)
- Full CI/CD pipeline — ci.yml runs experiments end to end, cd.yml automates GitHub releases

### Added
- xlade/core/lean.py — LeanResult dataclass, run_lake_script, run_lake_build, run_lean_file,
  run_script, lean_version, lake_version with capture/passthrough modes
- tests/test_lean_core.py — 33 tests covering all lean.py functions
- .github/workflows/ci.yml — integration workflow running experiments on every push and PR
- .github/workflows/cd.yml — release workflow triggered on version tags
- .github/workflows/kernel-protection.yml — renamed from xlade-ci.yml, cleaner output
- docs/RELEASE_CHECKLIST.md — all version bump locations and release steps in one place
- bin/README.md — explains why bin/xlade exists and when to use it
- security/SECURITY.md rewritten — PGP key, response timeline, scope, disclosure policy

### Changed
- xlade/cli/doctor.py — elan check added, actionable fix hints for all failing checks,
  aligned [tag] columns, pass/fail summary line
- xlade/cli/run.py — _execute() delegates to xlade/core/lean.py, elan install hint on skip
- xlade/cli/main.py — bare xlade shows full form, version, license, website; --help structured
- xlade/cli/init.py — shows created files and next steps on success
- xlade/cli/mode.py — numbered feature list per mode after separator
- xlade/cli/list_experiments.py — aligned table with type column, run count footer
- xlade/cli/check.py — [tag] format with hints, explicit all-clear output
- xlade/cli/status.py — structured sections, run summary with counts
- xlade/cli/metrics.py — aligned table, research artifacts section removed
- All workflows — permissions: contents: read added per CodeQL recommendation
- mirror.yml — [warn] style on push failures
- tests/test_doctor.py, test_check.py, test_init.py, test_list_experiments.py,
  test_metrics.py, test_mode.py, test_status.py — updated assertions for new output strings
- tests/test_run_execution.py — patch targets fixed to xlade.core.lean.shutil.which
- docs/CLI_DEMO.md — full rewrite, accurate command reference with real output
- docs/END_TO_END_TRACE.md — full rewrite, all three experiments, real terminal output
- docs/overview.md, architecture.md, WHY_xLaDe.md, RUNTIME_STATE.md,
  roadmap.md, research_roadmap.md, RESEARCH_SCOPE.md,
  REPRODUCIBILITY_AND_COMPATIBILITY.md — all rewritten for v1.6.0
- INSTALL.md — full rewrite, step-by-step elan → lean → lake, platform notes
- LIMITATIONS.md — expanded with honest per-limitation explanations
- HOW_TO_READ_THIS_REPO.md — updated reading order and file guidance
- README.md — full rewrite, professional, logo, name origin removed, problems first
- CONTRIBUTING.md — experiment proposal process, development setup, security redirect
- security/SECURITY_POLICY.md, THREAT_MODEL.md, TRUST_MODEL.md — all rewritten

### Notes
- EXP-001 execution requires Lake — skips cleanly without it
- CLI output strings changed significantly — any tooling parsing xlade output needs updating
- xlade-ci.yml deleted — replaced by kernel-protection.yml and ci.yml
- Verified working on FreeBSD and Android aarch64 (Termux) — pip install and all bash experiments run

## [1.7.0] — 2026-07-11

### Highlights
- Added EXP-004 and EXP-005 experiment content and documentation.
- Strengthened code quality checks and release automation.
- Tightened CI to the supported Python version and kept the Lean submodule out of repo-wide linting.
- Cleaned up packaging and repository hygiene after formatting passes.

### Added
- Automated sync to sourceforge mirror
- `.github/workflows/formatting.yml` — automated formatting checks in CI.
- `.flake8` — repository-level flake8 configuration.
- `experiments/exp-004-project-proof-1/README.md` — EXP-004: Project Proof 1.
- `projects/externals/exp-005-lean4-courses/README.md` — EXP-005: Lean4 Courses.

### Changed
- `.github/workflows/ci.yml`, `cd.yml`, `pypi.yml`, `tests.yml` — pinned to Python 3.14.
- `.gitignore` — simplified to keep only local, repository-specific entries.
- `pyproject.toml` — excluded the Lean submodule from Black checks and adjusted formatting settings.
- `pyproject.toml` and `.flake8` — aligned linting and formatting rules with the current codebase.
- `assets/logo/xlade-logo.svg` — polished logo geometry and path naming.
- `README.md` — updated to document experiment 5.
- `tests/` and `xlade/` files touched by the formatter — normalized formatting only, no functional change.

### Notes
- No new user-facing CLI features were added in this batch.
- The Lean submodule is now explicitly excluded from automatic formatting and checks to avoid touching upstream code.

## [Unreleased]

### Changed
- `scripts/experiments/run-exp-005.sh` now uses the EXP-005 submodule's
  committed Lean toolchain (`leanprover/lean4:v4.29.0`) instead of overwriting
  `lean-toolchain` with v4.30.0.
