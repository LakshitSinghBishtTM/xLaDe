import os
import tomllib


def run():
    base_path = "experiments"

    if not os.path.isdir(base_path):
        print("  [error]  No experiments/ directory found.")
        print("           Make sure you are running from the xLaDe repository root.")
        return

    experiments = []

    for name in sorted(os.listdir(base_path)):
        exp_path = os.path.join(base_path, name)

        if not os.path.isdir(exp_path):
            continue

        config_path = os.path.join(exp_path, "experiment.toml")

        if not os.path.exists(config_path):
            continue

        try:
            with open(config_path, "rb") as f:
                config = tomllib.load(f)
        except Exception:
            experiments.append((name, "invalid", "unknown", "unknown"))
            continue

        exp_id = name
        status = config.get("status", "unknown")
        modes = config.get("allowed_modes", [])
        exp_type = config.get("type", "unknown")
        mode_str = ", ".join(modes) if modes else "none"

        experiments.append((exp_id, status, exp_type, mode_str))

    if not experiments:
        print("  No valid experiments found in experiments/")
        print("  See experiments/EXPERIMENT_TEMPLATE.md to add one.")
        return

    col_id = max(len(e[0]) for e in experiments)
    col_id = max(col_id, 10)
    sep = "-" * 100

    print()
    print(f"  Experiments  ({len(experiments)} found)")
    print(f"  {sep}")
    print(f"  {'Experiment':<{col_id}}  {'Status':<8}  {'Type':<16}  Modes")
    print(f"  {sep}")

    for exp_id, status, exp_type, modes in experiments:
        print(f"  {exp_id:<{col_id}}  {status:<8}  {exp_type:<16}  {modes}")

    print()
    print("  Run with: xlade run <experiment-id>")
    print()
