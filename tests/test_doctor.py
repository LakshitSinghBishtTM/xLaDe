import os
import shutil
import pytest
from xlade.cli.doctor import run


# -----------------------------------------------------------------------
# Existing tests — all original assertions preserved
# -----------------------------------------------------------------------

def test_doctor_detects_missing_lake(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: None)
    run()
    captured = capsys.readouterr()
    assert "lake not found" in captured.out


def test_doctor_detects_missing_lean_core(tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "lean-core missing" in captured.out


def test_doctor_detects_lean_toolchain(tmp_project, capsys):
    open("lean-toolchain", "w").write("leanprover/lean4:stable\n")
    run()
    captured = capsys.readouterr()
    assert "lean-toolchain present" in captured.out


def test_doctor_detects_lean_core_present(tmp_project, capsys):
    os.makedirs("lean-core")
    # populate so it is not treated as uninitialised
    open(os.path.join("lean-core", "README.md"), "w").write("lean\n")
    run()
    captured = capsys.readouterr()
    assert "lean-core submodule present" in captured.out


# -----------------------------------------------------------------------
# New tests — actionable guidance
# -----------------------------------------------------------------------

def test_doctor_lake_missing_shows_install_hint(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: None)
    run()
    captured = capsys.readouterr()
    assert "elan" in captured.out


def test_doctor_lean_core_empty_dir_shows_submodule_hint(tmp_project, capsys):
    os.makedirs("lean-core")   # exists but empty
    run()
    captured = capsys.readouterr()
    assert "lean-core missing" in captured.out
    assert "git submodule update" in captured.out


def test_doctor_lean_core_absent_shows_clone_hint(tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "lean-core missing" in captured.out
    assert "git submodule update" in captured.out


def test_doctor_lean_toolchain_missing_shows_hint(tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "lean-toolchain missing" in captured.out
    assert "leanprover/lean4:stable" in captured.out


def test_doctor_elan_missing_shows_curl_hint(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: None)
    run()
    captured = capsys.readouterr()
    assert "curl" in captured.out
    assert "elan-init.sh" in captured.out


def test_doctor_elan_found(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: "/usr/bin/elan" if x == "elan" else None)
    run()
    captured = capsys.readouterr()
    assert "elan found" in captured.out


def test_doctor_all_clear_shows_pass_summary(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: f"/usr/bin/{x}")
    os.makedirs("lean-core")
    open(os.path.join("lean-core", "README.md"), "w").write("lean\n")
    open("lean-toolchain", "w").write("leanprover/lean4:stable\n")
    run()
    captured = capsys.readouterr()
    assert "All checks passed" in captured.out


def test_doctor_issues_found_shows_count(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: None)
    run()
    captured = capsys.readouterr()
    assert "issues found" in captured.out


def test_doctor_workspace_not_init_shows_warning(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: f"/usr/bin/{x}")
    os.makedirs("lean-core")
    open(os.path.join("lean-core", "README.md"), "w").write("lean\n")
    open("lean-toolchain", "w").write("leanprover/lean4:stable\n")
    # no .xlade dir
    run()
    captured = capsys.readouterr()
    assert "workspace not initialised" in captured.out


def test_doctor_workspace_init_shows_ok(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: f"/usr/bin/{x}")
    os.makedirs("lean-core")
    open(os.path.join("lean-core", "README.md"), "w").write("lean\n")
    open("lean-toolchain", "w").write("leanprover/lean4:stable\n")
    os.makedirs(".xlade")
    run()
    captured = capsys.readouterr()
    assert "workspace initialised" in captured.out