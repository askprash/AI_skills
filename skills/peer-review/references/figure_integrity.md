# Figure and Data Integrity

Figures are where scientific fraud most often surfaces and where honest sloppiness most often misleads readers. Treat them as primary data, not decoration.

## Table of contents

1. [Western blots and gels](#western-blots-and-gels)
2. [Microscopy and fluorescence images](#microscopy-and-fluorescence-images)
3. [Flow cytometry](#flow-cytometry)
4. [Image duplication and reuse](#image-duplication-and-reuse)
5. [Quantitative figures](#quantitative-figures)
6. [Error bars and statistics on figures](#error-bars-and-statistics-on-figures)
7. [Color and accessibility](#color-and-accessibility)
8. [Image manipulation forensics](#image-manipulation-forensics)
9. [Workflow for image-heavy papers](#workflow-for-image-heavy-papers)

---

## Western blots and gels

**What to check:**

- **Cropping**: Is the full blot shown, or only a tight band? Tight crops can hide loading-control problems or splice marks. Cropped blots are acceptable for the main figure but the full blot should be in supplementary.
- **Splice marks**: Sharp edges, mismatched backgrounds, or step changes in lane spacing indicate the lanes have been spliced together. Splicing isn't always misconduct (sometimes lanes are reordered from a larger blot), but it must be disclosed.
- **Loading controls**: Are loading controls (β-actin, GAPDH, vinculin) shown? Are they from the *same* blot as the test bands? "Loading control" from a different blot doesn't control for loading.
- **Same loading control across panels**: If the same β-actin image appears for multiple test proteins claimed to be from separate blots, that's a flag.
- **Band intensity quantification**: Is densitometry reported with replicates? Is the linear range demonstrated? Saturated bands can't be quantified.
- **Molecular weight markers**: Are MW markers shown adjacent to the band of interest? Bands without MW context can't be confirmed as the expected protein.
- **Antibody validation**: Is the antibody validated for the application (knockout/knockdown control, multiple bands explained)?

**Red flags:**

- Identical bands across "different" conditions.
- Identical backgrounds across "different" blots.
- Bands that appear unusually clean against a noisy background, or vice versa.
- Sharp rectangular boundaries that don't follow the blot's natural texture.

## Microscopy and fluorescence images

**What to check:**

- **Scale bars**: Present, labeled with units, appropriate size?
- **Acquisition parameters**: Magnification, exposure, gain, laser power, pinhole — reported, and the same across conditions being compared?
- **Linear processing**: Are adjustments (brightness, contrast) applied linearly and to the entire image, or only to parts? Selective enhancement is misconduct.
- **Channel separation**: For multi-channel fluorescence, are individual channels shown alongside merged?
- **Pseudocolor**: Is the choice of colors disclosed (and accessible — see Color and Accessibility below)?
- **Representative images**: Is "representative" actually representative? Are quantifications across multiple fields shown alongside the representative image?
- **Sample size for imaging**: How many cells / fields / animals were analyzed per condition?
- **Threshold for analysis**: If positive/negative cells are counted, what threshold was used and how was it set (blinded? pre-specified?)?
- **Z-stacks vs. single planes**: For 3D structures, is the z-handling appropriate?

**Red flags:**

- Identical cells or features across "different" conditions (often rotated, flipped, or cropped to hide reuse).
- Sharp boundaries within an image suggesting clone-and-paste.
- Backgrounds that don't match the visible features.
- Saturated channels (clipped pixels) used for quantification.

## Flow cytometry

**What to check:**

- Gating strategy shown (FSC/SSC → singlets → live → CD3 → etc.).
- Compensation controls described.
- Fluorochrome panel and spectral overlap addressed.
- Frequencies reported, not just gates drawn.
- Comparison conditions shown side-by-side with matched scales.
- For rare-event analysis (e.g., <1%): n events collected, FMO controls, isotype controls.

**Red flags:**

- Gating drawn around regions that conveniently include some events and exclude others, without justification.
- Different gates for the same population across panels.
- Compensation never shown for spectral overlap.

## Image duplication and reuse

The most common form of figure misconduct is image reuse — same image, presented as different experiments. Tools and habits:

- **Visual scan**: When reviewing a paper, lay all figures side-by-side (or open them in separate tabs). Look for any image that strikes you as familiar.
- **Suspect patterns**: Same loading control across multiple "independent" experiments. "Representative" images that look identical to images in the authors' earlier publications. Backgrounds that match across different conditions.
- **Tools (for editors and forensic specialists, generally not reviewers)**: ImageTwin, Imagecheck, Proofig, Forensically. Reviewers typically don't use these but can flag visual concerns to editors.

**What to do**: If you suspect image reuse, do **not** accuse in the public review. Raise it privately with the editor in the confidential comments, with specifics: "Figure 2D and Figure 4B appear to share a region — the cell cluster at upper right looks identical. An image-forensics review may be warranted."

## Quantitative figures

- **Axes**: Labeled, with units, with appropriate scale (linear vs. log)? Truncated y-axes can exaggerate effects — flag if egregious.
- **Sample size**: Shown for each group, ideally as individual data points (strip plot, swarm plot, or jittered dots over a bar/box plot).
- **Distribution shown**: Bar charts hide distribution; box plots, violin plots, or strip plots show it. Bar-with-SEM is widely deprecated for small-n biology.
- **Independence of points**: Each point should be one experimental unit. Cells from the same animal are not independent.
- **Statistical annotations**: What test? What correction? What does each asterisk represent? Defined in the legend?
- **Color choices**: Distinguishable for colorblind viewers? Sufficient contrast? Print-safe if relevant?
- **Legends self-contained**: Could a reader understand the figure from the legend alone?

## Error bars and statistics on figures

A perennial issue: error bars are often included without specifying what they represent.

- **SD vs. SEM vs. CI**: Different things. SEM is ~1/√n times SD, so SEM bars are smaller — using SEM where SD is more informative is a way to make figures look cleaner.
  - SD: variability of the data.
  - SEM: precision of the mean estimate.
  - 95% CI: range of plausible values for the parameter.
- **Always say which one** in every figure legend.
- **For comparisons**, CIs are most informative; non-overlapping 95% CIs roughly correspond to p<0.05 for the difference but this is rough.
- **No error bars at all**: Means without measures of variability are uninterpretable.
- **Asymmetric bars** for log-transformed or proportion data may be appropriate (don't assume symmetric).
- **Sample size**: SEM and CI depend on n. Reporting just "error bars" with no n is uninterpretable.

## Color and accessibility

- **Colorblind safety**: About 8% of men and 0.5% of women have some form of color vision deficiency. Avoid red/green as the primary contrast. Use viridis, cividis, or other CVD-safe palettes for continuous data; use ColorBrewer "Set2" or similar for categorical.
- **Heatmaps**: Sequential (light-to-dark) for unsigned data, diverging (color-neutral-color) for signed data. Avoid rainbow palettes (jet, hsv) for quantitative data — they create perceptual edges where none exist.
- **Print-safe**: Will the figure be readable in grayscale? If the paper prints, this still matters.
- **Sufficient contrast**: WCAG-style contrast checks for important text on colored backgrounds.

## Image manipulation forensics

These signs warrant flagging to the editor in confidential comments:

- **Sharp rectangular regions** with different texture, contrast, or noise level than the surrounding image.
- **Repeated patterns** within a single image (same cell, same band, copy-pasted).
- **Smooth blurry patches** in otherwise sharp images (clone-tool artifacts).
- **Unnatural uniformity** of background (rubber-stamp or pattern-fill artifacts).
- **Inconsistent shadows or lighting** suggesting elements were composited.
- **Missing or implausible noise** in regions where pixel-level noise should be visible.
- **JPEG artifacts** localized to suspicious regions of a TIFF/PNG file.

Reviewers usually can't run forensic tools, but trained eyes catch a lot. If something looks edited, it may be.

## Workflow for image-heavy papers

1. **Open all figures at once** at the start of review, not as you encounter them in the text.
2. **Make a mental inventory**: how many distinct images are claimed, and do they look distinct?
3. **For each figure, read the legend first**. Then look at the image. Are they consistent?
4. **For quantitative panels, sanity-check the numbers**: do the bar heights match the reported means? Do error bars make sense given the n?
5. **Note any concerns** as you go. Group them into "ask in review" (clarifications, missing info) and "flag to editor" (integrity concerns).

## What to put in the review

- **Constructive figure suggestions**: clearer labels, better axes, distribution shown, color accessibility — these go in the review text (minor or major as appropriate).
- **Integrity concerns**: confidential comments to editor, not in author-facing review.
- **Specific, located comments**: "Figure 3B: the y-axis is truncated below 50%, which visually exaggerates the difference; please use a full-scale axis or add a clear break." Beats: "Figures could be improved."
