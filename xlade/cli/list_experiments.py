import os

def run():
    if not os.path.isdir("experiments"):
        print("No experiments directory found.")
        return

    experiments = sorted(
        d for d in os.listdir("experiments")
        if os.path.isdir(os.path.join("experiments", d))
    )

    if not experiments:
        print("No experiments available.")
        return

    print("Available experiments:")
    for exp in experiments:
        print(f"  - {exp}")
