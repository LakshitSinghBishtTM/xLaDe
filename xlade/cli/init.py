import os

def run():
    root = os.getcwd()
    state_dir = os.path.join(root, ".xlade")

    if os.path.exists(state_dir):
        print("xLaDe already initialized in this directory.")
        return

    os.mkdir(state_dir)

    with open(os.path.join(state_dir, "experiments.lock"), "w") as f:
        f.write("# Locked experiments\n")

    with open(os.path.join(state_dir, "last-run"), "w") as f:
        f.write("none\n")

    print("Initialized xLaDe workspace.")
