---
type: entity
category: venture / youtube channel
created: 2026-07-27
---

# Neuro (YouTube channel)

Cole's neuroscience-explainer **YouTube Shorts channel** — a stick-figure character named
**Neuro** (a friendly cartoon *brain* for a head, walking on stick-figure legs) who explains one
neuroscience idea in plain language per ~45–90s vertical video. Tagline in video #1: *"brain
science, simplified."* A separate code repo (`neuro-video/`, Remotion project) — this page is the
vault's record of the venture.

## The why (Cole's mission)
Make neuroscience **accessible**. Cole's belief: *"there's so much cool stuff that has helped me
learn, be better, mental health, everything — it could all be better if people understood their
brains better."* This is the purest expression of his central identity tension (see
[[cole|profile]]): **science ↔ building a company**, and **help others with what you've been given**.
It literally resolves his "why not both" — a business that commercializes his neuroscience
expertise *by* teaching people. Ties to his [[neuroscience-of-behavior|neuro obsession]] and Duke
Neuroscience major / [[marsh-memory-lab|Marsh lab]] work.

## Brand identity (decided 2026-07-27)
- **Name / handle:** **Doodlecortex** — doodle (the hand-drawn art style) + cortex (brain). Fits
  both the mascot and the visual format. Claim `@doodlecortex` on YouTube / TikTok / IG.
- **Email:** `doodlecortex@gmail.com` — creation **paused**: awaiting Cole's phone for verification.
- **Domain:** `doodlecortex.com` (~$12/yr one-time, later — not a subscription).
- **Credentials never live here** (this vault syncs to GitHub) — the account password belongs in a
  password manager / Keychain. See the vault-system password-holder task.

## The character
- **Neuro** — hand-drawn stick figure, head is a cartoon brain with a simple friendly face. The
  walking-brain-head *is* the joke and lands instantly. Source art: `public/neuro.png`.
- **Video #1 (current):** uses the PNG as a flat image — whole-figure motion only (bob, tilt,
  slide, scale, bounce). Deliberately simple to ship.
- **Future:** rebuild Neuro as a fully articulated SVG (gesturing arms, blinking eyes, mouth
  synced to speech, brain that pulses) — *only when Cole asks*. Design for how: **[[neuro-character-rig]]**
  (an SVG skeletal rig Claude Code authors as code — the "automatically with Claude Code" answer).

## Pipeline (semi-automated)
1. **Topic** (Cole) — one narrow, punchy idea (e.g. "why you forget why you walked into a room").
2. **Script + storyboard** (claude.ai chat) — ~150–200 word voice-ready script + scene-by-scene
   storyboard as JSON/table. Cole can use his **[[claude-chat-prompt]]** skill for this.
3. **Voiceover** (Cole) — [[elevenlabs|ElevenLabs]] custom "Neuro" voice → MP3 into `public/`.
4. **Build** (Claude Code) — `ffprobe` the MP3 for exact duration → author the [[remotion|Remotion]]
   composition timed to audio → `remotion studio` preview → render MP4.
5. **Polish** (Cole, ~10 min) → **Upload** (Cole, manual for now).

## Status
- **Video #1** — channel-trailer / intro, **36.4s**, `out/neuro-intro.mp4`, rendered & ready to
  upload. Built via the Python/PIL+ffmpeg fallback (claude.ai sandbox couldn't fetch Chromium);
  **Remotion is the path forward** for all future videos.

## The vault is the content engine (the key connection)
This channel and this vault are the **same project pointed two directions**: Cole ingests
neuroscience into the wiki, and the wiki becomes the **topic bank + researched script source** for
Neuro. Every concept page below is a ready Short:

| Concept page | Video hook |
|---|---|
| [[conscious-vs-subconscious]] (7±2 working memory) | "Why you forget why you walked into a room" |
| [[reticular-activating-system]] | "Why you suddenly see your new car *everywhere*" |
| [[neuroplasticity]] | "Why New Year's resolutions fail — and what actually works" |
| [[memory-consolidation]] | "Why cramming doesn't work (your brain learns while you sleep)" |
| [[productive-discomfort]] | "Why hard things literally rewire your brain" |
| [[hebbian-learning]] | "Neurons that fire together, wire together" |
| [[predictive-processing]] | "Your brain is a prediction machine" |
| [[knowledge-types]] / [[learning-by-connection]] | "Why you remember *nothing* from that podcast" |
| [[cognitive-biases]] | one Short per bias (anchoring, sunk cost, FAE…) |
| [[temporal-discounting]] | "Why your brain sabotages your future self" |

Each ingest of a new neuro source (see the [[neuroscience-of-behavior]] hub) refills this bank —
the same compounding loop as [[llm-wiki-pattern]], now feeding a channel.

**First 3 scripts drafted (2026-07-29):** the top three rows above now have ready
voice-ready scripts + storyboard JSON in **[[neuro-scripts-batch-1]]**, built on the
short-form rules researched in **[[neuro-shorts-benchmark]]** (which channels to model, hooks,
pacing, titles). Awaiting Cole's topic approval — recommend the doorway-effect one first.

## The app (channel × app) — Cole's larger vision
The channel is top-of-funnel for a **learning app** that embodies the neuroscience it teaches.
The thesis (worked out 2026-07-27, grounded in the spaced-learning ingest): **not "another Anki,"
but a spacing engine that triages material into [[knowledge-types|Skill / Concept / Fact]] and
schedules the *right retrieval modality per type*** — flashcards for facts ([[spaced-repetition]],
wrapping Anki/FSRS as a commodity), spaced **explain-from-scratch** for concepts (LLM-graded),
spaced **[[interleaving|interleaved]] practice** for skills. The LLM does what a flashcard can't:
triage, grade a from-scratch explanation, generate interleaved problems.

- **Why it's defensible:** the competitor [[spacerep|SpaceRep]] (FSRS + Google Calendar) and Anki
  schedule *one* modality for everything; the evidence says types need different retrieval
  ([[spacing-math-meta-analysis-murray-2025]] — flashcard-style retrieval was *not* robust for
  math). On-brand for a neuroscience channel; the science *is* the marketing.
- **Why "now, not last summer":** the differentiator moved from the scheduler (now a commodity —
  don't rebuild FSRS) to LLM coaching of concepts/skills, which is newly good.
- **The vault de-risks it:** start as a **Learning-Triage skill in this vault**, run it on real
  class material this semester; if the loop changes how Cole studies, *that validated loop is the
  app's core*. Adoption (people know spacing works and don't do it —
  [[neuroscience-of-spacing-brainfacts]]) is the real problem, so the intervention belongs at
  *capture time*. Full strategy captured in the concept pages under [[neuroscience-of-behavior]];
  a design spec is the natural next step (see [[tasks/index|tasks]]).

## Tech
[[remotion|Remotion]] (React → MP4, headless Chrome), [[elevenlabs|ElevenLabs]] (voice),
[[claude-code]] (build/render), Node 22+. Planned: auto caption-sync (`@remotion/media-utils`),
script-gen via the [[claude-api|Claude API]], YouTube Data API upload, GitHub Actions render.

## Producing & storing automatically
See **[[neuro-production-pipeline]]** for the design: a spec-driven pipeline (Claude API script →
ElevenLabs voice → Remotion render → YouTube upload) where the **`spec.json` is the source of truth
and the MP4 is a rebuildable artifact**, with the vault holding a queryable video **catalog**.

## Production status (2026-07-27) — pivot to AI doodle scenes
Reference bar: **@Zenn0009** — those channels are **hand-drawn illustrated explainers** (a new custom
doodle scene every few seconds), *not* one animated character. Validated that **Gemini / Nano Banana
generates Zenn-quality doodle scenes free** through Cole's Google login. **Direction:** AI-generated
doodle scenes are the engine; the `~/Desktop/neuro-video` **Remotion** rig shrinks to captions +
assembly + an optional Neuro cameo. The rig now uses Cole's *actual* drawing (`neuro-real.png` /
`neuro-head.png`) and can walk/gesture. Next: build the script → doodle-scenes → captions/voice →
render pipeline (route A Gemini API vs B free web UI — Cole to decide). See the [[Neuro]] bucket board.

Related: [[cole]], [[neuroscience-of-behavior]], [[neuro-production-pipeline]], [[Neuro]] bucket.
