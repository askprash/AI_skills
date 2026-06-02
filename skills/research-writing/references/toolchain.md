# Toolchain — LaTeX / Markdown-Pandoc / Word

Match the output format to how you work, and the **reference style to the journal**. Author-year: ERL (IOP), ACP/AMT (EGU), AGU. Numbered: RSC (E&ES), Nature, Science, AIAA.

---

## Reference-style cheat sheet

| Journal | In-text | List | BibTeX/CSL |
|---|---|---|---|
| E&ES (RSC) | numbered superscript | RSC | `rsc.csl` / RSC `.bst` |
| ERL (IOP) | author-year (Harvard) | alphabetical, titles incl. | `institute-of-physics-numeric`? → use **Harvard**: `harvard-cite-them-right.csl` or IOP CSL |
| ACP / AMT (EGU) | author-year | alphabetical, titles incl. | `copernicus-publications.csl` / `copernicus.bst` |
| AGU (GRL/JGR:A) | author-year | alphabetical | `american-geophysical-union.csl` / AGU `.bst` |
| Nature / NCC / NGeo / Nat. Commun. | numbered sequential | titles incl. (long-form) | `nature.csl` |
| Science | numbered sequential | — | `science.csl` |
| AIAA (all) | numbered brackets [n] | **all authors, full titles, DOI** | `aiaa.csl` / AIAA `.bst` |

Get CSL files from the Zotero Style Repository / citation-style-language GitHub. Verify the live author guide before submission.

---

## LaTeX / Overleaf (default for AIAA + math-heavy work)

Use the journal's official class — do not hand-roll formatting:
- **AIAA:** Overleaf "LaTeX Template for AIAA Technical Journals" (`mqqbqqvyhtwm`); conference template (`rsssbwthkptn`). Has the Nomenclature environment and AIAA `.bst`.
- **EGU (ACP/AMT):** `copernicus.cls` (Copernicus package) — includes the required sections scaffolding.
- **AGU:** AGU LaTeX template / `agujournal` class; SI via `agutexSI`.
- **RSC:** RSC article template.
- **Nature family:** Nature/Springer template (often Word-preferred; LaTeX accepted for some).

Workflow:
```bash
# Bibliography from a .bib file
# (BibTeX for numbered AIAA/Nature; biblatex+biber or natbib for author-year)
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
# or with biber:
pdflatex main && biber main && pdflatex main && pdflatex main
```
Figures: include vector **PDF** from `research-figures`/`research-schematics` via `\includegraphics`. Embed fonts. Keep one figure per file (EGU/AGU combine panels into a single file).

---

## Markdown + Pandoc (fast drafting, version control, format-agnostic)

Draft in Markdown with a YAML header; cite with `[@key]`; render to any target with `--citeproc` + the journal CSL.

```bash
# To Word for collaborators / Family A submission
pandoc paper.md --citeproc \
  --bibliography refs.bib --csl american-geophysical-union.csl \
  -o paper.docx

# To LaTeX/PDF
pandoc paper.md --citeproc --bibliography refs.bib --csl copernicus-publications.csl \
  -o paper.pdf --pdf-engine=xelatex

# To a journal .tex skeleton (then drop into the class file)
pandoc paper.md --bibliography refs.bib --natbib -o body.tex
```
Notes: use `crossref`/`pandoc-crossref` for `\ref`-style figure/equation numbering; keep figures as referenced files, not embedded images; equations in `$$ … $$`.

---

## Word (.docx)

- Use **real paragraph styles** (Heading 1/2/3, Caption) — never bold text faking a heading. This is what `research-writing`'s Word output should do; if generating a `.docx` programmatically, use the `docx` skill with proper styles.
- **References:** drive from a CSL style via Zotero/Mendeley or generate with Pandoc (above) so the style matches the journal; don't hand-type a reference list.
- **Figures:** insert as **EPS/TIFF/PNG** at the journal's DPI (600 for E&ES/AIAA line art; 300 elsewhere). Keep captions as text below the figure, not inside the image.
- **Equations:** Word's equation editor or MathType; keep symbols italic, units upright.

---

## Bibliography (.bib) workflow

Keep one master `refs.bib`. For these fields, prefer the **journal version** over the preprint/conference version of a paper (AIAA explicitly). Always include the DOI. For datasets/software, create `@misc`/`@dataset` entries with DOI (required by AGU Open Research, EGU, Nature). Example AIAA-style entry:
```bibtex
@article{teoh2024,
  author = {Teoh, Roger and Engberg, Zebediah and Schumann, Ulrich and others},
  title  = {Global aviation contrail climate effects from 2019 to 2021},
  journal= {Atmospheric Chemistry and Physics},
  volume = {24}, pages = {6071--6093}, year = {2024},
  doi    = {10.5194/acp-24-6071-2024}}
```
(For AIAA output, expand "others" to all authors — the AIAA list permits no "et al.")
