# Refactor Candidates

After a TDD cycle, look for:

- **Duplication** → Extract a function or struct (e.g., the same Reynolds-number computation copied across drag routines)
- **Long functions** → Break into private helpers; keep tests on the public interface
- **Shallow modules** → Combine or deepen (hide solver knobs, expose results)
- **Feature envy** → Move logic to where the data lives (e.g., a method on the `Wing` struct rather than a free function reaching into its fields)
- **Primitive obsession** → Introduce small types for physical quantities or grouped state (`FlightState`, `Atmosphere`, or `Unitful` quantities) instead of passing tuples of bare floats whose units and order callers must remember
- **Magic numbers** → Name constants (`γ_air = 1.4`, `R_specific_air = 287.05`) and locate them next to the physics that uses them
- **Existing code** the new code reveals as problematic — note it and discuss before sprawling the refactor scope
