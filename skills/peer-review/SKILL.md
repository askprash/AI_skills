---
name: peer-review
description: Conduct rigorous peer review of scientific manuscripts, preprints, grant proposals, and referee reports. Use whenever the user asks to "review", "referee", "critique", or "evaluate" a paper, manuscript, submission, preprint, or grant — including phrasings like "write reviewer comments", "act as reviewer 2", "give me a referee report", "is this publishable", or "what would a reviewer say". Triggers on uploaded PDFs/DOCX of academic papers, arXiv/bioRxiv/medRxiv links, and grant drafts (NIH, NSF, ERC, NHMRC, Wellcome, etc.). Produces a structured review report with summary, major comments, minor comments, and questions for authors.
allowed-tools: Read, Write, Edit
license: MIT
---

# Peer Review

A systematic toolkit for refereeing scientific manuscripts and grant proposals. Produces constructive, rigorous, venue-appropriate reviews.

## Step 0 — Reviewer ethics gate (read first, every time)

Before reading the manuscript or producing any review content, confirm:

1. **Confidentiality and AI-use policy.** Most major publishers (Springer Nature, Elsevier, Wiley, NEJM, JAMA, ICML, NeurIPS, ICLR, CVPR) prohibit uploading confidential manuscripts to third-party LLMs, including ChatGPT/Claude/Gemini, because doing so breaches confidentiality. If the user is an invited reviewer, surface this constraint explicitly and ask them to confirm one of: (a) the venue permits AI assistance, (b) the manuscript is a public preprint, (c) the manuscript is their own and they want self-review, or (d) they want training/mock-review on a hypothetical. Do not proceed silently. See `references/reviewer_ethics.md`.
2. **Conflicts of interest.** Ask the user to confirm no undisclosed COI (co-authorship in last 3–5 years, same institution, collaboration, advisor/advisee, competing grants).
3. **Scope.** Confirm what the user wants: full review report, focused critique on one section, sanity check on stats, response to specific reviewer comments, or revision-letter drafting.

If any of these are unclear, ask before continuing. If the user is doing self-review or reviewing a public preprint, note that briefly and proceed.

## Step 1 — Triage: identify the manuscript type

Different manuscript types need different rubrics. Identify which apply (often more than one) before applying checklists:

| Type | Primary rubric | Reference file |
|------|----------------|----------------|
| Randomized clinical trial | CONSORT + preregistration check | `references/clinical_trial_specifics.md`, `references/reporting_standards.md` |
| Observational clinical study | STROBE | `references/reporting_standards.md` |
| Systematic review / meta-analysis | PRISMA, search-strategy critique | `references/reporting_standards.md` |
| Animal study | ARRIVE, 3Rs | `references/reporting_standards.md`, `references/reviewer_ethics.md` |
| Genomics / omics | MIAME, MINSEQE, data deposition | `references/reporting_standards.md` |
| ML / AI benchmark or method | Leakage, seeds, baselines, compute disclosure | `references/ml_paper_specifics.md` |
| Theory / mathematical | Proof correctness, novelty, scope of claims | (general only — see Step 2) |
| Methods / tool paper | Validation vs. existing methods, reproducibility | `references/common_issues.md` |
| Case report / short letter | Adapt expectations for brevity | `references/section_checklists.md` |
| Grant proposal | NIH / NSF / ERC criteria | `references/grant_review.md` |

For grants, jump directly to `references/grant_review.md` — the rest of this workflow is manuscript-oriented.

For venue-specific calibration (Nature/Science prestige bar vs. specialty journal vs. ML conference), defer to the `venue-templates` skill if available.

## Step 2 — Read the manuscript

Read the abstract and introduction first, then jump to the results and figures, then the methods, then the discussion. Reading methods after results lets you check whether the methods actually support what was claimed.

If the file is a PDF with figures and the agent host doesn't render PDF text reliably, convert to images for figure inspection — but use the host's native PDF reader for text first (do not rasterize unnecessarily; it wastes context).

Take working notes as you read. Don't generate review prose yet.

## Step 3 — Apply checklists by section

For each section, walk through the relevant checklist in `references/section_checklists.md`. Don't recite the checklist in the output; use it to surface real issues.

In parallel, scan for:

- **Statistical pitfalls** — see `references/statistical_pitfalls.md` (p-hacking, HARKing, multiple testing, baseline imbalance, garden of forking paths, post-hoc subgroup analyses presented as planned).
- **Figure and data integrity** — see `references/figure_integrity.md` (image duplication, splicing in blots, suspicious gel bands, inappropriate scale bars, error bars not defined, colorblind accessibility).
- **Citation hygiene** — see `references/common_issues.md` (verify a sample of citations actually exist and say what's claimed; in 2026 fabricated citations from AI-assisted writing are common).
- **Reproducibility** — code, data, materials, protocols, accession numbers. A claim of "data available upon request" is widely considered non-compliant by modern standards.
- **Reporting-standard compliance** — see `references/reporting_standards.md` for the relevant checklist (CONSORT, PRISMA, ARRIVE, STROBE, MIAME, MINSEQE, TRIPOD, SRQR, COREQ).

For ML papers specifically (or any paper with significant ML methodology), `references/ml_paper_specifics.md` covers data leakage, train/test contamination, benchmark cherry-picking, hyperparameter tuning on test set, missing seeds, missing error bars, undisclosed compute.

For clinical trials, `references/clinical_trial_specifics.md` covers preregistration drift, primary-endpoint switching, ITT vs. per-protocol, blinding, equipoise.

## Step 4 — Categorize and write

Sort findings into:

- **Critical** — the manuscript's central claims are not supported, or there are serious integrity concerns. These drive a "reject" or "major revisions" recommendation.
- **Major** — meaningful methodological or interpretive issues that authors must address but that don't invalidate the work.
- **Minor** — clarifications, missing citations, presentational issues, typos.
- **Questions** — items where you need the authors to clarify before judging.

Then fill in `assets/review_template.md`. Don't generate sections the template doesn't have; don't omit sections it does.

## Step 5 — Calibrate tone and recommendation

Before finalizing:

- **Constructive, not dismissive.** Frame every critical comment with what would fix it. "X is unsupported" is worse than "X is unsupported by the current data; either Y would establish it, or the claim should be softened to Z."
- **Balanced.** Lead the summary with what works before what doesn't. A review with no strengths section reads as hostile and is often discounted by editors.
- **Specific and located.** Every comment names a section, page, line, figure, or equation. "The statistics seem off" is unactionable.
- **Proportionate.** Don't demand a second study to address a third-order concern. Don't pad minor comments to look thorough.
- **Recommendation matches comments.** "Major revisions" with no critical issues, or "accept" with three critical issues, is incoherent and editors will notice.

For recommendation language, use the venue's exact terms if known (Nature uses different language than IEEE; some venues use "accept/reject" only).

## Step 6 — Final pass

Verify against the checklist in `assets/review_template.md` before delivering. Specifically check:

- Citations you cited (e.g., "this conflicts with Smith 2023") actually exist and say what you claim.
- Statistical critiques are technically correct (don't accuse authors of p-hacking based on a misreading of their multiple-comparison correction).
- No identifying information about yourself slipped in if the review is double-blind.
- The review reads at the appropriate length for the manuscript (a 4-page letter doesn't need a 6-page review).

## Output

Final deliverable: a filled-in `assets/review_template.md`, saved to the output directory. If the user asked for a different format (free-form prose, journal portal fields, an editor's letter), adapt — but use the template as the working scaffold.

## Reference files

- `references/reviewer_ethics.md` — Confidentiality, COI, COPE guidelines, publisher AI-use policies (read first if unsure whether to proceed)
- `references/section_checklists.md` — Section-by-section evaluation criteria for abstract, intro, methods, results, discussion, references
- `references/statistical_pitfalls.md` — p-hacking, HARKing, multiple testing, common stats issues
- `references/figure_integrity.md` — Image manipulation, blot/gel inspection, microscopy, accessibility
- `references/ml_paper_specifics.md` — Leakage, benchmarks, seeds, compute, evaluation rigor for ML papers
- `references/clinical_trial_specifics.md` — Preregistration, endpoint switching, CONSORT, ITT
- `references/reporting_standards.md` — CONSORT, PRISMA, ARRIVE, STROBE, MIAME and friends
- `references/common_issues.md` — General methodology pitfalls and citation verification
- `references/grant_review.md` — NIH, NSF, ERC, NHMRC, Wellcome review frameworks
- `assets/review_template.md` — Fillable review report template
