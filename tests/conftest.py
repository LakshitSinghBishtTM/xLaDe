import os
import subprocess
import sys
from pathlib import Path

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


# --- New-suite helpers ---------------------------------------------------------
# Everything below serves the layered suite in tests/{unit,integration,system,static}.
# The fixtures above are kept as-is for the legacy test files in tests/.

TESTS_DIR = Path(__file__).resolve().parent
LAYERS = ("unit", "integration", "system", "static")


def pytest_collection_modifyitems(items):
    """Mark each test with its layer, taken from the folder it lives in."""
    for item in items:
        try:
            layer = item.path.resolve().relative_to(TESTS_DIR).parts[0]
        except ValueError, IndexError:
            continue
        if layer in LAYERS:
            item.add_marker(getattr(pytest.mark, layer))


@pytest.fixture
def isolated_home(monkeypatch, tmp_path):
    """A throwaway HOME so nothing reads or writes the real ~/.xlade."""
    home = tmp_path / "home"
    home.mkdir()
    monkeypatch.setenv("HOME", str(home))
    return home


@pytest.fixture
def xlade_cli(isolated_home, tmp_path):
    """Run the real `xlade` console script in a subprocess.

    Returns run(*args, cwd=None) -> CompletedProcess. The script is looked up
    next to the running interpreter, so the test exercises the installed entry
    point rather than importing the package directly.
    """
    exe = Path(sys.executable).parent / "xlade"
    if not exe.exists():
        pytest.skip("xlade console script is not installed in this environment")

    workdir = tmp_path / "work"
    workdir.mkdir()

    def run(*args, cwd=None):
        return subprocess.run(
            [str(exe), *args],
            cwd=cwd or workdir,
            capture_output=True,
            text=True,
            env={**os.environ, "HOME": str(isolated_home)},
            timeout=60,
            check=False,
        )

    return run
