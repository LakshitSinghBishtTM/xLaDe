import os

from xlade.cli.mode import run


def test_mode_sets_valid_mode(tmp_project, fake_home):
    run("experimental")
    mode_file = os.path.join(os.path.expanduser("~"), ".xlade", "mode")
    assert open(mode_file).read().strip() == "experimental"


def test_mode_stable(tmp_project, fake_home):
    run("stable")
    mode_file = os.path.join(os.path.expanduser("~"), ".xlade", "mode")
    assert open(mode_file).read().strip() == "stable"


def test_mode_onboarding(tmp_project, fake_home):
    run("onboarding")
    mode_file = os.path.join(os.path.expanduser("~"), ".xlade", "mode")
    assert open(mode_file).read().strip() == "onboarding"


def test_mode_invalid_prints_error(tmp_project, fake_home, capsys):
    run("invalid_mode")
    captured = capsys.readouterr()
    assert "not a valid mode" in captured.out


def test_mode_creates_xlade_home_dir(tmp_project, fake_home):
    run("stable")
    assert os.path.isdir(os.path.join(os.path.expanduser("~"), ".xlade"))
