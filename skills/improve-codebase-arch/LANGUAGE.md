# Language

Shared vocabulary for every suggestion this skill makes. Use these terms exactly — don't substitute "component," "kernel," "library," or "boundary." Consistent language is the whole point.

The vocabulary is language-agnostic but maps cleanly onto Python and Julia: a **module** can be a function, a class, a Python module/package, a Julia `module`, or a multi-file slice (a pipeline stage, a solver backend, a data loader). "Module" overlaps with the Python/Julia language keyword on purpose — both refer to a unit with an interface and an implementation.

## Terms

**Module**
Anything with an interface and an implementation. Deliberately scale-agnostic — applies equally to a function, class, Python package, Julia module, notebook section, or pipeline stage.
_Avoid_: unit, component, util, helper, kernel (overloaded — Linux kernel, GPU kernel, ML kernel, integration kernel — say "module" or be explicit, e.g. "the CUDA kernel").

**Interface**
Everything a caller must know to use the module correctly. Includes the type signature, but also invariants (units, dtype, shape, dimension order), ordering constraints, error modes, required configuration, RNG/seed handling, and performance characteristics (memory footprint, GPU/CPU, in-place vs out-of-place).
_Avoid_: API, signature, type — too narrow. A function whose signature is `solve(problem, solver)` still has an interface that includes "must be called after `setup`," "raises `ConvergenceError` after `max_iter`," "mutates `problem.state` in place," and "results are deterministic given `solver.rng`."

**Implementation**
What's inside a module — its body of code. Distinct from **Adapter**: a thing can be a small adapter with a large implementation (an HDF5-backed `Dataset`) or a large adapter with a small implementation (an in-memory synthetic-data fake). Reach for "adapter" when the seam is the topic; "implementation" otherwise.

**Depth**
Leverage at the interface — the amount of behaviour a caller (or test) can exercise per unit of interface they have to learn. A module is **deep** when a large amount of behaviour sits behind a small interface. A module is **shallow** when the interface is nearly as complex as the implementation.

**Seam** _(from Michael Feathers)_
A place where you can alter behaviour without editing in that place. The *location* at which a module's interface lives. Choosing where to put the seam is its own design decision, distinct from what goes behind it. In Python, seams are typically expressed with `Protocol` classes (PEP 544), `ABC`s, or plain duck-typed callables passed as arguments. In Julia, seams are expressed through abstract types and multiple dispatch — the seam is the set of methods a caller expects to be defined for a type.
_Avoid_: boundary (overloaded with DDD's bounded context); layer (too rigid).

**Adapter**
A concrete thing that satisfies an interface at a seam. Describes *role* (what slot it fills), not substance (what's inside). A `ParquetDataset`, an `HDF5Dataset`, and an `InMemoryDataset` are three adapters at the same seam. A `DaskBackend` and a `LocalBackend` are two adapters at a compute seam.

**Leverage**
What callers get from depth. More capability per unit of interface they have to learn. One implementation pays back across N call sites and M tests.

**Locality**
What maintainers get from depth. Change, bugs, knowledge, and verification concentrate at one place rather than spreading across callers. Fix once, fixed everywhere.

## Principles

- **Depth is a property of the interface, not the implementation.** A deep module can be internally composed of small, mockable, swappable parts — they just aren't part of the interface. A module can have **internal seams** (private to its implementation, used by its own tests) as well as the **external seam** at its interface.
- **The deletion test.** Imagine deleting the module. If complexity vanishes, the module wasn't hiding anything (it was a pass-through). If complexity reappears across N callers, the module was earning its keep.
- **The interface is the test surface.** Callers and tests cross the same seam. If you want to test *past* the interface, the module is probably the wrong shape. In research code this often means: assert on the output array / DataFrame / fitted parameters, not on which intermediate helper was called.
- **One adapter means a hypothetical seam. Two adapters means a real one.** Don't introduce a seam unless something actually varies across it. A `Solver` protocol with only `ScipySolver` behind it is just indirection — wait until you also have `JAXSolver`, `MockSolver`, or a synthetic-data fixture before promoting it to a seam.
- **Stochasticity belongs in the interface.** If a module's output depends on randomness, the RNG (or seed) is part of its interface — not a global, not a hidden default. This is the single most common shallow-module pattern in research code.

## Relationships

- A **Module** has exactly one **Interface** (the surface it presents to callers and tests).
- **Depth** is a property of a **Module**, measured against its **Interface**.
- A **Seam** is where a **Module**'s **Interface** lives.
- An **Adapter** sits at a **Seam** and satisfies the **Interface**.
- **Depth** produces **Leverage** for callers and **Locality** for maintainers.

## Rejected framings

- **Depth as ratio of implementation-lines to interface-lines** (Ousterhout): rewards padding the implementation. We use depth-as-leverage instead.
- **"Interface" as a Python `Protocol`/`ABC` or a Julia abstract type alone**: too narrow — those describe the type-level surface, but interface here includes every fact a caller must know (units, shapes, dtypes, RNG handling, in-place vs out-of-place, convergence behaviour).
- **"Boundary"**: overloaded with DDD's bounded context. Say **seam** or **interface**.
- **"Pipeline stage" as the unit of design**: pipelines are how research code runs, not how it's *designed*. A stage may be one deep module, several shallow ones, or a thin wrapper over a deep module — the stage boundary is not automatically the right seam.
