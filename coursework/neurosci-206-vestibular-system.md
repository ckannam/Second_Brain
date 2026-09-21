---
type: coursework-knowledge
course: NEUROSCI 206L
week: 5
unit: 1 (Sensation)
topic: Vestibular system (Ch 11)
created: 2026-09-21
---

# NEUROSCI 206 — Vestibular System (Week 5)

Week 5 knowledge note for [[neurosci-206]] — **Unit 1 (Sensation)**, textbook *Neuroscience* 7e **Ch 11**.
Built from the [[neurosci-206-vestibular-tutorial-notes|tutorial notes]] + [[neurosci-206-vestibular-deck|lecture
deck]] (Prof [[Leonard White]]). Follows the auditory system (Wk4) in the sensory arc and **reuses its exact
hair-cell transduction machinery** → study these two together (see [[neurosci-206-auditory-system]]). **Big idea:**
the vestibular labyrinth is an **inner-ear inertial sensor** — hair cells convert head motion + gravity into neural
signals that the brainstem/cerebellum use to **stabilize gaze and posture reflexively**, and that cortex uses to build
a conscious **sense of orientation in 3D space**.

> **Exam framing:** the deck/notes are organized around **5 Key Concepts (11.1–11.5)**. Learn each as a one-sentence
> claim, then its mechanism. The **3 study questions** at the bottom are the professor's own (answers #1 = C & E, #2 = B,
> #3 = B) — know them cold. ⚠️ **AI is banned on RAs/midterm/final** — study with this note, don't use it in assessments.

## The one-line spine (memorize the arc)
**Transduce head motion → reflexively stabilize eyes (VOR) + body (vestibulospinal) → consciously perceive orientation.**
Three-part chain: peripheral organs sense → brainstem/cerebellum act → parietal/insular cortex perceives.

## The master mechanism — one hair-cell trick, shared with hearing
Every vestibular organ uses the **identical transduction** to cochlear hair cells (see [[neurosci-206-auditory-system]] §10.3):
- Stereocilia bent **toward the tallest** (the kinocilium side) → **depolarize** → **more** neurotransmitter → afferent **fires more**.
- Bent **away** → **hyperpolarize** → less transmitter → fires less.
- Same fluids: hairs sit in **endolymph (high K⁺)**, surrounded by **perilymph (low K⁺)**; both labyrinths share the
  **otic placode** embryonic origin. The **only difference between vestibular organs is what mechanically bends the hairs.**
- Afferents leave via the **vestibular division of CN VIII**; cell bodies are **bipolar neurons in Scarpa's ganglion**
  (temporal bone) — the vestibular twin of the auditory **spiral ganglion**.

## 11.1 — The vestibular system senses position + movement in space
- **Vestibular labyrinth** = inner-ear extension that senses head motion + inertial effects of gravity. Two sensor families per side:
  - **Otolith organs** (utricle + saccule) → **static tilt + linear acceleration**.
  - **Three semicircular canals** (orthogonal) → **rotational acceleration**.
- **Hair-cell orientation is the key coding principle:** stereocilia are arranged **parallel to the direction of effective
  biomechanical motion** in each organ, so which cells fire encodes *direction*, not just "motion happened."
  - **Canals:** hairs in the ampulla all point one way → endolymph flow one direction depolarizes, opposite hyperpolarizes.
  - **Otoliths:** hairs split into **two mirror-opposed populations across the striola** → one motion depolarizes one
    subpopulation and hyperpolarizes the other.
- **Signal fate:** afferents → **vestibular nuclei** (brainstem) + **vestibulocerebellum** → adjust **postural reflexes +
  eye movements**; also ascend to **parietal/insular cortex** for conscious orientation (and, in pathology, **dizziness**).

## 11.2 — Utricle + saccule sense static tilt + dynamic linear movement (otoliths)
- **Macula** = otolith sensory epithelium: hair cells + supporting cells under a gelatinous **otolithic membrane** studded
  with **otoconia** (calcium-carbonate crystals). The crystals make the membrane **heavier than the surrounding fluid** — that mass is the whole trick.
- **Static tilt:** gravity pulls the heavy membrane, shearing it across the epithelium → **tonic** (sustained) depolarization/hyperpolarization for as long as the head is tilted.
- **Linear acceleration:** the heavy membrane **lags behind** the epithelium (which is fixed to bone) → same shearing → **phasic** signal during accel/decel.
- **Geometry (know this):** **utricle = horizontal plane** (senses horizontal-plane motion/tilt); **saccule = vertical
  plane** (up/down motion + sagittal tilts). The curved striola + curved maculae make **both** organs sensitive to **most
  directions** of linear acceleration — together they resolve the full direction.

## 11.3 — Semicircular canals sense head rotation in 3D
- **Ampulla** = bulbous canal base holding the sensory epithelium (**crista**) + a gelatinous flap (**cupula**) that the
  stereocilia poke into. The cupula **seals the canal** to endolymph flow.
- **Rotation in the canal's plane** → endolymph inertia lags → **transient force distends the cupula** away from the
  rotation → bends stereocilia → de/hyperpolarize.
- **⚠️ Canals encode ACCELERATION, not velocity.** At constant spin, endolymph "catches up" within seconds, the cupula
  relaxes to neutral, and firing returns to baseline (Fig 11.9). This is *why* sustained spinning stops feeling like
  motion — and why you feel motion again when you actually stop. **Contrast:** otoliths hold a **tonic** signal for
  constant tilt (gravity never relents); canals are **phasic**.
- **Push-pull pairs** (complementary across the two sides — the system's master principle):
  - **Left horizontal ↔ Right horizontal**
  - **Left anterior (superior) ↔ Right posterior (inferior)**
  - **Left posterior ↔ Right anterior**
  - Rotation depolarizes one member and hyperpolarizes its partner; **the brain reads the difference (balance), not absolute rate.**

## Central vestibular processing (bridges 11.3 → 11.4/11.5)
- Scarpa's ganglion central processes → **vestibular nuclei** in the **lateral tegmentum of the rostral medulla / caudal
  pons** + direct projection to the **vestibulocerebellum (flocculonodular lobe)**.
- Core jobs of the vestibular nuclei: **coordinate eye + head movements for stable fixation** (→ VOR) and **postural
  reflexes** (→ vestibulospinal). Signals also reach **parietal + insular cortex** for orientation.

## 11.4 — Vestibular + visual cues → self-motion + gaze stabilization
- **Optic flow** = the visual motion field of self-movement; combined with vestibular signal to judge self-motion.
- **VOR (vestibulo-ocular reflex):** head rotates one way → eyes **counter-rotate** the opposite way at equal speed → stable fixation.
  - **Horizontal VOR circuit (know the sides — Fig 11.10):** horizontal canal → **vestibular nucleus** → **excites the
    CONTRALATERAL abducens nucleus** → **lateral rectus** (that eye **abducts**). Abducens interneurons **cross via the MLF**
    → opposite **oculomotor nucleus** → **medial rectus** (other eye **adducts**). Simultaneous **inhibition** of the antagonist muscles.
- **Vestibular nystagmus:** rhythmic eye movement during sustained rotation = **slow phase (the VOR tracking)** + **fast
  reset phase (a saccade)**. Named by the fast-phase direction; type/direction set by the balance across the canal pair.
- **VOR gain** must be recalibrated (e.g. new glasses) to keep the image stable despite head movement.

## 11.5 — Synthesis: perception + equilibrium
- **Postural (vestibulospinal) reflexes** — the vestibular nuclei's other main output:
  - **Lateral vestibulospinal tract → IPSILATERAL extensor (anti-gravity) muscles** in trunk/legs. Jostled left → left
    lateral tract fires → left-side extensors catch you. (Ipsilateral because you push down on the side you're falling toward.)
  - **Medial vestibulospinal tract → BILATERAL upper-cervical / axial + neck muscles** — head stabilization; e.g. neck
    dorsiflexion + arm extension on superior-canal activation (protects you in a forward trip/fall).
- **Vestibular perception pathway:** vestibular nuclei → **ventral posterior complex of the thalamus (VPC)** →
  **parieto-insular vestibular cortex** + lateral somatosensory cortex near the face area. **No single dedicated "primary
  vestibular cortex"** — it's always **multimodal**, fused with vision + proprioception in **posterior parietal cortex** to build a **body schema**.
- **Autonomic hook (why you get seasick):** vestibular output reaches **medullary reticular / autonomic centers** →
  **nausea** and altered wellbeing, especially on **vestibular–visual mismatch** (motion sickness).

## Study questions (professor's own — memorize)
1. **Looking up at the night sky (head tilts back) — pick two.** → **(C)** the **superior (anterior) semicircular canals**
   on both sides were **phasically** activated during the backward tilt, **and (E)** ~**one-quarter of the saccular hair
   cells** on both sides were depolarized while the head was **held** in backward tilt. *(Canals fire on the accel of the
   tilt; the saccule — vertical plane — holds a tonic tilt signal, but only the subpopulation oriented for that direction.)*
2. **Fixate ahead, turn head right without breaking fixation — what happened?** → **(B) both eyes rotated to the LEFT** (the VOR counter-rotates the eyes opposite the head).
3. **Jostled to the LEFT on a bus, stayed standing — what helped?** → **(B) the LEFT lateral vestibulospinal tract increased its activation** (ipsilateral extensors fire on the side you're pushed toward).

## Highest-yield / most-testable
The **push-pull canal pairs**, the **horizontal VOR circuit** (abducens ↔ oculomotor via MLF), **canals = acceleration vs.
otoliths = tonic tilt**, and **lateral (ipsilateral extensor) vs. medial (bilateral neck) vestibulospinal tracts**. These
are hard to reconstruct from intuition — drill them.

## Links
Course: [[neurosci-206]] · **unit sibling + shared mechanism:** [[neurosci-206-auditory-system]] (identical hair-cell
transduction, CN VIII, endolymph/perilymph, ganglion→brainstem arc — the vestibular labyrinth is the cochlea's twin).
Anatomy vocabulary: [[neurosci-206-human-neuroanatomy]] (brainstem, thalamus, cerebellum, MLF). Broader:
[[neuroscience-of-behavior]]. Sources: [[neurosci-206-vestibular-tutorial-notes]], [[neurosci-206-vestibular-deck]].
Faculty: [[Leonard White]].
