---
type: coursework-knowledge
course: CHEM 210D
unit: 1
topic: Periodic Trends
created: 2026-08-26
---

# CHEM 210 — Periodic Trends (Unit 1)

Knowledge note for the third block of [[chem-210]] Unit 1. Built from the [[chem-210-unit1-nuclear-quantum|lecture
slides]] (p44–59) + syllabus objectives. **Mastering HW due Sept 22.** Reading: Tro Ch. 3 §3.3–3.8 + Cox's
Relativistic Effects handout. Everything here is driven by one master variable: **effective nuclear charge, Z_eff.**

## Effective nuclear charge (Z_eff) & Slater's rules
Inner electrons **shield** outer electrons from the full nuclear charge. The outer electron feels
**`Z_eff = Z − S`** (S = shielding constant). This single idea explains nearly every trend below.

**Slater's rules (from the slides) for the shielding constant S:**
1. Electrons in the **same group/shell** shield each other by **0.35** each (35%).
2. Electrons in the **(n−1) shell** shield by **0.85** each (85%).
3. Electrons in the **(n−2) shell and deeper** shield by **1.00** each (100%).
- *(For d/f electrons the rules differ slightly — electrons in shells inside a d/f electron count 1.00; know the general
  s/p version the slides give.)* Slide self-test: **Z_eff for a 3p electron in sulfur** (S, Z=16). Set up 1s²(2s2p)⁸(3s3p)⁶:
  same-shell (five other n=3) ×0.35 + n=2 (eight) ×0.85 + n=1 (two) ×1.00, so `Z_eff = 16 − S`.
- **Penetration matters** (ties to [[chem-210-quantum-atomic-structure]] radial distribution): s penetrates more than p
  more than d, so at the same n, s-electrons feel a larger Z_eff and sit lower in energy.

## Ionization energy (IE)
Energy to *remove* an electron: `X → X⁺ + e⁻`. Governed by Z_eff and n.
- **Trend:** increases **left→right** across a period (Z_eff ↑), decreases **top→bottom** down a group (n ↑, electron farther/shielded).
- **Successive IEs** rise (harder to pull from a more positive ion); a **huge jump** appears when you break into a core (noble-gas) shell.
- **Two famous anomalies to know:**
  - **Group 2→13 dip** (e.g. B < Be): removing B's 2p is easier than Be's filled 2s.
  - **Group 15→16 dip** (e.g. O < N): O must remove a *paired* 2p electron (pairing repulsion); N's half-filled 2p³ is stable.
- **Photoelectron spectroscopy (PES)** is the experimental read-out (slides): peak positions = binding energies of each
  subshell, peak areas ∝ number of electrons → confirms electron configurations and Z_eff ordering.

## Atomic & ionic radii
- **Trend:** radius **decreases** left→right (Z_eff pulls the same shell in), **increases** down a group (higher n).
- **Cations smaller** than the parent atom (lost a shell / less e⁻–e⁻ repulsion); **anions larger** (added repulsion).
- **Isoelectronic series:** same electron count → smaller radius for higher Z (more protons pulling the same electrons).

## The lanthanide contraction
Filling the **4f subshell** across the lanthanides adds poorly-shielding f-electrons, so Z_eff creeps up and radii
contract steadily. Consequence (objective): the **5d transition metals end up nearly the same size as the 4d ones
directly above them** — e.g. **Zr≈Hf**, and the Ru–Cd / Os–Hg pairs — which makes those pairs chemically very similar
and hard to separate. Sets up the relativistic-effects discussion.

## Electron affinity (EA)
Energy change when an atom *gains* an electron: `X + e⁻ → X⁻`. More negative = more favorable.
- Generally more favorable (more exothermic) toward the upper right (excluding noble gases); **halogens** are the extreme.
- Irregularities from subshell filling (e.g. group 2 and group 15 are unfavorable — filled s / half-filled p resist an extra e⁻).

## Electronegativity — three scales (the slides do "Take 1/2/3")
The tendency of a bonded atom to attract electron density. Know that **different chemists defined it differently**:
- **Pauling (χ_P):** the original; from **bond dissociation energies** — how much stronger an A–B bond is than the geometric
  mean of A–A and B–B. The most commonly tabulated scale.
- **Mulliken:** electronegativity as the **average of ionization energy and electron affinity** (energy of adding/removing charge).
- **Allred–Rochow (χ_AR):** electronegativity as an **electrostatic force** at the atom's surface, using Z_eff:
  `χ_AR = 0.359·Z_eff / r_cov² + 0.744` (covalent radius in Å, since it's a property of a bonded atom).
- All three roughly agree and rise toward F (upper right). Fluorine is the most electronegative element.

## Relativistic effects (Cox's handout topic) — Au, Hg, Tl, Pb
Extends the lanthanide-contraction logic one level deeper for the **heaviest** elements. As Z_eff gets very large, inner
(especially 6s) electrons approach relativistic speeds → their mass increases → **s-orbitals contract and stabilize**.
Consequences the slides call out:
- **Gold (Au):** the contracted 6s lowers the s–d gap into the visible → gold's **color**; and the stabilized 6s makes Au
  unusually **electronegative** (it even forms Au⁻ aurides).
- **Mercury (Hg):** the 6s² pair is so stabilized/contracted it behaves almost like a closed shell → Hg is a **liquid**,
  reluctant to bond, "acts like a noble gas."
- **Thallium & Lead — the inert-pair effect:** the 6s² pair resists ionization, so lower oxidation states are favored
  (**Tl⁺ over Tl³⁺**, **Pb²⁺ over Pb⁴⁺**); **Pb⁴⁺ is a strong oxidizer** (readily reduced to Pb²⁺). Slide data: Tl³⁺
  combined IE 5438 kJ/mol vs In³⁺ 5082 kJ/mol — the heavier element is *harder*, not easier, to triply ionize.
- Slide self-tests: most common oxidation state of **Bi** (→ +3, inert pair); why **Pb⁴⁺** reduction is favored.

## Learning outcomes to self-check (from the slides)
1. Explain IE and radii trends via Z_eff and n. 2. Compare the electronegativity scales. 3. Locate where relativistic
effects matter on the periodic table. 4. Explain the inert-pair effect. 5. Compute Z_eff with Slater's rules.

## Links
[[chem-210]] · [[chem-210-quantum-atomic-structure]] (penetration/shielding & configs feed these trends) ·
[[chem-210-nuclear-chemistry]] · sources: [[chem-210-unit1-nuclear-quantum]] (relativistic-effects + Slater slides).
