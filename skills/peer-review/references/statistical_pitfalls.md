# Statistical Pitfalls

A working reference for the statistical and methodological issues that come up most often in peer review. Each entry: what it is, how to detect it, what to ask of authors.

## Table of contents

1. [P-hacking and the garden of forking paths](#p-hacking-and-the-garden-of-forking-paths)
2. [HARKing](#harking)
3. [Multiple testing without correction](#multiple-testing-without-correction)
4. [Underpowered studies and post-hoc power](#underpowered-studies-and-post-hoc-power)
5. [Inappropriate test choice](#inappropriate-test-choice)
6. [Pseudoreplication and wrong unit of analysis](#pseudoreplication-and-wrong-unit-of-analysis)
7. [Baseline imbalance and confounding](#baseline-imbalance-and-confounding)
8. [Inappropriate causal language](#inappropriate-causal-language)
9. [Subgroup analyses](#subgroup-analyses)
10. [Selection bias and survivorship](#selection-bias-and-survivorship)
11. [Regression-to-the-mean errors](#regression-to-the-mean-errors)
12. [Missing data handling](#missing-data-handling)
13. [Reporting issues](#reporting-issues)
14. [Bayesian-specific issues](#bayesian-specific-issues)
15. [Detecting p-hacking from reported values](#detecting-p-hacking-from-reported-values)

---

## P-hacking and the garden of forking paths

Researchers (often unintentionally) try multiple analytic choices and report the one that "worked". Choices include: which variables to include as covariates, where to set cutoffs, which transformation to apply, which outliers to exclude, which subgroup to focus on, when to stop collecting data.

**Detection cues:**
- Unusual cutoffs that aren't justified by external criteria (e.g., "we excluded participants over 64.7 years old").
- Many borderline p-values clustered around 0.05.
- Lots of covariates in the final model with no preregistration.
- Exclusions performed *after* the analysis was begun.
- Different methods used across "similar" comparisons in the paper.

**Ask authors:** Was the analysis preregistered (and if so, where)? What pre-specified decisions did you change, and why? Provide a sensitivity analysis varying the key analytic choices.

## HARKing

Hypothesizing After Results are Known: the paper presents a post-hoc finding as if it were a pre-specified hypothesis.

**Detection cues:**
- Introduction frames a question that exactly matches a positive result in the data.
- A "surprising" finding is also the central finding, and the introduction predicts it.
- The hypothesis appears designed-to-fit the available outcome.
- Preregistration (if any) doesn't mention the now-central hypothesis.

**Ask authors:** Was this hypothesis specified in advance? If so, where (preregistration, prior grant)? If not, please label it as exploratory.

## Multiple testing without correction

Running many statistical tests inflates the chance of false positives. With α=0.05 and 20 tests, expected false positives is 1 by chance alone.

**Detection cues:**
- Many tests, no correction mentioned.
- "Significant" results scattered through a results table of many comparisons.
- Omics, imaging, or any high-dimensional analysis without FDR or family-wise correction.
- Multiple primary outcomes in a clinical trial without prespecified hierarchy.

**Ask authors:** Apply Bonferroni / Holm / FDR correction. State the family of tests. If using a closed-testing or hierarchical procedure, describe it explicitly.

**Note:** Bonferroni is conservative; Benjamini-Hochberg FDR is appropriate for many high-dimensional contexts. Don't reflexively demand Bonferroni.

## Underpowered studies and post-hoc power

Small samples have low power to detect real effects and inflate the magnitude of any "detected" effect (winner's curse).

**Detection cues:**
- Small n with large reported effects, especially with wide CIs.
- "Power calculation" after data collection, conveniently matching n.
- Conclusions of "no difference" based on non-significant tests in underpowered designs.

**Ask authors:** Justify the planned sample size with a power calculation referenced to the smallest effect of interest. Report CIs around effect sizes. Don't interpret p>0.05 as "no effect" without explicit equivalence testing.

**Note:** Post-hoc power calculations using the observed effect size are uninformative and should not be used.

## Inappropriate test choice

- **t-test on non-normal small samples** without checking assumptions or using a rank-based alternative.
- **ANOVA followed by t-tests** without correction for the family of pairwise comparisons.
- **Pearson correlation on non-linear or rank data**.
- **Chi-square with low expected cell counts** (use Fisher's exact).
- **Linear regression on bounded outcomes** (proportions, counts, durations) without transformation or a generalized linear model.
- **Repeated measures analyzed as independent** (a common pseudoreplication error).
- **Censored survival data analyzed with t-tests** instead of survival methods.

**Ask authors:** Justify the test choice. Verify assumptions (normality, homoscedasticity, independence). Where assumptions fail, refit with an appropriate method as a sensitivity analysis.

## Pseudoreplication and wrong unit of analysis

The fundamental question: what's the experimental unit?

- If animals are randomized but cells within animals are analyzed as independent, the test is pseudoreplicated.
- If clinics are randomized but patients are analyzed as independent, the test is pseudoreplicated.
- Hierarchical / mixed-effects models with random effects for the clustering unit are the standard fix.

**Detection cues:**
- "n=1,200 cells from 3 mice." The n is 3, not 1,200, for many comparisons.
- "n=600 patients from 4 hospitals." The n for hospital-level effects is 4.
- No mixed-effects model in a clearly clustered design.

**Ask authors:** Identify the unit of randomization / sampling. Use mixed-effects models or analyze at the appropriate level.

## Baseline imbalance and confounding

In observational studies, comparison groups differ in ways that confound the exposure–outcome relationship.

**Detection cues:**
- Table 1 shows statistically or practically significant baseline differences that aren't addressed.
- No adjustment for known confounders.
- "Adjusted" models that omit important confounders or include mediators (which biases the estimate).
- Propensity-score matching without checking balance after matching.

**Ask authors:** Adjust for known confounders. Show balance after matching/weighting. Justify the variable selection (DAG-based reasoning preferred). Don't adjust for mediators or colliders.

## Inappropriate causal language

Observational studies usually can't establish causation. Watch for:

- "Caused", "led to", "resulted in", "produces", "drives" in observational designs.
- Headline claims that imply intervention will yield the observed association.
- Mechanistic claims without mechanistic evidence (in vitro mechanism plus observational human association ≠ established causal pathway in humans).

**Ask authors:** Soften causal language to associational where appropriate. Discuss residual confounding and reverse causation. If using formal causal inference (instrumental variables, regression discontinuity, difference-in-differences), justify identifying assumptions.

## Subgroup analyses

Subgroup analyses are prone to false positives. A "significant" subgroup result with no significant main effect, or a subgroup result that's bigger than the main effect, is suspicious.

**Detection cues:**
- Many subgroups tested, one is significant, headline focuses on that one.
- Subgroup not preregistered, no formal interaction test, no adjustment for multiple subgroups.
- Forest plot with many subgroups in which only one or two CIs exclude the null.

**Ask authors:** Was the subgroup pre-specified? Report a formal interaction test. Correct for the number of subgroups examined. Label exploratory subgroup findings as such.

## Selection bias and survivorship

When the sample isn't representative of the target population, or attrition is informative, conclusions don't generalize.

**Detection cues:**
- Convenience sample described as representative.
- High attrition without comparison of dropouts vs. completers.
- "Per-protocol" analyses that exclude non-adherent participants without complementary ITT analysis.
- Sampling from clinics, online platforms, or registries presented as population-level.

**Ask authors:** Characterize selection. Compare baseline characteristics of included and excluded individuals. Provide ITT analysis for trials.

## Regression-to-the-mean errors

When participants are selected on extreme baseline values, their follow-up values tend to move toward the mean regardless of any intervention. Mistaking this for treatment effect is common in pre–post designs without a control group.

**Detection cues:**
- Pre–post design with no control group, selecting extreme baseline participants.
- "Patients improved after intervention" with no comparator.

**Ask authors:** Include a control group. Or use a design (e.g., RCT) that can separate intervention from regression to the mean.

## Missing data handling

- **Listwise deletion** assumes data are missing completely at random and discards information.
- **Single imputation** (mean, last observation carried forward) understates uncertainty and can bias estimates.
- **Multiple imputation** with appropriate models is the modern standard.
- **Complete-case analysis** can bias estimates when missingness is informative.

**Ask authors:** Report the extent and pattern of missingness. Justify the handling method. Provide a sensitivity analysis under alternative missingness assumptions.

## Reporting issues

- p-values reported without effect sizes.
- p-values reported without CIs.
- Means without measures of variability (SD or SEM, *clearly labeled*).
- "Significant" without specifying α or method.
- Bar charts for distributions (use box plots, violin plots, or strip plots that show the distribution).
- Selective reporting of subgroups.
- Discrepancies between abstract, results text, figures, and tables.

## Bayesian-specific issues

- **Priors not justified.** "Uninformative" priors aren't always uninformative.
- **Prior sensitivity not assessed.** Reasonable priors should yield reasonable conclusions.
- **Bayes factors over-interpreted.** A BF of 3 is "moderate" evidence, not "definitive".
- **Posterior probabilities reported without prior probability context.**
- **Posterior predictive checks omitted.**

**Ask authors:** Justify priors. Provide prior sensitivity analysis. Show posterior predictive checks.

## Detecting p-hacking from reported values

Some heuristic checks that can flag suspicious reporting:

- **Last-digit distribution** of reported p-values. Excessive 0.04 and 0.05 may indicate rounding or hacking.
- **statcheck** (an R package) can check whether reported p-values are consistent with the reported test statistics and df. Mismatches are worth flagging.
- **GRIM test** (Granularity-Related Inconsistency of Means): for studies reporting means of integer-valued data, the mean must be a possible value for the given n. Many published means are arithmetically impossible.
- **SPRITE** (Sample Parameter Reconstruction via Iterative TEchniques) reconstructs plausible source data from summary statistics.

These tools are not gotchas — false positives occur. Use them as one piece of evidence, not as accusations.

## What to ask vs. what to demand

- **Reasonable to ask:** clarification, sensitivity analyses, additional reporting of existing data, correction of clear errors, softened conclusions.
- **Reasonable in some cases:** reanalysis with an appropriate method, additional control group from existing data.
- **Generally unreasonable:** demanding a second study, demanding orthogonal validation experiments outside the scope, demanding the authors collect a different dataset to answer your different research question.

Don't ask for what you wish they had done instead of what they did do, unless what they did do is fatally flawed.
