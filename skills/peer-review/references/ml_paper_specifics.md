# Reviewing ML and AI Papers

ML/AI peer review has its own failure modes. This reference complements `statistical_pitfalls.md` and `section_checklists.md` with issues specific to machine learning, statistical learning, and AI papers.

## Table of contents

1. [Data leakage](#data-leakage)
2. [Benchmark and baseline rigor](#benchmark-and-baseline-rigor)
3. [Hyperparameter tuning on the test set](#hyperparameter-tuning-on-the-test-set)
4. [Seeds, variance, and significance](#seeds-variance-and-significance)
5. [Compute and resource disclosure](#compute-and-resource-disclosure)
6. [Train/test/contamination for LLMs and foundation models](#traintestcontamination-for-llms-and-foundation-models)
7. [Generalization claims](#generalization-claims)
8. [Reproducibility (code, weights, prompts)](#reproducibility-code-weights-prompts)
9. [Human evaluation](#human-evaluation)
10. [Ethics, dual use, and broader-impact statements](#ethics-dual-use-and-broader-impact-statements)
11. [Theoretical claims](#theoretical-claims)
12. [Application papers (e.g., ML for biology, ML for medicine)](#application-papers)

---

## Data leakage

The most common substantive problem in ML papers. Leakage = test set influences training, directly or indirectly.

**Types:**

- **Direct leakage**: test examples appear in training data (often through deduplication failures).
- **Feature leakage**: features computed using future information, target information, or test-set statistics. E.g., normalizing by mean/std computed on the full dataset including test.
- **Group leakage**: samples from the same patient / user / source split across train and test. Models learn the source, not the label.
- **Temporal leakage**: training on future data to predict past data. Common in financial and clinical time-series.
- **Selection leakage**: the train/test split is itself informative (e.g., one site's data is the test set and differs systematically).

**Detection cues:**

- Suspiciously high performance, especially on small or hard datasets.
- No discussion of how train/test were split.
- "Random split" without checking group / temporal independence.
- Normalization or feature engineering done before the split is described.
- The paper's eval framework reads more like cross-validation than held-out testing.

**Ask:**
- Describe the split (group-based? temporal? subject-level?).
- Was any preprocessing (normalization, feature scaling, vocabulary construction) fit on the test set?
- Run a sanity check: can a trivial baseline predict the label from non-target features?

## Benchmark and baseline rigor

Many ML papers compare a new method to weak baselines or report on cherry-picked benchmarks.

**What to check:**

- **Baselines are tuned**: Are baseline methods tuned with the same compute / hyperparameter search as the proposed method? Untuned defaults vs. tuned proposed method is not a fair comparison.
- **Baselines are state of the art**: Or at least, the strongest reasonable comparison. Comparing to a 2018 method when 2024 methods exist is a flag.
- **Benchmark suite is appropriate**: Is the benchmark suite the field-standard one (e.g., GLUE/SuperGLUE for NLU; ImageNet/CIFAR for vision; MTEB for embeddings; HELM/MMLU/BIG-bench for LLMs)?
- **No cherry-picked benchmarks**: A long benchmark suite from which only winning results are shown is suspect.
- **Statistical significance**: Are differences between methods tested? Many "improvements" are within noise.

**Ask:**
- Tune baselines with the same compute budget.
- Report results across the full benchmark suite, not just the wins.
- Include error bars / confidence intervals.

## Hyperparameter tuning on the test set

If hyperparameters are selected by performance on the test set, the test set has effectively been used for training. Validation sets exist for this reason.

**Detection cues:**

- "We selected the best learning rate from {1e-4, 1e-3, 1e-2}" with results on a held-out test set.
- No validation set described.
- The paper sweeps hyperparameters and reports the best result on the test set as final performance.

**Ask:**
- Use a validation set for tuning. Report final results on a held-out test set used only once.
- If the test set is small and reusable, use cross-validation properly (nested CV for tuning + evaluation).

## Seeds, variance, and significance

A single training run isn't a result. Different seeds give different results, sometimes by margins larger than the claimed improvement.

**What to check:**

- **Multiple seeds**: 3 minimum, 5+ preferred. Mean and standard deviation (or CI) reported.
- **Variance acknowledged**: Are differences between methods larger than the within-method variance?
- **Statistical tests**: For ML benchmarks, paired tests (e.g., paired t-test, Wilcoxon signed-rank) across seeds are appropriate when comparing methods.
- **Compute-controlled comparisons**: Many "improvements" go away when methods are matched on compute.

**Ask:**
- Report results across at least 3 seeds. Provide std dev and a test of significance.
- Match baselines on compute (training time, parameter count, dataset size).

## Compute and resource disclosure

Many strong ML results require resources most groups can't replicate. Disclosure matters for fairness and for understanding what was actually demonstrated.

**Should be reported:**

- Hardware (GPU/TPU type and count).
- Training time (wall-clock and accelerator-hours).
- Model size (parameters).
- Dataset size and source.
- Inference cost.
- Total compute for the project including failed runs and hyperparameter searches (the "ML reproducibility checklist" style disclosure).

**Why:** Two methods with similar performance but very different compute have different practical implications. Hidden compute disparity is a common reason a "new SOTA" doesn't replicate.

## Train/test contamination for LLMs and foundation models

Modern foundation models are trained on huge web corpora, including most public benchmarks. A model "solving" a benchmark may have memorized it.

**Detection / ask:**

- Has the model been tested for contamination on the benchmark? (Verbatim n-gram matching, paraphrase detection, "canary" probing.)
- Are evaluation prompts new (held-out, generated post-training cutoff)?
- For LLM evaluation, prefer benchmarks released after the model's training cutoff, or use private / unreleased eval sets.
- Public benchmarks like MMLU, HumanEval, GSM8K are partially contaminated for most major LLMs. Treat results on these as a floor, not a ceiling.

## Generalization claims

A model that works on benchmark X doesn't necessarily work on real-world deployment.

**Watch for:**

- Claims of generalization based on a single distribution.
- Out-of-distribution (OOD) evaluation absent or weak.
- "Robustness" claims based on artificially perturbed inputs, not naturally distributed shift.
- For medical / clinical ML: validation on data from a single site or single scanner.

**Ask:**
- OOD evaluation on a held-out distribution shift (different hospital, different photo source, different time period).
- Failure analysis: where does the model fail, and why?
- For deployment-oriented claims, evaluation in the deployment setting, not the lab setting.

## Reproducibility (code, weights, prompts)

The ML community has converged on stronger reproducibility norms than most of science. Reviewers should hold papers to those norms.

**Should be available:**

- **Code**: For methods papers, the implementation. Public GitHub, with a license. Reasonable documentation.
- **Trained weights**: Where releasing weights is feasible (most academic settings), the trained model.
- **Prompts**: For LLM papers, the exact prompts used in evaluation, in a format that allows exact replication (whitespace, formatting, system prompts).
- **Data**: Where licensable, the dataset. Where not, a description detailed enough to reconstruct the eval.
- **Environment**: Requirements file, container, or environment.yml.
- **Seeds**: Random seeds used in reported results.

**"Available upon request"** is generally insufficient. Major venues (NeurIPS, ICML, ICLR) increasingly require code submission with the paper.

## Human evaluation

When human judgments are used to evaluate ML output (LLM responses, generated images, etc.):

- **Number of raters**: Single rater is usually too few. Aim for 3+ per item.
- **Inter-rater agreement**: Reported (Cohen's κ, Krippendorff's α, etc.). Without agreement metrics, the eval is uninformative.
- **Rater training and rubric**: Was there a rubric? Were raters trained? Calibration items?
- **Blinding**: Were raters blinded to which model produced which output? Otherwise rater preference for "my team's method" can swing results.
- **Compensation and demographics**: Reported, with attention to whether the rater pool matches the intended user population.
- **Sample size**: How many items rated, and is the comparison powered?

## Ethics, dual use, and broader-impact statements

For ML papers with potential societal impact (generative models, surveillance, medical, security):

- Is there a broader-impact / ethics / responsible-disclosure section?
- Are dual-use concerns (the model can be misused) addressed?
- For datasets, are there datasheet / data-statement disclosures, especially for human-derived data?
- For models trained on web data, are licensing and consent addressed?

**Reviewer note:** Don't reflexively demand broader-impact statements where the venue doesn't require them. Do flag when a paper plausibly enables harm without any acknowledgment.

## Theoretical claims

For papers with theoretical analysis (bounds, convergence proofs, identifiability claims):

- Are assumptions realistic, or are they assumptions that make the proof go through but rarely hold in practice?
- Does the theorem actually apply to the proposed method, or does it apply to a simplified version?
- Are constants and orders specified, not hidden under big-O?
- Is the gap between theory and the empirical setting acknowledged?

A common failure mode: theorems about a simplified model presented as if they justify the empirical method. Ask explicitly.

## Application papers

For ML applied to biology, medicine, climate, social science, etc.:

- **Domain validity**: Does the model respect domain-specific constraints (e.g., physical laws, biological priors)?
- **Domain baseline**: Is the comparison to the field's actual state-of-the-art, not to weak baselines you happen to know?
- **Data quality**: Are the application-domain quality controls applied (e.g., for clinical data: ICD code accuracy, missingness patterns, site effects)?
- **Clinical / scientific relevance**: Is the metric of optimization actually what the field cares about? (AUC may be optimized; clinical net benefit may be what matters.)
- **External validation**: Was the method validated on data the developers didn't have access to during method development?

For clinical ML specifically, see also `clinical_trial_specifics.md` — many of those concerns (preregistration, primary endpoints, ITT) apply.

## Common requests in ML reviews

- More seeds, std devs, statistical tests.
- Tuned baselines or stronger baselines.
- Compute disclosure.
- Released code / weights / prompts.
- OOD evaluation.
- Ablation studies that isolate the contribution.
- Failure analysis.
- Specific evidence for generalization claims.

## What's usually unreasonable

- Demanding entirely new experiments outside the paper's scope.
- Insisting on a specific baseline that's tangential to the paper's claim.
- Requiring released weights for models that genuinely can't be released (proprietary training data, etc.) — though authors should acknowledge this clearly.
