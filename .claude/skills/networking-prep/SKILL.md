---
name: networking-prep
description: >
  Use whenever Cole needs to prep for AND pitch himself in a networking conversation — an
  informational interview, coffee chat, call, or meeting with someone he wants to connect with.
  Trigger on "I'm networking with X", "prep for a meeting/call with X", "info interview with X",
  "I'm meeting someone at [company]", or any upcoming career/relationship conversation — even if he
  doesn't ask for a document. This is the vault-native prep+pitch skill: it reads Cole's LIVE
  positioning and CRM history from the Second Brain (never a hardcoded profile), researches the
  person, and produces a linked markdown prep page in the vault that feeds the [[outreach-pipeline]].
  Complements the outreach engine — this is the deep, per-person brief.
---

# Networking Prep + Pitch (vault-native)

Produce a research-backed brief for anyone Cole is meeting, and arm him to **pitch himself** with
his *current* positioning. **Ground everything in the vault** — Cole's profile, the outreach kit,
the CRM, and his own wiki knowledge — so the prep is always current and connected, never frozen.

> **Freshness principle (do not violate):** never bake Cole's bio, goals, or pitch into this file.
> Facts age (this skill already went stale once). **Always load them live from the vault at run
> time.** If a vault file is unreadable, say so and use only what you can read — don't invent.

---

## Step 0 — Inputs
Minimum: **the person's name** (+ ideally a city or employer to disambiguate). Don't ask Cole for
their title/background — research it in Step 2. Infer the meeting's purpose from the conversation;
ask one targeted question only if it's genuinely unclear after research.

## Step 0.5 — Read the vault FIRST (before any web search)
The vault already knows a lot. Load, in order:
1. **Cole's live positioning** — `profile/cole.md`, `profile/five-year-plan.md`, and
   `crm/outreach-kit.md` (the canonical pitch, proof-point bank, ask-menu, opener patterns).
   This replaces the old hardcoded "Who Cole Is." Use whatever these say *today*.
2. **This person's existing history** — `crm/<Name>.md` if it exists (relationship, iMessage
   history, prior interactions, prep docs), and their row in `crm/outreach-pipeline.md` (lane +
   status). Grep the vault for other mentions. **Fold the relationship-so-far into the prep** —
   don't prep them as a stranger if they aren't one.
3. **Cole's own knowledge to draw on** — skim `index.md` for wiki clusters relevant to this person
   (e.g. neuroscience, AI-building/agentic, future-of-work, health/bio/AI) to source genuine,
   grounded talking points in Step 4 §5.

If `crm/<Name>.md` doesn't exist yet, note it — Step 6 will create it.

## Step 1 — (context) Anchor to Cole's current lane
From `five-year-plan.md`: Cole's direction drives Sections 2, 4, and 5. Use the **current** lane
(don't assume — read it). As of this writing it's *operator-first in health/bio/AI, NYC or DC,
grad May 2027* — but **trust the file over this sentence** if they differ.

## Step 2 — Research the person
Start from name + city and work outward: `[name] [city]` → `[name] [employer]` →
`[name] [employer] LinkedIn` → `[name] [field/topic relevant to the meeting]`. Disambiguate common
names by city/context; note any assumption at the top. If web presence is thin, work with what you
find and mark inferences. **Do not fabricate specific claims.**

## Step 3 — Build the brief
Six sections below, full content, no placeholders. Sections **1, 3, 6** keep the original strong
structure; **2, 4-as-§4, 5** are vault-grounded. Output format is in Step 5-output.

### Section 1 — Their Career Path (what each role actually meant)
For each role: **subheading** (Role — Org, approx years) · **"What they did:"** (1-2 concrete
sentences) · **"What this role actually is in the field:"** (2-4 paras of real industry mental
model — not a title restatement) · end with what the role *gave* them. Shorter for transitional roles.

### Section 2 — How their background connects to Cole (current lane)
Draw explicit, specific lines between what they've done and **Cole's current goals/lane from
`five-year-plan.md`** (health/bio/AI operator path, the science×funding×AI edge) — plus his JHTV
work where relevant, but framed as *one credential*, not the whole identity. 2-4 connections, each a
subheading + 2-3 paras: name the specific overlap and why it's useful to Cole *now*.

### Section 3 — Questions worth asking
6-8 questions, grouped, ordered experience → strategic insight → career advice for Cole. Each
specific enough to show homework; add a one-line italic note on why it's worth asking.

### Section 4 — The actual ask
**Primary goal** (recommended ask + a verbatim closing line — pull the right ask from the
outreach-kit **ask-menu**, sized to the relationship) · **Secondary goal** (next ask if it goes
well) · **What NOT to do** (1 para tailored to this context: warm vs. cold, first call vs. follow-up).

### Section 5 — Cole's pitch (from the outreach kit)
The point of this section: make Cole **interesting, not just interested**, in his *current* voice.
Pull from `crm/outreach-kit.md` and tailor to this person:
1. **Intro** — adapt the kit's **3-sentence pitch** into a 2-sentence opener that names the real
   work + why it's relevant to *this* person. First-person quoted script.
2. **Proof points** — pick the **1-2 from the kit's proof-point bank** that land most for this
   reader (operator / capital / AI / science), as quoted scripts he can say.
3. **A grounded take** — one genuine opinion to put on the table, sourced from Cole's *own wiki*
   (the clusters skimmed in Step 0.5 — e.g. a neuroscience or future-of-work view), framed to invite
   pushback. This is where his real knowledge shows. Quoted script.
Keep it consistent with the kit — if the kit changes, this section changes with it.

### Section 6 — After the call
**Within 24h:** non-generic thank-you referencing `[specific thing they said]`. **If they named a
person/resource:** specific follow-ups + timelines. **Re-engage (timed to Cole's search):** a warm
template for later. Close on the long-game value of this person's network to Cole's lane.

## Step 5-output — Save it into the vault (markdown only)
Write a markdown prep page to `crm/prep/<FirstName> <LastName>.md` (create the `crm/prep/` folder if
needed; it's under the local-only `crm/`). Frontmatter `type: crm/prep`, `created`, `person`,
`meeting`. **Cross-link** it to `[[<Name>]]` (their CRM record) and `[[outreach-pipeline]]`. Add a
footer: "Research compiled <month year>. Sources: <list>." Tell Cole the vault path.
**No .docx / no external export** — the vault markdown page is the artifact (Cole's decision 2026-07-27).

## Step 6 — Feed the engine (so prep compounds)
- If `crm/<Name>.md` doesn't exist, **create it** (per `AGENTS.md` CRM rules) with what research +
  any iMessage history gave you; else **update** it. Link the prep page.
- Add/update their row in `crm/outreach-pipeline.md` (right lane; status `queued`/`warm` + next
  action) and update `crm/index.md`.
- Append a one-line entry to `log.md`.

---

## Tone & quality bar
Write as a smart colleague briefing Cole before an important meeting. Every section should contain
something he couldn't have written without 2 hours of research or without the vault. Ready to read
and act on — no filler, no generic praise. Avoid empty lines like "she has extensive experience
in…" / "he brings a wealth of knowledge…"; every sentence carries a specific, actionable insight.
