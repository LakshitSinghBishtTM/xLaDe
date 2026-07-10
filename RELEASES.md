# xLaDe Releases

This file mirrors GitHub Releases for archival and offline reference.

---

## v1.0.0 - 2025-12-31

### Highlights
- Created the open-source project on GitHub.
- Added core folders and essential files.
- Updated project with formal content and README.
- Forked and integrated the official Lean 4 Theorem Prover repository.
- Added contribution guidelines and listed initial contributors.
- Set up GitHub essentials:
  - issue templates
  - PR templates
  - badges
  - `.gitignore`

## v1.1.0 - 2026-01-24

### Highlights
- xLaDe ecosystem framework is now operational and enforceable.
- Executable ecosystem experiments (EXP-001, EXP-002).
- Mode-based usage (onboarding, experimental, stable).
- CI-backed governance and kernel protection.
- Qualitative metrics for experiment evaluation.

## v1.2.0 - 2026-02-20

### Highlights
- License changed to **GNU General Public License v3.0 (GPL-3.0)**.
- Repository structure refined to reflect architectural boundaries.
- Documentation significantly expanded and clarified.
- README rewritten for clarity and architectural context.
- Policies, experiments, and modes aligned with documented design intent.
- Improved consistency across experiment layouts and metadata.
- Updated governance and contributor-facing files.

## v1.3.0 - 2026-03-31

### Highlights
- Added a few examples for support in further experiments.
- Modified and improved documents regarding prerequisites of xLaDe, its use, contributions and README.
- Made the official site of xLaDe, available at "http://xladeajfgkh32qgq5sj2mtmho3te5pivto7lav44dsbov6uduciz6hqd.onion/". 
- Clarification added regarding why an onion site was chosen instead of a random site, along with other documents.
- Added a dedicated folder for security instead of adding files directly in root folder, added two new documents
- Imported project to GitLab for long-term availability and usefulness. Added mirror list for officially supported mirrors.

## v1.4.0 - 2026-04-27

### Highlights
- Added .toml for recording metadata in each experiment
- Modified CLI tool for running experiments
- Added and configured mirrors to sync automatically (sourceforge remaining)
- Restructured tools section for future modifications
- Regular improvements in docs for updated info

## v1.5.0 - 2026-05-26

### Highlights
- xlade is now pip-installable via pyproject.toml
- 50-test pytest suite, all passing
- EXP-002 executes check-kernel.sh for real
- EXP-003 (doc coverage) added and executable
- metrics.json written and displayed on every run
- xlade metrics and xlade status show real run history
- errors.py duplication removed
- CODE_OF_CONDUCT.md contact filled in
- ROADMAP.md added covering v1.5.0 to v2.0.0

## v1.6.0 - 2026-06-01

### Highlights
- xlade doctor completely overhauled, now it works with actions
- CLI output made like a real CLI tool
- 83-test suite, all passing on Python 3.11-3.14
- Verified working on Android aarch64 (Termux)
- Full CI/CD pipeline added 
- All GitHub workflows updated with least-privilege permissions per CodeQL
- 14 documentation files rewritten to accurately reflect v1.6.0
- RELEASE_CHECKLIST.md added

## v1.7.0 - 2026-07-11

### Highlights
- EXP-004: Project Proof 1 added under `experiments/`.
- EXP-005: Lean4 Courses added under `experiments/`.
- Added EXP-004 and EXP-005 experiment content and documentation.
- Strengthened code quality checks and release automation.
- Tightened CI to the supported Python version and kept the Lean submodule out of repo-wide linting.
- Cleaned up packaging and repository hygiene after formatting passes.
- `README.md` updated to document experiments.
- Automated sourceforce sync