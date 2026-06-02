# Reporting Standards

Reporting guidelines tell authors what to include and reviewers what to check. The EQUATOR Network (https://www.equator-network.org/) maintains the canonical index of over 600 guidelines.

This file lists the most commonly invoked ones in peer review.

## Table of contents

1. [Selection guide](#selection-guide)
2. [Clinical trials](#clinical-trials)
3. [Observational epidemiology](#observational-epidemiology)
4. [Systematic reviews and meta-analyses](#systematic-reviews-and-meta-analyses)
5. [Diagnostic and prognostic studies](#diagnostic-and-prognostic-studies)
6. [Animal research](#animal-research)
7. [Genomics and omics](#genomics-and-omics)
8. [Qualitative research](#qualitative-research)
9. [Case reports](#case-reports)
10. [Health-economic evaluation](#health-economic-evaluation)
11. [AI in medicine and ML reporting](#ai-in-medicine-and-ml-reporting)
12. [Other useful guidelines](#other-useful-guidelines)

---

## Selection guide

| Study type | Guideline | Notes |
|------------|-----------|-------|
| Randomized trial (parallel) | CONSORT 2010 | + extensions for non-pharmacologic, cluster, AI, etc. |
| Trial protocol | SPIRIT 2013 | Companion to CONSORT |
| Observational (cohort, case-control, cross-sectional) | STROBE | + STROBE-vet, STROBE-ID, STROBE-RDS extensions |
| Systematic review / meta-analysis | PRISMA 2020 | + PRISMA-P (protocols), PRISMA-ScR (scoping), PRISMA-IPD |
| Diagnostic accuracy | STARD 2015 | |
| Prognostic model | TRIPOD 2015 | + TRIPOD+AI for AI-based prognostic models |
| Animal preclinical | ARRIVE 2.0 | |
| Microarray | MIAME | |
| Sequencing | MINSEQE | |
| Mass spectrometry | MIAPE | |
| Qualitative research | SRQR or COREQ | |
| Case report | CARE | |
| Health-economic | CHEERS 2022 | |
| Quality improvement | SQUIRE 2.0 | |
| ML for health | TRIPOD+AI, CONSORT-AI, SPIRIT-AI, DECIDE-AI, MI-CLAIM | |
| Real-world evidence | RECORD, RECORD-PE | |

When in doubt, search EQUATOR (https://www.equator-network.org/reporting-guidelines/) for the study type.

## Clinical trials

### CONSORT 2010

For parallel-group randomized trials. 25-item checklist covering:

- Title and abstract (identification as randomized, structured summary)
- Introduction (background, objectives)
- Methods (trial design, participants, interventions, outcomes, sample size, randomization, blinding, statistics)
- Results (participant flow, recruitment, baseline, numbers analyzed, outcomes and estimation, ancillary analyses, harms)
- Discussion (limitations, generalizability, interpretation)
- Other (registration, protocol, funding)

CONSORT flow diagram (enrollment → allocation → follow-up → analysis) is mandatory.

**Extensions:**
- CONSORT-NPT (non-pharmacologic treatments)
- CONSORT-Cluster (cluster randomization)
- CONSORT-PRO (patient-reported outcomes)
- CONSORT-Harms
- CONSORT-Equity
- CONSORT-AI (AI interventions)
- Many others — check EQUATOR.

### SPIRIT 2013

Companion checklist for trial protocols. 33 items. If reviewing a protocol or a paper that cites its protocol, check that the protocol followed SPIRIT.

## Observational epidemiology

### STROBE

For cohort, case-control, and cross-sectional studies. 22-item checklist.

Key items:
- Study design clearly stated.
- Setting, participants, eligibility criteria.
- Variables defined a priori, including outcomes, exposures, predictors, potential confounders, effect modifiers.
- Data sources and measurement.
- Bias addressed.
- Statistical methods including handling of missing data, sensitivity analyses.
- Participants flow.
- Effect estimates with CIs and adjusted/unadjusted comparisons.

Extensions: STROBE-vet (veterinary), STROBE-ID (infectious disease), STROBE-RDS (respondent-driven sampling), STROBE-MR (Mendelian randomization), RECORD (routinely collected data), RECORD-PE (pharmacoepidemiology).

## Systematic reviews and meta-analyses

### PRISMA 2020

27-item checklist for systematic reviews. Major elements:

- Title identifies as a systematic review.
- Structured abstract.
- Rationale, objectives, registration (PROSPERO or equivalent).
- Eligibility criteria, information sources, search strategy.
- Selection process, data collection, data items.
- Study risk-of-bias assessment, effect measures, synthesis methods, additional analyses, certainty assessment (GRADE).
- Results: study selection (PRISMA flow diagram), characteristics, risk of bias, results of syntheses, additional analyses.
- Discussion, conclusions, funding, registration.

PRISMA flow diagram is mandatory.

Extensions: PRISMA-P (protocols), PRISMA-ScR (scoping reviews), PRISMA-IPD (individual patient data), PRISMA-DTA (diagnostic test accuracy), PRISMA-NMA (network meta-analysis), PRISMA-Equity, PRISMA-Harms, PRISMA-S (search), PRISMA-A (abstracts).

Risk-of-bias tools to expect:
- **Cochrane RoB 2** for randomized trials.
- **ROBINS-I** for non-randomized intervention studies.
- **QUADAS-2** for diagnostic accuracy.
- **PROBAST** for prognostic models.
- **AMSTAR 2** for reviews of systematic reviews.

Heterogeneity and certainty:
- **I²** (proportion of variance from heterogeneity), τ² (between-study variance) reported.
- **GRADE** for certainty of evidence by outcome.
- **Funnel plots / Egger's test** for small-study effects / publication bias when ≥10 studies.

## Diagnostic and prognostic studies

### STARD 2015

For studies of diagnostic accuracy. 30-item checklist. Key items: index test and reference standard described, participants flow, 2×2 table, sensitivity, specificity, predictive values with CIs.

### TRIPOD 2015 / TRIPOD+AI

For prognostic and prediction-model studies. 22-item checklist. Type of analysis (development, validation, development+validation), predictors, outcome, sample size, missing data, model specification, performance (discrimination AUC, calibration), validation (internal, external).

TRIPOD+AI extends TRIPOD for AI-based models with additional items on data sources, fairness, code/model availability, and updating.

## Animal research

### ARRIVE 2.0

20 items in two priority sets. Essential 10 (priority 1):
- Study design (groups, control, randomization, blinding)
- Sample size justification
- Inclusion and exclusion criteria
- Randomization
- Blinding
- Outcome measures
- Statistical methods
- Experimental animals (species, sex, age, weight, source)
- Experimental procedures
- Results (numbers, summary statistics, effects)

Plus recommended set (priority 2): abstract, background, objectives, ethical statement, housing/husbandry, animal care/monitoring, interpretation, generalizability, protocol registration, data access, declaration of interests.

The 3Rs (replacement, reduction, refinement) should be addressed.

## Genomics and omics

- **MIAME** (Minimum Information About a Microarray Experiment): experimental design, samples, hybridization, measurements, controls, data normalization, annotation.
- **MIAPE** (Minimum Information About a Proteomics Experiment).
- **MINSEQE** (Minimum Information About a high-throughput SEQuencing Experiment).
- **MIQE** (Minimum Information for publication of Quantitative real-time PCR Experiments).
- **MIRAGE** (Minimum Information Required About a Glycomics Experiment).
- **MIBBI portal** indexes these and others.

Data deposition is expected:
- Microarray / sequencing → GEO (NCBI), ArrayExpress, ENA, SRA.
- Proteomics → PRIDE, MassIVE.
- Metabolomics → MetaboLights, Metabolomics Workbench.
- Single-cell → cellxgene, HCA Data Portal, GEO.
- Genomic variation → dbGaP, EGA, ClinVar.

Accession numbers should be reported in the paper.

## Qualitative research

- **SRQR** (Standards for Reporting Qualitative Research): 21 items covering title/abstract, problem formulation, research design, sampling, data collection, analysis, results, discussion.
- **COREQ** (Consolidated criteria for Reporting Qualitative research): 32 items focused on interviews and focus groups.

Check that the chosen approach (phenomenological, ethnographic, grounded theory, etc.) is appropriate and consistently applied; that reflexivity is addressed; that data saturation or theoretical sufficiency is discussed.

## Case reports

### CARE

For case reports. 13 items including: title, key words, abstract, introduction, patient information, clinical findings, timeline, diagnostic assessment, therapeutic intervention, follow-up and outcomes, discussion, patient perspective, informed consent.

Informed consent for case publication (especially with identifying images) is essential.

## Health-economic evaluation

### CHEERS 2022

28-item checklist for health-economic evaluations. Title, abstract, intro, methods (population, setting, perspective, comparators, time horizon, discount rate, outcomes, measurement, valuation, currency/conversion, cost-effectiveness analysis, modeling, assumptions, analytics), results (parameters, summary, base case, uncertainty, heterogeneity), discussion, other.

## AI in medicine and ML reporting

A relatively new and rapidly evolving area:

- **TRIPOD+AI** (2024) — prediction models including AI.
- **CONSORT-AI** — RCTs of AI interventions.
- **SPIRIT-AI** — protocols for trials of AI interventions.
- **DECIDE-AI** — early-stage clinical evaluation of AI decision support.
- **MI-CLAIM** — medical AI checklist (more general).
- **CLAIM** (Checklist for Artificial Intelligence in Medical Imaging) — imaging-specific.
- **STARD-AI** — diagnostic accuracy of AI.
- **CHARMS-AI** — systematic reviews of prediction-model studies including AI.

For ML papers outside medicine, see the NeurIPS reproducibility checklist, ML reproducibility checklist (Pineau et al.), and `ml_paper_specifics.md`.

## Other useful guidelines

- **SQUIRE 2.0** — quality improvement.
- **TIDieR** — intervention description (use alongside CONSORT for non-pharmacologic; alongside SPIRIT for protocols).
- **PRISMA-S** — reporting literature searches.
- **CHEERS** — economic evaluations.
- **STREGA** — STROBE extension for genetic association.
- **STROBE-MR** — Mendelian randomization.
- **GRIPP2** — patient and public involvement reporting.
- **GUIDED** — guidelines for reporting medical devices.
- **REMARK** — tumour marker prognostic studies.
- **AGREE II** — clinical practice guideline evaluation.

## Practical advice for reviewers

- Look up the relevant guideline before reviewing if you're unsure of the field's conventions.
- Don't demand a guideline that doesn't apply (CONSORT for an observational study, ARRIVE for a human study).
- A missing checklist item is rarely fatal in isolation but a pattern of missing items suggests under-reporting.
- Many journals require authors to upload a completed checklist; verify if you can.
- EQUATOR Network is the authoritative source (https://www.equator-network.org/).
