# bin

This directory contains the `xlade` CLI entrypoint script.
In simple language, you can run xLaDe directly using it if you don't want to do the boring pip install process.

---

## How to run

```bash
./bin/xlade
```

It will be same as running `xlade` after install.
So, you can run all available commands

For example:

```bash
./bin/xlade --help
```

---

## Usage

Works from the repo root with just Python 3.14+ installed. 
No venv, no pip, no installation step is required. 
This was the original way to run xLaDe and we fully support it.

Both this and pip install call the same `xlade.cli.main:main` function.
So, all the features are available and there is no compromise.

---

## Notes

Real men use `./bin/xlade` over pip install.
In case of any brokerage of it, please report to us.

---