---
type: concept
created: 2026-08-01
---
# Agent Skills (the portable format)

Anthropic's **Agent Skills** are modular, filesystem-based capabilities that turn a
general-purpose model into a specialist — a directory of instructions, metadata, and optional
scripts/resources that Claude loads *automatically* when relevant. This is the **platform
primitive** beneath [[claude-code-skills]]: the same `SKILL.md` format Claude Code uses is the
one that runs on claude.ai and the Claude API. This page owns the *format & architecture*;
[[claude-code-skills]] is the Claude-Code view and [[writing-reliable-skills]] is the authoring
craft. Grounded in Anthropic's official [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Why a skill, not a prompt or a fine-tune

A prompt is a one-off, conversation-level instruction; a fine-tune bakes behavior into weights
at training cost. A **skill sits in between**: created once, versioned, and loaded on demand —
"an onboarding guide you'd write for a new teammate," not a retrain. Three benefits:
**specialize** Claude for a domain, **reduce repetition** (no re-pasting the same guidance),
and **compose** — multiple skills combine within one multi-step task.

## The three-level architecture (progressive disclosure)

The format's whole point is context economy. Content loads in three stages, each with a
different token cost:

| Level | When loaded | Token cost | Content |
|---|---|---|---|
| **1 · Metadata** | always, at startup | **~100 tokens/skill** | `name` + `description` (YAML) — the trigger surface, injected into the system prompt |
| **2 · Instructions** | when the skill triggers | **< ~5k tokens** | the `SKILL.md` body (workflows, guidance) |
| **3 · Resources & code** | as needed | **0 until accessed** | bundled reference files (load when read) + scripts (run via bash — *only their output* costs tokens) |

So you can install *many* skills for ~100 tokens each; you pay for a skill's body only when it
fires, and never for un-touched bundled files. This is the same context-economy lever covered
in [[token-context-management]], and the authoring technique that exploits it is on
[[writing-reliable-skills]].

## Cross-surface — one format, but NOT one copy

The format is portable across every Claude agent product, yet **custom skills do not sync
between surfaces** — a real gotcha:

- **Claude Code** — filesystem-based, no upload: drop a directory in `~/.claude/skills/`
  (personal) or `.claude/skills/` (project); shareable via [[claude-code|Claude Code]] plugins.
  *(This vault's own skills live here.)*
- **claude.ai** — upload a skill as a **`.zip`** in Settings → Features; **individual to each
  user** (no org-wide admin management).
- **Claude API** — upload via the `/v1/skills` endpoints; reference a `skill_id` in the
  `container` param with the code-execution tool; **workspace-wide** sharing. Runs sandboxed:
  **no network, no runtime package installs**.

A skill uploaded to one surface must be uploaded separately to the others. Sharing scope and
runtime (network access, package installs) differ per surface — plan the skill for where it runs.

## Pre-built vs custom

Anthropic ships **pre-built** skills for document work — **`pptx` · `xlsx` · `docx` · `pdf`**
(available on claude.ai + the API; *not* in Claude Code) — plus open-source skills in the
[skills repo](https://github.com/anthropics/skills) (e.g. the bundled **Claude API skill** with
up-to-date SDK docs). **Custom** skills package *your* domain/organizational knowledge.
*(Cole's environment surfaces exactly these pre-built document skills — `pptx`, `xlsx`, `docx`,
`pdf` — alongside his custom vault skills.)*

## Security — a skill is executable code

A skill grants Claude new capabilities through **instructions and code**, so a malicious skill
can direct Claude to invoke tools or run code outside its stated purpose → data exfiltration or
unauthorized access. **Use skills only from trusted sources** (self-authored or Anthropic); audit
every bundled file (scripts, images, resources) before use; skills that **fetch external URLs**
are especially risky (fetched content can carry injected instructions). This is the skill-shaped
instance of the threat model on [[agent-security-risks]] — treat installing a skill like
installing software. Org-scale vetting/governance is the [[governed-skills-framework]].

## Why it matters here

This vault runs *on* the format: `.claude/skills/` holds `vault-autoresearch`, `wiki-query`, and
the prompt-architect skills — the same primitive documented here. Understanding the format (token
budget, cross-surface limits, security posture) is what lets the "[[writing-reliable-skills|skill
max]]" track author skills that are portable and safe, not just locally handy.

Related: [[claude-code-skills]] · [[writing-reliable-skills]] · [[skills-vs-subagents]] ·
[[claude-code-subagents]] · [[token-context-management]] · [[agent-security-risks]] ·
[[governed-skills-framework]] · [[ai-second-brain-levels]] (Level 3 = skills) · [[claude-code]].
