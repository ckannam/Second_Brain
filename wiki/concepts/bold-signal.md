---
type: concept
created: 2026-08-26
---

# BOLD signal (Blood-Oxygenation-Level-Dependent contrast)

The physiological signal that virtually all of [[fmri|fMRI]] is built on. Rather than measuring
neural activity directly, fMRI measures a **metabolic/hemodynamic correlate** of it — changes in
blood oxygenation over time. Covered in **Huettel Chapters 6 & 7** ("From neuronal to hemodynamic
activity" / "BOLD fMRI"); introduced in [[fmri-week1-lecture-intro|Week 1]].

## The mechanism
- **Oxygenated hemoglobin (oxy-Hb) is diamagnetic** — it barely perturbs the local magnetic field.
  **Deoxygenated hemoglobin (deoxy-Hb) is paramagnetic** — it distorts the local field, which
  dephases spins and *reduces* the [[mri-contrast|T2*]] signal.
- So **more deoxy-Hb → less signal; less deoxy-Hb → more signal.**
- **Neurovascular coupling:** when a brain region is active, local blood flow increases to supply
  oxygen — and the flow response *overcompensates*, delivering more oxygenated blood than the tissue
  extracts. Net effect: **local deoxy-Hb concentration falls**, so the **T2*-weighted signal rises**.
- BOLD is therefore an **indirect, relative** measure — it reflects the difference between two (or
  more) conditions, not an absolute quantity of neural firing. This is why fMRI is a comparison /
  [[mri-contrast|functional-contrast]] technique.

## The hemodynamic response function (HDR)
- **Sluggish:** takes **1–3 s to rise** above baseline and **4–6 s to peak** after neural onset,
  followed by a return to baseline and a **post-stimulus undershoot**.
- This sluggishness is the main limit on fMRI **temporal resolution** (~1–3 s in typical designs;
  see [[mri-contrast#Resolution]]).
- Because the HDR has a roughly consistent shape, task regressors are **convolved with an HDR model**
  during [[fmri-glm-analysis|GLM analysis]] to predict the expected BOLD time course.

## How it's measured
- **T2*-weighted** [[mri-physics|gradient-echo]] sequences — **EPI** (echo-planar) or **spiral** —
  which are fast enough to sample the whole brain every ~2 s ([[mri-contrast|TR]] = 2 s in the class
  datasets).
- **CNR is low in fMRI** — the BOLD change is a small fraction of the signal, so we need many
  repetitions and statistics to detect it confidently.

## History
- **Seiji Ogawa (1990)** discovered that endogenous blood-oxygenation could serve as an MR contrast —
  the birth of fMRI. **Kwong et al. (1992)** produced the first human fMRI with a simple visual
  stimulation paradigm. See the MR-imaging timeline in [[mri-physics#History]].

## Links
Core method of [[fmri]]. Depends on [[mri-physics]] and [[mri-contrast]] (T2*). Feeds
[[fmri-preprocessing]] → [[fmri-glm-analysis]]. Related brain-science: [[neuroscience-of-behavior]].
