---
type: entity
created: 2026-08-26
---

# SPM (Statistical Parametric Mapping)

The **MATLAB-based neuroimaging software** used throughout the [[fmri]] course for viewing,
preprocessing, and statistically analyzing MR data.

- Developed by the **Wellcome Centre for Human Neuroimaging (FIL), UCL** —
  `https://www.fil.ion.ucl.ac.uk/spm/`.
- **Runs on MATLAB** (course requires MATLAB 2026b or earlier; "no toolboxes necessary"). Started by
  typing `spm fmri` at the MATLAB prompt.
- **Latest version is SPM25**, which the syllabus/lecture tells students to install. ⚠️ The class
  **lab handouts were written for `spm12`** (they reference the `spm12` folder and its `canonical`
  templates) — use the version the instructor specifies for a given lab; the workflow is the same.
- **What it does in class:**
  - *Display / Check Reg* — view anatomical & functional volumes in 3 orthogonal planes; scroll BOLD
    time series ([[fmri-lab1-neuroanatomy]]).
  - *Batch Editor* — the [[fmri-preprocessing]] pipeline (Realign, Slice Timing, Coregister, Segment,
    Normalize, Smooth), saved as reusable batch files.
  - *Results / contrast manager* — [[fmri-glm-analysis|GLM]] contrasts on a glass brain with FWE
    thresholding.
- Files use the **NIfTI** (`.nii`) format; the design/analysis is stored in **`SPM.mat`**.
- Viewing-only alternative mentioned: **MRIcron** (no MATLAB required).

## Links
Runs [[fmri-preprocessing]] and [[fmri-glm-analysis]]; targets [[mni-space]]; used on [[biac]] data.
Course: [[fmri]].
