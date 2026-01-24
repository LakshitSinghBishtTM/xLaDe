# xLaDe Modes

Modes define alternative ways of running Lean within xLaDe.

Each mode represents a different development context, such as:
- onboarding
- experimental exploration
- stable usage

Modes may change:
- what files are built
- which policies are enforced
- warning and error behavior

# xLaDe Build Modes

xLaDe supports multiple build modes to reflect different
development contexts.

Available modes:
- onboarding: learning-oriented, minimal enforcement
- experimental: enables ecosystem experiments
- stable: conservative, policy-driven usage

Modes define expectations and may influence enforcement,
tooling, and build behavior.

## Experiments and Modes

Ecosystem experiments are enabled selectively depending
on the active mode.

By default:
- Experimental mode enables experiments
- Stable and Onboarding modes do not

