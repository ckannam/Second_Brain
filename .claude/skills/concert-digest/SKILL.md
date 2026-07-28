---
name: concert-digest
description: Use to compose (and, in standalone mode, send) Cole's weekly "Concerts near you" iMessage digest. Reads profile/concert-taste.md, uses the active metro + today's date passed in the prompt, web-searches his artists and local venue calendars, ranks by taste and proximity with taste-matched discovery, and delivers a short text-native block to his iMessage self-chat. Triggered by the Monday launchd run or when Cole says "run the concert digest".
---

# Concert Digest

You compose Cole's weekly concert digest. Two hobbies he is investing in: travel + live music.

## Inputs (from the launch prompt)
- `ACTIVE_METRO`: `baltimore` or `triangle` — already decided for you; do NOT recompute.
- `TODAY`: ISO date to treat as "now".
- `MODE`: `standalone` (compose AND send) or `section` (compose and return the block only, no send).

## Steps
1. Read `profile/concert-taste.md`. Note `## Love / seen`, `## Want to see`,
   `## Discovery seeds`, the `## Venues` list for `ACTIVE_METRO`, and `## Settings` `window_weeks`.
2. Define the window: `TODAY` .. `TODAY + window_weeks`.
3. Search (use web search):
   - For each **Love / seen** and **Want to see** artist, find tour dates in/near the active
     metro within the window.
   - Scan the active metro's listed venue calendars for shows in the window.
   - Find a few **discovery** shows: artists NOT on his lists but matching the Discovery-seed
     lanes (favor the high-weight jam/Americana lanes) playing the active metro in the window.
4. Rank: taste tier (love > want-to-see > discovery) → then soonest date. Cap at ~8–12 shows so
   the text stays scannable. Deduplicate.
5. Compose the block, plain text, no markdown bold, emoji ok:
   ```
   🎵 Concerts near you — {Metro}, week of {Mon DD}

   {Artist} — {Venue}, {City} — {Day Mon DD} — {ticket link or "tix: search"}
   ... (soonest first)

   🔎 Discovery ({one-phrase lane})
   {Artist} — {Venue} — {Day Mon DD} — {link}
   ```
   Keep it tight and text-native (this is an iMessage). If NOTHING credible is found, send an
   honest short note instead, e.g. "🎵 Quiet week near you — nothing strong in {metro}. Worth a
   drive: {1–2 nearby options or 'none this week'}."
6. Deliver:
   - `MODE=standalone`: send the block with
     `osascript /Users/colekannam/.claude/concerts/send.scpt "<block>"`.
     Then stop. Do not also print a duplicate.
   - `MODE=section`: output ONLY the block as your final message; do NOT send.

## Rules
- Never invent shows, dates, venues, or ticket links. Only report what search actually returns.
  If unsure of a link, write `tix: search "{artist} {venue}"` instead of a fabricated URL.
- Do not recompute the metro or override the cutover; trust `ACTIVE_METRO`.
- Keep the whole message comfortably readable on a phone.
