# Writing Style — Aerospace Engineering (AIAA)

Conventions for novel-aircraft and advanced-propulsion papers in AIAA journals (AIAA Journal, Journal of Aircraft, Journal of Propulsion and Power, JGCD) and AIAA conference papers. These differ sharply from atmospheric-science norms — see contrasts in §6.

---

## 1. Abstract (third person, 100–200 words, no citations/figures/acronyms)
Compressed **problem → approach → quantitative result → significance**, but framed for engineers:
- **Open on the engineering problem/gap directly** — not broad societal context. *"The transonic performance of this boundary-layer-ingesting inlet topology has not been characterized at Mach 0.85."*
- **Approach:** 1–2 sentences of method (*"A RANS solver with a k–ω SST model was used…"* / *"A thermodynamic cycle model was developed and validated against…"*).
- **Result must be quantitative in engineering units** — "a 4.3 % reduction in induced drag," not "significant improvement." Reviewers watch for this.
- **Significance in design utility**, not policy/emissions (unless a sustainability paper). *"…providing a validated aerodynamic database for BWB trade studies at landing conditions."*

## 2. Nomenclature, symbols, equations
- **Nomenclature section** between abstract and intro when many symbols are used: two-column `symbol = definition, units`; alphabetical, capitals before lowercase, Roman → Greek → numerals → special; subscripts/superscripts in their own sub-headings.
- **If a nomenclature list is used, do NOT redefine symbols in text. Acronyms go in text only**, never in nomenclature.
- Still introduce each symbol verbally at first use in prose (*"…where c is chord and V∞ is freestream velocity"*).
- **Variables italic; vectors bold (no arrows/bars); functions and descriptive subscripts upright.** Equations numbered sequentially, no terminal period; break at ~40 symbols with the operator starting the next line.
- **Dual units (SI + English)** preferred — thrust in N and lbf, fuel flow in kg/s and lbm/s.
- Derivations are compressed: cite the source, state governing equations + BCs, jump to solution. Full line-by-line derivations are for Technical Notes, not full papers.

## 3. Reporting computational / experimental / cycle results (V&V — desk-reject if missing)
**CFD:** (1) code verification (analytical/MMS or cite solver's validation DB — never just "the code is validated"); (2) **grid-independence study, ≥3 meshes, report GCI** (% ; <1 % publishable, 1–5 % discuss); (3) iterative convergence (residual criterion *and* converged integrated quantities); (4) temporal convergence for unsteady; (5) **validation vs experiment/higher-fidelity with % error + uncertainty bands.** Use *verified* (code correctness) vs *validated* (physical agreement) precisely (AIAA G-077). Never "agrees well" without numbers.

**Experiment / wind tunnel:** facility (size, turbulence intensity, blockage), instrumentation + calibration, **bias and precision uncertainty estimated separately then combined (RSS), reported as ±X at 95 % confidence**, repeatability runs, blockage correction, Reynolds-number statement.

**Cycle / propulsion:** state thermodynamic assumptions (ideal gas, polytropic efficiency defn), validate component maps vs published/manufacturer data (acknowledge export-controlled redactions), report cycle closure (energy/mass balance convergence). Carpet plots and T–s/h–s diagrams expected.

## 4. Figure types reviewers expect (build with `research-figures`/`research-schematics`)
- **Aircraft:** three-view orthographic with dimensions/reference lengths; isometric CAD with labeled components; **computational-domain schematic** (BCs, extent in chord lengths, grid topology).
- **Aerodynamics:** L/D and C_L, C_D, C_m vs α **polars** (the money figure); drag breakdown (pressure/friction/induced); **C_p distributions** (chordwise cuts + surface contours); Mach/total-pressure contours (inlet/nozzle); wake surveys.
- **Propulsion:** **compressor/fan map** (PR vs corrected mass flow, speed lines, surge line) with efficiency overlay; **T–s / h–s cycle diagrams**; TSFC carpet plots; specific power vs specific energy (electric/hybrid); combustor pattern factor.
- **MDO:** **Pareto fronts**; design-space scatter colored by constraint; surrogate validation (predicted vs actual); convergence histories.
- **Structures/aeroelasticity:** mode shapes; V–f flutter diagram; weight breakdown.
- Always error bars on experimental points; mesh-detail inset on CFD contours; perceptually-uniform colormaps (not jet); labeled colorbar with units.

## 5. Voice, tense, novelty
- **Tense:** past for what was done (*"a RANS simulation was performed," "grid independence was demonstrated"*); present for what the paper shows / facts (*"Fig. 3 shows," "the throat Mach number is 0.85"*); past for literature; present for conclusions.
- **Voice:** third-person passive is the default; first-person active acceptable in the body's contribution statement (but **abstracts must be third person**).
- **Novelty the engineering way:** state precisely what hasn't been done, with citations proving the gap (*"While [4–6] examined subsonic configurations, transonic behaviour of this topology at M 0.85 has not been characterized"*). Claim contribution in measurable outcomes. **Avoid "novel"/"revolutionary" without cited justification — "novel" is the most over-scrutinized word in AIAA review.** Enumerate contributions at the end of the Introduction. Conclusions restate what was actually shown, quantitatively, parallel to the abstract — no new concepts or citations.

## 6. Key contrasts vs atmospheric-science papers
| | Atmospheric/climate | AIAA engineering |
|---|---|---|
| Intro opening | societal significance, forcing budget | the engineering problem, directly |
| "Significance" | emissions/policy/climate | design utility, engineering units |
| Uncertainty | ensemble spread, 5–95 % bracket ranges, IPCC confidence | GCI, total uncertainty at a coverage factor, comparison error |
| References | author-year (mostly) | numbered brackets, all authors, full titles |
| Symbols | inline | Nomenclature section, dual units |
| Section heads | generic / thematic | descriptive & specific ("III. RANS Methodology") |
| Phenomenon | the end in itself | a means to an engineering end |

## 7. Common AIAA mistakes to flag (use in `research-critique`)
Nomenclature/text symbol redundancy · no grid-convergence/GCI · experimental uncertainty without coverage factor · "et al." in the reference list · abbreviated journal names · figure fonts <8 pt at 3.25 in · PowerPoint/GIF figures · acronyms in nomenclature · first-person or cited abstract · conclusions introducing new material · "novel" without cited gap · jet colormap.

## 8. Templates & key sources
- Journal LaTeX (Overleaf): overleaf.com/latex/templates/.../mqqbqqvyhtwm · Word: arc.aiaa.org/r/journalwordtemplate · Conference LaTeX: .../rsssbwthkptn
- Figures/Tables: https://aiaa.org/publications/journals/Journal-Author/Guidelines-for-Journal-Figures-and-Tables/
- Nomenclature: https://aiaa.org/publications/journals/journal-author/nomenclature-guidelines/
- References: https://aiaa.org/publications/journals/reference-style-and-format/
- V&V editorial policy: https://aiaa.org/publications/publish-with-aiaa/publication-policies/editorial-policy-statement-on-numerical-and-experimental-accuracy/
