import os


def run():
    issues = []

    if not os.path.isdir(".xlade"):
        issues.append(("workspace", "not initialised", "run: xlade init"))

    if not os.path.isdir("experiments"):
        issues.append(
            (
                "experiments",
                "directory not found",
                "expected experiments/ in project root",
            )
        )

    sep = "-" * 100

    print()
    print("  xLaDe Check")
    print(f"  {sep}")

    if issues:
        for label, status, hint in issues:
            print(f"  {label:<14}  [error]  {status}")
            print(f"  {'':14}           {hint}")
        print(f"  {sep}")
        print(f"  {len(issues)} issue(s) found.")
    else:
        print("  workspace     [ok]")
        print("  experiments   [ok]")
        print(f"  {sep}")
        print("  All checks passed.")

    print()
