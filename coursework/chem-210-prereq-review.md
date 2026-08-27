---
type: coursework-knowledge
course: CHEM 210D
unit: 0 (prereq review)
topic: Stoichiometry & Gas Laws
created: 2026-08-26
---

# CHEM 210 — Prereq Review: Stoichiometry & Gas Laws

**Discussion I** review of Chem 101/110 prereq skills — *assumed knowledge*, not new CHEM 210 content. The point is
to have these cold for closed-book exams. Raw worksheet: `raw/Processed/CHEM 210 Discussion 1 - Stoichiometry Review.pdf`.
Part of [[chem-210]]. Worked solutions below (done 2026-08-26).

## The prereq methods to have automatic
- **Limiting reagent:** convert every reactant to moles, divide each by its coefficient; the **smallest** value limits.
  Everything (product amount, leftover reactant) flows from the limiting reagent.
- **Leftover reactant:** moles reacted = (limiting moles) × (excess-coeff / limiting-coeff); leftover = initial − reacted.
- **Ideal gas law:** `PV = nRT`, R = 0.08206 L·atm·mol⁻¹·K⁻¹. **Always T in kelvin** (K = °C + 273.15). Use to go
  between moles of a gas and its measured V, P, T.
- **Molarity:** mol = M × V(L).
- **Formula from a mole ratio (empirical/oxidation-state logic):** for `Mn + x HCl → MnClₓ + (x/2)H₂`, the H₂:metal
  mole ratio pins x (electrons lost by metal = electrons gained making H₂).
- **% composition / source purity:** usable mass = total mass × mass-fraction (e.g. Al in a soda can).

## Worked solutions (Discussion I)

### 1 — Alum synthesis · `2 Al + 2 KOH + 4 H₂SO₄ + 22 H₂O → 2 K[Al(SO₄)₂]·12H₂O + 3 H₂`
**(a) Max H₂ volume + leftover Al** — reactants: Al 2.33 g = 0.0864 mol; KOH 0.028 L×0.88 = 0.0246 mol;
H₂SO₄ 0.031 L×0.65 = 0.0202 mol. Divide by coefficients → Al 0.0432, KOH 0.0123, **H₂SO₄ 0.00504 (limiting)**.
- H₂ (4:3 to H₂SO₄): n = 0.0202×¾ = 0.01511 mol → V = nRT/P = (0.01511)(0.08206)(298) = **0.370 L H₂ (≈370 mL)**.
- Al used (Al:H₂SO₄ = 2:4): 0.0202×½ = 0.01008 mol = 0.272 g → **2.06 g Al remains** (of 2.33 g).

**(b) Soda cans for ≥4.5 kg alum** (Al excess elsewhere) — M(alum) = **474.4 g/mol**; n = 4500/474.4 = 9.49 mol;
Al is 1:1 with alum → 256 g Al needed. Al/can = 15.0 g × 0.937 = 14.06 g → 256/14.06 = 18.2 → **round up to 19 cans**.

### 2 — Formula of MnClₓ · `Mn + x HCl → MnClₓ + (x/2)H₂`
n(Mn) = 2.747/54.94 = 0.0500 mol; n(H₂) = PV/RT = (0.951)(3.22)/[(0.08206)(373)] = 0.1000 mol.
H₂:Mn = 2.0 = x/2 → **x = 4 → MnCl₄**. *(Clean by design; real Mn–Cl chemistry favors MnCl₂ — this is a pure
mole-ratio formula drill, so trust the math but don't read MnCl₄ as a stable species.)*

### 3 — Liquid O₂ vaporizing in the stomach · `PV = nRT`
mass = 0.050 mL × 1.14 g/mL = 0.0570 g → n = 0.0570/32.00 = 0.001781 mol; T = 37 °C = 310 K.
V = nRT/P = (0.001781)(0.08206)(310) = **0.0453 L ≈ 45 mL** (~900× expansion — why swallowing liquid O₂ is dangerous).

**Answers:** 1a) 0.370 L H₂, 2.06 g Al · 1b) 19 cans · 2) MnCl₄ · 3) ≈45 mL.

> Fun tie-in: Problem 1's **alum in shaving cream** (styptic — stops bleeding from nicks) is literally Cole's
> **Shave & Buzz** domain.

## Links
[[chem-210]] · gas laws resurface in [[chem-210-nuclear-chemistry]] (activity/volume) and Unit 2 solubility.
This is prereq; the first *new* CHEM 210 unit is [[chem-210-nuclear-chemistry|Unit 1: Nuclear]].
