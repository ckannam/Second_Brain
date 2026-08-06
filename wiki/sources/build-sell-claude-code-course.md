---
source: youtube
channel: "Nate Herk"
url: "https://www.youtube.com/watch?v=mpALXah_PBg"
title: "Build & Sell with Claude Code (10+ Hour Course)"
created: 2026-07-24
updated: 2026-08-04
---
# Build & Sell with Claude Code — 10+ Hour Course

**Thesis:** The complete zero-to-professional Claude Code course — setup through
building, deploying, and *selling* automations — with no hand-written code. It is the
**umbrella source**: nearly every other Nate Herk page in this vault deep-dives a single
chapter of this course, so this page doubles as a **map of content** into that batch.

## Chapter map (timestamps → the vault page that expands each)

Grounded in the transcript's own outline (`raw/Processed/Build & Sell with Claude Code
(10+ Hour Course).md`, "Course Outline" at 00:00). Each row: the course chapter and the
vault page(s) that carry the full treatment. Chapters without a dedicated page are covered
inline here.

---

## Deeper chapter notes (web-grounded, 2026-08-03)

### Skills chapter

Nate's skills chapter covers the anatomy, the triggering model, and a live six-step build. Key lessons that go beyond what the vault previously captured:

- **Three Ms of AI™ (Nate's framework):** Memory (CLAUDE.md + skills), Mindset (how you prompt), and Methodology (skill workflow). Skills are the Memory layer.
- **"Workflows beat agents"** — Nate's central thesis: a well-tuned skill + workflow outperforms a more complex multi-agent setup for most repeatable tasks.
- The Skill Creator update (March 2026) + evals workflow — see [[claude-code-skill-creation-playbook]] for the full synthesis.
- He also shipped `AIS-OS`: an AI Operating System starter kit (`/onboard`, `/audit`, `/level-up` skills + the Three Ms + Four Cs frameworks) as a companion to a separate 2+ hour AIOS masterclass (distinct from this course).

See [[master-claude-code-skills-28min]] and [[claude-code-skills-update]] for the dedicated source pages. The detailed playbook is [[claude-code-skill-creation-playbook]].

### Agent Teams chapter

The Agent Teams pattern: multiple Claude Code instances run in parallel on the same repo, coordinating through the shared Git state. Each instance is an independent process with its own terminal, its own worktree, its own branch, and its own context. No merge contention while agents are running.

**The three main setup patterns (2026):**

1. **tmux multi-pane (2–3 agents):** Launch each Claude Code session in a tmux pane. Simple — glance at each pane, check progress, intervene if stuck. Good for solo devs.
2. **Git worktrees + per-agent branches:** `git worktree add ../feature-agent-1 feature-branch-1` — each agent gets its own checkout. Supports 5–10 agents without file conflicts. Claude Code v2.1.49+ has native worktree support.
3. **Orchestrator session:** A dedicated Claude Code instance whose job is to coordinate the other agents — checks their status, handles blockers, routes new work. The "AI command center." Better suited to teams or complex multi-step tasks.

**Practical limits:** Beyond 3–5 agents, coordination overhead becomes the bottleneck, not the agents themselves. DIY tmux + worktrees fits solo devs and small teams.

See [[claude-code-agent-teams]] (concept page) and [[orchestrate-agents]] (vault skill) for actionable detail.

---

Tools/entities: [[claude-code]], [[nate-herk]]. Concepts: [[selling-ai-automations]], [[agentic-workflows]], [[second-brain-system]].

**Raw clip:** [[Build & Sell with Claude Code (10+ Hour Course)]]
