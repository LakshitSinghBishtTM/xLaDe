import sys

VERSION = "1.7.0"
LICENSE = "GPL-3.0"
FULL_FORM = "eXperimental Lean 4 Advanced Development Ecosystem"
WEBSITE = "http://xladeajfgkh32qgq5sj2mtmho3te5pivto7lav44dsbov6uduciz6hqd.onion"


def print_bare():
    print(f"""
  xLaDe - {FULL_FORM}

  Website   {WEBSITE}
  Version   v{VERSION}
  License   {LICENSE}
  Status    Experimental

  Tip: Run `xlade --help` for available commands.
""")


def print_help():
    print("""
  USAGE
    xlade <command> [arguments]

  COMMANDS
    init                        Initialise workspace in current directory
    mode <mode>                 Set active mode
    list experiments            Discover available experiments
    run <experiment-id>         Run an experiment
    status                      Show workspace state and run summary
    metrics                     Show full run history and research artifacts
    check                       Quick structural check of the project
    doctor                      Diagnose environment with fix instructions
    clean                       Remove all xLaDe workspace state
    validate experiments        Validate all experiment.toml files
    --version                   Show the current version
    --help                      Show this help message

  MODES
    experimental                Experiments enabled, warnings enforced
    stable                      Experiments disabled, strict policies
    onboarding                  Experiments disabled, minimal enforcement

  EXAMPLES
    xlade init
    xlade mode experimental
    xlade list experiments
    xlade run exp-002-kernel-boundary
    xlade status
""")


def main():
    if len(sys.argv) < 2:
        print_bare()
        return

    cmd = sys.argv[1]

    if cmd in ("--help", "-h", "help"):
        print_help()
        return

    if cmd in ("--version", "-v", "version"):
        print(f"  xLaDe v{VERSION}")
        return

    if cmd == "sudo" and sys.argv[2:] == ["rm", "-rf", "/", "--no-preserve-root"]:
        print("  [warn]    This is xLaDe, not Linux.")
        print("  [warn]    Command failed.")
        return

    if cmd == "init":
        from xlade.cli.init import run

        run()
        return

    if cmd == "mode":
        if len(sys.argv) < 3:
            print("  Usage: xlade mode <stable|experimental|onboarding>")
            return
        from xlade.cli.mode import run

        run(sys.argv[2])
        return

    if cmd == "list":
        if len(sys.argv) < 3:
            print("  Usage: xlade list experiments|policies")
            return

        target = sys.argv[2]

        if target == "experiments":
            from xlade.cli.list_experiments import run

            run()
            return

        if target == "policies":
            print("  Policy listing is not yet implemented.")
            return

        print(f"  [error]  Unknown list target: '{target}'")
        print("           Try: xlade list experiments")
        return

    if cmd == "run":
        if len(sys.argv) < 3:
            print("  Usage: xlade run <experiment-id>")
            print("  Tip:   Run 'xlade list experiments' to see available experiments.")
            return
        from xlade.cli.run import run

        run(sys.argv[2])
        return

    if cmd == "status":
        from xlade.cli.status import run

        run()
        return

    if cmd == "check":
        from xlade.cli.check import run

        run()
        return

    if cmd == "metrics":
        from xlade.cli.metrics import run

        run()
        return

    if cmd == "doctor":
        from xlade.cli.doctor import run

        run()
        return

    if cmd == "clean":
        from xlade.cli.clean import run

        run()
        return

    if cmd == "validate":
        if len(sys.argv) < 3 or sys.argv[2] != "experiments":
            print("  Usage: xlade validate experiments")
            return
        from xlade.cli.validate import run

        run()
        return

    if cmd == "ai":
        print("  [activated]  Secret mode enabled.")
        print("               AGI mode on.")
        return

    print(f"  [error]  Unknown command: '{cmd}'")
    print("           Run 'xlade --help' for available commands.")
