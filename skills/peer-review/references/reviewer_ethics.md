# Reviewer Ethics

Read this **before** producing any review content. The peer review process depends on confidentiality, fairness, and disclosure. Breaching these damages individual authors, the literature, and trust in the system.

## Confidentiality

A manuscript under review is a confidential document. Treat every sentence, figure, dataset, and supplementary file as private until the work is published.

**What confidentiality means in practice:**

- Do not share the manuscript with anyone not formally invited as a co-reviewer by the editor.
- Do not discuss specific contents with colleagues, on social media, in lab meetings, at conferences, or in chats.
- Do not use unpublished ideas, data, or methods from the manuscript in your own work.
- Do not retain copies after submitting the review (most publishers ask reviewers to destroy them).
- Do not delegate the review to a student or junior colleague without informing the editor and obtaining permission.

## AI-use policies (publisher and venue list)

As of 2025–2026, most major scientific publishers and conferences treat uploading a confidential manuscript to a general-purpose LLM (ChatGPT, Claude, Gemini, etc.) as a breach of confidentiality. Their reasoning: the manuscript leaves the reviewer's control, the LLM provider may log or train on the content, and the authors did not consent to that exposure.

**Publishers and venues that prohibit or restrict reviewer LLM use (representative list — confirm the current policy at the specific journal):**

- **Springer Nature** — prohibits uploading manuscripts or substantial portions to generative AI tools.
- **Elsevier** — same; reviewers may not use generative AI in any part of the peer-review process that would breach confidentiality.
- **Wiley** — confidentiality obligations preclude uploading to AI tools.
- **NEJM, JAMA, Lancet** — strict confidentiality; no AI assistance with the manuscript content.
- **NIH** (for grant review) — prohibits use of generative AI tools in peer review of grant applications.
- **NSF** — has issued similar guidance for merit review.
- **NeurIPS, ICML, ICLR, CVPR, ACL, EMNLP** — most have explicit policies against uploading submissions to LLMs; check the year's reviewer instructions.

**What is generally permitted (verify per venue):**

- Using LLMs for *language polish of your own review text*, after you've drafted the content yourself, without ever showing the LLM the manuscript.
- Using LLMs for general background on a methodology you're unfamiliar with, without referencing the manuscript content.
- Reviewing publicly available preprints (the confidentiality argument is weaker, but the venue may still have a policy).

**What to do if the user wants AI assistance on a manuscript under formal review:**

Surface this constraint explicitly. Offer to:
1. Help them check the specific venue's policy.
2. Discuss methodology in the abstract (e.g., "what are common pitfalls in propensity-score matching") without referencing manuscript content.
3. Polish review text they've drafted, with the manuscript content kept out.
4. Proceed only if they confirm the venue permits AI assistance or that the manuscript is public (preprint, their own work, etc.).

## Conflicts of interest

Before agreeing to review, confirm none of the following apply:

- Co-authorship with any author in the last 3–5 years (varies by venue).
- Current or recent collaboration, including unpublished work.
- Advisor–advisee relationship (current or recent, varies — typically last 5–10 years).
- Same institution or department.
- Personal relationship (family, close friend, romantic).
- Competing or directly overlapping research project, especially one nearing publication.
- Financial COI: equity, consulting, licensing, or competing commercial interest.
- Recent dispute or rivalry that would impair objectivity.

When in doubt, disclose to the editor and let them decide.

## COPE Ethical Guidelines for Peer Reviewers

The Committee on Publication Ethics (COPE) publishes guidelines that are the de facto standard. Key points:

- **Conduct review only if you have the expertise.** Decline if outside your area or refer to a colleague with editor approval.
- **Be timely.** If you can't meet the deadline, tell the editor early.
- **Be objective and constructive.** Critique the science, not the scientists.
- **Don't use the privileged access for personal gain.** No scooping, no using unpublished methods, no sharing.
- **Disclose to the editor.** Suspected misconduct, redundant publication, plagiarism, fabrication, image manipulation, or undisclosed COI should be raised privately with the editor, not in the review text.
- **Maintain confidentiality even after the review.** Don't reveal that you reviewed a particular manuscript, the outcome, or other reviewers' comments.
- **Don't contact authors directly.** All communication goes through the editor.

Full text: https://publicationethics.org/peerreviewer

## Reviewing as the author's own self-review or critique of public preprints

These cases relax confidentiality but not rigor:

- **Self-review** (the user is reviewing their own draft): no confidentiality issue. Proceed fully.
- **Public preprint** (arXiv, bioRxiv, medRxiv, SSRN, ChemRxiv): the preprint is public, so uploading to an AI tool doesn't breach confidentiality. The authors may still have submitted a (different, confidential) version to a journal; comments on the preprint are fine.
- **Mock review for training**: stage the work as hypothetical or use a published paper.

## Handling suspected misconduct

If during review you suspect fabrication, falsification, plagiarism, image manipulation, or undisclosed COI:

- **Do not accuse in the public review text.** This protects authors from baseless accusations and protects you from defamation exposure.
- **Raise it privately with the editor** in the confidential comments-to-editor field, citing specific evidence (e.g., "Figure 3B panels appear to share features with Figure 1A; an image-forensics check is warranted").
- **Let the editor handle the investigation.** They have institutional and COPE pathways for this.

## Reviewing for predatory journals

If asked to review for a journal whose practices are concerning (no editorial board listed, vague scope, suspiciously fast turnaround, fees not disclosed up front), check resources like Cabells Predatory Reports or Beall's archived list. Declining to review for predatory venues is appropriate.

## Reviewing manuscripts on contested topics

For manuscripts on socially or politically contested topics (e.g., gender medicine, racial differences, climate policy, pandemic policy, dual-use research):

- Apply the same methodological standards as for any other paper.
- Separate empirical questions ("does this design support this inference") from normative ones ("is this question worth asking").
- Don't use the review to litigate the broader debate.
- If you have a strong prior, disclose to the editor and let them decide whether to use your review.

## The reviewer's identity

- **Single-blind** (default at most journals): authors don't see reviewers; reviewers see authors.
- **Double-blind** (common in CS conferences, some journals): neither sees the other. Don't put identifying information in your review.
- **Open review** (eLife, BMJ, some others): the review and reviewer name may be published. Write accordingly.
- **Signed review** (optional at many venues): you choose to sign. Fine, but commit to the same constructive standard.

## Quick checklist before producing review text

- [ ] Confidentiality OK (venue permits AI assistance, or manuscript is public, or self-review).
- [ ] No COI.
- [ ] Within expertise (or scoped to the parts you can evaluate).
- [ ] Within the deadline.
- [ ] Recommendation will be in the venue's accepted vocabulary.
- [ ] If reporting suspected misconduct, doing so in confidential editor channel, not public review.
