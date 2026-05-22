import json
import os
from xlade.cli.run import run

def test_run_writes_metrics_json(initialized_project, experiments_dir, fake_home):
    mode_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(mode_dir, exist_ok=True)
    open(os.path.join(mode_dir, "mode"), "w").write("experimental\n")

    run("EXP-001")

    metrics_path = ".xlade/metrics.json"
    assert os.path.isfile(metrics_path)

    with open(metrics_path) as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["experiment_id"] == "EXP-001"
    assert data[0]["mode"] == "experimental"
    assert "timestamp" in data[0]


def test_run_appends_multiple_runs(initialized_project, experiments_dir, fake_home):
    mode_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(mode_dir, exist_ok=True)
    open(os.path.join(mode_dir, "mode"), "w").write("experimental\n")

    run("EXP-001")
    run("EXP-001")

    with open(".xlade/metrics.json") as f:
        data = json.load(f)

    assert len(data) == 2


def test_run_metrics_survives_corrupt_json(initialized_project, experiments_dir, fake_home):
    mode_dir = os.path.join(os.path.expanduser("~"), ".xlade")
    os.makedirs(mode_dir, exist_ok=True)
    open(os.path.join(mode_dir, "mode"), "w").write("experimental\n")

    open(".xlade/metrics.json", "w").write("not valid json{{")

    run("EXP-001")

    with open(".xlade/metrics.json") as f:
        data = json.load(f)

    assert len(data) == 1