import os

VALID_MODES = ["stable", "experimental", "onboarding"]

def run(mode):
    if mode not in VALID_MODES:
        print(f"Invalid mode: {mode}")
        print("Valid modes:", ", ".join(VALID_MODES))
        return

    home = os.path.expanduser("~")
    state_dir = os.path.join(home, ".xlade")

    if not os.path.isdir(state_dir):
        os.mkdir(state_dir)

    with open(os.path.join(state_dir, "mode"), "w") as f:
        f.write(mode + "\n")

    print(f"xLaDe mode set to: {mode}")
