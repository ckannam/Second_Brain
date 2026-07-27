# vault-improve Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Because this builds a *skill* (a markdown SKILL.md), the authoring sub-skill for the content is **superpowers:writing-skills** — read it before Task 1.

**Goal:** Build a `vault-improve` skill: say `improve [target]` and get a vision-diagnosis + venue-tagged (`[local]`/`[cloud]`/`[human]`) plan that stops for approval before executing only the local parts.

**Architecture:** A single thin-router `SKILL.md` at `.claude/skills/vault-improve/`, matching the pattern of `wiki-query` and `vault-autoresearch` — it points at `AGENTS.md` as the source of truth and states only the trigger + procedure + guardrails. Plans it produces are persisted to a new `tasks/improvements/` folder. No code, no scorer; judgment-driven, separate from the autoresearch ratchet.

**Tech Stack:** Markdown (Claude Code skill format with YAML frontmatter). No runtime dependencies.

## Global Constraints

- `AGENTS.md` is the single source of truth and wins on any conflict; the skill must **not restate** its rules — only route to it. (verbatim from spec)
- Improvement = a denser, more current, better-connected graph. **Links > pages. Enrichment before creation. Never invent facts.** (verbatim from spec)
- Separate from `vault-autoresearch`: may *read* `python3 autoresearch/score.py` as one signal, **never bound by the ratchet, never edits the scorer**, never edits anything under `raw/`. (verbatim from spec)
- Every plan step the skill emits carries exactly one venue tag: `[local]`, `[cloud]`, or `[human]`. (verbatim from spec)
- Hard approval gate: after writing a plan the skill STOPS; only `[local]` runs after the user says go; `[cloud]`/`[human]` never auto-run and are never auto-merged. (verbatim from spec)
- Primary targets (weight here): (1) skills/vault machinery, (2) projects — grant finder, JHTV second brain. Others secondary. (verbatim from spec)
- Skill name `vault-improve`; plan files at `tasks/improvements/YYYY-MM-DD-<target>.md`. (verbatim from spec)

---

## File Structure

- **Create** `.claude/skills/vault-improve/SKILL.md` — the entire skill (frontmatter + procedure + guardrails). One responsibility: route + define the improve procedure.
- **Create** `tasks/improvements/.gitkeep` — establish the plan-output folder so the skill's step 3 has a home from day one.
- **Modify** none required. (`AGENTS.md` is deliberately not touched — the skill routes to it. If, during review, we decide the vault schema should *mention* the improve op, that is a separate `improve AGENTS.md` run per the spec's out-of-scope note.)

---

### Task 1: Author the `vault-improve` SKILL.md

**Files:**
- Create: `.claude/skills/vault-improve/SKILL.md`
- Reference (read-only, do not edit): `AGENTS.md`, `.claude/skills/vault-autoresearch/SKILL.md`, `.claude/skills/wiki-query/SKILL.md`
- Verify against: `docs/superpowers/specs/2026-07-27-vault-improve-design.md`

**Interfaces:**
- Consumes: nothing (first task).
- Produces: a skill named `vault-improve` triggered by "improve X" / `/vault-improve`, whose body defines the 5-step procedure (Resolve target → Diagnose → Write tagged plan → Approval gate → Execute+report) that Task 3 dry-runs.

- [ ] **Step 1: Read the sibling skills and writing-skills guidance for the house style**

Read `.claude/skills/wiki-query/SKILL.md` and `.claude/skills/vault-autoresearch/SKILL.md` to match tone and the "thin router to AGENTS.md" convention. Confirm the frontmatter shape: `---\nname: <kebab>\ndescription: <trigger sentence(s)>\n---`.

- [ ] **Step 2: Write the frontmatter (the "failing test" is the description trigger)**

The `description` is what makes the skill fire. Write it so a bare "improve X against the vault" routes here, and so it disambiguates from `vault-autoresearch` (metric loop) and `wiki-query` (questions):

```yaml
---
name: vault-improve
description: Use when the user says "improve" a target in this Second Brain vault — a skill/workflow (a SKILL.md, AGENTS.md, the ingest process), a project (grant finder, JHTV second brain), a bucket/life-area, a wiki page, a task item, or bare "improve" for the whole vault. Diagnoses the gap to Cole's vision and writes a venue-tagged (local/cloud/human) plan that waits for approval before executing. For the autonomous metric-driven heal loop use vault-autoresearch; for answering a question from the vault use wiki-query.
---
```

- [ ] **Step 3: Write the body — overview + the invariants that mirror Global Constraints**

Keep it thin. Open with one paragraph: what improve is, and that `AGENTS.md` is the source of truth and wins on conflict (do not restate it). Then an "Invariants" list copying the Global Constraints above in skill voice (links>pages, enrich before create, never invent facts, separate from autoresearch/never edit score.py or raw/, every plan step tagged, hard approval gate).

- [ ] **Step 4: Write the Procedure section — the 5 steps from the spec, verbatim in intent**

Write the numbered procedure exactly matching the spec §Procedure:
1. **Resolve the target** — list target types primary-first (skill/workflow/schema; project/bucket; then wiki page, task item, whole-vault). Ambiguous → ask one sharp question.
2. **Diagnose against the vision** — the four grounding sources (AGENTS.md; Cole's profile+memory+buckets/journal; the target's own graph; optional score.py). Output a short gap diagnosis in LLM-Wiki terms (missing links, thin/orphan pages, stale claims, uncited assertions, dangling wikilinks, weak MOC coverage). Genuinely ambiguous vision → one AskUserQuestion.
3. **Write the plan** — ordered, every step tagged `[local]`/`[cloud]`/`[human]` (define each venue in one line). Show in chat AND persist to `tasks/improvements/YYYY-MM-DD-<target>.md`.
4. **Approval gate (hard stop)** — stop; run `[local]` only after "go"; file `[cloud]`/`[human]` as checkboxes in `tasks/index.md` per AGENTS.md Action Items; offer `/schedule` for `[cloud]`; never auto-merge.
5. **Execute + report** — local work follows AGENTS.md exactly (enrich-before-create, reciprocal links, update `index.md`, add bucket link, append `log.md`); report what changed + what's left.

- [ ] **Step 5: Write the Guardrails section**

Copy the spec §Guardrails as a short bullet list (AGENTS.md wins / never invent facts / never edit score.py or raw/ / never auto-merge cloud work / plan-first gate is sacred / don't duplicate the ratchet / links>pages).

- [ ] **Step 6: Commit**

```bash
cd "/Users/colekannam/Desktop/Second Brain"
git add .claude/skills/vault-improve/SKILL.md
git commit -m "vault-improve: add skill (thin router, DIAGNOSE→PLAN→gate→EXECUTE)

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 2: Establish the plan-output folder

**Files:**
- Create: `tasks/improvements/.gitkeep`

**Interfaces:**
- Consumes: nothing.
- Produces: the directory `tasks/improvements/` that the skill's procedure step 3 writes dated plan files into.

- [ ] **Step 1: Create the folder with a tracked placeholder**

```bash
cd "/Users/colekannam/Desktop/Second Brain"
mkdir -p tasks/improvements
printf '%s\n' "Dated vault-improve plans land here: YYYY-MM-DD-<target>.md" > tasks/improvements/.gitkeep
```

- [ ] **Step 2: Verify it is tracked**

Run: `git status --porcelain tasks/improvements/`
Expected: shows `?? tasks/improvements/.gitkeep` (untracked, ready to add).

- [ ] **Step 3: Commit**

```bash
git add tasks/improvements/.gitkeep
git commit -m "vault-improve: add tasks/improvements plan-output folder

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 3: Verify the skill registers, triggers, and its procedure runs end-to-end (dry run)

**Files:**
- Verify: `.claude/skills/vault-improve/SKILL.md`
- Exercise (read-only target): an existing skill, e.g. `.claude/skills/wiki-query/SKILL.md`

**Interfaces:**
- Consumes: the `vault-improve` skill from Task 1 and the folder from Task 2.
- Produces: evidence (a written dated plan file with correctly-tagged steps and NO auto-execution) proving the skill behaves per spec.

- [ ] **Step 1: Validate the frontmatter parses**

Run:
```bash
cd "/Users/colekannam/Desktop/Second Brain"
python3 - <<'PY'
import re,sys,pathlib
t=pathlib.Path(".claude/skills/vault-improve/SKILL.md").read_text()
m=re.match(r"^---\n(.*?)\n---\n",t,re.S)
assert m, "no frontmatter block"
fm=m.group(1)
assert re.search(r"^name:\s*vault-improve\s*$",fm,re.M), "name wrong/missing"
assert re.search(r"^description:\s*\S",fm,re.M), "description missing"
print("frontmatter OK")
PY
```
Expected: `frontmatter OK`.

- [ ] **Step 2: Confirm thin-router discipline (does not restate AGENTS.md)**

Run: `grep -c "single source of truth\|AGENTS.md" ".claude/skills/vault-improve/SKILL.md"`
Expected: ≥1 (it *points* to AGENTS.md). Then manually confirm the body does not copy AGENTS.md's Ingest/Query/Lint/CRM rule text — it references them. If it restates rules, trim to a reference and re-commit.

- [ ] **Step 3: Confirm every venue tag and the gate are present**

Run: `grep -o "\[local\]\|\[cloud\]\|\[human\]" ".claude/skills/vault-improve/SKILL.md" | sort -u`
Expected: all three of `[cloud]`, `[human]`, `[local]` appear. Also `grep -i "approval\|stop\|go " ` confirms the hard gate is described.

- [ ] **Step 4: Dry-run the procedure on a real target (the actual behavioral test)**

In a fresh session/subagent, invoke: `improve the wiki-query skill`. Observe that the run:
1. resolves the target as a skill,
2. diagnoses against the four grounding sources,
3. writes a plan to `tasks/improvements/<today>-wiki-query.md` with every step carrying exactly one `[local]`/`[cloud]`/`[human]` tag,
4. **STOPS at the approval gate without editing `wiki-query/SKILL.md`.**

Expected: a plan file exists; no target files were modified; no commit of changes to the target. This is the pass/fail gate for the whole feature.

- [ ] **Step 5: Verify the gate held (no unauthorized writes)**

Run: `git status --porcelain`
Expected: the only new file is under `tasks/improvements/`; `wiki-query/SKILL.md` is unmodified. If the target was edited, the approval gate failed — fix the SKILL.md wording (strengthen "STOP" language) and repeat Step 4.

- [ ] **Step 6: Commit the verification artifact**

```bash
git add tasks/improvements/
git commit -m "vault-improve: verify dry-run produces tagged plan, honors approval gate

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Self-Review

**1. Spec coverage:**
- Purpose / say-improve-get-tagged-plan → Task 1 (procedure) + Task 3 (dry-run proof). ✓
- Framework alignment (links>pages, enrich, never invent) → Global Constraints + Task 1 Steps 3/5. ✓
- Thin-router shape, separate from autoresearch → Task 1 Steps 1/3 + Task 3 Step 2. ✓
- Invocation / triggering (skills + projects primary) → Task 1 Step 2 (description) + Step 4 (target list). ✓
- 5-step procedure (resolve/diagnose/plan/gate/execute) → Task 1 Step 4. ✓
- Venue tags + hard approval gate → Task 1 Steps 4/5 + Task 3 Steps 3/4/5. ✓
- Plan persisted to `tasks/improvements/` → Task 2 + Task 3 Step 4. ✓
- Guardrails (never edit score.py/raw, never auto-merge) → Global Constraints + Task 1 Step 5. ✓
- Out-of-scope: AGENTS.md untouched → File Structure note. ✓

No uncovered spec requirements.

**2. Placeholder scan:** No "TBD"/"handle edge cases"/"similar to Task N" — each step names exact files, commands, and expected output. ✓

**3. Type consistency:** Names are stable across tasks — skill `vault-improve`, folder `tasks/improvements/`, tags `[local]`/`[cloud]`/`[human]`, procedure steps Resolve/Diagnose/Write-plan/Gate/Execute. ✓
