---
type: concept
created: 2026-08-26
---

# fMRI statistical analysis (the GLM, 1st & 2nd level)

How preprocessed BOLD data becomes statistical maps of "where the brain was active." Covered in
**Huettel Chapter 10** (Basic Statistical Analyses) and **Chapter 11** (Advanced), with hands-on
labs in **Week 9 (1st-level)** and **Week 11 (2nd-level)**. Built on the **General Linear Model
(GLM)** in [[spm|SPM]]. Previewed in the [[fmri-lab1-neuroanatomy|Week 2 lab]] (viewing SPM results).

## First-level analysis (single subject)
- Fit each voxel's **BOLD time series** with a **design matrix**: task regressors (condition
  onsets/durations) **convolved with the [[bold-signal|hemodynamic response function]]**, plus
  nuisance regressors (e.g. motion parameters).
- The GLM estimates a **beta** (weight) per regressor → `beta_*.nii` images.
- A **contrast** is a weighted combination of betas testing a hypothesis, e.g. **Right hand > Left
  hand** or "Effects of Interest" → `con_*.nii`, giving **t-maps (`spmT_*`)** or **F-maps
  (`spmF_*`)**.
- View in the **SPM contrast manager**: results shown on a **glass brain** and superimposed on the
  anatomical; threshold by **p-value with multiple-comparisons correction (FWE)** and a **voxel
  extent** threshold.

## Second-level analysis (group)
- Take each subject's first-level **contrast images** into a group model for **random-effects**
  inference — conclusions that generalize to the population, not just the sampled subjects.

## Multiple comparisons
- A brain has tens of thousands of voxels, so uncorrected thresholds yield many false positives.
  Correct with **FWE (family-wise error)** or **FDR (false discovery rate)**, optionally combined
  with cluster-extent thresholds. (Advanced topics, Ch 11.)

## Links
Preceded by [[fmri-experimental-design]] (the timing/condition choices that generate the design
matrix). Consumes [[fmri-preprocessing]] output; runs in [[spm]]; the "contrast" is the **functional
contrast** of [[mri-contrast]] and rides on the [[bold-signal]]. Applied in the group
[[fmri|project]]. Textbook: [[huettel-fmri-textbook]].
