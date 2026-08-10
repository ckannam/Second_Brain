---
type: doc
category: JHTV / Capital Strategy
created: 2026-08-10
author: Cole Kannam
audience: Justin (operator handoff)
status: draft for review
---

# Second Brain (VC Matcher) — Operator's Guide

*For Justin. One page to keep it running and keep using it. Full context:
[[JHTV-Second-Brain-Vision-and-Handoff]].*

## What it is
An internal tool with two front doors: **firm → the Hopkins techs it's most likely to fund** (with fit
scores, JHU-alumni warm-intro paths, and downloadable one-pagers), and **tech → its best-fit funders +
a non-dilutive grant screen.** It's what you open to prep a firm meeting or advise a team on next capital.

## How it works (plain version)
- **A static website on GitHub Pages — no server database, no build step.** The browser downloads a few
  JSON files and does all matching/scoring in JavaScript, on the machine.
- **The `data/` JSON files *are* the database** (`vcs.json`, `technologies.json`, `jhu_connections.json`,
  `jhtv_relationships.json`, `vc_portfolios.json`, deal histories…). **Git is the version history, the
  review (diffs/PRs), and the undo button.**
- **One optional moving part:** a small **Render backend** (`server.js`) that wakes only when you search a
  firm the tool has never seen — it runs Claude + web search and commits the new firm into `vcs.json`. On
  the free tier it **spins down after 15 min (~30s cold start)** — expected, not a bug. Nothing in
  day-to-day matching depends on it being awake.

## How to maintain it
- **Add / edit a tech or firm** → edit the JSON in `data/`, commit. Live on next deploy.
- **Run a match** → type a firm (→ techs) or click a tech (→ firms). No upkeep.
- **One-pagers** → live in `one-pagers/` (Tech and VC folders — note the real trailing space in the VC
  folder name; keep it).
- **Add a new VC automatically** → just search it; the backend researches + saves it.
- **Refresh the JHU alumni network** → source of truth is `JHU_VC_Network.xlsx`; after editing, run
  `node scripts/convert_jhu_connections.js` to regenerate `jhu_connections.json`, then commit.
- **Grants** → powered by the **shared grant engine** (same engine as the external Grant Finder — update
  once, both stay in sync).

## Why it won't break — and recovery
Because it's JSON-in-git: a bad change is **one `git revert` away**, every edit is a reviewable diff, and
there's no server state to corrupt. Realistic failure modes are small:
- **Malformed JSON edit** → that file won't load; fix the syntax and recommit.
- **Backend asleep** → wait ~30s; only affects researching *brand-new* firms.

## What your full-time internal access unlocks
I built this from outside Hopkins' internal systems. You can wire it to **authoritative internal
sources** — the live tech pipeline, real relationship/CRM data, and the internal system Oliver's vision
describes — so the data stops being a hand-maintained snapshot and becomes a live mirror of the office.
That's the whole next chapter.

## Quick reference
Repo `ckannam/VC_Matching_Second_Brain` · frontend = GitHub Pages (static) · backend = Render
(`server.js`) · data = `data/*.json` · one-pagers = `one-pagers/` · scripts = `scripts/`.
⚠️ **Licensed PitchBook data + the JHU VC-network database live in the repo — keep them internal.**
