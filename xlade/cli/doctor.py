import shutil
import os

SEP       = "-" * 100
COL_LABEL = 16
COL_TAG   = 7   # "[error]" is longest tag at 7 chars


def _row(label, tag, message, hint=None):
    tag_str = f"[{tag}]"
    print(f"  {label:<{COL_LABEL}}  {tag_str:<{COL_TAG}}  {message}")
    if hint:
        indent = "  " + " " * COL_LABEL + "  " + " " * COL_TAG + "  "
        for line in hint:
            print(f"{indent}{line}")


def run():
    issues = 0

    print()
    print("  xLaDe Doctor")
    print(f"  {SEP}")

    # elan
    if shutil.which("elan"):
        _row("elan", "ok", "found")
    else:
        _row("elan", "error", "not found",
             ["Install: curl https://elan.lean-lang.org/elan-init.sh -sSf | sh",
              "Then restart your shell and re-run xlade doctor."])
        issues += 1

    # lake
    if shutil.which("lake"):
        _row("lake", "ok", "found")
    else:
        _row("lake", "error", "not found",
             ["Install elan first, then:",
              "elan toolchain install leanprover/lean4:stable"])
        issues += 1

    # lean-core
    if os.path.isdir("lean-core"):
        if os.listdir("lean-core"):
            _row("lean-core", "ok", "submodule present")
        else:
            _row("lean-core", "error", "submodule empty",
                 ["Run: git submodule update --init --recursive"])
            issues += 1
    else:
        _row("lean-core", "error", "not found",
             ["Run: git submodule update --init --recursive"])
        issues += 1

    # lean-toolchain
    if os.path.isfile("lean-toolchain"):
        toolchain = open("lean-toolchain").read().strip()
        _row("lean-toolchain", "ok", f"present  ({toolchain})")
    else:
        _row("lean-toolchain", "error", "not found",
             ["Create it: echo 'leanprover/lean4:stable' > lean-toolchain"])
        issues += 1

    # workspace
    if os.path.isdir(".xlade"):
        _row("workspace", "ok", "initialised")
    else:
        _row("workspace", "warn", "not initialised",
             ["Run: xlade init"])

    print(f"  {SEP}")

    if issues == 0:
        print("  All checks passed.")
    else:
        plural = "issue" if issues == 1 else "issues"
        print(f"  {issues} {plural} found. Fix above and re-run xlade doctor.")

    print()