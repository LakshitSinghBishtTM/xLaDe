#!/usr/bin/env python3
import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: lean-error-hints.py <lean-file>")
    sys.exit(1)

lean_file = sys.argv[1]

proc = subprocess.run(
    ["lean", lean_file],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Lean prints errors to stdout (and sometimes stderr)
output = proc.stdout + proc.stderr

# ---- Error: instance synthesis failure ----
if "failed to synthesize instance" in output:
    output += (
        "\nHint (xLaDe): Lean could not find a required typeclass instance.\n"
        "• A required instance may be missing\n"
        "• Try importing the relevant module\n"
        "• Provide the instance explicitly\n"
    )

# ---- Error: type / proof mismatch ----
if "proposition" in output:
    output += (
        "\nHint (xLaDe): Lean expected a proof (a proposition), "
        "but you provided a value.\n"
        "• In Lean, proofs and data are different\n"
        "• Use `by` blocks to construct proofs\n"
        "• Check the expected type carefully\n"
    )

print(output, end="")
