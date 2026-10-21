import os
import stat
import subprocess

import pytest


@pytest.fixture
def script_path():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(repo_root, "scripts", "experiments", "run-exp-005.sh")


@pytest.fixture
def exp005_toml():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(repo_root, "experiments", "exp-005-lean4-courses", "experiment.toml")


@pytest.fixture
def submodule_path():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(repo_root, "experiments", "exp-005-lean4-courses", "lean4-courses")


def test_exp005_script_exists(script_path):
    assert os.path.isfile(script_path), f"Script not found: {script_path}"


def test_exp005_script_is_executable(script_path):
    mode = os.stat(script_path).st_mode
    assert mode & stat.S_IEXEC, "Script is not executable"


def test_exp005_toml_exists(exp005_toml):
    assert os.path.isfile(exp005_toml)


def test_exp005_toml_has_required_fields(exp005_toml):
    import tomllib

    with open(exp005_toml, "rb") as f:
        config = tomllib.load(f)
    assert config["id"] == "EXP-005"
    assert config["type"] == "script-policy"
    assert config["status"] == "active"
    assert "experimental" in config["allowed_modes"]
    assert config["entry"] == "scripts/experiments/run-exp-005.sh"
    assert config["project_repo"] == "https://github.com/BaDaaS/lean4-courses"


def test_exp005_submodule_directory_exists(submodule_path):
    assert os.path.isdir(submodule_path), (
        f"Submodule not found: {submodule_path}\n" "Run: git submodule update --init --recursive"
    )


def test_exp005_script_fails_without_submodule(script_path, tmp_path):
    """Script should exit non-zero when project dir does not exist."""
    result = subprocess.run(
        ["bash", script_path],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "not found" in result.stdout or "not found" in result.stderr
