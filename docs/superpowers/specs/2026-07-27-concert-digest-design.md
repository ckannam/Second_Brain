# Concert Digest — weekly iMessage module

**Date:** 2026-07-27
**Owner:** Cole
**Status:** design approved (pending spec review)

## Purpose

Cole's two favorite hobbies are travel and live music, and he wants to devote more
deliberate time to hobbies. He wants a **weekly iMessage update** of concerts near him —
artists he loves plus taste-matched discovery — delivered to his iMessage self-chat, the
same channel as his networking brief. He is in **Baltimore** now and **moves to Durham
(Triangle: Durham/Raleigh)** on ~**2026-08-17**, so the digest must follow him.

This is built as a **module of a future combined weekly update**, but ships **standalone
now** so it delivers value immediately. Same code path exposes both modes.

## Decisions (locked with Cole)

| Decision | Choice |
|---|---|
| Data source | **Agentic weekly run** — a scheduled Claude session web-searches artists + local venue calendars each week. No API keys; understands taste fuzzily. |
| Discovery | **Yes** — surface taste-matched artists he hasn't named, tagged as discovery (🔎). |
| Delivery shape | **Module of one weekly update.** Ships standalone now; exposes a "section" mode for the future orchestrator. |
| Location | **Auto-flip on set date.** Baltimore until 2026-08-17, then Triangle. |
| Schedule | **Monday ~8am**, matching the networking-brief rhythm. |
| Artist seed | Cole pastes his full concert history into `concert-taste.md`; seeded with named artists until then. |

## Architecture

Three parts, mirroring the proven networking-brief pattern
(`~/.claude/networking/`: composer → AppleScript send → launchd):

```
profile/concert-taste.md   (source of truth, Cole-editable)
        │
        ▼
concert-digest skill  ── agentic weekly run ──▶ iMessage self-chat (+14436822254)
  (read profile → pick metro by date → web-search → rank → compose → send)
        │
        └── section mode ──▶ returns just the "🎵 Concerts near you" text block
                             (for the future weekly-update orchestrator)
```

Because the run needs **live web search**, it is agentic (a Claude session), not a
deterministic Python composer like `brief.py`. Delivery reuses the **AppleScript iMessage
send** pattern for reliability in a headless/scheduled context.

## Component 1 — `profile/concert-taste.md` (source of truth)

Plain markdown so Cole edits it anytime; the next run picks up changes. Schema:

- **Love / seen** (full pasted history, normalized — **Cole to confirm the guesses**):
  Tyler Childers, Zach Bryan, Billy Strings (×2), Phish (×3), Trampled by Turtles (×2),
  Joe Russo's Almost Dead / "Joey Russo" (×2), Greensky Bluegrass, Caamp, Turnpike
  Troubadours ("Turnpikes"), Nathaniel Rateliff (?"Nate Radcliffe"), Mt. Joy (?"My Joy"),
  Twiddle, Deer Tick, Joey Bada$$, Baby Keem, Lil Yachty, Redveil (?"Redvail"), Jack
  Johnson, Paul Simon, Bruno Mars, Maroon 5, Damian Marley.
  Also named recently: Goose, Sturgill Simpson.
  *(Guesses to confirm: Joe Russo's Almost Dead, Turnpike Troubadours, Nathaniel Rateliff,
  Mt. Joy, Redveil.)*
- **Want to see** — Stews, Harvey Street, Geese, Sturgill Simpson.
- **Discovery seeds** — genre anchors, weighted toward the core lane:
  **jam / newgrass** (Phish, Billy Strings, Goose, JRAD, Greensky, Twiddle, Trampled) and
  **Americana / country** (Tyler Childers, Zach Bryan, Turnpike, Sturgill, Nathaniel
  Rateliff); secondary lanes **indie folk-rock** (Caamp, Mt. Joy, Deer Tick, Jack Johnson)
  and, lower weight, **hip-hop** (Joey Bada$$, Baby Keem, Lil Yachty, Redveil). Discovery
  favors the jam/Americana core; other lanes surface only for standout shows.
- **Venues by metro:**
  - *Baltimore/DC:* Merriweather Post Pavilion, Rams Head Live, Ram's Head On Stage
    (Annapolis), The Ottobar, Baltimore Soundstage, Pier Six Pavilion, CFG Bank Arena,
    The 8x10, The Anthem (DC), 9:30 Club (DC).
  - *Triangle:* Cat's Cradle (Carrboro), DPAC, Motorco (Durham), The Pinhook (Durham),
    Haw River Ballroom (Saxapahaw), The Ritz (Raleigh), Red Hat Amphitheater (Raleigh),
    Coastal Credit Union Music Park / Walnut Creek (Raleigh), Lincoln Theatre (Raleigh),
    Kings (Raleigh).
- **Location cutover** — `baltimore until 2026-08-17, then triangle`.
- **Search window** — next ~6–8 weeks.

## Component 2 — `concert-digest` skill (the weekly agent's job)

Steps the scheduled run follows:

1. **Read** `profile/concert-taste.md`.
2. **Pick active metro** by comparing today's date to the cutover date.
3. **Search:** for each named artist, find upcoming tour dates in/near the active metro;
   scan each metro venue's calendar for the search window.
4. **Rank:** taste match (love > want-to-see > discovery) → then soonest date / proximity.
   Cap the list (~8–12 shows) so the text stays scannable. Tag discovery picks 🔎.
5. **Compose** the "🎵 Concerts near you" block: one line per show —
   `Artist — Venue, City — Date — [tickets]`, grouped soonest-first, discovery at the end.
6. **Deliver:**
   - *standalone mode:* send the block (with a one-line header) to the iMessage self-chat.
   - *section mode:* return the block as text for the weekly-update orchestrator.

### Output format (example)

```
🎵 Concerts near you — Triangle, week of Aug 17

Billy Strings — Red Hat Amphitheater, Raleigh — Fri Aug 21 — [tix]
Goose — Cat's Cradle, Carrboro — Sat Aug 22 — [tix]
Caamp — DPAC, Durham — Thu Sep 4 — [tix]

🔎 Discovery (your jam/Americana lane)
Trampled by Turtles — Haw River Ballroom — Sep 12 — [tix]
```

## Component 3 — Delivery + schedule

- **iMessage:** AppleScript send to `+14436822254`, reusing the networking-brief send
  approach (no interactive session required).
- **Schedule:** weekly, **Monday ~8am**, via a scheduled Claude run (agentic). Chosen over
  a launchd-only Python job because live web search requires an LLM session. Mechanism
  (cloud routine vs. launchd invoking headless `claude`) is an implementation-plan detail.

## Location logic

`active_metro = "baltimore" if today < 2026-08-17 else "triangle"`. During implementation,
the cutover date is a single constant in `concert-taste.md` so Cole can shift it if the
move slips.

## Error handling

- If a search yields nothing for the window, send a short honest note ("Quiet week — no
  strong matches near you; here are 2 worth a drive") rather than a fake or empty list.
- If iMessage send fails, log to a run log (like `brief.log`) and no-op; next week retries.
- Never invent shows or ticket links; only report what search surfaces.

## Testing

- **Dry run:** invoke the skill in section mode, inspect the composed block for a known
  metro/date without sending.
- **Location flip:** run with a simulated date before and after 2026-08-17, confirm the
  metro and venue set switch.
- **Delivery:** one manual standalone send to the self-chat, confirm receipt (as the
  networking brief was verified).

## Open items

- **Cole to confirm** the 5 name-normalization guesses above (JRAD, Turnpike
  Troubadours, Nathaniel Rateliff, Mt. Joy, Redveil) before the profile is finalized.
- Combined weekly-update orchestrator is out of scope here; this module only exposes the
  section-mode interface it will call.

## Non-goals (YAGNI)

- No concert API / ticketing integration, no calendar auto-add, no RSVP tracking.
- No building the full weekly-update shell — only the concert module + its integration
  point.
