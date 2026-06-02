# Checklists — Uncertainty (Family A) & V&V (Family B)

Run the checklist matching the paper's family. Each item is phrased as the question a referee will ask.

---

## Family A — Uncertainty & forcing-claim checklist (atmospheric/climate)

**Claim discipline**
- [ ] Is every headline result reported with its uncertainty interval, not as a bare number?
- [ ] Is the confidence matched to the evidence (best estimate from a well-constrained model vs a "suggests")?
- [ ] Are claims bounded to the scenario/period studied (no silent extrapolation to other years/fleets/regions)?

**Interval & metric form**
- [ ] Bracket notation `X [lo, hi]` for asymmetric ranges, with the percentile stated (5–95 % by default)? (No ± on asymmetric distributions.)
- [ ] "Best estimate" used for the central value (not "mean"/"average"/"expected")?
- [ ] ERF preferred over RF, with the ERF/RF ratio stated and acknowledged as an extra uncertainty?
- [ ] IPCC AR6 likelihood/confidence terms used consistently where invoked?

**Uncertainty sourcing**
- [ ] Are the uncertainty sources enumerated, not gestured at?
- [ ] Is the dominant source named and the sources ranked (sensitivity)?
- [ ] For contrails specifically: are humidity-field/ERA5, initial ice-crystal number (nvPM EIn), optical depth, and the RF→ERF ratio each addressed?
- [ ] Is the sign of any sign-uncertain forcing (NOₓ, aerosol indirect) handled explicitly?

**Framing & numbers**
- [ ] CO₂/non-CO₂ partition given whenever net aviation forcing is discussed (correct denominator = net aviation ERF)?
- [ ] Units correct (mW m⁻² for global forcing; Tg yr⁻¹; EIn) and spelled out on first use?
- [ ] Significant figures honest (3 for best estimates; no false precision)?
- [ ] CO₂-equivalent framing for contrails avoided, or GWP horizon stated with the lifetime caveat?

**Reproducibility & journal furniture**
- [ ] Data and code in a repository with a DOI (never "available upon request" — banned at AGU)?
- [ ] Mandatory sections present: ACP implications; AGU Open Research + 3 Key Points + Plain Language Summary; ERL Justification Statement; RSC TOC graphic?
- [ ] Correct citation family (author-year for ERL/EGU/AGU)?

---

## Family B — Verification & Validation checklist (AIAA)

**Code verification (solving the equations right)**
- [ ] Verification stated — analytical solution, Method of Manufactured Solutions, or a cited solver-validation database (not just "the code is validated")?
- [ ] Spatial scheme order of accuracy stated (formally ≥2nd order)?

**Grid / mesh independence (the desk-reject item)**
- [ ] At least three systematically refined meshes?
- [ ] Grid Convergence Index (GCI) reported for the key quantities of interest (e.g. C_L, C_D, total-pressure recovery)?
- [ ] Observed order of convergence reported and sensible?
- [ ] GCI magnitude discussed (<1 % typically fine; 1–5 % needs comment)?

**Iterative / temporal convergence**
- [ ] Residual convergence criterion stated (e.g. 10⁻⁶ normalized) AND integrated quantities shown converged (not residuals alone)?
- [ ] Time-step sensitivity shown for unsteady cases?

**Validation (right equations vs reality)**
- [ ] Comparison to experiment or higher-fidelity data with percentage comparison error?
- [ ] Uncertainty bands on both the data and the comparison?
- [ ] "Verified" vs "validated" used precisely (AIAA G-077)?

**Experimental papers**
- [ ] Facility characterized (size, turbulence intensity, blockage ratio)?
- [ ] Instrumentation and calibration described?
- [ ] Bias and precision uncertainty estimated separately and combined (RSS)?
- [ ] Total uncertainty reported as ±X at a stated coverage factor (e.g. 95 % confidence)?
- [ ] Repeatability runs; blockage/Re corrections; Reynolds-number statement?

**Cycle / propulsion**
- [ ] Thermodynamic assumptions stated (gas model, polytropic-efficiency definition)?
- [ ] Component maps validated vs published/manufacturer data (redactions acknowledged)?
- [ ] Cycle closure (energy/mass balance) convergence reported?

**Conventions**
- [ ] Nomenclature section present and not duplicated in text; acronyms in text only?
- [ ] Numbered-bracket references, all authors listed, full journal titles, DOIs?
- [ ] Dual SI/English units; perceptually-uniform (non-jet) colormaps; ≥8 pt figure fonts?
- [ ] Conclusions restate findings quantitatively without new concepts/citations?
- [ ] Any "novel"/"first" claim backed by a cited gap?
