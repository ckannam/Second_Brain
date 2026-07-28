---
type: improvement-plan
target: networking outreach engine ([[outreach-pipeline]] + [[outreach-kit]])
created: 2026-07-27
status: local-steps-1-4-executed (2026-07-27); step 5 @cloud + step 7 @human parked on board
---

## Executed 2026-07-27 (local steps 1–4)
- **1 ✅ Closed loop:** runbook now reconciles `drafted/sent` rows via Gmail `search_threads`
  (reply → `replied`; 7–10-day rule fires follow-ups).
- **2 ✅ Warm-lead harvest:** iMessage career-signal scan run → **Warm-leads queue** added to
  [[outreach-pipeline]] with 2 real candidates ("Vishwas Aunt" connector w/ Forus ties; Uncle Tom →
  Chai Discovery). Method re-found Arielle + Sean (validated). Made a repeatable runbook step.
- **3 ✅ Assets wired:** kit's "résumé look" ask → real `Cole_Kannam_Resume.pdf`; **`networking-prep`
  skill installed** to `.claude/skills/` (Tier 1 briefs generate in-session).
- **4 ✅ PIKE roster mined:** parsed the full ~1,900-person PDF (pdfplumber) → **NY/DC Tier-2
  expansion** on the board. Caveat recorded: email column garbles on auto-extract → pull addresses
  from the source PDF at draft time; no grad-year field → verify recency.
- **Remaining:** step 5 (@cloud target-org map — now also seed **Chai Discovery**), step 6 (reply-rate
  scoreboard, local — deferred), step 7 (@human confirm inputs). See `tasks/index.md`.

# Improve — the networking outreach engine

**Target:** the [[outreach-pipeline]] + [[outreach-kit]] + "run the outreach batch" workflow
(see [[Job Search]]). **Vision:** a *self-improving* "network like crazy" machine — closed-loop,
richly supplied, directed at real target orgs, and measured — not a static hand-kept board.

## Diagnosis (gap to vision)
Currently an **open loop with a thin, manual supply**: no Gmail read-back (follow-up rule never
fires), only 6+8 seeded contacts while the ~1,000-name PIKE PDF and 378-person CRM sit un-mined,
no target-org map, no reply-rate metric, and the résumé + `networking-prep.skill` aren't wired in.

## Plan (every step one venue tag; highest-leverage first)

- **1. [local] Close the loop with Gmail read-back.** ⭐ Add a reconcile step to the runbook:
  `search_threads` each `drafted/sent` contact → auto-advance status (reply found → `replied`),
  and actually fire the 7–10-day follow-up flags. Turns the board from static to live.
- **2. [local] Harvest warm leads.** Scan iMessage + Gmail for 2-way threads with people in Cole's
  lanes (health/bio/AI/VC, NYC/DC) → propose a **warm-leads queue** for Cole to confirm into Lane 0
  (the repeatable version of how Arielle was found).
- **3. [local] Wire the assets.** Point the kit's "résumé look" ask at the real
  `~/Desktop/Personal Stuff/Cole_Kannam_Resume.pdf`; install Cole's `networking-prep.skill`
  (`~/Documents/Networking People/networking-prep.skill`) into `.claude/skills/` so Tier 1 briefs
  generate in-session.
- **4. [local] Mine + rank the full PIKE PDF.** Parse the ~1,000-member roster
  (`~/Desktop/Personal Stuff/Past Pikes…(4).pdf`), rank for Cole's lanes + NYC/DC, extract emails →
  deepen Tier 2 from 8 to a real ranked queue.
- **5. [cloud] Build the target-org map.** Web-research NYC/DC **health-bio-AI startups + venture
  funds** → ranked `crm/target-orgs.md`; then **[local]** map known contacts → orgs so outreach
  becomes directed. (Answers Job-Search action item #2.)
- **6. [local] Add a reply-rate scoreboard.** Lightweight metric block on the pipeline
  (sent / replied / meetings + reply-rate by tier & template) to A/B templates over time.
  *Not* bound to `autoresearch/score.py`'s ratchet — just a visible metric.
- **7. [human] Confirm inputs.** Arielle's full name/role at Forus; the warm-lead candidates from
  step 2; and post-Tuesday, drop **Stewart's 2–3 intros** into Lane 0.

## Recommended first move
Steps **1–3** as one `[local]` batch now (biggest leverage, all doable this session). Step 4 next,
step 5 to cloud, step 6 quick, step 7 to Cole.
