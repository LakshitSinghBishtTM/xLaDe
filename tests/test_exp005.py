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


def test_exp005_toml_records_toolchain_mismatch():
    """
    EXP-005 documents a toolchain mismatch.
    The toml should record the version actually used, not the upstream pin.
    """
    import tomllib

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    toml_path = os.path.join(repo_root, "experiments", "exp-005-lean4-courses", "experiment.toml")
    with open(toml_path, "rb") as f:
        config = tomllib.load(f)
    # We ran on v4.30.0, not the upstream v4.29.0
    assert config["lean_toolchain"] == "leanprover/lean4:v4.30.0"


def test_exp005_submodule_directory_exists(submodule_path):
    assert os.path.isdir(submodule_path), (
        f"Submodule not found: {submodule_path}\n" "Run: git submodule update --init --recursive"
    )


def test_exp005_submodule_is_not_empty(submodule_path):
    if not os.path.isdir(submodule_path):
        pytest.skip("Submodule not populated")
    contents = os.listdir(submodule_path)
    assert len(contents) > 0, "Submodule directory is empty"


def test_exp005_submodule_has_lakefile(submodule_path):
    if not os.path.isdir(submodule_path):
        pytest.skip("Submodule not populated")
    has_lakefile = os.path.isfile(os.path.join(submodule_path, "lakefile.lean")) or os.path.isfile(
        os.path.join(submodule_path, "lakefile.toml")
    )
    assert has_lakefile, "No lakefile found in submodule"


def test_exp005_submodule_has_lean_toolchain(submodule_path):
    if not os.path.isdir(submodule_path):
        pytest.skip("Submodule not populated")
    assert os.path.isfile(os.path.join(submodule_path, "lean-toolchain"))


def test_exp005_submodule_has_expected_structure(submodule_path):
    """lean4-courses should have numbered course directories."""
    if not os.path.isdir(submodule_path):
        pytest.skip("Submodule not populated")
    entries = os.listdir(submodule_path)
    course_dirs = [e for e in entries if e.startswith("000")]
    assert len(course_dirs) >= 10, f"Expected at least 10 course directories, found {len(course_dirs)}"


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
