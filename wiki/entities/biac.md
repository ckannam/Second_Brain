---
type: entity
created: 2026-08-26
---

# BIAC (Brain Imaging and Analysis Center, Duke)

Duke's neuroimaging facility where the [[fmri]] class acquires its own data.

- Houses the **GE 3 T MRI scanner** used for the class datasets (functional EPI, T2\*-weighted).
- **Scanning is expensive — ~$640 per hour** — so scripts must be fully working before a
  participant is run. Each group gets **two 2-hour scanning sessions** (≈2 participants).
- Data filenames from BIAC carry the **`bia5_…`** prefix (e.g. `bia5_20105_003.nii` anatomical,
  `bia5_20105_006_01.nii` functional) — see the class [[fmri-lab1-neuroanatomy|lab dataset]].
- The **Week 1 class includes a "Tour of BIAC."** Clinical-fMRI guest lecture (Week 13) is by
  **Jim Voyvodic**, a BIAC faculty member.

## Links
Scanner data flows into [[fmri-preprocessing]] → [[fmri-glm-analysis]] via [[spm]]. Course: [[fmri]]
at [[Duke]]. Run by [[crm/Tobias Overath|Prof. Overath]] for the class.
