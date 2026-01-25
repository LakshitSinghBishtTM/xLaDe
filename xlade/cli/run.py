import os
import time
from xlade.core.errors import error

def run(exp_id):
    if not os.path.isdir(".xlade"):
        error(
        "Workspace not initialized",
        "No .xlade directory found.",
        "Run `xlade init` in this project."
        )
        return

    exp_path = os.path.join("experiments", exp_id)
    if not os.path.isdir(exp_path):
        print(f"Experiment not found: {exp_id}")
        return

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(".xlade/last-run", "w") as f:
        f.write(exp_id + "\n")

    print(f"Running experiment {exp_id}")
    print(f"Timestamp: {timestamp}")
    print("Status: completed (stub)")
