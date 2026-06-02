# Common Issues

A catch-all reference for issues that don't fit cleanly into the discipline-specific files. Use alongside `statistical_pitfalls.md`, `figure_integrity.md`, `ml_paper_specifics.md`, and `clinical_trial_specifics.md`.

## Table of contents

1. [Citation verification](#citation-verification)
2. [Methods-results-discussion alignment](#methods-results-discussion-alignment)
3. [Scope drift between abstract and body](#scope-drift-between-abstract-and-body)
4. [Conclusions exceeding evidence](#conclusions-exceeding-evidence)
5. [Reproducibility concerns](#reproducibility-concerns)
6. [Authorship and contribution issues](#authorship-and-contribution-issues)
7. [Data and code availability](#data-and-code-availability)
8. [Conflicts of interest](#conflicts-of-interest)
9. [Salami slicing and duplicate publication](#salami-slicing-and-duplicate-publication)
10. [AI-generated text and citations](#ai-generated-text-and-citations)
11. [Methods papers and software](#methods-papers-and-software)
12. [Translation and language quality](#translation-and-language-quality)
13. [The "what would the editor want to know" filter](#the-what-would-the-editor-want-to-know-filter)

---

## Citation verification

In 2025–2026, fabricated or wrong citations are a frequent issue, partly due to AI-assisted writing. A reviewer should verify a sample.

**How to verify:**

1. Pick 5–10 citations, weighted toward:
   - Load-bearing claims in the introduction or discussion.
   - Surprising claims ("X has been shown to cause Y").
   - Citations to obscure or very recent papers.
   - Citations where the author–year combination feels off.
2. For each, search Google Scholar, PubMed, or the publisher's site.
3. Confirm: (a) the paper exists, (b) authors and year are correct, (c) it actually supports the cited claim.
4. If you can't find a citation, flag it. Sometimes it's a typo; sometimes it's fabricated.

**Red flags:**

- Author names that don't match (e.g., "Smith J. & Jones A., 2023" but the actual paper is "Smith J. & Patel R., 2023").
- Years that don't match.
- Journal names that don't exist or are misspelled.
- Citation to a different paper than the one that actually supports the claim.
- "Citation rot": the cited paper exists but says the opposite of what's claimed.

**What to write in the review:**

If you find a fabricated or wrong citation, list it specifically: "Reference 17 (Smith & Patel, 2023, J. Mol. Biol.) does not appear to exist in PubMed or Google Scholar; please verify."

## Methods-results-discussion alignment

A common failure mode: the methods describe one study, the results report a different one, and the discussion talks about a third.

**Check:**

- Every method described has a corresponding result.
- Every result has a method that produced it.
- Every claim in the discussion has a result that supports it.
- No "surprise" methods appear in the results that weren't pre-specified in methods.
- Sample sizes in methods match sample sizes in results.

This is best done by reading methods after results.

## Scope drift between abstract and body

The abstract is what gets indexed, cited, and read most. Mismatches:

- Effect sizes in abstract larger than in main results.
- Conclusions in abstract more definitive than in discussion.
- Sample size or population described differently.
- Statistical significance claimed in abstract for results that are borderline or non-significant in the body.

This is a serious issue when the abstract overstates because the abstract is what propagates.

## Conclusions exceeding evidence

Watch for:

- Causal language for associational data.
- Generalization beyond the studied population.
- Mechanistic claims without mechanistic evidence.
- Clinical / practical implications from preclinical or basic-science findings.
- "Translational" claims that depend on assumptions not tested.
- "This suggests" used to launder speculation as data-supported.

The fix is usually softening language, not removing claims entirely.

## Reproducibility concerns

Beyond what's covered in discipline-specific files:

- **Materials**: Unique reagents (antibodies, cell lines, plasmids, mouse strains) should be cited with RRIDs or with clear deposit identifiers (Addgene, ATCC, JAX). "Available from the corresponding author upon request" is no longer sufficient at most venues.
- **Cell line authentication**: Has the cell line been authenticated (STR profiling)? Mycoplasma testing reported?
- **Antibody validation**: Knockout/knockdown controls? Single-band reactivity at expected MW?
- **Protocol availability**: Detailed protocols deposited (protocols.io) where appropriate.
- **Equipment-specific dependencies**: Are results dependent on specific equipment (rare instrument, particular software version) and is this acknowledged?

## Authorship and contribution issues

- **CRediT taxonomy**: Increasingly required by journals. Authors specify which of 14 contribution roles each performed.
- **Ghost authorship**: Someone who contributed substantially is not listed.
- **Gift authorship**: Someone listed who didn't contribute substantially. Common red flag: a senior figure on every paper from a lab regardless of actual involvement.
- **Disputes**: If the author list seems implausible or the contribution statements seem off, flag to editor (confidentially), not in public review.

## Data and code availability

The standard is moving toward "available without restrictions" for most data and code. Specifically:

- **Genomic and other omics data**: Deposited in standard public repositories with accession numbers reported in the paper.
- **Clinical data**: De-identified data shared via approved platforms (e.g., dbGaP, EGA with controlled access, or institutional data warehouses); the data-availability statement should specify the access route.
- **Code**: Public repository (GitHub, GitLab, Zenodo for archived versions) with a license and reasonable documentation. "Code available upon request" is generally insufficient.
- **Restricted data**: Sometimes restrictions are legitimate (patient privacy, embargoed). The data-availability statement should explain.
- **Datasheet / model card**: For datasets and trained models, increasingly expected.

If a paper claims data/code is available but the link is dead, private, or empty, flag it. (Quick check: click the link.)

## Conflicts of interest

- All authors disclose financial COI and non-financial COI (advocacy, personal relationships) in the manuscript.
- Funding sources disclosed.
- Role of funders in design, conduct, analysis, reporting disclosed.
- For industry-sponsored research: independent statistician? Sponsor access to raw data? Sponsor sign-off on submission?

Reviewer's role: read these statements; if they seem missing or incomplete, ask. Don't accuse based on suspicion alone.

## Salami slicing and duplicate publication

- **Salami slicing**: A single study split into multiple papers, each with overlapping data and minimal independent contribution. Sometimes appropriate (large studies with different research questions can yield multiple papers); often not.
- **Duplicate publication**: Substantively the same paper submitted to multiple venues or republished.
- **Self-plagiarism**: Text reused from authors' own prior work without citation.

Indicators: cite-yourself patterns to other recent papers from the same group, overlapping author lists with mostly the same data, descriptions of the same experiments.

What to do: flag to editor confidentially, not in public review.

## AI-generated text and citations

A 2025–2026 reality: many manuscripts now have AI-assisted writing. Some venues require disclosure; others prohibit certain uses.

**Reviewer-visible signs of unrevised AI text:**

- Repetitive sentence structure ("It is important to note that...", "Furthermore, it should be emphasized...").
- Vague, generic statements where domain specificity would be expected.
- "Smooth" prose with little technical content.
- Disclaimers or hedging that doesn't fit the venue ("As an AI language model...").
- Fabricated citations (see Citation Verification above).
- Inconsistent technical depth across sections.
- Lists of similar items in suspiciously parallel form.

**What to do:**

- Don't accuse authors of "using AI" based on style alone — many humans write that way.
- Do flag specific concerns: unverifiable citations, generic statements where specificity is needed, technical inconsistencies.
- If the venue requires AI-use disclosure and none is given, the editor can ask.

**Reviewer's own AI use**: see `reviewer_ethics.md` — most venues prohibit uploading manuscripts to AI for review purposes.

## Methods papers and software

For papers introducing new methods or software:

- **Comparison fair**: Existing methods compared with appropriate effort (tuned, current versions, appropriate datasets).
- **Failure modes characterized**: A method's limitations should be described, not just successes.
- **Software actually works**: If a tool is described, can a user install and run it from the supplied instructions? (You can spot-check this if time permits.)
- **Documentation**: Reasonable for the audience.
- **License**: Stated and appropriate.
- **Maintenance plan**: For software intended for community use, who maintains it?

## Translation and language quality

For manuscripts from authors writing in a non-native language:

- **Don't penalize for non-native English quality** beyond what's needed for clarity. A separate copyedit pass at the journal handles polishing.
- **Do flag** specific passages where the meaning is unclear, ambiguous, or potentially wrong.
- **Don't suggest a "native English speaker" should be involved** — phrase it as "professional editing may help clarify specific passages, e.g., [page X, line Y]."
- Recognize that some clarity issues are conceptual, not linguistic; don't dismiss real issues as "language."

## The "what would the editor want to know" filter

Before submitting the review, ask:

- Does the editor have what they need to decide?
- Are the major issues prioritized so the editor sees them?
- Is the recommendation justified by the comments?
- If you'd reject, do the comments make it clear why?
- If you'd accept, are the minor issues genuinely minor?

Editors read many reviews. Be specific, be calibrated, and don't bury the main point under minutiae.

## A note on tone

The cumulative effect of many specific comments shouldn't be more dismissive than any individual comment is. Re-read the review as a whole; if it reads as hostile, soften connecting language without softening substantive critique.
