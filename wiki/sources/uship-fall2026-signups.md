---
type: source
source: data-export
platform: Wix Forms
title: "UShip — Fall 2026 move-in signups (Wix form export)"
created: 2026-07-29
raw: "raw/private/Forms & Submissions.md (LOCAL-ONLY — customer PII, gitignored)"
privacy: "Underlying export holds ~100 customers' names, emails, phones, home addresses. Raw file is kept local-only and NOT synced. Only the aggregate analytics below live in the (synced) wiki."
---

# Source: UShip Fall 2026 move-in signups (aggregate)

A Wix Forms export of **100 [[uship|UShip]] move-in booking submissions** (Jul 6–28 2026) for the
**Fall 2026** Duke move-in season. Per the vault's standing rule, **customers are not catalogued as
contacts** — the raw PII file lives **local-only** (`raw/private/`, gitignored). Only the aggregates
here are synced. Feeds the [[uship]] "Fall 2026 demand snapshot."

## What the data shows (n = 100 submissions)

**Acquisition channel ("how did you hear about us"):**
- **Email Campaign — 58** (dominant; validates the [[uship#Email marketing — Cole's engine & the scraped-list moat|email-list moat]] Cole built)
- **Customer Referral — 19** · **Previous Customer — 16** → **~35% repeat/referral**, a strong loyalty base
- Co-President of Marketing referrals — 3 (named campus ambassadors) · Google — 2 · Social Media — 1 · Flyers — 1

**Service mix:** Home Pickup (+$100) — **47** · Service Stop — **22** · Out-of-Route ship-in — **20**.
The paid **home-pickup upsell is the most-chosen option** (~half), skewing to NYC-metro families.

**Timing:** **69** target the **Aug 15 first-year move-in**; **17** chose **peak days (+$40 surcharge)**
— the surcharge is successfully shaping demand off the busiest day.

**Geography (Service Stops + home addresses):** heavy **NYC-metro** (Manhattan UES/UWS, Brooklyn) +
**Long Island, Westchester (Scarsdale), CT (Darien/Greenvale), NJ (Short Hills/Tenafly), MA
(Chestnut Hill/Weston), PA (Bala Cynwyd)** — i.e. the **Massachusetts→Durham I-95 corridor**, NYC-centric.

## Takeaways for Cole / UShip
1. **Email is the engine.** 58% of signups came from the email campaigns Cole built — the scraped
   Net-ID list is doing the heavy lifting; keep guarding deliverability.
2. **Loyalty compounds.** ~35% are referrals or returning customers → a referral incentive + the
   ambassador program are worth doubling down on.
3. **Home-pickup upsell is popular** (47/100 paid +$100) → margin-positive; the NYC-metro base will
   pay for convenience. Consider tightening the Service-Stop network around the visible clusters.
4. **Data hygiene:** the export has **duplicate/edited re-submissions** (same customer, changed
   service) and a revised form (old "Deleted" columns) → dedupe before treating 100 as unique
   customers; a few malformed emails would bounce (deliverability risk).

Related: [[uship]] · [[uship-os]] · [[carson-uship-vault-page]] · [[Uship]] (bucket).
