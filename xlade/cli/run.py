import os
import time
import tomllib
from xlade.core.errors import error


def run(exp_id):
    # --------------------
    # Workspace check
    # --------------------
    if not os.path.isdir(".xlade"):
        error(
            "Workspace not initialized",
            "No .xlade directory found.",
            "Run `xlade init` in this project."
        )
        return

    # --------------------
    # Experiment path
    # --------------------
    exp_path = os.path.join("experiments", exp_id)
    if not os.path.isdir(exp_path):
        print(f"Experiment not found: {exp_id}")
        return

    # --------------------
    # Load experiment config
    # --------------------
    config_path = os.path.join(exp_path, "experiment.toml")
    if not os.path.exists(config_path):
        print(f"No experiment.toml found for {exp_id}")
        return

    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
    except Exception as e:
        print(f"Failed to parse experiment.toml: {e}")
        return

    # --------------------
    # Read current mode
    # --------------------
    home = os.path.expanduser("~")
    mode_file = os.path.join(home, ".xlade", "mode")

    current_mode = "unknown"
    if os.path.exists(mode_file):
        with open(mode_file) as f:
            current_mode = f.read().strip()

    # --------------------
    # Mode enforcement
    # --------------------
    allowed_modes = config.get("allowed_modes", [])
    if allowed_modes and current_mode not in allowed_modes:
        print(f"Experiment {exp_id} is not allowed in mode: {current_mode}")
        print(f"Allowed modes: {', '.join(allowed_modes)}")
        return

    # --------------------
    # Environment info
    # --------------------
    lean_toolchain = config.get("lean_toolchain", "unspecified")

    # --------------------
    # Execution (minimal as of now)
    # --------------------
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Save last run
    with open(".xlade/last-run", "w") as f:
        f.write(exp_id + "\n")

    # Output
    print(f"Running experiment: {exp_id}")
    print(f"Mode: {current_mode}")
    print(f"Required Lean: {lean_toolchain}")
    print(f"Timestamp: {timestamp}")

    print("Execution: simulated")
    print("Status: success")