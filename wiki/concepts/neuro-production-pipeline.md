---
type: concept
kind: design
created: 2026-07-27
---

# Neuro production pipeline (automate produce + store)

Design for producing and storing [[neuro-channel|Neuro]] videos automatically. Filed from Cole's
question "do you have an idea how to actually produce and store these automatically?" — a design
doc, **not built yet**.

## The one principle that makes this simple
**The spec is the source of truth; the MP4 is a disposable build artifact.** Each video is fully
described by a small JSON file (topic, script, storyboard, cue frames, voice settings). Given the
spec + the voice MP3, the exact video re-renders on demand. So you **version the spec, not the
video** — no hoarding gigabytes of binaries, and any old video is reproducible/editable forever.
This is the same "reproducible source → rebuildable output" idea behind [[remotion|Remotion]]
compositions and [[llm-wiki-pattern|this vault]].

## Produce — a spec-driven pipeline
One folder per video (`videos/<slug>/` in the `neuro-video` repo): `spec.json`, `voice.mp3`,
`out.mp4`. The chain, each step already API-automatable:

1. **Topic** → pulled from the vault's [[neuroscience-of-behavior]] topic bank (a concept page per
   idea). A scheduled routine can *propose* the next one.
2. **Script + storyboard → `spec.json`** — a [[claude-api|Claude API]] call given the topic **plus
   the matching vault concept page as context**, returning structured JSON (script lines +
   per-scene cues + **per-scene image + animation prompts** + Neuro's motion). This is why the vault
   matters: the scripts are *researched*, not hallucinated. (Interim: draft in claude.ai with
   [[claude-chat-prompt]].) Per-scene art from **Nano Banana 2 using `neuro.png` as the consistency
   reference** — see [[neuro-free-tool-stack]].
3. **Voiceover → `voice.mp3`** — **free AI TTS now** (MS Clipchamp / Google AI Studio) for
   drafting/preview; **swap in Cole's own recorded voice as the final step before publishing**
   (decided 2026-07-27). No paid [[elevenlabs|ElevenLabs]] — **no subscription but Claude**; see
   **[[neuro-free-tool-stack]]**.
4. **Render → `out.mp4`** — `ffprobe` the MP3 for exact duration → build/update the Remotion
   composition timed to it → `remotion render`.
5. **Publish** — YouTube Data API v3 upload as **unlisted/private draft** for Cole's final call.

**Where it runs (pick by ambition):**
- **v1 — local Mac, one command.** A `make video SLUG=…` (or small Node script) runs steps 2–4 on
  Cole's machine (he already has Node + Remotion). Simplest real automation; zero cloud. **Start
  here.**
- **v2 — no Mac needed.** Render on **Remotion Lambda** or a **GitHub Action** (render on push,
  artifact the MP4) so it runs headless in the cloud — pairs with [[claude-code-scheduled-tasks]]
  to run overnight.

**Keep one human gate — Cole reviews before it's posted (hard requirement).** The pipeline stops at
a rendered MP4; Cole watches it, does his ~10-min taste/polish pass, and is the **only** one who
uploads. Nothing auto-publishes — even once the YouTube API is added it stays draft/unlisted until
Cole publishes. Automate the grunt work, not the judgment. Detail in [[neuro-free-tool-stack]].

## Store — three layers, each holding the right thing
- **Source (git, in `neuro-video`):** every `spec.json` + script. Small, diffable, the real
  archive — the videos *are* these files.
- **Masters (binaries, NOT git):** MP4s bloat a repo. Options, cheapest first: treat **YouTube
  (unlisted) as the archive**; or a **Cloudflare R2 / S3 bucket**; or **Git LFS**. Recommendation:
  YouTube-as-archive + keep the spec; only push masters to R2 if you need raw files.
- **Catalog (this vault):** the vault "stores" the videos as a **queryable catalog** — one row/page
  per video linking back to the concept it teaches. This closes the loop *ingest → wiki → video →
  catalog → back into the wiki*. Seed table below; grow into a `neuro/videos/` folder + Dataview
  if volume justifies.

| Video | Concept source | Status | Duration | URL |
|---|---|---|---|---|
| #1 — intro / trailer | — (channel intro) | rendered, ready to upload | 36.4s | _(pending)_ |

## Honest gaps / risks
- **YouTube API:** OAuth + daily quota; an unverified app can only upload **private/unlisted** until
  Google review — fine for a human-in-the-loop publish flow, plan for it before full auto-publish.
- **ElevenLabs:** per-character cost/quota — cheap at this length, but metered.
- **Remotion Lambda:** needs AWS setup; skip until v1 proves the format.
- **Cost at this scale is trivial** (cents/video); the real budget is Cole's taste pass.

## Plan A — automated doodle-scene pipeline (chosen 2026-07-27)
After the [[neuro-channel|Zenn-bar]] pivot, the engine is **AI-generated hand-drawn doodle scenes**
(Gemini **Nano Banana 2**, ~$0.045–0.067/image → ~$0.40–0.60 per ~12-scene Short, free tier for
testing); Remotion is reduced to captions + assembly + an optional Neuro cameo.
- **Prereq (Cole):** Gemini API key (aistudio.google.com) → Keychain/env, never the vault.
- **Pipeline:** topic + vault concept page → Claude writes `spec.json` (per scene: caption, image
  prompt, duration, Neuro-in-scene?) → Node calls Nano Banana 2 with a **locked doodle-style prompt +
  `neuro-real.png` reference** (2 variants, keep best) → free TTS voice (own voice final) → Remotion
  assembles scene images (subtle zoom/pop) + [[#Review-before-post gate|kinetic captions]] + voice →
  render → **Cole reviews** → upload.
- **Phases:** P0 API key · P1 scene-gen script (prove 3–4 consistent scenes) · P2 Remotion
  scene-sequence comp · P3 voice+timing · P4 first full Short ("walk into a room and forget") · P5
  polish (consistency, transitions, thumbnail) + templatize.

## Recommended path
Ship **v1 (local one-command spec→render)** next, keep the human gate, catalog each video here, and
only add cloud render + auto-publish once the format is proven. Related: [[neuro-channel]],
[[remotion]], [[elevenlabs]], [[claude-code-scheduled-tasks]], [[claude-api]].
