"""
Tests for xlade.core.lean

These tests never require a real Lean or Lake installation.
They use monkeypatching and a tiny real bash binary (always present
in CI) to exercise both the capture and passthrough paths.
"""

import os
import stat
import pytest
from xlade.core.lean import (
    LeanResult,
    run_lake_script,
    run_lake_build,
    run_lean_file,
    run_script,
    lean_version,
    lake_version,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def pass_script(tmp_path):
    """A minimal bash script that exits 0."""
    s = tmp_path / "pass.sh"
    s.write_text("#!/bin/bash\necho 'ok'\nexit 0\n")
    s.chmod(s.stat().st_mode | stat.S_IEXEC)
    return str(s)


@pytest.fixture
def fail_script(tmp_path):
    """A minimal bash script that exits 1."""
    s = tmp_path / "fail.sh"
    s.write_text("#!/bin/bash\necho 'fail'\nexit 1\n")
    s.chmod(s.stat().st_mode | stat.S_IEXEC)
    return str(s)


@pytest.fixture
def no_lean(monkeypatch):
    """Patch shutil.which inside lean.py so lean and lake report as not found."""
    monkeypatch.setattr("xlade.core.lean.shutil.which", lambda x: None)


@pytest.fixture
def fake_lake(monkeypatch):
    """Patch shutil.which inside lean.py so lake is found but lean is not."""
    monkeypatch.setattr(
        "xlade.core.lean.shutil.which",
        lambda x: "/usr/bin/lake" if x == "lake" else None,
    )


@pytest.fixture
def fake_lean(monkeypatch):
    """Patch shutil.which inside lean.py so lean is found but lake is not."""
    monkeypatch.setattr(
        "xlade.core.lean.shutil.which",
        lambda x: "/usr/bin/lean" if x == "lean" else None,
    )


# ---------------------------------------------------------------------------
# LeanResult dataclass
# ---------------------------------------------------------------------------

def test_lean_result_truthy_when_success():
    r = LeanResult(success=True, returncode=0)
    assert r


def test_lean_result_falsy_when_failed():
    r = LeanResult(success=False, returncode=1)
    assert not r


def test_lean_result_default_fields():
    r = LeanResult(success=True)
    assert r.returncode == -1
    assert r.stdout == ""
    assert r.stderr == ""
    assert r.command == []


def test_lean_result_stores_command():
    r = LeanResult(success=True, command=["lake", "build"])
    assert r.command == ["lake", "build"]


# ---------------------------------------------------------------------------
# run_script — uses real bash (always available in CI)
# ---------------------------------------------------------------------------

def test_run_script_success(pass_script):
    result = run_script(pass_script, passthrough=False)
    assert result.success
    assert result.returncode == 0
    assert "ok" in result.stdout


def test_run_script_failure(fail_script):
    result = run_script(fail_script, passthrough=False)
    assert not result.success
    assert result.returncode == 1
    assert "fail" in result.stdout


def test_run_script_captures_stdout(pass_script):
    result = run_script(pass_script, passthrough=False)
    assert result.stdout.strip() == "ok"


def test_run_script_passthrough_returns_empty_stdout(pass_script):
    result = run_script(pass_script, passthrough=True)
    assert result.success
    assert result.stdout == ""   # passthrough — not captured


def test_run_script_missing_file():
    result = run_script("/nonexistent/path/script.sh", passthrough=False)
    assert not result.success


def test_run_script_command_recorded(pass_script):
    result = run_script(pass_script, passthrough=False)
    assert pass_script in result.command


def test_run_script_missing_entry_file():
    # Passing a path that does not exist goes through bash but fails
    # because the script file is not found — bash exits non-zero.
    result = run_script("/nonexistent/no_such_script.sh", passthrough=False)
    assert not result.success


# ---------------------------------------------------------------------------
# run_lake_script — lake not found
# ---------------------------------------------------------------------------

def test_run_lake_script_no_lake(no_lean):
    result = run_lake_script("enforceReview")
    assert not result.success
    assert "lake" in result.stderr


def test_run_lake_script_no_lake_returncode(no_lean):
    result = run_lake_script("enforceReview")
    assert result.returncode == -1


# ---------------------------------------------------------------------------
# run_lake_build — lake not found
# ---------------------------------------------------------------------------

def test_run_lake_build_no_lake(no_lean):
    result = run_lake_build()
    assert not result.success
    assert "lake" in result.stderr


# ---------------------------------------------------------------------------
# run_lean_file — lean not found
# ---------------------------------------------------------------------------

def test_run_lean_file_no_lean(no_lean):
    result = run_lean_file("some/file.lean")
    assert not result.success
    assert "lean" in result.stderr


# ---------------------------------------------------------------------------
# lean_version / lake_version — not found
# ---------------------------------------------------------------------------

def test_lean_version_no_lean(no_lean):
    result = lean_version()
    assert not result.success
    assert "lean" in result.stderr


def test_lake_version_no_lake(no_lean):
    result = lake_version()
    assert not result.success
    assert "lake" in result.stderr


def test_lean_version_command_field(no_lean):
    result = lean_version()
    assert "lean" in result.command


def test_lake_version_command_field(no_lean):
    result = lake_version()
    assert "lake" in result.command


# ---------------------------------------------------------------------------
# lean_version / lake_version — binary present (capture mode)
# ---------------------------------------------------------------------------

def test_lean_version_capture_returns_string(monkeypatch):
    monkeypatch.setattr("xlade.core.lean.shutil.which", lambda x: "/usr/bin/lean" if x == "lean" else None)
    monkeypatch.setattr("xlade.core.lean._run", lambda cmd, **kw: LeanResult(success=True, returncode=0, stdout="Lean (version 4.x.x)", command=cmd))
    result = lean_version(passthrough=False)
    assert isinstance(result, LeanResult)


def test_lake_version_capture_returns_string(monkeypatch):
    monkeypatch.setattr("xlade.core.lean.shutil.which", lambda x: "/usr/bin/lake" if x == "lake" else None)
    monkeypatch.setattr("xlade.core.lean._run", lambda cmd, **kw: LeanResult(success=True, returncode=0, stdout="Lake version 4.x.x", command=cmd))
    result = lake_version(passthrough=False)
    assert isinstance(result, LeanResult)

# ---------------------------------------------------------------------------
# bool convenience
# ---------------------------------------------------------------------------

def test_bool_true_result_in_conditional():
    r = LeanResult(success=True)
    assert r  # used as: if result: ...


def test_bool_false_result_in_conditional():
    r = LeanResult(success=False)
    assert not r