# xLaDe Tools

This module contains various tools for xLaDe.  
Currently, it is not well-developed but we hope to make it work soon. (I can't give a fixed date but we will work on it soon)  

---

## What Tools are

Technically, tools are utilities which can be used by xLaDe CLI, experiments and scripts, etc.
They are usually an additional layer for xLaDe by which xLaDe can have more features.

### Conceptual Examples

- Tool for extracting lean code
- Tool to find errors inside lean files in experiments
- Tool to check metadata
- Tool for importing or exporting
- Tool for translating errors
- Tool to call AI

In addition, users and developers can add any custom tool they would like to xLaDe.  
This is like a mini-library for xLaDe.  

---

## Requirement

Suppose I am writing an experiment and I have a helper tool file which does some sort of useful thing (for example translating lean 4 errors to humanized version).  
If I have that in experiment only, then no other experiment and any other person can use it directly.  
They will have to copy and rewrite it if they want in separate experiment.   
So instead of separating it, we add the helper file as a tool.  
Now, everyone can import it easily and use it directly.  
This serves use for multiple experiments in addition to CLI.  

---

## Addition

If there is a utility which may by needed for multiple experiments, multiple users, etc., then it can be added as tool.
We generally prefer tools having categories. Every tool should be under a specific category, which can be named by its use.  
The helper tools need to be written in Python, Lean 4 or Bash only due to restraints of projects 
(I am not good in combining multi-languages projects, so I apologize for that. Otherwise I won't be able to ship)

---

## Note

Tools module is not a focus for us right now, because we first want to make the core xLaDe better.
We will develop the tools according to the CLI development and CLI requirements first. For custom use, we ask to the community for help in tools. 

---
