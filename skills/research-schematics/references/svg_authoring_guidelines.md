# SVG Authoring Guidelines — conceptual diagrams for manuscripts

Conceptual/structural diagrams (flowcharts, mechanism sketches, pipelines, system
boundaries, apparatus, block/architecture diagrams) are authored as **hand-written /
model-written SVG**, then rendered to vector PDF (and PNG for preview). A capable model
(e.g. Sonnet) asked to write an SVG to these rules produces cleaner, more modern diagrams
than rigid code templates — *provided* the rules below are enforced. SVG keeps everything
the manuscript needs: true vector, real selectable text, and fully editable source.

This is **not** AI raster image generation. There is no pixel model in the loop — the
output is plain SVG markup with real `<text>` and `<path>` elements, reviewed and edited
like any other source file.

---

## Workflow

1. **Describe the structure first** — list the nodes (boxes), the edges (arrows), the
   grouping/branches, and the left→right or top→down reading order. Decide the grid.
2. **Author the SVG to the hard rules below** (have a strong model write it, or write it
   directly). One idea per diagram.
3. **Render and inspect** at the *final* column width and in grayscale:
   ```bash
   rsvg-convert -f pdf -o model_pipeline.pdf model_pipeline.svg      # manuscript vector
   rsvg-convert -f png --zoom 3 -o model_pipeline.png model_pipeline.svg   # preview
   ```
4. **Iterate** — fix any covered text, misalignment, or per-word/per-line text splitting,
   and re-render. `examples/model_pipeline.svg` is a worked reference to copy from.

---

## Hard rules

### 1. One `<text>` element per label — never one per word
A label that is a phrase or sentence is a **single** `<text>` element containing the whole
string. Do **not** emit one `<text>` per word and position each word absolutely — this is
the most common failure when a model writes SVG, and it produces uneven spacing,
mis-kerned text, and an un-editable mess.

```xml
<!-- GOOD: one text element, the whole phrase -->
<text x="340" y="133" text-anchor="middle">Contrail model</text>

<!-- BAD: one text element per word -->
<text x="312" y="133">Contrail</text>
<text x="372" y="133">model</text>
```

### 2. A multi-line label is one `<text>` with `<tspan>` lines — never separate boxes
When a label wraps to multiple lines, keep it as **one** `<text>` element and break lines
with `<tspan>` children that share the same `x` and step down with `dy`. Do **not** create
a separate `<text>` element per line (the other common model failure).

```xml
<!-- GOOD: one text element; lines are tspans inside it -->
<text x="570" y="279" text-anchor="middle">
  <tspan x="570">Sensitivity /</tspan>
  <tspan x="570" dy="1.2em">uncertainty</tspan>
</text>

<!-- BAD: each line is its own text box -->
<text x="570" y="279">Sensitivity /</text>
<text x="570" y="299">uncertainty</text>
```

### 3. Keep text as real text — do not convert to paths
Set one `font-family` on the root `<svg>` (a system sans-serif stack, no external font
files) and never outline/flatten text to `<path>`. Real text stays searchable, editable,
restyleable, and crisp at any scale.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 910 360"
     font-family="Helvetica, Arial, sans-serif"> … </svg>
```

### 4. Text on top, never covered
SVG has no z-index — **paint order is document order**: elements written later are drawn
on top. Author shapes and connectors first, then a **text layer last**, so no fill,
arrow, or line can cover a label. After rendering, verify every label is fully legible and
nothing overlaps it. Give boxes enough padding that the text never touches an edge.

### 5. Colorblind-safe, grayscale-legible color
Use the Okabe-Ito palette as **pale fills with a strong same-hue stroke** — the lightness
difference keeps boxes distinct in grayscale, and meaning is also carried by position,
stroke, arrow style (solid vs dashed), and label, never by hue alone.

| Role        | Fill      | Stroke    |
|-------------|-----------|-----------|
| blue        | `#D6E6F2` | `#0072B2` |
| green       | `#D2EFE6` | `#009E73` |
| vermillion  | `#F6D9CC` | `#D55E00` |
| orange      | `#F9E7C7` | `#E69F00` |
| sky         | `#DCEFF9` | `#56B4E9` |
| purple      | `#F2DCE9` | `#CC79A7` |
| grey        | `#E6E6E6` | `#4D4D4D` |

Text fill `#1a1a1a`; connectors/edge labels `#555555`. Use a dashed stroke
(`stroke-dasharray="5 4"`) for secondary/feedback/uncertainty edges.

### 6. No title or source text on the figure
Same rule as data figures: **no on-figure title, super-title, or provenance note** — those
go in the manuscript caption (`research-writing`). The SVG contains only nodes, edges, and
their labels.

### 7. Consistent geometry
Align boxes to a grid; use a uniform box height and corner radius (`rx`), uniform stroke
widths, and **one** reusable arrowhead `<marker>` (define once in `<defs>`, reference with
`marker-end`). Keep generous, even whitespace. One concept per diagram.

### 8. Valid, self-contained XML
UTF-8; self-contained (no external images or fonts). **XML comments must not contain `--`**
(double-hyphen) — it is illegal and breaks every renderer; reword the comment instead. The
file must parse with `rsvg-convert` without error.

### 9. Sizing and fonts
Design at a sensible `viewBox` and render to the target column width; ensure body text is
≥ ~9 pt at final size (≈14 px in a ~900-unit-wide viewBox rendered to a single column).
Always check the rendered output at the real width, not just zoomed in.

---

## Reusable building blocks

**Arrowhead marker (define once, reuse everywhere):**
```xml
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8.5" refY="5"
          markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="#555555"/>
  </marker>
</defs>
```

**A node (box + centered label):** a `<rect rx="9">` with a pale fill + strong stroke, and
a single `<text text-anchor="middle">` whose baseline sits ~5 px below the box center for a
14 px font. Multi-line labels use `<tspan>` as in rule 2.

**Edges:** `<line>` or `<path>` with `marker-end="url(#arrow)"`; elbow connectors with a
path like `M340,158 V285 H486` (down then across); dashed for secondary branches.

---

## Pre-delivery checklist

- [ ] Every label is a single `<text>` (no per-word splitting); multi-line labels use
      `<tspan>` inside one `<text>` (no per-line splitting).
- [ ] Text is real (not outlined to paths); one root `font-family`.
- [ ] No label is covered by any shape, arrow, or line (text layer painted last).
- [ ] Okabe-Ito pale-fill + strong-stroke; legible in grayscale; meaning not hue-only.
- [ ] No title / super-title / source note on the figure (those go in the caption).
- [ ] Boxes grid-aligned; uniform size, radius, stroke; one shared arrowhead marker.
- [ ] Valid XML (no `--` in comments); renders cleanly with `rsvg-convert`.
- [ ] Checked at final column width and in grayscale.
