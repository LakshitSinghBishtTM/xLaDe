import os
import tomllib


def run():
    base_path = "experiments"

    if not os.path.isdir(base_path):
        print("No experiments directory found.")
        return

    print("Available experiments:\n")

    found = False

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
            print(f"{name}  [invalid config]")
            continue

        exp_id = config.get("id", name)
        status = config.get("status", "unknown")
        modes = config.get("allowed_modes", [])

        mode_str = ",".join(modes) if modes else "none"

        print(f"{exp_id}  {status}   [{mode_str}]")

        found = True

    if not found:
        print("No valid experiments found.")