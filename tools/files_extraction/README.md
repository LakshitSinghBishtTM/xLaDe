# `xlade cat`

`xlade cat` is the Lean-aware file inspection command. It keeps the familiar file-viewing behavior of Linux `cat`, and adds source inspection features for Lean experiments.

Run `xlade cat --help` for the live command help.

## Basic viewing

```bash
xlade cat path/to/File.lean
xlade cat first.lean second.lean
xlade cat path/to/File.lean --head 20
xlade cat path/to/File.lean --tail 20
xlade cat path/to/File.lean --lines 10-25
xlade cat path/to/File.lean --pager
```

Linux-style display flags are supported:

```text
-n, --number             Number every output line
-b, --number-nonblank    Number non-blank lines
-s, --squeeze-blank      Suppress repeated blank lines
-E, --show-ends          Show `$` at line ends
-T, --show-tabs          Show tabs as `^I`
-v, --show-nonprinting   Show non-printing characters
-A, --show-all           Equivalent to -vET
```

## Lean inspection

Use these options when the file is Lean source:

```bash
xlade cat File.lean --summary
xlade cat File.lean --imports
xlade cat File.lean --symbols
xlade cat File.lean --context 42
xlade cat File.lean --context 42 --context-lines 5
xlade cat File.lean --diagnostics
xlade cat File.lean --diagnostics --explain
```

`--summary` reports the path, line count, imports, declarations, `sorry` count, and Lean check status. `--imports` lists imported modules with line numbers. `--symbols` lists common declarations such as theorems, definitions, structures, namespaces, and examples. `--context` marks the requested source line and displays nearby lines. `--diagnostics` runs `lean` on the file. `--explain` uses the database in `tools/errors/` to add human explanations to diagnostics.

Inspection options can be combined. For example:

```bash
xlade cat File.lean --summary --symbols --diagnostics --explain
```

## Experiment-aware viewing

List Lean files in an experiment:

```bash
xlade cat --experiment exp-006-teorth-analysis
```

Inspect a path relative to an experiment directory:

```bash
xlade cat --experiment exp-006-teorth-analysis Analysis.lean --summary
```

Inspect every Lean file discovered in an experiment with a selected report:

```bash
xlade cat --experiment exp-006-teorth-analysis --all --summary
xlade cat --experiment exp-006-teorth-analysis --all --symbols
```

If the experiment does not exist, the command reports that error. If it exists but contains no `.lean` files, the command says so explicitly.
