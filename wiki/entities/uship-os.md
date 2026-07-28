---
type: entity
category: software
created: 2026-07-27
---

# uship-os

The internal **multi-tenant operating system** for [[uship|University Shipping]], **built by
[[Carson Eisner]]** (in Claude Code) from his data/analytics + finance seat. It is the
**linchpin of the 2027 multi-campus expansion** — the thing meant to absorb the manual labor
that made the Columbia launch a 50/50 instead of an 80/20 deal. [[carson-uship-vault-page]]

## What it does (v2.0.0)
- **Public booking funnel** → signup/confirmation tracking with an auto-"bump."
- **HQ admin console** + **per-campus co-owner workspaces** + a **mover day-of view**, all under
  role-based access (`campus_scope`).
- **Read-only Square + QuickBooks sync**, provenance-aware finance, and the **80/20
  profit-waterfall payout engine**.
- **QR inventory**, a **New Campus Wizard**, and a comms-timeline engine behind a co-owner
  **batch approval gate**.

## Stack & hosting
Next.js 14 · Prisma · **Postgres/Supabase** · NextAuth · Tailwind. Hosted on **Render**
(~$32/mo). Repo: **`DudeslyGames/uship-os`**. Carson also built the separate student-ID
**web-scraper** behind the ~16k Net-ID marketing list.

## Why it matters to the plan
The 2027 wave (4–5 campuses, no fallback season) is **Option A with the OS as Priority #1**:
it must be **production-ready ~Feb 2027**, built *before* the target schools are even picked and
parameterized per campus's move-out day. The flip side: because there's no fallback season, an
**OS slip risks all 6–7 campuses at once.** [[carson-uship-vault-page]]

Related: [[uship]] · [[Carson Eisner]] · [[carson-uship-vault-page]] · [[Uship]] (bucket).
