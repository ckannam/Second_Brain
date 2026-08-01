---
type: concept
created: 2026-08-01
---
# Agentic Automation Patterns

Reusable design patterns for building autonomous agentic automations — the "how"
beneath the general concept of [[agentic-workflows]]. Where that page explains *why*
agentic beats deterministic, this page catalogues *how to structure* the agent so it
runs safely and resiliently unattended.

## Core patterns

### 1. Human-in-the-loop (HITL) gates
Insert an approval checkpoint before the agent takes an irreversible or high-risk action.
The key discipline: **maximize agent autonomy for low-risk steps; gate only the high-stakes
ones.** A HITL gate that blocks every small decision is just a slow human workflow.

Implementations in the Claude ecosystem:
- **[[claude-code-permissions|Auto Mode]] + deny rules** — let the agent proceed freely
  within allowed actions; specific destructive tools (write, push, delete) require human
  approval automatically. See [[claude-code-permissions]] for deny-rule setup.
- **Plan mode (read-only first)** — agent proposes; human approves the plan before execution
  starts. Good for first runs of a new automation.
- **Structured output + async check** — agent writes a decision to a file/log; a human
  approves asynchronously; the next run picks up the decision. Works well with
  [[claude-code-scheduled-tasks]] where each run is a fresh stateless session.

Pattern rule (from best practice): the *application* owns execution control, path safety,
audit logs, and command allowlists; the *model* owns reasoning and tool selection.

### 2. Retry and circuit-breaker
Agents encounter transient failures (rate limits, network blips, external-API errors). Good
retry design:
- **Exponential backoff with jitter** — prevents thundering-herd retries from compounding the
  problem.
- **Idempotency first** — only retry operations that are *proven idempotent* (re-running
  won't duplicate a transaction). For unknown outcomes (payment, email), query the destination
  using an idempotency key *before* retrying.
- **Circuit breaker** — after N consecutive failures, stop retrying and escalate (alert, log,
  move to the next item). Avoids runaway loops burning tokens on a permanently broken service.
- **Retry budget** — cap total retries per run (not per call) so a pathological case doesn't
  consume the whole scheduled window.

### 3. Heartbeat loop (scheduled + conditional)
Pattern: **wake on schedule → check condition → act if needed → sleep → log**.

Variations:
- **[[claude-code-scheduled-tasks|Scheduled task]]** (calendar-based, indefinite, fresh
  session each run) — best for daily/nightly jobs. The results file is the cross-run memory.
- **[[claude-code-loops.md|Loop]]** (short repeating interval, ≤3 days, same session window)
  — best for continuous polling within a bounded experiment window, e.g. "check every 5 min
  for 48 hours then stop."
- **GitHub Actions cron** — external trigger, runs in cloud regardless of machine state.
  [[nick-saraev]]'s cold-email optimizer and this vault's own nightly routine use this pattern.

The self-improving variant: the agent fixes its own script, refines its own prompt, and
overwrites a status/results file — each run starts from the last run's outcome. See
[[self-healing-workflows]] and [[autoresearch]] for the git-as-ratchet extension.

### 4. Single-file state / results log
The cheapest cross-run memory for a stateless scheduled agent: write one structured line per
run to a `results.tsv` or `status.json`. The next run reads it to know where things stand.
No database, no external state. Used throughout this vault (`autoresearch/results.tsv`) and
recommended in [[claude-code-scheduled-tasks]] as the standard cross-run memory pattern.

### 5. Scoped tool permissions (blast-radius control)
Run agents with the **minimum necessary tool scope**. In practice:
- Use [[claude-code-permissions|Auto Mode]] + explicit deny-rules for destructive tools.
- Scope file-write access to specific directories — agents that can only write to `output/`
  can't accidentally clobber `src/`.
- For multi-agent setups ([[claude-code-agent-teams]]), give each agent write access to
  non-overlapping paths to eliminate race conditions.

## Anti-patterns to avoid

| Anti-pattern | Why it hurts | Fix |
|---|---|---|
| Unbounded retry loop | Burns tokens/budget on a permanently broken step | Add circuit breaker + retry budget |
| Blind retry on unknown outcome | Risk of duplicate transactions | Query idempotency key first |
| Hidden state | Next run can't tell if prior run succeeded | Write explicit results log each run |
| Over-broad tool scope | Agent touches files it shouldn't | Scope with deny-rules |
| HITL on every step | Defeats the automation | Gate only irreversible/high-risk actions |
| No audit log | Can't diagnose failures overnight | Every run writes a timestamped row |

## Where these fit in the vault

The [[vault-autoresearch]] loop implements patterns 2 (git-as-ratchet / commit-or-revert),
3 (nightly heartbeat), 4 (results.tsv cross-run memory), and 5 (deny-rules for score.py +
raw/) in a single nightly automation. [[self-healing-workflows]] covers the self-repair
variant. [[agentic-workflows]] covers the general case.

Related: [[agentic-workflows]], [[self-healing-workflows]], [[claude-code-scheduled-tasks]],
[[claude-code-loops]], [[claude-code-permissions]], [[claude-code-agent-teams]],
[[vault-autoresearch]], [[autoresearch]].
