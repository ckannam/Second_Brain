---
source: shared-vault-page
author: Carson Eisner
shared_by: Cole (Carson is a co-owner; page is Carson's, not Cole's)
shared_date: 2026-07-27
note: >
  Carson's own Second-Brain "UShip" topic page, shared by Cole as a source to fill gaps in
  his vault. Written from Carson's POV (Carson as protagonist, expansion as headline) and
  well-sourced from primary data Carson holds (QuickBooks, iMessage/Gmail archives, the
  uship-os codebase, LinkedIn). Treat as a rich SECONDARY compilation, not primary data —
  and cross-check against what Cole already knows (e.g. early alumni Ray/Nick, Cole's own
  broader ops role) rather than deferring to it wholesale.
---

# UShip (University Shipping & Storage) — Carson's page

type: topic
aliases: [UShip, University Shipping, Uship, University Shipping & Storage, shipping-storage-company]
tags: [topic, venture, work, entrepreneurship, company]
created: 2026-06-18
updated: 2026-07-01
sources: 14
confidence: high

**University Shipping & Storage** ("UShip"; legacy legal entity **"University Shipping & Storage 6 LLC"**, North Carolina) is a **multi-campus student storage business** that Carson **co-owns** — one of **6 current owners** — and is helping expand to new campuses.

> The "6" is legacy naming, not a count of owners. Carson clarified (2026-06-22) that the **"6" in "UShip 6 LLC" is a relic** — the team used to incorporate a new LLC every year and stopped at the sixth; the name is not derived from having six owners (it's coincidental that there are currently six). The **legacy LLC cap table is a class-year ladder** that forfeits on graduation: Gorman 35% · Cole 35% (seniors, graduating ~2027) · Danny 10% · Matty 10% (juniors) · Carson 5% · Luca 5% (sophomores) — so the two seniors hold **70%**. **No operating agreement exists** for the legacy LLC.

> Carson joined an established business. UShip is **not Carson's founding** — Duke storage history runs back to **Fall 2018** (16 seasons of Square data). Carson became a **co-owner in February 2026**, joining a running operation; graduated seniors (Mehbod, Marshall Seligson) are now alumni.

## What it is
- A **summer move-out storage** service for college students: store boxes/furniture/appliances between terms, with local truck rentals supporting move-out. Whale mascot; customer-facing site **universityshipping.com**.
- **Business model = franchise:** one software platform serves many campuses; each campus is run near-solo by a local **co-owner** who keeps a profit share while **HQ provides the platform and keeps the rest**. Profit split by campus: **Duke = HQ 0%** (founding team keeps 100%), **Columbia = 50/50**, **all new schools = 80/20** (HQ 80 / co-owner 20).

> Storage-first vs. the shipping pitch. Customer-facing marketing headlines year-round storage **plus shipping to/from home** ("cheapest of any competitor"). The internal OS treats UShip as **storage-only with a small shipping add-on** (~20% Square service charge on shipping items). Likely the home-shipping option is a smaller East-Coast offering, not the core. (inferred)

## Finances — verified
- **2026 YTD (QuickBooks, Jan 1–May 29):** income **$83,685**, expenses **$3,612**, **net income $80,055**; balance sheet **$80.5K cash, $100 liabilities, zero debt**. Sharp **May move-out spike** ($63.4K of it in May).
- **2025 (internal records):** ~**$135.8K revenue / ~$101.7K net**.
- **Duke history (8 seasons, Fall '22–Spring '26):** real margins **54–79%**; e.g. Spring 2026 $84.4K rev / $66.6K net.
- Carson's latest resume states **"$150k+ annual revenue"** and frames the Columbia launch as **$10K+ revenue** while leading expansion to **5+ universities**. That's rounder/higher than the internal figures; audited net is ~$80–100K and Columbia's internal figure is $9,972.55 revenue.

## Scale
- Duke all-time: **1,827 payments · 1,582 customers · 16 seasons** (Fall 2018→Spring 2026); ~1,300–1,500 on the customer roster. **2 active campuses** (Duke; Columbia, with units stored in NJ).
- Marketing reach: ~**16,000 email contacts** (built via Carson's student-ID web-scraper), ~200 returning customers, 70+ spring-2026 signups.

## Operations & pricing
- **Seasonal cycle:** spring move-out dorm pickup → summer storage (Public Storage) → fall move-in delivery; local 16-ft Penske/U-Haul rentals; payments at the table via Square Reader / Tap-to-Pay.
- **Per-item pricing (catalog):** Small Box $55 · Large $70 · XL $85 · Wardrobe $110 · Mattress/Desk $125 · Dresser $165 · 3-seat couch $245 · Fridge $65 · TV $85 · Bike $95; surcharges +$20 (>50 lb) / +$40 (>100 lb). A full dorm ≈ $1,200–1,400.
- **Customer-facing extras:** $100 roommate discount, +$40 peak-day, +$100 home delivery; ambassadors paid $40/signup.
- **From the live email record (spring 2026):** the `contact@universityshipping.com` inbox **auto-forwards to Carson** (set up 2026-03-31); team answers from individual `*.uss@gmail.com` addresses. UShip **does not provide boxes** (recommends Home Depot/Amazon); offers a **15% military discount**; sizes by volume; a small box ≈ **$60** covers pickup + summer storage + fall drop-off; 3 large boxes summer+fall ≈ **$450**; **+$100 home delivery**. Northeast service stops include **Scarsdale, NYC, Long Island, Greenwich CT, East Hampton, Massachusetts (Marblehead), and Philadelphia**; spring move-out runs through ~May 3 with **rented trucks returned by May 9**; fall freshman move-in is **Aug 14–15**. Many customers are **repeat multi-year** affluent NE parents.

## Email marketing — the Wix engine & the scraped-list moat
Documented when Cole trained Carson on it (2026-06-30) and handed off the "emails" role.
- **Tooling:** customer email runs on **Wix email marketing**, off an inherited **template** iterated year-over-year. **Cadence:** ~1×/week in summer, **2×/week (Tue/Thu)** in the school year, ramping hard before move-out/move-in. Confirmation emails on signup are **built into Wix** (automatic).
- **The list:** everyone sits under one Wix label, **"2026 scrape,"** sub-segmentable by class year (~1,700 incoming freshmen as "class of 2029"); the freshman blast historically draws the most clicks (~4,000). Covers **all Duke students tied to unique Net-IDs — undergrad and grad** (via the DUID scrape).
- **Deliverability is the load-bearing rule:** send only to **accurate Net-ID emails** — bounces flag the sending address as spam, tanking reputability ("the biggest harm"). This is **what broke the Richmond expansion attempt** (no Net IDs → inaccurate scraped addresses → bounces). Sending from a personal/contact address uses **`contact@` + BCC-everyone** hygiene; `contact@universityshipping.com` re-routes to all six operators.
- **The scraped list is treated as a competitive moat.** Cole rates it well above how peers (Bull City Beds, Blue Box) gather emails; original scrape credited to "Joe Zachaloys" (spelling inferred; graduated); CSVs held by Matthew Moskow. A **monetization idea** (selling CSVs to BCB for ~$2k) was floated but is **legally unresolved**.

## The software — uship-os
Carson works the **data/analytics + finance** seat, and built **uship-os**, the internal multi-tenant operating system (v2.0.0): public booking funnel, HQ admin console, per-campus co-owner workspaces, mover day-of view, role-based access control, read-only **Square** and **QuickBooks** sync, provenance-aware finance, a New Campus Wizard. **Stack:** Next.js 14 · Prisma · **Postgres/Supabase** · NextAuth · Tailwind; hosted on **Render** (~$32/mo); repo `DudeslyGames/uship-os`. He also built the student-ID **web-scraper** behind the 16k marketing list.

## Team — the 6 current operators
Carson, Luca Adams Agresti, Daniel Heiman, Matthew Moskow, John Gorman, Cole Kannam. Carson says nobody in this group is passive. Tag and Marshall Seligson are alumni.
Operating roles: Carson (data/finance + OS), Matthew Moskow (data/website, "Matty"; LinkedIn title "Co-Owner and CTO"), Daniel Heiman ("Danny," expansion), John Gorman ("Gorm," logistics/Duke liaison), Cole Kannam (email), Luca (outreach/ambassadors).

## Expansion & risk
- **Columbia** was the first new market (spring 2026), verified: revenue **$9,972.55**, net **$7,248.31**, **72.68% margin**, **~25 customers**; stored locally in **New Jersey**. Ran on Daniel Heiman's friends **Orion** and **Gunner** (Danny flew up to run it in person) — which is why it was **50/50, not 80/20** ("Orion and Gunner did all the manual work and held the liability"). That gap is what the OS is meant to absorb.

> Columbia trademark cease-and-desist (May 2026). On **2026-05-01**, Columbia's **Director of Licensing (Daniela Elliott)** sent a formal **cease-and-desist** demanding UShip take down its **"Columbia University Shipping & Storage"** branding (a Canva site, the `columbiauniversitystorage@gmail.com` account, all use of Columbia's trademarked name + campus photos) within **5 business days (by May 8)**, and asked whether a legal entity by that name had been incorporated. Fallout: by mid-June Carson had brought in his father, attorney **Daniel Eisner** (McDermott Will & Schulte), to advise the team. (inferred from timing)

- For 26-27, the team has **not decided the specific target schools yet**. Earlier planning discussed pushing **4–5 schools in parallel** (NYU a candidate); platform built to scale toward "100 campuses." Each new school defaults to **80/20**. Carson's stated goal: "15 schools by this time next year."
- **Banking/legal (decided):** each campus = its own LLC + EIN + Square + bank account that **HQ controls** (HQ = sole banking authority), eliminating collection risk; chose Square over Stripe Connect.
- **Risk:** Duke admin may **ban UShip from move-in day** over equity optics; the team reframes as a shipping/drop-off service. Duke liaison is an administrator, **"Ben"**; move-in plan is trucks off campus, build "piles" early, blend in with early move-ins.

## The 2027 expansion playbook (formalized)
By May 2026 the strategy was written as a **Master Expansion Plan + a "Turnkey Platform Blueprint"**:
- **Scope:** every new school is **storage-only** (Duke's shipping line stays legacy/off-platform). The **wave = 4–5 new campuses for spring/summer-2027**, run **concurrently** with a Duke + Columbia pilot — Option A, **no fallback season**, so an **OS slip would risk all 6–7 campuses at once.**
- **The OS is Priority #1**, built (by Carson, in Claude Code) *before* schools are picked, parameterized by each campus's move-out day, **production-ready by ~Feb 2027.** Carries: master DB, per-campus dashboards, signup/confirmation tracking with auto-"bump," QR inventory, the **80/20 profit-waterfall payout engine**, role-scoped `campus_scope` access, a comms-timeline engine behind a co-owner **batch approval gate**.
- **Co-ownership = 20% of campus profit**, with a **graduation forfeit + pass-down** (each grad recruits a continuing-student successor). Legal vehicle routed to **Salus (CPA) + a lawyer**.
- **School selection leans on Carson's network.** A "Connection Map" tabulates warm contacts per target school — Theo (Michigan), Oliver Guyer (UChicago), Sam Bialkin (Emory), Joe Brener (Columbia passdown), Charlie & Gideon (Harvard). Research matrix favors high-OOS, high-dorm, remote, low-competition schools (Dartmouth "perfect"; avoid NYU/Harvard/UPenn).
- **Spring 2026 whole-business P&L:** income **$84,395**, net **$66,637.53 (78.96% margin)**.

### Legal restructure — UShip Ventures (in motion, 2026-06-22)
Expansion set up in a **new entity, "University Shipping & Storage Ventures LLC" (Delaware)** — a **holding company** over per-campus sub-LLCs (UShip Michigan, UShip Penn…), kept **separate from the legacy UShip 6 LLC** (NC, the Duke business). Structure **open and under active discussion** (draft IP-license and founder-OA documents exist), with live questions around HoldCo ownership and how Ventures acquires the "UShip" brand — which currently sits in the **70%-Gorman/Cole legacy LLC**. Carson treats the brand as a hard requirement.

## Story & how it runs
Carson joined as a co-owner in February 2026 and became its data/finance engine. His signature contribution: a **student-ID web-scraper** ("saved literally days," powers the ~16k list). He audits Square/the master sheet for unpaid invoices, calculates ambassador payouts, co-runs sorority-ambassador recruiting with Luca. Columbia launch ran through Daniel's friend "Gunner" (~25 customers). In June 2026, Carson + Luca ran a **C-suite recruiting push** — cold-emailing Duke students to become "Co-President of Marketing / future CMO," pitching UShip as **"$150,000+/year,"** low-commitment, a résumé asset. Demand-gen runs on **Duke Student Government email blasts**, **Google Search Console SEO**, and urgency campaigns; **BlueBox** is a competing Duke move-out service.

## Timeline (Carson's UShip year)
- **Feb 2026** — joins as co-owner (1 of 6).
- **Spring 2026** — builds the scraper; runs the ambassador program; Columbia pilot launches (~$10K, ~73% margin).
- **Apr–May 2026** — flyering push; big Duke move-out (~$63K May spike).
- **May 30, 2026** — new "Uship 26-27" team chat; reconstitutes minus graduated seniors.
- **June 2026** — finishes scraping; opens fall signups; debates the 4–5-school expansion; recruits Natalia Posen.
