import os

from xlade.cli.init import run


def test_init_creates_xlade_dir(tmp_project):
    run()
    assert os.path.isdir(".xlade")


def test_init_creates_experiments_lock(tmp_project):
    run()
    assert os.path.isfile(".xlade/experiments.lock")


def test_init_creates_last_run(tmp_project):
    run()
    assert os.path.isfile(".xlade/last-run")


def test_init_last_run_default_value(tmp_project):
    run()
    content = open(".xlade/last-run").read().strip()
    assert content == "none"


def test_init_idempotent(tmp_project, capsys):
    run()
    run()
    captured = capsys.readouterr()
    assert "already initialised" in captured.out
