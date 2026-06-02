---
name: research-schematics
description: Author conceptual and structural scientific diagrams for research manuscripts as clean, editable, vector SVG — mechanism schematics, model/data pipelines and workflows, system-boundary/LCA diagrams, experimental apparatus/setup, block/flow/architecture diagrams, geometry/domain schematics, and conceptual frameworks. Diagrams are written as SVG markup (by a capable model or by hand) to a strict set of visual rules, then rendered to vector PDF. Use for any non-data diagram (trigger words: schematic, conceptual diagram, flowchart, mechanism, block diagram, system boundary, pipeline/workflow diagram, apparatus/setup, architecture diagram, computational domain). Real selectable text, colorblind-safe, never AI raster images. Climate and aerospace diagrams ship as worked examples.
allowed-tools: Read Write Edit Bash
---

# Research Schematics — Conceptual & Structural Diagrams (SVG)

## Approach: author clean SVG, then render to vector PDF

Conceptual diagrams are authored as **SVG markup** — written by a capable model (e.g.
Sonnet) prompted to the rules below, or by hand — and then rendered to vector PDF for the
manuscript. A model asked to write an SVG to a tight spec produces a **prettier, more
modern** diagram than rigid code templates, while SVG keeps everything a manuscript needs:
true **vector**, **real selectable text**, and fully **editable** source you can restyle or
correct at any time.

This is **not** AI raster image generation. There is no pixel model in the loop — the
output is plain SVG (`<rect>`, `<path>`, `<text>`), reviewed and edited like source code.
AI raster "schematics" garble labels, invent arrows, and can't be edited or re-exported at
column width; SVG has none of those problems.

**Data vs. concept — the split that decides the skill.** For *data* plots — anything driven
by numbers where the axes carry meaning (bar charts, maps, time series, polars,
distributions, performance/parameter maps) — use **`research-figures`**. This skill is for
the **conceptual/structural** diagrams that explain a *mechanism*, a *workflow*, a *system
boundary*, an *apparatus*, an *architecture*, or a *geometry* — diagrams whose content is
the relationships between labeled parts, not the values on an axis.

## Workflow

1. **Describe the structure** — nodes (boxes), edges (arrows), branches/grouping, and the
   left→right or top→down reading order. Pick a grid. One idea per diagram.
2. **Author the SVG to the hard rules** in `references/svg_authoring_guidelines.md` — have a
   strong model write it, or write it directly. Copy `examples/model_pipeline.svg` as a
   starting point.
3. **Render and inspect** at the final column width and in grayscale:
   ```bash
   rsvg-convert -f pdf -o diagram.pdf diagram.svg          # manuscript vector
   rsvg-convert -f png --zoom 3 -o diagram.png diagram.svg # preview / grayscale check
   ```
4. **Iterate** — fix any covered text, misalignment, or per-word/per-line text splitting,
   then re-render.

## The hard rules (full detail → `references/svg_authoring_guidelines.md`)

These are non-negotiable; most exist because they are the ways model-written SVG usually
goes wrong:

1. **One `<text>` element per label/sentence — never one per word.** A phrase like
   "Contrail model" is a single `<text>`, not one `<text>` per word.
2. **A multi-line label is one `<text>` with `<tspan>` lines — never separate text boxes.**
   Break lines with `<tspan x="…" dy="1.2em">` inside the same `<text>`.
3. **Real text, not paths.** One `font-family` on the root `<svg>`; never outline text.
4. **Text on top, never covered.** SVG paint order = document order (no z-index): draw
   shapes and connectors first, the text layer **last**, and verify nothing overlaps a label.
5. **Colorblind-safe, grayscale-legible color** — Okabe-Ito **pale fills + strong same-hue
   strokes**; carry meaning by position/stroke/arrow-style/label too, never hue alone.
6. **No title, super-title, or source text on the figure** — those belong in the manuscript
   caption (`research-writing`). The SVG holds only nodes, edges, and their labels.
7. **Consistent geometry** — grid-aligned boxes, uniform size/corner-radius/stroke, one
   reusable arrowhead `<marker>`, generous even whitespace.
8. **Valid, self-contained XML** — UTF-8, no external fonts/images, and **no `--` inside XML
   comments** (illegal; breaks every renderer). Must parse with `rsvg-convert`.

## A taxonomy of conceptual diagrams

Each type is general (any field) and illustrated by a worked example domain in
atmospheric/climate and aerospace research. Build each by adapting the rules and the
`examples/` SVG; the visual standard is identical across types.

- **Mechanism schematic** — a physical/causal process and how its stages connect, with
  directional arrows for fluxes, transitions, or effects. *e.g.* contrail / contrail-cirrus
  formation (exhaust → mixing → ice nucleation in an ice-supersaturated region → persistent
  contrail → spreading cirrus, with SW-cooling / LW-warming arrows).
- **Pipeline / workflow diagram** — data/processing flow from inputs through models to
  outputs, often with a branch (e.g. sensitivity/uncertainty). *Worked example:*
  `examples/model_pipeline.svg` (ERA5 + flight inventory → contrail model → radiative
  transfer → ERF, with a dashed uncertainty branch).
- **System-boundary / LCA diagram** — encloses the analysis scope in a dashed boundary box
  with flows crossing it. *e.g.* well-to-wake life-cycle for a fuel/SAF study.
- **Apparatus / experimental setup** — instruments, sample, sources, and signal paths in a
  measurement chain.
- **Block / flow / architecture diagram** — control loops, estimation pipelines, software or
  system architectures, decision logic, propulsion/power architectures (turbo-electric,
  hybrid).
- **Geometry / domain schematic** — a labeled, dimensioned drawing of an object or a
  computational/spatial domain. *e.g.* an aircraft three-view with span/length/chord
  references; a CFD domain with farfield/inlet/outlet/wall boundary conditions and a
  refinement region.
- **Conceptual framework** — boxes-and-relationships organizing ideas, hypotheses, or
  categories (a driver→response framework, a typology, a theory-of-change).

## Design standards (also in the guidelines + `journal_guidelines.md`)

Vector output; fonts ≥ ~8 pt at final column width (≈14 px in a ~900-unit viewBox rendered
to one column); a single sans-serif family (Arial/Helvetica) across all figures;
colorblind-safe Okabe-Ito; grayscale-legible (shape/stroke/position/label, not hue alone);
one idea per diagram; grid-aligned boxes with consistent radii and stroke weights; a
self-contained caption (written with `research-writing`, not on the figure).

## How it fits the workflow

`research-writing` decides which schematics a paper needs, where they go, and how their
captions read; this skill authors them as SVG; `research-figures` builds the data plots;
`research-critique` checks that every diagram is legible in grayscale, has a self-contained
caption, and is referenced result-first in the prose.

> Need a LaTeX-native, equation-heavy diagram inside a TikZ document? That is the one case
> where TikZ can still be the right tool; this skill otherwise standardizes on SVG for the
> cleaner result and the model-authoring workflow. Ask if you want a TikZ template restored.

## References / Examples
- `references/svg_authoring_guidelines.md` — **the authoring contract**: hard rules,
  good/bad snippets, Okabe-Ito palette, reusable arrowhead/box patterns, render commands,
  and a pre-delivery checklist. Read this before authoring.
- `examples/model_pipeline.svg` — worked, polished SVG to copy from (pipeline with a dashed
  uncertainty branch; demonstrates single-`<text>` labels and a `<tspan>` multi-line label).
- `references/journal_guidelines.md` — figure specs per target journal.
- `references/house_style.md` — figure & caption conventions (voice layer).
- `references/atmospheric_climate_style.md`, `references/aiaa_engineering_style.md` §4 —
  field grounding for the worked-example domains.
