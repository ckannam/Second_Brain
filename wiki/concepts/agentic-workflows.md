# Agentic Workflows

The vault's central technical theme: automations built as **autonomous AI agents** (via [[claude-code]]) rather than fixed node graphs. An agent reads the whole project, uses all its tools, and **self-heals** on errors instead of failing on a fixed step.

## Agentic vs deterministic
- **Deterministic** (scripts, [[n8n]]): step 1→2→3; on error it just fails. Predictable but brittle.
- **Agentic**: sees context, tries alternatives, fixes itself, and can improve over time. You trade some predictability for robustness — but you can force determinism by having the agent just run a script. See [[agentic-vs-deterministic]].

## Why it matters (per [[nate-herk]])
- The high-leverage skill for 2026 — "the third AI wave" — over learning [[n8n-vs-claude-code|n8n]].
- Premium value: packaged agentic workflows sell for **$10k+**. See [[selling-ai-automations]].
- Self-healing: agents fix broken pipelines automatically ([[self-healing-workflows]]).

## The frontier form: self-optimizing loops
The most autonomous version of an agentic workflow closes the loop on **improving itself**: not just self-healing on errors, but running experiments against a metric and keeping only the winners. [[andrej-karpathy]]'s [[autoresearch]] is the canonical example (edit one file → train → score `val_bpb` → keep or `git reset` → repeat forever), and creators have ported the pattern onto business metrics — e.g. [[nick-saraev]]'s cold-email reply-rate optimizer. See [[autoresearch]] for the mechanism and its limits (needs an objective metric + automated eval + one changeable input).

## Sources
[[how-to-build-10k-agentic-workflows]], [[from-zero-first-agentic-workflow-26min]], [[how-id-teach-10-year-old-agentic]], [[agentic-workflows-changed-automation]], [[stop-learning-n8n-2026]], [[build-sell-claude-code-course]]. Self-optimizing frontier: [[autoresearch-repo]], [[autoresearch-tutorial-david-andre]]. Scale up via [[claude-code-agent-teams]] and [[claude-code-scheduled-tasks]].

For specific implementation patterns (HITL gates, retry loops, circuit breakers, scoped permissions), see [[agentic-automation-patterns]].
