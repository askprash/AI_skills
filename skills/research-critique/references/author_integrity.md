# Author Integrity & Policy Gate (pre-submission)

Run this **before** the technical critique. It checks that *you*, the author, are compliant with research-integrity and venue policy — so a problem surfaces here, on your own desk, rather than from an editor, a referee, or a post-publication investigation. Self-critique of your own draft raises no confidentiality issue; the work is yours. The job here is honest reporting and policy compliance, not defending against others.

Treat each item as a question to answer about your own manuscript. Where the answer is "no" or "unsure," fix it or flag it before submission.

## Research integrity & honest reporting

The foundation: the paper says what the data actually support, and nothing more.

- No fabrication (inventing data) or falsification (altering data, selectively trimming, manipulating results).
- Every headline claim is matched to the evidence — no over-statement of effect size, generality, or certainty (the most common honest failure; see the proportionality test in `SKILL.md`).
- All analyses that were run are accounted for; you are not silently reporting only the run that "worked" (see p-hacking / the garden of forking paths in `statistical_pitfalls.md`).
- Negative and null results from pre-specified analyses are reported, not dropped.
- Outliers, exclusions, and analytic choices are disclosed and justified, not made to fit the desired result.
- The abstract does not claim more than the body delivers (a frequent self-inflicted wound — see `common_issues.md`).

## Authorship & contributorship

Get the author list and contribution statements right before submission, not after a dispute.

- **Authorship criteria met** (ICMJE, where the venue uses it): substantial contribution to conception/design or analysis/interpretation; drafting or critical revision; final approval; accountability. Everyone listed meets the bar; everyone who meets the bar is listed.
- **No gift/guest authorship** — no senior name added purely for status or by lab convention without a real contribution.
- **No ghost authorship** — no substantial contributor (including paid medical writers, or a key student) omitted.
- **CRediT taxonomy** completed if the venue requires it (14 contribution roles; AGU and many others mandate it).
- **Corresponding author and ORCIDs** set; author order agreed by all parties in writing.
- **Acknowledgments** cover non-author contributors (technical help, facilities, advice) and they have consented to being named.

## Data & code availability

The standard has moved to "available without restriction." Prepare deposits before, not after, acceptance.

- Data deposited in an appropriate repository with a **DOI or accession number cited in the paper** (Zenodo, PANGAEA, GEO, etc.), not "available from the authors upon request" — explicitly **banned at AGU** and discouraged everywhere.
- Code in a public repository (GitHub/GitLab) with a **license and an archived, versioned snapshot** (Zenodo DOI); the link is live, public, and non-empty (click it).
- A proper **Data Availability** and (separately, where required, e.g. EGU) **Code/Model Availability** statement is present.
- Legitimate restrictions (privacy, embargo, export control) are stated and explained, with the access route specified.
- Unique materials cited with stable identifiers (RRIDs, repository IDs) where applicable.

## Figure & image integrity

Figures are primary data. Treat any image adjustment as something you must be able to defend.

- No improper manipulation: brightness/contrast applied **linearly and to the whole image**, never to selected regions.
- No undisclosed **splicing** of lanes/panels; no **duplication** or reuse of an image (or a region of one) to stand for a different experiment, condition, or paper.
- No cloning, erasing, or compositing of features; no rubber-stamped backgrounds.
- The same control/background image is not silently reused across "independent" panels.
- Axes honest (no misleading truncation), error bars defined, distributions shown rather than hidden behind bare bars. See `figure_integrity.md` for the full self-check.
- Keep the unprocessed originals — if asked, you can produce them.

## Plagiarism & self-plagiarism / text recycling

Both copying others and recycling yourself are problems.

- No text, figures, or ideas taken from others without attribution and quotation where verbatim.
- No **self-plagiarism / text recycling**: substantial passages reused from your own prior papers without citation and clear demarcation (Methods boilerplate has some tolerance; check the venue).
- No **salami slicing**: a single study sliced into multiple thin papers with overlapping data and minimal independent contribution.
- No **duplicate/redundant submission**: the same work is not under review elsewhere.
- Run a similarity check (e.g. iThenticate/Turnitin) if available, and resolve flagged overlaps before submission.

## AI-use disclosure (per venue policy)

Using AI to help write or analyze is increasingly permitted *with disclosure*, but the rules vary and are tightening.

- Check the **target venue's current author AI-use policy** — many require a disclosure statement describing what AI tools were used and how (e.g. drafting, editing, code, figures).
- **AI is generally not allowed to be listed as an author** (it cannot take accountability) — most publishers state this explicitly.
- **You remain fully responsible** for all content, including any AI-assisted text, analysis, or citations.
- **Verify every AI-touched citation** — fabricated or wrong references are a well-known failure mode (see `common_issues.md`); confirm each cited work exists and supports the claim.
- Disclose AI use in images/figures where the venue requires it.

## Dual-use, biosecurity, export control

Some results carry sensitivity beyond the science.

- Consider whether the work is **dual-use research of concern** (could be repurposed to cause harm — pathogens, toxins, certain cyber/AI capabilities) and whether institutional dual-use review applies.
- Consider **biosecurity** review for gain-of-function or select-agent-adjacent work.
- Consider **export-control** sensitivity (ITAR/EAR for some aerospace, propulsion, and defense-adjacent topics) — confirm what can be published; acknowledge redactions (e.g. proprietary or export-controlled engine/component maps) explicitly rather than fudging.
- If any apply, confirm institutional clearance before submission.

## Prior publication, preprints & embargoes

Make sure nothing about prior dissemination conflicts with the venue.

- Confirm the venue's **preprint policy** — most allow preprints (arXiv, bioRxiv, ESSOAr/Earth ArXiv), some have conditions; EGU/ACP **posts your submission publicly as a discussion paper with its own DOI**, so there is no embargo option there.
- Disclose any **prior publication** of part of the work (conference paper, thesis, workshop) and confirm the venue permits the overlap and that you have rights to reuse it.
- Respect any **embargo** (press, funder, or partner) on the findings.
- Confirm you hold the rights to any reproduced figures/tables (permissions obtained where needed).

## Conflicts of interest & funding disclosure

Disclose, don't conceal — the test is what a reasonable reader would want to know.

- Declare all **financial COI**: funding, equity, consulting, patents/licensing, paid advisory roles, competing commercial interests.
- Declare **non-financial COI**: advocacy roles, personal relationships, or affiliations that could be seen to bias the work.
- State **all funding sources** with grant numbers, and the **role of the funder** in design, conduct, analysis, and the decision to publish.
- For industry-sponsored work, address data access and independence of analysis where relevant.

## Ethics approvals & consent (where applicable)

Mostly a cross-cutting / biomedical concern, but check it whenever human or animal data are involved.

- **IRB/ethics-committee approval** for human-subjects research, with the approval/protocol number stated.
- **Informed consent** obtained and documented; consent for publication of identifying material (especially images) where relevant.
- **IACUC / animal-ethics approval** for animal work, with the number, and ARRIVE-compliant reporting (see `reporting_standards.md`).
- Relevant permits for field/environmental sampling, protected sites, or restricted materials.

---

## Quick pre-submission integrity checklist

- [ ] Claims matched to evidence; no over-statement; abstract consistent with body.
- [ ] Authorship meets ICMJE; no gift/ghost authors; CRediT done if required; order agreed.
- [ ] Data + code deposited with DOIs/accessions; statements present; links live; no "upon request."
- [ ] Figures defensible: linear whole-image adjustments only; no undisclosed splicing/duplication; originals retained.
- [ ] No plagiarism/self-plagiarism, salami slicing, or duplicate submission; similarity check clear.
- [ ] AI use disclosed per venue policy; AI not an author; AI-assisted citations verified.
- [ ] Dual-use / biosecurity / export-control sensitivity considered and cleared.
- [ ] Preprint/prior-publication/embargo policy satisfied; reuse permissions obtained.
- [ ] COI and funding (with roles) fully disclosed.
- [ ] Ethics approvals and consent in place and stated (where human/animal data apply).
