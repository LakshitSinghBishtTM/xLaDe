import os

def run():
    if not os.path.isdir(".xlade"):
        print("xLaDe is not initialized.")
        return

    last_run_file = ".xlade/last-run"

    if not os.path.exists(last_run_file):
        print("No experiment has been run yet.")
        return

    with open(last_run_file) as f:
        last = f.read().strip()

    if last == "none" or last == "":
        print("No experiment has been run yet.")
    else:
        print(f"Last experiment run: {last}")
