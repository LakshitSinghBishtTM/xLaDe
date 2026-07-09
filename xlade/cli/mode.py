import os

VALID_MODES = ["stable", "experimental", "onboarding"]

SEP = "-" * 100

MODE_FEATURES = {
    "experimental": [
        "Experiments enabled",
        "Policies emit warnings",
        "No stability guarantees",
        "Intended for researchers and contributors",
    ],
    "stable": [
        "Experiments disabled",
        "Strict policy enforcement",
        "Predictable behaviour",
        "Intended for validation and long-term use",
    ],
    "onboarding": [
        "Experiments disabled",
        "Minimal enforcement",
        "Learning-friendly defaults",
        "Intended for new users",
    ],
}


def run(mode):
    if mode not in VALID_MODES:
        print(f"  [error]  '{mode}' is not a valid mode.")
        print(f"           Valid modes: {', '.join(VALID_MODES)}")
        return

    home = os.path.expanduser("~")
    state_dir = os.path.join(home, ".xlade")

    if not os.path.isdir(state_dir):
        os.mkdir(state_dir)

    with open(os.path.join(state_dir, "mode"), "w") as f:
        f.write(mode + "\n")

    print()
    print(f"  Mode set: {mode}")
    print(f"  {SEP}")
    for i, feature in enumerate(MODE_FEATURES[mode], 1):
        print(f"  {i}. {feature}")
    print()
