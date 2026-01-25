import sys

def print_help():
    print("""
xLaDe — Experimental Lean Ecosystem Orchestrator

Usage:
  xlade init
  xlade mode <stable|experimental|onboarding>
  xlade list experiments
  xlade list policies
  xlade run <experiment-id>
  xlade status
  xlade check
  xlade metrics
  xlade doctor
  xlade --help
""")


def main():
    if len(sys.argv) < 2:
        print("xLaDe CLI")
        print("Run `xlade --help` for available commands.")
        return

    cmd = sys.argv[1]

    # --------------------
    # Help
    # --------------------
    if cmd in ("--help", "-h", "help"):
        print_help()
        return

    # --------------------
    # init
    # --------------------
    if cmd == "init":
        from xlade.cli.init import run
        run()
        return

    # --------------------
    # mode
    # --------------------
    if cmd == "mode":
        if len(sys.argv) < 3:
            print("Usage: xlade mode <stable|experimental|onboarding>")
            return
        from xlade.cli.mode import run
        run(sys.argv[2])
        return

    # --------------------
    # list
    # --------------------
    if cmd == "list":
        if len(sys.argv) < 3:
            print("Usage: xlade list experiments|policies")
            return

        target = sys.argv[2]

        if target == "experiments":
            from xlade.cli.list_experiments import run
            run()
            return

        if target == "policies":
            print("Policy listing not yet implemented.")
            return

        print(f"Unknown list target: {target}")
        return

    # --------------------
    # run
    # --------------------
    if cmd == "run":
        if len(sys.argv) < 3:
            print("Usage: xlade run <experiment-id>")
            return
        from xlade.cli.run import run
        run(sys.argv[2])
        return

    # --------------------
    # status
    # --------------------
    if cmd == "status":
        from xlade.cli.status import run
        run()
        return

    # --------------------
    # check
    # --------------------
    if cmd == "check":
        from xlade.cli.check import run
        run()
        return

    # --------------------
    # metrics
    # --------------------
    if cmd == "metrics":
        from xlade.cli.metrics import run
        run()
        return

    # --------------------
    # doctor
    # --------------------
    if cmd == "doctor":
        from xlade.cli.doctor import run
        run()
        return

    # --------------------
    # Unknown command
    # --------------------
    print(f"Unknown command: {cmd}")
    print("Run `xlade --help` for available commands.")
