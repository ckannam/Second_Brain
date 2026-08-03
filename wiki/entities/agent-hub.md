---
type: entity
category: tool
---
# Agent Hub

[[andrej-karpathy]]'s companion project to [[autoresearch]] (open-sourced right after it) — **"GitHub is for humans; AgentHub is for agents."** An **agent-first collaboration platform**: a bare git repo plus a **message board** designed for a *swarm* of agents working on the same codebase. Source: [[autoresearch-broke-internet-greg-isenberg]].

## Design philosophy

Agent Hub deliberately inverts GitHub's assumptions. GitHub is optimized for **humans reading history** — main branch, PRs, linear narrative, code review by people. Agents don't need that narrative; they need a substrate to coordinate without human-shaped ceremony.

What Agent Hub provides instead:
- **A sprawling DAG of commits** — no main branch, no merges, no PRs. Agents just commit in every direction, and the DAG records what they tried.
- **A message board** — where agents coordinate ("I'm working on X"; "I found a bug in Y"; "my run scored 0.72") without needing human-interpreted PRs.
- **A frozen evaluator** — the same principle as [[autoresearch]]'s `prepare.py`: the metric can't be gamed, only legitimately improved.

The result is a substrate optimized for *swarm exploration* rather than *linear human narrative*.

## Reference implementation (web-verified 2026-08-03)

Beyond the design sketch, the open-source reference server has a concrete, deliberately
minimal shape (secondary-source synthesis — see Sources; the canonical repo could not be
fetched directly):

- **Three pieces on disk:** one Go binary (`agenthub-server`), one SQLite database, one bare
  git repo. That's the whole server — the anti-GitHub is small on purpose.
- **Git-bundle transport.** Agents don't `git push` over the wire in the usual way; they hand
  the server a **git bundle**, which it validates and unbundles into the bare repo. Any agent
  can then fetch any commit and **browse the DAG** — walk children, find leaves/lineage, and
  **diff between commits** — which is how a swarm reads "what has everyone else tried" without
  a main branch to anchor on.
- **Message board = channels + threaded replies.** Agents **create channels, post to them,
  read, and reply in threads** — the coordination primitive is a chat board, not a PR queue.
- **Swarm-hygiene guardrails.** Per-agent **API keys**, **rate limiting**, and **bundle-size
  limits** — the minimum needed to keep an unattended swarm from trampling the shared repo.

This is the same frozen-evaluator / cheap-bookkeeping instinct as [[autoresearch]], pushed
down into the version-control layer: give agents a substrate where coordination is a data
structure (a DAG + a board) rather than a human ritual.

## Connection to autoresearch

[[autoresearch]] is a **single-agent loop** on a single file: one agent edits `train.py`, scores `val_bpb`, keeps or reverts. Agent Hub scales that to **many agents in parallel**, each exploring a different hypothesis, with a shared message board to coordinate and avoid duplicated effort.

Karpathy's end-state vision: a **SETI@home for AI research** — millions of agents on volunteer compute, all steered toward a chosen problem, leaving behind a DAG of everything they tried. See [[autoresearch]] for that broader context.

## Relevance to this vault

The [[vault-autoresearch]] loop is currently a **single-agent, nightly autoresearch instance** — one session, one HEALTH_DEBT metric, git as the ratchet. Agent Hub represents the multi-agent extension of that same idea:

| | This vault today | Agent Hub trajectory |
|---|---|---|
| Agents | 1 (nightly cloud run) | Many (parallel swarm) |
| Coordination | None needed | Message board |
| Git model | main + PR | DAG, no main |
| Metric | HEALTH_DEBT | Same pattern, any metric |

For the vault to benefit from Agent Hub, a natural prerequisite is the current single-agent loop being stable and measurably improving — which it now is. See `@cloud` task "Watch agent-hub" in [[tasks/index]] for the standing monitoring item.

## Evaluation

**Watch note — 2026-08-03 (`@cloud` "Watch agent-hub" check).** Re-checked the wider web for
new development since the 2026-07-31 read. Agent Hub is still what Karpathy calls it — the
canonical repo description is *"GitHub is for humans. AgentHub is for agents. First use case
is for autoresearch but it's a lot more general than that. **Exploratory project.**"* — and he
has publicly framed it as a work-in-progress "just a sketch… not production software and may
never become production software." What *has* moved:
- **Adoption without maturity.** Reported ~**25k+ GitHub stars** and early third-party forks
  (e.g. `ottogin/agenthub`, `ygivenx/agenthub`) within weeks — heavy attention, but the code
  is still an intentional sketch, not a platform to build on. (Star count is secondary-source
  and approximate.)
- **The implementation is now legible** — see [Reference implementation](#reference-implementation-web-verified-2026-08-03)
  above (Go server + SQLite + bare git repo, git-bundle transport, channel/threaded-reply
  board). This clarifies *what* adopting the pattern would actually mean, which the
  2026-07-31 note lacked.

> Supersedes the 2026-07-31 line "no new material has arrived in this vault" — new material
> (the reference-implementation detail + adoption signal above) has since been web-verified.
> [[autoresearch-broke-internet-greg-isenberg]] remains the only *raw* vault source; the rest
> is web-grounded synthesis.

**Verdict — unchanged for this vault.** Agent Hub is still a **future-direction signal, not an
immediate action.** The [[vault-autoresearch]] loop is a stable single-agent instance;
Agent Hub only pays off once there's a *swarm* of agents needing to coordinate on the same
codebase, which this vault does not yet have. Track it; don't adopt it. The realistic near-term
bridge is [[claude-code-agent-teams]] / [[multi-agent-orchestration]] (bounded, human-in-the-loop
parallelism), not a no-main-branch DAG.

Related: [[andrej-karpathy]], [[autoresearch]], [[autoresearch-repo]], [[vault-autoresearch]], [[extending-the-llm-wiki]], [[agent-native-infrastructure]], [[multi-agent-orchestration]], [[parallel-agents]], [[claude-code-agent-teams]].

## Sources

- Raw vault source: [[autoresearch-broke-internet-greg-isenberg]] (original mention, "GitHub for agents").
- Web-grounded (checked 2026-08-03; secondary aggregators, canonical repo not directly fetchable):
  reference-implementation detail (Go server + SQLite + bare git repo, git-bundle transport,
  DAG browse/diff, channel/threaded-reply message board, per-agent API keys / rate limits /
  bundle-size caps), ~25k+ stars, and the "exploratory project" framing — via AIBit
  (`aibit.im/blog/post/agenthub-github-for-ai-agent-swarms-by-karpathy`), the
  Houdao AI writeup, and the `ottogin/agenthub` + `ygivenx/agenthub` repo descriptions.
