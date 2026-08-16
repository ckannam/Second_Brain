---
type: concept
created: 2026-08-05
---

# Outreach Pipeline

Cole's **job-search outreach system** — the architecture, weekly cadence, and templates for
finding and approaching target orgs. Built 2026-07-28 as part of the "target-org intake engine."
Tracker for the live pipeline state lives in the [[Job Search]] bucket.

## The tier structure

| Tier | Description | Source |
|---|---|---|
| **Lane 0 — warm intros** | Existing relationships + intro'd contacts (e.g., Stewart Neifart's introductions) | CRM inner-circle |
| **Tier 1 — funded targets** | Funded startups in Cole's target domain (health/bio/AI, AI-infra, NYC) that pass the 🟢 triage | [[target-orgs]] board from weekly funding feed |
| **General** | Cold outreach to target orgs after enrichment; warm-first framing even in cold email | [[cold-email-job-search]] playbook |

## The weekly batch (Monday runbook)

The scan step is automated by the **[[startup-radar]]** skill, which sweeps the free funding
surfaces, lane-filters, and dedupes before anything reaches the triage board.

1. **Scan** `startups.gallery/news` (and other funding feeds) for new rounds — via [[startup-radar]].
2. **Filter** for health/bio/AI + AI-infra alignment.
3. **Triage** into [[target-orgs]] board: 🟢 (high-fit, pursue now) · 🟡 (watch) · ⚪ (skip).
4. **Enrich** 🟢 orgs: named contact, geo, funding context, warm angle.
5. **Promote** enriched orgs to this pipeline for active outreach.
6. **Send batch** using the right template (see below).
7. **Log outcomes** → reply-rate scoreboard (step 6 of the engine, deferred — see [[tasks/index]]).

## Outreach templates

**Fresh-funding / value-first template** — the default for Tier-1 targets:
- Leads with their recent funding as the hook ("congratulations on the X round").
- Pivots quickly to a specific insight or relevant skill.
- One clear ask (15-min call, not a job application).
- ≤200 words, per [[cold-email-job-search]] rules (no fake personalization).

**Warm-intro template (Lane 0)** — shorter, references the connector explicitly.

## Kits and tools

- **[[outreach-kit]]** — master template library (fresh-funding template, warm-intro template, follow-up cadence).
- **[[target-orgs]]** — live 🟢/🟡/⚪ board; the top of the funnel.
- **[[cold-email-job-search]]** — the underlying playbook (rules, the who/why/why-they-care format, 9 sources for unposted roles).
- **CRM** (`crm/`) — per-contact records, history, next actions (local-only).

## Reply-rate scoreboard (deferred)

Planned metric block: sent / replied / meetings booked + reply-rate by tier and template.
Goal: A/B test templates to improve reply rates. Currently deferred — build during the first
live outreach batch. See [[tasks/index]].

## Current pipeline (as of 2026-07-28 build)

Initial 🟢 triage: **Chai Discovery** · **Engram** · **Collate** (from funding feed); **Forus**
(already-connected via Arielle at JHTV). Per-org enrichment (named contact, geo) runs in the
Monday batch.

Lane 0: **[[Joshua Vogelstein]]** (Flourish / JHU) — outreach drafted and sent 2026-08-04
(source: log.md). **Stewart Neifart** introductions pending (post-Tuesday per [[tasks/index]]).

## The "go" auto-trigger (deferred)

Background watcher planned: detect "go" in Cole's self-chat → headless Claude runs the batch
→ texts summary. Deferred until the first live batch is run. (`@local` lane item.)

Related: [[cold-email-job-search]] · [[outreach-kit]] · [[target-orgs]] · [[Job Search]] · [[claude-code-imessage]] · [[proactive-agents]].
