# Good and Bad Tests

## Good Tests

**Integration-style**: Test through real interfaces, not mocks of internal parts. Anchor numerical assertions to physics, analytical solutions, conservation laws, or trusted reference values — never to whatever number the code happens to produce today.

```julia
# GOOD: Tests observable behavior against a known physical value
@testset "ISA atmosphere" begin
    p, T, ρ = isa_atmosphere(0.0)            # sea level
    @test p ≈ 101325.0 atol=1.0
    @test T ≈ 288.15   atol=0.01
end

@testset "design mission fuel burn" begin
    ac = load_aircraft("b738.toml")
    result = size_mission(ac)
    @test result.converged
    @test result.fuel_burn ≈ 20_500.0 rtol=5e-3   # vs. published reference
end
```

```python
# GOOD: Tests observable behavior
def test_drag_polar_matches_reference():
    cl = np.linspace(0.0, 1.2, 13)
    cd = drag_polar(cl, mach=0.78, altitude=10_668)
    cd_ref = np.loadtxt("references/b738_polar_M078.csv")
    np.testing.assert_allclose(cd, cd_ref, rtol=1e-3)
```

Characteristics:

- Tests behavior callers care about (a converged result, a physical quantity)
- Uses public API only
- Survives internal refactors (changing the integration scheme shouldn't break it)
- Describes WHAT, not HOW
- One logical assertion per test; tolerances are explicit and justified

## Bad Tests

**Implementation-detail tests**: Coupled to internal structure.

```julia
# BAD: Tests implementation details
@testset "size_mission calls compute_drag" begin
    calls = Ref(0)
    patched_drag = (args...) -> (calls[] += 1; 0.025)
    size_mission(ac; drag_fn=patched_drag)
    @test calls[] == 7    # asserts iteration count, not the answer
end
```

```python
# BAD: Reaches into private state
def test_solver_internal_residual():
    sol = NewtonSolver(f)
    sol.solve(x0)
    assert sol._residual_history[-1] < 1e-8   # private field
```

Red flags:

- Mocking internal collaborators (your own drag model, your own atmosphere model)
- Testing private functions or fields (anything starting with `_` in Python, non-exported names in Julia)
- Asserting on iteration counts, call counts, or call order
- Snapshotting whatever number came out, with no physical justification for the value
- Test breaks when refactoring without behavior change
- Test name describes HOW not WHAT
- Verifying through internal state instead of the returned result

```python
# BAD: Bypasses interface and snapshots an arbitrary number
def test_lift_coefficient():
    wing = Wing(span=35.0, area=124.0)
    wing._build_panels()                    # private
    assert wing._panels[0].cl == 0.4123     # snapshot, no physical meaning

# GOOD: Verifies through interface against a meaningful baseline
def test_elliptic_wing_matches_lifting_line_theory():
    wing = Wing(span=35.0, area=124.0, planform="elliptic")
    cl, cdi = wing.aero(alpha=5.0, mach=0.0)
    # Prandtl lifting-line: CDi = CL^2 / (pi * AR) for elliptic loading
    AR = 35.0**2 / 124.0
    assert cdi == pytest.approx(cl**2 / (np.pi * AR), rel=1e-3)
```

## Choosing Tolerances

Numerical tests need tolerances. Pick them deliberately:

- **Tight (`rtol=1e-10`)**: only when comparing to an analytical solution or to deterministic bit-for-bit output
- **Loose (`rtol=1e-2` to `1e-3`)**: comparing iterative solvers, ODE integrations, or different implementations of the same physics
- **Documented**: write a comment when the tolerance reflects a physical or numerical reason (e.g., "RK4 truncation error at this step size")

A test that passes with `rtol=1e-1` but no justification is usually hiding a bug or an arbitrary snapshot.
