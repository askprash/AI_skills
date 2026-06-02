# Structured Ideation Methods (with field examples)

Use these when free-flowing brainstorming stalls or when systematic coverage is wanted. Each is illustrated in this researcher's fields.

## SCAMPER (transform an existing study/system)
- **Substitute** — swap a component: replace ERA5 humidity with radiosonde or a higher-resolution reanalysis; substitute a fleet-average nvPM index with engine-resolved values.
- **Combine** — merge two threads: couple a contrail model with an air-traffic-flow optimizer; combine cycle analysis with emissions accounting for a hybrid-electric concept.
- **Adapt** — borrow from elsewhere: adapt CFD grid-convergence/GCI machinery to quantify discretization error in a global contrail simulation.
- **Modify / magnify** — change scale or resolution: push a regional contrail study to global, or refine to per-flight; magnify the time horizon (decadal response).
- **Put to another use** — repurpose data: use operational flight-tracking (ADS-B) data, collected for ATM, to estimate contrail formation.
- **Eliminate** — drop an assumption or step: remove the constant-ice-crystal-number assumption; eliminate the RF→ERF fixed ratio and model the response directly.
- **Reverse** — invert the question: instead of "how much do contrails warm?", ask "which 2 % of flights cause most of the forcing, and what do they have in common?"

## Morphological analysis (systematic combination)
List the independent dimensions of a problem and enumerate combinations. *Example — contrail mitigation:* dimensions = {lever: reroute vertically / reroute laterally / engine tech / fuel} × {decision data: forecast humidity / nowcast / climatology} × {objective: min energy forcing / min net climate incl. CO₂ penalty} × {scale: single airline / regional / global}. Each cell is a candidate study; the empty/under-studied cells are your gaps.

## Assumption reversal
Write the field's load-bearing assumptions, then flip each:
- "Contrail cirrus is net warming globally" → where/when is it net cooling, and what controls the sign?
- "Humidity-field error dominates contrail-RF uncertainty" → construct a case where ice-crystal-number error dominates.
- "Non-CO₂ effects should be expressed as CO₂-equivalent" → what breaks when you do, and what metric is better?

## Cross-domain analogy
Map structure from another field onto yours:
- *Operations research* → contrail-avoidance routing as a constrained optimization / Pareto problem (fuel penalty vs forcing reduction).
- *Epidemiology of skew* (a few causes → most of an effect) → "2 % of flights → 80 % of energy forcing" type concentration analyses (Lorenz curves).
- *CFD verification & validation* → formal uncertainty quantification for climate-forcing estimates.
- *Propulsion systems* → boundary-layer ingestion, distributed/hybrid-electric architectures as new emissions/forcing regimes.

## Literature-gap finding (push against the state of the art)
Use the exemplar papers in `atmospheric_climate_style.md` §H (and `aiaa_engineering_style.md` for the engineering side) as the current frontier and interrogate them:
1. **What did the landmark estimate assume** that newer data could relax? (e.g. Burkhardt & Kärcher's parameterizations; Lee et al.'s expert-judgement uncertainty terms.)
2. **Which uncertainty did the authors flag as dominant** and say needed future work? That sentence is often a ready-made project.
3. **What changed in the world** since the paper (new inventories, COVID natural experiment, SAF deployment, new satellite retrievals) that lets you redo or extend it?
4. **What's the next metric or scale** the result hasn't been expressed in (temperature, economic cost, per-route, real-time operational)?
5. **Where do two landmark papers disagree**, and can you design the study that reconciles them?

Then state the gap the way a paper would: a specific methodological or data limitation of prior work, enumerated (i)/(ii)/(iii) — which is exactly how the Introduction will later motivate the study.

## Six-hats quick pass (for a group or a self-check)
Run an idea through: facts (what's known/measured), feelings (intuition about what's interesting), caution (what could be wrong — hand to `research-critique`), optimism (best case), creativity (wild variants), process (next concrete step). A fast way to make sure an exciting idea is also a sound one.
