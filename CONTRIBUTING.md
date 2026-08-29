# Contributing to xLaDe

xLaDe is an experimental research project. Contributions at all levels
are welcome — experiments, documentation, tooling, tests, bug reports,
and research feedback.

---

## What You Can Contribute

**Experiments** — the most valuable contribution. A new experiment means
a new research question being investigated. See
[Proposing an Experiment](#proposing-an-experiment) below.

**Documentation** — improvements to any file in `docs/`, the root-level
docs, or inline code comments. Accuracy matters more than volume.

**Code** — CLI improvements, new commands, test coverage, bug fixes.
All code contributions must pass the existing test suite and include
tests for new behaviour.

**Bug reports** — clear, reproducible reports are genuinely useful.
See [Reporting Issues](#reporting-issues).

**Research feedback** — if you work with Lean 4 or formal verification
and have thoughts on xLaDe's direction, open a GitHub Discussion.

---

## Ground Rules

- **Do not modify `lean-core/`**. This is enforced by CI and any PR
  touching the Lean submodule will be rejected. This is not negotiable.
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
- Keep pull requests focused. One concern per PR.
- Write clear commit messages. Describe what changed and why, not just what.

---

## Development Setup

```sh
git clone --recurse-submodules https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
python3 -m venv venv
source venv/bin/activate
pip install -e .
pip install pytest
pytest tests/ -v
```

All tests should pass before you start making changes. If they do not,
check [`docs/INSTALL.md`](docs/INSTALL.md) or open an issue.

---

## Making a Contribution

**1. Fork the repository**

Fork on GitHub, then clone your fork:

```sh
git clone https://github.com/your-username/xLaDe.git
cd xLaDe
git remote add upstream https://github.com/LakshitSinghBishtTM/xLaDe.git
```

**2. Create a branch**

```sh
git checkout -b your-branch-name
```

Use a descriptive name — `fix-doctor-elan-check`, `add-exp-004-tactic-coverage`,
`docs-update-runtime-state`.

**3. Make your changes**

- Code changes must include tests
- Documentation changes should be accurate and consistent with the
  current version
- Experiment additions must follow the structure in
  [`experiments/EXPERIMENT_TEMPLATE.md`](experiments/EXPERIMENT_TEMPLATE.md)

**4. Run the test suite**

```sh
pytest tests/ -v
```

All tests must pass. If you added new behaviour, add tests for it.

**5. Commit**

```sh
git commit -m "Short description of what and why"
```

**6. Push and open a pull request**

```sh
git push origin your-branch-name
```

Open a PR against `main`. In the description include:

- What the change does
- Why it is needed
- Any known limitations or follow-up work
- Reference any related issue with `#issue-number`

---

## Proposing an Experiment

Experiments are the primary research artifacts of xLaDe. Adding one
means proposing a research question, not just writing a script.

Before opening a PR, open a GitHub Issue describing:

- The research question or hypothesis
- What the experiment would enforce or measure
- What type it would be (`script-policy`, `lean-policy`, etc.)
- How it would be evaluated
- Exit criteria — when would it be promoted or abandoned

Once the direction is agreed, create the experiment directory following
[`experiments/EXPERIMENT_TEMPLATE.md`](experiments/EXPERIMENT_TEMPLATE.md).
The directory name is the experiment ID — choose it carefully, it cannot
be changed without breaking run history.

---

## Reporting Issues

Use [GitHub Issues](https://github.com/LakshitSinghBishtTM/xLaDe/issues)
for bug reports, feature requests, and documentation problems.

A useful bug report includes:

- xLaDe version (`cat VERSION`)
- Python version (`python --version`)
- OS and platform
- The exact command that failed
- Full output including any error messages
- What you expected to happen

For security issues, do not open a public issue.
See [`SECURITY.md`](SECURITY.md).

---

## Code of Conduct

All contributors are expected to follow the
[Code of Conduct](CODE_OF_CONDUCT.md).

---

## Notes

xLaDe is experimental. Interfaces change between versions. If you are
building on top of xLaDe or integrating it into another tool, be aware
that no stability guarantees are made before v2.0.0.

Contributions do not need to be production-ready. This is a research
project — exploratory, partial, and honest work is welcome.
