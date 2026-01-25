import os
import time

def run(exp_id):
    if not os.path.isdir(".xlade"):
        print("xLaDe is not initialized. Run `xlade init` first.")
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
