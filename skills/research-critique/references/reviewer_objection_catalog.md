# Reviewer Objection Catalog — and how to preempt each

The objections referees in these fields raise most, with the fix to apply before submission. Quote: the typical reviewer phrasing; Fix: what to change.

---

## Family A — atmospheric / climate

**1. "The headline number is stated without uncertainty / the uncertainty seems underestimated."**
Fix: report `X [lo, hi]` (5–95 %); show the sensitivity/ensemble design; enumerate and rank sources; name the dominant one.

**2. "The authors over-interpret the forcing/benefit."**
Fix: scale the claim to the interval and the scenario; hedge to evidence strength ("we estimate", not "we show", for model-derived results); state the limits of generalization.

**3. "RF and ERF are conflated / the RF→ERF ratio is hidden."**
Fix: report ERF, state the ratio (≈0.42 for contrail cirrus) and that it adds uncertainty; don't treat RF as the climate response.

**4. "± is inappropriate for this distribution."**
Fix: switch to bracket notation with the percentile; if you must summarize, say the distribution is asymmetric and give both bounds.

**5. "How sensitive is this to the humidity field / ice-crystal number / optical depth?"**
Fix: pre-empt with a sensitivity table ranking these; cite ERA5 limitations; justify the nvPM EIn assumption or make it engine-resolved.

**6. "The CO₂/non-CO₂ comparison is missing or framed oddly."**
Fix: give the partition with the net-aviation-ERF denominator; if using CO₂-equivalents, state the GWP horizon and the short-lifetime caveat (or use a ratio instead).

**7. "Data/code availability is inadequate."**
Fix: deposit with a DOI; never "available upon request" (AGU bans it); add the journal's required Data/Code/Open Research statements.

**8. "A required section is missing."**
Fix: ACP needs an explicit atmospheric/climate-implications paragraph in the conclusions; AGU needs Key Points + Plain Language Summary; ERL needs the Justification Statement; RSC needs a TOC graphic. Check `journal_guidelines.md`.

**9. "This contradicts [prior estimate] and the discrepancy isn't explained."**
Fix: reconcile explicitly and attribute the difference ("18 % lower than Lee et al. (2021), attributable to engine-resolved nvPM").

**10. "Figures are unreadable / fail in grayscale."**
Fix: colorblind-safe palette, redundant encoding, ≥ journal-minimum fonts at column width, self-contained captions, result-first references.

---

## Family B — aerospace engineering (AIAA)

**1. "No grid-convergence study."** (Often fatal.)
Fix: ≥3 meshes, report GCI and observed order for key quantities; discuss the GCI magnitude.

**2. "Verification and validation are confused."**
Fix: separate them explicitly using AIAA G-077 terms — verification (MMS/analytical/cited DB) vs validation (vs experiment with uncertainty).

**3. "'Agrees well' is not quantitative."**
Fix: give comparison error (%) and uncertainty bands on data and prediction.

**4. "Experimental uncertainty lacks a coverage factor."**
Fix: combine bias + precision; report ±X at 95 % confidence; describe facility and calibration.

**5. "The novelty claim is unsupported."**
Fix: cite the gap precisely; state the contribution as a measurable outcome; drop bare "novel/revolutionary".

**6. "Conclusions introduce new material / aren't quantitative."**
Fix: restate the actual quantitative findings parallel to the abstract; no new concepts or citations.

**7. "Reference list / nomenclature formatting is off."**
Fix: all authors (no "et al." in the list), full journal titles, DOIs; nomenclature section with symbols only (acronyms in text), not duplicated in prose.

**8. "Units and figures don't meet AIAA norms."**
Fix: dual SI/English; ≥8 pt fonts at 3.25 in; vector/600 dpi line art; perceptually-uniform colormaps; error bars on experimental points; mesh-detail inset on CFD contours.

**9. "Insufficient relevance to real aerospace systems."** (Especially JGCD/JPP.)
Fix: connect the result to a design decision, a flight condition, or hardware; state the engineering utility, not just the physics.

---

## A pre-submission pass (do this last)
Read the abstract and conclusions side by side — do the quantitative claims match, and are both bounded by the uncertainty/validation evidence? Then read only the figures and captions — does the story hold from figures alone? Most reviewer objections surface in that 10-minute pass.
