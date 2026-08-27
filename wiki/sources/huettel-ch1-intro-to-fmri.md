---
type: source
source: textbook-chapter
book: Huettel Song McCarthy — fMRI (3rd ed.)
chapter: 1
created: 2026-08-26
---

# Source: Huettel Ch. 1 — An Introduction to fMRI

Chapter 1 of the [[huettel-fmri-textbook|course textbook]] (Week 1 reading). Full OCR notes captured;
this is the exam-oriented digest.

## What fMRI is
- **fMRI** uses standard MRI scanners to investigate **changes in brain function over time**; within
  ~20 years of its 1990s birth it became the **dominant technique in cognitive neuroscience**.
- **Structural vs functional neuroimaging:** structural images anatomy; functional (fMRI, PET,
  optical) images active processing. Most fMRI measures **blood oxygenation** ([[bold-signal|BOLD]]).
- **PET** — functional imaging via injected radioactive tracer (blood flow/glucose); can target
  specific chemicals/receptors but is **invasive, slow, expensive**. fMRI is noninvasive & repeatable.

## Measurement vs manipulation (key distinction)
- **Measurement techniques** record the brain during a task: fMRI, PET, **EEG** (great temporal, poor
  spatial), **MEG**, ERP, single-unit. **Manipulation techniques** alter the brain and observe
  behavior: **lesions**, **TMS** ("virtual lesion"), drugs.
- **fMRI shows correlation, not necessity** — combine with manipulation (lesion/TMS) for causal
  claims. Know the "unplugging a radio component" limitation of lesion inference.
- History: **Broca (1861)** — patient "Tan," left-frontal lesion → language-production localization.

## Four core measurement concepts → [[mri-contrast]]
- **Contrast** (3 senses: intensity difference / physical quantity measured / statistical comparison),
  **CNR**, **spatial resolution** (pixel vs **voxel**; signal ∝ voxel volume; ~3 mm typical human
  fMRI), **temporal resolution** (limited by the sluggish hemodynamic response, not the scanner).
- **Technique space (Fig 1.8):** every method trades spatial × temporal resolution × invasiveness;
  fMRI sits in a favorable middle. **Tesla:** 1 T ≈ 20,000× Earth's field; 1.5 T clinical, 3 T
  research standard, 7 T+ research.

## History of fMRI → [[mri-physics#History]]
Pauli (spin) → Rabi (1938, Nobel '44) → Bloch & Purcell (1946, Nobel '52) → Damadian (1971 cancer
relaxation; 1977 first human MRI "Indomitable"/Minkoff) → Lauterbur (1973 gradients → first image) →
Mansfield (EPI, 1976) → Lauterbur & Mansfield **Nobel 2003** (Damadian controversially excluded, Box
1.2) → Ogawa (1990s BOLD). MRI advantages: superior soft-tissue contrast, noninvasive, no ionizing
radiation, any plane.

## Book roadmap (chapters)
Ch 2 scanners/safety · Ch 3 MR physics (T1/T2 relaxation) · Ch 4 gradients→[[k-space]]→image · Ch 5
static vs motion contrasts · Ch 6–8 BOLD biology & [[fmri-preprocessing|preprocessing]] · Ch 9 design
(rapid event-related & blocked) · Ch 10 [[fmri-glm-analysis|GLM]] & multiple comparisons · Ch 11
data-driven/connectivity/MVPA · Ch 12 advanced · Ch 13 cognitive-neuro applications · Ch 14 ethics.

## Links
Concepts: [[bold-signal]], [[mri-contrast]], [[mri-physics]]. Next: [[huettel-ch2-mri-scanners]].
Lecture: [[fmri-week1-lecture-intro]]. Course: [[fmri]].
