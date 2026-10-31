from xlade.cli import clean, doctor, init, list_experiments, metrics, mode, run, status, validate
from xlade.cli.exitcodes import ExitCode


def _code(result):
    """Modules that return nothing count as success; ints pass through."""
    return ExitCode.OK if result is None else result


def usage(text, tip=None):
    print(f"  Usage: {text}")
    if tip:
        print(f"  Tip:   {tip}")
    return ExitCode.USAGE


def unknown_command(name):
    print(f"  [error]  Unknown command: '{name}'")
    print("           Run 'xlade --help' for available commands.")
    return ExitCode.USAGE


# --- Commands -----------------------------------------------------------------


def cmd_init(args):
    return _code(init.run())


def cmd_mode(args):
    if not args:
        return usage("xlade mode <stable|experimental|onboarding>")
    return _code(mode.run(args[0]))


def cmd_list(args):
    if not args:
        return usage("xlade list experiments")
    if args[0] != "experiments":
        print(f"  [error]  Unknown list target: '{args[0]}'")
        print("           Try: xlade list experiments")
        return ExitCode.USAGE
    return _code(list_experiments.run())


def cmd_run(args):
    if not args:
        return usage(
            "xlade run <experiment-id>",
            tip="Run 'xlade list experiments' to see available experiments.",
        )
    return _code(run.run(args[0]))


def cmd_status(args):
    return _code(status.run())


def cmd_metrics(args):
    return _code(metrics.run())


def cmd_doctor(args):
    return _code(doctor.run())


def cmd_clean(args):
    return _code(clean.run())


def cmd_validate(args):
    if args != ["experiments"]:
        return usage("xlade validate experiments")
    return _code(validate.run())


COMMANDS = {
    "init": cmd_init,
    "mode": cmd_mode,
    "list": cmd_list,
    "run": cmd_run,
    "status": cmd_status,
    "metrics": cmd_metrics,
    "doctor": cmd_doctor,
    "clean": cmd_clean,
    "validate": cmd_validate,
}


# --- Easter eggs -----------------------------------------


def egg_sudo(args):
    if args != ["rm", "-rf", "/", "--no-preserve-root"]:
        return unknown_command("sudo")
    print("  [warn]    This is xLaDe, not Linux.")
    print("  [warn]    Command failed.")
    return ExitCode.FAILURE


def egg_ai(args):
    print("  [activated]  Secret mode enabled.")
    print("               AGI mode on.")
    return ExitCode.OK


EASTER_EGGS = {
    "sudo": egg_sudo,
    "ai": egg_ai,
}
