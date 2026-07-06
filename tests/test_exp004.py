import os
import stat
import subprocess

import pytest


@pytest.fixture
def script_path():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(repo_root, "scripts", "experiments", "run-exp-004.sh")


@pytest.fixture
def exp004_toml():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(
        repo_root, "experiments", "exp-004-project-proof-1", "experiment.toml"
    )


@pytest.fixture
def submodule_path():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(
        repo_root, "experiments", "exp-004-project-proof-1", "exp-004-project-proof-1"
    )


def test_exp004_script_exists(script_path):
    assert os.path.isfile(script_path), f"Script not found: {script_path}"


def test_exp004_script_is_executable(script_path):
    mode = os.stat(script_path).st_mode
    assert mode & stat.S_IEXEC, "Script is not executable"


def test_exp004_toml_exists(exp004_toml):
    assert os.path.isfile(exp004_toml)


def test_exp004_toml_has_required_fields(exp004_toml):
    import tomllib

    with open(exp004_toml, "rb") as f:
        config = tomllib.load(f)
    assert config["id"] == "EXP-004"
    assert config["type"] == "script-policy"
    assert config["status"] == "active"
    assert "experimental" in config["allowed_modes"]
    assert config["entry"] == "scripts/experiments/run-exp-004.sh"


def test_exp004_submodule_directory_exists(submodule_path):
    assert os.path.isdir(submodule_path), (
        f"Submodule not found: {submodule_path}\n"
        "Run: git submodule update --init --recursive"
    )


def test_exp004_submodule_is_not_empty(submodule_path):
    if not os.path.isdir(submodule_path):
        pytest.skip("Submodule not populated")
    contents = os.listdir(submodule_path)
    assert len(contents) > 0, "Submodule directory is empty"


def test_exp004_submodule_has_lakefile(submodule_path):
    if not os.path.isdir(submodule_path):
        pytest.skip("Submodule not populated")
    has_lakefile = os.path.isfile(
        os.path.join(submodule_path, "lakefile.lean")
    ) or os.path.isfile(os.path.join(submodule_path, "lakefile.toml"))
    assert has_lakefile, "No lakefile found in submodule"


def test_exp004_submodule_has_lean_toolchain(submodule_path):
    if not os.path.isdir(submodule_path):
        pytest.skip("Submodule not populated")
    assert os.path.isfile(os.path.join(submodule_path, "lean-toolchain"))


def test_exp004_script_fails_without_submodule(script_path, tmp_path):
    """Script should exit non-zero when project dir does not exist."""
    result = subprocess.run(
        ["bash", script_path],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "not found" in result.stdout or "not found" in result.stderr
