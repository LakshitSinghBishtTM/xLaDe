import os
import shutil

SEP = "-" * 100


def run():
    project_local = ".xlade"
    global_state = os.path.join(os.path.expanduser("~"), ".xlade")

    deleted = []
    not_found = []

    print()
    print("  xLaDe Clean")
    print(f"  {SEP}")

    # Project-local state
    if os.path.isdir(project_local):
        shutil.rmtree(project_local)
        deleted.append(".xlade/  (workspace, run history, metrics)")
    else:
        not_found.append(".xlade/")

    # Global state
    if os.path.isdir(global_state):
        shutil.rmtree(global_state)
        deleted.append("~/.xlade/  (mode)")
    else:
        not_found.append("~/.xlade/")

    for item in deleted:
        print(f"  [deleted]  {item}")

    for item in not_found:
        print(f"  [skip]     {item} not found")

    print(f"  {SEP}")

    if deleted:
        print(f"  {len(deleted)} item(s) removed. Run 'xlade init' to start fresh.")
    else:
        print("  Nothing to clean.")

    print()
