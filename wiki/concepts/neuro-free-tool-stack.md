---
type: concept
kind: design
created: 2026-07-27
---

# Neuro free-tool stack (no subscription but Claude)

Cole's constraint: build the [[neuro-channel|Neuro]] pipeline so it adds **no new subscription** —
the only paid tool is the **Claude** plan he already has. Synthesized from the 7-video
[[stickman-animation-free-ai-tutorials|free-stickman-tutorial batch]], which proves the entire
faceless-animation workflow can run on **free accounts** (free ≠ subscription — a Google/CapCut/
YouTube login costs nothing). Also hard-wires Cole's second requirement: **he reviews every video
before it's posted.**

## The stack (step → free tool)
| Step | Tool (free) | Notes |
|---|---|---|
| Brain / orchestration | **Claude** (already have) | Claude Code runs the staged prompt + files/render; Claude chat drafts scripts. Replaces the tutorials' DeepSeek/ChatGPT. |
| Script + scene breakdown + **character consistency rules** | **Claude** | One staged prompt → concept, character profile, per-scene *image prompt + animation prompt + duration*. |
| Character art (consistent) | **Google Flow / Nano Banana 2** (free, unlimited image gen) | **Upload `neuro.png` as the reference** so the brain-head stays identical every scene; gen 2/scene, keep the clean one. → [[nano-banana-2]] |
| Voice | **Now:** free AI TTS (**MS Clipchamp** unlimited / **Google AI Studio** Gemini TTS). **Later:** **Cole's own voice** as the final pre-publish step. | **Decided 2026-07-27:** produce/preview with AI voice; **the last step before posting is to re-record in Cole's own voice** (better + dodges AI-voice **demonetization**). No paid [[elevenlabs|ElevenLabs]]. |
| Motion / animation | **His [[remotion|Remotion]] rig** (code, free) *or* **Google Flow** video (VO3, ~50 free credits/day ≈ one short) *or* static **image-per-scene** | Three paths — see [[neuro-character-rig]]. Simplest = image-per-scene; most "his own" = Remotion. |
| Timestamps / transcription | **Claude** directly, or TurboScribe (3/day) / Descript | Only needed if syncing images to a pre-recorded voice. |
| Music | **YouTube Studio audio library** (free) or Udio | Royalty-free. |
| Edit + captions | **[[remotion|Remotion]]** (code, free) or **CapCut** (free, auto-captions) | Remotion keeps it code-driven + reproducible; CapCut is the fast manual path. |
| Thumbnail / branding | **Google Flow** image + **Canva** free | Thumbnail from a generated frame + ≤3 words. |
| Publish | **Manual upload by Cole** | See the review gate below. |

**Net:** every step has a $0 option; the only recurring cost is the existing Claude plan. Google
Flow's daily-credit ceiling (~50/day) is the one real limiter → batch renders or use the static /
Remotion paths to avoid it.

## Review-before-post gate (Cole's requirement)
**Nothing auto-publishes.** The pipeline stops at a rendered MP4 and hands it to Cole:
1. Agent produces `out.mp4` + a draft title/description/thumbnail into the video folder.
2. **Cole reviews** — watches the render, does his ~10-min taste/polish pass, approves or sends
   notes.
3. **Voice swap (final pre-publish step):** before anything goes public, the AI TTS track is
   replaced with **Cole's own recorded voice** and re-rendered. AI voice is for drafting/preview
   only.
4. **Only Cole uploads** to YouTube (manual for now). Even when the YouTube API is added later, it
   stays **draft/unlisted-only** until Cole publishes. This is the human gate already in
   [[neuro-production-pipeline]] — made explicit and non-negotiable here.

## Recommended v1 (ship this)
Claude drafts script + per-scene prompts → **Cole records the voiceover** → Nano Banana 2 makes
the per-scene art from `neuro.png` → assemble to the voice in **Remotion** (or CapCut) with captions
→ **Cole reviews** → Cole uploads. Zero new subscriptions, one human gate, fully reproducible.
Related: [[neuro-production-pipeline]], [[neuro-character-rig]], [[neuro-channel]],
[[stickman-animation-free-ai-tutorials]].
