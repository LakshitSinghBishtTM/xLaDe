import os

sep = "-" * 100


def run():
    root = os.getcwd()
    state_dir = os.path.join(root, ".xlade")

    if os.path.exists(state_dir):
        print("  [warn]  Workspace already initialised in this directory.")
        print("          Location: .xlade/")
        return

    os.mkdir(state_dir)

    with open(os.path.join(state_dir, "experiments.lock"), "w") as f:
        f.write("# Locked experiments\n")

    with open(os.path.join(state_dir, "last-run"), "w") as f:
        f.write("none\n")

    print()
    print("  Workspace initialised.")
    print(f"  {sep}")
    print("  Created  .xlade/experiments.lock")
    print("  Created  .xlade/last-run")
    print(f"  {sep}")
    print("  Next:  xlade mode experimental")
    print()
