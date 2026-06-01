import os
import json

SEP = "-" * 100


def run():
    home = os.path.expanduser("~")
    mode_file = os.path.join(home, ".xlade", "mode")

    mode = "not set"
    if os.path.exists(mode_file):
        with open(mode_file) as f:
            mode = f.read().strip()

    print()
    print("  xLaDe Status")
    print(f"  {SEP}")

    if not os.path.isdir(".xlade"):
        print(f"  Workspace   not initialised")
        print(f"  Mode        {mode}")
        print(f"  {SEP}")
        print("  Run 'xlade init' to initialise the workspace.")
        print()
        return

    last_run_file = os.path.join(".xlade", "last-run")
    last_exp = "none"
    if os.path.exists(last_run_file):
        with open(last_run_file) as f:
            last_exp = f.read().strip()

    print(f"  Workspace   initialised")
    print(f"  Mode        {mode}")
    print(f"  Last run    {last_exp}")

    metrics_path = os.path.join(".xlade", "metrics.json")

    if not os.path.isfile(metrics_path):
        print(f"  {SEP}")
        print("  No experiment runs recorded yet.")
        print("  Try: xlade run exp-002-kernel-boundary")
        print()
        return

    try:
        with open(metrics_path, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        print(f"  {SEP}")
        print("  [error]  metrics.json is corrupted.")
        print("           Delete .xlade/metrics.json to reset run history.")
        print()
        return

    if not data:
        print(f"  {SEP}")
        print("  No experiment runs recorded yet.")
        print()
        return

    total   = len(data)
    success = sum(1 for r in data if r.get("status") == "success")
    failed  = sum(1 for r in data if r.get("status") == "failed")
    skipped = sum(1 for r in data if r.get("status") == "skipped")
    other   = total - success - failed - skipped

    parts = [f"success: {success}"]
    if failed:
        parts.append(f"failed: {failed}")
    if skipped:
        parts.append(f"skipped: {skipped}")
    if other:
        parts.append(f"other: {other}")

    print(f"  {SEP}")
    print(f"  Runs        {total}  ({', '.join(parts)})")
    print()
    print("  Recent:")

    for r in data[-5:]:
        status = r.get("status", "unknown")
        exp_id = r.get("experiment_id", "unknown")
        ts     = r.get("timestamp", "")
        print(f"    {exp_id:<38}  {ts}  {status}")

    print()