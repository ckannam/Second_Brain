---
type: coursework
term: Fall 2026
course: CHEM 210D
created: 2026-09-29
updated: 2026-09-29
---

# CHEM 210D — Midterm 1 Learning Objectives (ELI15 → Normal → Problem)

Study sheet for **[[chem-210]] Midterm 1 (Thu Oct 1)**, covering Units 1 & 2. Built from Cox's 29 stated
learning objectives, run through the **[[study-playbook]]**: each objective gets a *smart-15-year-old*
explanation, a *normal (exam-level)* explanation, and a *potential exam problem* with a short answer key
so Cole can cover the answer and self-test (Phase 3). Topic detail lives in the per-topic notes:
[[chem-210-nuclear-chemistry]] · [[chem-210-quantum-atomic-structure]] · [[chem-210-periodic-trends]] ·
[[chem-210-intermolecular-forces-phases]] · [[chem-210-salts-lattice-dissolution]] ·
[[chem-210-colligative-properties]] · [[chem-210-solubility-equilibrium]].

> **How to use:** read the ELI15, then the normal version, then *solve the problem before* looking at the
> key. If you can't, that objective isn't done. Answers are one line under each problem — cover them.

---

## Unit 1A — Nuclear Chemistry (Obj. 1–3)

### 1. Write balanced nuclear reactions for alpha, beta, and positron decay
**ELI15:** The nucleus can spit out different things. **Alpha** = it throws out a little helium chunk (2 protons + 2 neutrons). **Beta** = a neutron turns into a proton and flings out an electron. **Positron** = a proton turns into a neutron and flings out a "positive electron." The rule for balancing: the top numbers (mass) must add up on both sides, and so must the bottom numbers (charge).

**Normal:** Conserve mass number (A, top) and atomic number (Z, bottom) across the arrow.
- **Alpha (α):** emit ⁴₂He. A drops by 4, Z drops by 2. Ex: ²³⁸₉₂U → ²³⁴₉₀Th + ⁴₂He.
- **Beta minus (β⁻):** a neutron → proton + emitted electron ⁰₋₁e. A unchanged, **Z + 1**. Ex: ¹⁴₆C → ¹⁴₇N + ⁰₋₁e.
- **Positron (β⁺):** a proton → neutron + emitted positron ⁰₊₁e. A unchanged, **Z − 1**. Ex: ¹¹₆C → ¹¹₅B + ⁰₊₁e.

**Problem:** Uranium-235 (Z=92) undergoes alpha decay, then the daughter undergoes β⁻ decay. Write both balanced equations and give the final nuclide.
*Key:* ²³⁵₉₂U → ²³¹₉₀Th + ⁴₂He; then ²³¹₉₀Th → ²³¹₉₁Pa + ⁰₋₁e. Final = **²³¹₉₁Pa (protactinium-231)**.

### 2. Use the band of stability to decide beta vs positron decay
**ELI15:** Every stable nucleus has a "just right" ratio of neutrons to protons. If a nucleus has **too many neutrons**, it fixes itself by turning a neutron into a proton → **beta decay**. If it has **too few neutrons** (too many protons), it turns a proton into a neutron → **positron decay** (or grabs an electron). Compare the isotope's mass to the element's normal average mass: heavier = neutron-rich = beta; lighter = proton-rich = positron.

**Normal:** Plot N vs Z. **Above** the band (n/p ratio too high, neutron-rich) → **β⁻** (raises Z, lowers n/p). **Below** the band (n/p too low, proton-rich) → **β⁺ emission or electron capture** (lowers Z, raises n/p). Quick heuristic: if isotope mass > average atomic mass on the periodic table → likely β⁻; if < → likely β⁺/EC.

**Problem:** For each, predict decay mode: (a) ¹⁹₈O, (b) ¹³₇N. (Oxygen avg ≈ 16, nitrogen avg ≈ 14.)
*Key:* (a) O-19 is heavier than ~16 → neutron-rich → **β⁻**. (b) N-13 is lighter than ~14 → proton-rich → **β⁺ (positron)**.

### 3. Use E=mc² to find binding / fission energy
**ELI15:** A nucleus weighs *less* than its individual protons and neutrons added up. That "missing mass" got converted into the energy gluing the nucleus together (E=mc²). Bigger missing-mass-per-nucleon = more stable nucleus. In fission, products weigh slightly less than the starting nucleus, and that lost mass comes out as a huge amount of energy.

**Normal:** Mass defect Δm = (Σ masses of individual protons + neutrons) − (actual nuclear mass). Binding energy = Δm·c². For a reaction, energy released = (mass of reactants − mass of products)·c². Unit shortcut: **1 amu = 931.5 MeV**. Binding energy per nucleon peaks near **Fe-56** (Cox's flagged slide) — the reason fusion of light nuclei and fission of heavy nuclei both release energy.

**Problem:** The mass defect for ⁴₂He is 0.03038 amu. Find the total binding energy and the binding energy per nucleon.
*Key:* BE = 0.03038 × 931.5 ≈ **28.3 MeV**; per nucleon = 28.3/4 ≈ **7.07 MeV/nucleon**.

---

## Unit 1B — Bohr Model, Quantum & Orbitals (Obj. 4, 7, 8)

### 4. Centrifugal vs centripetal forces in the Bohr model
**ELI15:** Picture the electron as a ball on a string circling the nucleus. The nucleus pulls it inward (that's the attraction). For the electron to keep circling instead of flying off, that inward pull has to exactly supply the "you need this much inward force to go in a circle" amount. Balance the pull against the circling requirement and you get the allowed orbits.

**Normal:** In Bohr's model the **centripetal force** required for circular motion (mv²/r, directed inward) is *supplied by* the **Coulomb attraction** between the +nucleus and −electron (ke²/r²). ("Centrifugal" is the apparent outward tendency in the electron's frame.) Setting ke²/r² = mv²/r, combined with quantized angular momentum (mvr = nℏ), yields the discrete Bohr radii and energies. *(Cox: the derivation itself isn't tested — the force-balance concept is.)*

**Problem:** In the Bohr model, which force provides the centripetal force keeping the electron in orbit, and what happens to the required centripetal force if the orbit radius decreases?
*Key:* The **Coulomb (electrostatic) attraction** provides it; as r decreases, both the Coulomb force (∝1/r²) and the required centripetal force increase — the electron must move faster in tighter orbits.

### 7. Number of radial and angular nodes for an orbital
**ELI15:** A node is a place where the electron is never found. There are two flavors: **angular nodes** (flat planes/cones through the atom) and **radial nodes** (spherical shells, like layers of an onion). The orbital's name tells you how many of each: the letter gives angular nodes, and the number gives the total.

**Normal:** For quantum numbers n and l:
- **Angular nodes = l** (s=0, p=1, d=2, f=3).
- **Radial nodes = n − l − 1.**
- **Total nodes = n − 1.**

**Problem:** How many radial and angular nodes does a **4d** orbital have?
*Key:* n=4, l=2. Angular = **2**; radial = 4−2−1 = **1**; total = 3. ✓

### 8. Recognize orbitals / energy levels from radial and angular nodes
**ELI15:** Run the rule backwards. Count the flat planes (angular nodes) → that tells you if it's s, p, d, or f. Count the onion-shell nodes (radial), add them up with the angular ones plus one, and you get the shell number n. Now you know exactly which orbital it is.

**Normal:** Given nodes: **l = number of angular nodes** → orbital letter; **n = (radial nodes) + (angular nodes) + 1**. Higher n and higher total nodes = higher energy. Use the Orbitron visualizations to connect shapes to node counts.

**Problem:** An orbital has 2 radial nodes and 1 angular node. Identify it (n and letter).
*Key:* l=1 → **p**; n = 2 + 1 + 1 = 4 → **4p**.

---

## Unit 1C — Electron Configurations & Shielding (Obj. 5, 6, 9)

### 5. Electron configurations for transition metals and their cations
**ELI15:** Electrons fill up 4s *before* 3d when building the atom — but here's the trick everyone misses: when the atom becomes a cation, it loses the **4s electrons first**, not the 3d. Also two elements cheat for extra stability: chromium and copper steal an electron from 4s to half-fill or fill the 3d.

**Normal:** Fill 4s before 3d (Aufbau), but **ionize 4s first**. Anomalies: **Cr = [Ar]4s¹3d⁵**, **Cu = [Ar]4s¹3d¹⁰** (half-filled/filled d stability).
- Fe = [Ar]4s²3d⁶ → Fe²⁺ = [Ar]3d⁶ → Fe³⁺ = [Ar]3d⁵.

**Problem:** Write configurations for (a) Mn, (b) Co³⁺, (c) Cu⁺.
*Key:* (a) Mn = **[Ar]4s²3d⁵**; (b) Co = [Ar]4s²3d⁷, remove 4s² then one 3d → Co³⁺ = **[Ar]3d⁶**; (c) Cu = [Ar]4s¹3d¹⁰, remove 4s¹ → Cu⁺ = **[Ar]3d¹⁰**.

### 6. Use Slater's rules to calculate effective nuclear charge
**ELI15:** The outer electrons don't feel the full pull of the nucleus because inner electrons "block" some of it. Slater's rules are a scoring system: you add up how much each other electron blocks (the shielding S), subtract from the real nuclear charge, and get the "real" pull an electron feels (Z_eff = Z − S). Closer electrons block more; same-shell electrons block a little; outer electrons block nothing.

**Normal:** Z_eff = Z − S. Group orbitals: [1s][2s2p][3s3p][3d][4s4p]… For an **s/p** electron:
- same group: **0.35** each (1s: 0.30),
- n−1 shell: **0.85** each,
- n−2 and deeper: **1.00** each.
For a **d/f** electron: same group 0.35; **everything to the left counts 1.00**.

**Problem:** Calculate Z_eff for a **valence 3p electron in sulfur** (Z=16, [Ne]3s²3p⁴).
*Key:* Same group (3s3p) has 6 total, minus the electron itself = 5 × 0.35 = 1.75; n−1 (2s2p, 8 e⁻) = 8 × 0.85 = 6.80; 1s (2 e⁻) = 2 × 1.00 = 2.00. S = 10.55. Z_eff = 16 − 10.55 = **5.45**.

### 9. Why s orbitals shield outer orbitals more significantly
**ELI15:** An s electron spends part of its time *very* close to the nucleus (it can even sit right at the center) because s orbitals have no flat nodal plane blocking that region. Being close to the nucleus so often, it does a great job of standing between the nucleus and the electrons farther out — so it shields them well. p, d, f electrons avoid the center more, so they shield less.

**Normal:** **Penetration** order is s > p > d > f. s orbitals have nonzero electron density at the nucleus (no angular node at r=0), so an s electron penetrates inside the other shells and spends more time near the nucleus. This means (a) it is itself less shielded (feels higher Z_eff) and (b) it more effectively screens nuclear charge from electrons in outer orbitals. This penetration difference is *why* the ns/np/nd/nf sub-shells split in energy.

**Problem:** Explain, in terms of penetration, why the 3s electron in Na is lower in energy than a hypothetical 3p or 3d electron would be.
*Key:* 3s penetrates closest to the nucleus (density at r=0), so it feels the **highest Z_eff** and is **most stabilized/lowest energy**; 3p penetrates less, 3d least, so energy rises 3s < 3p < 3d.

---

## Unit 1D — Periodic Trends & Relativistic Effects (Obj. 10–14)

### 10. Lanthanide contraction and the role of f-orbitals
**ELI15:** As you walk across the lanthanide row, you keep adding protons, but the new electrons go into f-orbitals that are terrible at shielding. So the outer electrons feel a stronger and stronger pull, and the atoms shrink steadily. The knock-on effect: the elements *after* the lanthanides end up surprisingly small — an element like hafnium is almost the same size as zirconium right above it.

**Normal:** Across the 4f series, added 4f electrons **shield poorly** (f-orbitals are diffuse and non-penetrating), so Z_eff rises and atomic/ionic radii contract steadily. Consequence: 5d elements are much smaller than expected — **Zr ≈ Hf** in size, 5d metals are dense, and their chemistry is similar to the 4d elements above them.

**Problem:** Why are Zr⁴⁺ and Hf⁴⁺ nearly identical in ionic radius despite Hf having ~32 more electrons?
*Key:* The intervening **lanthanide contraction** (poor 4f shielding → rising Z_eff → contraction) cancels the expected size increase from the extra shell, so Hf⁴⁺ ≈ Zr⁴⁺.

### 11. The inert-pair effect for Tl, Pb, Bi
**ELI15:** These heavy elements have a pair of s electrons that get "lazy" and don't want to participate in bonding. So instead of using all their outer electrons, they hang onto that s pair, and prefer an oxidation state that's 2 lower than you'd expect from their group.

**Normal:** For heavy p-block elements, the **ns² ("inert pair")** electrons are held tightly (relativistic stabilization/contraction of the 6s orbital + poor shielding by intervening d/f), so the **lower oxidation state (group − 2)** becomes more stable: **Tl⁺ > Tl³⁺, Pb²⁺ > Pb⁴⁺, Bi³⁺ > Bi⁵⁺**. This is why PbO₂ (Pb⁴⁺) is a strong oxidizer while Pb²⁺ is stable.

**Problem:** Predict the more stable oxidation state of thallium and explain in one sentence.
*Key:* **Tl⁺** — the 6s² inert pair is relativistically stabilized and reluctant to ionize, so the +1 state (Tl³⁺ minus the s pair) is favored.

### 12. Why relativistic effects are more profound for s-orbitals
**ELI15:** Electrons in s orbitals swing *right past* the nucleus, and near a heavy nucleus with tons of protons, they get whipped up to nearly the speed of light. When something moves that fast, it effectively gets heavier (relativity), which pulls its orbital in tighter. p, d, f electrons steer clear of the nucleus, so they don't get the same speed boost.

**Normal:** s electrons have nonzero probability density *at* the nucleus and penetrate closest, so for high-Z atoms their average velocity approaches a significant fraction of c. Relativistic mass increase → the Bohr-like radius contracts → **s orbitals (and to a lesser extent p₁/₂) contract and stabilize**, while d and f orbitals expand/destabilize (better shielded from the now-tighter core). Explains gold's color, mercury's low melting point, and the inert-pair effect (Obj. 11).

**Problem:** Why does relativity contract the 6s orbital of gold much more than its 5d orbital?
*Key:* The 6s penetrates to the nucleus and reaches relativistic speeds → mass increase → contraction; the 5d has an angular node at the nucleus, low penetration, so it's barely accelerated (and actually expands as the contracted s-core shields it better).

### 13. Trends in electronegativity and ionization energy
**ELI15:** Going **across** a row (left→right), atoms pull electrons harder and are tougher to steal electrons from — because the nucleus has more protons pulling on a same-size shell. Going **down** a column, it gets easier to remove electrons and atoms pull less, because the outer electrons are farther away and shielded. A couple of small hiccups break the smooth "across" trend for ionization energy.

**Normal:** **Both increase ← across a period** (rising Z_eff, shrinking radius) **and decrease ↓ down a group** (larger radius, more shielding). Two classic **IE dips**: Be→B (2p is higher energy than 2s, easier to remove) and N→O (removing O's paired 2p electron relieves pairing repulsion). EN follows the same overall pattern; F is the most electronegative.

**Problem:** Order by first ionization energy: **B, C, N, O**. Explain any anomaly.
*Key:* B < C < O < N. Expected B<C<N<O, but **O < N**: O must lose a paired 2p electron (pairing repulsion lowers its IE below N's half-filled 2p³).

### 14. Compare the different calculations of electronegativity
**ELI15:** "Electronegativity" is one idea — how much an atom hogs electrons — but chemists measure it three different ways. One uses bond strengths, one averages how hard it is to remove vs. how much it wants to add an electron, and one uses the actual electric pull at the atom's edge. They mostly agree but come from different starting points.

**Normal:**
- **Pauling:** derived from **bond dissociation energies** (extra bond stability in A–B vs. average of A–A, B–B); a relative, dimensionless scale.
- **Mulliken:** **(IE + EA)/2** — average of ionization energy and electron affinity; ties EN directly to measurable atomic energies.
- **Allred–Rochow:** electrostatic — proportional to **Z_eff/r²**, the force the nucleus exerts on a valence electron at the covalent radius.

**Problem:** Which EN scale would you use if you only had ionization energy and electron affinity data, and how would you compute it for chlorine (IE ≈ 1251 kJ/mol, EA ≈ 349 kJ/mol)?
*Key:* **Mulliken**; EN_Mulliken ∝ (IE + EA)/2 = (1251 + 349)/2 = **800 kJ/mol** (then scaled to Pauling units).

---

## Unit 2A — Lattice Energy, IMFs & Dissolution (Obj. 15–18)

### 15. Construct a Born–Haber cycle to compute lattice energy
**ELI15:** You usually can't measure the "glue energy" of an ionic solid directly, so you build a staircase of steps you *can* measure — vaporize the metal, break the nonmetal bonds, rip electrons off, add electrons on — and use the fact that total energy around a loop is fixed (Hess's law) to solve for the one step you couldn't measure: the lattice energy.

**Normal:** Born–Haber applies **Hess's law** around a thermodynamic loop:
ΔH_f = ΔH_sublimation(metal) + ½·BE(dissociation) + IE(metal) + EA(nonmetal) + U(lattice).
Solve for **U (lattice energy)**. Watch signs: IE is +, EA is usually −, lattice-energy formation (gaseous ions → solid) is large and negative.

**Problem:** For NaCl: ΔH_f = −411, ΔH_sub(Na) = +108, ½BE(Cl₂) = +122, IE(Na) = +496, EA(Cl) = −349 (all kJ/mol). Find the lattice energy.
*Key:* −411 = 108 + 122 + 496 − 349 + U → U = −411 − 377 = **−788 kJ/mol**.

### 16. Identify the intermolecular forces present in a system
**ELI15:** Molecules stick to each other with different "stickiness." From strongest to weakest for neutral molecules: **hydrogen bonds** (H stuck to N, O, or F), **dipole–dipole** (permanently lopsided molecules), and **dispersion** (temporary lopsidedness — every molecule has this). If ions are involved, **ion–dipole** is even stronger.

**Normal:** Rank/identify: **ion–dipole** (ion + polar solvent, e.g. Na⁺ in water) > **hydrogen bonding** (H–N/O/F donor + N/O/F acceptor) > **dipole–dipole** (polar molecules) > **London dispersion** (all molecules; grows with molar mass/polarizability/surface area). Determine polarity from geometry to decide which apply.

**Problem:** List all IMFs present in (a) liquid CH₃OH, (b) liquid CO₂, (c) a solution of KBr in water.
*Key:* (a) H-bonding, dipole–dipole, dispersion; (b) **dispersion only** (CO₂ is nonpolar); (c) **ion–dipole** (K⁺/Br⁻ with water) plus water's H-bonding.

### 17. Enthalpy of dissolution from lattice energy and hydration enthalpies
**ELI15:** Dissolving a salt is a tug-of-war: it *costs* energy to pull the ions out of the crystal (break the lattice), and it *releases* energy when water wraps around the freed ions (hydration). Add the cost and the payback; if the payback wins it's exothermic, if the cost wins it's endothermic.

**Normal:** **ΔH_soln = ΔH_lattice(to separate ions, +) + ΔH_hydration(−).** Equivalently ΔH_soln = −U + ΣΔH_hyd(ions). If |hydration| > |lattice| → exothermic (ΔH_soln < 0); if lattice dominates → endothermic.

**Problem:** For KCl, lattice energy = −717 kJ/mol (so +717 to separate) and total hydration enthalpy = −701 kJ/mol. Find ΔH_soln and state exo/endothermic.
*Key:* ΔH_soln = +717 + (−701) = **+16 kJ/mol → endothermic** (cold pack behavior).

### 18. Why gas phases are used for lattice energies and hydration enthalpies
**ELI15:** To add up energies fairly, everyone needs the same starting line. **Gas-phase, isolated ions** are that starting line — they're far apart and not interacting with anything, so their energy is cleanly defined. Lattice energy is measured from gas ions → solid, and hydration from gas ions → dissolved, so the two share a reference and can be added.

**Normal:** Lattice energy is defined for **gaseous ions → crystalline solid**, and hydration enthalpy for **gaseous ions → aqueous ions**. Gas-phase ions are non-interacting (a well-defined common reference state), so the two processes connect through the same intermediate and the dissolution cycle (Obj. 17) is valid. Without the shared gas-phase reference the enthalpies couldn't be summed.

**Problem:** In one sentence, why must both lattice energy and hydration enthalpy be defined relative to gaseous ions?
*Key:* Because gaseous, isolated ions are a common non-interacting reference state that lets the two enthalpies share an intermediate and be added via Hess's law to get ΔH_soln.

---

## Unit 2B — Colligative Properties (Obj. 19–23, 25)

### 19. Define colligative properties
**ELI15:** Some properties of a solution only care about *how many* solute particles are dissolved, not *what* they are. Ten particles of salt or ten particles of sugar do the same thing. These are colligative properties.

**Normal:** **Colligative properties depend only on the number (concentration) of solute particles, not their identity:** vapor-pressure lowering, boiling-point elevation, freezing-point depression, and osmotic pressure.

**Problem:** Which affects freezing point more per mole dissolved: NaCl or glucose? Why?
*Key:* **NaCl** — it dissociates into 2 particles (i=2) vs glucose's 1, and colligative effects scale with particle count.

### 20. Vapor-phase composition via Raoult's and Dalton's laws (ideal solution)
**ELI15:** Each liquid in a mixture pushes some of itself into the vapor, and how much depends on how much of it is in the liquid and how eager it is to evaporate (Raoult). The vapor above the liquid is always **richer in the more volatile** (eager-to-evaporate) component. Dalton's law just says each gas contributes its share of the total pressure.

**Normal:** **Raoult:** P_A = x_A(liquid)·P°_A. Total P = P_A + P_B. **Dalton:** vapor mole fraction y_A = P_A / P_total. Because the more volatile component has higher P°, the vapor is enriched in it relative to the liquid.

**Problem:** A liquid is 0.50 mol-fraction each of A and B; P°_A = 100 torr, P°_B = 40 torr. Find the total pressure and the vapor mole fraction of A.
*Key:* P_A = 50, P_B = 20, P_total = **70 torr**; y_A = 50/70 = **0.71** (vapor is richer in the more volatile A).

### 21. Define the van't Hoff factor
**ELI15:** It's a multiplier that counts how many pieces one dissolved unit breaks into. Sugar stays as 1 piece; table salt splits into 2; CaCl₂ into 3. That multiplier scales up all the colligative effects.

**Normal:** **i = moles of particles in solution per mole of solute dissolved.** Ideal: NaCl i=2, CaCl₂ i=3, glucose i=1. Real i is slightly lower than ideal due to **ion pairing**. It multiplies every colligative-property formula.

**Problem:** Give the ideal van't Hoff factor for (a) K₃PO₄, (b) glucose, (c) Al₂(SO₄)₃.
*Key:* (a) **4** (3 K⁺ + PO₄³⁻); (b) **1**; (c) **5** (2 Al³⁺ + 3 SO₄²⁻).

### 22. Boiling point and freezing point of solutions (colligative)
**ELI15:** Dumping solute in makes a liquid boil at a *higher* temperature and freeze at a *lower* one. How much depends on the concentration (in molality), a constant for that solvent, and the van't Hoff multiplier.

**Normal:** **ΔT_b = i·K_b·m** (elevation, add to normal BP). **ΔT_f = i·K_f·m** (depression, subtract from normal FP). m = molality (mol solute / kg solvent).

**Problem:** Dissolve 0.50 mol CaCl₂ in 1.0 kg water (K_f = 1.86 °C/m). Find the freezing point.
*Key:* i=3, m=0.50 → ΔT_f = 3 × 1.86 × 0.50 = 2.79 °C → FP = **−2.79 °C**.

### 23. Osmotic pressure and U-tube height differences
**ELI15:** If a solution and pure water are separated by a filter that only lets water through, water flows into the solution to dilute it, pushing that side up. **Osmotic pressure** is how hard you'd have to push back to stop it — and it shows up as a height difference in a U-tube. More particles = more pressure = taller column.

**Normal:** **Π = i·M·R·T** (M = molarity, R = 0.08206 L·atm/mol·K, T in K). The pressure supports a fluid column: **Π = ρgh**, so the U-tube height difference **h = Π/(ρg)**.

**Problem:** A 0.010 M glucose solution at 300 K — find Π, then the water-column height it supports (ρ = 1000 kg/m³, g = 9.8).
*Key:* Π = 1 × 0.010 × 0.08206 × 300 = **0.246 atm** ≈ 2.49 × 10⁴ Pa; h = 24900/(1000 × 9.8) ≈ **2.5 m**.

### 25. Enthalpy vs entropy for solutions versus pure solvents
**ELI15:** Adding solute makes a liquid *more disordered* (higher entropy) than the pure solvent. Nature likes disorder, so the solution "wants" to stay liquid more — that's why it's harder to freeze (you're taking away disorder) and its vapor pressure drops. The freezing/boiling shifts are really an entropy story.

**Normal:** Dissolving solute **raises the entropy** of the liquid relative to pure solvent, lowering the solvent's **chemical potential**. This is the thermodynamic root of colligative effects: the lowered solvent chemical potential depresses vapor pressure and freezing point and elevates boiling point. Enthalpy of solution (Obj. 17) governs *whether it dissolves and heat flow*; the entropy increase governs *the colligative shifts*.

**Problem:** Using entropy, explain why a solution freezes below the pure solvent's freezing point.
*Key:* The solution's higher entropy lowers the solvent's chemical potential, so the liquid stays favored to a lower temperature; you must cool further (remove more entropy) before solid and liquid chemical potentials equalize.

---

## Unit 2C — Solubility Equilibrium & Thermodynamics (Obj. 24, 26–29)

### 24. Use Ksp to compute molar solubility
**ELI15:** For a barely-soluble salt, Ksp is a number describing how much dissolves. Call the amount that dissolves "s," write out the ions it makes, plug into the Ksp expression, and solve for s. Watch the coefficients — they become exponents and multipliers.

**Normal:** For **AB → A + B**: Ksp = s². For **AB₂ → A + 2B**: Ksp = (s)(2s)² = 4s³. General **AₓBᵧ**: Ksp = (x·s)ˣ(y·s)ʸ.

**Problem:** Ksp of PbCl₂ = 1.6 × 10⁻⁵. Find its molar solubility.
*Key:* PbCl₂ → Pb²⁺ + 2Cl⁻; Ksp = 4s³ → s³ = 4.0 × 10⁻⁶ → s = **1.6 × 10⁻² M**.

### 26. Use Q and K to judge equilibrium / spontaneity
**ELI15:** Q is a "snapshot" of where a reaction is right now; K is where it wants to end up. If Q is smaller than K, the reaction runs forward (spontaneous). If Q is bigger, it runs backward. If they're equal, it's at rest (equilibrium).

**Normal:** Compare Q to K: **Q < K → forward spontaneous (ΔG < 0)**; **Q = K → equilibrium (ΔG = 0)**; **Q > K → reverse spontaneous (ΔG > 0)**. Quantitatively **ΔG = ΔG° + RT ln Q** and **ΔG° = −RT ln K**.

**Problem:** A reaction has K = 10. At a moment Q = 100. Which direction is spontaneous, and is ΔG positive or negative?
*Key:* Q > K → reaction proceeds in **reverse**; ΔG = RT ln(Q/K) = RT ln(10) > 0 → **ΔG positive**.

### 27. Determine whether a precipitate forms (Q vs Ksp)
**ELI15:** When you mix two solutions, calculate the "ion product" Q for the possible solid using the diluted concentrations after mixing. If Q is bigger than Ksp, there's more dissolved than can stay dissolved, so a solid crashes out. If Q is less, everything stays dissolved.

**Normal:** Compute **Q = ion product** using concentrations **after mixing (account for dilution)**. **Q > Ksp → precipitate forms**; **Q = Ksp → saturated, on the edge**; **Q < Ksp → no precipitate**.

**Problem:** Mix 50 mL of 0.0020 M Pb(NO₃)₂ with 50 mL of 0.0020 M NaCl. Ksp(PbCl₂) = 1.6×10⁻⁵. Precipitate?
*Key:* After mixing (2× dilution): [Pb²⁺] = 0.0010, [Cl⁻] = 0.0010. Q = (0.0010)(0.0010)² = 1.0 × 10⁻⁹ ≪ Ksp → **no precipitate**.

### 28. Molar solubility in the presence of a common ion
**ELI15:** If the solution already contains one of the salt's ions, the salt dissolves *less* (Le Châtelier pushes back). Set up the Ksp expression but start with that ion's concentration already present, and the salt's solubility comes out much smaller.

**Normal:** **Common-ion effect** suppresses solubility. Set up the ICE/Ksp with the pre-existing ion concentration; the added-ion term is dominated by the initial amount, so you can often approximate it as constant.

**Problem:** Find the molar solubility of AgCl (Ksp = 1.8×10⁻¹⁰) in **0.10 M NaCl**.
*Key:* Ksp = [Ag⁺][Cl⁻] ≈ s(0.10) → s = 1.8×10⁻¹⁰/0.10 = **1.8 × 10⁻⁹ M** (vs 1.3×10⁻⁵ in pure water — far less).

### 29. Graphically depict relationships between equilibrium, Q, G, and G°
**ELI15:** Imagine a valley: as a reaction proceeds, its free energy G drops to a lowest point and then would rise again — that lowest point *is* equilibrium. The slope of the valley at any spot is ΔG. Where you are along the valley sets Q; the bottom is where Q = K and ΔG = 0. Whether the valley bottom sits toward products or reactants is set by ΔG°.

**Normal:** Plot **G vs. reaction progress (extent ξ)**: a curve with a **minimum at equilibrium**. The **slope = ΔG** (negative left of min → forward spontaneous; positive right of min → reverse). At the minimum **Q = K, ΔG = 0**. **ΔG = ΔG° + RT ln Q**; a **negative ΔG°** shifts the minimum toward products (K>1), positive ΔG° toward reactants (K<1). ΔG° is the difference between pure-products and pure-reactants ends of the curve.

**Problem:** On a G-vs-reaction-progress plot, mark where ΔG = 0, where Q < K, and how the curve differs for ΔG° < 0 vs ΔG° > 0.
*Key:* ΔG = 0 at the **minimum** (Q=K); **Q < K** is left of the minimum (downhill/forward); ΔG° < 0 puts the minimum **near the products side** (K>1), ΔG° > 0 puts it **near the reactants side** (K<1).

---

## Self-check before the exam
Cover the answer keys and re-derive each. You're done with an objective when you can (1) give the ELI15 out
loud, (2) state the governing equation/rule, and (3) solve its problem cold. Weakest-first per Cox's flagged
templates: Born–Haber (15), Slater Z_eff (6), nodes (7–8), Raoult/Dalton (20), Ksp + common-ion (24/28),
Q-vs-K precipitation (27). Links back: [[chem-210]] · [[study-playbook]].
