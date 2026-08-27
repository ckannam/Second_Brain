---
type: coursework-knowledge
course: CHEM 210D
unit: 1
topic: Nuclear Chemistry
created: 2026-08-26
---

# CHEM 210 — Nuclear Chemistry (Unit 1)

Knowledge note for the first block of [[chem-210]] Unit 1. Built from the [[chem-210-unit1-nuclear-quantum|lecture
slides]] (p1–21) + syllabus objectives. **Mastering HW due Sept 8.** Reading: Tro Ch. 20 §20.2–20.4, 20.6–20.8.

## The 20th-century discovery arc (why this matters)
The slides open with the experiments that revealed nuclear/atomic structure — know the *people → conclusion* chain:
- **Becquerel / the Curies (1896–1903):** uranium, then thorium/radium, spontaneously emit rays → radioactivity is
  **an atomic property of the element itself**, independent of chemical/physical state. (Marie Curie coined "radioactivity.")
- **Thomson (1897) — cathode rays:** the electron; charged particles deflect in a field per Coulomb's law `F = kq₁q₂/r²`.
- **Rutherford — gold-foil:** alpha particles mostly pass through but some deflect sharply → a tiny, dense, **positive nucleus**.
- **T.W. Richards — gravimetric analysis:** careful "weighing" of elements gave odd atomic masses → hint of **isotopes**.
- **Mass spectrometry (time-of-flight):** separates isotopes by mass/charge — e.g. Mg-24 (23.99 amu), Mg-25, Mg-26 with
  their relative abundances → explains non-integer atomic masses as **abundance-weighted averages of isotopes**.

## The nucleus and the strong force
- Protons + neutrons = **nucleons**. They're held together by the **strong nuclear force** — very strong but only
  acts over *very short* (sub-femtometer) ranges.
- **Neutrons stabilize** the nucleus: they add to the strong-force attraction but (being neutral) don't add proton–proton
  Coulomb repulsion. This is why heavier stable nuclei need proportionally *more* neutrons (see band of stability).

## Mass defect & binding energy (Einstein)
The heart of the quantitative work. A nucleus weighs **less** than its separated nucleons; the missing mass = the
energy that binds it (`E = mc²`).
- **Mass defect** `Δm = (Z·m_p + N·m_n) − m_nucleus`. (Use nuclear masses, or bookkeep electrons consistently.)
- **Binding energy** `E_b = Δm·c²`, with `c = 3.00×10⁸ m/s`. Conversion: `1 amu = 1.66×10⁻²⁷ kg` (→ `1 amu ≈ 931.5 MeV`).
- **Binding energy per nucleon** peaks near **Fe-56** — the reason fusion (light nuclei) *and* fission (heavy nuclei) both
  release energy by moving toward iron.
- Worked example from the slides — **Fe-56** (nucleus 55.921 amu; m_p 1.00728, m_n 1.008665, m_e 0.00054848 amu):
  compute Δm from 26 p + 30 n, then `E_b = Δm·c²`. (This exact problem is on slide 9 — a likely exam template.)
- **Why nuclear reactions are ~10⁶× more energetic than chemical:** chemical reactions rearrange electrons (eV scale);
  nuclear reactions change the *nucleus* and convert measurable mass to energy (MeV scale). Objective 5 wants this comparison.
- Extra-practice framing on the slides: "how long could a 100 W bulb run on the mass defect of one mole of C-14?"
  → `E = Δm·c²`, then `t = E / 100 W` (1 W = 1 J/s). Good `E=mc²`-to-macroscopic drill.

## Band of stability & why decay happens
Plot **N vs Z**. Stable nuclei cluster in a **band**; light stable nuclei sit near N≈Z, heavier ones curve to N>Z.
- **Even/even nuclei are most stable** (166 stable isotopes are even-Z/even-N; only ~6 are odd/odd) — a pairing effect.
- A nucleus decays to move *toward* the band:
  - **Above the band (too many neutrons, high N/Z):** **β⁻ decay** — a neutron → proton (raises Z, lowers N).
  - **Below the band (too many protons, low N/Z):** **positron (β⁺) emission** or **electron capture** — a proton → neutron.
  - **Very heavy (beyond Z≈83, past the band):** **α decay** — sheds a compact He-4 to lose mass/charge.

## Modes of decay — write balanced nuclear equations
Conserve **mass number A** (top) and **atomic number Z** (bottom). Slide examples:
- **Alpha (α = ⁴₂He):** ²²⁶₈₈Ra → ²²²₈₆Rn + ⁴₂He
- **Beta-minus (β⁻ = ⁰₋₁e):** ³₁H → ³₂He + ⁰₋₁e  *(n → p + e⁻; A constant, Z +1)*
- **Positron (β⁺ = ⁰₊₁e):** ²¹₁₁Na → ²¹₁₀Ne + ⁰₊₁e  *(p → n + e⁺; A constant, Z −1)*
- **Electron capture:** p + e⁻ → n (Z −1); competes with positron emission below the band.
- **Gamma (γ):** high-energy photon released as an excited nucleus relaxes; no change in A or Z.

## Fission & fusion
- **Fission:** a heavy nucleus (e.g. **U-235**) absorbs a neutron and splits into two mid-mass nuclei + several neutrons
  + energy. Slide mass-balance example: ²³⁵U + ¹₀n → (Ba + Kr) + 3 ¹₀n; reactant mass (236.05 amu) > product mass
  (235.87 amu) — the **~0.18 amu deficit is the released energy** (`E=Δm·c²`). Extra neutrons enable a **chain reaction**.
- **Fusion:** light nuclei combine (powers stars); higher energy yield per nucleon but needs enormous temperature/pressure.
- Both are driven by climbing the binding-energy-per-nucleon curve toward Fe-56.

## Kinetics of nuclear decay (first-order)
Radioactive decay is **first-order** — this is the canonical, purest first-order process (see [[reaction-order-kinetics]]).
- **Rate law:** `A = A₀ e^(−kt)`, where **activity** A = disintegrations per unit time (∝ number of nuclei N).
- **Half-life:** `t½ = ln2 / k = 0.693 / k` — **constant**, independent of how much remains (the defining feature of first-order).
- **Activity ↔ mass:** `Activity = (mass / molar mass) × N_A × k` — the slides use this to go from a required disintegration
  rate to a mass to inject.
- Worked medical examples on the slides (great exam templates):
  - **Renal binding:** need 2.4×10¹⁵ dis/s after 75 min of decay; t½ = 7.5 h, M = 114.2 g/mol → back out **initial mass to inject**
    (decay-correct the activity *up* over 75 min, then convert activity → moles → grams).
  - **Sodium-24** (t½ = 15 h, A₀ = 2.5×10⁹ d/s): fraction remaining after 4 days = `e^(−kt)` with `k = 0.693/15h`.

## Learning outcomes to self-check (from the slides)
1. Explain the significance of mass defect; use it to compute binding energy. → *Fe-56 problem.*
2. Write balanced equations for α, β⁻, β⁺, and fission. → *conserve A and Z.*
3. Define half-life; do decay kinetics calculations. → *`A=A₀e^(−kt)`, `t½=0.693/k`, activity↔mass.*

## Links
[[chem-210]] · [[chem-210-quantum-atomic-structure]] (the "nuclear → electrons" handoff) · [[chem-210-periodic-trends]] ·
[[reaction-order-kinetics]] (decay = the purest first-order case) · sources: [[chem-210-unit1-nuclear-quantum]].
