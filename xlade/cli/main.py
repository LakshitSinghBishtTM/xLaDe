import sys

def main():
    if len(sys.argv) < 2:
        print("xLaDe CLI")
        print("Run `xlade --help` for commands.")
        return

    cmd = sys.argv[1]

    if cmd == "--help":
        print_help()
    elif cmd == "init":
        from xlade.cli.init import run
        run()
    elif cmd == "list":
        print("Listing resources...")
    elif cmd == "list":
        if len(sys.argv) < 3:
            print("Usage: xlade list experiments|policies")
            return

        sub = sys.argv[2]
        if sub == "experiments":
            from xlade.cli.list_experiments import run
            run()
        else:
            print(f"Unknown list target: {sub}")

    elif cmd == "run":
        print("Running experiment...")
    elif cmd == "doctor":
        print("Running diagnostics...")
    else:
        print(f"Unknown command: {cmd}")

def print_help():
    print("""
xLaDe — Experimental Lean Ecosystem Orchestrator

Commands:
  init
  mode <stable|experimental|onboarding>
  list experiments
  list policies
  run <experiment-id>
  check
  metrics
  status
  doctor
""")
