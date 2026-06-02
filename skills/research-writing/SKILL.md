---
name: research-writing
description: Draft and revise research manuscripts in any field, in flowing prose (never bullet points in the final manuscript). Use for any section of a paper — abstracts, introductions, methods, results, discussion — plus cover letters, reviewer responses, and adapting a draft to a specific journal. Built on a two-stage outline→prose method and dependency-order drafting (figures/tables → Methods → Results → Discussion → Introduction → Abstract → Title). Carries two fully worked author cultures — atmospheric/environmental/climate science and AIAA aerospace engineering — with their distinct IMRAD structure, uncertainty vs verification-and-validation (V&V) rigor, citation styles (APA/AMA/Vancouver/Chicago/IEEE, author-year vs numbered), units, and toolchains (LaTeX, Markdown/Pandoc, Word). General references cover IMRAD, the Nature seven-move abstract, figures/tables, reporting guidelines (CONSORT/STROBE/PRISMA/ARRIVE), and clarity/conciseness/accuracy/objectivity, so it adapts to other fields and journals.
allowed-tools: Read Write Edit Bash
---

# Research Manuscript Writing

## What this skill is for

Writing and revising research manuscripts to a publishable standard, in flowing prose, for any field and any target journal. It pairs a general writing engine (IMRAD, abstracts, citations, figures/tables, reporting guidelines, writing principles) with two **fully worked author cultures** that double as the core worked examples:

- **Family A — atmospheric / environmental / climate science:** Energy & Environmental Science, Environmental Research Letters, ACP/AMT (EGU), JGR-Atmospheres / GRL / Earth's Future / AGU Advances, Nature / Science / Nature Climate Change / Nature Geoscience / Nature Communications.
- **Family B — aerospace engineering (AIAA):** AIAA Journal, Journal of Aircraft (incl. Design Forum), Journal of Propulsion and Power, JGCD, and AIAA conference papers.

These two families differ sharply — in structure, in how rigor is expressed (**uncertainty quantification** for A, **verification & validation** for B), in citation style, and in units — and learning to write either well is most of the value here. The general layer makes the same machinery transfer to other disciplines (biomedical, clinical, ML, social science), where you swap in the matching field conventions and reporting guideline.

**First question to resolve:** *which journal, and therefore which family / culture?* It changes structure, citation style, the language of rigor, and units. If the venue is unknown, ask, or draft to Family A defaults and flag the decision.

**Before drafting, load the matching references:**
- **House voice (authoritative) → `references/house_style.md`** — the default writing voice for these domains; **read first**. It takes precedence over the general field guides; when it conflicts with a journal's hard requirement, the journal wins.
- General writing engine → `references/imrad_structure.md`, `references/abstract_writing.md`, `references/citation_styles.md`, `references/figures_tables.md`, `references/writing_principles.md`, `references/reporting_guidelines.md`.
- Per-journal hard specs (length, abstract, figures, refs, data policy) → `references/journal_guidelines.md`.
- Field style A → `references/atmospheric_climate_style.md`; Field style B → `references/aiaa_engineering_style.md`.
- Section-by-section templates (both families) → `references/section_playbook.md`.
- Output format & reference mapping → `references/toolchain.md`.

## Core principle

**Write in complete, flowing prose. Never leave bullet points in a final manuscript.** Bullets are for planning only. Three narrow exceptions: an enumerated objective list at the end of an Introduction (common and welcome), AIAA contribution lists, and inclusion criteria / numbered method steps where a journal expects them.

The voice to default to (see `house_style.md`): **result-first, first-person, active** ("we find / we estimate / we show / we demonstrate"); the headline number stated early with its uncertainty in the *same* sentence and the *source* of that uncertainty named; novelty framed as an **integration gap** ("no previous work has … together") with a "Here we …" pivot; close on a specific, grounded implication, framed as guidance, not advocacy. Switch between **Nature-flagship mode** (compressed, lean, sparse citations) and **engineering-systems mode** (expanded, numbered sections, more acknowledged limitations) by venue.

## The two-stage method (use for every section)

**Stage 1 — outline with evidence.** Gather the relevant literature and data (search tools, your reference manager, datasets, prior drafts), then write a bullet scaffold marking the claims to make, the specific numbers/citations behind each, and the logical order. This is scaffolding, not the manuscript.

**Stage 2 — convert to prose.** Turn each bullet into full sentences with transitions; integrate citations inside sentences (not as trailing lists); add the context bullets omit; vary sentence structure; read aloud for flow. Apply the three pillars throughout — **clarity, conciseness, accuracy, objectivity** (`references/writing_principles.md`).

**Draft sections in dependency order, not paper order:** **figures/tables first** (they are the spine of the argument), then **Methods**, **Results**, **Discussion/Conclusions**, **Introduction**, **Abstract**, **Title** last.

## Structure: IMRAD and its variants

IMRAD (Introduction–Methods–Results–and–Discussion) is the backbone; full per-section guidance, tense tables, and study-type variants (clinical trials, systematic reviews, case reports, observational studies, ML-conference Intro–Method–Experiments–Conclusion) are in `references/imrad_structure.md`. Section proportions and length targets vary by venue; check `journal_guidelines.md` for the target.

### Narrative arc (OCAR) — the principle behind IMRAD

IMRAD is the *container*; **story structure** is what makes it hold a reader. A draft that satisfies IMRAD but has no arc is a data dump. Underneath every section sits the **OCAR** spine — **Opening** (the broad problem and characters), **Challenge** (the specific question), **Action** (Methods + Results + most of the Discussion), **Resolution** (how understanding changed). Full treatment in **`references/narrative_craft.md`**; the load-bearing moves:

- **Choose the assembly by audience patience:** specialist journals → straight **OCAR**; *Nature/Science* → **LDR** (a strong lead up front); proposals → **ABDCE** (hook by page one).
- **The paper is an hourglass:** open wide → narrow to Challenge/Methods/Results → widen back out in the Resolution. **Match opening width to resolution width** — opening wider than the resolution over-promises (the worst error); narrower under-sells.
- **The Introduction frames ignorance, not knowledge** (a gap, not a literature review). Diagnostic: prefer "**X occurs (Smith 2003)**" over "**Smith (2003) found X**"; ban "little is known about X"; never sell a method before you sell the problem.
- **The Challenge is a question, not a list of objectives** — "to learn X, we did Y," with "to learn X" load-bearing.
- **The Resolution synopsizes → synthesizes (answers the Challenge) → contextualizes (closes back to the Opening).** Never end on "more research is needed" or a brand-new idea.
- **OCAR is fractal** — every section and paragraph is its own arc, with the point in a power position (start or end).

### Section guidance (summary — full templates in `references/section_playbook.md`)

**Abstract.** Flowing paragraph (unless the journal mandates a structured one). General method = the **Nature seven-move summary paragraph** (basic introduction → detailed background → specific problem → "Here we show" main result → results in context → general context → optional broader perspective), an hourglass of ≈190–250 words; full sentence-by-sentence guide, worked example, and venue word limits in `references/abstract_writing.md`. The house-style **5-beat abstract** (`house_style.md`) is the compressed, domain-tuned form of the same arc: macro context with a prior-estimate anchor → the gap → brief method naming the key differentiator → **headline result + interval in one sentence** → close on a named implication. Per family:
- *Family A:* declarative opening (the phenomenon stated as fact, no "In recent years…"); name forcing agents; specific gap; "**Here we use…**"; headline number-then-comparator; bracket interval for the key result; close on implications.
- *Family B (AIAA):* third person, 100–200 words, no citations/figures/acronyms; engineering problem → approach → **quantitative** result in engineering units → design significance.

**Introduction.**
- *A:* significance → "benefits *but also* emits" pivot → quantify the share both absolutely and as a fraction → mechanism paragraphs with dense citations → prior estimates reviewed model-by-model → gap as a specific (i)/(ii)/(iii) limitation → explicit objective list.
- *B:* go straight to the engineering problem; cite the gap precisely; enumerate contributions at the end; avoid "novel" without a cited gap.

**Methods.** Past tense, reproducible — another expert should be able to repeat the work. *A:* data sources (e.g. ERA5), model, filtering, forcing definitions, and the uncertainty/sensitivity design. *B:* descriptively-titled sections; **V&V is mandatory** — code verification, grid-independence (≥3 meshes, GCI), iterative/temporal convergence, validation vs experiment with uncertainty; experiments need bias+precision uncertainty at a stated coverage factor. Use *verified* vs *validated* precisely.

**Results.** Result first, **figure reference parenthetical** (never "Figure 3 shows…"). Pair each number with its mechanism. Active voice for findings; objective, no interpretation (that is the Discussion's job).

**Discussion / Conclusions.** *A:* compare to prior estimates with attributions; rank uncertainty sources; ACP **requires** an atmospheric/climate-implications statement. *B:* Conclusions restate what was shown quantitatively, parallel to the abstract — **no new concepts or citations**.

## Uncertainty language is the craft (Family A)

This field lives on uncertainty; weak uncertainty language reads as naïveté. Apply rigorously:
- **ERF over RF;** state the ERF/RF ratio (≈0.42 for contrail cirrus) and that it adds uncertainty.
- **Bracket notation for asymmetric ranges:** `62.1 [34.8, 74.8] mW m⁻²`; state the percentile (5–95 % default). **No ± for asymmetric distributions.**
- **"Best estimate,"** never "mean"/"average." IPCC AR6 terms: *likely* (66–100 %), *very likely* (5–95 %).
- **Enumerate and rank uncertainty sources;** name the dominant one explicitly.
- **CO₂ / non-CO₂ partition** whenever net aviation forcing appears (denominator = net aviation ERF).

Full detail and phrasings: `references/atmospheric_climate_style.md` §D–E.

## V&V language is the craft (Family B)

A modeling/CFD paper without verification + validation + grid convergence (GCI) is desk-rejected. A wind-tunnel paper without combined bias/precision uncertainty at a coverage factor is incomplete. Distinguish *verification* (solving the equations right) from *validation* (right equations) using AIAA G-077 terms. Detail: `references/aiaa_engineering_style.md` §3.

## Units and numbers
- *A:* **mW m⁻²** for global forcing (spell out on first use); 3 sig figs for best estimates; Tg yr⁻¹, EIn (per kg fuel); avoid CO₂-equivalents for contrails (use a ratio or state the GWP horizon).
- *B:* **dual SI + English** (N and lbf, kg/s and lbm/s); SI primary.
- Numerals for any number with a unit; spell out integers < 10 without units.

## Citations

Match the citation style to the journal, and integrate citations *inside* sentences, not as trailing lists. The five major science styles — **APA** (author-date), **AMA** and **Vancouver** (numbered), **Chicago**, **IEEE** (numbered) — plus ACS/NLM, with in-text and reference-list formats, are detailed in `references/citation_styles.md`. For these two families specifically: **author-year** for ERL/EGU/AGU; **numbered** for RSC/Nature/Science/AIAA (see the per-journal map in `references/toolchain.md`). Verify every citation appears in text and list, and vice versa.

## Figures and tables — always vector, reproducible from code, never AI-generated

Decide figure vs table by `references/figures_tables.md` (precise values → table; trends/patterns/relationships → figure), and make every display item self-contained with an interpretive caption. Produce them as **reproducible vector output**:

- **Data figures** (forcing bars, maps, time series, polars, performance maps, cycle diagrams, Pareto fronts) → **`research-figures`**.
- **Concept / structural diagrams** (mechanism schematics, model pipelines, system boundaries, three-views, CFD domains) → **`research-schematics`**.
- **Low-level, fully customized plotting** → **`matplotlib`**.

**Never generate publication figures as AI raster/images.** They produce garbled text, wrong numbers, and are not reproducible. There is no minimum figure count; each figure must earn its place and read correctly in grayscale.

## Professional (non-journal) reports

For deliverables that are **not** journal submissions — research/technical reports, white papers, grant/progress reports, policy briefs, feasibility studies — use the bundled LaTeX report system instead of a journal class:
- `assets/scientific_report.sty` — professional report style package (Helvetica, colored box environments for key findings / methodology / results / limitations / recommendations, professional tables, statistical-notation commands). Compile with XeLaTeX or LuaLaTeX.
- `assets/scientific_report_template.tex` — a complete starter template.
- `assets/REPORT_FORMATTING_GUIDE.md` — quick reference.
- `references/professional_report_formatting.md` — when-to-use guidance, box/table/figure patterns, and a quality checklist.

These prioritize readability for general/stakeholder audiences. For anything destined for a journal, use that journal's own class file (`references/toolchain.md`), not this style.

## Output toolchain (LaTeX / Markdown / Word)

Pick the format from how the user works (full commands, per-journal CSL/class mapping, and a `.bib` workflow in `references/toolchain.md`):
- **LaTeX/Overleaf** (default for AIAA and math-heavy work): the journal's class file (AIAA template; `copernicus.cls` for EGU; AGU template; RSC/Nature templates), BibTeX/`.bib`, vector PDF figures from `research-figures` / `research-schematics`.
- **Markdown/Pandoc** (fast drafting, version control): `pandoc --citeproc` with the journal CSL (`american-geophysical-union.csl`, `copernicus-publications.csl`, `nature.csl`, `aiaa.csl`); convert to `.docx`/`.tex`/PDF.
- **Word**: real paragraph styles (Heading 1/2, never bold-as-heading); figures as EPS/TIFF/PNG at the journal's DPI; references driven from a CSL/`.bib`-backed manager.

## Reporting guidelines (light, general layer)

When the study type has an established reporting guideline, follow it and submit its checklist. **Use the guideline matching your study type** — CONSORT (randomized trials), STROBE (observational), PRISMA (systematic reviews/meta-analyses), ARRIVE (animal studies), and others catalogued by the EQUATOR Network. `references/reporting_guidelines.md` is a general-purpose pointer; it is clinical/biomedical-heavy by origin, so treat it as an optional layer and map it onto your field's equivalents (e.g. data/code availability and V&V reporting in Families A/B).

## Revision & response to reviewers

For **pre-submission self-critique** — running a referee-style report against your *own* draft and anticipating objections — use **`research-critique`**. For point-by-point reviewer responses: mirror the reviewer's structure, quote each comment verbatim, state the change made and its exact manuscript location, keep a courteous, evidence-led tone, and supply a marked-up manuscript (template in `references/section_playbook.md`).

## Common rejection triggers
Over-claiming a result beyond its uncertainty; missing/weak uncertainty quantification (A) or missing grid-convergence / uncertainty coverage factor (B); "available upon request" data statements (banned at AGU); wrong citation family; ignoring a mandatory section (ACP implications, AGU Key Points/Plain Language Summary/Open Research, ERL Justification Statement, RSC TOC graphic); units/sig-fig sloppiness; bullet points left in the manuscript; figures that fail in grayscale or contain non-reproducible AI artwork.

## References
- `references/house_style.md` — **the default house voice (authoritative); read first.**
- `references/imrad_structure.md` — IMRAD detail, tense tables, study-type and venue variants.
- `references/narrative_craft.md` — the story layer beneath IMRAD: OCAR, the four structures (OCAR/LDR/ABDCE/LD), the hourglass, the Funnel/knowledge-gap, the Challenge, the Action, and the Resolution. Adapted from Schimel, *Writing Science*.
- `references/abstract_writing.md` — the Nature seven-move abstract; sentence-by-sentence guide, word limits, checklist.
- `references/citation_styles.md` — APA / AMA / Vancouver / Chicago / IEEE (+ ACS/NLM) in-text and reference-list formats.
- `references/figures_tables.md` — figure-vs-table decisions and display-item best practices.
- `references/writing_principles.md` — clarity, conciseness, accuracy, objectivity; plus sentence craft (character/action, topic vs. stress positions, the given→new contract, fuzzy verbs, zombie nouns), condensing, and the SCFL editing-pass order.
- `references/reporting_guidelines.md` — CONSORT/STROBE/PRISMA/ARRIVE etc. (light, general-purpose layer).
- `references/section_playbook.md` — section-by-section templates and worked phrasings for both families, plus cover-letter and reviewer-response templates.
- `references/journal_guidelines.md` — per-journal hard specs (length, abstract, figures, refs, data policy).
- `references/atmospheric_climate_style.md` — Family A field style + external exemplar papers (general grounding).
- `references/aiaa_engineering_style.md` — Family B (AIAA) style rules.
- `references/toolchain.md` — LaTeX class files, Pandoc/CSL mapping, Word styles, `.bib` workflow, reference-style cheat sheet.
- `references/professional_report_formatting.md` — formatting guidance for non-journal professional reports.

## Assets
- `assets/scientific_report.sty` — LaTeX style package for professional (non-journal) reports.
- `assets/scientific_report_template.tex` — complete report starter template.
- `assets/REPORT_FORMATTING_GUIDE.md` — quick reference for the report style.
