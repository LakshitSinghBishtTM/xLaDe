import json
import os
import shutil

from xlade.cli.exitcodes import ExitCode

SEP = "-" * 100
COL_LABEL = 16
COL_TAG = 7  # "[error]" is longest tag at 7 chars


def _row(label, tag, message, hint=None):
    tag_str = f"[{tag}]"
    print(f"  {label:<{COL_LABEL}}  {tag_str:<{COL_TAG}}  {message}")
    if hint:
        indent = "  " + " " * COL_LABEL + "  " + " " * COL_TAG + "  "
        for line in hint:
            print(f"{indent}{line}")


def _info(label, message):
    """A row with no status tag, aligned with the tagged rows."""
    print(f"  {label:<{COL_LABEL}}  {'':<{COL_TAG}}  {message}")


def _section(title):
    print()
    print(f"  {title}")


def _check_dependencies():
    issues = 0

    # elan
    if shutil.which("elan"):
        _row("elan", "ok", "found")
    else:
        _row(
            "elan",
            "error",
            "not found",
            [
                "Install: curl https://elan.lean-lang.org/elan-init.sh -sSf | sh",
                "Then restart your shell and re-run xlade doctor.",
            ],
        )
        issues += 1

    # lake
    if shutil.which("lake"):
        _row("lake", "ok", "found")
    else:
        _row(
            "lake",
            "error",
            "not found",
            [
                "Install elan first, then:",
                "elan toolchain install leanprover/lean4:stable",
            ],
        )
        issues += 1

    # lean-toolchain
    if os.path.isfile("lean-toolchain"):
        toolchain = open("lean-toolchain").read().strip()
        _row("lean-toolchain", "ok", f"present  ({toolchain})")
    else:
        _row(
            "lean-toolchain",
            "error",
            "not found",
            ["Create it: echo 'leanprover/lean4:stable' > lean-toolchain"],
        )
        issues += 1

    return issues


def _read_text(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return f.read().strip() or default
    return default


def _check_state():
    issues = 0

    mode = _read_text(os.path.join(os.path.expanduser("~"), ".xlade", "mode"), "not set")

    # workspace
    if not os.path.isdir(".xlade"):
        _row("workspace", "warn", "not initialised", ["Run: xlade init"])
        _info("mode", mode)
        return issues

    _row("workspace", "ok", "initialised")
    _info("mode", mode)
    _info("last run", _read_text(os.path.join(".xlade", "last-run"), "none"))

    # run history
    metrics_path = os.path.join(".xlade", "metrics.json")
    if not os.path.isfile(metrics_path):
        _info("runs", "none recorded yet")
        return issues

    try:
        with open(metrics_path) as f:
            data = json.load(f)
    except json.JSONDecodeError, OSError:
        _row(
            "runs",
            "error",
            "metrics.json is corrupted",
            ["Delete .xlade/metrics.json to reset run history."],
        )
        return issues + 1

    if not data:
        _info("runs", "none recorded yet")
        return issues

    counts = {}
    for r in data:
        key = r.get("status", "unknown")
        counts[key] = counts.get(key, 0) + 1
    summary = ", ".join(f"{k}: {v}" for k, v in counts.items())
    _info("runs", f"{len(data)}  ({summary})")

    print()
    print("  Recent runs:")
    for r in data[-5:]:
        exp_id = r.get("experiment_id", "unknown")
        mode_ = r.get("mode", "")
        ts = r.get("timestamp", "")
        status = r.get("status", "unknown")
        print(f"    {exp_id:<38}  {mode_:<12}  {ts}  {status}")

    return issues


def run():
    print()

    _section("Dependencies")
    print(f"  {SEP}")
    issues = _check_dependencies()
    print()

    _section("State")
    print(f"  {SEP}")
    issues += _check_state()

    print()
    print(f"  {SEP}")

    if issues == 0:
        print("  All checks passed.")
    else:
        plural = "issue" if issues == 1 else "issues"
        print(f"  {issues} {plural} found. Fix above and re-run xlade doctor.")

    print()
    return ExitCode.OK if issues == 0 else ExitCode.ENVIRONMENT
