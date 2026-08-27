---
type: concept
created: 2026-08-26
---

# MNI space (standard stereotactic space)

The **common coordinate space** fMRI data are warped into during
[[fmri-preprocessing#The pipeline (SPM order used in class)|normalization]] so that results can be
compared across subjects and studies.

- **MNI = Montreal Neurological Institute.** The space is defined from anatomical scans of **hundreds
  of neuro-typical, right-handed individuals**, averaged together.
- Every brain differs — even identical twins have different cortical gyrations — so normalizing to a
  template puts a region like **V1 at roughly the same (x, y, z) coordinate in everyone**.
- Reference volumes used in [[spm|SPM]]'s `canonical` folder:
  - **`avg305T1.nii` / avg152** — the average of hundreds of normalized brains; looks **blurry**
    precisely *because* it is an average over many individually-different brains.
  - **`single_subject_T1.nii`** — one individual brain from the MNI database that best matches the
    reference space (sharp; used for overlaying results).
- Coordinates are reported in **mm** relative to a defined origin (near the anterior commissure —
  see the AC–PC landmarks in [[neuroanatomy-landmarks]]).

## Links
The target of [[fmri-preprocessing]] normalization; enables group [[fmri-glm-analysis]]. Related:
[[neuroanatomy-landmarks]].
