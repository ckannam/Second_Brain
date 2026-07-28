---
type: entity
category: tool
---

# Remotion

Framework for making **videos as React components**, rendered to MP4 via headless Chrome
(remotion.dev). The preferred renderer for Cole's [[neuro-channel|Neuro]] channel — live browser
preview + hot reload (`remotion studio`), composable scenes, and version-controlled compositions.

- **Timing is frame-based:** `FPS = 30`; every cue point is `seconds * 30`. Always derive
  `TOTAL_FRAMES` from the *actual* audio duration (`ffprobe` the [[elevenlabs|ElevenLabs]] MP3),
  never a hardcoded guess.
- **Motion primitives:** `spring()` for pop-in entries, `interpolate()` (clamped) for slides/fades.
- **Render:** `npx remotion render …`; **preview:** `npx remotion studio` (localhost:3000).
- Requires a local Chromium (auto-installed on first run) — which is exactly why the claude.ai
  sandbox couldn't use it for [[neuro-channel|video #1]] (Python/PIL+ffmpeg fallback instead).

Planned use of `@remotion/media-utils` (`getAudioData` / `visualizeAudio`) to drive caption timing
from the audio waveform instead of hand-mapped frames.
