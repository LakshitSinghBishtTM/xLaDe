import os
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
CHECK_SCRIPT = ROOT / "scripts" / "experiments" / "check-kernel.sh"


def git(repo, *args, check=True):
    return subprocess.run(
        ["git", *args], cwd=repo, check=check, text=True, capture_output=True
    )


def commit_all(repo, message):
    git(repo, "add", ".")
    git(repo, "commit", "-m", message)


def run_kernel_check(repo, base_ref):
    environment = {**os.environ, "KERNEL_BASE_REF": base_ref}
    return subprocess.run(
        ["bash", str(CHECK_SCRIPT)], cwd=repo, env=environment, text=True, capture_output=True
    )


@pytest.fixture
def kernel_project(tmp_path):
    kernel = tmp_path / "kernel"
    kernel.mkdir()
    git(kernel, "init", "-q")
    git(kernel, "config", "user.name", "Test User")
    git(kernel, "config", "user.email", "test@example.com")
    (kernel / "Kernel.lean").write_text("-- baseline\n")
    commit_all(kernel, "initial kernel")

    project = tmp_path / "project"
    project.mkdir()
    git(project, "init", "-q")
    git(project, "config", "user.name", "Test User")
    git(project, "config", "user.email", "test@example.com")
    (project / "README.md").write_text("test project\n")
    commit_all(project, "initial project")
    git(project, "-c", "protocol.file.allow=always", "submodule", "add", "-q", str(kernel), "lean-core")
    commit_all(project, "add kernel submodule")

    return project, git(project, "rev-parse", "HEAD").stdout.strip()


def test_clean_kernel_submodule_passes(kernel_project):
    project, baseline = kernel_project

    result = run_kernel_check(project, baseline)

    assert result.returncode == 0
    assert "Kernel untouched" in result.stdout


def test_missing_baseline_fails_closed(kernel_project):
    project, _ = kernel_project

    result = run_kernel_check(project, "missing-baseline")

    assert result.returncode == 1
    assert "Cannot verify baseline" in result.stdout


def test_changed_submodule_gitlink_fails(kernel_project):
    project, baseline = kernel_project
    submodule = project / "lean-core"
    (submodule / "Kernel.lean").write_text("-- changed\n")
    commit_all(submodule, "change kernel")
    git(project, "add", "lean-core")
    git(project, "commit", "-m", "update kernel revision")

    result = run_kernel_check(project, baseline)

    assert result.returncode == 1
    assert "submodule revision changed" in result.stdout


def test_uninitialized_submodule_fails_closed(kernel_project):
    project, baseline = kernel_project
    git(project, "submodule", "deinit", "-f", "lean-core")

    result = run_kernel_check(project, baseline)

    assert result.returncode == 1
    assert "not initialized" in result.stdout


def test_dirty_submodule_fails_even_if_git_is_configured_to_ignore_submodules(kernel_project):
    project, baseline = kernel_project
    (project / "lean-core" / "Kernel.lean").write_text("-- uncommitted change\n")
    git(project, "config", "diff.ignoreSubmodules", "all")

    result = run_kernel_check(project, baseline)

    assert result.returncode == 1
    assert "uncommitted changes" in result.stdout


def test_ci_workflows_pass_an_explicit_base_to_the_shared_check():
    for workflow_name in ("ci.yml", "kernel-protection.yml"):
        content = (ROOT / ".github" / "workflows" / workflow_name).read_text()

        assert "KERNEL_BASE_REF:" in content
        assert "github.event.pull_request.base.sha" in content
        assert "github.event.before" in content
        assert "fetch-depth: 0" in content

    assert "bash scripts/experiments/check-kernel.sh" in (
        ROOT / ".github" / "workflows" / "kernel-protection.yml"
    ).read_text()
