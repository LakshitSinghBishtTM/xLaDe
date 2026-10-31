import sys

from xlade.cli.commands import COMMANDS, EASTER_EGGS, unknown_command
from xlade.cli.errors import error
from xlade.cli.exitcodes import ExitCode

VERSION = "2.0.0"
MODEL = "Hippasus"
LICENSE = "GPL-3.0"
FULL_FORM = "eXperimental Lean 4 advanced Development ecosystem"
SEP = "-" * 100


def print_bare():
    print(f"""
  {FULL_FORM}

  {SEP}
  Model     {MODEL}
  Version   v{VERSION}
  License   {LICENSE}
  {SEP}

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


def dispatch(args):
    if not args:
        print_bare()
        return ExitCode.OK

    name, rest = args[0], args[1:]

    if name in ("--help", "-h"):
        print_help()
        return ExitCode.OK

    if name in ("--version", "-v"):
        print(f"  xLaDe v{VERSION}")
        return ExitCode.OK

    handler = COMMANDS.get(name) or EASTER_EGGS.get(name)
    if handler is None:
        return unknown_command(name)
    return handler(rest)


def main(argv=None):
    """Run the CLI and return an exit code for sys.exit()."""
    args = sys.argv[1:] if argv is None else argv
    try:
        return int(dispatch(args))
    except KeyboardInterrupt:
        print("\n  [cancelled]")
        return int(ExitCode.INTERRUPTED)
    except PermissionError as exc:
        error("Permission denied", str(exc), "Check file permissions and try again.")
        return int(ExitCode.PERMISSION)
    except OSError as exc:
        error("I/O error", str(exc))
        return int(ExitCode.IO)
    except Exception as exc:
        error("Unexpected error", f"{type(exc).__name__}: {exc}")
        return int(ExitCode.INTERNAL)


if __name__ == "__main__":
    sys.exit(main())
