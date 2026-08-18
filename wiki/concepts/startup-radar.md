---
type: concept
created: 2026-08-16
---

# Startup Radar

Cole's **weekly startup-discovery engine** — the [[claude-code-skills|skill]] that feeds the
top of the [[outreach-pipeline]]. It sweeps free public surfaces, filters to his two job-search
lanes, dedupes against what he already tracks, and writes new company notes he can act on. The
operational procedure lives in the skill file (`.claude/skills/startup-radar/SKILL.md`); this
page is the *what and why* and how it connects into the [[Job Search]] system.

## What it does (the pipeline)

1. **Sweep** free surfaces only — HN "Who's Hiring," YC Jobs, VC portfolio job boards
   (Sequoia / a16z / Index / Greylock), Harmonic Hot 25, Founders You Should Know,
   `startups.gallery/news`, and a few public Substacks. No paid or authenticated sources.
2. **Lane-filter** to Cole's two target domains, dropping everything else:
   - **health-bio-AI** — biotech, clinical AI, drug discovery, diagnostics, genomics, any
     biology/medicine × AI intersection.
   - **AI-infra** — agents, memory, dev tooling for AI, LLM infra, MLOps, orchestration.
3. **Geo-fit** each candidate (`strong` = NYC/DC/Baltimore metro → `weak` = SF/elsewhere/unknown).
4. **Dedupe** against existing tracker notes, never re-surfacing `parked`/`passed` companies.
5. **Write** a schema-valid company note per survivor + a first-pass outreach contact, then
   report a geo-ranked shortlist.

## Where it sits in the job-search engine

Startup Radar is the **discovery rung** that supplies **Tier 1 (funded targets)** of the
[[outreach-pipeline]] — the weekly funding feed the pipeline's Monday batch enriches and
promotes. The company notes it writes live in the gitignored, **local-only** `startup-tracker/`
folder (never synced), so the discovery output stays private while the pipeline architecture and
this page stay in the wiki. Discovery here → triage → promotion to the outreach board is the
same intake loop the [[Job Search]] bucket describes.

## Design notes

A **low-freedom, consistency-critical** skill (exact source URLs, an exact note schema, a
`validate.py` gate) — the right call for a data-pipeline task per the
[[skill-authoring-playbook]]'s freedom-vs-fragility rule. Its trigger surface was widened on
2026-08-16 (it previously under-fired with only two named triggers); the outstanding
improvement is behavioral evals for the lane-filter and dedup steps (schema validation alone
doesn't test *correctness*). See the worked-example audit on [[skill-authoring-playbook]].

Related: [[outreach-pipeline]] · [[Job Search]] · [[skill-authoring-playbook]] · [[claude-code-skills]].
