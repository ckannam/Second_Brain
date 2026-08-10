---
type: doc
category: JHTV / Capital Strategy
created: 2026-08-10
author: Cole Kannam
audience: Justin (operator handoff) · Stewart & Oliver (vision discussion)
status: draft for review
---

# JHTV Capital Strategy "Second Brain" — Handoff & Long-Term Vision

**Author:** Cole Kannam · **Date:** August 2026
**For:** Justin (taking over day-to-day) · Stewart & Oliver (the forward discussion)

---

## 1. How to read this

This document does two jobs. **First, continuity:** enough that Justin can keep the tool running,
keep using it, and not fear it breaking. **Second, vision:** where I see the tool heading and how it
could compound as the office builds toward a live internal portfolio system. The two halves are
deliberately separated — §3 is the operator handoff; §5–7 are the roadmap for the room.

One-line thesis: **the tool is the capital-matching brain for our team's core job — walking into a
meeting with a firm *or* a tech team and knowing exactly what to say — and its destination is to become
the office's shared capital-and-connections intelligence layer, feeding the internal portal rather than
competing with it.**

Everything about the future portal here is drawn from Oliver's direction and the internal/external
mockups; it's **directional, not a spec.** I'm using it to show the *kinds of live data* that would
make this tool sharper, not to commit anyone to a design.

---

## 2. What the tool is today

The tool serves the two sides of our team's actual job:

- **Firm-facing (the meeting):** *"We're meeting Firm X — which Hopkins techs and teams should we put in
  front of them, and why?"* Type a VC firm → get the top matched JHTV technologies, a fit rationale, the
  warm-intro paths through JHU alumni, and downloadable one-pagers to leave behind.
- **Tech-facing (the advice):** *"This spinout is at stage Z — where's its next capital, and how does it
  get there?"* Click any technology → its funding landscape: best-fit investors (ranked, tiered) plus a
  preliminary non-dilutive **grant** screen.

**The backbone is two first-class profiles matched against each other:**
- **Tech profile** — a Hopkins technology/team: sector, stage, readiness, the investors it fits.
- **Firm profile** — a funder: sectors, stages, check size, geography, portfolio, JHTV relationship, and
  the JHU alumni who connect in.

**What it does well today.** Fit scoring by sector/stage/check-size/geography (rubric v2, portfolio-led);
splitting results into **firms JHTV already has a relationship with vs. new prospects**; surfacing
**JHU-alumni warm intros**; a **self-extending dataset** (an unknown firm triggers a Claude + web-search
backend that researches it and commits it to the database); and a **shared grant engine** with the
external Grant Finder so internal and external funding answers can never diverge. Current data footprint:
~74 technologies, ~28 curated firms, 827 JHU-connected people, plus a few hundred PitchBook investors.

**Honest current limitations — and they're exactly where the upside is:**
1. **Deal data is manual.** The firm "revealed" signal (what they *actually* fund) rests on deal
   histories I pulled by hand — ~60 firms so far. Valuable, but not the long-term play. → **§5: a
   PitchBook API turns this into live, authoritative deal data.**
2. **Technologies are static.** Techs are added by hand and don't update. A tech that just got licensed,
   or moved a stage, stays as-is until someone edits it. → **§6: live portal data keeps tech positions
   current and excludes techs that are no longer in play.**
3. **Translational Funding isn't modeled.** A large part of our team's job — the TF program and the
   non-dilutive escalator it kicks off — lives outside the tool today. → **§4 and §5 make it a pillar.**

---

## 3. Operational continuity — for Justin

**Plain-English architecture.** The whole thing is a **static website hosted on GitHub Pages** — no
server database, no build step. When someone opens it, their browser downloads a handful of JSON files
from the repo and does all the matching and scoring **in JavaScript, on their machine**. The data files
in `data/` (`vcs.json`, `technologies.json`, `jhu_connections.json`, `jhtv_relationships.json`,
`vc_portfolios.json`, deal histories, etc.) *are* the database — **git is the version history, the review
process, and the undo button.**

There's one optional moving part: a small **backend on Render** (`server.js`) that only wakes up when
someone searches a VC the tool has never seen. It runs Claude + web search, then commits the new firm
into `vcs.json` via the GitHub API. It's on Render's free tier, so it **spins down after 15 min and takes
~30s to cold-start** — that's expected, not a bug.

**Routine operations you'll actually do:**
- **Add / edit a technology or firm** → edit the JSON in `data/`, commit. It's live on the next deploy.
- **Run a match** → type a firm (firm → techs) or click a tech (tech → firms). No maintenance needed.
- **Generate a one-pager** → the `one-pagers/` folder holds the tech and VC one-pagers the tool serves.
- **Add a new VC automatically** → just search the firm; the backend researches and saves it.
- **Refresh the JHU alumni network** → the source of truth is the `JHU_VC_Network.xlsx` sheet; after
  editing it, run the convert script to regenerate `jhu_connections.json`, then commit.
- **Grants** → the shared grant engine powers both this tool and the Grant Finder; update it once.

**Why it won't break, and how to recover if it does.** Because it's static JSON-in-git: a bad edit is
**one `git revert` away**, every change is reviewable as a diff, and there's no server state to corrupt.
The realistic failure modes are small: a malformed JSON edit (the page fails to load that file — fix the
syntax, recommit), or the Render backend being asleep (wait ~30s, or it only affects researching *brand-new*
firms). Nothing about the day-to-day matching depends on the backend being up.

**What your full-time internal access unlocks that I couldn't reach.** As an intern I was working from
the outside of Hopkins' internal systems. You can wire the tool to **authoritative internal sources** —
the real technology pipeline, live relationship/CRM data, and the portal Oliver's team is building — so
the data stops being a hand-maintained snapshot and starts being a live reflection of the office. That
single difference is most of the roadmap below.

---

## 4. The three pillars of our team's job — and where the tool sits

Our team helps ventures answer *"where's the next capital, and how do we get there?"* That breaks into
three funding levers. The tool covers one well, touches one, and misses one entirely:

1. **Equity capital (VC / corporate).** ✅ *The tool's core.* Firm ↔ tech matching, warm intros,
   one-pagers, meeting prep.
2. **Non-dilutive grants.** ◐ *Partially.* The shared grant engine screens likely-eligible grants for a
   tech, but doesn't yet manage the *workflow*.
3. **Translational Funding (TF) — our own money.** ✗ *Not modeled, and it's central.* TF is how our team
   **gets the ball rolling**: small internal checks (here, ~$50K) that buy the specific de-risking work
   nobody else will fund — the milestone experiment or document that moves a technology from "interesting"
   to "investable" across the valley of death. JHTV runs three named funds (Cohen, Thalheimer, Zizic);
   faculty submit per-technology proposals; external reviewers independently score science / product
   potential / budget; a committee ranks and either funds directly or invites a live pitch. Awards pay out
   **against milestones** — money releases only as evidence arrives. Success isn't revenue; it's the
   **next** unlock: a license, an SBIR or **MII** award, a spinout, a term sheet. TF most often leads into
   MII — it's the first push in a continuous wave of funding.

**The insight for the vision:** these three aren't separate — they're **rungs on one escalator**
(TF → MII/SBIR → seed → Series A), and *milestones* are the unit of progress. The tool today jumps
straight to the top rung (VC). The vision is to model the **whole escalator**, starting where our team
actually starts: TF.

---

## 5. The vision — where the tool is heading

**A. Two-sided profiles that get richer and truer.** Keep tech profiles and firm profiles as the
backbone, but deepen both — and, critically, separate what a firm **says** from what it **does**. The
mockups already nail the principle: *a firm's portfolio does the most work, because it's how you tell a
real track record from a stated interest.* Their thesis is a claim; their holdings are behavior. The tool
should always match on behavior first.

**B. The copilot loop (tech-facing).** For any venture, one iterative loop: **diagnose stage & readiness
→ recommend the next capital (TF → grants → equity) *and* the right mentor → draft the narrative/one-pager
→ track the outreach → define the next milestone → re-run at the next stage.** This is the "advice"
half of our job, made repeatable.

**C. Meeting-memory (firm-facing).** The firm page should *remember*: what we've pitched to whom, what a
firm engaged with, what they passed on. The internal mockup already shows this as **touchpoint history**
("Shared 3 oncology one-pagers; interested in IL-2 asset") — that history should *feed the matching*, not
just sit there.

**D. The integrated next-stage playbook.** The payoff narrative the tool should be able to generate for a
venture: *"To reach Stage X and become fundable by a firm like Y, the next milestone is Z — here's the
TF/grant that pays for Z, and here's the internal mentor who's done it before."* Capital + action +
mentorship as one path. That's the whole point of the office pulling these tools together.

---

## 6. How it fits the office — Oliver's portal & Justin's Programs

Oliver's direction is a **live internal portfolio ("Studio Portal") that runs the office** — tracking
ventures, people, meetings, and updating each tool from a shared source of truth. **This is beyond my
scope to build, but it's the direction, so the tool should be built to feed it, not to duplicate it.**

**The clean division of labor:**
- **The portal = system of record.** Ventures, people, meetings/touchpoints, internal & external views,
  the Feedback Queue.
- **This tool = the capital-matching engine** behind the portal's **Capital Management** module.
- **Justin's mentorship matcher = the Programs engine** — the right senior person to move a project to its
  next stage. Same "get to the next stage" loop; capital is one lever, mentorship is another.

**How live portal data makes the tool measurably better** (the mockups name the streams):
- **Live venture/tech status** → tech profiles stay current automatically; a tech that just got licensed
  is *excluded*, and matching surfaces techs that are genuinely **in the right position** for a firm now.
- **Touchpoints / meeting history** → matching factors in what a firm actually engaged with, not just
  their stated profile.
- **The Feedback Queue** (firm reactions from the external self-service view) → a firm thumbs-up or
  follow-up request **upweights** similar techs, live.
- **Portfolio evidence with provenance** ("source · date") → and a **PitchBook API** makes that portfolio
  live and authoritative instead of hand-pulled, so the *revealed* profile is always current.
- **Translational Funds + Programs modules** → let the tool assemble the full escalator (TF milestone →
  next grant → equity) and the mentorship match into one playbook.

**Two firm views, one data model** (from the mockups — directional):
- **Internal firm view** (team-facing): a facts strip (check size, round, stages, focus) → **portfolio
  evidence** (the primary signal, with source/date) → **matched JHTV technologies** with fit scores and
  Strong/Good/Possible tiers → contacts + touchpoint history. This is essentially today's firm profile,
  rendered live inside the portal.
- **External self-service view** (firm-facing): the firm maintains its own profile, **scored portfolio**,
  watchlist, and contacts, sees a live match count, and gives feedback on techs we've sent. Guardrails:
  their edits update the *stated* layer only (self-reported, and firms notoriously "say one thing, do
  another"); their *behavior* (portfolio, reactions) is the trusted signal. Whether to show a firm our
  classification of their past deals is a real choice — default to keeping our analysis internal and
  showing firms only neutral facts to confirm.

**The line to hold:** the tool supplies the **data model and the matching intelligence** behind the
portal's investor pages. It should not try to become the portal.

---

## 7. Roadmap (phased)

**Phase 1 — Continuity & enrichment (now; Justin owns).** Keep it running; enrich firm and tech profiles;
use it for real firm-meeting prep and tech-funding advice. Deal data stays manual for now. *Goal: it stays
useful and trusted through the transition.*

**Phase 2 — Live data & the missing pillar.** (a) **PitchBook API** → replace hand-pulled deals with live
portfolio/deal data (a major matching-quality jump and the end of manual upkeep). (b) **Model
Translational Funding** → the escalator (TF → MII/SBIR → seed → A), milestone tracking, and the review
workflow, so the tool reflects where our team actually starts. (c) Begin capturing **meeting-memory /
touchpoints**.

**Phase 3 — Portal integration.** Consume the portal's live streams (venture stage, touchpoints, Feedback
Queue, TF status) so matching reflects reality; push the tool's match outputs into the portal's Capital
Management + firm pages; and combine capital with **Programs (mentorship)** into the unified next-stage
playbook.

**Phase 4 — The office's capital-and-connections intelligence layer (north star).** The tool is the brain
the portal orchestrates for every venture: given any company at any stage, the next milestone, the capital
that funds it, the firm it's aiming at, and the mentor to get it there — meeting-ready and memory-keeping.

---

## 8. Guardrails & what to preserve

- **Data licensing.** Licensed PitchBook data and the JHU VC-network database live in the repo and stay
  internal — never copy them out. A PitchBook *API* must respect the same licensing.
- **One grant engine, one answer.** Keep the internal tool and the external Grant Finder on the *shared*
  engine so they can never give conflicting funding answers.
- **Stated vs. revealed discipline.** Match on behavior (portfolio/deals/reactions) first; treat
  self-reported thesis and geography as reference. Firm-supplied edits never silently overwrite internal
  truth.
- **Human-reviewed.** Matching *assists* the meeting; it doesn't replace judgment. Keep a person in the
  loop on what actually gets pitched.
- **Don't become the portal.** Stay the best capital-matching engine; let the portal own tracking.

---

## 9. Open questions for the discussion

1. **Portal timeline & data access** — when do the live streams (venture status, touchpoints, Feedback
   Queue, TF) become available for the tool to consume, and through what interface?
2. **PitchBook API** — is licensed API access something the office will fund? It's the single biggest
   quality unlock and removes the manual-deal burden.
3. **Ownership post-transition** — who owns the tool day-to-day, and how do we sequence the integration
   with Justin's Programs matcher and Oliver's portal so the three fit without duplicated data?
4. **TF in the tool** — how much of the TF workflow (review, milestones, renegotiation) should live in the
   tool vs. the portal's Translational Funds module?
5. **External data reconciliation** — the policy for how firm-supplied data (external view) reconciles with
   our internal, PitchBook-verified truth.

---

*Companion context in the vault: [[vc-matching-second-brain]] (how the tool is built), [[capital-strategy]]
(the team's mandate), [[translational-funding]] (the TF landscape), [[jhtv-grant-finder]] (the non-dilutive
sibling), [[jhtv]] / [[JHTV]] (the org + bucket).*
