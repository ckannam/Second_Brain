# Claude Code Skills

Reusable capabilities you give [[claude-code]]: a folder with a markdown instruction file (name + description that controls **when it triggers**) plus optional **reference files**. Skills are one instance of Anthropic's portable [[agent-skills]] format — the *same* `SKILL.md` runs on claude.ai and the API too; Claude Code just loads it from the filesystem (`~/.claude/skills/` or `.claude/skills/`).

> **The *craft* of authoring one reliably — description/trigger tuning, progressive
> disclosure, and the eval loop — lives on [[writing-reliable-skills]] (the "skill max" track).**
> This page is the *what*; that page is the *how*.

## Key ideas
- **Anatomy & triggering:** the description is the trigger surface; tune it so the skill fires reliably (Claude tends to *under*-trigger, so lean the description slightly pushy). See [[writing-reliable-skills]]. Src: [[master-claude-code-skills-28min]].
- **Skill Creator + evals:** Anthropic's Skill Creator scaffolds skills; **evals** measure performance; trigger tuning improves reliability — the [[writing-reliable-skills#The eval/iteration loop how skills actually get reliable|eval/iteration loop]]. Src: [[claude-code-skills-update]].
- **Progressive disclosure:** `SKILL.md` under ~500 lines as a table of contents; reference files one level deep, read only when needed (a context-economy move — [[token-context-management]]).
- **When to build one:** the feedback cycle — build a skill when you keep repeating the same instructions.
- **In practice:** content repurposing ([[generate-content-9-socials-blotato]]), [[json-prompting]] images ([[nano-banana-2-antigravity-json-prompting]]), website builds.

Related: [[skills-vs-subagents]], [[claude-code-subagents]], [[ai-second-brain-levels]] (Level 3). Anthropic first-party depth (Code with Claude batch): [[evals-for-taste]] and [[governed-skills-framework]] on evaluating and governing skills at scale.
