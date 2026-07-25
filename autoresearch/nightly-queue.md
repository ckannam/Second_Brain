# Nightly Queue — vetted `@cloud` tasks

The overnight routine works this queue **after** the AutoResearch loop (MODE C). Only tasks
that are **cloud-safe** live here: they touch the *synced* vault + web/connectors, need **no
local data** (`crm/`, `profile/`, `finance/`, iMessage, Contacts — invisible to the cloud), and
take **no outward/irreversible actions**.

## Rules for the routine
- Work the **top 1–2 unchecked items** per night, top-down. Don't do more.
- These are **research → wiki** tasks: use **WebSearch/WebFetch** to verify, then update the
  relevant page per `AGENTS.md` — **cite sources, mark uncertainty, honor freshness** (sources are
  point-in-time; don't overwrite, flag/supersede).
- **Check off** what you finish. If an item **isn't doable** (needs local data, source not found,
  or needs a human decision), **leave it unchecked and note *why* in the PR body** — never guess or
  fabricate. That "why" is how the queue gets smarter.
- **SAFETY:** research/draft/organize only. **Never** send email/messages, spend money, or take
  outward/irreversible actions. Everything stays on the night branch for morning review.

## Queue (@cloud)
- [ ] Ground a single-source feature claim: pick one `claude-code-*` concept page that cites only
      [[nate-herk]], verify it against **official Anthropic docs**, add the official citation, and
      correct/flag any discrepancy. (One page per night.)
- [ ] Verify the **Auto Dream** trigger cadence (currently community-inferred) → update
      [[claude-code-memory]] with a sourced answer, or explicitly mark it unverified + what you checked.
- [ ] Confirm the **Clawdbot** / **OpenClaw** identities & spellings → update [[clawdbot]] / [[openclaw]].
- [ ] Capture the **Opus 4.6 vs GPT 5.4** benchmark numbers from a primary source → add to the
      relevant page with citation (or mark not-found).

## Not eligible here (for reference — these are @local or @human)
- CRM enrichment from message content, ingesting IG/YouTube exports → **@local** (needs your Mac).
- Password-holder design, Journal-pillar decision, Stewart prep, IG/Spotify exports → **@human**.
