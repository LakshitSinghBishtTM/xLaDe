import os

from xlade.cli.doctor import run


def test_doctor_detects_missing_lake(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: None)
    run()
    captured = capsys.readouterr()
    assert "lake" in captured.out
    assert "not found" in captured.out


def test_doctor_detects_lean_toolchain(tmp_project, capsys):
    open("lean-toolchain", "w").write("leanprover/lean4:stable\n")
    run()
    captured = capsys.readouterr()
    assert "lean-toolchain" in captured.out
    assert "present" in captured.out


def test_doctor_lake_missing_shows_install_hint(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: None)
    run()
    captured = capsys.readouterr()
    assert "elan" in captured.out


def test_doctor_lean_toolchain_missing_shows_hint(tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "lean-toolchain" in captured.out
    assert "leanprover/lean4:stable" in captured.out


def test_doctor_elan_missing_shows_curl_hint(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: None)
    run()
    captured = capsys.readouterr()
    assert "curl" in captured.out
    assert "elan-init.sh" in captured.out


def test_doctor_elan_found(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr(
        "xlade.core.lean.shutil.which",
        lambda x: "/usr/bin/elan" if x == "elan" else None,
    )
    monkeypatch.setattr("shutil.which", lambda x: "/usr/bin/elan" if x == "elan" else None)
    run()
    captured = capsys.readouterr()
    assert "elan" in captured.out
    assert "[ok]" in captured.out


def test_doctor_all_clear_shows_pass_summary(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: f"/usr/bin/{x}")
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
    open("lean-toolchain", "w").write("leanprover/lean4:stable\n")
    run()
    captured = capsys.readouterr()
    assert "not initialised" in captured.out
    assert "[warn]" in captured.out


def test_doctor_workspace_init_shows_ok(tmp_project, capsys, monkeypatch):
    monkeypatch.setattr("shutil.which", lambda x: f"/usr/bin/{x}")
    open("lean-toolchain", "w").write("leanprover/lean4:stable\n")
    os.makedirs(".xlade")
    run()
    captured = capsys.readouterr()
    assert "workspace" in captured.out
    assert "initialised" in captured.out
    assert "[ok]" in captured.out
