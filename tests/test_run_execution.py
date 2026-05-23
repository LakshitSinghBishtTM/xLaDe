import os
import json
import stat
import pytest
from xlade.cli.run import run


@pytest.fixture
def exp_with_script(initialized_project, fake_home):
    exp_dir = initialized_project / "experiments" / "EXP-SCRIPT"
    exp_dir.mkdir(parents=True)

    (exp_dir / "experiment.toml").write_text(
        'id = "EXP-SCRIPT"\n'
        'name = "Script Test"\n'
        'type = "script-policy"\n'
        'status = "active"\n'
        'allowed_modes = ["experimental"]\n'
        'lean_toolchain = "leanprover/lean4:stable"\n'
        'entry = "scripts/pass.sh"\n'
        'description = "Test script execution."\n'
    )

    scripts_dir = initialized_project / "scripts"
    scripts_dir.mkdir(exist_ok=True)

    pass_script = scripts_dir / "pass.sh"
    pass_script.write_text("#!/bin/bash\necho 'policy check passed'\nexit 0\n")
    pass_script.chmod(pass_script.stat().st_mode | stat.S_IEXEC)

    mode_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(mode_dir, exist_ok=True)
    open(os.path.join(mode_dir, "mode"), "w").write("experimental\n")

    return initialized_project


@pytest.fixture
def exp_with_failing_script(initialized_project, fake_home):
    exp_dir = initialized_project / "experiments" / "EXP-FAIL"
    exp_dir.mkdir(parents=True)

    (exp_dir / "experiment.toml").write_text(
        'id = "EXP-FAIL"\n'
        'name = "Failing Script Test"\n'
        'type = "script-policy"\n'
        'status = "active"\n'
        'allowed_modes = ["experimental"]\n'
        'lean_toolchain = "leanprover/lean4:stable"\n'
        'entry = "scripts/fail.sh"\n'
        'description = "Test failing script."\n'
    )

    scripts_dir = initialized_project / "scripts"
    scripts_dir.mkdir(exist_ok=True)

    fail_script = scripts_dir / "fail.sh"
    fail_script.write_text("#!/bin/bash\necho 'violation detected'\nexit 1\n")
    fail_script.chmod(fail_script.stat().st_mode | stat.S_IEXEC)

    mode_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(mode_dir, exist_ok=True)
    open(os.path.join(mode_dir, "mode"), "w").write("experimental\n")

    return initialized_project


def test_script_execution_success(exp_with_script, capsys):
    run("EXP-SCRIPT")
    captured = capsys.readouterr()
    assert "Status: success" in captured.out


def test_script_execution_records_success_in_metrics(exp_with_script):
    run("EXP-SCRIPT")
    with open(".xlade/metrics.json") as f:
        data = json.load(f)
    assert data[0]["status"] == "success"


def test_script_execution_failure(exp_with_failing_script, capsys):
    run("EXP-FAIL")
    captured = capsys.readouterr()
    assert "Status: failed" in captured.out


def test_script_execution_records_failure_in_metrics(exp_with_failing_script):
    run("EXP-FAIL")
    with open(".xlade/metrics.json") as f:
        data = json.load(f)
    assert data[0]["status"] == "failed"


def test_missing_entry_script(initialized_project, fake_home, capsys):
    exp_dir = initialized_project / "experiments" / "EXP-MISSING"
    exp_dir.mkdir(parents=True)
    (exp_dir / "experiment.toml").write_text(
        'id = "EXP-MISSING"\n'
        'name = "Missing Script"\n'
        'type = "script-policy"\n'
        'status = "active"\n'
        'allowed_modes = ["experimental"]\n'
        'lean_toolchain = "leanprover/lean4:stable"\n'
        'entry = "scripts/nonexistent.sh"\n'
        'description = "Missing entry."\n'
    )
    mode_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(mode_dir, exist_ok=True)
    open(os.path.join(mode_dir, "mode"), "w").write("experimental\n")

    run("EXP-MISSING")
    captured = capsys.readouterr()
    assert "not found" in captured.out

def test_lean_policy_without_lake(initialized_project, fake_home, capsys, monkeypatch):
    exp_dir = initialized_project / "experiments" / "EXP-LEAN"
    exp_dir.mkdir(parents=True)
    (exp_dir / "experiment.toml").write_text(
        'id = "EXP-LEAN"\n'
        'name = "Lean Policy Test"\n'
        'type = "lean-policy"\n'
        'status = "active"\n'
        'allowed_modes = ["experimental"]\n'
        'lean_toolchain = "leanprover/lean4:stable"\n'
        'entry = "policy.lean"\n'
        'description = "Test lean policy without lake."\n'
    )

    mode_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(mode_dir, exist_ok=True)
    open(os.path.join(mode_dir, "mode"), "w").write("experimental\n")

    monkeypatch.setattr("shutil.which", lambda x: None)

    run("EXP-LEAN")
    captured = capsys.readouterr()
    assert "lake not found" in captured.out

def test_lean_policy_records_skipped_in_metrics(initialized_project, fake_home, monkeypatch):
    exp_dir = initialized_project / "experiments" / "EXP-LEAN2"
    exp_dir.mkdir(parents=True)
    (exp_dir / "experiment.toml").write_text(
        'id = "EXP-LEAN2"\n'
        'name = "Lean Policy Test 2"\n'
        'type = "lean-policy"\n'
        'status = "active"\n'
        'allowed_modes = ["experimental"]\n'
        'lean_toolchain = "leanprover/lean4:stable"\n'
        'entry = "policy.lean"\n'
        'description = "Test lean policy skipped."\n'
    )

    mode_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(mode_dir, exist_ok=True)
    open(os.path.join(mode_dir, "mode"), "w").write("experimental\n")

    monkeypatch.setattr("shutil.which", lambda x: None)

    run("EXP-LEAN2")

    with open(".xlade/metrics.json") as f:
        data = json.load(f)
    assert data[0]["status"] == "skipped"