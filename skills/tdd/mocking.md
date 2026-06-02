# When to Mock

In scientific code, mocking is rarer than in web/backend code — most of what you compute is deterministic math you actually want to exercise. Mock at **system boundaries** only:

- External solvers or processes (CFD runs, optimization servers, subprocess calls to compiled binaries)
- File I/O for large input decks or experimental data (sometimes — prefer a tiny real fixture)
- Network calls (remote databases, weather/atmosphere services)
- Time and randomness (RNG seeds, wall-clock timers used for performance gating)

Don't mock:

- Your own physics models, solvers, or numerics
- Internal collaborators (e.g., the atmosphere model called by your drag routine)
- Pure functions you control — just call them

In Julia, mocking is often unnecessary: pass an alternative function or a different concrete type via multiple dispatch. In Python, the same is true with dependency injection — reach for `unittest.mock` only at true boundaries.

## Designing for Mockability

At system boundaries, design interfaces that are easy to substitute:

**1. Use dependency injection**

Pass external dependencies in rather than constructing them internally:

```julia
# Easy to substitute
size_mission(ac; atmos = ISAAtmosphere(), engine_deck = load_deck("CFM56.dat"))

# Hard to substitute — hidden globals
function size_mission(ac)
    atmos = ISAAtmosphere()
    deck  = load_deck(ENV["ENGINE_DECK"])
    ...
end
```

```python
# Easy to substitute
def run_optimization(problem, solver):
    return solver.solve(problem)

# Hard to substitute
def run_optimization(problem):
    solver = IPOPT(license_path=os.environ["IPOPT_LIC"])
    return solver.solve(problem)
```

**2. Prefer specific functions over one generic dispatcher**

Create a separate function for each external operation rather than one generic call with a mode flag:

```python
# GOOD: Each function is independently substitutable
class EngineDB:
    def get_thrust_table(self, engine_id): ...
    def get_sfc_table(self, engine_id): ...
    def get_weight(self, engine_id): ...

# BAD: Mocking requires conditional logic inside the substitute
class EngineDB:
    def query(self, kind, engine_id): ...   # kind in {"thrust","sfc","weight"}
```

The specific-function approach means:

- Each substitute returns one specific shape
- No `if kind == ...` ladders in test setup
- Easier to see which external lookups a test exercises
- Type stability per call (matters for Julia performance tests too)

**3. Make randomness and time explicit**

If a result depends on random draws (Monte Carlo, stochastic optimization, perturbed initial conditions) or wall-clock time, take an RNG or clock as an argument. Then a test passes a seeded RNG and gets reproducibility for free, without a mock.

```julia
monte_carlo_range(ac; rng=Random.default_rng(), n=1000)
# Test passes rng = Xoshiro(42) for a deterministic, exact assertion.
```
