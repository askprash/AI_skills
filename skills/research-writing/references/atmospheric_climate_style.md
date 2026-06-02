# Writing Style — Aviation & Climate / Atmospheric Science

Rhetorical and quantitative conventions distilled from landmark papers (Lee et al. 2021; Burkhardt & Kärcher 2011; Kärcher 2018; Teoh et al. 2020/2024; Bock & Burkhardt 2019; Klöwer et al. 2021; Wuebbles/Singh et al. 2024). Use when drafting any atmospheric/environmental aviation manuscript.

---

## A. Abstract architecture
1. **Open declaratively.** First sentence asserts aviation's climate role as fact, no scene-setting. *"Aviation makes a significant contribution to anthropogenic climate forcing."* Never "In recent years…" or "Climate change is one of the greatest challenges…".
2. **Name the forcing agents** in order of magnitude (contrail cirrus, CO₂, NOₓ, aerosols, water vapour).
3. **State the specific gap** — frame around a poorly-constrained mechanism, not vague "little is known."
4. **Methods anchor:** one short active sentence, pivoting with "**Here we use [model] to…**".
5. **Headline result = number first, then comparator.** *"…about nine times larger than that from line-shaped contrails alone."* Don't bury it.
6. **Uncertainty:** include the key interval in bracket notation for the headline number (long-form venues); short Nature-family abstracts may defer ranges to the text.
7. **Close on implications / use**, not policy prescriptions (those go in Discussion for Nature-family).

## B. Introduction
- **Para 1:** societal significance → scientific complexity, often with a "benefits, *but also* emits…" pivot; anchor the overall budget to Lee et al. (2021).
- **Quantify aviation's share both ways:** absolute *and* fraction (e.g. ~3.5 % of anthropogenic RF in 2018; contrail cirrus > 50 % of aviation RF).
- **Mechanism paragraphs** carry dense inline citations (2–4 per sentence is normal here).
- **Review prior estimates model-by-model**, each as number + source + data year — this maps the gap.
- **State the gap as a specific methodological/data limitation** of prior work; enumerate with (i)/(ii)/(iii).
- **Close the intro with an explicit objective list:** *"In this study we … to: (i) quantify…; (ii) identify…; (iii) evaluate…"* — maps to later headings.

## C. Results & Discussion
- Structure is journal-dependent: combined R&D with subheads (Nature family) vs separate numbered sections (ACP, Atmos. Env.).
- **Result first, figure reference parenthetical.** *"Contrail net RF is largest over Europe (Fig. 3)."* Never start with "Figure 3 shows…".
- **Number + mechanism travel together:** state the value, then *"This pattern reflects…"*.

## D. Uncertainty communication — the critical discipline
- **Prefer ERF over RF;** state the ERF/RF ratio used (commonly 0.42 for contrail cirrus, Lee 2021) and that the ratio adds uncertainty.
- **Bracket notation, asymmetric ranges:** `62.1 [34.8, 74.8] mW m⁻²`. State the percentile ("5–95 % likelihood range"). **Don't use ± for asymmetric distributions** (they almost never are symmetric).
- **Enumerate uncertainty sources**, don't gesture. Contrail set: (i) humidity field/ERA5, (ii) initial ice-crystal number / nvPM EIn, (iii) optical depth, (iv) ERF/RF ratio.
- **Name the dominant source explicitly,** ranked: *"…most sensitive to humidity-field corrections, followed by particle-number assumptions, and least sensitive to radiative heating."*
- **IPCC AR6 terms:** "best estimate" (never "mean"/"expected"); "likely" (66–100 %), "very likely" (5–95 %); confidence labels reserved for synthesis in Discussion/Conclusions.

## E. Numbers, units, framing
- **mW m⁻²** for global-mean forcing (never W m⁻²; spell out "milliwatts per square metre" on first use). Negative-exponent units (m⁻²).
- **Sig figs:** 3 for best estimates, ≤3 for bounds; never 4+.
- **CO₂ / non-CO₂ partition is mandatory** whenever net aviation forcing is discussed; denominator = net aviation ERF. Canonical (Lee 2021): CO₂ 34.3 (34 %), contrail cirrus 57.4 (57 %), NOₓ 17.5 (17 %); note components don't sum linearly due to interactions.
- **Mass/EI units:** Tg yr⁻¹ (fuel/emissions), EIn (number per kg fuel), kg fuel⁻¹.
- **Avoid CO₂-equivalents for contrails** (time-horizon-dependent); use a ratio ("contrail cirrus ERF ≈ 1.7× aviation CO₂ ERF") or state GWP₁₀₀/GWP₂₀ explicitly with the lifetime caveat.

## F. Figure types (build these with `research-figures`)
- **Forcing-components bar chart** (canonical Fig.): one bar per agent, ordered by magnitude, red=warming/blue=cooling, asymmetric 5–95 % whiskers, zero line, separate net-total bar. (Lee 2021 Fig. 2 is the benchmark.)
- **Global map** of contrail RF / coverage (Robinson or PlateCarrée), diverging or sequential scale, year+model labeled, regional call-outs.
- **Time series** of forcing / activity with uncertainty bands; COVID-19 dip now standard.
- **Distribution / concentration** plots (violin, PDF, Lorenz-style cumulative — e.g. "2 % of flights → 80 % of energy forcing").
- **Mitigation scatter / Pareto** (energy forcing vs fuel penalty, point = flight).
- **Captions are self-contained:** what's plotted, what shading/whiskers mean, year/model/dataset, units.

## G. Voice, hedging, tense
- **Voice by function:** passive in Methods (*"ERA5 data were used"*); active for key findings (*"We estimate a 2019 contrail net RF of 62.1 mW m⁻²"*); active for mechanism.
- **Hedge to evidence strength:** strong → "We show/demonstrate"; model-derived → "We estimate / results suggest"; weak → "remains poorly constrained / highly uncertain"; sign-uncertain → "the sign of … is uncertain and depends on…".
- **Tense:** present for established facts & your now-established results; past for prior studies and your methods; conditional/future for projections.
- **Transitions:** gap = "However, [prior] did not account for…"; contribution = "Here we address this by…"; comparison = "Our estimate is X % lower than … which we attribute to…".

## H. Exemplar papers (style models)
1. **Lee et al. (2021)**, *Atmos. Environ.* 244:117834 — canonical assessment; bar chart, CO₂/non-CO₂ partition, bracket intervals, enumerated uncertainty.
2. **Burkhardt & Kärcher (2011)**, *Nat. Clim. Change* 1:54 — model short-form Nature paper; 5-sentence abstract; map + bar; "nine times larger."
3. **Kärcher (2018)**, *Nat. Commun.* 9:1824 — review structure by process; clean gap framing.
4. **Bock & Burkhardt (2019)**, *ACP* 19:8163 — exemplary ACP projection format; numbered model runs.
5. **Teoh et al. (2020)**, *ES&T* 54:2941 — mitigation paper; "2 % → 80 %" lever; tradeoff framing; bracket-notation % reductions.
6. **Teoh et al. (2024)**, *ACP* 24:6071 — state-of-the-art global simulation; reconciling prior estimates; COVID natural experiment.
7. **Klöwer et al. (2021)**, *ERL* 16:104027 — temperature-metric framing; "4 % of human-induced warming."
8. **Wuebbles/Singh et al. (2024)**, *ACP* 24:9219 — comprehensive review; conclusion = prioritized research agenda.

## 10 rules to internalize
1. First sentence = declarative assertion, no hedging. 2. Every number gets a bracket interval (5–95 % default). 3. "Best estimate," never "mean." 4. ERF over RF; state the ratio. 5. CO₂/non-CO₂ partition is mandatory. 6. "Here we…" pivots background→contribution. 7. Intro closes with (i)/(ii)/(iii) objectives. 8. Result = number + mechanism, figure ref parenthetical. 9. Active for findings, passive for methods. 10. mW m⁻²; EIn; Tg yr⁻¹.
