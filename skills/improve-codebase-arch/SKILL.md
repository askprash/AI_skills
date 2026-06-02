---
name: improve-codebase-architecture
description: Find deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and the decisions in docs/adr/. Use when the user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more testable and AI-navigable.
---

# Improve Codebase Architecture

Surface architectural friction and propose **deepening opportunities** — refactors that turn shallow modules into deep ones. The aim is testability, reproducibility, and AI-navigability.

This skill is tuned for research and scientific engineering codebases — Python and Julia in particular — where the typical pathologies are notebooks-grown-into-packages, RNG and config plumbed by hand, plotting tangled with analysis, and "utility" modules that hide nothing. The architectural vocabulary in [LANGUAGE.md](LANGUAGE.md) is language-agnostic, but the examples and dependency categories in [DEEPENING.md](DEEPENING.md) are written for the dependencies this kind of code actually has: gridded atmospheric data (NetCDF/Zarr, ERA5, MERRA-2), tabular performance databases (BADA, ICAO emissions tables), array/DataFrame libraries, ODE/PDE solvers (DifferentialEquations.jl, SciPy, ModelingToolkit), and HPC schedulers.

## Glossary

Use these terms exactly in every suggestion. Consistent language is the point — don't drift into "component," "kernel," "library," or "boundary." Full definitions in [LANGUAGE.md](LANGUAGE.md).

- **Module** — anything with an interface and an implementation (function, class, Python package, Julia module, pipeline stage).
- **Interface** — everything a caller must know to use the module: types, invariants (units, dtype, shape, dimension order), error modes, ordering, configuration, RNG handling. Not just the type signature.
- **Implementation** — the code inside.
- **Depth** — leverage at the interface: a lot of behaviour behind a small interface. **Deep** = high leverage. **Shallow** = interface nearly as complex as the implementation.
- **Seam** — where an interface lives; a place behaviour can be altered without editing in place. (Use this, not "boundary.")
- **Adapter** — a concrete thing satisfying an interface at a seam (e.g. `HDF5Dataset`, `DaskBackend`, `MockInstrument`).
- **Leverage** — what callers get from depth.
- **Locality** — what maintainers get from depth: change, bugs, knowledge concentrated in one place.

Key principles (see [LANGUAGE.md](LANGUAGE.md) for the full list):

- **Deletion test**: imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it was earning its keep.
- **The interface is the test surface.**
- **One adapter = hypothetical seam. Two adapters = real seam.**

This skill is _informed_ by the project's domain model. The domain language gives names to good seams; ADRs record decisions the skill should not re-litigate.

## Process

### 1. Explore

Read the project's domain glossary and any ADRs in the area you're touching first.

Then use the Agent tool with `subagent_type=Explore` to walk the codebase. Don't follow rigid heuristics — explore organically and note where you experience friction. General signals:

- Where does understanding one concept require bouncing between many small modules?
- Where are modules **shallow** — interface nearly as complex as the implementation?
- Where have pure functions been extracted just for testability, but the real bugs hide in how they're called (no **locality**)?
- Where do tightly-coupled modules leak across their seams?
- Which parts of the codebase are untested, or hard to test through their current interface?

Research-code signals to add to the sweep:

- **RNG plumbed by hand or by global.** Functions that call `np.random.*` / `torch.manual_seed` / `Random.randn` against globals; tests pinned to magic seeds; results that "look about right" but aren't bit-reproducible. The RNG belongs in the interface (see [DEEPENING.md](DEEPENING.md)).
- **I/O entangled with computation.** A function that opens an HDF5/NetCDF/FITS/CSV file *and* does the science — usually two modules in a trench coat. The seam between "load data" and "compute on data" wants to exist.
- **Plotting tangled with analysis.** `plt.plot(...)` calls living inside the same function that fits a model or computes a statistic. The figure-rendering module is almost always shallow; its inputs (the analysis result) usually want to become a real, testable type.
- **Hard-coded paths and configuration drift.** `"/data/runs/2024-03-...`" embedded in modules; the same hyperparameter spelled three different ways across `argparse`, a YAML file, and a function default. Config that's read implicitly is a hidden seam.
- **Notebook → script → module drift.** The same transformation reimplemented slightly differently in a notebook, a `scripts/` file, and a package module. Classic deletion-test target: pick the deepest version, point everyone at it.
- **"Utils" / "helpers" / "common" modules.** These are usually shallow by construction — no coherent interface, just a grab-bag of functions. Ask whether each function belongs to a real concept; pull it home.
- **Solvers, optimisers, samplers, datasets baked in.** Direct calls to `scipy.optimize.minimize`, `optax.adam`, a specific `Dataset` constructor — no seam, no swap. If the project will ever try a second backend or a synthetic-data fixture, the seam is worth introducing.

Apply the **deletion test** to anything you suspect is shallow: would deleting it concentrate complexity, or just move it? A "yes, concentrates" is the signal you want.

### 2. Present candidates

Present a numbered list of deepening opportunities. For each candidate:

- **Files** — which files/modules are involved
- **Problem** — why the current architecture is causing friction
- **Solution** — plain English description of what would change
- **Benefits** — explained in terms of locality and leverage, and also in how tests would improve

**Use CONTEXT.md vocabulary for the domain, and [LANGUAGE.md](LANGUAGE.md) vocabulary for the architecture.** If `CONTEXT.md` defines "Trajectory," talk about "the Trajectory ingest module" — not "the `traj_utils.py` helpers," and not "the trajectory service." If `CONTEXT.md` defines "Mission," "Engine," "Contrail," "Plume," "Emissions Inventory," "Fleet," or "Run," use those names.

**ADR conflicts**: if a candidate contradicts an existing ADR, only surface it when the friction is real enough to warrant revisiting the ADR. Mark it clearly (e.g. _"contradicts ADR-0007 — but worth reopening because…"_). Don't list every theoretical refactor an ADR forbids.

Do NOT propose interfaces yet. Ask the user: "Which of these would you like to explore?"

### 3. Grilling loop

Once the user picks a candidate, drop into a grilling conversation. Walk the design tree with them — constraints, dependencies, the shape of the deepened module, what sits behind the seam, what tests survive.

Side effects happen inline as decisions crystallize:

- **Naming a deepened module after a concept not in `CONTEXT.md`?** Add the term to `CONTEXT.md` — same discipline as `/grill-with-docs` (see [CONTEXT-FORMAT.md](../grill-with-docs/CONTEXT-FORMAT.md)). Create the file lazily if it doesn't exist.
- **Sharpening a fuzzy term during the conversation?** Update `CONTEXT.md` right there.
- **User rejects the candidate with a load-bearing reason?** Offer an ADR, framed as: _"Want me to record this as an ADR so future architecture reviews don't re-suggest it?"_ Only offer when the reason would actually be needed by a future explorer to avoid re-suggesting the same thing — skip ephemeral reasons ("not worth it right now") and self-evident ones. See [ADR-FORMAT.md](../grill-with-docs/ADR-FORMAT.md).
- **Want to explore alternative interfaces for the deepened module?** See [INTERFACE-DESIGN.md](INTERFACE-DESIGN.md).
