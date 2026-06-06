import os
import time
import json
import tomllib
from xlade.core.errors import error
from xlade.core import lean

SEP = "-" * 100


def run(exp_id):
    if not os.path.isdir(".xlade"):
        print("  [error]  Workspace not initialised.")
        print("           Run 'xlade init' in this project.")
        return

    exp_path = os.path.join("experiments", exp_id)
    if not os.path.isdir(exp_path):
        print(f"  [error]  Experiment not found: {exp_id}")
        print("           Run 'xlade list experiments' to see available experiments.")
        return

    config_path = os.path.join(exp_path, "experiment.toml")
    if not os.path.exists(config_path):
        print(f"  [error]  No experiment.toml found for {exp_id}")
        return

    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
    except Exception as e:
        print(f"  [error]  Failed to parse experiment.toml: {e}")
        return

    home = os.path.expanduser("~")
    mode_file = os.path.join(home, ".xlade", "mode")

    current_mode = "unknown"
    if os.path.exists(mode_file):
        with open(mode_file) as f:
            current_mode = f.read().strip()

    allowed_modes = config.get("allowed_modes", [])
    if allowed_modes and current_mode not in allowed_modes:
        print(f"  [error]  Experiment '{exp_id}' is not allowed in mode: {current_mode}")
        print(f"           Allowed modes: {', '.join(allowed_modes)}")
        return

    lean_toolchain = config.get("lean_toolchain", "unspecified")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    exp_type = config.get("type", "unknown")
    entry = config.get("entry", None)

    print()
    print(f"  Running experiment: {exp_id}")
    print(f"  Mode:      {current_mode}")
    print(f"  Toolchain: {lean_toolchain}")
    print(f"  Timestamp: {timestamp}")
    print(f"  {SEP}")

    status = _execute(exp_type, entry, exp_path)

    print(f"  {SEP}")
    print(f"  Status: {status}")
    print()

    with open(".xlade/last-run", "w") as f:
        f.write(exp_id + "\n")

    _write_metrics(exp_id, current_mode, lean_toolchain, timestamp, config, status)


def _execute(exp_type, entry, exp_path):
    if exp_type == "script-policy" and entry:
        if not os.path.isfile(entry):
            print(f"  [error]  Entry script not found: {entry}")
            return "error"

        result = lean.run_script(entry, passthrough=True)
        return "success" if result else "failed"

    if exp_type == "lean-policy" and entry:
        result = lean.run_lake_script("enforceReview", cwd=exp_path, passthrough=True)
        if not result.success and "not found on PATH" in result.stderr:
            print("  [skip]  lake not found -- cannot run lean-policy experiment.")
            print("          Install Lean 4 and Lake via elan:")
            print("          curl https://elan.lean-lang.org/elan-init.sh -sSf | sh")
            return "skipped"
        return "success" if result else "failed"

    print("  Execution: simulated (no entry point defined)")
    return "simulated"


def _write_metrics(exp_id, mode, lean_toolchain, timestamp, config, status):
    metrics_path = os.path.join(".xlade", "metrics.json")

    existing = []
    if os.path.exists(metrics_path):
        try:
            with open(metrics_path, "r") as f:
                existing = json.load(f)
        except (json.JSONDecodeError, IOError):
            existing = []

    entry = {
        "experiment_id":   exp_id,
        "experiment_name": config.get("name", exp_id),
        "type":            config.get("type", "unknown"),
        "mode":            mode,
        "lean_toolchain":  lean_toolchain,
        "timestamp":       timestamp,
        "status":          status,
    }

    existing.append(entry)

    with open(metrics_path, "w") as f:
        json.dump(existing, f, indent=2)