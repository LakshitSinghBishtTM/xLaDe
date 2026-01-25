import os

def run():
    if not os.path.isdir("metrics"):
        print("No metrics directory found.")
        return

    files = os.listdir("metrics")

    if not files:
        print("No metrics available.")
        return

    print("Available metrics artifacts:")
    for f in files:
        print(f"  - {f}")
