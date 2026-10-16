---
type: improvement-plan
target: AutoResearch source-seeking rung (MODE B extension) — [[extending-the-llm-wiki]] · [[autoresearch]] · [[proactive-agents]]
created: 2026-09-13
status: design proposed (@cloud slice); program.md wiring is Cole's call (rides the morning PR)
---

# Improve — the source-seeking rung (the vault researching *itself*)

**Target:** the nightly AutoResearch loop (`autoresearch/program.md`). **Vision** (from
[[extending-the-llm-wiki]]): close Karpathy's loop so the wiki doesn't just *heal and enrich what
it already has* but **finds the sources it is missing** — "a cron lint that finds graph gaps *and
seeks new sources* — the vault researching itself." This is the one roadmap rung
[[extending-the-llm-wiki]] still flags as open ("The scheduled *source-seeking* rung remains open").

This doc is the **cloud-safe, reviewable slice**: the design. It deliberately does **not** edit
`program.md` (the human-owned loop brain — "the human edits it; the loop follows it") or the frozen
`score.py`. Wiring it in is Cole's decision; this proposal is what that decision reads from. Same
split the loop already draws between its auto-merge fast-track and its review-lane PR.

## Diagnosis (gap to vision)

The loop today has three lanes that all work **inward** on the existing graph:
- **Phase 3 / MODE A** — objective self-heal (orphans → missing-from-index → stale-claims), scored.
- **Phase 4 / MODE B** — one generative enrichment *from material already in the vault or a
  fully-specified web lookup*.
- The `wiki-query` skill files answers back, but only for questions **Cole** thinks to ask.

Nothing proposes *what to read next*. The `tasks/index.md` **"Sourcing & verification"** section
exists precisely for this and today reads **"(no open items)"** — the loop never fills it. New
inputs arrive only when Cole hand-drops a clip into `raw/assets/`. So the graph's freshness is
capped by Cole's manual sourcing, and the parts that age fastest (model/tool capability claims —
the AGENTS.md **snapshot** principle) silently rot between ingests.

## Design — a bounded MODE-B sub-mode ("MODE B-src")

The rung is **proposal-only**: it never ingests, never writes claims into `wiki/` as fact, never
takes an outward action. Its entire output is **one prioritized `tasks/index.md` entry under
"Sourcing & verification"** — a candidate source, why it matters, and what it would refresh — for
Cole to accept (→ he drops the source in `raw/assets/` and the normal AGENTS.md ingest runs) or
reject. That keeps it squarely in the review lane and honors "never fabricate," "no outward action,"
and the verification discipline.

### Where it looks (the gap signals, cheapest first)

1. **Staleness gaps (highest value).** The AGENTS.md snapshot rule says model/tool claims age fast.
   Scan `wiki/` for pages carrying a dated capability claim or a `point-in-time`/`snapshot` marker
   (e.g. [[claude-code]], [[claude-code-skills]], [[opus-4-6]], [[claude-code-memory]],
   [[claude-code-subagents]]) whose subject has likely moved since the page's last edit → propose
   the primary source that would refresh it (a release-notes page, a changelog, an official doc).
2. **Dangling-concept gaps.** A `[[link]]` that many pages point to but no page owns, *and* that
   isn't a local/personal file (not `crm/`, `profile/`, `finance/`), signals a concept the graph
   wants but has no grounding source for. (Tonight's dangling-link scan shows almost all of these
   are local CRM/profile pages — correctly out of scope — which is itself a useful signal that the
   *public* graph has few true content gaps right now.)
3. **Anchor-author signals.** The vault has named intellectual anchors — [[andrej-karpathy]]
   (the [[llm-wiki-pattern]] itself), Anthropic ([[claude-code]] et al.). New primary output from an
   anchor that the vault already tracks is a high-precision candidate.
4. **Active-goal frontier.** Cross-reference the open `@cloud`/`@human` goals in `tasks/index.md`
   (Claude Mastery, Neuro channel, Fulbright thesis) against recent public material — propose a
   source only when it maps to a *named existing page* it would enrich.

### How it filters (precision over recall — this is the whole risk)

A proposal is emitted **only if all hold** (mirrors the Doability rubric's "when unsure → skip"):
- it maps to a **named existing page** it would refresh or a **≥2-inbound dangling concept** it
  would ground (no speculative net-new topics);
- it is a **primary or reputable source** (official docs/changelog, the anchor's own post, a paper)
  — not an SEO listicle;
- it is **cloud-reachable & non-personal** (honors `@local`/`@human` lanes and the egress policy);
- **cap: one proposal per run.** The bottleneck is Cole's review attention, not source supply —
  so the rung is tuned hard against spraying the board (the same "no thin filler" rule as MODE B).

### What it writes (the only mutation)

One checkbox under **`tasks/index.md` → Sourcing & verification**, in the standard lane format:

```
- [ ] @human **Ingest+verify: <source title>** — refreshes [[page-a]], [[page-b]]; likely-stale:
  <one line>. Primary source: <url>. Surfaced by MODE B-src <date>. (added <date>)
```

`@human` because ingesting new factual claims needs Cole to verify against primary sources before
they become wiki truth — the AGENTS.md **snapshot / never-invent** discipline. (A pure
*re-verification* of an existing page against a known primary URL could be `@cloud`; a *new* source
is `@human`.)

### Guardrails (why this is safe to auto-run)

- **Proposal-only** — zero writes to `wiki/`, zero ingests, zero outward actions.
- **Frozen boundaries untouched** — never edits `score.py` or `raw/`.
- **Review lane** — the one `tasks/index.md` line rides the morning PR; nothing reaches `main`
  unreviewed. HEALTH_DEBT is unaffected (the scorer only scans `wiki/` + `crm/`).
- **Rate-limited** — one proposal/run; if no candidate clears the filter, it writes nothing and
  says so (a clean no-op, like a debt-0 heal night).

## Plan (venue-tagged; highest-leverage first)

- **1. [human] Approve the sub-mode.** Decide whether MODE B-src becomes a standing part of Phase 4
  (e.g. "Phase 4 alternates: enrichment one week, source-seeking the next," or "both, capped at one
  each"). This doc is the artifact for that decision.
- **2. [cloud, on approval] Wire it into `program.md`** as a Phase-4 sub-mode with the filter +
  one-proposal cap above. Small, additive edit to the loop brain — but a loop-brain edit, so it
  waits for step 1.
- **3. [cloud] Keep the "Sourcing & verification" section live.** Once wired, each run either adds
  one proposal or logs a clean no-op — the section stops being permanently empty.
- **4. [cloud, later] Optional: a staleness marker convention.** If pages carried an explicit
  `verified: <date>` note on capability claims, signal #1 would go from heuristic to exact — but
  that is a scorer/schema change (touches the AGENTS.md schema), so it's a separate human decision,
  not part of this rung.

## First live run (see Phase 4 tonight)

To prove the design isn't abstract, tonight's MODE B ran the rung **once, by hand**, against
signal #1 (staleness) + #3 (anchor-author) and emitted exactly one proposal — filed under
`tasks/index.md` → Sourcing & verification. See that entry and `autoresearch/results.tsv`.

Related: [[extending-the-llm-wiki]] · [[autoresearch]] · [[vault-autoresearch]] · [[proactive-agents]] ·
[[claude-code-scheduled-tasks]] · [[ingest-query-lint]] · [[llm-wiki-pattern]].
