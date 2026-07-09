"""
xlade.core.lean
~~~~~~~~~~~~~~~

Clean subprocess wrappers for lake and lean.

All public functions return a LeanResult dataclass.
Callers never see raw subprocess.CompletedProcess or exceptions from
missing binaries — those are caught here and surfaced as a failed
LeanResult with a human-readable message.

Passthrough mode (passthrough=True) streams output directly to the
terminal and leaves stdout/stderr as empty strings in the result.
Capture mode (passthrough=False, the default) captures both streams
and populates them in the result.
"""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Result type
# ---------------------------------------------------------------------------


@dataclass
class LeanResult:
    success: bool
    returncode: int = -1
    stdout: str = ""
    stderr: str = ""
    command: list[str] = field(default_factory=list)

    def __bool__(self) -> bool:
        return self.success


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _require(binary: str) -> LeanResult | None:
    """Return a failed LeanResult if binary is not on PATH, else None."""
    if not shutil.which(binary):
        return LeanResult(
            success=False,
            returncode=-1,
            stdout="",
            stderr=f"{binary} not found on PATH",
            command=[binary],
        )
    return None


def _run(
    cmd: list[str],
    cwd: str | None = None,
    passthrough: bool = False,
) -> LeanResult:
    """
    Run cmd as a subprocess and return a LeanResult.

    passthrough=True  — output streams directly to terminal; stdout/stderr
                        fields in the result will be empty strings.
    passthrough=False — output is captured and returned in the result.
    """
    try:
        if passthrough:
            result = subprocess.run(cmd, cwd=cwd)
            return LeanResult(
                success=result.returncode == 0,
                returncode=result.returncode,
                stdout="",
                stderr="",
                command=cmd,
            )
        else:
            result = subprocess.run(
                cmd,
                cwd=cwd,
                capture_output=True,
                text=True,
            )
            return LeanResult(
                success=result.returncode == 0,
                returncode=result.returncode,
                stdout=result.stdout,
                stderr=result.stderr,
                command=cmd,
            )
    except FileNotFoundError:
        # Binary disappeared between the which() check and the run() call.
        return LeanResult(
            success=False,
            returncode=-1,
            stdout="",
            stderr=f"Binary not found when executing: {' '.join(cmd)}",
            command=cmd,
        )
    except OSError as exc:
        return LeanResult(
            success=False,
            returncode=-1,
            stdout="",
            stderr=f"OS error running {' '.join(cmd)}: {exc}",
            command=cmd,
        )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def run_lake_script(
    script_name: str,
    cwd: str | None = None,
    passthrough: bool = True,
) -> LeanResult:
    """
    Run `lake script run <script_name>` in the given directory.

    Defaults to passthrough=True so experiment output is visible in the
    terminal during `xlade run`.
    """
    missing = _require("lake")
    if missing is not None:
        return missing
    return _run(["lake", "script", "run", script_name], cwd=cwd, passthrough=passthrough)


def run_lake_build(
    cwd: str | None = None,
    passthrough: bool = True,
) -> LeanResult:
    """
    Run `lake build` in the given directory.

    Used for lean-policy experiments that require a full build.
    """
    missing = _require("lake")
    if missing is not None:
        return missing
    return _run(["lake", "build"], cwd=cwd, passthrough=passthrough)


def run_lean_file(
    path: str,
    passthrough: bool = False,
) -> LeanResult:
    """
    Run `lean <path>` and return the result.

    Defaults to capture mode so callers can inspect output (e.g. the
    error-hints tool in tools/errors/).
    """
    missing = _require("lean")
    if missing is not None:
        return missing
    return _run(["lean", path], passthrough=passthrough)


def run_script(
    entry: str,
    cwd: str | None = None,
    passthrough: bool = True,
) -> LeanResult:
    """
    Run `bash <entry>` as a script-policy experiment.

    entry  — path to the shell script (relative to cwd if cwd is set)
    Defaults to passthrough=True so script output is visible live.
    """
    missing = _require("bash")
    if missing is not None:
        return missing
    return _run(["bash", entry], cwd=cwd, passthrough=passthrough)


def lean_version(passthrough: bool = False) -> LeanResult:
    """
    Run `lean --version` and return the result.

    Useful for doctor checks and run metadata.
    stdout will contain the version string in capture mode.
    """
    missing = _require("lean")
    if missing is not None:
        return missing
    return _run(["lean", "--version"], passthrough=passthrough)


def lake_version(passthrough: bool = False) -> LeanResult:
    """
    Run `lake --version` and return the result.

    Useful for doctor checks and confirming lake is functional
    (not just present on PATH).
    """
    missing = _require("lake")
    if missing is not None:
        return missing
    return _run(["lake", "--version"], passthrough=passthrough)
