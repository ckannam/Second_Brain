---
type: entity
category: project
created: 2026-07-25
updated: 2026-07-25
---
# VC Matching Second Brain (Cole's flagship JHTV project)

Cole's **longest-term project** and the centerpiece of his [[capital-strategy|Capital
Strategy]] work: an internal tool where a [[jhtv|JHTV]] staffer types a **VC firm** and gets
back the **top Hopkins technologies that firm is most likely to fund** — with a fit score,
**warm-intro paths through JHU alumni**, and a downloadable **one-pager**. It also runs in
reverse (technology → best-fit VCs). Built with [[claude-code]] (**151 commits**).

## How it works (the interesting part)
- **JSON-in-git IS the database.** A static **GitHub Pages** site; the browser loads a few JSON
  files and runs **all matching/scoring client-side in JavaScript** — no live server DB. Cole
  can articulate *why* (tiny read-mostly dataset, free hosting, git = free version history +
  PR review + rollback, human-readable/editable, atomic deploys) **and** the honest tradeoffs
  (wrong for large data / frequent writes / many editors). That's real engineering judgment.
- **Optional AI backend.** A Render/Vercel `server.js` wakes **only** to research a VC the tool
  has never seen — **Claude + web search** → commits the new firm into `vcs.json` via the GitHub
  API. Self-extending dataset.
- **Matching logic:** fit by **sector, stage, check size, geography**; splits results into
  **firms JHTV already has a relationship with vs. new prospects**; surfaces **JHU-alumni warm
  intros**; scoring **rubric (v2)**; tech **cohorts** + `tech_status` (pause/unpause).
- **Data model:** ~**74** JHTV technologies · ~**28** curated VC firms · **827** JHU-connected
  people · plus **391 PitchBook investors** catalogued. *(Counts are point-in-time; the tool grows.)*

## One brain, two front doors
Shares its **grant engine** with the external [[jhtv-grant-finder|Grant Finder]] (self-serve for
professors/founders) so the internal and external tools **can never give different answers** —
when the funding picture hits the non-dilutive part, both call the same engine.

- Repo: `ckannam/VC_Matching_Second_Brain`. ⚠️ **Licensed PitchBook data + the JHU VC network
  database live in the repo, deliberately not copied here.**

Embodies Cole's **science → capital + AI-building** edge — his top recruit artifact.

## Long-term vision & handoff
Forward roadmap + Justin-handoff doc: **[[JHTV-Second-Brain-Vision-and-Handoff]]** (2026-08-10). Frames
the tool as the **capital-matching engine** behind Oliver's internal "Studio Portal," adds the
**[[translational-funding|Translational Funding]]** pillar + the TF→MII/SBIR→seed→A escalator, and the two
data upgrades that compound it (a **PitchBook API** for live deal data; **live portal data** to keep
tech/firm profiles current). Anchor use case: the team walking into a firm/tech meeting knowing what to say.

Related: [[capital-strategy]], [[jhtv-grant-finder]], [[claude-code]], [[Job Search]].
