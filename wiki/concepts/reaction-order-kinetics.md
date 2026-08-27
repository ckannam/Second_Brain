---
type: concept
created: 2026-07-30
---

# Orders of kinetics — zero-order vs first-order

The "order" of a process describes **how its rate depends on how much substrate is present**.
One question: as the amount changes, does the processing speed change with it? Foundational for
understanding drug/[[alcohol-sleep-dementia|alcohol]] metabolism (and why some things clear on a
half-life and others don't).

## First-order — a fixed *percentage* per hour
- **Rate ∝ amount present** (rate = k·[C]). More present → faster absolute clearance; less →
  slower. It self-scales.
- Gives a **constant half-life** (time to halve is the same regardless of starting amount).
- Curve: **exponential decay**.
- Machinery is **unsaturated** — spare capacity, so throughput scales with the load.
- Examples: **caffeine** (~5 h half-life), **radioactive decay** (the purest case — a fixed % of atoms decay per unit time regardless of how many remain; e.g. carbon-14, 5,730 yr; this is *where the idea of half-life comes from*), nicotine (~2 h), most medications at normal doses.
- Analogy: a store with plenty of open cashiers — more customers in, more served per hour.

## Zero-order — a fixed *amount* per hour
- **Rate is constant**, independent of amount present (rate = k). **No half-life.**
- Curve: straight **linear decline**.
- Machinery is **saturated** — enzymes already flat-out, can't go faster, so extra substrate
  just waits.
- Analogy: one cashier at max speed — 5 or 50 in line, same throughput; the line just gets longer.

## Alcohol = the classic zero-order case
Liver enzymes (alcohol dehydrogenase) saturate almost immediately, so alcohol clears at a flat
**~1 standard drink/hour** no matter the blood level. *This is why you cannot speed it up*, and
why drinking faster than ~1/hr makes alcohol **accumulate** and linger into the night's
deep-sleep clearance window (see [[alcohol-sleep-dementia]]).

**Nuance:** alcohol is first-order at very low concentrations and flips to zero-order once the
enzyme saturates (almost immediately at real drinking levels). That concentration-dependent
transition is **Michaelis–Menten kinetics**; treat alcohol as zero-order for any practical dose. Other drugs also flip to
zero-order once they **saturate** their enzymes — **aspirin** and the seizure drug **phenytoin**
(dangerous: past saturation, a small dose bump sends blood levels shooting up).

**One-liner:** first-order = a percentage per hour (a half-life); zero-order = a flat amount per
hour (a conveyor belt you can't speed up).

## In coursework
**Radioactive decay** is the textbook-pure first-order process — a fixed *fraction* of nuclei decay per unit time,
giving a constant half-life (`t½ = 0.693/k`). Worked in Cole's [[chem-210-nuclear-chemistry|CHEM 210 nuclear chemistry]]
note (activity `A = A₀e^(−kt)`, activity↔mass conversions, medical-isotope problems).

Related: [[alcohol-sleep-dementia]] · [[glymphatic-system]] · [[chem-210-nuclear-chemistry]].
