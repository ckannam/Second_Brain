---
type: concept
created: 2026-08-26
---

# MRI contrast & resolution

The two paired "key concepts" of the [[fmri-week1-lecture-intro|Week 1 lecture]], and the subject of
**Huettel Chapters 4 & 5** (MR image formation & MRI contrast). Explored hands-on in the
[[fmri-lab2-kspace-contrast|Week 3 contrast lab]] (T1 vs T2 tissue values).

## Contrast — three meanings
1. **Anatomical contrast** — reflects **intrinsic tissue properties** (e.g. longitudinal relaxation
   time → *T1 contrast*). Two aspects: *what* is measured, and *how much* intensity difference there
   is between tissues.
2. **CNR (contrast-to-noise ratio)** — the intensity difference between two quantities **divided by**
   the overall variability in their measurement. High CNR = sensitive to small differences.
   **CNR is critical but low in fMRI** — it sets how confidently we can call a region "active."
3. **Functional contrast** — in fMRI, a **statistical comparison between two or more experimental
   conditions**: is there a significant difference? (This is the sense used in
   [[fmri-glm-analysis|GLM contrasts]] like "Right hand > Left hand.")

## Weightings and timing parameters
- **T1-weighted** — anatomical scans; excellent gray/white/CSF distinction (e.g. SPGR sequence).
- **T2-weighted** — sensitive to T2; different tissue appearance (CSF bright).
- **T2\*-weighted** — the **[[bold-signal|BOLD]]** contrast used for functional imaging (EPI/spiral).
- **Proton density** — reflects tissue proton concentration.
- **TR (repetition time)** — time between successive excitations of the same slice; expressed in
  **seconds**; most associated with **T1**.
- **TE (echo time)** — time between excitation and signal readout (echo); expressed in
  **milliseconds**; most associated with **T2**.
- *Class datasets:* anatomical SPGR (T1, 0.938×0.938×1 mm); functional EPI T2\* (TR 2 s, TE ~27 ms,
  flip 77°, 3.75×3.75×4 mm) — see [[fmri-lab3-preprocessing]].

## Resolution — three kinds
- **Spatial resolution** — set by **voxel** (3-D volume element) size. Anatomical (MRI) voxels
  ~**0.5–1 mm**; functional (fMRI) voxels ~**2–4 mm**. Smaller voxels = higher anatomical resolution.
- **Temporal resolution** — set by **sampling rate (TR)** and limited by the **sluggish
  [[bold-signal|BOLD]] response**; typically **~1–3 s** (rarely pushed to a few 100 ms).
- **Functional resolution** — the ability to actually measure the relationship between neural
  activity and the cognitive/behavioral phenomenon of interest. Limited both by the intrinsic
  measure (hemodynamics) **and** by how well the **experimental design** isolates the phenomenon.

## Links
Built on [[mri-physics]] and read out through [[k-space]]. T2\* underlies [[bold-signal]]. Functional
contrast is realized in [[fmri-glm-analysis]]. Textbook: [[huettel-fmri-textbook]].
