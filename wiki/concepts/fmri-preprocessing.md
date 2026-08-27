---
type: concept
created: 2026-08-26
---

# fMRI preprocessing

The routines you run on raw functional data **before** any statistical analysis. Subject of
**Huettel Chapter 8** (Signal, Noise & Preprocessing) and the hands-on
[[fmri-lab3-preprocessing|Week 5 preprocessing lab]] (done in [[spm|SPM]] via the Batch Editor GUI).

> Data comes off the scanner already reconstructed into **image space** (recall it is *acquired* in
> [[k-space]]). Preprocessing cleans and standardizes it. There is **no single correct pipeline** —
> steps, order, and parameters vary by researcher; the rule is to **document exactly what you did** so
> another researcher can replicate it.

## The pipeline (SPM order used in class)
1. **Realignment (motion correction)** — aligns the (often hundreds of) volumes to a reference
   volume (usually the first) using a **least-squares, 6-parameter rigid-body** transform.
   *Estimate* the motion parameters, then *Reslice* to apply them. Produces a **mean** functional
   image and motion-parameter plots. (Optional **unwarp** for susceptibility × motion interactions.)
2. **Slice-timing correction** — volumes are built slice-by-slice, so slices within one TR are
   acquired at different times (class data: **interleaved** `[1 3 5…29 2 4…30]`). Corrects each
   slice to a **reference slice**; needs number of slices, TR, and TA.
3. **Coregistration** — aligns the **same subject's** high-resolution anatomical scan to the **mean
   functional** image so low-res BOLD activations can be shown on high-res anatomy.
4. **Segmentation** — classifies the anatomical scan into **gray matter, white matter, CSF** using
   tissue templates; also writes a **deformation field** (the parameters used for normalization) and
   an optional bias-corrected image.
5. **Normalization** — warps the data into a **common stereotactic space ([[mni-space|MNI]])** so a
   given region (e.g. V1) sits at roughly the same coordinates in every subject, enabling comparison
   across subjects and studies. Functional images resampled to ~2 mm; structural kept at 1 mm to
   preserve detail.
6. **Spatial smoothing** — convolve each voxel with a **Gaussian kernel** (size in **FWHM**).
   Increases **SNR** and validity of the statistics. Rule of thumb: **FWHM ≈ 2× voxel size**; **6–8
   mm** for most cortical data; smaller (or none) for small structures like the inferior colliculus.

Each step adds a **filename prefix** in SPM (e.g. `r` realigned, `a` slice-time-corrected, `w`
normalized, `s` smoothed → `swra…`), which is why the fully preprocessed files are named `swra*`.

## Links
Runs in [[spm|SPM]]; output feeds [[fmri-glm-analysis|1st-level GLM analysis]]. Depends on
[[k-space]] (reconstruction) and targets [[mni-space]]. Data from [[biac]]. Textbook:
[[huettel-fmri-textbook]].
