# Interface Design

When the user wants to explore alternative interfaces for a chosen deepening candidate, use this parallel sub-agent pattern. Based on "Design It Twice" (Ousterhout) — your first idea is unlikely to be the best.

Uses the vocabulary in [LANGUAGE.md](LANGUAGE.md) — **module**, **interface**, **seam**, **adapter**, **leverage**.

## Process

### 1. Frame the problem space

Before spawning sub-agents, write a user-facing explanation of the problem space for the chosen candidate:

- The constraints any new interface would need to satisfy — including data-shape invariants (units, dtype, dimension order, batched vs unbatched), reproducibility requirements (RNG handling, determinism), and numerical guarantees (tolerances, conservation laws, convergence behaviour) where relevant
- The dependencies it would rely on, and which category they fall into (see [DEEPENING.md](DEEPENING.md))
- A rough illustrative code sketch in the project's primary language (Python or Julia) to ground the constraints — not a proposal, just a way to make the constraints concrete

Show this to the user, then immediately proceed to Step 2. The user reads and thinks while the sub-agents work in parallel.

### 2. Spawn sub-agents

Spawn 3+ sub-agents in parallel using the Agent tool. Each must produce a **radically different** interface for the deepened module.

Prompt each sub-agent with a separate technical brief (file paths, coupling details, dependency category from [DEEPENING.md](DEEPENING.md), what sits behind the seam, the language idioms in use — `Protocol`/`ABC`/`dataclass` for Python, abstract types and multiple dispatch for Julia). The brief is independent of the user-facing problem-space explanation in Step 1. Give each agent a different design constraint:

- Agent 1: "Minimise the interface — aim for 1–3 entry points max. Maximise leverage per entry point."
- Agent 2: "Maximise flexibility — support many use cases, swappable solvers/backends/datasets."
- Agent 3: "Optimise for the most common caller — make the default case trivial; one call from a notebook should just work."
- Agent 4: "Optimise for reproducibility — every source of nondeterminism (RNG, thread count, device, dtype, solver tolerances) is an explicit, recorded parameter. The interface makes it impossible to do an irreproducible run by accident."
- Agent 5 (if cross-seam dependencies are central): "Design around ports & adapters — production cluster/instrument backend on one side, in-memory/synthetic backend on the other."

Include both [LANGUAGE.md](LANGUAGE.md) vocabulary and CONTEXT.md vocabulary in the brief so each sub-agent names things consistently with the architecture language and the project's domain language.

Each sub-agent outputs:

1. Interface (types, methods, params — plus invariants, units/shapes/dtypes, ordering, error modes, RNG handling)
2. Usage example showing how callers use it (a script or notebook cell, in the project's language)
3. What the implementation hides behind the seam
4. Dependency strategy and adapters (see [DEEPENING.md](DEEPENING.md))
5. Trade-offs — where leverage is high, where it's thin, and what tests look like at the new interface

### 3. Present and compare

Present designs sequentially so the user can absorb each one, then compare them in prose. Contrast by **depth** (leverage at the interface), **locality** (where change concentrates), **seam placement**, and — for research code — **reproducibility surface** (what an irreproducible run would look like; how easy is it to commit one by accident).

After comparing, give your own recommendation: which design you think is strongest and why. If elements from different designs would combine well, propose a hybrid. Be opinionated — the user wants a strong read, not a menu.
