# Reviewing Clinical Trials

Clinical trials have stringent reporting and design standards. Many flaws are detectable by checking the trial registration against the manuscript and applying CONSORT.

## Table of contents

1. [The preregistration check](#the-preregistration-check)
2. [Primary endpoint integrity](#primary-endpoint-integrity)
3. [Population: ITT, mITT, per-protocol](#population-itt-mitt-per-protocol)
4. [Blinding](#blinding)
5. [Randomization](#randomization)
6. [Sample size and stopping rules](#sample-size-and-stopping-rules)
7. [Equipoise and ethics](#equipoise-and-ethics)
8. [Equivalence and non-inferiority trials](#equivalence-and-non-inferiority-trials)
9. [Subgroup analyses in trials](#subgroup-analyses-in-trials)
10. [Pragmatic vs. explanatory trials](#pragmatic-vs-explanatory-trials)
11. [Adaptive designs](#adaptive-designs)
12. [Observational clinical studies](#observational-clinical-studies)
13. [CONSORT checklist](#consort-checklist)

---

## The preregistration check

Before evaluating anything else, look up the trial registration.

**Registries:**

- ClinicalTrials.gov (US, default for most international work)
- ISRCTN registry (UK)
- EU Clinical Trials Register / CTIS
- ANZCTR (Australia/New Zealand)
- Japan Primary Registries Network
- ChiCTR (China)

**What to verify:**

- A registration number is in the manuscript (NCT, ISRCTN, EudraCT, ChiCTR, etc.).
- Registration date precedes enrollment.
- The registered primary endpoint matches the manuscript's primary endpoint.
- The registered analysis plan matches the manuscript's primary analysis.
- The registered sample size is consistent with the achieved sample size (or deviations are explained).
- The registered inclusion/exclusion criteria match the manuscript.

**Red flags:**

- Trial registered after enrollment began (or registered after the analysis was complete).
- Primary endpoint changed between registration and publication without justification.
- Analysis plan changed without justification.
- Trial publication omits results for some registered outcomes (selective reporting).
- The same trial is reported across multiple papers with different "primary" outcomes (salami slicing).

**Tools**: COMPare project documented discrepancies between registered and reported outcomes in many top journals. Reviewers can do a quick version of this manually.

## Primary endpoint integrity

The primary endpoint should be **pre-specified, singular (or hierarchically ordered), and stable** between protocol and report.

**What to check:**

- Is there one primary endpoint, or many "co-primary" endpoints? Co-primary endpoints require α adjustment.
- Is the primary endpoint clinically meaningful, or a surrogate? Surrogates need justification.
- Has the primary endpoint changed between protocol and publication?
- Are secondary endpoints clearly labeled as such?
- For trials with hierarchical testing, is the hierarchy pre-specified, and was it followed (don't claim significance for endpoint 3 if endpoint 2 failed without a closed-testing procedure)?

**Common issues:**

- "Primary endpoint switching": the trial was negative on the registered primary; a secondary endpoint becomes the headline.
- "Composite endpoint inflation": the primary endpoint is a composite (e.g., death + MI + stroke + revascularization), and the positive driver is the softest component (revascularization).
- Endpoint definitions changed (e.g., from "30-day mortality" to "in-hospital mortality").

## Population: ITT, mITT, per-protocol

- **Intention-to-treat (ITT)**: All randomized participants are analyzed in their assigned group, regardless of adherence. Preserves the benefits of randomization. Default for superiority trials.
- **Modified ITT (mITT)**: ITT with some justified exclusions (e.g., those who never received any treatment). Should be pre-specified and minimal.
- **Per-protocol (PP)**: Only adherent participants. Biased toward showing efficacy but informative as a secondary.
- **As-treated**: Analyzed by treatment actually received. Used in safety analyses.

**What to check:**

- Is the primary analysis ITT (for superiority trials)?
- Are exclusions from ITT (creating mITT) pre-specified and justified?
- Is there a CONSORT flow diagram showing how participants are accounted for?
- For non-inferiority trials, both ITT and PP analyses should support non-inferiority (more conservative for NI claims).

**Red flag**: Per-protocol presented as primary in a superiority trial.

## Blinding

- Who was blinded (participants, providers, outcome assessors, statisticians)?
- Were assessments of subjective outcomes done by blinded assessors?
- Was blinding successful (sometimes assessed by a post-trial questionnaire)?
- For unblinded trials (open-label), are objective endpoints used or were outcome assessors blinded?

**Common issues:**

- Open-label trial with subjective primary endpoint (e.g., patient-reported pain) — high risk of bias.
- "Double-blind" without specifying who the two parties are.
- Loss of blinding through obvious treatment differences (taste, side effects) that compromises the trial.

## Randomization

- How was the randomization sequence generated (computer-generated random numbers, block, stratified)?
- How was allocation concealed (central randomization, sealed envelopes, web-based)?
- Was baseline balance achieved? Imbalance suggests randomization failure.

**Red flag**: Significant baseline imbalance in a randomized trial may indicate a randomization problem (especially in small trials, but should be examined in larger ones too).

## Sample size and stopping rules

- Is the sample size calculation pre-specified, with clinically meaningful effect size, power, and α?
- For event-driven trials, is the number of events specified?
- For trials with planned interim analyses, are stopping rules pre-specified (e.g., O'Brien-Fleming, Lan-DeMets)?
- Was the trial stopped early? If so, why (efficacy, futility, safety, other)?

**Red flag**: Trial stopped early for efficacy without pre-specified stopping rules often overestimates effects.

## Equipoise and ethics

- Was there genuine clinical equipoise (collective uncertainty about which arm is better) at the time of the trial?
- Are placebo-controlled designs justified when effective treatments exist? Active-comparator designs are often more ethical.
- Are inclusion criteria appropriate (no exclusion of populations that will receive the treatment in practice)?
- Are stopping rules for adverse events pre-specified?

## Equivalence and non-inferiority trials

- Is the non-inferiority margin (Δ) pre-specified and clinically justified?
- Is the margin smaller than the effect size on which the active comparator was approved?
- Both ITT and PP analyses should support non-inferiority.
- The CI for the difference should lie entirely within the non-inferiority margin.
- Was the trial designed with sufficient sample size to demonstrate non-inferiority?

**Common issue**: A non-inferiority margin chosen post-hoc to fit the observed difference.

## Subgroup analyses in trials

- Are subgroups pre-specified?
- Is the formal interaction test reported (not just within-subgroup comparisons)?
- Are subgroup effects within the range expected by chance given the number tested?
- Headline claims about subgroups, especially when the main effect is null, should be treated as exploratory.

## Pragmatic vs. explanatory trials

- **Explanatory** (efficacy): Tightly controlled, narrow population, optimal adherence. "Can it work?"
- **Pragmatic** (effectiveness): Real-world conditions, broader population, usual adherence. "Does it work?"

Different designs for different questions. Reviewers should check that the design matches the claim. Don't apply explanatory standards to pragmatic trials or vice versa. PRECIS-2 framework characterizes where on the spectrum a trial sits.

## Adaptive designs

Trials with adaptive features (sample-size re-estimation, response-adaptive randomization, basket/umbrella designs):

- Adaptations should be pre-specified in the protocol and statistical analysis plan.
- Type I error rate should be controlled at the planned level.
- Analysis methods should account for adaptation.
- DSMB decisions and access to interim data should be tightly controlled.

## Observational clinical studies

For cohort, case-control, and cross-sectional studies, STROBE applies.

Key concerns:
- Confounding (see `statistical_pitfalls.md` baseline imbalance section).
- Reverse causation.
- Selection bias.
- Misclassification (especially differential between groups).
- Time-related biases (immortal time bias, lead-time bias, length bias).

For database studies (claims, EHR, registries):
- Code-list validation (ICD, CPT, SNOMED codes are imperfect proxies for clinical conditions).
- Missingness pattern (in EHR data, missingness is often informative).
- Channeling and confounding by indication.

## CONSORT checklist

CONSORT 2010 (with extensions) is the standard reporting guideline for parallel-group randomized trials. The checklist has 25 items covering title/abstract, introduction, methods, results, discussion, and other information.

Reviewers should:
- Verify CONSORT compliance for trial papers in journals that endorse it (most major medical journals).
- Check for the CONSORT flow diagram showing screening, randomization, allocation, follow-up, and analysis.
- Use CONSORT extensions where applicable: CONSORT-NPT (non-pharmacologic), CONSORT-Cluster (cluster randomization), CONSORT-PRO (patient-reported outcomes), CONSORT-AI (AI interventions), SPIRIT (protocols), CONSORT-Equity, etc.

Source: https://www.equator-network.org/reporting-guidelines/consort/

## Common review requests for clinical trials

- Report ITT analysis as primary.
- Provide CONSORT flow diagram.
- Explain discrepancy between registered and reported endpoints.
- Provide pre-specified analysis plan.
- Sensitivity analyses for missing data.
- Subgroup analyses with formal interaction tests.
- Effect sizes with CIs (not just p-values).
- Adverse events tabulated systematically.

## What's usually unreasonable

- Demanding an additional trial.
- Demanding analyses outside what the protocol enables.
- Insisting on a specific design feature when the existing one is reasonable.
