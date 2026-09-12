import json
import os

import pytest

from xlade.cli.status import run


@pytest.fixture
def status_with_history(initialized_project, fake_home):
    mode_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(mode_dir, exist_ok=True)
    open(os.path.join(mode_dir, "mode"), "w").write("experimental\n")

    open(".xlade/last-run", "w").write("EXP-002\n")

    data = [
        {
            "experiment_id": "EXP-002",
            "experiment_name": "Kernel Boundary",
            "type": "script-policy",
            "mode": "experimental",
            "lean_toolchain": "leanprover/lean4:stable",
            "timestamp": "2026-05-22 14:20:09",
            "status": "success",
        }
    ]
    with open(".xlade/metrics.json", "w") as f:
        json.dump(data, f)

    return initialized_project


def test_status_shows_mode(status_with_history, capsys):
    run()
    captured = capsys.readouterr()
    assert "experimental" in captured.out


def test_status_shows_last_run(status_with_history, capsys):
    run()
    captured = capsys.readouterr()
    assert "EXP-002" in captured.out


def test_status_shows_total_runs(status_with_history, capsys):
    run()
    captured = capsys.readouterr()
    assert "Runs" in captured.out
    assert "1" in captured.out


def test_status_shows_success_count(status_with_history, capsys):
    run()
    captured = capsys.readouterr()
    assert "success" in captured.out


def test_status_no_init(tmp_project, fake_home, capsys):
    run()
    captured = capsys.readouterr()
    assert "not initialised" in captured.out


def test_status_corrupted_metrics(initialized_project, fake_home, capsys):
    open(".xlade/metrics.json", "w").write("{{bad")
    run()
    captured = capsys.readouterr()
    assert "corrupted" in captured.out
