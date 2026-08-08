# Skill-authoring playbook

The actionable "how to write a [[claude-code-skills|skill]] that triggers reliably and stays
lean" checklist — the *build* companion to the [[claude-code-skills]] overview (which is the
*what*). Grounded in Anthropic's official **Skill authoring best practices**
(platform.claude.com/docs, 2026) plus the vault's skill sources
([[master-claude-code-skills-28min]], [[claude-code-skills-update]]) and the governance/eval
lens ([[governed-skills-framework]], [[evals-for-taste]]). This is the page Cole works from
when building or improving the vault's own skills (the **Claude Mastery** goal:
[[Claude Mastery]]). For the checklist **run end-to-end against a real skill** — verdict +
fix per section, plus a copy-paste audit template — see the worked example
[[skill-audit-worked-example]].

## The two failure modes a skill has

Every skill can fail in exactly two ways, and the playbook is organized around them:
1. **It doesn't fire when it should** (under-trigger) → a *description* problem.
2. **It fires but wastes context or misleads** (bloat / drift) → a *body & structure* problem.

Get the description right and it activates; get progressive disclosure right and it stays cheap.

## 1. The description is the trigger surface

At startup Claude pre-loads **only** each skill's `name` + `description` — never the body — so
the description is the *entire* basis on which Claude picks this skill out of 100+. Treat it as
the most load-bearing sentence in the whole skill.

- **What + when, both.** Pack in *what it does* **and** the *specific triggers/contexts* that
  should fire it. `description: Extract text and tables from PDF files… Use when working with
  PDFs, forms, or document extraction.` — not `description: Helps with documents`.
- **Third person, always.** The description is injected into the system prompt; "I can help you…"
  / "You can use this to…" cause discovery problems. Write "Processes Excel files and generates
  reports."
- **Key terms in, so retrieval hits.** Include the concrete nouns and file types a user would say
  (`.xlsx`, "pivot table", "commit message"). These are the match surface.
- **Be pushy against under-triggering.** Claude's default is to *under*-fire skills. Specific,
  confident triggers ("Use whenever the user mentions X, Y, or Z") beat timid ones. The vault's
  own skills lean into this — e.g. `standard-of-care` lists a dozen trigger phrasings.
- **Limits:** `name` ≤64 chars, lowercase/numbers/hyphens, no reserved words (`anthropic`,
  `claude`); prefer **gerund form** (`processing-pdfs`, `analyzing-spreadsheets`).
  `description` ≤1,024 chars, non-empty, no XML tags.

Description is also where **trigger tuning** happens: when a skill mis-fires or misses, the first
fix is almost always the description, not the body.

## 2. Progressive disclosure keeps it cheap

The context window is a public good ([[token-context-management]]). Structure the skill so tokens
load only when earned:

- **Three tiers of loading:** metadata (always) → `SKILL.md` body (on trigger) → reference files
  (on demand, read via bash, zero context cost until opened).
- **Body under ~500 lines.** Past that, split into `reference/*.md` files that `SKILL.md` links to.
- **References one level deep.** `SKILL.md → reference.md`, never `SKILL.md → a.md → b.md` — Claude
  may only `head -100` a nested file and get partial info.
- **TOC on any reference >100 lines** so a partial read still shows the full scope.
- **Domain-split large skills** (`reference/finance.md`, `reference/sales.md`) so a sales question
  never loads finance context.
- **Scripts are executed, not loaded** — a bundled `validate.py` costs only its *output* in tokens,
  never its source. Say explicitly whether Claude should *run* a script or *read it as reference*.

## 3. Be concise — assume Claude is already smart

Only add context Claude doesn't already have. Challenge each line: "Does Claude need this?
Can I assume it knows this? Does this paragraph justify its token cost?" A 50-token "use
pdfplumber, here's the call" beats a 150-token explanation of what a PDF is.

## 4. Match degrees of freedom to task fragility

The "robot on a path" heuristic:
- **Open field → high freedom.** Many valid approaches (e.g. a code review) → give direction in
  prose, trust Claude to route.
- **Narrow bridge → low freedom.** Fragile, consistency-critical, exact-sequence (e.g. a DB
  migration) → give the exact script and say "do not modify."
- **In between → medium.** A preferred pattern with parameters (pseudocode / templated script).

Over-constraining a flexible task wastes tokens and blocks good judgment; under-constraining a
fragile one invites errors.

## 5. Build evals *first*, then iterate with Claude

This is the core of "master reliable skill creation" — the discipline that separates a skill that
*documents an imagined problem* from one that *solves a real one*:

1. **Find the gap** — run the task with **no** skill; record the specific failures.
2. **Write ~3 evals** (query + files + `expected_behavior`) that test those gaps; measure the
   no-skill **baseline**.
3. **Write minimal instructions** — just enough to pass the evals; resist pre-emptive bloat.
4. **The Claude-A / Claude-B loop** — "Claude A" helps *author/refine* the skill; a fresh
   "Claude B" *uses* it on real tasks; you observe where B struggles and bring specifics back to
   A ("B forgot to filter test accounts — make that rule more prominent, use MUST not always").
5. **Watch how Claude navigates** — unexpected read order, ignored files, or a file read every
   time all signal a structure fix. `name`/`description` are the highest-leverage things to tune.

Evals are the skill's version of the vault's own **HEALTH_DEBT ratchet** ([[vault-autoresearch]])
and the enterprise **evals-for-taste** discipline ([[evals-for-taste]], [[llm-as-judge]]): an
objective signal that a change is an improvement, not a vibe. At org scale this eval + versioning
discipline is what makes a skill library *governable* ([[governed-skills-framework]]).

## 6. Anti-patterns to avoid

- **Time-sensitive info** ("before August 2025, use…") → put deprecated guidance in a collapsed
  "Old patterns" section instead.
- **Too many options** ("use pypdf or pdfplumber or PyMuPDF or…") → give one default + one escape
  hatch.
- **Deep nested references** (see §2) and **Windows-style paths** (`scripts\x.py`) → always forward
  slashes.
- **Inconsistent terminology** — pick one term ("field", "extract", "API endpoint") and keep it.
- **Voodoo constants** in scripts (`TIMEOUT = 47  # why?`) → justify every value; **solve, don't
  defer** (handle errors in the script rather than making Claude figure them out).
- **Vague `helper`/`utils` names** → name for the activity.

## Relation to the rest of the toolbox

A skill is one rung of the reusability ladder — reach for it when you keep repeating the same
instructions. When the job needs a *separate context* or *parallel work* instead of a reusable
procedure, that's a **sub-agent / agent team**, not a skill: see [[skills-vs-subagents]],
[[claude-code-subagents]], [[claude-code-agent-teams]], and the [[orchestrate-agents]] decision
ladder. Anthropic's **Skill Creator** scaffolds the folder + frontmatter, but Claude writes
well-structured `SKILL.md` content natively — no special "writing-skills" skill required
([[claude-code-skills-update]]).

Related: [[claude-code-skills]] · [[token-context-management]] · [[evals-for-taste]] ·
[[governed-skills-framework]] · [[skills-vs-subagents]] · [[master-claude-code-skills-28min]] ·
[[claude-code-skills-update]] · [[claude-code]].
