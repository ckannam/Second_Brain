---
source: youtube
channel: "David Andre"
url: "https://www.youtube.com/watch?v=uBWuKh1nZ2Y"
title: "(18) The only AutoResearch tutorial you’ll ever need"
created: 2026-07-24
---
# The only AutoResearch tutorial you'll ever need (David Andre)

**Thesis:** the clearest beginner explanation of [[autoresearch]] + a live build. Covers the mechanism, why it generalizes past ML, and a from-scratch loop optimizing a website's load time.

## Key points
- **What it is:** an open-source project by [[andrej-karpathy]] that lets AI improve itself. Give it *one file, one metric*, let it run hundreds of experiments while you sleep, keeping what works via git and reverting what doesn't.
- **Why `prepare.py` is off-limits:** if the agent could edit the scorer, it would cheat the eval. `prepare.py` defines what "better" means. (Frames the three-file architecture: `program.md` = human's goal/rules, `train.py` = the one editable file, `prepare.py` = untouchable metric.)
- **Fixed time budget = fair comparison** — like giving every job applicant the same 7 minutes; only the raw idea wins, not more training time.
- **The three conditions for success** (the vault records these on [[autoresearch]]): a clear scalar metric, an automated eval with no human in the loop, and exactly **one** file the agent can change.
- **Where it fails:** subjective "better" — brand, UX, most pricing — or slow/subjective loops. A bad metric is confidently optimized in the wrong direction.
- **Karpathy's end vision:** a SETI@home-style distributed swarm for AI research; predicts all frontier labs run some form of autoresearch. "Early stages of the singularity."
- **Live demo:** clones the repo with [[claude-code]], has [[codex]] write a Puppeteer benchmark, adapts Karpathy's `program.md`, and runs a loop that cuts a portfolio site's median load from 50 ms → 33 → 28 → 25 ms in minutes.
- **The valuable skill shifts** to picking the metric and constraints — "this is the skill that will make millionaires."

Use cases named: trading (Sharpe ratio), marketing/AB tests, code speedups, on-device model fine-tuning, prompt engineering. (Sponsor: Oxylabs — noted, not endorsed.)

Entities: [[andrej-karpathy]], [[david-andre]], [[claude-code]], [[codex]]. Concepts: [[autoresearch]], [[eval-driven-model-selection]], [[agentic-workflows]].
