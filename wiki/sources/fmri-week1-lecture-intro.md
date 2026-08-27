---
type: source
source: lecture-slides
course: Functional Neuroimaging (NEUROSCI 382 / PSY 303)
week: 1
created: 2026-08-26
---

# Source: Week 1 Lecture — Introduction & Chapters 1 & 2

The Week 1 lecture deck (`Week1_Chapters1+2_Final.pptx`, 65 slides) — course intro plus a tour of
[[huettel-fmri-textbook|Chapters 1 & 2]]. Reading pairs: [[huettel-ch1-intro-to-fmri]] and
[[huettel-ch2-mri-scanners]].

## 1. What fMRI is NOT
- **Not phrenology** ("bumpology") — but it inherited phrenology's one durable idea, **localization
  of function**. **Not mind-reading** (though decoding is improving). **Not a simple one-to-one map**
  — a region (e.g. the insula) participates in many functions, so "activation ≠ function."
  **Not invasive** (unlike PET or intracranial recording).

## What fMRI IS
- A technique for measuring **metabolic correlates of neural activity** using a standard MRI scanner:
  non-invasive, non-ionizing (radiofrequency), repeatable, with good spatial + reasonable temporal
  resolution. A **measurement** (not manipulation) technique — see [[huettel-ch1-intro-to-fmri]].

## 2. Key concepts — Contrast & Resolution
- **Contrast:** anatomical (intrinsic tissue property, e.g. T1), functional (statistical comparison
  between conditions), and **CNR** (low in fMRI). **Resolution:** spatial (voxels — anat 0.5–1 mm,
  func 2–4 mm), temporal (TR-limited by sluggish BOLD ~1–3 s), functional. → [[mri-contrast]].

## 3. History of MR imaging
- Pauli (1924, spin) → Rabi (1937) → Purcell & Bloch (1946, Nobel '52) → Damadian (1971–77, tumor
  detection & "Indomitable") → Lauterbur (1973, gradients → first image) → Mansfield (EPI) → Ernst
  (1975, 2D FT) → **Ogawa (1990, BOLD)**. Kwong (1992) first human fMRI. → [[mri-physics#History]].

## 4. MRI scanners & 5. Safety
- Components: **static-field coils (B₀, always on)**, **RF coils** (send/receive; surface/volume/
  phased-array), **gradient coils** (x/y/z spatial encoding; Maxwell pair z, Golay pair x/y), shim
  coils. → [[mri-physics]]. **BOLD:** oxy-Hb (diamagnetic) vs deoxy-Hb (paramagnetic) → [[bold-signal]].
- **Safety by component:** magnet → projectiles (translation/torsion); gradients → dB/dt peripheral
  nerve stimulation; RF → SAR/heating. The fatal 2001 oxygen-tank accident. → [[huettel-ch2-mri-scanners]].

## Course logistics from the deck
- **Software to install before Week 2:** MATLAB (2026b or earlier, no toolboxes) + **[[spm|SPM]]**
  (deck says latest **SPM25**). Bring laptop to lab. Grading 30/30/30/10.
- ⚠️ *Deck template says "Thursdays"; the Fall 2026 syllabus says the class meets **Tuesdays** — trust
  the [[fmri-syllabus-fall2026|syllabus]].*

## Links
Reading: [[huettel-ch1-intro-to-fmri]], [[huettel-ch2-mri-scanners]]. Concepts: [[mri-physics]],
[[mri-contrast]], [[bold-signal]]. Course: [[fmri]].
