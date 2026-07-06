import json

import pytest

from xlade.cli.metrics import run


@pytest.fixture
def with_run_history(initialized_project):
    data = [
        {
            "experiment_id": "EXP-001",
            "experiment_name": "Enforced Proof Review",
            "type": "lean-policy",
            "mode": "experimental",
            "lean_toolchain": "leanprover/lean4:stable",
            "timestamp": "2026-05-22 10:00:00",
            "status": "simulated",
        },
        {
            "experiment_id": "EXP-002",
            "experiment_name": "Kernel Boundary",
            "type": "script-policy",
            "mode": "experimental",
            "lean_toolchain": "leanprover/lean4:stable",
            "timestamp": "2026-05-22 10:05:00",
            "status": "success",
        },
    ]
    with open(".xlade/metrics.json", "w") as f:
        json.dump(data, f)
    return initialized_project


def test_metrics_no_init(tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "not initialised" in captured.out


def test_metrics_no_runs(initialized_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "no runs recorded" in captured.out


def test_metrics_shows_experiment_ids(with_run_history, capsys):
    run()
    captured = capsys.readouterr()
    assert "EXP-001" in captured.out
    assert "EXP-002" in captured.out


def test_metrics_shows_status(with_run_history, capsys):
    run()
    captured = capsys.readouterr()
    assert "success" in captured.out


def test_metrics_shows_run_count(with_run_history, capsys):
    run()
    captured = capsys.readouterr()
    assert "2 run" in captured.out


def test_metrics_shows_research_artifacts(with_run_history, tmp_project, capsys):
    run()
    captured = capsys.readouterr()
    assert "EXP-001" in captured.out
    assert "EXP-002" in captured.out


def test_metrics_corrupted_json(initialized_project, capsys):
    open(".xlade/metrics.json", "w").write("{{not json")
    run()
    captured = capsys.readouterr()
    assert "corrupted" in captured.out
