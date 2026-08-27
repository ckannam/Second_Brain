---
type: source
source: lab-handout
course: Functional Neuroimaging (NEUROSCI 382 / PSY 303)
week: 3
created: 2026-08-26
---

# Source: Lab 2 (Week 3) — Understanding k-Space & Contrast

Week 3 lab handout (`2025_Week3_kspace_and_contrast.docx`) — two exercises done in MATLAB/[[spm|SPM]],
pairing with [[huettel-fmri-textbook|Chapters 4 & 5]]. Concepts: [[k-space]], [[mri-contrast]].

## Part A — k-Space (MATLAB)
- Load the [[fmri-lab1-neuroanatomy|Anat dataset]] with `spm_vol` / `spm_read_vols`; extract slice 80
  (256×256). Transform to [[k-space]] with `fftshift(fft2(...))`; view magnitude on a **log scale**
  (`20*log10`) because the low-frequency center dominates.
- **Demonstrations (exam-relevant intuition):**
  - **Corrupt one k-space point** ("spike") → a **striped wave artifact** across the whole image; the
    point's position sets stripe direction/frequency (Q2–Q4 ask you to recreate ////, \\\\, and
    high-frequency horizontal stripes by choosing points).
  - **Keep only the center** (low spatial frequencies) → **blurry** image (Q5).
  - **Zero out the center, keep the periphery** (high spatial frequencies) → **edges only** (Q6).
- Ties EPI (line-by-line) vs spiral (whirlpool) k-space traversal to their artifacts.

## Part B — Contrast (SPM)
- Compare co-registered **T1.nii vs T2.nii** axial scans in *Check Reg*; read out signal intensity
  (Y) per tissue type. **Q3 table:** record T1 & T2 values for white matter, gray matter, CSF, skull,
  air (the crux: CSF is dark on T1, bright on T2, etc.).
- **Pulse-sequence parameters (Q4–Q7, exam material):**
  - **TR (repetition time)** — time between two excitations of the same slice; in **seconds**;
    associated with **T1**.
  - **TE (echo time)** — time between excitation and echo readout; in **milliseconds**; associated
    with **T2**. → [[mri-contrast]].

## Links
Concepts: [[k-space]], [[mri-contrast]], [[mri-physics]]. Tools: [[spm]]. Course: [[fmri]].
Prev: [[fmri-lab1-neuroanatomy]] · Next: [[fmri-lab3-preprocessing]].
