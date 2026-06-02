# Section Playbook — templates & worked phrasings

Concrete scaffolds for each section, in both families. Fill the brackets; then convert to prose (Stage 2). These are starting points, not formulas to follow mechanically.

---

## ABSTRACT

### Family A (atmospheric/environmental) — flowing paragraph
> [Aviation / commercial aviation] contributes to anthropogenic climate forcing through [CO₂ and a set of non-CO₂ effects, of which contrail cirrus is the largest]. [The magnitude of {specific component} remains poorly constrained because {specific reason}.] Here we use [model/dataset, e.g. a global contrail simulation driven by ERA5 and {flight inventory}] to [quantify {quantity} for {year/scenario}]. We estimate [headline number] of [X.X [lo, hi] mW m⁻² (5–95 %)], [comparator: e.g. comparable to / N times the ERF from aviation CO₂]. [Second key result + its mechanism.] [The dominant uncertainty arises from {source}.] These results [imply / enable / suggest] [implication].

Checklist: declarative open ✓ · agents named ✓ · specific gap ✓ · "Here we…" ✓ · number-then-comparator ✓ · bracket interval ✓ · implications close ✓ · no "In recent years" ✗.

### Family B (AIAA) — third person, 100–200 words, no citations/acronyms
> [The {performance quantity} of {configuration/component} is not well characterized at {condition}.] [A {method: RANS with k–ω SST / thermodynamic cycle model / wind-tunnel campaign} was used to {do what}.] [Grid independence was established and results were validated against {data}.] [Results show a {quantitative outcome in engineering units, e.g. 4.3 % reduction in induced drag / 1.8 % SFC improvement}.] [This provides {design utility}.]

Checklist: engineering problem first ✓ · method ✓ · **quantitative** result in engineering units ✓ · design significance ✓ · third person ✓ · no citations/figure refs/acronyms ✓.

---

## INTRODUCTION

### Family A
1. **Significance + pivot.** "Aviation provides substantial social and economic benefits, but also emits CO₂ and non-CO₂ pollutants that warm the climate." Anchor the budget: "Aviation was responsible for ~3.5 % of anthropogenic effective radiative forcing in 2018 (Lee et al., 2021)."
2. **Partition.** State CO₂ vs non-CO₂ and the contrail-cirrus dominance, with numbers + citation.
3. **Mechanism** (1–2 paras, dense citations): Schmidt–Appleman, ISSR, ice nucleation, optical depth, SW cooling / LW warming.
4. **Prior estimates, model-by-model:** "Burkhardt and Kärcher (2011) estimated a 2002 contrail-cirrus RF of 37.5 mW m⁻²; Bock and Burkhardt (2016) … (56 mW m⁻²); …"
5. **Gap as specific limitation:** "However, these estimates assume a constant ice-crystal number that does not resolve differences in nvPM EIn between engine types, which could bias … because (i) …; (ii) …; (iii) …."
6. **Objective list:** "In this study, we use [X] to: (i) quantify …; (ii) identify …; (iii) evaluate …; and (iv) compare …." (Maps to your Results headings.)

### Family B (AIAA)
1. **Engineering problem, directly:** what system, what condition, why it matters for design. No societal preamble.
2. **Targeted literature gap:** "While [4–6] examined {subsonic / cruise / clean configuration}, the {transonic / off-design / installed} behaviour of {topology} at {condition} has not been characterized."
3. **Approach in one line** + what makes it adequate (fidelity, validation basis).
4. **Enumerated contributions:** "The contributions of this paper are: (1) …; (2) …; (3) …." Claim measurable outcomes; avoid bare "novel."

---

## METHODS / MODEL / EXPERIMENT

### Family A
- Past tense, reproducible. Cover: meteorology source (e.g. "ERA5 HRES hourly fields were used to identify ice-supersaturated regions"), flight/emissions inventory, contrail/forcing model and version, key parameterizations (ice-crystal number, optical depth), radiative-transfer scheme, the forcing metric and ERF/RF treatment, and the **uncertainty/sensitivity design** (which inputs perturbed, ranges, ensemble).
- End Methods (or open Results) with how uncertainty was propagated and reported.

### Family B (AIAA) — descriptively-titled sections, V&V mandatory
- **Governing equations / model:** state assumptions (turbulence model, ideal-gas/calorically-perfect, polytropic-efficiency definition), BCs, solver.
- **Verification:** analytical/MMS check or cite solver validation database. "Spatial discretization is formally second-order accurate."
- **Grid independence:** "Three systematically refined meshes (N = …, …, …) were used; the grid convergence index (GCI) for {C_L, C_D / total-pressure recovery} was {X} %." Report a table.
- **Iterative/temporal convergence:** residual criterion (e.g. 10⁻⁶ normalized) *and* converged integrated quantities; time-step sensitivity if unsteady.
- **Validation:** compare to experiment/higher-fidelity with % comparison error and uncertainty bands. Keep *verified* vs *validated* distinct.
- **Experiment:** facility (size, turbulence intensity, blockage ratio), instrumentation + calibration, **bias and precision uncertainty combined (RSS), reported as ±X at 95 % confidence**, repeatability, corrections, Re statement.

---

## RESULTS

Both families: **result first, figure reference parenthetical.**
- A: "The contrail net ERF is largest over Europe and the North Atlantic (Fig. 3a). This pattern reflects dense traffic intersecting persistent ice-supersaturated regions." Then numbers with intervals.
- B: "The configuration achieves an L/D of 18.4 at the cruise design point (Fig. 5), a 6 % improvement over the baseline." Then mechanism/cause.
Pair every number with a mechanism or cause in the adjacent sentence. Active voice for findings ("We estimate…", "The results indicate…").

---

## DISCUSSION / CONCLUSIONS

### Family A
- Reconcile with prior estimates and **attribute differences:** "Our estimate is 18 % lower than Lee et al. (2021), which we attribute to {humidity correction / engine-resolved nvPM}."
- **Rank uncertainty sources;** name the dominant one.
- Implications: ACP **requires** an explicit atmospheric/climate-implications statement in the conclusions; Nature-family puts broader/policy framing here (not in the abstract).

### Family B
- Conclusions = quantitative restatement of what was shown, parallel to the abstract. **No new concepts, no new citations.** Note design implications and bounded future work.

---

## TITLE
- A: specific + quantitative where possible; name the system and the climate quantity. "Global contrail-cirrus radiative forcing from 2019–2021 air traffic."
- B: name the configuration/component, the condition, and the contribution. "Transonic performance of a boundary-layer-ingesting inlet: a validated CFD characterization."

## COVER LETTER / REQUIRED EXTRAS (check `journal_guidelines.md`)
- RSC: cover letter establishing energy-community impact in para 1; **TOC graphic**.
- ERL: **Justification Statement** (separate, goes to reviewers).
- AGU: **3 Key Points** (≤140 chars), **Plain Language Summary** (≤200 words, no jargon), **Open Research** (data + code DOIs; never "upon request"), CRediT.
- ACP/EGU: data + code availability sections; remember the public preprint.
- Nature family: cover letter on broad significance; Data/Code Availability statements.

## RESPONSE TO REVIEWERS (template)
For each comment: quote it verbatim → "We thank the reviewer…" (brief) → the change made → exact location ("p. 7, ll. 210–218; new Fig. 4b"). Group by reviewer, number to match. Where you disagree, do so with evidence, courteously. Provide a marked-up manuscript.
