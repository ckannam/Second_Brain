---
type: concept
created: 2026-08-26
---

# MRI physics (spins, resonance, the scanner)

The physical basis of magnetic resonance imaging — the foundation the whole [[fmri]] course builds
on. **Huettel Chapter 3** (MR Physics, "Conceptual Path") and the [[fmri-week1-lecture-intro|Week 1
lecture]]. These first weeks are the hardest, most physics-heavy part of the class.

## MR = Magnetic + Resonance
- Atomic nuclei with an odd number of protons (esp. **hydrogen, ¹H**, abundant in water/fat) have
  **spin** and therefore a **magnetic moment** — they behave like tiny bar magnets.
- In a strong static field **B₀** they **align** with the field and **precess** at a characteristic
  **resonant (Larmor) frequency** that is **proportional to field strength** (in the radiofrequency /
  MHz range at clinical field strengths).
- The static field alone produces **no usable signal**. Signal is created by the sequence:
  align → **excite with an RF pulse at the resonant frequency** → nuclei absorb the energy → after
  the pulse stops they **relax and re-emit** the energy → **RF coils receive it = the raw MR signal.**

## Relaxation and time constants
- **T1 (longitudinal relaxation):** recovery of magnetization along B₀; governs **[[mri-contrast|TR]]**
  (repetition time, in seconds).
- **T2 (transverse relaxation):** decay of magnetization in the plane; governs **[[mri-contrast|TE]]**
  (echo time, in ms).
- **T2\*:** T2 plus dephasing from field inhomogeneity — the contrast the [[bold-signal|BOLD signal]]
  exploits.

## The scanner — main components
- **1. Static field coils** → generate **B₀** (e.g. **1.5 T, 3 T**). Dense parallel wire coilings
  (Helmholtz pair / solenoid). Two things matter: **homogeneity** and **field strength**.
  **The magnet is always on.**
- **2. RF coils** → **send and receive** the oscillating field at the resonant frequency; turned on
  briefly. Types: **surface, volume, phased-array** (received intensity falls off with distance).
- **3. Gradient coils** → three **orthogonal linear magnetic gradients** (x, y, z) that make the
  resonant frequency **spatially dependent**, enabling **spatial encoding** of the signal
  (z = Maxwell pair; x, y = Golay pairs). This is what turns NMR into **imaging** and defines
  [[k-space]].
- **Others:** shim coils (improve homogeneity), computers, stimulus/physiological hardware.

## History (MR-imaging timeline)
- **1924 Pauli** — nuclei have spin/magnetic moment. **1937 Rabi** — measures nuclear magnetic
  moment, coins "magnetic resonance." **1946 Purcell & Bloch** — resonant absorption & detectable
  precession (shared **1952 Nobel**). **1971 Damadian** — NMR distinguishes tumor vs healthy tissue
  (relaxation-time differences; first medical application). **1973 Lauterbur** — first NMR *image*
  using magnetic gradients; **Mansfield** independently, later develops fast **EPI**. **1975 Ernst** —
  2D Fourier transform for MR (**NMR → MRI**). **1990 Ogawa** — endogenous blood-oxygenation contrast
  (**MRI → fMRI**; see [[bold-signal]]).

## Advantages & safety
- **Advantages:** high-resolution, images many tissue types in one image, **any imaging plane**,
  **no ionizing radiation** (unlike X-ray/CT/PET).
- **Safety risks by component:** static magnet → **projectile effects** (translation, torsion) — the
  magnet is always on; gradients → rapid **dB/dt** can cause **peripheral nerve stimulation**; RF →
  **SAR** (specific absorption rate), tissue heating/burns. Metal is the central hazard (the fatal
  2001 oxygen-tank accident).

## Links
Foundation of [[mri-contrast]], [[k-space]], and [[bold-signal]]. Scanning happens at [[biac]]
(Duke's 3 T GE scanner). Textbook: [[huettel-fmri-textbook]].
