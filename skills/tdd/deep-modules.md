# Deep Modules

From "A Philosophy of Software Design":

**Deep module** = small interface + lots of implementation

```
┌─────────────────────┐
│   Small Interface   │  ← Few functions, simple params
├─────────────────────┤
│                     │
│                     │
│  Deep Implementation│  ← Complex numerics hidden
│                     │
│                     │
└─────────────────────┘
```

A drag build-up module exposing one function `total_drag(ac, state) -> Cd` and hiding the friction, induced, wave, and interference contributions inside is deep. The caller doesn't need to know which Reynolds-number correlation or wave-drag rise model is being used.

**Shallow module** = large interface + little implementation (avoid)

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Many functions, leaky params
├─────────────────────────────────┤
│  Thin Implementation            │  ← Just passes through
└─────────────────────────────────┘
```

A drag module that requires the caller to separately invoke `friction_drag`, `induced_drag`, `wave_drag`, then sum them — and exposes the Reynolds-number correlation choice as a parameter on every call — is shallow. Internals leak into the caller.

When designing interfaces, ask:

- Can I reduce the number of exported functions / methods?
- Can I simplify the parameters? (A whole `FlightState` struct may be cleaner than 8 scalars.)
- Can I hide more numerical machinery inside? (Solver tolerances, iteration limits, switching logic — all internal unless the user genuinely needs to override them.)
