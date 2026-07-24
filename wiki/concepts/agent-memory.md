# Agent memory

Persistent storage that lets an agent **carry learnings forward** so each task improves on
the last — and, critically, learn **agent→agent** and **environment→environment**, not just
within one session. The [[claude-managed-agents]] memory primitive (from
[[memory-and-dreaming-self-learning-agents]]) is Anthropic's production take.

## Design
- Modeled as a **file system** — "get out of Claude's way; let it cook." [[opus-4-7]] is SOTA
  at file-system memory (deciding what to save, how to structure it). Same philosophy as
  [[claude-code-skills|skills]].
- Three layers: **storage** (change tracking), **structure** (Claude-optimal format),
  **Claude-driven processing** (take notes while working).
- Multi-agent: shared stores with **read-only vs read-write scopes** (org-wide read-only +
  granular read-write → a hierarchy), **optimistic concurrency control** for write conflicts.
- Enterprise: version history, diffs, per-agent **attribution**, standalone **memory API**
  (CRUD + exports/redactions).

Its failure mode at scale — locally-but-not-globally-optimal updates — is what
[[agent-dreaming]] fixes. Consumer analogue: [[claude-code-memory]] (CLAUDE.md + Auto Dream).
Related: [[the-capability-curve]], [[proactive-agents]].
