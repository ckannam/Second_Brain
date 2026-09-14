---
type: entity
created: 2026-09-12
---
# ECC (affaan-m/ECC)

A large, third-party **"agent harness operating system"** for [[claude-code]] (and ~12 other
harnesses — [[codex]], Cursor, OpenCode, Gemini, Zed, Antigravity, Qwen, Copilot, Kimi). MIT
open source by a solo maintainer (affaan-m); trending GitHub repo, ~40k stars. Ships **68 agents,
291 skills, 94 command shims, hooks, rules, a memory vault, and a security scanner** as an
installable `ecc@ecc` plugin. Source: [[affaan-ecc-agent-harness-os]] (README snapshot 2026-09-11).

Its one-line thesis is worth stealing even if the package isn't:

> plan → test → implement → review → verify → remember → improve.
> **Optimize the context window; persist everything else.**

That is the same philosophy this vault already runs on — ECC's value is as a **menu of concrete
patterns**, not as software to install.

## Why I am NOT installing it (the real lesson first)
- **~70% overlaps the `superpowers` plugin Cole already runs.** Plan-before-build, TDD, fresh-context
  review, verification loops, [[claude-code-worktrees|worktrees]], [[parallel-agents]], memory, and
  security review are all already covered. ECC teaches nothing new on the core spine.
- **It advertises its whole catalog into context.** The README itself admits the plugin "advertises
  the installed catalog to the model" — 291 skills' metadata is a context tax that fights the very
  [[token-context-management|context economy]] it preaches. Directly contradicts this vault's
  dense-context discipline.
- **Large third-party attack surface.** Hooks run shell, the bundled MCPs hold credentials, and the
  README is ringed with "install only from official sources — mirrors may contain malware" warnings
  and sponsor/affiliate links. By its own [[agent-security-risks]] logic, installing it is adding a
  big trusted-code surface. **Steal the ideas, not the install.**

## The genuinely net-new lessons (what the vault didn't already have)
1. **Instincts / continuous-learning-v2** — the biggest gap. ECC auto-extracts patterns from finished
   sessions into **confidence-scored "instincts,"** then injects the top-N relevant ones at
   `SessionStart` (ranked by confidence + stack relevance; tunable via `ECC_MAX_INJECTED_INSTINCTS`,
   `ECC_INSTINCT_CONFIDENCE_THRESHOLD`). Lifecycle: `/learn` → `/evolve` (cluster instincts into
   skills) → `/prune`. This is the OSS/consumer analog of [[agent-dreaming]] and a structured layer
   *on top of* [[claude-code-memory|plain memory]] — and Cole currently runs **no instinct store at
   all** (verified: empty). See [[agent-dreaming]].
2. **Hooks as enforcement, with starter recipes.** Reframes "please use TDD" (an instruction the model
   forgets) as a deterministic [[claude-code-hooks|hook]] outside the prompt. Liftable recipes:
   secret-scan on prompt submit (`sk-`/`ghp_`/`AKIA`), auto-format + typecheck on `Edit|Write`,
   dev-server-outside-tmux guard, git-push review gate. Plus a concrete gotcha → see [[claude-code-hooks]].
3. **Rules as a third layer.** ECC separates **rules** (always-loaded, selectively-installed language/
   project standards) from **skills** (loaded on demand) from **hooks** (run outside the model). Cole
   collapses all of this into `CLAUDE.md`; the "install one language pack of always-on standards"
   model is cleaner. See [[token-context-management]], [[instructions-as-code]].
4. **Concrete context-economy knobs.** `CLAUDE_CODE_SUBAGENT_MODEL=haiku` (cheap sub-agents),
   `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50` (compact earlier), `MAX_THINKING_TOKENS`, and the **MCP budget
   rule: keep <10 MCPs / <80 tools active or a 200k window effectively shrinks to ~70k.** Directly
   relevant — Cole runs many MCP servers. See [[token-context-management]].
5. **Scan your own harness as an attack surface (AgentShield).** A scanner that audits `CLAUDE.md`,
   `settings.json`, MCP configs, hooks, and skills for injection/secret/permission risk — a red-team /
   blue-team / auditor agent pipeline. The *posture* (not the binary) belongs in [[agent-security-risks]].

## Ecosystem placement
A harness-framework **rival/complement** in the same band as [[openclaw]] and [[paperclip]] (always-on
/ multi-agent harnesses), but ECC is a **workflow-discipline layer** rather than a runtime — closest in
spirit to Anthropic's own `superpowers` plugin and to this vault's home-grown skills
([[vault-autoresearch]], the prompt architects). Ships adapters so the same skills/rules run across
[[codex]] and others via a root `AGENTS.md` + DRY hook-adapter pattern.

**Snapshot caveat:** README examples cite Opus 4.6 (AgentShield) / Sonnet defaults; reconcile against
the current [[opus-4-8]] flagship. Release 2.2.1 (2026-08-31).

Related: [[claude-code]] · [[agent-dreaming]] · [[agent-memory]] · [[token-context-management]] ·
[[claude-code-hooks]] · [[agent-security-risks]] · [[test-driven-development]] ·
[[adversarial-code-review]] · [[governed-skills-framework]] · [[openclaw]] · [[paperclip]].
