# Flight Buy-Timing Companion — travel module for the weekly iMessage update

**Date:** 2026-07-27
**Owner:** Cole
**Status:** design approved (pending spec review)

## Purpose

Cole's two favorite hobbies are travel + live music; he's investing more in both. He is **bad at
being proactive about buying flights** and wants a companion that tells him **the sweet spot for
when to buy** — a real BUY / WAIT verdict per trip, delivered to his iMessage self-chat (same
channel as his networking brief and [[cole-concert-digest]]). Sibling to the concert digest; reuses
its proven pattern (Cole-editable profile → agentic run → AppleScript iMessage send, with a
date-based Baltimore→Triangle airport flip).

Immediate real need: **Vegas for fall break** (RDU→LAS, out flexible Thu Oct 8–Sat Oct 10, back
Tue Oct 13 with no late red-eye, cash/cheapest). Plus idea-generation for spring break
(Mar 13–21, 2027), winter break (Dec 18, 2026 → mid-Jan), and a post-grad East Asia trip
(after graduation May 9, 2027).

## Decisions (locked with Cole)

| Decision | Choice |
|---|---|
| Fare data source | **Travelpayouts / Aviasales Data API** (free, no credit card) for tracked-trip fares + price-history/cheapest-date endpoints, with an **agentic Google Flights cross-check** to confirm the live bookable fare when a BUY signal fires. |
| Airports | **RDU primary + smart alternates** (CLT/GSO) after the 2026-08-17 move; BWI + DCA/IAD before. Same auto-flip as concerts. |
| Idea trips | **Yes** — surface destination ideas + rough fares for undecided trips (spring/winter/post-grad). Once Cole picks one, it becomes a tracked trip. |
| Cadence | **Twice weekly** (Mon + Thu). Monday = full digest always. Thursday = silent price-log update, sends only if a BUY signal or backstop nudge fires. |
| Urgency | Weekly digest **+ same-day BUY-NOW ping** when a tracked fare enters its buy zone (after live cross-check). |
| Vegas backstop | **Yes** — escalating "just book it" nudge if no BUY has fired by ~3 weeks out (~Sep 22), since waiting past the domestic window usually costs more. |
| Payment | Cash / cheapest fare, any airline (no miles). |
| Delivery | iMessage self-chat via the proven AppleScript path; built standalone with a `section` mode for the future combined weekly update. |
| Setup on Cole | Register a **free Travelpayouts account** for an API token (~5 min, no card). |

## Architecture

Mirrors the concert digest, with a flight-specific deterministic core:

```
profile/travel-watchlist.md   (source of truth, Cole-editable, gitignored/local-only)
        │
        ▼
~/.claude/travel/fares.py  ── deterministic, twice weekly (Mon+Thu) ──▶ appends
        │                                                        pricelog.csv (history)
        │                                                                │
        │  evaluates buy/wait signal (pure, unit-tested) ◀───────────────┘
        ▼
 (Monday) OR (BUY signal) OR (Vegas backstop)  ──▶ travel-digest skill (agentic)
        │   live Google Flights cross-check on BUY; destination ideas for idea-trips
        ▼
   iMessage self-chat (+14436822254)      [section mode: return the block only]
```

The **deterministic Python core** (`fares.py`) does the cheap, reliable work every run: pull
current fares, append to the price log, compute the signal. An **agentic Claude session** fires
only when there's something to say — a Monday digest, a BUY-NOW ping, or a backstop nudge — so
most Thursday runs are silent, LLM-free, and free.

## Component 1 — `profile/travel-watchlist.md` (source of truth)

Cole-editable markdown, gitignored/local-only (same policy as the taste profile and `finance/` —
never committed). Schema:

- **Home airports** — `primary: RDU`, `alternates: CLT, GSO`; `before_cutover: BWI (+ DCA, IAD)`;
  `cutover: 2026-08-17`. Alternates are only suggested when savings beat the drive
  (`alternate_min_savings: 60` USD).
- **Tracked trips** — one block each with: `id`, `origin`, `dest`, `depart` (date or flexible
  range), `return` (date or range + constraints, e.g. `no_redeye_return: true`), `budget` (optional
  target USD), `buy_by` (optional hard date), `purchased: false`.
  - Seed: **vegas** — `origin: RDU (+CLT,GSO)`, `dest: LAS`, `depart: 2026-10-08..2026-10-10`,
    `return: 2026-10-13 (no late arrival, no red-eye)`, `budget: (Cole to set or leave blank)`,
    `hard_nudge_days: 21`, `purchased: false`.
- **Idea trips** — `id`, `window` (date range), `vibe/budget hint`, optional destination shortlist.
  - Seed: **spring-break** (`2027-03-13..2027-03-21`, ideas), **winter-break**
    (`2026-12-18..2027-01-11`, ideas), **postgrad-asia** (`after 2027-05-09`, East Asia:
    Thailand, Hong Kong, …; long-lead, ideas).
- **Settings** — booking-window + signal thresholds (see Component 2), all editable.

## Component 2 — the sweet-spot engine

### `~/.claude/travel/fares.py` (deterministic, outside the repo)
For each tracked trip: query the Travelpayouts Data API for the cheapest fare across the
route + date flexibility + active-metro airports, and **append one row** to
`~/.claude/travel/pricelog.csv`:
`checked_on, trip_id, origin, dest, depart, return, cheapest_usd, source`.
That growing log is Cole's personal price history (Travelpayouts' own cache is only ~7 days, so
our log is what enables long-run trend detection). The plan pins the exact Travelpayouts endpoints
(cheapest-fares-for-route/dates, price calendar, and cheapest-destinations-from-origin) against the
live API docs; auth via the free token in `~/.claude/travel/.token` (gitignored).

### Buy/wait signal (pure function, unit-tested)
`buy_signal(current, history, days_to_departure, trip_type, budget, hard_nudge_days, purchased)`
→ one of `BUY_NOW | BUY_SOON | WAIT | BACKSTOP_NUDGE`. Defaults (tunable in watchlist Settings):

- **Booking windows:** domestic optimal `21–56` days out; international `60–150` days out.
- **BUY_NOW** if `current ≤ min(history) * 1.03` **and** `days_to_departure ≤ window_high`
  **and** (`budget` unset or `current ≤ budget`); **or** `current` is ≥ **8%** below the trailing
  14-day median while inside the window.
- **BACKSTOP_NUDGE** if `not purchased` and `days_to_departure ≤ hard_nudge_days` (Vegas: 21) —
  escalates regardless of deal quality, message intensity rising as the date nears.
- **BUY_SOON** if inside the window and trending down but not yet at a low.
- **WAIT** otherwise (too early, or fare high with no drop).

Only `BUY_NOW` and `BACKSTOP_NUDGE` trigger an out-of-band (non-Monday) message. The Monday digest
always reports every trip's current fare, trend arrow, and verdict.

## Component 3 — `travel-digest` skill (agentic, fires only when needed)
Inputs from the launcher: `MODE` (`digest` | `alert` | `section`), `ACTIVE_METRO`, `TODAY`, and the
list of triggered trips (for `alert`).
1. Read `travel-watchlist.md` + `pricelog.csv` (+ the signals `fares.py` computed).
2. **`digest` (Monday):** compose the full block — each tracked trip: cheapest fare, trend vs.
   history, days-to-departure, and BUY/WAIT verdict; plus 2–3 **destination ideas** per idea-trip
   (Travelpayouts cheapest-from-RDU within the window + agentic enrichment), with ballpark fares.
3. **`alert` (any day a BUY/backstop fired):** agentic **Google Flights cross-check** to confirm the
   real bookable fare/flights for the triggered trip, then a short "✈️ BUY NOW" (or escalating
   backstop) message with the confirmed fare + a booking link.
4. **`section`:** return the digest block only; no send.
5. Compose text-native; **never fabricate fares, flights, or links** — report only what the API /
   cross-check returns; if a link is uncertain, write `book: search "<route> <dates>"`.

## Component 4 — delivery + schedule
- **iMessage:** AppleScript send to `+14436822254` (reuse the concert/networking pattern).
- **Schedule:** launchd **twice weekly, Mon + Thu ~8am** → `run_travel.sh`:
  1. Compute active metro (reuse the concert digest's date→metro logic / cutover).
  2. Run `fares.py` → update `pricelog.csv`, emit per-trip signals.
  3. If **Monday** → invoke the skill in `digest` mode (compose + send full digest).
  4. Else if any **BUY_NOW/BACKSTOP_NUDGE** → invoke the skill in `alert` mode (cross-check + ping).
  5. Else → exit silently (log only). Most Thursdays cost nothing.

## Error handling
- API/token failure → log, keep last known fares, skip this run's signal (no false BUY); the Monday
  digest notes "fare check unavailable" rather than guessing.
- BUY-NOW ping only sends **after** the live cross-check confirms a real bookable fare.
- Empty idea results → honest short note, no padding.
- Never invent fares, flights, dates, or booking links.

## Testing
- **Unit:** `buy_signal` across a matrix — too-early WAIT, in-window low BUY_NOW, 8%-drop BUY_NOW,
  backstop nudge inside `hard_nudge_days`, budget cap respected, purchased→silent. Pure function,
  TDD.
- **fares.py dry run:** one real Travelpayouts call for RDU→LAS, confirm a row appends to the log
  (no message sent).
- **Skill dry run:** `section` mode for a seeded log, inspect the composed digest.
- **Live bundle (supervised):** one real Monday-mode send + one simulated BUY alert (cross-check +
  ping), verified received; then load the twice-weekly launchd agent.

## Open items
- **Cole:** register a free Travelpayouts account and paste the API token (I'll give exact steps);
  optionally set a Vegas budget target.
- Exact Travelpayouts endpoint paths pinned during implementation against the live docs.

## Non-goals (YAGNI)
- No auto-booking, no seat/price-freeze, no miles/award optimization (cash only), no hotel/lodging.
- No building the combined weekly-update shell — only the travel module + its `section` interface
  (shared with the concert module).
- No live-to-the-second fare feed; cache lag is covered by the buy-time cross-check.
