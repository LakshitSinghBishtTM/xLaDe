import os
from xlade.core.errors import error

def run():
    warnings = []

    if not os.path.isdir(".xlade"):
        warnings.append("Project not initialized")

    if not os.path.isdir("experiments"):
        warnings.append("No experiments directory")

    if warnings:
        print("xLaDe check completed with warnings:")
        for w in warnings:
            print(f"  - {w}")
    else:
        print("xLaDe check passed. No issues found.")
