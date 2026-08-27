---
type: source
source: lab-handout
course: Functional Neuroimaging (NEUROSCI 382 / PSY 303)
week: 5
created: 2026-08-26
---

# Source: Lab 3 (Week 5) — Preprocessing

Week 5 lab handout (`2025_Week5_Preprocessing.docx`) — running the full [[fmri-preprocessing|SPM
preprocessing pipeline]] via the Batch Editor GUI, pairing with [[huettel-fmri-textbook|Chapter 8]].

## Dataset
- `Lab_03` (from Canvas): a **GE 3 T [[biac|BIAC]]** EPI **T2\*** acquisition — **160 volumes × 30
  slices**, **TR 2 s, TE/TA 27 ms, flip 77°, FOV 240×240, voxel 3.75×3.75×4 mm**, **ascending
  interleaved** slice order `[1 3 5…29 2 4…30]`. Two runs (`bia5_20105_006_01`, `…007_01`) + an Anat
  scan. Same left/right hand-squeeze task as [[fmri-lab1-neuroanatomy|Lab 1]].

## The pipeline (each step saved as a reusable Batch file)
1. **Realign (Est & Reslice)** — motion-correct all volumes to the first (6-param rigid body, least
   squares); produces motion plots + a `mean` image. → prefix `r`.
2. **Slice timing** — correct interleaved acquisition; enter #slices, TR, TA, slice order
   `[1:2:30 2:2:30]`, reference slice 1. → prefix `a`.
3. **Coregister (Estimate)** — align the subject's anatomical (moved) to the **mean functional**
   (fixed/reference).
4. **Segment** — split anatomical into GM/WM/CSF; save bias-corrected image + **forward deformation
   field** (`y_*`) for normalization.
5. **Normalize (Write)** — apply the `y_*` field to warp functional (2 mm voxels) and structural
   (1 mm voxels) into **[[mni-space|MNI space]]**. Check vs `avg305T1.nii` (blurry = average of 305
   brains) and `single_subject_T1.nii`. → prefix `w`.
6. **Smooth** — Gaussian **FWHM 6 6 6** mm (rule of thumb ≈ 2× voxel; 6–8 mm cortical; small for tiny
   structures like the inferior colliculus). → prefix `s`.

Cumulative prefixes → `swra…` = smoothed-normalized-realigned-slicetimed (why the fully processed
files are named that way). **No single correct pipeline** — document every step for replication.

## Links
Concept: [[fmri-preprocessing]] → feeds [[fmri-glm-analysis]]. Targets [[mni-space]]. Tools: [[spm]].
Data: [[biac]]. Course: [[fmri]]. Prev: [[fmri-lab2-kspace-contrast]].
