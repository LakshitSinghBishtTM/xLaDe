import shutil
import os

def run():
    print("xLaDe Doctor Report")

    if shutil.which("lake"):
        print("✔ lake found")
    else:
        print("✘ lake not found")

    if os.path.isdir("lean-core"):
        print("✔ lean-core submodule present")
    else:
        print("✘ lean-core missing")

    if os.path.isfile("lean-toolchain"):
        print("✔ lean-toolchain present")
    else:
        print("✘ lean-toolchain missing")
