# Startup Tracker — Design Spec

**Date:** 2026-07-29
**Status:** Approved design (pre-implementation-plan)
**Owner:** Cole

## Overview

An end-to-end **startup discovery → outreach → logging → analytics** engine for Cole's job
search, rendered as an interactive dashboard **inside Obsidian** using the native **Bases**
plugin. It closes the one missing half of Cole's existing outreach engine — **automated
discovery** — and unifies company tracking into a queryable, one-note-per-company database.

The vault already has the outreach half:
- [[target-orgs]] — org-centric startup tracker (single markdown table)
- [[outreach-pipeline]] — people board + weekly "run the outreach batch" runbook (Gmail draft
  creation, follow-up rules, interaction logging)
- [[outreach-kit]] — positioning/drafting fuel
- [[cold-email-job-search]] — methodology + the 9 discovery sources

This project builds the **Discovery Radar** (the gap), migrates org tracking to a
one-note-per-company model, and renders it all through a native Bases dashboard.

## Goals

1. **Discovery Radar** — a repeatable sweep of accessible startup-discovery sources that
   auto-populates the tracker with fresh, lane-filtered, deduped companies.
2. **In-Obsidian dashboard** — native Bases views (Fresh Finds / Reach Now / In Progress /
   By Lane / Metrics) that update live and are edited in-app.
3. **Close the loop** — reuse the existing outreach/logging/analytics machinery so discovery
   flows straight into drafting (Gmail drafts, never auto-send), logging, and reply-rate metrics.

## Non-goals (YAGNI / scope boundaries)

- **No paid-API integrations** (Ramp vendor-spend data, full Harmonic). Free/public surfaces only.
- **No standalone web app** now. The clean markdown/frontmatter data layer keeps that door open
  for a future "product" build (Approach C) with zero rework, but it is out of scope.
- **Company-centric only.** Relationship/alumni networking — Lane 0 warm contacts and the PIKE
  cold roster — **stays in [[outreach-pipeline]]** (a different axis: people you know vs. companies
  you're chasing). The two cross-link but do not merge.
- **No auto-sending.** All outreach remains draft-only (Cole reviews + sends), per existing engine.

## Architecture

New **local-only** folder (gitignored, like `crm/` — this is outreach/contact data):

```
startup-tracker/                (gitignored)
  companies/                    one markdown note per company (the "rows")
    ataraxis-ai.md
    formation-bio.md
    ...
  Startup Tracker.base          the dashboard (Bases views)
  README.md                     how it works + how to run the radar
```

Rendering: **Obsidian Bases** (core plugin, already enabled). No community-plugin dependency.

### Data flow

```
9 sources ──(startup-radar skill)──> companies/*.md (status: discovered)
                                            │
                          Bases "Fresh Finds" view (Cole triages)
                                            │
                        status: reach-now ──> outreach-kit / networking-prep
                                            │        draft cold email (Gmail draft)
                                            │
                          status: contacted → (Gmail reconcile) → replied/meeting/nurtured
                                            │
                                  Bases "Metrics" view (reply rate, funnel)
```

## Component 1 — Company note (the data model)

One markdown note per company in `startup-tracker/companies/`, `kebab-case` filename.

Frontmatter schema:

```yaml
---
company: Ataraxis AI
aliases: []
website: ""
careers_url: "https://jobs.ashbyhq.com/ataraxis-ai"
lane: health-bio-ai        # health-bio-ai | ai-infra | other
location: "NYC"
geo_fit: strong            # strong | ok | remote | weak
status: reach-now          # discovered | triaged | enriching | reach-now | contacted | replied | meeting | nurtured | parked | passed
funding: "hiring Jul 2026" # round · amount · date · lead, when known
person: ""                 # named contact once found
contact: ""                # email / LinkedIn
angle: "NYC precision-oncology AI; JHTV translational lens + I build AI"
source: july-hiring-thread # discovery origin (which of the 9 / feed)
discovered: 2026-07-29
last_touch:                # date of last outreach touch
replied: false
next_action: "find hiring manager, draft cold email"
---
# Ataraxis AI
<free-text notes>
## Interaction log
- 2026-07-29 discovered via Ben Lang July hiring thread
```

**Status ladder** (merges the old `target-orgs` bucket vocabulary + `outreach-pipeline`
statuses): `discovered → triaged → enriching → reach-now → contacted → replied → meeting →
nurtured`, plus terminal `parked` (killed, never re-surface) and `passed`.

Real people Cole builds relationships with still get their own `crm/` record, cross-linked from
the company note (e.g. `person` links to `[[Joshua Vogelstein]]`).

## Component 2 — Dashboard (`Startup Tracker.base`)

One `.base` file, multiple views (tabs), all reading `companies/`:

- **📥 Fresh Finds** — `discovered` within ~14 days AND `status` in {discovered, triaged}. The
  Radar's landing zone / weekly triage queue.
- **🟢 Reach Now** — `status: reach-now`, sorted by freshness. The action queue.
- **🚚 In Progress** — `status` in {contacted, replied, meeting}, with a **follow-up flag**
  (formula: `last_touch` older than 7 days AND `replied` false → "⏰ nudge").
- **🗂 By Lane** — grouped by `lane`, all active companies (excludes parked/passed).
- **📊 Metrics** — funnel counts by `status` + **reply rate** (replied ÷ contacted) + count
  discovered in the last 7 days.

Interaction: Cole edits `status`/`next_action` in the note properties panel; views re-sort live.
No refresh step.

**Risk/uncertainty:** Bases is newer than Dataview. Filters, sorts, group-by, and simple
formulas (freshness age, follow-up flag) are solid. A computed ratio (reply rate) may need a
Bases summary row or, worst case, a tiny companion note. Exact Bases formula syntax to be
confirmed at build time, not assumed here.

## Component 3 — Discovery Radar (`startup-radar` skill)

A new Claude Code skill in `.claude/skills/startup-radar/` (sibling to `concert-digest`),
triggered by "run the startup radar" (and optionally invoked inside the Monday batch). Each run:

1. **Sweep accessible sources** (free/public surfaces only):
   - ✅ Fetchable: HN "Who's Hiring" (public/Algolia), YC jobs directory, VC portfolio boards
     (Sequoia/a16z/Index/Greylock), Harmonic Hot 25 (public page), Founders You Should Know,
     public Substack posts (Next Play, Early Days, a16z Build), startups.gallery/news.
   - ⚠️ Gated (skip / free-surface only): Ramp vendor-spend data, full Harmonic. If Cole wants a
     paid source in, he forwards/pastes it.
2. **Extract** company + metadata (name, location, careers URL, funding if present, source).
3. **Lane-filter** to health/bio/AI + AI-infra Cole can credibly speak to; NYC/DC/remote preferred
   (weak-geo still logged but flagged `geo_fit: weak`).
4. **Dedupe** against existing `companies/` notes (by company name + domain) and never re-surface
   `parked`/`passed` companies.
5. **Write new company notes** (`status: discovered`, `source` tagged, first-pass `angle` guess,
   `discovered` date).
6. **Report** a ranked "new this week" shortlist in-session; optional iMessage push (reusing the
   concert-digest AppleScript delivery pattern).

Mechanism: a Claude web-fetch/web-search session (same pattern as the existing startups.gallery
Monday fetch). No persistent scraper/server.

## Component 4 — Loop integration (reuse existing engine)

- **Triage:** Fresh Finds → Cole moves to `reach-now` or `parked`.
- **Reach out:** for `reach-now`, reuse [[outreach-kit]] (pre-send checklist, value-first template)
  + [[networking-prep]] (deep brief for marquee targets), drafting per [[cold-email-job-search]]
  rules → **Gmail draft** (`mcp__claude_ai_Gmail__create_draft`), Cole sends.
- **Log:** update the company note's `status`, `last_touch`, `replied`, and append to its
  Interaction log. The weekly **Gmail reconcile** step (from the [[outreach-pipeline]] runbook)
  flips `replied`/`status`.
- **Analytics:** the Bases **Metrics** view.

## Migration plan

1. Create `startup-tracker/` (+ gitignore rule) and the `companies/` folder.
2. Migrate the existing [[target-orgs]] rows (~15 active + the parked list) into company notes
   (Engram, Collate, Flourish, Chai, Candid, Assort, Prime Intellect, Dust, Nourish, Prosper,
   CuspAI, Ataraxis, Formation Bio, PhotonHealth, FedTech, Forus-as-connected, + the ⚪ parked
   names as `status: parked`). Preserve their bucket→status, angle, person, funding.
3. Build `Startup Tracker.base` with the five views.
4. Reduce `target-orgs.md` to a **thin pointer** to the Base (keep it as a breadcrumb; don't delete
   history).
5. Update the [[outreach-pipeline]] runbook so its "scan → triage" step reads/writes company notes
   + the Base (its Lane 0 / PIKE people rows stay as-is).
6. Build the `startup-radar` skill.

## Privacy

`startup-tracker/` is **gitignored** (contains contacts + outreach data), consistent with the
`crm/`/`finance/`/`profile/` policy and [[vault-pii-raw-private]]. Only non-personal design docs
(this spec) are synced.

## Success criteria

- Running "run the startup radar" produces N new, lane-filtered, deduped company notes with sources.
- The Bases dashboard renders all five views and updates live as statuses change.
- A discovered company can flow discovered → reach-now → contacted (Gmail draft) → replied, with
  the Metrics view reflecting reply rate.
- No customer/contact PII is ever committed to git.
- Cole can operate the whole loop inside Obsidian without leaving the vault.

## Open questions (resolve at plan/build time)

- Exact Bases formula syntax for the follow-up flag + reply-rate metric (confirm against the
  installed Bases version; fall back to a summary note if needed).
- Whether the radar runs standalone only, or is also wired into the Monday batch launchd trigger.
- HN "Who's Hiring" access path (Algolia API vs. public thread fetch).
