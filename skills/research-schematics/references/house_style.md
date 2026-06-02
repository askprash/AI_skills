# House Voice — Research Writing (climate / atmospheric + aerospace-engineering)

**This is the authoritative voice layer. When drafting or revising, it takes precedence over the field-exemplar guide (`atmospheric_climate_style.md`), which remains as general grounding.** It encodes a specific, opinionated way of writing top-journal manuscripts in two related cultures — atmospheric/environmental science and aerospace engineering. Emulate these habits; don't just follow generic norms.

This voice is distilled from the conventions of high-impact papers in these fields. Treat it as the default house style for manuscripts in these domains, and override it only when a journal's hard requirement conflicts (then the journal wins).

---

## House voice in brief
1. **Result-first, first-person, active.** "We find / we estimate / we show / we demonstrate / we quantify / we propose." Passive only for standard methods and prior literature.
2. **Quantified confidence, never overclaimed.** The headline number appears early and always carries its 95% CI in the same sentence; the *number* is never hedged — mechanisms and policy implications are.
3. **The gap is an integration gap.** Novelty is claimed as "no previous work has [done X and Y] together," then "Here we …" — not bare "first/novel."
4. **Policy stakes named, not asserted.** Papers close on a specific, grounded implication (ICAO/CORSIA/CARB/LCFS), framed as guidance ("may help to guide"), not advocacy.
5. **Scale and lineage made explicit.** State resolution/scope vs prior work ("50 km, an order of magnitude finer"), and compare quantitatively to prior estimates, decomposing any difference into labeled multiplicative factors.

---

## Section-level habits

**Title.** Short (5–10 words), declarative **noun phrase, no verb, no colon**; names the phenomenon/object/achievement, not the method or the finding. "Global" recurs. (e.g. *Flight of an aeroplane with solid-state propulsion*; *Near-zero environmental impact aircraft*.)

**Abstract (≈200–300 words, unstructured prose).** Five beats: (1) macro context with a prior-estimate anchor; (2) the gap/limitation ("does not account for", "has not been integrated"); (3) brief method, naming the tool and the *key differentiator* ("we use … at 50 km global resolution"); (4) **headline result + 95% CI in one sentence** ("21,200 (95% CI 19,400–22,900)"); (5) close on a **named policy/implication or recommendation** (forward-looking, not a restated finding). Engineering-mode abstracts may enumerate the method inline ("we (1) … (2) … (3) …").

**Introduction.** Open with a macro statistic that sets scale (e.g. aviation ≈ X% of …), pivot quickly to health/climate/policy stakes with regulatory acronyms introduced early. State the gap as a specific methodological/coverage deficiency, building to "**no previous work has integrated these … into a single study**." State objectives in prose ("In this work, we present/quantify/identify and assess …"); enumerate only in engineering mode. Cite 2–4 refs for a consensus point, then assert the gap (often without a citation).

**Methods & Results.** Separate sections (Nature: online Methods; RSC/ACP: full numbered sections 2.1, 2.2…). Each Methods subsection opens by saying *what it accomplishes* before naming tools. **Results are narrated result-first with the figure reference parenthetical at the end** — "We find that 41–53% of … occurs outside that state (Fig. 1a,b)." Never "Figure 1 shows…". Pair each number with a one-clause mechanism or interpretation ("This implies / highlights / reflects …").

**Conclusions / implications.** Synthesize, then give the specific regulatory/technological implication as guidance. Reconcile with prior estimates explicitly and attribute differences.

---

## Uncertainty, numbers, units (the signature rigor)
- **One unit system (SI), stated throughout**; compound units written out (`50 N kW⁻¹`, `µg m⁻³`, `kg-CO₂eq/barrel`). For climate forcing follow the field convention (mW m⁻²) from `atmospheric_climate_style.md`.
- **95% CI in parentheses, with the *source* of uncertainty named** ("95% CI due to the concentration–response function: …"). **Taxonomize and rank uncertainty types**; identify the single largest contributor.
- **Never hedge the central estimate**; hedge mechanisms ("likely driven by…") and policy ("may help to guide…").
- **Significant figures:** 2–3 for computed/measured quantities; round numbers for contextual/policy figures. **Tilde (~)** for approximations is acceptable in *engineering mode*, generally avoided in Nature-mode prose.
- **Diction:** "premature mortalities," never "deaths"; "we find/estimate," not "it was found"; reserve "**we note that**" for caveats; use "**However**" to pivot to a complicating factor right after a positive result; "Although [objection], [conclusion holds]" to pre-empt referees.
- Report results **normalized for comparison** where possible ("per Tg fuel burned") and **compare to prior work with explicit multiplicative factors** ("a factor of 7.8 higher, of which 1.84× is updated epidemiology…").

## Claiming contribution
Establish novelty structurally via the integration-gap sentence + "Here we …" pivot. Avoid bare "first/novel." Calibrate the closing claim to the evidence: "**proof of concept**" for a demonstration (Nature-mode), "**a framework for holistic analysis**" for an integrative/systems study. Cite prior work plainly and quantitatively, and reuse established methods by reference ("following the method of …") rather than restating.

## Figure & caption conventions
Order figures by the paper's logic: **configuration/geometry → performance → comparison/demonstration.** Recurring types: global maps (concentration/forcing/CI), bar charts with uncertainty, violin/distribution plots, source–receptor matrices, attribution/waterfall decompositions, supply-chain/system diagrams; Nature-mode demonstration photos. **Captions are self-contained and interpretive** — name every panel (a, b, c), state what the reader should notice, define error bars, and end with the key quantitative takeaway. Build all of these with `research-figures`/`research-schematics` (vector, colorblind-safe). 3–4 lean figures in Nature mode; more, denser multi-panel figures in engineering mode.

## Recognizable fingerprints (use deliberately)
"No [X] has yet [verb]" gap sentence · "Here we [demonstrate/quantify/show/find/propose]" pivot · "We find that …" result opener · "This [implies/highlights/reflects] …" interpretation · transboundary / counterintuitive geographic finding as the intellectual climax · multiplicative decomposition of differences from prior estimates · quantitative sector analogies ("≈100 million gasoline cars") · policy-acronym anchoring · precise resolution-vs-prior-work statements · aggressive use of SI/ESI for sensitivity cases to keep the main text lean.

---

## Two modes — switch by venue

| | **Nature-flagship mode** (Nature, Nat. Commun., Nature Climate Change) | **Engineering-systems mode** (E&ES, Sust. Energy & Fuels, ACP, AIAA) |
|---|---|---|
| Structure | compressed: summary paragraph, bold-opening intro, ~3–4 pp, online Methods | expanded: numbered sections + subsections, full Methods section |
| Abstract | one flowing paragraph, clean gap sentence | may enumerate methods inline "(1)…(2)…" |
| Numbers | whole numbers + 95% CI; avoid tilde | tilde (~) for approximations OK; explicit Monte Carlo |
| Figures | 3–4 lean; demonstration photos matter | more, denser multi-panel; renderings + parameter insets |
| Citations | sparse, clustered superscripts | denser; every literature number cited |
| Hedging | minimal ("opening up possibilities") | more acknowledged limitations and scope notes |
| Novelty | gap→achievement; "proof of concept" | "no assessment to date"; "framework" |

Core voice is identical across both — first-person active, result-first, explicit CI, "Here we" pivot, short declarative gap sentence. Add granularity and explicit limitations in engineering mode; enforce compression and load-bearing sentences in Nature mode.

**Third mode — geoscience letter (GRL / JGR / ACP).** Compressed like Nature mode but with discipline furniture: no numbered sections, a combined "Conclusions and Discussion," AGU **Key Points + Plain Language Summary + CRediT** statements, and supporting information on Zenodo (see `journal_guidelines.md`). The gap sentence carries an epistemic hedge here — "to our knowledge, no study to date has…" — whereas Nature-family papers drop the hedge.

---

## Domain & venue refinements

**AIAA voice — override the field default.** The general AIAA norm is third-person passive (`aiaa_engineering_style.md`), but this voice writes **first-person active in the body** of AIAA papers ("we identify the constraints," "we design and optimize," "we find") — only the **abstract stays third person** ("This paper finds that…", because AIAA mandates it). Two more AIAA habits: the **macro-stakes opening is kept even in AIAA abstracts** (a societal/regulatory context sentence before the engineering problem — not the field's "problem-first"), and introductions **close with a paper-outline paragraph** ("This paper is outlined as follows: Section II…"). Nomenclature section, numbered refs, dual units, and validation-with-%-error are all followed faithfully.

**Observational / remote-sensing papers.** Structure the paper as a **use-case audit**: enumerate the downstream purposes (model validation, real-time avoidance, MRV…) and score the instrument against each — every reported number is anchored to which use cases it affects. Frame error as **counteracting effects** (an omission source and an over-estimation source named together) so the net bias is presented as scene-dependent, not a simple direction. **Bound the reference instrument too** ("an imperfect imager… not observational ground truth") — observational uncertainty is sensor-resolution-imposed incompleteness, distinct from the parametric/CI uncertainty of modeling papers. Re-cite each sensor's ground resolution every time it appears ("VIIRS; 750 m", "ABI; 2–3 km"), the way modeling papers cite grid resolution.

**Reduced-order-model / scaling papers.** Motivate the ROM with the three-part formula: (1) name the high-fidelity tool and why it's unsuitable for the task ("computationally expensive… not suited for parametric analysis"); (2) state the ROM captures "first-order governing effects… trends," not high accuracy; (3) anchor it by calibrating coefficients to named validated tools (NPSS, pyNA, NASA STCA). **Validate model-on-model** and state the **layered chain explicitly** (experiment → validated high-fidelity tool → ROM vs that tool). Run **Buckingham-Pi / dimensional analysis *before* regression** to defend the scaling-group choice, and **present results in both forms** — a first-principles dimensionless relationship *and* the fitted polynomial with coefficients stated in the main text (not relegated to SI).

**Propulsion figures-of-merit.** State performance as a **joint pair — "X at a Y of Z"** ("thrust density of 100 N m⁻² at a thrust-to-power ratio of 5.6 N kW⁻¹"); one metric alone is incomplete. Name a fundamental tradeoff analytically, then pivot with "**this motivates the use of** [the fix]" (e.g. multistaging). Benchmark against the prior demonstration of record and report **order-of-magnitude improvements**.

**Aeroacoustics / noise.** Certification metric is **EPNL in EPNdB** (not dB/dB(A)), reported as the cumulative sum of lateral + flyover + approach with components distinguished; lay the microphone-location definitions (ICAO Annex 16) before any number; **justify metric choice** when rejecting community metrics (SEL, DNL); invoke Lighthill's eighth-power law by citation, then isolate the dominant velocity term.

**Design-tradeoff papers.** Lead the reader to the trade by showing the single-objective optimum **falling in an infeasible region** for another constraint ("…located in the infeasible region because blade temperatures exceed the limits"). State the trade quantitatively with all competing metrics in one sentence ("≈4.5% lower SFC, ≈2.5× higher EI(NOx), +1.2 EPNdB"). Add a **design-space feasibility plot** (shaded infeasible regions, metric contours) to the engineering figure repertoire alongside Pareto fronts and carpet plots.

**Pathway / scenario papers** (e.g. Nature Climate Change "Analysis" format). Use an **accounting identity as the narrative spine** (e.g. CO₂eq = RTK × Energy/RTK × CO₂eq/Energy − offsets), then analyze each factor in turn. Report findings as **ranges that span scenarios** (Low/Mid/High demand × fuel pathways), keeping scenario-range distinct from within-scenario uncertainty. Compress the concession into the headline ("89–94% reduction **despite** a 2–3× demand growth"), then **state the residual gap as a forward finding** ("our pathways reduce CO₂-equivalent by only 46–69%; more action is required for non-CO₂"). Architecture: single pathways → identify failure modes → combined ("bridging") pathways as the fix. Note: pathway papers anchor the close to **treaty/sector goals (Paris)** rather than regulatory acronyms (ICAO/CORSIA) — the acronym-anchoring fingerprint belongs to the air-quality/health papers.

**Added fingerprints:** "this motivates the use of [approach]" (tradeoff → fix pivot) · use-case audit before any number (observational) · "This paper finds that…" (AIAA third-person abstract seam, body reverts to "we") · "despite [growth], [target achievable]" (Nature-mode concession compressed into the headline) · "Notwithstanding these uncertainties, it is understood that…" (move from large magnitude-uncertainty to an actionable, sign-certain finding).

> Note: this guide encodes *how* to write in this voice. Pair it with `journal_guidelines.md` (the venue's hard requirements) and the relevant field/AIAA style file. When the house style and a journal requirement conflict, the journal requirement wins.
