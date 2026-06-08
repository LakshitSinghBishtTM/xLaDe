import os
import stat
import subprocess
import pytest


@pytest.fixture
def repo_with_docs(tmp_path):
    """Minimal repo structure that passes doc coverage check."""
    for exp in ["exp-001", "exp-002", "exp-003"]:
        d = tmp_path / "experiments" / exp
        d.mkdir(parents=True)
        (d / "README.md").write_text(f"# {exp}\n")

    for mode in ["onboarding", "experimental", "stable"]:
        d = tmp_path / "modes" / mode
        d.mkdir(parents=True)
        (d / "README.md").write_text(f"# {mode}\n")

    policies = tmp_path / "policies"
    policies.mkdir()
    (policies / "kernel-protection.md").write_text("# Kernel Protection\n")

    return tmp_path


@pytest.fixture
def script_path():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(repo_root, "scripts", "experiments", "check-doc-coverage.sh")


def test_passes_complete_repo(repo_with_docs, script_path):
    result = subprocess.run(
        ["bash", script_path],
        cwd=repo_with_docs,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "All documentation checks passed" in result.stdout


def test_fails_missing_experiment_readme(repo_with_docs, script_path):
    missing = repo_with_docs / "experiments" / "exp-004"
    missing.mkdir()

    result = subprocess.run(
        ["bash", script_path],
        cwd=repo_with_docs,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "Missing README.md" in result.stdout


def test_fails_missing_mode_readme(repo_with_docs, script_path):
    broken = repo_with_docs / "modes" / "broken"
    broken.mkdir()

    result = subprocess.run(
        ["bash", script_path],
        cwd=repo_with_docs,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "Missing README.md" in result.stdout


def test_fails_empty_policies(repo_with_docs, script_path):
    for f in (repo_with_docs / "policies").iterdir():
        f.unlink()

    result = subprocess.run(
        ["bash", script_path],
        cwd=repo_with_docs,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "No .md files" in result.stdout


def test_actual_repo_passes(script_path):
    """The real xLaDe repo should pass its own doc coverage check."""
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    result = subprocess.run(
        ["bash", script_path],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Real repo failed doc coverage:\n{result.stdout}"
    )