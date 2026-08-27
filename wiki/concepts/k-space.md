---
type: concept
created: 2026-08-26
---

# k-space

**k-space** is the **spatial-frequency domain** in which raw MRI data are actually acquired; the
image we look at is produced by **reconstructing** k-space with an **inverse 2-D Fourier transform**.
Subject of **Huettel Chapter 4** and the hands-on [[fmri-lab2-kspace-contrast|Week 3 k-space lab]]
(done in MATLAB with `fft2` / `fftshift` / `ifft2`).

## Why it matters
- k-space is the **link between the physics** (how [[mri-physics|gradients]] spatially encode the MR
  signal) **and the images** — the raw signal is inherently a set of spatial frequencies.
- Different **pulse sequences traverse k-space differently**, which drives their trade-offs and
  artifacts:
  - **Echo-planar (EPI)** — sweeps k-space **line by line**.
  - **Spiral** — traverses in a **whirlpool/spiral** motion (used for the class BOLD data).

## The structure of k-space
- **Center of k-space = low spatial frequencies** → overall **contrast and brightness**; these
  points carry huge magnitude (a bright spot in the middle; best viewed on a log scale).
- **Periphery = high spatial frequencies** → **edges and fine detail**.
- Manipulations demonstrated in lab:
  - **Corrupt a single k-space point** ("spike," e.g. bad electronics) → a **striped artifact**
    across the whole image; the location of the point sets stripe orientation/frequency.
  - **Keep only the center** (low-pass) → a **blurry** image (loses detail).
  - **Keep only the periphery** (high-pass) → only **edges** remain.

## Links
Depends on [[mri-physics]] (gradient encoding) and connects to [[mri-contrast]] (image formation).
The reconstructed image is what enters [[fmri-preprocessing]]. Textbook: [[huettel-fmri-textbook]].
