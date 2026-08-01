---
type: concept
created: 2026-08-01
---
# Writing reliable skills

The *craft* behind [[claude-code-skills|Claude Code skills]] — how to author a skill that
**triggers when it should**, **costs the least context**, and **holds up on the edge cases**.
The overview page says *what* a skill is; this page is the "**skill max**" track: the
authoring technique, grounded in Anthropic's official [skill-authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
and the vault sources [[master-claude-code-skills-28min]] and [[claude-code-skills-update]]
(Skill Creator + evals).

## The three levers (each governs a different failure)

A skill can fail three distinct ways; each has its own lever:

1. **The `description` decides whether the skill runs at all.** At startup only every
   skill's `name` + `description` is preloaded into the system prompt; Claude picks from
   potentially 100+ on that text alone. So the description is the **trigger surface** — the
   single highest-leverage field.
2. **Progressive disclosure decides how much context it costs.** `SKILL.md` is read only
   when the skill fires; reference files are read only when linked to and needed. Structure
   controls the token bill.
3. **"Explain the why" + known gotchas decide whether it handles the edge cases.** Once
   loaded, the body's clarity and completeness determine whether Claude gets the fragile
   steps right.

The rest is how to pull each lever.

## Lever 1 — the description (trigger surface)

- **Third person, always.** The description is injected into the system prompt; a first/second
  person voice ("I can help you…", "You can use this to…") causes discovery problems. Write
  "Processes Excel files and generates reports."
- **State both *what* it does AND *when* to use it**, with specific trigger terms/file types.
  Good: *"Extract text and tables from PDF files, fill forms, merge documents. Use when working
  with PDFs, forms, or document extraction."* Bad: *"Helps with documents."*
- **Lean slightly pushy.** Claude has a measured tendency to **under-trigger** skills, so the
  Skill Creator recommends descriptions that err toward firing. Under-triggering (skill never
  runs) is the more common failure than over-triggering.
- Limits: `name` ≤ 64 chars, lowercase-hyphen only, no `anthropic`/`claude`; `description`
  ≤ 1,024 chars. Prefer **gerund naming** (`processing-pdfs`, `analyzing-spreadsheets`); avoid
  `helper`/`utils`/`tools`.

## Lever 2 — progressive disclosure (context cost)

- **Keep the `SKILL.md` body under ~500 lines.** Past that, split into reference files. One
  real data point: splitting a 1,200-line "mega skill" into a ~200-line `SKILL.md` + three
  supporting files improved instruction-following by nearly **40%**.
- **`SKILL.md` is a table of contents**, not the whole manual — a high-level guide that points
  to `REFERENCE.md`, `EXAMPLES.md`, domain files, and scripts loaded only when needed.
- **Keep references one level deep.** Nested references (SKILL → advanced → details) get
  partially read (`head -100`) and produce incomplete information. Link every reference file
  directly from `SKILL.md`.
- **Scripts execute, they don't load.** A bundled utility script consumes zero context until
  run — only its *output* costs tokens — so prefer a pre-made `validate.py` over asking Claude
  to regenerate the code (more reliable + consistent). Make execute-vs-read intent explicit.
- Reference files > 100 lines get a **table of contents** at the top so a partial read still
  reveals the full scope.

## Lever 3 — the body (edge cases)

- **Concise is key — assume Claude is already smart.** Only add what Claude *doesn't* already
  have; challenge every paragraph's token cost. Don't explain what a PDF is.
- **Set the right degrees of freedom** (the "robot on a path" analogy):
  - *High freedom* (prose steps) when many approaches are valid — e.g. a code review.
  - *Low freedom* (an exact script, "do not modify the command") when the operation is fragile
    and consistency is critical — e.g. a database migration. Narrow bridge → guardrails; open
    field → general direction.
- **Workflows + checklists** for multi-step tasks: give a copy-in checklist Claude ticks off,
  so it can't skip a validation step.
- **Feedback loops:** the *run validator → fix → repeat* pattern (a script **or** a
  `STYLE_GUIDE.md` as the "validator") sharply improves output quality.
- **Plan-validate-execute** for batch/destructive work: emit a structured plan file, validate
  it with a script, *then* execute — catches errors before they land.
- **Consistent terminology** (always "field", never a mix of field/box/element) and **no
  time-sensitive info** (use an "old patterns" `<details>` block instead of "before August…").

## The eval/iteration loop (how skills actually get reliable)

Reliability is *found*, not written — via evals, matching the vault's own
[[eval-driven-model-selection|evals-before-edits]] discipline (the same rule the
[[prompt-engineering-playbook]] applies to prompts):

- **Build evals first — before extensive docs.** Run Claude on representative tasks *without*
  the skill, document the specific failures, then write **three** eval scenarios
  (skills / query / files / `expected_behavior`) that target those gaps and establish a
  baseline. Write just enough skill content to pass them, then iterate. (There's no built-in
  runner yet — you build the harness; the eval set is your source of truth.)
- **Claude A builds, Claude B uses.** Develop the skill with one Claude instance ("A") and
  test it on real tasks with a fresh instance ("B") that has it loaded. Watch **Claude B's
  behavior** — where it struggles, which files it never opens, which references it misses —
  and bring specifics back to A. Claude natively understands the skill format, so no
  "meta-skill" is needed to author one.
- **Trigger tuning is an eval, not a guess.** If B doesn't fire the skill when it should,
  the fix is in `name`/`description`; if it fires but botches a step, the fix is in the body
  or a stronger imperative ("MUST filter" > "always filter"). Variance/benchmark analysis
  across runs tells reliable from lucky — the job of Anthropic's **Skill Creator + evals**
  ([[claude-code-skills-update]]).

At org scale this loop *is* the [[governed-skills-framework]]: versioned, evaluated, centrally
governed skills (Man Group ran 100+ across ~750 developers) so a better idea is
distinguishable from a different measurement.

## Anti-patterns

Windows-style backslash paths (break on Unix); offering too many options instead of a default
with an escape hatch; "voodoo constants" in scripts (`TIMEOUT = 47 # why?`); assuming a
package is installed; deferring errors to Claude instead of handling them in the script.

## The vault's own skills

This vault is a live testbed for all of the above — `.claude/skills/` holds `vault-autoresearch`,
`wiki-query`, and the three prompt-architect skills (the "[[prompt-engineering-playbook|prompt max]]"
track). Every one is a description (trigger surface) + a body + progressive-disclosure references,
tuned by watching whether it fires on the right request.

Related: [[claude-code-skills]] · [[skills-vs-subagents]] (when a skill vs a subagent) ·
[[claude-code-subagents]] · [[ai-second-brain-levels]] (Level 3 = skills) ·
[[eval-driven-model-selection]] · [[governed-skills-framework]] · [[token-context-management]]
(progressive disclosure is context economy).
