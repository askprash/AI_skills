# Section-by-Section Checklists

Use as a working aid, not a script to recite in the review. The goal is to surface real, specific issues — not to confirm that all boxes are checked.

## Table of contents

1. [Title and abstract](#title-and-abstract)
2. [Introduction](#introduction)
3. [Methods](#methods)
4. [Results](#results)
5. [Discussion](#discussion)
6. [References and citations](#references-and-citations)
7. [Supplementary materials](#supplementary-materials)
8. [Letters, short reports, and case reports](#letters-short-reports-and-case-reports)
9. [Review articles and meta-analyses](#review-articles-and-meta-analyses)
10. [Methods and tools papers](#methods-and-tools-papers)

---

## Title and abstract

- Does the title accurately reflect the work? Avoid both blandness ("A study of X") and overclaim ("A novel breakthrough in X").
- Does the abstract follow the venue's structure (structured: Background/Methods/Results/Conclusions, vs. unstructured)?
- Are the headline numbers in the abstract consistent with the body? (Look for this — abstract-body mismatch is common.)
- Are conclusions in the abstract proportionate to the evidence?
- Are key terms searchable? (Important for indexing and citation.)
- Does the abstract include effect sizes / confidence intervals, not just p-values?

**Common issues:**
- Abstract claims an effect that the body actually shows is not statistically significant.
- "Significant" used to mean "important" rather than "statistically significant", or vice versa.
- Causal language in the abstract for an observational study.

---

## Introduction

- Is the research question clearly stated by the end of the introduction?
- Is the gap in the literature articulated specifically (not "much remains unknown")?
- Is the prior literature represented fairly, including work that disagrees with the authors' framing?
- Are hypotheses (if any) preregistered or post-hoc? Watch for HARKing — see `statistical_pitfalls.md`.
- Is the contribution claim accurate? (Sometimes "first to" is technically wrong.)
- Is the introduction proportionate? A long introduction often masks thin results.

**Common issues:**
- The introduction motivates one question; the methods answer a different one.
- Citation padding — long strings of citations after each claim without engaging substance.
- Cherry-picked literature that omits inconvenient prior findings.

---

## Methods

The methods section bears most of the rigor weight. Read it carefully and read it *after* results so you can check whether the methods actually support what was claimed.

**Reproducibility:**
- Could a competent peer reproduce the study from this description plus reasonable inquiry?
- Are reagents, equipment, kits, antibodies (with RRIDs), cell lines, and software versions specified?
- Are exact parameters (concentrations, durations, temperatures, software flags) given?
- Are protocols deposited (protocols.io, OSF) where appropriate?

**Design:**
- Is the design appropriate for the research question? (E.g., a cross-sectional design can't answer a causal question.)
- Are positive and negative controls included where needed?
- Are biological and technical replicates distinguished? Are they sufficient?
- Is randomization described, including the method (block, stratified, simple)?
- Is blinding described (single, double, none, and at which stages: allocation, data collection, analysis)?
- Are inclusion/exclusion criteria preregistered or post-hoc?

**Sample size:**
- Is sample size justified — power calculation, precision target, feasibility constraint?
- Is the justification plausible? (Power calculations are often performed post-hoc to fit the achieved sample size.)
- For multi-level designs, is the unit of analysis correct? (E.g., are mice or pups the unit; are cells or wells the unit?)

**Ethics and approvals:**
- IRB / ethics committee approval for human subjects research (with approval number).
- IACUC or equivalent approval for animal work (with approval number, ARRIVE compliance).
- Informed consent procedure.
- Data-sharing agreements where applicable.

**Statistics:**
- Are tests appropriate for the data (normality, independence, balance, censoring)?
- Are multiple-comparison corrections applied, and is the method specified?
- Are confidence intervals reported with effect sizes?
- Are missing data handled explicitly (listwise, imputation, sensitivity analysis)?
- Is the analysis preregistered or post-hoc?
- Is software (with version) and code availability stated?

See `statistical_pitfalls.md` for deeper coverage. See `clinical_trial_specifics.md` for trials. See `ml_paper_specifics.md` for ML methods.

**Computational:**
- Software versions, dependencies, hardware where relevant (especially compute hours and accelerator type for ML).
- Code availability statement (a real link to a real repo, not "available upon request").
- Containers, environment files, seeds.

---

## Results

- Are results presented in the same order as the methods?
- Are all preregistered analyses reported, including null results?
- Are post-hoc analyses labeled as exploratory?
- Are effect sizes reported with confidence intervals, not just p-values?
- Are visualizations appropriate for the data type? (Bar charts for distributions, line plots for trajectories, etc. — see `figure_integrity.md`.)
- Do the numbers in the text match the numbers in the figures and tables?
- Are sample sizes reported with every result (n per group, not just total n)?
- For each statistical comparison: test name, test statistic, df, p-value, effect size, CI.

**Common issues:**
- Selective reporting (results from some preregistered outcomes omitted).
- Over-reliance on representative images for variable phenomena (n=1 western blots for "representative" of unspecified replicates).
- Subgroup analyses presented as planned when they were exploratory.
- "Trends toward significance" language (p=0.07 is not a trend; it's a p-value).

---

## Discussion

- Does the discussion accurately summarize what was found?
- Are conclusions proportionate to the evidence? Causal claims from observational data are a frequent over-reach.
- Are limitations enumerated specifically, not boilerplate?
- Is contradicting evidence from prior work addressed (not just ignored)?
- Is the mechanism, where claimed, actually supported by the data?
- Are clinical / practical implications proportionate? "May lead to new therapies" is often unsupported.
- Are next steps concrete or vague hand-waving?

**Common issues:**
- "Significance" overstated by switching from statistical to clinical/practical importance without justification.
- Mechanism inferred from association.
- Limitations dispatched in two sentences as if to clear a checklist.
- The discussion talks about a different paper than the methods and results did.

---

## References and citations

- **Existence and accuracy**: spot-check 5–10 citations. Do the papers exist? Do they say what's claimed? In 2026, fabricated citations from AI-assisted writing are common — verify a sample, especially for surprising or load-bearing claims.
- **Currency**: are recent landmark papers cited, especially anything in the last 2–3 years?
- **Balance**: are critics of the authors' framing cited?
- **Self-citation**: excessive self-citation (or self-citation networks) is a flag.
- **Predatory venue citations**: citations to retracted papers or known predatory journals should be noted.
- **Citation style consistency**: minor but worth flagging if egregious.

**Procedure**: pick 3–5 surprising or central claims. For each, locate the cited reference and confirm it actually supports the claim. If you can't verify (paywall, language), say so.

---

## Supplementary materials

- Are the supplements actually supplementary, or is critical methodology hidden there because it wouldn't fit the main text?
- Are supplementary figures necessary or padding?
- Do supplementary tables include the data needed to reproduce main analyses?
- Are deposition links live? (Sometimes "deposited at GEO under accession GSE######" is stated and the accession doesn't exist yet.)

---

## Letters, short reports, and case reports

Apply scaled-down expectations:

- **Brief reports** still need adequate methods (often in supplement), appropriate statistics, and proportionate conclusions.
- **Case reports** need clear novelty justification (why this case is publishable), informed consent for case details (especially images), and CARE-statement compliance.
- **Letters / commentaries** should be evaluated on argument strength and engagement with the work they comment on, not on novel data generation.

---

## Review articles and meta-analyses

- **Systematic reviews / meta-analyses**: PRISMA flow diagram, preregistration (PROSPERO), search strategy reported (databases, dates, keywords, filters), inclusion/exclusion criteria, risk-of-bias assessment (Cochrane RoB 2, ROBINS-I, etc.), heterogeneity (I², τ²), publication-bias assessment.
- **Narrative reviews**: scope, organization, criticality (not just summarization), balance, currency.
- **Scoping reviews**: PRISMA-ScR.

See `reporting_standards.md` for the relevant checklists.

**Common issues:**
- "Systematic review" without a documented search strategy.
- Meta-analysis pooling heterogeneous studies without justifying combinability.
- Funnel plot omitted or unaddressed publication bias.

---

## Methods and tools papers

- Is the method validated against existing methods on appropriate benchmarks?
- Are limitations and failure modes characterized, not just successes?
- Is the tool actually available (working code, working installation instructions, working examples)?
- Is the user community served (documentation, license, dependency management)?
- For ML tools, see `ml_paper_specifics.md`.

**Common issues:**
- Comparison to weakened baselines (default hyperparameters for the comparison, tuned for the proposed method).
- Benchmark cherry-picking.
- "Available at github.com/..." links that are private, empty, or 404.

---

## What to do with each issue

For every issue you flag, assign it to one of:

- **Critical** — central claims unsupported, integrity concerns, fatal design flaw.
- **Major** — methodological or interpretive issues authors must address but that don't invalidate the work.
- **Minor** — clarification, missing citation, typo, presentational nit.
- **Question** — needs author response before judgment.

Then map them into the review template (`assets/review_template.md`). Don't put minor issues in the major section; doing so makes the major comments seem padded and undermines the serious points.
