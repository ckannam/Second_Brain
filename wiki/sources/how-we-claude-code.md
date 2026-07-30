---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=IlqJqcl8ONE"
event: "Code with Claude"
speaker: "Arno (Applied AI, architect)"
created: 2026-07-24
---

# How we Claude Code

Arno (Applied AI architect) runs a hands-on workshop on how Anthropic engineers actually
configure [[claude-code]] internally — project context, custom commands, hooks, subagents —
built on a talk by **[[tariq]]** (Claude Code team) from SF. Three levels: interview,
HTML specs, verification-native artifacts.

## The framing
Agents get more capable because models do → they run longer on more complex tasks → you
must change your habits. Longer runs burn tokens if the spec is wrong, so **front-load
verification**.

## Level 1 — let Claude interview you
Invokes the [[bitter-lesson]] (Richard Sutton): the more capable the model, the more you
should **resist constraining it**. "Claude is likely better at extracting what you want
than you are at specifying it." Bad prompt: "make it better." Good prompt: give the
*domains* you care about, don't over-specify the outcome, and tell Claude to use the
**AskUserQuestion tool** so it interviews you turn-by-turn into a spec. Uses fast mode, auto
mode (strongly recommended), and the effort parameter (recommendation: "X high").

## Level 2 — [[html-over-markdown-specs|HTML files over markdown]]
"The markdown file is the lingua franca of the AI-native SDLC," but past ~200 lines nobody
reads it. Tariq's blog post **"The Unreasonable Effectiveness of HTML files"**: render the
plan/design as **HTML** — information-dense, ergonomic, screenshottable, feed-back-able (via
Playwright MCP). Demo: had [[opus-4-7]] generate four HTML design directions (brutalist,
Tokyo fintech, …) for a bill-splitting app to react to.

## Level 3 — verification-native artifacts
Make verification part of the artifact so an agent can drive it. React to-do app with
**Storybook fixtures**, data contracts/attributes in the DOM, and **Playwright MCP**;
verification runs three ways — human-readable dashboard, agent-driven (from Claude Code),
and headless (`run verify` in CI). The Claude Code team **records** verification runs and
shares them (e.g. to S3), reducing human touchpoints over time.

Companion internal-practice talk: [[running-ai-native-engineering-org]]. Related:
[[claude-code-hooks]], [[claude-code-subagents]], [[claude-md-router]], [[adversarial-code-review]].

**Raw clip:** [[How we Claude Code]]
