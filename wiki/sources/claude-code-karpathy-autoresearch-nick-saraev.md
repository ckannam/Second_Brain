---
source: youtube
channel: "Nick Saraev"
url: "https://www.youtube.com/watch?v=4Cb_l2LJAW8"
title: "Claude Code + Karpathy Autoresearch = The New Meta"
created: 2026-07-24
---
# Claude Code + Karpathy Autoresearch = The New Meta (Nick Saraev)

**Thesis:** you can integrate [[autoresearch]] into [[claude-code]] in minutes and point it at business metrics — Nick's own build is a self-optimizing **cold-email** loop. Framed as "self-improving AI / RSI you can run yourself."

## Key points
- **His `email-optimizer`:** metric = **reply rate** (via the Instantly API), changeable input = **cold-email copy**. An `orchestrator.py` spins up a **baseline vs. challenger** each cycle, harvests results, and generates the next challenger from accumulated learnings.
- **`resource.md` as compounding memory:** every run logs what moved reply rate up; each fresh (stateless) orchestrator run inherits all prior context, growing "smarter" over time. Anticipates needing to **consolidate** learnings after ~500–1000 runs (echoes [[agent-dreaming]] / [[claude-code-memory]]).
- **Scheduling:** runs on **GitHub Actions cron** (every 1–4 hrs) so it works fully autonomously in the cloud — the creator-world analog of [[claude-code-scheduled-tasks]].
- **Requirements to generalize:** an objective metric + an **API (or Chrome DevTools MCP)** to change the input. Fast feedback loops win; fuzzy/slow metrics (e.g. "warmth") need proxies.
- **The honest caveat:** most AI-written challengers *lose* to his human-written baseline at first; the value is that eventually a challenger wins, becomes the new baseline, and the metric ratchets up.
- Use cases surveyed: landing-page CRO, ad creatives (CAC/ROAS), chatbot CSAT, e-comm product descriptions, newsletter subject lines, pricing pages.

Built with [[antigravity]] + Claude Opus 4.6; Slack webhook for monitoring. (Nick Saraev runs the agency **LeftClick**.)

Entities: [[nick-saraev]], [[andrej-karpathy]], [[claude-code]], [[antigravity]]. Concepts: [[autoresearch]], [[cold-email-outreach]], [[selling-ai-automations]], [[claude-code-scheduled-tasks]].

**Raw clip:** [[Claude Code + Karpathy Autoresearch = The New Meta]]
