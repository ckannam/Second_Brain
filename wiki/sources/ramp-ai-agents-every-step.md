---
type: source
source: youtube
channel: "Anthropic (Office Hours; host Boris Cherny)"
title: "How Ramp engineers work with AI agents at every step"
url: "https://www.youtube.com/watch?v=i4odXOmgMLw"
created: 2026-08-07
raw: "raw/Processed/How Ramp engineers work with AI agents at every step.md"
---

# Source: Ramp — AI agents across the entire engineering lifecycle

[[boris-cherny|Boris Cherny]] (Head of [[claude-code|Claude Code]]) interviews **Austin Ray** and
**Rahul Sengottuvelu** of **Ramp** (the fintech spend-management company) on how Ramp runs AI agents
across its *whole* engineering lifecycle — ideation, writing code, review, production monitoring, and
incident root-causing. A real-world, in-production corroboration of the vault's [[ai-native-engineering-org|
AI-native org]] thesis. (Channel inferred as Anthropic's Office Hours from Boris hosting + the
claude.com/office-hours reference; not stated verbatim in the clip.)

## Key takeaways

- **[[fable-5|Fable 5]] cleared a bar no prior model did.** Rahul keeps a private suite of hard tests he
  gives every new model; Fable is "the first model that just did all the things." In production (shadow
  mode for weeks) he had Fable **fix all the import cycles** in Ramp's large monolithic Python codebase
  and **make the app boot lazily** — large, deep-codebase refactors, much of it merged. → a customer,
  in-prod data point that **upgrades the vault's [[fable-5]] stub from rumor to corroborated frontier use.**

- **"Dynamic workflows" = a new form of [[test-time-compute]].** Claude orchestrates a swarm of
  sub-agents in a sandbox (parallel/serial, extra rounds of adversarial verification as the task needs).
  Mental model: a thinking dial **low → medium → high → extra-high → max** — the *maximum* compute the
  model may spend. Used it to cut Ramp's **CI time from 18-min → 6-min P50 (~66%)**, where the agent
  landed an optimization, **used a routine to reschedule itself a day later** to grab real production
  data, and repeated for days until it had all the wins.

- **Loops vs. dynamic workflows (two automation shapes):** [[claude-code-loops|Loops]] = *repetitive,
  known* work — a **horizontal slice** of the one task every engineer does daily (babysitting PRs, fixing
  CI, rebasing, a routine that **deletes dead code every day**). **Dynamic workflows** = *dynamic, unknown-
  steps* work (system optimization, where you don't know the next move). The **vertical slice** is
  [[claude-tag|Claude Tag]]: "tag, ship an experiment" → it lands the PR, sets itself a reminder to check
  the next day, balances exposures, cranks them, and weeks later ships the winning variant — *"I wasn't in
  the loop at all."*

- **Build for the model that's *coming*, not today's** → its own page: [[build-for-future-models]]. Ramp
  deliberately under-builds scaffolding because the next model outgrows the harness; they repeatedly
  *delete* their own harness code. A **velocity bet**: elaborate present-day scaffolding becomes tech debt
  fast. The CTO-advice punchline: watch the *rate of change*, build for **3–6 months out**.

- **Guardrails = least privilege + trace study, not vibes.** Give the model exactly what it needs and
  nothing more — **read-only service keys** to BigQuery/Datadog, network access policies set up *by the
  security team* (who are also heavy agent users). They study **individual traces** ("what's the *correct
  trace* — the command it should have run — and why didn't it get there?") over aggregate benchmarks, and
  shape the agent to that trace via prompts/tools/skills. Prompts stay **declarative** ("the iPhone
  experience": say *what* you need, not *how*). Ties to [[agent-security-risks]], [[brain-hands-decoupling]],
  [[mechanism-over-output]].

- **Internal agent products:** **Glass** (home base where *non-technical* staff interact with the coding
  agent), **Inspect** (a "digital coworker" with GitHub/Linear/Slack/Datadog/Sentry access; solves
  support tickets, fixes issues, runs on Modal in the background, multiplayer via `@Inspect` in Slack —
  which is how adoption *spread*), and an **on-call assistant / AI SRE on Claude Code** (running since
  ~Feb–Mar 2026) that root-causes every incident and puts up fix PRs.

- **More agent sessions now come from automations than from humans.** Triggered/scheduled sessions
  outnumber human-initiated ones; the org is **decentralized** — any team builds what it wants on the
  shared Inspect abstraction.

- **No token budgets for engineers.** Uncapped access to "any level of intelligence"; instead they manage
  cost with defaults (batch/flex APIs, cheaper models for non-human automations) and *reach out to top
  spenders* to platformize what's working. The economic frame: **once you're ROI-positive (each $1 of
  tokens makes >$1), stop minimizing cost** — push the frontier and let it sweat on hard problems. Ties to
  [[cost-per-successful-outcome]].

## Why it matters to Cole
This is the **outside, in-production validation** of the patterns this vault already runs — [[claude-code-loops|
loops]], [[claude-code-scheduled-tasks|scheduled routines]], [[self-healing-workflows|self-healing]], and
least-privilege [[agent-security-risks|guardrails]]. Ramp is also on Cole's own cold-email discovery list
([[cold-email-job-search]]) and a marquee AI-native operator culture — useful texture for the [[Job Search|
health/bio/AI-adjacent operator lane]] and directly feeds the [[Claude Mastery]] bucket. Freshness: it
**corroborates [[fable-5|Fable 5]]** as the current frontier from a real customer, not a creator rumor.

Related: [[ai-native-engineering-org]] · [[running-ai-native-engineering-org]] · [[future-of-work-claude-tag]] ·
[[build-for-future-models]] · [[test-time-compute]] · [[claude-code-loops]] · [[agent-security-risks]] · [[fable-5]].
