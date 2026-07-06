import os

import pytest


@pytest.fixture
def tmp_project(monkeypatch, tmp_path):
    """Simulates a fresh xLaDe project directory."""
    monkeypatch.chdir(tmp_path)
    return tmp_path


@pytest.fixture
def initialized_project(tmp_project):
    """Project with .xlade/ already initialized."""
    xlade_dir = tmp_project / ".xlade"
    xlade_dir.mkdir()
    (xlade_dir / "experiments.lock").write_text("# Locked experiments\n")
    (xlade_dir / "last-run").write_text("none\n")
    return tmp_project


@pytest.fixture
def fake_home(monkeypatch, tmp_path):
    """Redirects ~/.xlade/ to a temp dir so tests don't touch real home."""
    fake = tmp_path / "home"
    fake.mkdir()
    monkeypatch.setenv("HOME", str(fake))
    monkeypatch.setattr(
        os.path,
        "expanduser",
        lambda p: str(fake) if p == "~" else os.path.join(str(fake), p[2:]),
    )
    return fake


@pytest.fixture
def experiments_dir(tmp_project):
    """Creates a minimal experiments/ directory with one valid experiment."""
    exp_dir = tmp_project / "experiments" / "EXP-001"
    exp_dir.mkdir(parents=True)
    (exp_dir / "experiment.toml").write_text(
        'id = "EXP-001"\n'
        'name = "Test Experiment"\n'
        'type = "script-policy"\n'
        'status = "active"\n'
        'allowed_modes = ["experimental"]\n'
        'lean_toolchain = "leanprover/lean4:stable"\n'
        'entry = "policy.lean"\n'
        'description = "A test experiment."\n'
    )
    return tmp_project
