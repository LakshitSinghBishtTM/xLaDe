import os
import tomllib

SEP = "-" * 100

VALID_TYPES = {"script-policy", "lean-policy"}
VALID_STATUSES = {"draft", "active", "abandoned", "promoted"}
VALID_MODES = {"experimental", "stable", "onboarding"}
REQUIRED_FIELDS = [
    "id",
    "name",
    "type",
    "status",
    "allowed_modes",
    "lean_toolchain",
    "entry",
    "description",
]


def _check_experiment(exp_path, name):
    issues = []
    ok = []

    config_path = os.path.join(exp_path, "experiment.toml")

    if not os.path.exists(config_path):
        return ok, [("experiment.toml", "missing", "file does not exist")]

    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
    except Exception as e:
        return ok, [("experiment.toml", "parse error", str(e))]

    # Check each required field
    for field in REQUIRED_FIELDS:
        val = config.get(field)

        if val is None:
            issues.append((field, "absent", "field not present in experiment.toml"))
            continue

        if isinstance(val, str) and val.strip() == "":
            issues.append((field, "empty", "field is present but empty"))
            continue

        if isinstance(val, list) and len(val) == 0:
            issues.append((field, "empty", "list is present but empty"))
            continue

        # Value-level checks
        if field == "type" and val not in VALID_TYPES:
            issues.append((field, "invalid", f"'{val}' not in {sorted(VALID_TYPES)}"))
            continue

        if field == "status" and val not in VALID_STATUSES:
            issues.append((field, "invalid", f"'{val}' not in {sorted(VALID_STATUSES)}"))
            continue

        if field == "allowed_modes":
            bad = [m for m in val if m not in VALID_MODES]
            if bad:
                issues.append((field, "invalid", f"unknown mode(s): {bad}"))
                continue

        if field == "entry":
            exp_type = config.get("type", "")
            if exp_type == "script-policy" and not os.path.isfile(val):
                issues.append((field, "not found", f"script '{val}' does not exist on disk"))
                continue

        ok.append(field)

    return ok, issues


def run():
    base_path = "experiments"

    if not os.path.isdir(base_path):
        print()
        print("  [error]  experiments/ directory not found.")
        print("           Make sure you are running from the xLaDe repository root.")
        print()
        return

    entries = sorted(
        [
            name
            for name in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, name))
            and "." not in name
            and os.path.exists(os.path.join(base_path, name, "experiment.toml"))
        ]
    )

    if not entries:
        print()
        print("  No experiments with experiment.toml found.")
        print()
        return

    total_issues = 0

    print()
    print(f"  xLaDe Validate  ({len(entries)} experiment(s))")

    for name in entries:
        exp_path = os.path.join(base_path, name)
        ok, issues = _check_experiment(exp_path, name)

        print(f"  {SEP}")
        print(f"  {name}")
        print()

        for field in ok:
            print(f"    [ok]     {field}")

        for field, tag, detail in issues:
            print(f"    [error]  {field}  --  {tag}: {detail}")
            total_issues += 1

    print(f"  {SEP}")

    if total_issues == 0:
        print("  [pass]   All experiments valid.")
    else:
        plural = "issue" if total_issues == 1 else "issues"
        print(f"  [fail]   {total_issues} {plural} found across {len(entries)} experiment(s).")

    print()
