# Contributing

Contributing to xLaDe makes xLaDe better for everyone.
Kindly help in building xLaDe so that it becomes a helpful tool.

---

## What to Contribute

- Updating or improving documentation files and typos 
- Deleting bloat
- Adding a new experiment
- Fixing bugs
- Simplifying code
- Improving a module
- Adding a new feature or module

---

## What not to Contribute

- Deleting entire project as bloat
- Mirrors workflow files (unless there is a problem)
- Changing rules in files like Code of Conduct 
- Trying to rewrite entire xLaDe in Rust

---

## How to contribute

This depends on what you want to contribute. We divide it in two ways -

### Minor Changes

For minor changes like fixing a typo or updating documentation, etc.

Step 1. Fork xLaDe. This will create a copy of xLaDe.
Step 2. Go to your copy.
Step 3. Edit the file you want.
Step 4. Write what you changed in commit message precisely and save it.
Step 5. Send us a PR

Done.

Alternatively, contributors can use local CLI to edit and send us a PR.
However, this needs a setup and may feel difficult to some new users, so we suggest newcomers to use above method if the below setup feels hectic.

---

## Major Changes

For major changes like fixing bugs, we generally encourage a local CLI setup.
Use the following commands to setup xLaDe and contribute -

Step 1. Fork xLaDe and then clone locally

```sh
git clone https://github.com/{github_username}/xLaDe.git
cd xLaDe
git remote add upstream https://github.com/LakshitSinghBishtTM/xLaDe.git
```

Step 2. Create a branch

```sh
git checkout -b {branch-name}
```

Step 3. Edit the file(s) you want. 

Step 4. Check formatting of changed code with isort, black and flake, and then run tests.

```sh
isort .
black .
flake8 .
```

```sh
pytest tests/ -v
```

Step 5. Write what you changed in commit message precisely and save it.

```sh
git commit -m "Change summary" -m "Optional detailed description of change. May add AI tools disclosure here"
```

Step 6. Push and open a PR

```sh
git push -u origin {branch-name}
```

Done

Note: Please ensure you already have all things downloaded like git, python, pytest, etc.

---

## Note

- The cd command in step 1 is from Linux
- In case of Windows, either download WSL or read manual for commands
- git tool works same everywhere so these commands should work irrespective of the OS
- Please check the formatting and test suite, we already have enough history with it related to contributors
- In case of any problem regarding contributing, please create an issue
