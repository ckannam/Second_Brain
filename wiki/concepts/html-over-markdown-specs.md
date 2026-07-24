# HTML files over markdown specs

From [[tariq]]'s blog post **"The Unreasonable Effectiveness of HTML files"** (via
[[how-we-claude-code]]): the markdown file has been "the lingua franca of the AI-native
SDLC," but past ~200 lines nobody — you or your colleagues — actually reads it. Render the
plan/design/spec as **HTML** instead: it's information-dense, ergonomic, screenshottable,
and interactive, so a human can react to it richly (and feed screenshots back via Playwright
MCP). Example: generate four HTML **design directions** for an app and pick one, rather than
inferring a look from prose.

The deeper move is **verification-native artifacts**: bake verification into the thing
itself (Storybook fixtures, data contracts in the DOM, Playwright MCP) so an agent can drive
it human-readably, agent-first, or headless in CI — and even **record** the runs to share.
This front-loads the human's verification work, which matters more the longer an agent runs
autonomously.

Connects the [[bitter-lesson]] (don't over-constrain) to concrete practice. Related:
[[claude-code-hooks]], [[claude-code]], [[ai-native-engineering-org]].
