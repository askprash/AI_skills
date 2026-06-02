---
name: research-figures
description: >
  Build publication-quality DATA figures for any research field — always vector and
  fully reproducible from code (matplotlib + numpy; cartopy for maps), never AI raster
  image generation. Handles journal-correct column sizing and DPI, colorblind-safe
  (Okabe-Ito) and grayscale-legible color, multi-panel layouts, uncertainty bands, and
  per-journal export (PDF + PNG) via save_figure(). Ships worked examples from climate /
  atmospheric science (ERF/forcing bar charts, contrail RF maps, time series with
  uncertainty, Lorenz/distribution, mitigation Pareto fronts) and from aerospace / AIAA
  engineering (drag polars, C_p distributions, compressor/fan maps, T–s cycle diagrams,
  GCI grid-convergence, MDO Pareto fronts), readily adapted to other domains. Use this
  skill whenever the user asks to: make a publication figure, plot, journal figure,
  vector figure, forcing/ERF bar chart, drag polar, compressor map, GCI / grid-convergence
  / grid-independence plot, uncertainty band, time series, Pareto front, or any
  matplotlib figure for a paper or AIAA submission. For conceptual / structural vector
  diagrams (mechanisms, pipelines, system boundaries, three-view geometry) use
  research-schematics; for fine-grained low-level control of any plot element or a novel
  plot type, use the matplotlib skill.
allowed-tools: Read Write Edit Bash
metadata:
  domain: general academic; worked examples in atmospheric/climate & aerospace/AIAA
  style-variants: print (prash_print.mplstyle), slides (prash_slides.mplstyle)
---

# research-figures skill

This skill produces reproducible, journal-ready **data** figures for research papers in
any field. Every figure is generated entirely from code — matplotlib, numpy, and
optionally cartopy for global maps — so it is vector-first (PDF/EPS), exact, and
re-runnable. The skill carries fully worked examples from two domains the author
publishes in — climate / atmospheric science and aerospace / AIAA engineering — but the
workflow, export helper, and styling apply to any quantitative figure.

## When to invoke this skill

Reach for this skill any time you need a figure for a paper submission, not just a quick
plot. The distinction matters: journal figures require correct column widths, DPI, font
sizes at final print size, colorblind-safe palettes, and grayscale legibility. The export
helper handles all of that automatically once you name the target journal.

Use a different skill when the task is not a data plot:

- **Conceptual / structural diagrams** — mechanism sketches, data pipelines, system
  boundaries, aircraft three-views, CAD-style geometry — go to **research-schematics**
  (vector diagrams that go beyond matplotlib's native plotting).
- **Fine-grained, low-level control of any plot element, or a genuinely novel plot type**
  not covered by the recipes here, go to the **matplotlib** skill. That skill stays
  separate on purpose: it documents the library at the element level (artists, transforms,
  custom projections), whereas this skill is the publication-figure layer on top of it.
- **Caption prose and uncertainty wording** are drafted with **research-writing**; a
  pre-submission **figure self-review** is run with **research-critique** (see "How this
  skill pairs with others").

## Reproducibility rule — read this first

Every figure delivered with a paper must be reproducible from a script checked into the
project repository. The script must be self-contained (no manual steps, no saved
intermediate files that aren't also in the repo), apply the print style, and call
`save_figure()` for the target journal.

**Never use AI raster/image generation for figures.** Generated images garble text and
numbers, are not reproducible, and cannot be edited or re-exported at journal DPI. All
figures here are code → vector. This is enforced for both AIAA submissions (where raster
PowerPoint figures are a common desk-reject flag) and EGU/AGU submissions (where
embedded-font vector PDF is required).

## Two style variants

The user's matplotlib style lives in two files under `assets/`:

`assets/prash_slides.mplstyle` is the presentation style: ~14–18 pt axis labels, thick
lines, grid on. Use this for talks or posters where the figure is large on screen.

`assets/prash_print.mplstyle` is the publication-print variant: 7–9 pt labels, 1 pt
lines, grid off, top/right spines removed, Okabe-Ito color cycle, tight margins. Use this
for any journal submission. The font is Arial / Helvetica (sans-serif), appropriate for
AIAA, EGU, AGU, Nature-family, and most other journals.

Apply a style at the top of any script:

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))  # scripts/ on path
from figure_export import apply_style
apply_style("print")   # or "slides"
```

## Per-journal sizing and DPI

Never set figure size by eye. Use `save_figure()` from `scripts/figure_export.py`, which
maps journal name → correct column width in mm → correct DPI, and writes PDF + PNG in one
call.

```python
from figure_export import save_figure
# Single-column EGU (ACP/AMT): 83 mm, 300 dpi, PDF + PNG
save_figure(fig, "my_figure", journal="egu", width="single", formats=["pdf", "png"])

# Double-column AIAA: 7 in (177.8 mm), 600 dpi line art
save_figure(fig, "my_figure", journal="aiaa", width="double")

# Nature family single column: 90 mm, 300 dpi
save_figure(fig, "my_figure", journal="ncc", width="single")
```

`save_figure(fig, name, journal=, width=, height_scale=, formats=, out_dir=, dpi_override=,
line_art=)` resizes the figure to the journal column width (`single`/`double`/`triple`, or
a numeric mm value), picks line-art vs raster DPI, and exports each requested format. Pass
`height_scale=None` to keep the height you already set on the figure.

Supported journal keys: `ees`, `aiaa`, `egu`, `acp`, `amt`, `agu`, `grl`, `nature`,
`ncc`, `ngeo`, `natcommun`, `science` (plus full-name aliases). Print the table any time
with `python3 scripts/figure_export.py` (runs `list_journals()`).

**Authoritative journal specs are in `references/journal_guidelines.md`** — that file is
the single source of truth for the venues this author targets, and `figure_export.py`'s
table is derived from it. For other publishers (Cell Press, PLOS, IEEE, ACS, Elsevier,
BMC) consult `references/journal_requirements.md` as additional general detail, and
`references/publication_guidelines.md` for field-agnostic figure best practices. Treat
those two as supplementary, not as a competing source of truth.

## Colorblind and grayscale discipline

All figures use the Okabe-Ito 8-color palette by default (loaded via
`assets/prash_print.mplstyle`, or explicitly from `assets/palettes.py`). This palette is
safe for deuteranopia, protanopia, and tritanopia. For a sign convention
(e.g. warming/cooling, gain/loss), use `palettes.WARMING_COOLING["positive"]` (Okabe-Ito
vermilion) and `palettes.WARMING_COOLING["negative"]` (Okabe-Ito blue):

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "assets"))
from palettes import OKABE_ITO, OKABE_ITO_LIST, WARMING_COOLING, forcing_palette
```

`assets/palettes.py` is the **canonical** palette module (it defines `OKABE_ITO`,
`OKABE_ITO_LIST`, the `WARMING_COOLING` diverging scheme used by the worked scripts, and a
`COLORMAP_RECS` table). `assets/color_palettes.py` is supplementary — reach for it only
when you need an extra named categorical palette (Wong, Paul Tol bright/muted/light/
high-contrast); do not mix the two orderings within one figure.

Before submitting any figure, run a grayscale check:

```python
from figure_export import grayscale_preview
grayscale_preview("my_figure.png", show=False)
```

This renders the PNG with luminosity-weighted conversion side by side with the original.
If information is lost in grayscale, add line styles (solid/dashed/dotted), markers, or
hatching rather than relying on color alone.

For colormaps: use `viridis` or `cividis` for sequential fields; `RdBu_r` with
`TwoSlopeNorm(vcenter=0)` for diverging fields (anomalies, scenario differences). Never
use `jet`, `rainbow`, or `hsv` — they create false gradient perception and are unreadable
in grayscale. See `COLORMAP_RECS` in `assets/palettes.py` and `references/color_palettes.md`
for the full recommendation table.

## Titles, captions, and panel labels

Follow standard academic-figure convention: **the figure itself carries no title,
super-title, or source/provenance text** — those belong in the manuscript caption
(drafted with `research-writing`), never on the axes. On the figure, keep only the data,
axis labels (with units), legends, and in-plot data annotations.

- **No `ax.set_title()` / `fig.suptitle()`** on a submission figure. The title sentence
  and any "illustrative / data source / parameters" note go in the caption — the caption
  templates live with the recipes in `references/figure_recipes.md`.
- **Label multi-panel figures** `(a)`, `(b)`, … using the helper, placed just above the
  top-left corner of each panel:

  ```python
  from figure_export import add_panel_label
  add_panel_label(ax1, "(a)")
  add_panel_label(ax2, "(b)")
  ```

  Single-panel figures need no letter. `drag_polar.py` shows the two-panel pattern; the
  other four worked scripts are single-panel and title-less.
- **Keep every text element legible and unobstructed.** Text must never be covered by a
  line, marker, or patch: give annotations a high `zorder` (e.g. `zorder=10`) and confirm
  no other artist sits on top. Related polish that keeps figures clean at print size: draw
  a reference axis line *above* the bars it anchors (raise its `zorder`), make error bars
  **thinner than the data line** and markers modest, drop bar edge colors that would cross
  an axis, and thin legend frames with `leg.get_frame().set_linewidth(0.4)`.
- **Label line series on the line, not in a legend, when it reads cleaner.** Use the
  `labellines` package (`from labellines import labelLine, labelLines`) to place a label
  directly on a curve — it adds a white halo and rotates to the line's slope — instead of an
  arrowed annotation or a legend row. `gci_convergence.py` labels its RANS and
  Richardson-extrapolation lines this way (`pip install matplotlib-label-lines`).
- **No literal Unicode arrows or symbols in labels/legends** (`↓ ↑ → ←`): depending on the
  font/PDF backend they drop to missing-glyph boxes. Use a word ("reduction", "to") or
  matplotlib mathtext (`$\rightarrow$`, `$\downarrow$`).

## Field-specific figure catalog

The canonical figure types are documented in `references/figure_recipes.md`. Read the
relevant recipe entry — it states when to use the figure, the key design decisions, what
makes it effective for reviewers in that field, and a caption template — before building a
new figure type. The catalog covers:

**Family A — climate / atmospheric science:** forcing-components (ERF/RF) bar chart,
global contrail RF / coverage map, time series with uncertainty band, distribution /
Lorenz concentration plot, mitigation scatter / Pareto front.

**Family B — aerospace engineering (AIAA):** aircraft geometry & CFD-domain schematic,
aerodynamic polars (C_L / C_D / L/D vs α), C_p distributions, compressor / fan performance
maps, T–s / h–s thermodynamic cycle diagrams, MDO Pareto fronts, and grid-convergence /
GCI plots.

These two families are worked examples, not the limits of the skill. For a plot type the
catalog does not cover — generic line/bar/scatter/box/violin/heatmap, multi-panel layouts,
significance annotations — see the general cookbook in `references/matplotlib_examples.md`,
and drop down to the **matplotlib** skill for element-level control.

For figure ordering and caption conventions — order figures configuration/geometry →
performance → comparison/demonstration, and write self-contained, interpretive captions
that name each panel and end with the key quantitative takeaway — see
`references/house_style.md` ("Figure & caption conventions"). Field-specific figure and
caption grounding is in `references/atmospheric_climate_style.md` (§F) and
`references/aiaa_engineering_style.md` (§4).

## Worked example scripts

Five scripts in `scripts/` are tested and produce PDF + PNG without error. Each is
self-contained and imports `figure_export` (apply_style, save_figure, add_panel_label)
and, where needed, `palettes`, via relative-path insertion:

`scripts/forcing_bar_chart.py` — horizontal ERF-component bar chart with asymmetric
5–95 % error bars (Lee et al. 2021-like illustrative values). Target: EGU single column.

`scripts/time_series_uncertainty.py` — annual contrail ERF time series 1990–2022 with a
shaded uncertainty band and an annotated 2020 COVID-19 dip. Target: ACP single column.

`scripts/drag_polar.py` — dual-panel drag polar (C_L vs C_D) and L/D vs α for an
illustrative transonic transport wing. Target: AIAA double column.

`scripts/pareto_front.py` — contrail mitigation Pareto front (ERF reduction vs fuel
penalty) with the non-dominated front highlighted and a knee point marked. Target: EGU
single column.

`scripts/gci_convergence.py` — four-mesh grid-convergence study with Richardson
extrapolation and GCI error bars, for an AIAA V&V section. Target: AIAA single column.

Run any script directly from `scripts/` with `python3 <script>.py` (requires
matplotlib + numpy; `gci_convergence.py` also uses `labellines` —
`pip install matplotlib-label-lines`).

## Global maps

Global maps (e.g. contrail RF) require cartopy, which is **not** part of the core
dependency set — the worked scripts run on matplotlib + numpy (with `gci_convergence.py`
also using `labellines`). A complete,
commented recipe (Robinson projection, diverging scale, regional callouts, a ready-to-run
script block calling `save_figure()`) is in `references/maps_recipe.md`. Install cartopy
with `pip install cartopy` (and `brew install proj geos` on macOS).

## Optional tools (seaborn, plotly)

The default and submission path is matplotlib + numpy via `figure_export.py`. For quick
statistical exploration, seaborn (built on matplotlib) is convenient — `sns.despine()`,
`sns.set_palette([...])` with Okabe-Ito; for interactive exploration, plotly with
`fig.write_image(..., scale=3)` for ~300 DPI static export. Examples for both are in
`references/matplotlib_examples.md`. These are optional helpers: the vector / reproducible
/ no-AI rules and the Okabe-Ito discipline above still apply, and final submission figures
should go through `save_figure()` so sizing and DPI come from `journal_guidelines.md`.
For anything novel or element-level, prefer the **matplotlib** skill.

## A note on the alternative helper modules

`scripts/figure_export.py` (style + export) and `assets/palettes.py` (palettes) are the
**canonical** API used by every example here and by the five worked scripts.

The repository also carries an alternative, biomedical-leaning helper set —
`scripts/publication_export.py` (`save_publication_figure` / `save_for_journal` /
`check_figure_size`) and `scripts/style_presets.py` (`apply_publication_style` /
`configure_for_journal` / `set_color_palette`) — with a different API and a
nature/science/cell/plos/acs/ieee journal set. Use them only if you specifically need one
of those journals or their standalone size-check / font-embedding helpers; otherwise
prefer `apply_style()` + `save_figure()` so the output matches the rest of the skill.
Each alternative module carries a header note pointing back to the canonical one.

## How this skill pairs with others

`research-writing` — for caption prose, uncertainty reporting in bracket / CI notation,
and rhetorical conventions. Draft the figure captions there once the figure is finalized
here.

`research-schematics` — for conceptual and structural vector diagrams (mechanisms,
pipelines, system boundaries, aircraft three-views, CAD-style geometry) that go beyond
matplotlib's native plotting.

`research-critique` — for checking whether an existing figure meets reviewer expectations
before submission (font sizes at final width, GCI presence for CFD, colormap choice,
grayscale legibility, etc.).

`matplotlib` (separate skill) — for fine-grained, low-level control of any plot element,
custom artists/projections, or a novel plot type not covered by the recipes here.

## References / Scripts / Assets

**`references/`**
- `figure_recipes.md` — canonical field figure catalog (Families A & B; when/why/design/
  caption per type).
- `maps_recipe.md` — cartopy global-map recipe (Robinson, diverging scale).
- `journal_guidelines.md` — **authoritative** per-journal specs for this author's target
  venues (source of `figure_export.py`'s table).
- `journal_requirements.md` — supplementary general per-publisher figure specs (Cell,
  PLOS, IEEE, ACS, Elsevier, BMC, …).
- `publication_guidelines.md` — supplementary field-agnostic figure best-practices +
  submission checklist.
- `color_palettes.md` — color/colormap guide (Okabe-Ito, Wong, Tol; sequential/diverging).
- `matplotlib_examples.md` — general plot-type cookbook (line/bar/scatter/box/violin/
  heatmap, multi-panel, seaborn, plotly); uses the canonical export API.
- `house_style.md` — figure ordering & caption conventions (authoritative voice layer).
- `atmospheric_climate_style.md`, `aiaa_engineering_style.md` — field grounding for figure
  & caption conventions.

**`scripts/`**
- `figure_export.py` — **canonical** export module: `apply_style()`, `save_figure()`,
  `add_panel_label()`, `grayscale_preview()`, `list_journals()`.
- `forcing_bar_chart.py`, `time_series_uncertainty.py`, `drag_polar.py`, `pareto_front.py`,
  `gci_convergence.py` — the five tested worked scripts.
- `publication_export.py`, `style_presets.py` — alternative/legacy helper set (different
  API; biomedical journal set). Prefer the canonical module.

**`assets/`**
- `prash_print.mplstyle` — canonical publication (print) style.
- `prash_slides.mplstyle` — canonical presentation (slides) style.
- `palettes.py` — **canonical** palettes (Okabe-Ito + `WARMING_COOLING` + `COLORMAP_RECS`).
- `color_palettes.py` — supplementary palettes (Wong, Paul Tol; helper functions).
- `nature.mplstyle`, `publication.mplstyle`, `presentation.mplstyle` — alternative vendor
  style files (the canonical styles are the `prash_*` pair).
