---
type: coursework-knowledge
course: NEUROSCI 206L
week: 4
unit: 1 (Sensation)
topic: Auditory system (Ch 10)
created: 2026-09-14
---

# NEUROSCI 206 — Auditory System (Week 4)

Week 4 knowledge note for [[neurosci-206]] — **Unit 1 (Sensation)**, textbook *Neuroscience* 7e **Ch 10**.
Built from the [[neurosci-206-auditory-tutorial-notes|tutorial notes]] + [[neurosci-206-auditory-deck|lecture
deck]] (Prof [[Leonard White]]). Follows the visual system (Wk3) in the sensory arc; the anatomical vocabulary
comes from Wk1 [[neurosci-206-human-neuroanatomy]]. **Big idea:** the auditory system *transduces sound
waves into distinct patterns of neural activity* that are integrated with other senses to guide behavior.

> **Exam framing:** the deck/notes are organized around **9 Key Concepts (10.1–10.9)**. Learn each concept as a
> one-sentence claim, then its mechanism. The 5 study questions at the bottom are the professor's own — know them cold.
> ⚠️ **AI is banned on RAs/midterm/final** — use this note to *study*, not during assessments. See [[neurosci-206]].

## The 8-step signal flow (memorize the arc)
1. Sound collected + amplified by **external + middle ear** → transferred to inner ear.
2. **Inner ear decomposes** complex waves into sinusoidal components (frequency, amplitude, phase) encoded in receptor firing.
3. **Tonotopy** (systematic map of frequency) is preserved from cochlea through every central station.
4. **Brainstem** splits info into parallel pathways; some **compare the two ears** → sound localization.
5. Brainstem → **midbrain (inferior colliculus)** → **auditory thalamus (MGC)**.
6. **Auditory cortex** processes complex features (e.g. speech).
7. Every stage has **feedback** ("higher"→antecedent) + **binaural integration**.
8. Like all senses, hearing uses **active mechanisms** to shape the incoming signal.

## 10.1 — Sound is a pressure wave of many frequencies
- Sound = spherical **pressure waves** from vibrating air molecules; characterized by **amplitude (loudness)**,
  **frequency (pitch)**, **phase (temporal displacement)**.
- **Pitch / loudness / timbre** are the three perceptual attributes. Timbre = quality that distinguishes a violin
  from a voice at the same pitch/loudness (from the mix of harmonics).
- Natural sounds (speech, music, birdsong) are **acoustically complex** → decomposed by **Fourier analysis** into a
  **power spectrum** / **spectrogram** (frequency × time × power).
- Human hearing range: **20 Hz – 20 kHz**.

## 10.2 — The ear filters frequencies + transmits air→fluid
**Three divisions** (know each structure's job — Figure 10.4):
- **External ear** (pinna, concha, auditory meatus): gathers/focuses sound onto the **tympanic membrane**; the
  pinna's shape **filters frequencies → spectral cues for localization** (see 10.8).
- **Middle ear** (tympanic membrane + **ossicles**: malleus→incus→stapes): transmits acoustic energy air→inner ear
  and **amplifies pressure ~200-fold** (impedance matching — overcomes the air-to-fluid energy loss). Stapes pushes on the **oval window**.
- **Inner ear** (**cochlea** + auditory nerve). Two jobs: **(a) biomechanical** — decompose sound into sinusoids;
  **(b) neural transduction** — convert mechanical energy to neural signals.

**Cochlea anatomy** ("snail," Figure 10.5): coiled, bone-encased; **cochlear partition** bisects it into
**scala vestibuli** and **scala tympani** (both **perilymph**, low K⁺). The partition holds:
- **Organ of Corti** = **basilar membrane** + **tectorial membrane** + hair cells.
- **Inner hair cells (IHCs)** = the true **sensory receptors** (source of auditory input to brain).
- **Scala media** = third channel with **endolymph (high K⁺, +80 mV)** — the ionic environment that powers transduction.
- **Helicotrema** = apical opening where scala vestibuli & tympani connect.

**Pressure path:** stapes → oval window bulges in → perilymph wave through scala vestibuli → around helicotrema →
scala tympani → relieved by **round window** bulging out → sets up a **traveling wave** on the basilar membrane.

**Basilar membrane frequency tuning (tonotopy at the source — Figure 10.6):**
- **Base** = stiff, thick, narrow → tuned for **high frequencies**.
- **Apex** = flexible, thin, wide → tuned for **low frequencies**.
- A complex sound vibrates the place matched to each component frequency. Tuning is **sharpened by an active process** (outer hair cells → 10.4).

## 10.3 — Transduction by cochlear hair cells
- **Stereocilia** of hair cells project into **endolymph** (high K⁺). Basilar-membrane vibration → **shearing motion**
  between basilar and tectorial membranes → bends stereocilia.
- **Bend toward the tallest stereocilium** → **tip links** open **K⁺ channels** → K⁺ influx → **depolarization** →
  Ca²⁺ entry → **more neurotransmitter** → **↑ firing** in the auditory nerve.
- **Bend away** → channels close → **hyperpolarization** → **less transmitter** → **↓ firing**.
- Note the counterintuitive ionic logic: K⁺ flows *in* (not out) because endolymph is high-K⁺ at +80 mV vs. the hair
  cell's −45 mV — a large electrochemical driving force.

**Sensory coding in the auditory nerve (CN VIII):**
- **Temporal code (phase-locking):** receptor/action potentials follow the stimulus waveform up to **~3 kHz**.
- **"Labeled-line" (place) code:** each afferent fiber inherits the **tuning of the basilar-membrane spot it
  innervates** → frequency encoded by *which* fiber fires. This is the anatomical basis of **tonotopy in CN VIII**.

## 10.4 — Active mechanisms (outer hair cells + middle-ear muscles)
**Why active forces are needed** (evidence): (1) tuning curves are **too sharp** for passive mechanics; (2) at very
low sound levels the basilar membrane vibrates **more than expected**; (3) the ear can **emit sound** →
**otoacoustic emissions** (used clinically for newborn hearing screening).

- **Outer hair cells (OHCs) = the cochlear amplifier.** They are **motile** (cell bodies expand/contract). Their
  stereocilia are embedded in the tectorial membrane, so their movement **modulates the shearing force** and
  **amplifies the basilar-membrane response to faint sounds**. OHCs receive **efferent** innervation from the
  brainstem via CN VIII → **CN VIII is not purely sensory**.
- **Middle-ear muscles** (Figure 10.4): **tensor tympani** (damps malleus) + **stapedius** (damps stapes). Roles:
  protect against **very loud sounds** (acoustic reflex), reduce responsiveness to **self-generated sound** (own speech),
  and possibly **link hearing to gaze** — *fun fact: your eardrums move when your eyes move* (Gruters et al. 2018, PNAS).

## 10.5 — Central pathway (bilateral, feedforward + feedback)
Ascending chain (Figure 10.12) — **know the order and side**:
- **1st-order:** **spiral ganglion** cells (bipolar) — peripheral process → IHCs; central process → **cochlear nuclei** at the pontomedullary junction.
- **2nd-order:** **cochlear nucleus** → projects to multiple bilateral targets:
  - **Nucleus of the lateral lemniscus** (upper pons) — *monaural* (presence/timing from one ear).
  - **Superior olivary complex** (mid-pons, **bilateral**) — **binaural**, localizes sound:
    - **MSO (medial superior olive):** **interaural TIMING differences** → **low-frequency** localization (well-developed in humans).
    - **LSO (lateral superior olive):** **interaural INTENSITY differences** → high-frequency (vestigial in humans); uses **MNTB** inhibitory interneuron.
- **Inferior colliculus** (midbrain): **convergence point** — all lower projections converge; a **complete map of auditory space** is computed.
- **Auditory thalamus:** **medial geniculate complex (MGC)** — first station with pronounced selectivity for
  **spectral + temporal combinations** of sound.
- **Auditory cortex** (see 10.6). At every stage: **descending feedback** + **binaural integration**.

## 10.6 — Auditory cortex + perceptual synthesis
- Target of MGC = **primary auditory cortex** on the **superior temporal lobe** (**Heschl's / first transverse gyrus**).
- Organization (Figure 10.13): **"core"** (primary, tonotopic input from MGC, maps binaural interactions) surrounded
  by a **"belt"** of higher-order areas.
- **Asymmetry (structure + function):**
  - Posterior belt = **Wernicke's area** → **language reception / speech comprehension**; left-lateralized in
    **>99% of right-handers, >90% of left-handers**.
  - Structural correlate = **planum temporale** (larger on left in most people; even larger asymmetry in people with **perfect pitch**).
  - Functional: **right hemisphere > left for music**; **left > right for speech + environmental sounds**; both participate in all.
- **Semantic maps:** speech-listening vs. reading produce **similar cortical semantic maps** (Huth et al. 2016, *Nature*).
  Music is a powerful whole-brain modulator (perception + action + emotion networks; Vuust et al. 2022).

## 10.7 — Frequency coding: resonance vs. synchrony
Two complementary codes (recap of 10.2–10.3):
- **Place / resonance code:** frequency = **where** on the basilar membrane (→ which labeled-line fiber). Dominates at **high frequencies**.
- **Temporal / synchrony code:** frequency = **timing** of phase-locked firing. Works up to **~3 kHz** (low frequencies).
- **Key puzzle:** neither alone explains full pitch perception across the whole range — they overlap and combine.

## 10.8 — Sound localization (three cues — Figure 10.16)
- **Interaural TIMING difference (ITD):** sound reaches near ear first → **MSO** → best for **low frequencies**.
- **Interaural LEVEL/intensity difference (ILD):** head casts an **acoustic shadow** → far ear quieter → **LSO** →
  best for **high frequencies** (short wavelengths are blocked by the head).
- **Spectral cues:** the **pinna** filters frequencies differently by elevation/front-back → resolves the
  **cone-of-confusion** (up/down, front/back) that ITD+ILD can't.

## 10.9 — Hearing × vision (intersensory integration)
- **McGurk effect:** seeing lips say /ga/ + hearing /ba/ → perceive /da/. Vision **overrides** audition for speech;
  disruptable with **TMS to lateral temporal cortex** ~0 ms after auditory onset.
- **Coordinate-frame problem (Figure 10.19):** auditory space is **head-centered** (ears fixed); visual space is
  **retinotopic** and the eyes move (~40° in the orbits) → the brain must **account for eye position** to align them.
- **Receptive fields differ:** visual RFs are small/bounded; auditory RFs are **large** (up to a whole hemifield).
- How the brain fuses them for localization is **still unsolved** — likely both subcortical (superior/inferior colliculi)
  and cortical (temporal/parietal association) processing.

## Study questions (professor's own — memorize)
1. **Primary function of the three middle-ear bones?** → **Amplification of sound pressure to increase sensitivity** (C).
2. **Most accurate about hair-cell transduction?** → **Firing of 2nd-order neurons can be up- OR down-regulated depending on which way the cilia bundle bends** (D).
3. **What explains tonotopy in CN VIII?** → **The location where the fiber's peripheral process contacts hair cells along the basilar membrane** (C) — i.e., the labeled-line/place code.
4. **Which most depends on bilateral (two-ear) info?** → **Sound localization** (B).
5. **First structure with selectivity for spectral+temporal combinations?** → **Medial geniculate complex (MGC)** (F).

## Links
Course: [[neurosci-206]] · **mechanism twin:** [[neurosci-206-vestibular-system]] (Wk5) — the vestibular labyrinth
uses the **identical hair-cell transduction** taught here in §10.3 (bend toward tallest → K⁺-influx depolarization;
endolymph/perilymph; CN VIII; ganglion→brainstem arc), just driven by head motion instead of sound. Study the two
together. · unit sibling: [[neurosci-206-human-neuroanatomy]] (Wk1 anatomy vocabulary — temporal
lobe, brainstem, thalamus). **fMRI overlap:** [[neuroanatomy-landmarks]] (Heschl's gyrus = primary auditory cortex;
inferior colliculus = subcortical auditory station) — the same landmarks 206 teaches functionally. Broader:
[[neuroscience-of-behavior]]. Sources: [[neurosci-206-auditory-tutorial-notes]], [[neurosci-206-auditory-deck]].
Faculty: [[Leonard White]].
