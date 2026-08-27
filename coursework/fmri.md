---
type: coursework
term: Fall 2026
course: Functional Neuroimaging (NEUROSCI 382 / PSY 303)
created: 2026-07-25
updated: 2026-08-26
---

# fMRI (Functional Neuroimaging) — Senior Fall 2026

Part of [[coursework/index|Senior Fall]] · [[Duke]]. ✅ **Syllabus + Weeks 1–5 materials ingested**
(2026-08-26). Source pages: [[fmri-syllabus-fall2026]], [[fmri-week1-lecture-intro]], textbook
[[huettel-ch1-intro-to-fmri]] / [[huettel-ch2-mri-scanners]], labs [[fmri-lab1-neuroanatomy]] /
[[fmri-lab2-kspace-contrast]] / [[fmri-lab3-preprocessing]].

## Course info
- **Code / title:** NEUROSCI 382 / PSY 303 — Functional Neuroimaging
- **Meets:** **Tuesdays 3:05–5:45 PM**, Perkins LINK 088 (Classroom 4) — two periods (lecture + lab)
  with a ~10-min break.
- **Professor:** [[Tobias Overath]] (LSRC B248A · OH Tue 8:30–9:30 AM · t.overath@duke.edu · 919-684-6146)
- **TA:** [[Hector Sanchez Melendez]] (DIBS Cube M057 · OH Thu 2–3 PM · hector.sanchezmelendez@duke.edu)
- **Textbook:** [[huettel-fmri-textbook|Huettel, Song & McCarthy — *fMRI*, 3rd ed. (2014)]]
- **Software:** MATLAB (2026b or earlier, no toolboxes) + **[[spm|SPM]]** — *bring laptop to lab.*
- **Grading:** Midterm I **30%** · Midterm II **30%** · Project **30%** · Labs & Quizzes **10%**.
- ⚠️ **AI policy:** generative-AI writing tools are **prohibited on the project write-up** (grammar
  checkers only). See [[fmri-syllabus-fall2026]]. No-tech classroom; attendance mandatory (>5 misses ≈ fail).

## The material — full understanding here
The [[fmri]] concept cluster (build/review from these):
- **[[mri-physics]]** — spins, resonance, B₀, RF & gradient coils, scanner components, safety (Ch 2–3).
- **[[mri-contrast]]** — contrast (anatomical/functional/CNR) & resolution (spatial/temporal/functional),
  T1/T2/T2\*, TR/TE (Ch 4–5).
- **[[k-space]]** — spatial-frequency domain, Fourier reconstruction, EPI vs spiral (Ch 4).
- **[[bold-signal]]** — oxy/deoxy-Hb, neurovascular coupling, the sluggish HDR (Ch 6–7).
- **[[fmri-preprocessing]]** — realign → slice-time → coregister → segment → normalize → smooth (Ch 8).
- **[[fmri-glm-analysis]]** — GLM, 1st/2nd-level, contrasts, multiple comparisons (Ch 10–11).
- **[[neuroanatomy-landmarks]]** · **[[mni-space]]** — localizing & standardizing activations.
- Facility & tools: **[[biac]]** (Duke 3 T scanner) · **[[spm]]** (analysis software).

## Assignments & HW tracker
**Readings** (do *before* each Tuesday lecture — they're dense):
- [x] Week 1 (Aug 25) — Ch 1 & 2 (Intro; scanners) → [[huettel-ch1-intro-to-fmri]] / [[huettel-ch2-mri-scanners]]
- [ ] Week 2 (Sep 1) — Ch 3 MR Physics (focus on **Conceptual Path**)
- [ ] Week 3 (Sep 8) — Ch 4 (both Conceptual & Quantitative paths, *ignore equations*) & Ch 5
      (*exclude* "Motion Contrast", "Signal recovery…", "Parallel imaging")
- [ ] Week 4 (Sep 15) — Ch 6 (neuronal→hemodynamic) & Ch 7 (BOLD fMRI)
- [ ] Week 5 (Sep 22) — Ch 8 (Signal, Noise & Preprocessing)
- [ ] Week 7 (Oct 6) — Ch 9 (Experimental Design)
- [ ] Week 9 (Oct 20) — Ch 10 (Basic Statistical Analyses)
- [ ] Week 10 (Oct 27) — Ch 11 (Advanced Statistical Analyses)
- [ ] Week 11 (Nov 3) — Bem, *Writing the Empirical Journal Article*

**Labs** (10% with quizzes; SPM/MATLAB):
- [ ] Lab 1 (Sep 1) — Intro to Neuroanatomy → [[fmri-lab1-neuroanatomy]]
- [ ] Lab 2 (Sep 8) — k-Space & Contrast → [[fmri-lab2-kspace-contrast]]
- [ ] Lab 3 (Sep 22) — Preprocessing → [[fmri-lab3-preprocessing]]
- [ ] Lab 4 (Oct 20) — 1st-level Analysis
- [ ] Lab 5 (Nov 3) — 2nd-level Analysis (+ task programming if needed)
- [ ] Labs (Nov 10 / 17 / 24) — Project analysis sessions

**Exams:**
- [ ] **Midterm I** — Tue **Sep 29** (Weeks 1–5: physics → BOLD → preprocessing) — 30%
- [ ] **Midterm II** — Week 15, early **Dec** (design, analysis, clinical) — 30%

**Group project (30%)** — form a group of 4; design → program → scan at [[biac|BIAC]] → analyze:
- [ ] Meet Prof. [[Tobias Overath]] in **office hours Weeks 6 & 8** to discuss the project
- [ ] Design study + program experiment (with Overath's guidance)
- [ ] **Proposal presentation** — Week 10, Tue **Oct 27** (2 group members present)
- [ ] **Acquire data** at BIAC — start **~Nov 3**; **all data collected before class Tue Nov 17**
      (two 2-hour scan sessions, ~2 participants; ~$640/hr — scripts must work first!)
- [ ] **Results presentation** — last class, early Dec (other 2 members)
- [ ] **Individual write-up (~3000 words)** — due **Tue Dec 8, 11:59 PM** (Canvas + email). *No AI.*

## Key dates
- **Sep 29** — Midterm I · **Oct 13** — Fall Break (no class) · **Oct 27** — project proposals ·
  **Nov 17** — data-collection deadline + clinical-fMRI guest lecture ([[Jim Voyvodic]]) ·
  **early Dec** — Midterm II + results presentations · **Dec 8** — write-up due.
- ⚠️ Syllabus lists the final class as "TH 4 Dec" though the class otherwise meets Tuesdays — confirm
  the exact Week-15 date in class.

## Resources
- Textbook: [[huettel-fmri-textbook]] (companion site sites.sinauer.com/fmri3e).
- Software: [[spm|SPM]] (`fil.ion.ucl.ac.uk/spm`), MATLAB; viewer alt. MRIcron.
- **Lab dataset** (Cole's `Data/` folder — blocked finger-tapping, `bia5_20105_*`): kept at
  `/Users/colekannam/Downloads/Data` (~486 MB, *not* in the vault). Details in [[fmri-lab1-neuroanatomy]].
- Scanning facility: [[biac|BIAC]].

## Next
- [ ] Do Week 2 reading (Ch 3) + Lab 1 — I can walk through the SPM steps and the Q6 landmark coords.
- [ ] Form the project group and start brainstorming a study (Week 4 is the brainstorming session).
