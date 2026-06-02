---
name: research-critique
description: Pre-submission SELF-critique — be your own Reviewer 2. Use to read your own draft as a hostile-but-fair referee at the target journal would, find the weaknesses before a real referee does, and decide whether the work is publishable. Produces a structured referee-style report (Summary, Major, Minor, Questions, Recommendation) on your own manuscript, after an author-side ethics/policy gate (integrity, authorship, data/code, figure integrity, plagiarism, AI disclosure, COI). Triggers on "critique my draft", "is this publishable", "what would a reviewer say", "find weaknesses before I submit", "be reviewer 2 for my paper". Field examples are atmospheric/climate (uncertainty quantification, forcing claims) and aerospace/AIAA (verification & validation, grid convergence) with light cross-field rigor rubrics — not generic or clinical-only checklists.
allowed-tools: Read Write Edit Bash
---

# Pre-Submission Self-Critique — Be Your Own Reviewer 2

## What this is for

Reading **your own draft** the way a hostile-but-fair referee at the target journal would, so you fix the problems before a real referee ever sees them. The output is a **structured referee report** on your own manuscript — Summary, Major comments, Minor comments, Questions, Recommendation — pointed at the failure modes that actually sink papers, not at generic boilerplate.

This is self-critique, not refereeing someone else's submission: there is no confidentiality or conflict-of-interest barrier to clear, because the work is yours. The discipline is to read it adversarially anyway — to anticipate every objection and close it now, while you still can.

Work out which family the paper belongs to first (it changes the bar):
- **Family A — atmospheric/climate:** the make-or-break issues are uncertainty quantification, forcing claims, and mandatory journal sections.
- **Family B — aerospace engineering (AIAA):** the make-or-break issues are verification, validation, and convergence.
- **Light cross-field layer:** if the work is biomedical, clinical, or ML-flavored, add the relevant reporting-standard and statistics rubric on top — kept deliberately light.

Load `references/vv_uncertainty_checklist.md` and `references/reviewer_objection_catalog.md` before you start; have `references/journal_guidelines.md` open for the venue's mandatory sections.

## How to self-review

0. **Run the author-side ethics/policy gate first** (`references/author_integrity.md`). Confirm *you* are compliant before critiquing the science: honest reporting (claims matched to evidence), authorship & contributorship (ICMJE/CRediT, no gift/ghost authors), data & code availability (DOIs/repositories, never "available upon request"), figure/image integrity (no improper manipulation, splicing, or duplication), plagiarism & self-plagiarism / text recycling, AI-use disclosure per the venue's policy, dual-use / biosecurity / export-control sensitivity, prior-publication & preprint/embargo policy, conflicts-of-interest & funding disclosure, and ethics approvals / consent where applicable. Fix or flag anything that fails here before going further.
1. **Identify the family** (A / B, and any light cross-field rubric). This sets which checklist and which bar applies.
2. **Read for the claim.** What, exactly, does the paper assert, and how strong is the claim (proven / estimated / suggested)? Write it in one sentence.
3. **Test claim-vs-evidence proportionality.** Is the confidence matched to the evidence? Over-claiming is the most common fatal flaw here — a forcing or performance benefit stated more precisely or more generally than the analysis supports.
4. **Run the family checklist line by line** — uncertainty for A, V&V for B (`references/vv_uncertainty_checklist.md`).
5. **Run the cross-cutting rigor scans** — statistics pitfalls (`references/statistical_pitfalls.md`), figure/image integrity (`references/figure_integrity.md`), citation hygiene and reproducibility (`references/common_issues.md`), section-by-section criteria (`references/section_checklists.md`), and reporting-standard compliance where relevant (`references/reporting_standards.md`).
6. **Check the mandatory journal furniture** (`references/journal_guidelines.md`): implications section for ACP; Open Research / Key Points / Plain Language Summary for AGU; Justification Statement for ERL; TOC graphic for RSC; Nomenclature + dual units + GCI for AIAA; data/code statements; the right citation family; word/figure budgets.
7. **Check the draft against the house voice** (`references/house_style.md`) — see below.
8. **Write the severity-ranked report** (template below; `assets/review_template.md` is the fuller scaffold).

## Family A — what to attack (atmospheric/climate)

The discipline lives on uncertainty; weak treatment of it reads as naïveté and invites rejection.

- **Over-claiming forcing/benefit** beyond the stated range, or stating a best estimate without its interval.
- **Missing or weak uncertainty quantification** — no ensemble/sensitivity design, sources not enumerated, the dominant source not named or ranked.
- **± used for an asymmetric distribution** — these ranges are almost never symmetric; bracket notation `X [lo, hi]` with the percentile is expected.
- **RF reported without ERF context** — no ERF/RF ratio stated, or treating RF as if it were the climate response.
- **Missing CO₂/non-CO₂ partition** when net aviation forcing is discussed; or a partition whose denominator is wrong.
- **Unexamined key assumptions** — humidity-field/ERA5 limitations, initial ice-crystal number (nvPM EIn), optical depth, the RF→ERF ratio — each a known leading uncertainty.
- **Units / significant figures** — W m⁻² where mW m⁻² is meant; 4+ sig figs implying false precision; CO₂-equivalents for contrails without a stated time horizon.
- **Reproducibility** — "available upon request" (banned at AGU); missing data/code DOIs.

## Family B — what to attack (AIAA)

A modeling or experimental paper that skips V&V is desk-rejected; the editorial policy is explicit.

- **No grid-independence study** — fewer than three meshes, or no GCI reported. The single most common AIAA desk-reject trigger.
- **Verification and validation conflated** — using "validated" for code correctness, or claiming agreement without distinguishing the two (AIAA G-077 terms).
- **"Agrees well" without numbers** — comparison error and uncertainty bands required.
- **Experimental uncertainty without a coverage factor** — "±2 %" with no "at 95 % confidence"; bias and precision not combined.
- **"Novel" without a cited gap** — the most over-scrutinized word in AIAA review; the contribution must be measurable and the gap cited.
- **Nomenclature/text symbol redundancy; "et al." in the reference list; abbreviated journal names; conclusions introducing new material; missing dual units.** (Full mistake list: `references/aiaa_engineering_style.md` §7.)

## Cross-cutting reasoning (both families)

Correlation treated as causation; overgeneralization beyond the sample/scenario; cherry-picked comparisons; ignoring a contradictory prior estimate without explanation; sign of an uncertain forcing asserted without justification. Distinguish what was *found* from what it *means*, and statistical from practical significance. For the deeper rigor catalog — p-hacking, HARKing, multiple testing, underpowering, figure/image integrity, citation verification — see `references/statistical_pitfalls.md`, `references/figure_integrity.md`, and `references/common_issues.md`.

## Story-structure failure modes (Schimel)

A paper can be rigorous and still get rejected because it doesn't *read* as a story — referees feel adrift and lose trust. Read the draft once for structure and attack these (the constructive version is in `research-writing` → `references/narrative_craft.md`):

- **No explicit Challenge.** The Introduction states objectives ("our objectives were…") instead of a **question** ("to learn X, we did Y"). If a reader can't say in one sentence what question drove the work, neither can a referee — flag it. The most common structural flaw.
- **Introduction is a literature review, not a gap.** It piles up what we *know* instead of framing the *hole*. Tell: sentences whose subjects are authors ("Smith (2003) found X") rather than nature ("X occurs (Smith 2003)"); "little is known about X"; selling a method before establishing the problem (the "bizzwidget" error).
- **Opening gives no direction or misdirection** — the first paragraph points somewhere the paper doesn't go, or rehearses textbook material. **Hourglass mismatch:** the opening promises broader than the resolution delivers (over-claiming) or narrower (under-selling).
- **Action is a data dump.** Results report significance without **effect sizes** ("significantly increased" with no magnitude); interpretation is tangled into the data; the pattern is buried under numbers.
- **Resolution killers** (endings are power positions — these waste them): *weak* (asserts importance without saying how), *distracting* (a truism or a brand-new idea never set up earlier), or *self-undermining* — the reflexive **"more research is needed."** Also flag a Resolution that **summarizes without synthesizing** or never closes back to the Opening.

### Limitations: "but, yes," not "yes, but"

How a draft handles its own weaknesses is itself a review target — and the easiest thing to fix:

- **Invert "yes, but" into "but, yes."** The default is to give the good results, then end on the caveat — which makes the caveat the take-home message. Instead, address the limitation **early**, constrain the conclusions to fit it, and **end on a "yes."** Flag any Discussion/abstract/Conclusions that ends on a caveat.
- **Keep limitations out of the power positions** — never in the opening or resolution of the Discussion/Conclusions. "You should never make a limitation *the* conclusion."
- **Re-scope the question before defending the method.** Many "limitations" are really a question–method mismatch; narrowing the claim to what the method actually supports often dissolves the objection (and a smaller filled gap beats none).
- **Pre-empt the obvious objection.** For every weakness a referee will obviously raise, disarm it at the earliest point it becomes relevant — "if you avoid mentioning the negatives, reviewers will find them anyway, and probably recommend rejection."
- **Calibration dial:** *too much confidence blinds you to the limitations; too much humility blinds you to the accomplishments.* Aim between — honest about the blemish, unapologetic about the contribution.

## Delivering the critique

Lead with genuine strengths (so you don't gut a real strength while fixing a weakness). Rank issues: **Critical** (threatens the main conclusion) / **Important** (affects interpretation) / **Minor**. Be specific — quote the sentence, point to the figure or line, and give a concrete fix, not just a complaint. Be proportionate and consistent. The aim is a paper that survives review, so frame everything as "here's what a referee will say, and here's how to close it now."

## Check voice against the house style

Beyond correctness, check that the draft *sounds like the group's work*: result-first first-person prose, headline numbers carrying their 95% CI with the uncertainty source named, an integration-gap framing with a "Here we …" pivot, "premature mortalities" not "deaths," and a grounded policy/implication close. Flag generic or passive phrasing that drifts from `references/house_style.md`, and confirm the mode (Nature-flagship vs engineering-systems) matches the target venue.

## Report template

```
SUMMARY              — 2–4 sentences: what the paper does, the headline claim, your honest overall assessment.
MAJOR COMMENTS       — numbered; each: the issue, why it matters, the fix. (Critical first.)
MINOR COMMENTS       — numbered; wording, units, figure, citation, formatting, mandatory-section furniture.
QUESTIONS            — points a referee will press on that you must be able to answer before submission.
RECOMMENDATION       — predicted referee verdict (accept / minor / major / reject-and-reframe), with the one change that most improves the odds.
```

Use `assets/review_template.md` for a fuller fillable scaffold (adds the ethics gate, strengths, family-checklist result, cross-cutting scan, journal furniture, and house-voice sections). Keep it consistent with this inline template.

## Grant drafts

Self-critiquing your own proposal works the same way, but the bar is feasibility, significance, and team capacity rather than demonstrated results. Use `references/grant_review.md` as the rubric a panel will apply to your draft (NIH / NSF / ERC / NHMRC / Wellcome / UKRI criteria, plus the common proposal pitfalls), and run the author-side gate (`references/author_integrity.md`) for AI-use disclosure, COI/funding, and data-management plans.

## References
- `references/author_integrity.md` — **author-side ethics/policy gate** (step 0): integrity, authorship, data/code, figure integrity, plagiarism, AI disclosure, dual-use, preprint/embargo, COI, ethics approvals.
- `references/vv_uncertainty_checklist.md` — Family A uncertainty-reporting checklist; Family B V&V checklist.
- `references/reviewer_objection_catalog.md` — common reviewer objections per family and how to preempt each.
- `references/journal_guidelines.md` — mandatory sections, figure specs, and data policies per journal.
- `references/house_style.md` — the group's house voice (check the draft against it).
- `references/atmospheric_climate_style.md` — Family A field-exemplar writing conventions.
- `references/aiaa_engineering_style.md` — Family B AIAA conventions; §7 is the AIAA mistake list.
- `references/statistical_pitfalls.md` — p-hacking, HARKing, multiple testing, power, causal language (cross-cutting; clinical/ML kept light).
- `references/figure_integrity.md` — figure/image manipulation, error bars, axes, colorblind accessibility.
- `references/common_issues.md` — citation verification, abstract–body drift, reproducibility, authorship, COI, salami slicing, AI-text signs.
- `references/section_checklists.md` — section-by-section self-review criteria (title/abstract → discussion → refs → supplements).
- `references/reporting_standards.md` — CONSORT / STROBE / PRISMA / ARRIVE / TRIPOD+AI etc. (light cross-field layer).
- `references/grant_review.md` — self-review of your own grant proposal against funder criteria.

## Assets
- `assets/review_template.md` — fuller fillable self-critique report scaffold (consistent with the inline template above).
