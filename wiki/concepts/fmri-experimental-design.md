---
type: concept
created: 2026-08-30
---

# fMRI Experimental Design

The upstream step in any fMRI pipeline — choices made here determine what the
[[fmri-glm-analysis|GLM]] can and can't detect, how efficient the experiment is, and
how cleanly activations localize. Covered in **Huettel Chapter 7** (Block and Event-Related
Design) and woven through the [[fmri-syllabus-fall2026|NEUROSCI 382]] group-project work.

> **Synthesis note.** This page was generated from knowledge + vault context (2026-08-30);
> reconcile specific chapter references and timing numbers against the course syllabus and
> Huettel 3rd ed. before relying on them.

## Block designs

**Structure:** alternate long windows of a single condition ("A-A-A-A") with baseline rest
("B-B-B-B"). Typical block length 15–30 s.

**Pros:**
- Maximum statistical power for detecting *sustained* responses (the sustained BOLD signal
  accumulates across the block → high SNR).
- Simple to implement and analyze; the first fMRI experiments were all block designs.
- Easy to find in the SPM contrast manager — the design matrix looks like a square wave.

**Cons:**
- Participants *know* which condition they're in → **cognitive predictability / strategy**
  confound (they may not process naturalistic stimuli the same way).
- Can't separate the *onset* of a neural event from the *sustained* response — bad for
  cognitive chronometry questions ("when does this region activate?").
- **Ceiling and habituation** effects compound within a long block.

## Event-related designs

**Structure:** brief individual stimuli or trials intermixed and presented at varying intervals.
Each trial is a discrete event convolved with the [[bold-signal|hemodynamic response function]].

**Pros:**
- Randomization eliminates the predictability confound.
- Can sort trials *post-hoc* by behavioral response (e.g. remembered vs. forgotten) — a key
  advantage for [[memory-consolidation|memory]] studies. You can't do this with block designs.
- Answers "what happens at the moment of X" rather than "what is active during a block of X."

**Cons:**
- Lower raw power per unit time: the HRF takes ~5–6 s to peak and ~20 s to recover; if trials
  are spaced too tightly the responses overlap. Spacing them widely means few trials per run.
- Efficiency (see below) must be actively optimized.

## Mixed designs

Hybrid: long blocks of a *category* with varied event trials inside them. E.g. a block of
"face stimuli" where each face onset is a discrete event. Captures both sustained (category
encoding) and transient (individual trial) responses. More complex to model but powerful for
separating encoding from maintenance.

## Efficiency and jitter

**Efficiency** is the inverse of the variance of GLM beta estimates — a more efficient design
gives tighter confidence intervals. Because the HRF is slow and correlated across time, the
optimal inter-stimulus interval (ISI) is **not** zero (trials don't just stack additive power;
overlapping HRFs are harder to deconvolve).

**Jitter:** randomize the ISI, typically drawn from a distribution with mean ~4–6 s but
variable (e.g. exponential or truncated uniform). Jittering:
- Breaks up HRF autocorrelation, so the design matrix columns are more orthogonal.
- Improves efficiency: the GLM can estimate overlapping responses cleanly when onsets are
  unpredictable.
- A **null ISI** (a fraction of trials are simply empty) further boosts efficiency by sampling
  the baseline spontaneously.

Efficiency can be computed analytically from the design matrix **before data acquisition**
using tools like the SPM design efficiency function or FSL's `feat_model`. The course group
project designs go through this step.

## Contrast design and power

A contrast is a difference between conditions: **A − B**, **A − (B+C)/2**, etc. Good
experimental design pre-specifies the contrasts of interest and checks:
1. **Orthogonality** — the conditions being contrasted should differ on one dimension only
   (all else held equal). "Language vs. rest" confounds language processing with
   visual/auditory stimulus onset; "language vs. non-word control" is tighter.
2. **Counterbalancing** — stimulus order, side, and session effects balanced across
   conditions so they don't drive the contrast.
3. **Power calculations** — how many subjects and trials are needed to detect an effect of
   the expected size at acceptable α and power? Effect sizes in fMRI are often small; most
   adequately powered cognitive studies need ≥20 subjects for group-level inference.

## Practical rules for the NEUROSCI 382 group project

- Discuss the design with the group **before scanning** — a poor design can't be fixed in
  post-processing.
- For event-related studies: aim for ≥20–30 trials per condition per subject; jitter ISIs.
- Keep total run time ≤45 min; split into 2–4 runs to control head motion and habituation.
- Pre-register the contrast of interest; SPM's GLM will let you add exploratory contrasts
  but the confirmatory one should be chosen a priori.

## How this page connects

Experimental design feeds the **[[fmri-glm-analysis|GLM]]**: the onset timing you choose
becomes the design matrix (regressors convolved with the [[bold-signal|HRF]]). The
[[fmri-preprocessing|preprocessing pipeline]] runs on whatever data the design produces.
[[fmri-lab3-preprocessing|Lab 3]] assumes the design is already done; this page is the
step before it. See also [[mri-contrast]] (the BOLD signal being sampled) and
[[fmri-syllabus-fall2026]] (where in the course these topics appear).

Related: [[fmri]] · [[bold-signal]] · [[fmri-glm-analysis]] · [[fmri-preprocessing]] ·
[[mri-contrast]] · [[huettel-fmri-textbook]] · [[spm]] · [[fmri-syllabus-fall2026]].
