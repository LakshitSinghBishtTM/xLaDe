import os
import json


def run():
    print("xLaDe Status\n")

    # --------------------
    # Mode
    # --------------------
    home = os.path.expanduser("~")
    mode_file = os.path.join(home, ".xlade", "mode")

    mode = "unknown"
    if os.path.exists(mode_file):
        with open(mode_file) as f:
            mode = f.read().strip()

    print(f"Mode: {mode}")

    # --------------------
    # Workspace check
    # --------------------
    if not os.path.isdir(".xlade"):
        print("\nxLaDe is not initialized in this directory.")
        return

    # --------------------
    # Last run
    # --------------------
    last_run_file = os.path.join(".xlade", "last-run")

    last_exp = "none"
    if os.path.exists(last_run_file):
        with open(last_run_file) as f:
            last_exp = f.read().strip()

    print(f"Last experiment: {last_exp}")

    # --------------------
    # Metrics
    # --------------------
    metrics_file = os.path.join(".xlade", "metrics.json")

    if not os.path.exists(metrics_file):
        print("\nNo experiment runs recorded yet.")
        return

    try:
        with open(metrics_file, "r") as f:
            data = json.load(f)
    except Exception:
        print("\nMetrics file is corrupted or unreadable.")
        return

    if not data:
        print("\nNo experiment runs recorded yet.")
        return

    total_runs = len(data)
    last_run = data[-1]

    print(f"\nTotal runs: {total_runs}")
    print(f"Last run time: {last_run.get('timestamp', 'unknown')}")