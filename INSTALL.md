# Installing xLaDe

This document describes how to clone and set up xLaDe locally for experimentation and development.

---

## Requirements

Before installing xLaDe, ensure the following are available:

- Git
- Lean 4 toolchain
- Lake
- Elan

---

## Quick Install

Clone the repository:

```
git clone https://github.com/LakshitSinghBishtTM/xLaDe.git
cd xLaDe
```

Build with lake

```
lake update
lake build
```

Make the CLI executable:

```
chmod +x bin/xlade
```

This prepares the repository for local use.

---

## Verification

```
./bin/xlade doctor
```

Output on successful check:

```
xLaDe Doctor Report
lake found
lean-core submodule present
lean-toolchain present
```

---

## Uninstalling

```
cd ..
rm -rf xlade
```