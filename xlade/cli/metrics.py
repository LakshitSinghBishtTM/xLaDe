import json
import os

SEP = "-" * 100


def run():
    _show_run_history()


def _show_run_history():
    metrics_path = os.path.join(".xlade", "metrics.json")

    if not os.path.isdir(".xlade"):
        print()
        print("  [error]  Workspace not initialised. Run 'xlade init' first.")
        print()
        return

    if not os.path.isfile(metrics_path):
        print()
        print("  xlade metrics  --  no runs recorded yet")
        print("  Run an experiment with: xlade run <experiment-id>")
        print()
        return

    try:
        with open(metrics_path, "r") as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        print()
        print("  [error]  metrics.json is corrupted.")
        print("           Delete .xlade/metrics.json to reset run history.")
        print()
        return

    if not data:
        print()
        print("  xlade metrics  --  no runs recorded yet")
        print()
        return

    col_id = max((len(r.get("experiment_id", "")) for r in data), default=13)
    col_mode = max((len(r.get("mode", "")) for r in data), default=4)
    col_ts = max((len(r.get("timestamp", "")) for r in data), default=19)

    col_id = max(col_id, 10)
    col_mode = max(col_mode, 4)
    col_ts = max(col_ts, 19)

    print()
    print(f"  xLaDe Metrics  ({len(data)} run(s))")
    print(f"  {SEP}")
    print(
        f"  {'Experiment':<{col_id}}  {'Mode':<{col_mode}}  {'Timestamp':<{col_ts}}  Status"
    )
    print(f"  {SEP}")

    for r in data:
        status = r.get("status", "unknown")
        print(
            f"  {r.get('experiment_id', ''):<{col_id}}  "
            f"{r.get('mode', ''):<{col_mode}}  "
            f"{r.get('timestamp', ''):<{col_ts}}  "
            f"{status}"
        )

    print()
