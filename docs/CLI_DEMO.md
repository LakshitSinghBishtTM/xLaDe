# xLaDe CLI Demonstration Script

This script demonstrates xLaDe as an executable ecosystem tool.

## 1. Initialization

```
xlade init
```
Creates a project-local .xlade/ directory for runtime state.

2. Listing Experiments
```
xlade list experiments
```

Displays all available ecosystem experiments defined in the repository.

3. Purpose

The CLI acts as an orchestration layer over research artifacts
(experiments, policies, metrics) without modifying Lean core.

This enables controlled ecosystem experimentation while keeping
the core system immutable.
