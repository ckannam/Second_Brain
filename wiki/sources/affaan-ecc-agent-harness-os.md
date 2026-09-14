---
type: source
source: github
url: "https://github.com/affaan-m/ECC"
created: 2026-09-12
clipped: 2026-09-11
---
# affaan-m/ECC — the agent harness operating system (README)

GitHub README for **[[ecc|ECC]]**, a solo-maintained MIT "agent harness OS" that packages
plan→test→implement→review→verify→remember→improve into an installable plugin for [[claude-code]]
and ~12 other harnesses. Clipped into `raw/assets/`; ingested for **what it teaches about Claude
Code usage that the vault didn't already cover**, not as software to adopt.

## Why Cole surfaced it
Cole asked what ECC teaches beyond his current Claude Code setup (the `superpowers` plugin + his
file-memory + home-grown vault skills), and to fold the most helpful lessons into the vault.

## Verdict
**Don't install; mine the patterns.** ECC's core workflow spine is ~70% redundant with the
`superpowers` plugin Cole already runs, its 291-skill catalog advertises itself into context
(a [[token-context-management|context tax]] it elsewhere warns against), and it is a large
third-party trusted-code surface ([[agent-security-risks]]). The README doubles as a sales page
(sponsor/affiliate links, repeated "official sources only" malware warnings). Treat it as a **spec
for upgrades to Cole's own setup.**

## The five net-new lessons (captured across the graph)
1. **Instincts / continuous-learning** — confidence-scored patterns auto-extracted from sessions and
   injected at `SessionStart`; `/learn` → `/evolve` → `/prune`. OSS analog of [[agent-dreaming]];
   a structured layer over [[claude-code-memory]]. Cole runs no instinct store today.
2. **Hooks as enforcement + recipes** — "please use TDD" → a deterministic [[claude-code-hooks|hook]];
   secret-scan, typecheck-on-edit, dev-server/tmux guard, git-push gate. Plus the
   plugin-`hooks.json` double-fire gotcha (see [[claude-code-hooks]]).
3. **Rules as a distinct always-loaded layer** — selective language/project standards separate from
   skills (on-demand) and hooks (out-of-model). See [[token-context-management]], [[instructions-as-code]].
4. **Concrete context-economy knobs** — `CLAUDE_CODE_SUBAGENT_MODEL=haiku`,
   `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50`, `MAX_THINKING_TOKENS`; **MCP budget <10 servers / <80 tools**
   (else 200k → ~70k). See [[token-context-management]].
5. **Scan the harness itself (AgentShield)** — audit `CLAUDE.md`/settings/hooks/MCP/skills for
   injection, secrets, over-broad permissions; red/blue/auditor agent pipeline. See [[agent-security-risks]].

## Recommended follow-ups (sources worth clipping into `raw/` next)
ECC's depth lives in three linked guides not yet in the vault — highest-value first:
- **The Longform Guide** — context economics, memory persistence, eval/verification loops,
  parallelization, sub-agent iterative-retrieval. *Most implementable for Cole.*
- **The Security Guide** — prompt injection, hook/MCP threat model, config auditing.
- **The Shorthand Guide** — foundations / day-one setup.

Snapshot: release 2.2.1 (2026-08-31); README cites Opus 4.6 — reconcile vs [[opus-4-8]].
Ingested 2026-09-12. Related: [[ecc]], [[claude-code]], [[agent-dreaming]], [[token-context-management]],
[[claude-code-hooks]], [[agent-security-risks]], [[openclaw]], [[paperclip]].
