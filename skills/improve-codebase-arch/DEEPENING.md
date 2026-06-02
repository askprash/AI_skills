# Deepening

How to deepen a cluster of shallow modules safely, given its dependencies. Assumes the vocabulary in [LANGUAGE.md](LANGUAGE.md) — **module**, **interface**, **seam**, **adapter**.

## Dependency categories

When assessing a candidate for deepening, classify its dependencies. The category determines how the deepened module is tested across its seam.

### 1. In-process

Pure computation, in-memory state, no I/O. Numerical kernels, transforms over arrays/DataFrames, atmospheric and thermodynamic property functions, mission-segment integration, emissions indices, contrail microphysics steps, coordinate transforms, units conversions. ODE/PDE solves count as in-process when the solver runs locally (DifferentialEquations.jl, `scipy.integrate`, ModelingToolkit) — the right of the seam is just "the equations and the solver settings."

Always deepenable — merge the modules and test through the new interface directly. No adapter needed. This is the most common — and most under-exploited — deepening category in research code. A "pure function over arrays" cluster is a free deepening: pull the pieces into one module whose interface is `f(inputs, params) -> outputs` and let property-based tests (`hypothesis` in Python, `Supposition.jl` in Julia) cross the seam, asserting on physical invariants (mass/energy conservation, monotonicity in altitude, dimensional consistency).

### 2. Local-substitutable

Dependencies that have local test stand-ins built into the ecosystem. The deepened module is tested with the stand-in running in the test suite. The seam is internal; no port at the module's external interface.

Common examples in aviation/atmospheric code:

- **Gridded atmospheric data**: NetCDF, Zarr, GRIB. Slices of ERA5/MERRA-2/IFS, radiosonde profiles. Test with a tiny synthetic `xarray.Dataset` (Python) or a hand-built grid (Julia) — same shape and coordinate names, three altitudes and two times. The library is its own substitute.
- **Tabular performance / lookup data**: BADA tables, engine emissions tables (ICAO EDB), drag polars, atmosphere tables. Build a 5-row in-memory frame for tests; load the real CSV/Parquet/HDF5 in production.
- **Trajectory / waypoint files**: CSV, Parquet, custom flight-plan formats. Synthesize a 3-waypoint trajectory in the test.
- **DataFrames**: pandas / polars / DataFrames.jl. Synthesize input frames in the test.
- **Arrays**: NumPy / Julia arrays. Small arrays are the substitute for large ones; CPU is the substitute for GPU.
- **Local databases**: SQLite, DuckDB. Spin up an in-memory instance per test.
- **Plotting backends**: matplotlib's `Agg` backend, headless rendering. Assert on the figure object or saved bytes, not on visual diff.

If the dependency *doesn't* have a usable local substitute, treat it as one of the next two categories.

### 3. Remote but owned (Ports & Adapters)

Compute or storage you control, sitting across a process or network boundary: a SLURM/PBS cluster, a Dask/Ray scheduler, an internal run database, a tracking server (MLflow / W&B) you administer, an in-house dispatch/dispersion service. Define a **port** (interface) at the seam. The deep module owns the science; the transport is injected as an **adapter**. Tests use an in-memory or single-process adapter. Production uses the cluster/service adapter.

Recommendation shape: *"Define a `Backend` port at the seam, implement a `DaskBackend` for cluster runs and a `LocalBackend` (or `SerialBackend`) for tests, so the fleet-emissions calculation sits in one deep module even though it fans out across thousands of flights on a cluster."*

This pattern also covers caching: a `Cache` port with a `DiskCache` adapter (Parquet/HDF5 on a shared filesystem) for production and an `InMemoryCache` adapter for tests is a textbook two-adapter seam — useful for expensive contrail simulations or reanalysis lookups.

### 4. True external (Mock)

Things you don't control: third-party reanalysis or weather services (Copernicus CDS for ERA5, NASA GES DISC for MERRA-2, ECMWF MARS), aviation data feeds (OpenSky, ADS-B Exchange, FAA/Eurocontrol services), cloud object stores (S3, GCS), paid LLM/inference APIs, commercially licensed solvers and tools (Gurobi, CPLEX, proprietary engine cycle decks). The deepened module takes the external dependency as an injected port; tests provide a mock adapter that returns recorded responses or a synthetic generator.

For external data feeds specifically: prefer a port whose adapter can be backed by either the live service *or* a recorded-trace fake (a stored NetCDF slice, a captured ADS-B day). A trace fake is usually more valuable than a hand-written mock — it preserves the data's actual shape, gaps, and pathologies.

## Stochasticity is a seam

Random number generation deserves its own treatment because it shows up everywhere in research code and is almost always handled poorly.

- **Symptom**: the module calls `np.random.randn(...)` directly, or `Random.randn()` with the global RNG, or sets `torch.manual_seed(...)` inside the function. Tests are flaky or pinned to a magic seed nobody remembers picking.
- **Deepening move**: take an RNG as an explicit parameter. In Python, accept a `np.random.Generator` (modern API) or `torch.Generator`. In Julia, accept an `AbstractRNG`. Pass it down. Never read a global.
- **Seam character**: this is an in-process seam. The "adapter" choices are real (`default_rng(seed)` for runs, a fixed-seed `Generator` for tests, occasionally a counter-based RNG like `random123` for parallel reproducibility) and the seam is non-negotiable for any module that claims to be reproducible.

If the deepening candidate has stochastic behaviour, the recommendation should always include "the RNG becomes part of the interface."

## Seam discipline

- **One adapter means a hypothetical seam. Two adapters means a real one.** Don't introduce a port unless at least two adapters are justified (typically production + test, or two real backends like `Scipy` and `JAX`). A single-adapter seam is just indirection.
- **Internal seams vs external seams.** A deep module can have internal seams (private to its implementation, used by its own tests) as well as the external seam at its interface. Don't expose internal seams through the interface just because tests use them.
- **Configuration is part of the interface.** A module configured by reading `os.environ` or a global `config.yaml` has a hidden seam. If the config matters, take it as a parameter (a dataclass, a `pydantic` model, a Julia `struct`); if it doesn't, drop it.

## Testing strategy: replace, don't layer

- Old unit tests on shallow modules become waste once tests at the deepened module's interface exist — delete them.
- Write new tests at the deepened module's interface. The **interface is the test surface**.
- Tests assert on observable outcomes through the interface (output array, fitted parameters, figure object, written file, returned DataFrame), not on internal call sequences.
- Tests should survive internal refactors — they describe behaviour, not implementation. If a test has to change when you swap a `for` loop for a vectorized op, it's testing past the interface.
- For numerical modules, "observable outcome" means tolerances and invariants, not bit-exact equality. Prefer property tests (energy conservation, monotonicity, symmetry, scale invariance, gradient checks) over snapshot tests of array contents.
