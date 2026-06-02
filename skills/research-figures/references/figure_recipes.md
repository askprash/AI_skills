# Figure Recipes — Aviation Climate & Aerospace Engineering

Field-specific figure catalog for the research-figures skill. Two families:
Family A covers atmospheric/climate figures (use for E&ES, ACP, AMT, GRL, Nature family);
Family B covers aerospace engineering figures (use for AIAA journals and conference papers).

Drawn from conventions in `atmospheric_climate_style.md` §F and
`aiaa_engineering_style.md` §4.

---

## Family A — Aviation Climate & Atmospheric Science

### A1. Forcing-components bar chart

**When to use.** Any paper that presents or compares aviation ERF/RF components across
forcing agents (contrail cirrus, CO₂, NOₓ, water vapour, aerosols). This is the canonical
figure type in the field — every assessment paper has one. The benchmark is Lee et al.
(2021) Fig. 2.

**Key design choices.**
- Horizontal bars ordered by absolute magnitude of best estimate, largest at top.
- Red (Okabe-Ito vermilion `#D55E00`) for warming; blue (`#0072B2`) for cooling.
  Never map warming=red/cooling=blue with a saturated red that prints poorly in grayscale —
  Okabe-Ito holds up.
- Asymmetric 5–95 % error bars as a separate `ax.errorbar` call with `xerr` taking a
  2×N array `[lo_dist, hi_dist]` where distances are positive.
- Separate net-total bar below a thin dashed separator line. Use a dark charcoal
  (`#2C3E50`) for the total so it visually anchors the figure.
- Zero reference line in dark grey; thin (linewidth ≈ 0.8).
- Do NOT use symmetric ±σ bars — aviation ERF distributions are skewed.
- Caption must state: year, what the bars represent (ERF vs RF), the 5–95 % percentile
  definition, and the primary source.

**What makes it effective.** The human eye reads length naturally, so horizontal bars
outperform vertical ones when label text is long. Ordering by magnitude lets reviewers
immediately see the dominant contributors. Colour-coded sign removes the need for a
legend in many cases.

**Caption guidance.**
> "Aviation ERF components for [year], central estimates and 5–95 % likelihood ranges
> (mW m⁻²). Red bars indicate net warming; blue indicate net cooling. The net total
> (bottom) is not the arithmetic sum of components due to non-linear interactions.
> Values are illustrative estimates consistent with Lee et al. (2021) Table 2."

**Script:** `scripts/forcing_bar_chart.py`

---

### A2. Global contrail RF / coverage map

**When to use.** Papers presenting spatial distributions of contrail radiative forcing,
contrail coverage fraction, or energy forcing density. Standard for model output
validation, regional hotspot identification, or scenario comparison.

**Key design choices.**
- Robinson projection for global display (preserves mid-latitude shapes better than
  Mercator).
- Diverging colormap (`RdBu_r` with `TwoSlopeNorm(vcenter=0)`) for net RF; sequential
  (`viridis`) for coverage fraction.
- Colorbar horizontal below map, labeled in mW m⁻².
- Zero contour as a thin black isoline.
- Coastlines at linewidth 0.3 for print.
- Regional callout annotations for N. Atlantic, Europe, N. Pacific corridors.

**What makes it effective.** Geographic context immediately communicates where the
forcing matters. Diverging scale around zero makes sign visible at a glance. Robinson
avoids the Arctic distortion of Mercator that would visually over-weight high latitudes.

**Caption guidance.**
> "Spatial distribution of contrail [net ERF / coverage] for [year] from [model] with
> [meteorology]. [Positive/red = warming; negative/blue = cooling.] Hatching indicates
> regions where the 5–95 % range spans zero. Grid: [resolution]."

**Recipe:** `references/maps_recipe.md` (requires cartopy)

---

### A3. Time series with uncertainty band

**When to use.** Trend analysis of forcing, emissions, fuel burn, or coverage over
multi-decadal periods. Essential when showing the 2020 COVID-19 dip, which has become
a standard reference point in recent papers (Teoh et al. 2024).

**Key design choices.**
- Central estimate as a solid line; 5–95 % range as a `fill_between` band (alpha ≈ 0.2).
- Annotate the COVID dip explicitly with an arrow and year label — reviewers will ask.
- Year on x-axis; forcing in mW m⁻² on y.
- If showing multiple scenarios, use Okabe-Ito colors and a legend.
- For multi-panel figures (e.g., forcing + fuel burn stacked), share the x-axis.

**What makes it effective.** Shaded bands are more honest than single lines for model
ensembles. The COVID dip acts as a natural validation point: models that predicted a
proportional drop match the observed signal and this comparison belongs in text.

**Caption guidance.**
> "[Quantity] from [year1] to [year2] (central estimate, solid line) with 5–95 %
> uncertainty range (shading). The 2020 reduction reflects COVID-19-related traffic
> collapse (~73 % reduction in RPK). Data: [source/model]."

**Script:** `scripts/time_series_uncertainty.py`

---

### A4. Distribution / concentration plots (Lorenz-style)

**When to use.** Showing that a small fraction of flights dominates the total effect —
the "2 % of flights → 80 % of energy forcing" result from Teoh et al. (2020). Also for
PDF/violin plots of ERF per flight, flight duration, or waypoint humidity.

**Key design choices.**
- Cumulative distribution: x = cumulative fraction of flights (sorted by EF, lowest
  first); y = cumulative fraction of total energy forcing.
- Mark the 2 %/80 % (or your result's equivalent) with reference lines.
- For PDFs: violin plots preferred over box plots when the distribution shape matters;
  include the median and IQR as horizontal lines within the violin.
- Log-scale x-axis if the distribution spans orders of magnitude (common for EF/flight).

**What makes it effective.** The Lorenz curve makes the inequality of forcing
immediately legible to readers — the 45° line is the "equal distribution" reference,
and the area between curve and diagonal quantifies the Gini coefficient of forcing.

**Caption guidance.**
> "Cumulative distribution of energy forcing (EF) per flight. Flights are ranked from
> lowest to highest EF. The vertical dashed line marks the top [X] % of flights by EF,
> which account for [Y] % of total energy forcing. Year: [year]; dataset: [source]."

---

### A5. Mitigation scatter / Pareto front

**When to use.** Papers evaluating contrail avoidance strategies — re-routing, altitude
changes, timing shifts. The standard trade-off is ERF reduction (%) vs fuel penalty (%).

**Key design choices.**
- Each point = one flight or one strategy option.
- Pareto-optimal points highlighted in a contrasting color (e.g., Okabe-Ito vermilion).
- Pareto front traced as a line through the non-dominated points.
- Knee point marked with a star marker — this is the balanced design recommendation.
- Background points in grey (alpha ≈ 0.5) to show solution density.
- Axes: fuel penalty on x (cost), ERF reduction on y (benefit). Both in percent.

**What makes it effective.** The Pareto front tells the reader the best achievable
trade-off surface; the knee point gives an actionable recommendation without requiring
the reader to pick their own preference weights.

**Caption guidance.**
> "Trade-off between contrail ERF reduction and fuel penalty for [N] [re-routed flights /
> strategy variants]. Blue points: Pareto-optimal solutions. Star: knee point (maximum
> curvature of the Pareto front). Grey: dominated solutions. [Year/scenario/dataset]."

**Script:** `scripts/pareto_front.py`

---

## Family B — Aerospace Engineering (AIAA)

### B1. Aircraft geometry: three-view and computational-domain schematic

**When to use.** Any paper introducing a novel configuration (BWB, TTBW, HWB, eVTOL,
etc.). The three-view (top, side, front) communicates reference dimensions to reviewers.
The domain schematic is mandatory for CFD papers (AIAA V&V policy).

**Key design choices.**
- Three-view: dimensioned orthographic projections; label span, chord, sweep, and
  reference area in both SI and imperial (AIAA dual-unit convention).
- Domain schematic: show inlet/outlet boundary conditions by type (freestream, outflow,
  symmetry, wall); label domain extent in chord lengths (e.g., "20c upstream").
- Grid topology inset (O-grid near surface, C-grid near wake) is expected for RANS papers.
- Use `matplotlib.patches` or a schematics tool (`research-schematics` skill) — never
  raster screenshots of CAD.

**What makes it effective.** Reviewers check whether the domain is large enough to
avoid boundary reflections, and whether the grid resolves the boundary layer (y⁺ ≤ 1
for wall-resolved LES / y⁺ ≈ 30–100 for wall-modeled RANS). This figure answers both.

**Caption guidance.**
> "Computational domain for [configuration] RANS simulation at M [number], Re [number].
> Domain extends [X]c upstream, [Y]c downstream, [Z]c spanwise. Boundary conditions:
> freestream (inlet/top/bottom/sides), outflow (exit), no-slip wall (surface).
> Inset: surface grid at [location], y⁺_avg = [value]."

---

### B2. Aerodynamic polars: C_L, C_D, L/D vs alpha

**When to use.** The standard "money figure" for any aerodynamics paper. Present at
minimum: C_L vs alpha, C_D vs alpha, and the drag polar (C_L vs C_D). L/D vs alpha
completes the performance picture.

**Key design choices.**
- Dual-panel layout: polar (C_L vs C_D) left, L/D vs alpha right. Or 2×2 for full set.
- Mark the design point (max L/D) with a contrasting marker + annotation.
- Draw constant-L/D tangent lines from the origin on the drag polar as thin grey dashed
  lines.
- Include stall break clearly — a sharp change in slope or a separate marker at C_L_max.
- Error bars on experimental data points; shade CFD GCI band if multi-fidelity comparison.
- AIAA: ≥8 pt fonts at 3.25 in (single column).

**What makes it effective.** The drag polar compresses the entire performance envelope
into one curve; engineers immediately read off (L/D)_max as the tangent from origin.
The L/D vs alpha panel is more intuitive for structural and propulsion engineers.

**Caption guidance.**
> "(a) Drag polar and (b) lift-to-drag ratio for [configuration] at [conditions].
> Solid line: [method, e.g., RANS k–ω SST]. Symbols: [experiment/reference, if any].
> Design point (★): maximum L/D = [value] at α = [value]°. CD0 = [value], k = [value]."

**Script:** `scripts/drag_polar.py`

---

### B3. C_p distribution

**When to use.** Validating CFD surface pressure against experiment; showing shock
location; comparing baseline vs optimized geometry.

**Key design choices.**
- y-axis inverted (−C_p up is the convention; suction positive upward). Label clearly.
- Upper and lower surface distinguished by line style or color.
- Mark shock location with a vertical dashed line if present.
- For span stations in 3D: one panel per cut (e.g., η = 0.3, 0.6, 0.9).
- Experiment: symbols only (no connecting line — each point is independent).

**Caption guidance.**
> "Chordwise C_p distribution at η = [value] for [configuration] at M = [value],
> α = [value]°, Re = [value]. Line: RANS [solver/turbulence model]; symbols:
> wind-tunnel data from [source]. [Upper surface: solid; lower surface: dashed.]"

---

### B4. Compressor / fan performance map

**When to use.** Propulsion papers presenting fan or compressor characterization:
total pressure ratio (PR) vs corrected mass flow, with speed lines and surge line.
Efficiency overlay as color fill or iso-efficiency contours.

**Key design choices.**
- Speed lines as separate curves, labeled by % design corrected speed (60, 70, 80, 90,
  100 %).
- Surge line as a thick dashed red line connecting the stall points.
- Efficiency overlay: iso-efficiency contours (e.g., 0.80, 0.85, 0.88, 0.90 isentropic)
  as thin grey contour lines. Color fill with `viridis` or `cividis` is acceptable;
  never jet.
- Mark the design point (DP) with a star marker.
- Choke line (vertical mass flow limit at PR ≈ 1) at the right edge of each speed line.
- Use `np.interp` or a cubic spline for smooth speed lines from sparse map data.

**Caption guidance.**
> "Compressor performance map: total pressure ratio vs corrected mass flow rate.
> Speed lines: [percentages] of design corrected speed N/√T. Dashed red line: predicted
> surge line. Iso-efficiency contours (isentropic, %) shown in grey. Design point (★)
> at [conditions]. Validated against [source]."

---

### B5. T–s / h–s thermodynamic cycle diagram

**When to use.** Propulsion cycle papers — turbojet, turbofan, hybrid-electric, hydrogen
combustion, SAF cycle comparisons. Maps each thermodynamic process (compression,
combustion, expansion) in the state space.

**Key design choices.**
- State points numbered or labeled (1 = inlet, 2 = fan exit, 3 = HPC exit, 4 = combustor
  exit, 5 = HPT exit, etc.). Be consistent with your nomenclature section.
- Processes connected as lines (isentropic = vertical in h–s; isobaric = curved; isothermal
  = horizontal in T–s).
- Multiple cycles (e.g., baseline vs SAF) overlaid with Okabe-Ito colors.
- Axes: entropy s (kJ/kg·K) and temperature T (K) or specific enthalpy h (kJ/kg).

**Caption guidance.**
> "T–s diagram for [cycle name] at [design point conditions]. State points [1–N] labeled.
> [Solid: design; dashed: off-design at [condition].] Ideal gas assumed; γ = [value],
> cp = [value] kJ/kg·K."

---

### B6. Grid-convergence / GCI plot

**When to use.** Required in all AIAA CFD papers. Shows that the reported result is
grid-independent, quantifies the numerical discretization error, and provides the
Richardson-extrapolated limit.

**Key design choices.**
- x-axis: mesh spacing h (normalized so coarsest = 1.0). Alternatively: number of cells
  (then invert x-axis or label "finer →").
- y-axis: the reported quantity (C_L, C_T, pressure recovery, etc.).
- Three or more mesh levels required (AIAA policy).
- Richardson-extrapolated value as a horizontal dashed line with label.
- GCI error bars (Celik et al. 2008, Fs = 1.25 for three or more meshes) on fine and
  medium mesh points.
- Annotate observed order of convergence p.
- GCI_fine < 1 % is required for a clean V&V section; 1–5 % requires discussion.

**What makes it effective.** The convergence toward the RE value visually demonstrates
grid independence more compellingly than a table alone. Reviewers at AIAA are trained to
look for this figure; its absence is a frequent desk-reject trigger.

**Caption guidance.**
> "Grid-convergence study for [quantity] at [conditions]. Three mesh levels (coarse,
> medium, fine; h normalized to coarsest). Richardson-extrapolated value:
> Q_RE = [value]. GCI_fine = [X] %, GCI_medium = [Y] % (Fs = 1.25; Celik et al. 2008).
> Observed order of convergence: p = [value] (theoretical: [value] for [scheme])."

**Script:** `scripts/gci_convergence.py`

---

## Cross-family notes

- All figures must export cleanly as PDF (vector) + PNG (raster). Use `figure_export.save_figure()`.
- All figures must be legible in grayscale. Use `figure_export.grayscale_preview()` before submission.
- Never use jet, rainbow, or hsv colormaps.
- For color palettes, see `assets/palettes.py` — Okabe-Ito for categorical, `RdBu_r` for diverging,
  `viridis`/`cividis` for sequential.
- Per-journal sizing and DPI: see `figure_export.list_journals()` or `journal_guidelines.md`.
