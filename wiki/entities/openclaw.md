---
type: entity
category: tool
---
# OpenClaw (formerly Clawdbot)

An **open-source agent harness** that gives [[claude-code|Claude]] (or other models) persistent
memory, autonomous scheduling, and an "always-on" personal-assistant character — you run it on
your own hardware or a [[vps|VPS]] rather than a hosted service. Created by **Peter Steinberger**.

## Identity & naming (verified 2026-07-28)
- **Clawdbot and OpenClaw are the *same project***, not two competing tools. It launched as
  **Clawdbot** (~**Nov 2025**) and was **renamed OpenClaw** (~**Jan 2026**); some write-ups also
  list the alias **"Moltbot."** The earlier wiki framing that treated them as distinct rival
  products is **superseded** — see [[clawdbot]], now kept only as the former name.
- This reconciles the two source clusters the vault had filed separately: the "Clawdbot vs Claude
  Code" / "Klaus personal assistant" / "Clawdbot on a VPS" videos and the "OpenClaw memory system"
  discussion are all about **one** tool at different points in its life.
- Source: web research 2026-07-28 (community docs + multiple independent write-ups; creator
  attribution matches this page's earlier note of "Peter"). Treat exact dates as approximate —
  corroborated across secondary sources, not an official changelog.

## What sources say
- [[andrej-karpathy]] praised it (with [[sarah-guo]]): "at least five things that are really good
  ideas in here," especially the memory system; he has also called it a "sci-fi takeoff-adjacent"
  demo. Src: [[skill-issue-karpathy-sarah-guo]].
- **Memory** is the headline: plain-text Markdown vault memory (folders, MOCs, wiki-links) plus a
  "dreaming" consolidation pass — the same [[llm-wiki-pattern|LLM-wiki]]-style pattern this vault is built
  on. This is why it's noted for going **beyond default context-compaction**.
- **As a personal assistant:** the presenter built "Klaus," a proactive 24/7 assistant on it (under
  the Clawdbot name). Src: [[i-turned-clawdbot-personal-assistant]].
- **Hosting:** run it 24/7 on a [[vps|VPS]] (Hostinger) instead of a Mac mini. Src:
  [[set-up-clawdbot-vps]], [[hosting-ai-agents]].
- **Positioning:** framed as the thing [[paperclip]] "destroyed" in
  [[claude-code-paperclip-openclaw]] — that's competitive *marketing framing* against a different
  product ([[paperclip]], the AI-agent-*company* tool), not evidence that Clawdbot≠OpenClaw.

Running an autonomous, tool-wielding agent on your own box carries real risk — see
[[agent-security-risks]] (the "100 hours" review flagged this as the main caveat).

Related: [[paperclip]], [[claude-code]], [[ai-executive-assistant]], [[proactive-agents]].
Former name: [[clawdbot]].
