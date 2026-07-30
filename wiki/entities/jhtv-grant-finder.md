---
type: entity
category: project
created: 2026-07-25
---
# JHTV Grant Finder (Cole's project)

An AI tool Cole built to **find and track non-dilutive [[translational-funding|grants]]** for
Hopkins **spinouts** — the grant side of his [[capital-strategy|Capital Strategy]] work. Built
with [[claude-code]] (**38 commits**).

## How it's built
- Static **GitHub Pages** tool (`grant_engine.js`, `index.html`) surfacing relevant grants by stage.
- An **AI grant-deadline-updater** packaged as a **Claude [[claude-code-skills|skill]]**
  (`grant-deadline-updater.skill`) + `ai_grant_updater.js`.
- **CI workflows** (`.github/workflows`) that auto-refresh grant data (`grants_live.json`).
- Repo: `ckannam/jhtv-grant-finder`.

Complements the [[vc-matching-second-brain]] (equity funders) by covering **non-dilutive**
funding. Related: [[translational-funding]], [[capital-strategy]].

**Raw source clips:** [[ckannamVC_Matching_Second_Brain]] · [[ckannamjhtv-grant-finder]]
