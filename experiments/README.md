# xLaDe Experiments

This directory contains experiments for xLaDe.

In simple language, experiments are the projects or tests you run via xLaDe CLI.
These may be related to Lean 4 theorems, tools, workflows, policies, xLaDe, or even meta. 

As long as a Lean 4 project or something exist, just slap xLaDe's cover outside it and try running it.
If it succeeds, congratulations. If it fails, please mention it and we or someone else will try if there can be some help.

---

## What Is an Experiment?

Experiments in xLaDe are the primary artifacts which are run and preserved with the help of xLaDe and supporting tools.
They are normally related to the Lean 4 ecosystem and related fields, however new type of experiments are also welcome.
Experiments are primarily focused on preservation of external projects and their working on Lean 4 versions,
but other use cases are also welcome and encouraged.

In this process, we have some guidelines for experiment authors.

- The experiment should not modify Lean core or try related adventures
- The experiment should be reproducible
- The documentation should not be empty or poorly written, even though we have simplified it
- The experiment should not try to alter xLaDe's internals 
- The experiment should not run in stable or onboarding mode

---

## What is not an Experiment?

We welcome all the possible ideas users can think about.
However, please don't try to 

1. Change Lean 4 internals
2. Blow xLaDe

Rest is allowed.

== Some Jailbreak Ideas ==

1. Fork Lean 4 and put a moustache to add in experiments as separate repo. This ensures that Lean 4 repo is separate from original
2. Try something similar for xLaDe
3. Fork xLaDe and create your own rules

---

## How to create an Experiment?

1. Create a directory in experiments/ and name it accordingly
2. Make a readme file, an experiment toml and a metrics file (we have provided the templates for all three)
3. Add the project or thing you want to test
4. Optionally create script file in scripts/ if required
5. Done

---

## Experiments Directory

For a minimal experiment, we advise to have atleast the following --

1. README.md
2. experiment.toml
3. METRICS.md

However, it may be changed based on the context of experiments and intentions.

---

## How to run an Experiment

1. Go to xLaDe CLI                     ```xlade```
2. Set the mode to experimental        ```xlade mode experimental```
3. Check experiments                   ```xlade list experiments```
4. Execute experiment                  ```xlade run exp-000-test```
5. See the result                      

---

## Lifecycle of an Experiment

1. Draft       Proposals, normally for uncompleted experiments.
2. Active      Runnable, default for all the experiments.
3. Abandoned   Retired, someone messed up the experiment.
4. Promoted    Successful, someone did something great.

---

## Note

Experiments are allowed to fail, and failure is worth preserving.
We would rather have a fun failed experiment than no experiment.

---
