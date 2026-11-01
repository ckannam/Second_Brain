---
type: concept
created: 2026-11-01
---

# Wiki Query (`wiki-query`)

The vault's primary **query operation** — the standard way to ask a question against this Second
Brain and get a synthesized, sourced answer filed back into the wiki. The pattern from
[[AGENTS.md]]'s Query section made executable as the `wiki-query` skill
(`.claude/skills/wiki-query/SKILL.md`). The vault's counterpart to the write-side operations
(ingest → `vault-improve`; self-heal + grow → `vault-autoresearch`).

> **How to invoke:** say "according to my notes, what is X?", "what does the vault say about Y?",
> "query the wiki for Z", or use `/wiki-query`. The skill auto-fires on those phrasings.
> A navigational lookup ("which page covers X?") is not a real query and doesn't trigger the
> full pipeline.

## The pipeline (5 steps)

1. **Index first.** Read `index.md` (the content catalog) before touching any wiki page. Knowing
   what already exists is how you enrich rather than duplicate.
2. **Graph traversal.** Drill into the relevant pages; follow cross-links to related pages.
   A query often spans 3–6 pages. Treat dangling links as signals — the absence of a page is
   part of the answer.
3. **Freshness pass.** Reconcile page content against what's currently known (the vault is a
   snapshot; claims age). Flag superseded claims rather than trusting them as live truth.
4. **Synthesize.** Answer with citations back to `[[wiki pages]]` and raw sources. The vault's
   knowledge, not general LLM knowledge, is the ground truth.
5. **File back.** Every real query answer becomes a new wiki page (or an update to an existing
   one). Cross-link it, add it to `index.md`, append to `log.md`. This is mandatory, not optional
   — answers that disappear into chat don't compound. Skip only for pure navigational lookups.

## Why file back?

The vault is a **compounding knowledge base**, not a Q&A session. Each query answer is new
synthesis the vault didn't have before — it should persist. Without the file-back step, the
same question re-runs fresh every session. With it, the second query on a related topic finds
prior synthesis already waiting.

## When it fires (trigger signals)

- "According to my notes, what is X?"
- "What does the vault say about Y?"
- "Query / search the wiki for Z"
- `/wiki-query` command
- Any question the human directs at the vault rather than at general knowledge
- Implicitly: any question about something that *has* wiki pages (Cole navigating his own
  second brain)

**Does NOT fire:** pure navigational lookup ("which page is X on?", "where did I save the
Fulbright abstract?"), live web lookup questions, action-item questions (→ `tasks/index.md`),
or ingest requests (→ `vault-improve`).

## Siblings (when to redirect)

| Need | Use |
|---|---|
| Ingest a new source | `vault-improve` skill |
| Self-heal or grow the wiki (overnight loop) | `vault-autoresearch` skill |
| Navigational lookup (which page is X?) | read `index.md` directly |

## Quality constraints

- **Never invent.** Everything in a query answer traces to a wiki page or raw source; synthesis
  is clearly labeled as such.
- **Links > text.** Prefer `[[page-name]]` references over re-quoting page content — the link
  is the citation and the connection.
- **Snapshots age.** Model capability claims, deadlines, and pricing in the wiki are dated
  snapshots. Surface the date and flag stale-looking claims when synthesizing.
- **File back.** Every real synthesis answer becomes a page. See step 5 above.

## Audit record

Formally audited against [[skill-authoring-playbook]] twice: once in the combined log
([[skill-audits-2026]], 2026-09-13) and once in the standalone page ([[skill-audit-wiki-query]],
2026-09-27 + 2026-10-04). Findings: §1–§2–§4–§6 clean; §3 has a minor Guardrails condensation
recommendation (partly restates AGENTS.md); §5 no evals (3 recommended in the audit page).

Related: [[vault-autoresearch]] · [[vault-improve]] · [[AGENTS.md]] · [[skill-audit-wiki-query]] ·
[[skill-authoring-playbook]] · [[index.md]] · [[Claude Mastery]].
