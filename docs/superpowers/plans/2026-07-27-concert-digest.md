# Concert Digest Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a weekly Monday-8am iMessage digest of concerts near Cole — his artists plus taste-matched discovery — that auto-switches from Baltimore to the Triangle on his move date.

**Architecture:** A Cole-editable taste profile lives in the vault (`profile/concert-taste.md`). A launchd job fires Monday 8am → `run_digest.sh`, which computes the active metro deterministically (pure Python helper) and launches a headless Claude session that invokes the `concert-digest` skill. The skill web-searches artists + local venue calendars, ranks by taste and proximity, composes a scannable block, and sends it via an AppleScript iMessage send (the same delivery path the networking brief proved). A "section" mode returns just the text block for a future combined weekly update.

**Tech Stack:** Bash + launchd (scheduling), Python 3 (pure date→metro helper, unit-tested), AppleScript/osascript (iMessage delivery), headless Claude Code CLI (`claude -p`) with web search (the agentic compose step), Markdown (skill + profile).

## Global Constraints

- iMessage self-chat target: **+14436822254** (Cole's number; also colekannam@gmail.com).
- Location cutover date: **2026-08-17** — before it Baltimore metro, on/after it Triangle (Durham/Raleigh). Single constant, editable in `profile/concert-taste.md`.
- Schedule: **Monday ~8am** local (launchd `Weekday` 1).
- Scaffolding home: **`~/.claude/concerts/`** (mirrors `~/.claude/networking/`).
- Skill home: **`<vault>/.claude/skills/concert-digest/SKILL.md`** (vault-local skills dir; `networking-prep` already lives there).
- Claude CLI path: **`/Users/colekannam/.npm-global/bin/claude`**.
- Vault path: **`/Users/colekannam/Desktop/Second Brain`**.
- Delivery must be non-interactive (headless/launchd) — never require Cole to be at the keyboard.
- Never invent shows or ticket links; only report what live search surfaces. Empty week → send an honest short note, not a fake list.

---

### Task 1: Taste profile data file

**Files:**
- Create: `/Users/colekannam/Desktop/Second Brain/profile/concert-taste.md`

**Interfaces:**
- Produces: a markdown file with H2 sections `## Love / seen`, `## Want to see`, `## Discovery seeds`, `## Venues`, `## Settings`. The skill (Task 4) and the run script (Task 5) read `## Settings` for `cutover:` and `window_weeks:`.

- [ ] **Step 1: Write the profile file**

```markdown
---
type: reference
created: 2026-07-27
---
# Concert Taste  (source of truth for the weekly digest)

Cole-editable. The weekly [[concert-digest]] reads this file. Add/remove artists anytime;
the next run picks it up. Two hobbies Cole is investing in: travel + live music.

## Love / seen
Tyler Childers, Zach Bryan, Billy Strings, Phish, Trampled by Turtles,
Joe Russo's Almost Dead (JRAD), Greensky Bluegrass, Caamp, Turnpike Troubadours,
Nathaniel Rateliff, Mt. Joy, Twiddle, Deer Tick, Joey Bada$$, Baby Keem, Lil Yachty,
Redveil, Jack Johnson, Paul Simon, Bruno Mars, Maroon 5, Damian Marley, Goose,
Sturgill Simpson

## Want to see
Stews, Harvey Street, Geese, Sturgill Simpson

## Discovery seeds
Core lane (weight high): jam / newgrass — Phish, Billy Strings, Goose, JRAD, Greensky,
Twiddle, Trampled by Turtles; Americana / country — Tyler Childers, Zach Bryan,
Turnpike Troubadours, Sturgill Simpson, Nathaniel Rateliff.
Secondary (weight medium): indie folk-rock — Caamp, Mt. Joy, Deer Tick, Jack Johnson.
Lower (standout shows only): hip-hop — Joey Bada$$, Baby Keem, Lil Yachty, Redveil.

## Venues
### Baltimore / DC (active before cutover)
Merriweather Post Pavilion (Columbia), Rams Head Live, Ram's Head On Stage (Annapolis),
The Ottobar, Baltimore Soundstage, Pier Six Pavilion, CFG Bank Arena, The 8x10,
The Anthem (DC), 9:30 Club (DC).
### Triangle (active on/after cutover)
Cat's Cradle (Carrboro), DPAC (Durham), Motorco (Durham), The Pinhook (Durham),
Haw River Ballroom (Saxapahaw), The Ritz (Raleigh), Red Hat Amphitheater (Raleigh),
Coastal Credit Union Music Park / Walnut Creek (Raleigh), Lincoln Theatre (Raleigh),
Kings (Raleigh).

## Settings
cutover: 2026-08-17
window_weeks: 8
```

- [ ] **Step 2: Verify required sections exist**

Run:
```bash
cd "/Users/colekannam/Desktop/Second Brain" && \
for s in "## Love / seen" "## Want to see" "## Discovery seeds" "## Venues" "## Settings" "cutover: 2026-08-17" "window_weeks: 8"; do \
  grep -qF "$s" profile/concert-taste.md && echo "OK: $s" || echo "MISSING: $s"; done
```
Expected: seven `OK:` lines, no `MISSING`.

- [ ] **Step 3: Do NOT commit**

`profile/` is deliberately gitignored (local-only, derived-from-private-data — same policy
as `finance/`). The file must live on disk (the skill reads it from disk) but must NOT be
force-committed into git history. Leave it untracked/ignored. Verify:
```bash
cd "/Users/colekannam/Desktop/Second Brain" && git check-ignore profile/concert-taste.md
```
Expected: prints `profile/concert-taste.md` (confirming it's ignored, not tracked).

---

### Task 2: Active-metro date helper (pure, unit-tested)

**Files:**
- Create: `~/.claude/concerts/active_metro.py`
- Test: `~/.claude/concerts/test_active_metro.py`

**Interfaces:**
- Produces: `active_metro(today: datetime.date, cutover: datetime.date = date(2026,8,17)) -> str` returning `"baltimore"` or `"triangle"`. Also runnable as a CLI: `python3 active_metro.py YYYY-MM-DD` prints the metro (used by Task 5). With no arg, uses today.

- [ ] **Step 1: Write the failing test**

```python
# ~/.claude/concerts/test_active_metro.py
import datetime, subprocess, sys, pathlib
from active_metro import active_metro

CUT = datetime.date(2026, 8, 17)

def test_before_cutover_is_baltimore():
    assert active_metro(datetime.date(2026, 8, 16), CUT) == "baltimore"

def test_on_cutover_is_triangle():
    assert active_metro(datetime.date(2026, 8, 17), CUT) == "triangle"

def test_after_cutover_is_triangle():
    assert active_metro(datetime.date(2026, 9, 1), CUT) == "triangle"

def test_cli_prints_metro():
    here = pathlib.Path(__file__).parent
    out = subprocess.check_output(
        [sys.executable, str(here / "active_metro.py"), "2026-09-01"], text=True).strip()
    assert out == "triangle"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/.claude/concerts && python3 -m pytest test_active_metro.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'active_metro'`.

- [ ] **Step 3: Write minimal implementation**

```python
# ~/.claude/concerts/active_metro.py
"""Deterministic Baltimore->Triangle cutover for the weekly concert digest."""
import datetime, sys

DEFAULT_CUTOVER = datetime.date(2026, 8, 17)

def active_metro(today: datetime.date, cutover: datetime.date = DEFAULT_CUTOVER) -> str:
    return "baltimore" if today < cutover else "triangle"

if __name__ == "__main__":
    today = datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else datetime.date.today()
    print(active_metro(today))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `cd ~/.claude/concerts && python3 -m pytest test_active_metro.py -v`
Expected: 4 passed. (If pytest is unavailable, run `python3 -c "from active_metro import active_metro; import datetime; assert active_metro(datetime.date(2026,8,16))=='baltimore' and active_metro(datetime.date(2026,8,17))=='triangle'; print('ok')"` → prints `ok`.)

- [ ] **Step 5: Commit**

```bash
cd ~/.claude/concerts && git init -q 2>/dev/null; true
# (~/.claude is not the vault repo; these files are tracked only if ~/.claude is a repo.
#  If not a repo, skip the commit — the vault spec/plan already records them.)
```
Note: `~/.claude/concerts/` lives outside the vault git repo (like `~/.claude/networking/`). No commit needed there; the vault plan documents it. Skip this step if `~/.claude` is not a git repo.

---

### Task 3: iMessage send script

**Files:**
- Create: `~/.claude/concerts/send.scpt`

**Interfaces:**
- Produces: `osascript ~/.claude/concerts/send.scpt "<message text>"` sends the text to Cole's iMessage self-chat. Consumed by Task 4 (standalone mode) and Task 5.

- [ ] **Step 1: Write the send script** (mirrors the proven networking `send.scpt`)

```applescript
on run argv
	set msg to item 1 of argv
	tell application "Messages"
		set svc to 1st account whose service type = iMessage
		set toBuddy to participant "+14436822254" of svc
		send msg to toBuddy
	end tell
end run
```

- [ ] **Step 2: Verify with a real test send**

Run: `osascript ~/.claude/concerts/send.scpt "🎵 concert digest test send — ignore"`
Expected: exit 0, and the message arrives in Cole's iMessage self-chat. (First run may prompt macOS Automation/TCC permission for Messages — approve it, same as the networking brief required.)

- [ ] **Step 3: No commit** — outside the vault repo (see Task 2 note).

---

### Task 4: `concert-digest` skill (the agentic compose step)

**Files:**
- Create: `/Users/colekannam/Desktop/Second Brain/.claude/skills/concert-digest/SKILL.md`

**Interfaces:**
- Consumes: `profile/concert-taste.md` (Task 1); `~/.claude/concerts/send.scpt` (Task 3).
- Produces: the skill Claude invokes. Inputs passed in the launch prompt (Task 5): `ACTIVE_METRO` (`baltimore`|`triangle`), `TODAY` (ISO date), `MODE` (`standalone`|`section`).

- [ ] **Step 1: Write the skill file**

````markdown
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
````

- [ ] **Step 2: Dry-run in section mode (no send)**

Run:
```bash
cd "/Users/colekannam/Desktop/Second Brain" && \
/Users/colekannam/.npm-global/bin/claude -p \
"Use the concert-digest skill. ACTIVE_METRO=baltimore TODAY=2026-07-28 MODE=section. Compose the block only; do not send." \
--dangerously-skip-permissions
```
Expected: prints a "🎵 Concerts near you — Baltimore/DC …" block with real, plausible shows and no fabricated URLs; nothing is sent to iMessage.

- [ ] **Step 3: Commit the skill**

```bash
cd "/Users/colekannam/Desktop/Second Brain"
git add .claude/skills/concert-digest/SKILL.md
git commit -m "Concert digest: concert-digest skill (agentic compose + send)"
```

---

### Task 5: Run script (deterministic metro → headless agentic compose+send)

**Files:**
- Create: `~/.claude/concerts/run_digest.sh`

**Interfaces:**
- Consumes: `active_metro.py` (Task 2), the `concert-digest` skill (Task 4), `profile/concert-taste.md` `## Settings` cutover.
- Produces: the launchd entry point (Task 6). Logs to `~/.claude/concerts/digest.log`.

- [ ] **Step 1: Write the run script**

```bash
#!/bin/bash
# Weekly concert digest: compute the active metro deterministically, then let a headless
# Claude session run the concert-digest skill to search, compose, and send via iMessage.
# Runs from launchd (Mon 8am) or manually. Logs to ~/.claude/concerts/digest.log
set -o pipefail
VAULT="/Users/colekannam/Desktop/Second Brain"
CDIR="$HOME/.claude/concerts"
LOG="$CDIR/digest.log"
CLAUDE="/Users/colekannam/.npm-global/bin/claude"
TODAY="$(date +%F)"

# Read cutover from the profile so Cole can shift the move date in one place.
CUT="$(grep -E '^cutover:' "$VAULT/profile/concert-taste.md" | awk '{print $2}')"
METRO="$(/usr/bin/python3 "$CDIR/active_metro.py" "$TODAY" 2>>"$LOG")"
[ -n "$CUT" ] && METRO="$(/usr/bin/python3 - "$TODAY" "$CUT" <<'PY' 2>>"$LOG"
import datetime,sys
from importlib.machinery import SourceFileLoader
import os
m=SourceFileLoader("am",os.path.expanduser("~/.claude/concerts/active_metro.py")).load_module()
t=datetime.date.fromisoformat(sys.argv[1]); c=datetime.date.fromisoformat(sys.argv[2])
print(m.active_metro(t,c))
PY
)"
[ -z "$METRO" ] && METRO="baltimore"

echo "$(date) running digest: metro=$METRO today=$TODAY cutover=$CUT" >>"$LOG"
cd "$VAULT" || { echo "$(date) ERROR: no vault" >>"$LOG"; exit 1; }
"$CLAUDE" -p \
"Use the concert-digest skill. ACTIVE_METRO=$METRO TODAY=$TODAY MODE=standalone. Search, compose, and send the digest to iMessage per the skill." \
--dangerously-skip-permissions >>"$LOG" 2>&1 \
  && echo "$(date) digest run complete ($METRO)" >>"$LOG" \
  || echo "$(date) ERROR: digest run failed" >>"$LOG"
```

- [ ] **Step 2: Make executable**

Run: `chmod +x ~/.claude/concerts/run_digest.sh`
Expected: exit 0.

- [ ] **Step 3: Manual end-to-end run (real send)**

Run: `~/.claude/concerts/run_digest.sh; tail -n 5 ~/.claude/concerts/digest.log`
Expected: log shows `metro=baltimore` (today is before cutover) and `digest run complete`; a "🎵 Concerts near you" message arrives in Cole's iMessage self-chat.

- [ ] **Step 4: No commit** — outside the vault repo (see Task 2 note).

---

### Task 6: launchd schedule (Monday ~8am)

**Files:**
- Create: `~/Library/LaunchAgents/com.cole.concert-digest.plist`

**Interfaces:**
- Consumes: `~/.claude/concerts/run_digest.sh` (Task 5). Mirrors `com.cole.networking-brief.plist`.

- [ ] **Step 1: Write the plist**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>com.cole.concert-digest</string>
	<key>ProgramArguments</key>
	<array>
		<string>/bin/bash</string>
		<string>/Users/colekannam/.claude/concerts/run_digest.sh</string>
	</array>
	<key>StartCalendarInterval</key>
	<dict>
		<key>Weekday</key>
		<integer>1</integer>
		<key>Hour</key>
		<integer>8</integer>
		<key>Minute</key>
		<integer>5</integer>
	</dict>
	<key>StandardOutPath</key>
	<string>/Users/colekannam/.claude/concerts/launchd.out</string>
	<key>StandardErrorPath</key>
	<string>/Users/colekannam/.claude/concerts/launchd.err</string>
	<key>RunAtLoad</key>
	<false/>
</dict>
</plist>
```

- [ ] **Step 2: Load it**

Run: `launchctl unload ~/Library/LaunchAgents/com.cole.concert-digest.plist 2>/dev/null; launchctl load ~/Library/LaunchAgents/com.cole.concert-digest.plist`
Expected: exit 0, no error.

- [ ] **Step 3: Verify it is registered**

Run: `launchctl list | grep concert-digest`
Expected: a line containing `com.cole.concert-digest`.

- [ ] **Step 4: No commit** — outside the vault repo.

---

### Task 7: Wire-up docs, memory, and log

**Files:**
- Modify: `/Users/colekannam/Desktop/Second Brain/log.md` (append a dated entry)
- Modify: `/Users/colekannam/Desktop/Second Brain/buckets/Personal.md` (link the hobby/digest under Personal)
- Create: `/Users/colekannam/.claude/projects/-Users-colekannam-Desktop-Second-Brain/memory/cole-concert-digest.md`
- Modify: `/Users/colekannam/.claude/projects/-Users-colekannam-Desktop-Second-Brain/memory/MEMORY.md` (index line)

**Interfaces:**
- Consumes: everything above. This task records the system so future sessions can find and maintain it.

- [ ] **Step 1: Append a log entry** to `log.md` (follow the file's existing dated-entry format) summarizing: weekly concert digest shipped — Mon 8am, Baltimore→Triangle auto-flip 2026-08-17, taste profile at `profile/concert-taste.md`, skill `concert-digest`, scaffolding in `~/.claude/concerts/`.

- [ ] **Step 2: Add a Hobbies/live-music line** under the Personal bucket linking `[[concert-taste]]` and describing the weekly digest, so the vault surfaces it.

- [ ] **Step 3: Write the memory file**

```markdown
---
name: cole-concert-digest
description: Weekly iMessage concert digest — taste profile, skill, Mon 8am launchd, Baltimore->Triangle flip.
metadata:
  type: project
---

Cole's two favorite hobbies are travel + live music; he wants to invest more in hobbies.
A weekly **concert digest** texts his iMessage self-chat every **Monday ~8am**: his artists
+ taste-matched discovery near him. Source of truth: `profile/concert-taste.md` (Cole-editable
artist list, venues per metro, `cutover:` date). Skill: `concert-digest` (agentic — web-searches
+ composes + sends). Scaffolding: `~/.claude/concerts/` (`active_metro.py`, `send.scpt`,
`run_digest.sh`) + launchd `com.cole.concert-digest`. Auto-switches Baltimore -> Triangle
(Durham/Raleigh) on **2026-08-17** (his move). Built to also expose a section mode for a future
combined weekly update. Delivery reuses the [[cole-proactive-imessage-channel]] pattern.
```

- [ ] **Step 4: Add the MEMORY.md index line**

`- [Weekly concert digest](cole-concert-digest.md) — Mon 8am iMessage; taste profile + Baltimore→Triangle flip 2026-08-17.`

- [ ] **Step 5: Commit vault changes**

```bash
cd "/Users/colekannam/Desktop/Second Brain"
git add log.md buckets/Personal.md
git commit -m "Concert digest: log + Personal bucket wire-up"
```
(The memory files live outside the vault repo; no vault commit for them.)

---

## Self-Review

**Spec coverage:**
- Taste profile source of truth → Task 1. ✓
- Agentic weekly run (search + rank + compose) → Task 4. ✓
- Taste-matched discovery (🔎) → Task 4 step 1 (Discovery seeds + step 3/5). ✓
- Location auto-flip 2026-08-17 → Task 2 (helper) + Task 5 (reads cutover) + Task 1 (`## Settings`). ✓
- Monday ~8am schedule → Task 6. ✓
- iMessage delivery (proven path) → Task 3 + Task 5. ✓
- Standalone now / section-mode hook for future weekly update → Task 4 (`MODE`). ✓
- Error handling (empty week honest note; never fabricate) → Task 4 rules; log-and-noop on failure → Task 5. ✓
- Testing (dry-run, location flip, real send) → Task 2 unit tests, Task 4 step 2 dry-run, Task 5 step 3 real send. ✓

**Placeholder scan:** No TBD/TODO; every file has literal content. ✓

**Type consistency:** `active_metro(today, cutover)` signature identical in Task 2 test, impl, and Task 5 caller; `ACTIVE_METRO`/`TODAY`/`MODE` input names identical across Task 4 and Task 5. ✓

## Security note

`run_digest.sh` invokes `claude -p … --dangerously-skip-permissions` so the scheduled run is
non-interactive (web search + osascript send with no prompt). This runs only Cole's own local
job against his own vault and machine. If he prefers a tighter posture, replace the flag with an
explicit allowed-tools list once the exact tool names used by the run are known.
