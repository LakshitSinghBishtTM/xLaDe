# Why xLaDe?

This document explains the motivation behind xLaDe — the problems it is
trying to solve, why those problems matter, and why the approach taken is
the right one.

---

## The Two Problems

### 1. Backward Compatibility in Lean 4

Lean 4 evolves fast. That is one of its strengths — the language and
toolchain improve rapidly, new features land frequently, and the ecosystem
moves forward. But this comes with a cost that is rarely talked about openly:
**proofs and experiments written in Lean 4 are fragile over time.**

Something that compiles cleanly today may silently break next year. A proof
that was valid under one version of Lean may fail elaboration under the next.
A project built on a specific toolchain version becomes an archaeological
artifact within months if it is not actively maintained.

This is a known issue. Leonardo de Moura, the creator of Lean, has
acknowledged it publicly multiple times. It cannot be fully solved given
Lean's pace of development — the language is still being shaped, and
stability guarantees would slow that process down in ways the core team
is not willing to accept. That is a reasonable position for a language
under active research development.

But it creates a real problem for anyone trying to do **reproducible
research** with Lean. If an experiment runs today but not next year, it
is not a reproducible experiment — it is a snapshot. And snapshots rot.

**xLaDe's approach** is not to freeze Lean or ship every historical
version of the toolchain. That would be impractical and would defeat the
purpose of using a living language. Instead, xLaDe treats each experiment
as inseparable from its environment. Every experiment records its full
execution context as metadata — the Lean toolchain version, dependencies,
build configuration, and mode. When xLaDe runs an experiment, it
reconstructs that environment using elan and lake, allowing the experiment
to execute correctly even years after it was written.

The goal is **reproducibility**, not backward compatibility. The distinction
matters. Backward compatibility means the language stays stable enough that
old code keeps working. Reproducibility means you can always reconstruct
the environment in which old code worked. xLaDe pursues the second, because
the first is not achievable without sacrificing what makes Lean worth using.

This is a multi-stage idea. The metadata recording is already in place as
of v1.5.0. The environment reconstruction tooling is being built
incrementally. See [`REPRODUCIBILITY_AND_COMPATIBILITY.md`](REPRODUCIBILITY_AND_COMPATIBILITY.md)
for the detailed plan.

---

### 2. Kernel Drift in Lean-Based Projects

The second problem is more subtle but equally damaging in practice.

When someone wants to build a serious project on top of Lean 4, the natural
instinct is to fork the repository and start building. The fork starts life
as a clean copy of Lean. The project grows. Features are added. Workarounds
are patched in. The fork diverges from upstream, slowly at first and then
faster as the project matures.

One day, something breaks. It is not clear what changed or why. The project
has drifted so far from upstream Lean that diagnosing the problem requires
understanding both the original Lean codebase and every modification the
project made on top of it. That is often months of work. Sometimes it is
simply not recoverable.

This happens because there is no enforced boundary between the project and
the kernel it depends on. Everything is mutable. Everything is in the same
repository. There is no mechanism to say "this part is Lean, do not touch
it" — at least not one with teeth.

**xLaDe's approach** is to treat the Lean kernel as genuinely immutable
infrastructure. Lean is included in the repository as a Git submodule —
a versioned, read-only reference. Any modification to `lean-core/` is
detected by CI automatically and the build fails. There is no way to
accidentally modify the kernel and have it go unnoticed. The boundary is
enforced, not just documented.

This does two things. First, it makes the project's relationship with Lean
explicit and auditable — you always know exactly which version of Lean the
project is running against. Second, it makes all experimental effects
attributable. If an experiment changes behaviour, that change came from
the ecosystem layer, not from a kernel modification. That matters for
research validity.

---

## Why Not Just Contribute to Lean Directly?

This is a fair question. If the problems are ecosystem-level, why not
fix them in Lean itself?

The answer is that ecosystem-level experimentation is difficult to do
in upstream repositories where stability, backward compatibility, and
community coordination are critical concerns. Proposing a workflow change
to the Lean core team requires the idea to be mature, well-justified, and
low-risk. You cannot iterate quickly on half-formed ideas in a repository
that thousands of people depend on.

xLaDe exists to be the place where ideas mature. It is a controlled
laboratory — a space where experiments can be run, evaluated, and either
promoted to upstream proposals or abandoned without consequence. The goal
is not to replace Lean's development process but to operate upstream of it:
producing ideas that are ready to be proposed, rather than proposing ideas
that are not ready.

---

## Why This Approach

xLaDe's design is constrained by three principles that follow directly from
the problems above:

**The kernel is immutable.** Every design decision flows from this. Once
you commit to never modifying the kernel, the only place to work is the
ecosystem layer. That constraint is productive — it forces experiments to
be non-invasive and reproducible by construction.

**Experiments are first-class artifacts.** An experiment is not a script
someone ran once. It is a documented, versioned, executable unit with a
research question, a hypothesis, an enforcement mechanism, and exit
criteria. This structure makes experiments reviewable, repeatable, and
comparable.

**Reversibility is non-negotiable.** Any experiment can be disabled by
removing it or its enforcement call. No experiment writes permanent state.
No experiment modifies files outside its own directory. This makes the
cost of trying an idea effectively zero — you can always go back.

---

## The Bigger Picture

The immediate problems — backward compatibility and kernel drift — are
specific to Lean 4 today. But the approach xLaDe takes is more general.

Formal verification tools have historically been difficult to use not
because the underlying logic is wrong, but because the ecosystem around
them is immature. Tooling is fragile. Workflows are undocumented.
Onboarding is steep. Governance is informal. These are solvable problems,
but solving them requires a space to experiment with solutions safely.

That is what xLaDe is trying to be — not just a fix for two Lean-specific
problems, but a template for how ecosystem-level research around proof
assistants can be done in a principled, reproducible, and open way.