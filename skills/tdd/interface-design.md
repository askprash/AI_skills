# Interface Design for Testability

Good interfaces make testing natural:

1. **Accept dependencies, don't create them**

   ```julia
   # Testable: pass the atmosphere/engine model in
   compute_cruise(ac, atmos, engine_deck) = ...

   # Hard to test: hidden global construction
   function compute_cruise(ac)
       atmos  = ISAAtmosphere()
       engine = load_deck(ENV["ENGINE_DECK"])
       ...
   end
   ```

2. **Return results, don't mutate hidden state**

   ```python
   # Testable
   def trim_aircraft(state, controls) -> TrimResult: ...

   # Hard to test — mutation buried inside an aggregate
   def trim_aircraft(aircraft) -> None:
       aircraft.state.alpha = ...
       aircraft.state.elevator = ...
   ```

   Performance note: in Julia, in-place `!` functions are idiomatic for hot loops. That's fine — but the *outer* interface you test should still take inputs and return a result (or write into a caller-supplied buffer that the test owns and inspects). Keep the mutation local and explicit.

3. **Small surface area**

   - Fewer functions = fewer tests needed
   - Fewer parameters = simpler test setup
   - One module, one responsibility (atmosphere, drag build-up, mission integration)

4. **Push side effects to the edges**

   The core numerics should be pure functions of their inputs. File reads, plotting, logging, and database writes go in a thin shell around them. The pure core is trivially testable; the shell needs only a few smoke tests.
