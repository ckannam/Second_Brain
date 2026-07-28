---
type: improvement-plan
target: .claude/skills/networking-prep (the networking-prep skill)
created: 2026-07-27
status: local-steps-1-7-executed (2026-07-27); step 8 resolved 2026-07-27: markdown-only (docx dropped, doc_helper.py deleted)
---

## Executed 2026-07-27 (local steps 1–7)
Rewrote `.claude/skills/networking-prep/SKILL.md` to be vault-native: **(1)** killed the hardcoded
profile → loads `profile/cole.md` + `five-year-plan.md` + `outreach-kit.md` live + a freshness
principle; **(2)** new "Step 0.5 — read the vault first" (CRM record, iMessage history, pipeline
status) before any web search; **(3)** Section 5 pitch now pulls the kit's 3-sentence pitch +
proof-point bank + ask-menu, with a grounded take from Cole's own wiki; **(4)** Section 2 anchors to
the current health/bio/AI operator lane, not hardcoded JHTV; **(5)** output = a linked markdown prep
page at `crm/prep/<Name>.md` (dropped the Cowork-only present tool; `.docx` optional via
`doc_helper.py`); **(6)** new Step 6 feeds the engine (CRM record + pipeline row + index + log);
**(7)** refreshed description to "prep **and** pitch," vault-grounded. Kept the strong research
method (Sec 1/3), question design, and tone bar. `doc_helper.py` unchanged.

# Improve — the `networking-prep` skill

**Target:** `.claude/skills/networking-prep/SKILL.md` (+ `scripts/doc_helper.py`).
**Cole's vision:** it was built *before* this vault existed — make it **use the vault** to prep for
and **pitch himself to anyone he chats with**, always current, never a frozen profile.

## Diagnosis (gap to vision)
A strong web-researcher wrapped around a **frozen, off-strategy self-description** (hardcodes
"rising senior / JHTV summer / translational-funding-VC" — contradicts the locked
[[five-year-plan]]: operator-first, health/bio/AI, NYC/DC, grad May 2027). It **ignores the CRM +
[[outreach-pipeline]]**, re-invents the pitch each run instead of using [[outreach-kit]], doesn't
tap Cole's own wiki knowledge, and **dead-ends** as a `.docx` outside the graph (via a Cowork-only
present tool). Result: prep that's disconnected from everything the vault now knows.

## Plan (each step one venue tag)

- **1. [local] Live profile, not hardcoded.** Replace the "Who Cole Is" block with a run-time load
  of `profile/cole.md` + [[five-year-plan]] + [[outreach-kit]] (graceful fallback if unreadable).
  Add a **freshness principle**: never bake facts into the skill; always pull live.
- **2. [local] Read the vault before the web.** New "Step 0.5": check `crm/<Name>.md` (existing
  record, iMessage history, prior interactions) + [[outreach-pipeline]] status + a vault grep for
  any mention — fold that history into the prep so it's aware of the relationship so far.
- **3. [local] Pitch from the kit (Section 5 rewrite).** Pull the canonical **3-sentence pitch +
  proof-point bank + ask-menu + opener patterns** from [[outreach-kit]]; select/tailor proof points
  to the specific person. Add a "talking points in Cole's own voice" element grounded in his wiki
  clusters (neuroscience, AI-building, future-of-work) so his takes are genuinely his.
- **4. [local] Current lane (Section 2 rewrite).** "How their background connects to Cole" grounds
  in the current health/bio/AI operator lane from [[five-year-plan]], not the hardcoded JHTV summer.
- **5. [local] Vault-native output.** Primary artifact = a linked **markdown prep page** (e.g.
  `crm/prep/<Name>.md`) that cross-links the CRM record + pipeline row; drop the `mcp__cowork__…`
  dependency; keep `.docx` (via `doc_helper.py`) as an **optional** secondary export.
- **6. [local] Feed the engine.** After prep, create/update the person's `crm/` record + a
  [[outreach-pipeline]] row (status `queued`/`warm`) + `log.md` line — so prep compounds, not dead-ends.
- **7. [local] Description/trigger refresh.** Update the skill's `description` to say prep **and
  pitch**, vault-grounded; keep the strong research + tone bar (Sections 1/3/4/6 largely stay).
- **8. [human] One preference:** keep generating the `.docx` (nice for attaching/offline) or go
  **markdown-only**? Default = markdown page primary + `.docx` optional.

## Recommended first move
Steps **1–7 as one [local] batch** — it's a single coherent SKILL.md rewrite (keeping the good
research + tone bar intact). Step 8 is a quick preference; default handles it.
