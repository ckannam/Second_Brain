---
type: source
source: lab-handout
course: Functional Neuroimaging (NEUROSCI 382 / PSY 303)
week: 2
created: 2026-08-26
---

# Source: Lab 1 (Week 2) — Intro to Neuroanatomy in SPM

Week 2 lab handout (`2024_Week2_Anatomy.docx`) — first hands-on lab: viewing anatomical & functional
MR images in [[spm|SPM]] and identifying [[neuroanatomy-landmarks|anatomical landmarks]].

## Setup
- Create `Neurosci382/Software`, unzip **SPM** (`spm12`) into it, add to the MATLAB path. Start with
  `spm fmri`. Data (`Lab1_Data.zip`) → `Neurosci382/Lab1`. Viewing-only alternative: **MRIcron**.

## The lab dataset (also reused in later labs)
> This is exactly the **`Data/` folder Cole provided** (`Anat/` + `Func/`), a completed
> [[spm|SPM]] analysis of a **blocked finger-tapping** experiment. **Not copied into the vault**
> (~486 MB of NIfTI); it lives at `/Users/colekannam/Downloads/Data`.
- **Anat** — one high-res T1 anatomical (inversion-prepared 3D SPGR), **256×256×162**, voxel
  **0.938×0.938×1 mm**. Files `bia5_20105_003.nii` (raw), `wmbia5_20105_003.nii` (normalized).
- **Func** — gradient-echo spiral BOLD series, **64×64×34 × 160 volumes**, voxel **3.75×3.75×4 mm**,
  **TR 2 s** (160×2 s = 5.33 min). Task = blocked **[Rest – Right-hand tap – Rest – Left-hand tap]**,
  20 s (10 vol) blocks ×4. Contains `SPM.mat`, beta/con/spmT images, `swra…` preprocessed volumes.
- **NIfTI (`.nii`)** is the universal MR image format; SPM shows 3 orthogonal planes (Coronal,
  Sagittal, Axial) with **vx** and **mm** coordinates.

## What the lab teaches
1. **View anatomy** — load `bia5_20105_003.nii`, scroll orthogonal planes.
2. **View functional images** — scroll the 160-volume time series (see the head drift → motion, the
   reason for [[fmri-preprocessing|realignment]]); *Display Profile* plots a voxel's **BOLD time
   course** (motor-cortex voxel [42,35,24] shows clear task-locked ups/downs vs a random visual voxel).
3. **View activations** — `Results` → `SPM.mat` → *Effects of Interest*, threshold **FWE p<0.05** →
   glass brain, overlaid on the anatomical; switch contrast to **Right Hand > Left Hand**. Previews
   [[fmri-glm-analysis]].
4. **Identify landmarks (Q6)** — locate amygdala (given ≈ [24, 24, −16]), AC/PC, pons, IFG, anterior
   cingulate, hippocampus, central sulcus, inferior colliculus, insula, Heschl's gyrus →
   [[neuroanatomy-landmarks]].

## Links
Tools: [[spm]]. Concepts: [[neuroanatomy-landmarks]], [[bold-signal]], [[fmri-glm-analysis]],
[[mri-contrast]]. Data from [[biac]]. Course: [[fmri]]. Next lab: [[fmri-lab2-kspace-contrast]].
