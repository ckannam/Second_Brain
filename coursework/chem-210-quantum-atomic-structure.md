---
type: coursework-knowledge
course: CHEM 210D
unit: 1
topic: Quantum & Atomic Structure
created: 2026-08-26
---

# CHEM 210 — Quantum & Atomic Structure (Unit 1)

Knowledge note for the second block of [[chem-210]] Unit 1. Built from the [[chem-210-unit1-nuclear-quantum|lecture
slides]] (p22–43), the [[chem-210-bohr-model-handout|Bohr Model handout]], and syllabus objectives. **Mastering HW due
Sept 15.** Reading: Tro Ch. 2 §2.3–2.6 + Cox's Particle-in-a-Box handout.

## From the nucleus to the electrons
Unit 1 pivots from nuclear structure to the electron. The bridge is **spectroscopy**: atoms emit/absorb light at
discrete wavelengths (line spectra), which classical physics can't explain → the Bohr model, then quantum mechanics.

## The Bohr model (semi-classical) — see the [[chem-210-bohr-model-handout|derivation handout]]
Bohr treated the electron as orbiting the nucleus with two balanced forces:
- **Centripetal (attraction toward nucleus):** `F = Ze²/(k r²)` (Coulomb).
- **Centrifugal (outward):** `F = m v²/r`. Setting them equal: `m v²/r = Ze²/(k r²)`.
- **Quantization (Bohr's key postulate):** angular momentum is restricted — `m v r = n h / 2π` (n = 1, 2, 3…).
- Solving the two together gives the **Bohr radius** relation:
  `r = a₀ · n²/Z`, with **a₀ = 52.9 pm** (0.529 Å).
- **Energy** (total = KE + PE, with `PE = −Ze²/kr` and the virial result `E_total = −½ Ze²/kr`):
  `E = −2.18×10⁻¹⁸ J · Z²/n²`. (This is the Rydberg energy for hydrogen-like atoms.)
- **Key relationships to state (objective 1 / LO's):** deeper `n` → smaller `r`, higher `v`, more negative `E`;
  KE and PE are linked by the virial theorem (`E_total = −KE = ½·PE`). Higher Z pulls electrons in tighter (smaller r, lower E).
- Derivations themselves are **not tested** (per the Unit 1 overview), but the *relationships and the two force expressions are.*

## Why Bohr fails → wave–particle duality
Bohr works for one-electron atoms only and treats the electron as a classical particle on a fixed orbit. The fix:
- **de Broglie wavelength:** `λ = h / (m v)` — matter has wave character. Duality is "probable/observable" when λ is
  comparable to the system size (huge for electrons, negligibly tiny for macroscopic objects — a good drill: compute λ
  for an electron vs. a baseball to see why only the electron behaves as a wave).
- **Heisenberg indeterminacy:** you cannot simultaneously know an electron's position *and* momentum, so the idea of a
  definite orbit collapses. **Classical = determinacy** (definite, predictable path); **quantum = indeterminacy** — we can
  only give the **probability** of finding the electron in a region. This is the conceptual core of objective 6.

## The Schrödinger equation & wavefunctions
- **`Ĥψ = Eψ`** — Ĥ is the Hamiltonian (energy operator); solving gives allowed energies E and wavefunctions **ψ**.
- **ψ = a mathematical function describing the electron's wave nature.** It has no direct physical meaning, but:
  - **|ψ|² = probability density** (the Born interpretation) — where the electron is likely to be.
- The full 3-D form on the slides: `−(h²/8π²m)(∂²/∂x² + ∂²/∂y² + ∂²/∂z²)ψ = Eψ` (a kinetic-energy operator acting on ψ).

## Particle-in-a-box (the toy model that gives the intuition)
A 1-D box, `V=0` inside (0 to L), `V=∞` at the walls: `−(h²/8π²m)(d²ψ/dx²) = Eψ`. Standing-wave solutions give
**`E_n = n²h² / (8mL²)`**. The whole point (objective 7) is the set of proportionalities:
- **E ∝ n²** — energy rises steeply with the quantum number n.
- **E ∝ 1/L²** — a bigger box (more space for the electron) → *lower* energy. (Confinement raises energy.)
- **E ∝ 1/m** — heavier particle → lower energy.
- **Nodes:** the n-th state has **(n−1) nodes**; **more nodes → higher energy**. Nodes tie directly back to n. This node
  logic carries straight into real orbitals.

## Orbitals: quantum numbers, nodes, and shapes
Real atoms replace n alone with **four quantum numbers**:
- **n** (principal, 1,2,3…) — shell / size / energy.
- **ℓ** (angular momentum, 0…n−1) — subshell/shape: ℓ=0 **s**, 1 **p**, 2 **d**, 3 **f**.
- **mₗ** (magnetic, −ℓ…+ℓ) — orientation; gives the number of orbitals in a subshell (2ℓ+1).
- **mₛ** (spin, ±½) — electron spin.
- **Two kinds of nodes** (objective 8): **radial nodes** (spherical shells where ψ=0; count = `n − ℓ − 1`) and **angular
  nodes** (planar/conical; count = `ℓ`). **Total nodes = n − 1** — the same node/energy logic as the box.
- **Why there is no 1p orbital:** a p orbital needs ℓ=1, but for n=1 the only allowed ℓ is 0. So 1p is forbidden by
  `ℓ ≤ n−1`. (Classic conceptual question.)
- **Radial distribution curves** explain **penetration**: s-orbitals have a small inner lobe that pokes close to the
  nucleus, so an s-electron "feels" more nuclear charge than a p or d at the same n → s is lower energy / more penetrating.
  For a given n, the most-probable distance *decreases* as ℓ increases (slides: 3s vs 3p vs 3d). Sets up shielding & Z_eff.
- Visualize with **The Orbitron** (radial & angular nodes).

## Electron configurations
Fill orbitals using three rules (objective — define each; slide "Neon" example):
- **Aufbau:** fill lowest-energy orbitals first.
- **Pauli exclusion:** no two electrons share all four quantum numbers → max 2 per orbital, opposite spins.
- **Hund's rule:** singly fill degenerate orbitals (parallel spins) before pairing.
- **Valence vs core electrons** (slide: Sulfur) — valence = highest-n shell; drives chemical/physical behavior.
- **Orbital energies vary by Z** and by charge (slide: Fe vs Fe²⁺) — remove the outermost (highest-n) electrons first for
  cations; for transition metals that means the **4s electrons leave before 3d**.
- **Aufbau exceptions** (slide "Aufbau Doesn't Always Hold"): **Cr** = [Ar]4s¹3d⁵ and **Cu** = [Ar]4s¹3d¹⁰ — a half-/fully-
  filled d subshell is extra-stable. Know Cr and Cu specifically.

## Learning outcomes to self-check (from the slides)
1. Explain KE↔PE relationships from the Bohr model. 2. Relate energy to the number of nodes. 3. Write electron
configurations through Kr. 4. Identify quantum numbers for a given electron. Slide self-tests: configs for **Co, Co²⁺, Co³⁺**;
name the centripetal/centrifugal forces and which is greater (they're equal — balanced); why there's no "1g."

## Links
[[chem-210]] · [[chem-210-nuclear-chemistry]] (the nuclear→electron handoff) · [[chem-210-periodic-trends]]
(Z_eff, penetration, and shielding feed directly into trends) · [[chem-210-bohr-model-handout]] ·
sources: [[chem-210-unit1-nuclear-quantum]].
