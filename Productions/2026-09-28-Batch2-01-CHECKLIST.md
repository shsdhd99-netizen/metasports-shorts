# Mon Sep 28 - Batch 2 #1 checklist

**Short:** LeBron's 92% Pay Cut
**Title (exact, NO hashtags):** LeBron's 92% Pay Cut (use the Batch 2 emoji title as written)
**Post window:** 6:00-11:00 AM ET (aim ~8 AM if scheduling)
**Script source:** MetaSports - Scripts (Batch 2).md -> #1
**Pin within 1 min of upload:** Would you take a 92% pay cut to chase one more ring?
**Before post:** re-check roster/facts on ESPN link in Batch 2 notes (marked roster).

Do not download Drift. Do not block on ShortsOS Phase 0.

---

## Timeline (ET)

| Time | Step |
|---|---|
| ~6:00-6:15 | Confirm ElevenLabs Tools\.env has real key + voice ID (not placeholders). Run: python voiceover.py --check |
| ~6:15-6:30 | Prep production folder + script -> generate voiceover |
| ~6:30-7:15 | DaVinci edit (vertical 9:16) |
| ~7:15-7:30 | Export + watch once on phone |
| ~7:30-8:00 | Upload / schedule for 8 AM ET (or go live in-window) |
| by 11:00 | Must be public. Pin the question. Leave description blank (or one line). NO hashtags. |

---

## Step A - Voiceover

1. Open cmd in YouTube-Playbooks\Tools.
2. Make folder: Productions\MetaSports\2026-09-28 LeBron 92 pct pay cut\
3. Save spoken text only as script.txt in that folder (Batch 2 #1 body; no title line).
4. Optional dry run:
   python voiceover.py --script "..\Productions\MetaSports\2026-09-28 LeBron 92 pct pay cut\script.txt" --dry-run
5. Generate:
   python voiceover.py --script "..\Productions\MetaSports\2026-09-28 LeBron 92 pct pay cut\script.txt"
   Expect: voice.mp3 + captions.srt (+ words.json) in that folder.
6. Optional Claude path: /voiceover 1 from the playbooks folder.

---

## Step B - DaVinci Resolve (already installed)

1. Vertical project: File -> Project Settings -> Master Settings -> 1920x1080, Use vertical resolution, 30 fps.
2. Import voice.mp3 + NBA clips. Voice on A1, clips on V1. Moment on screen from frame 1 (no title card).
3. File -> Import -> Subtitle... -> captions.srt. Style: big bold white + black outline, middle third.
4. Optional quiet music under voice (~-25 dB).
5. Deliver: MP4 / H.264 / 1080x1920, burn subtitles into video -> Render.

(Claude + Resolve CursorBridge is optional; hand edit is fine for day 1.)

---

## Step C - Post (YouTube Short)

1. Upload the render as a Short.
2. Title exactly as in Batch 2 #1 (LeBron's 92% Pay Cut + emoji) - NO hashtags in title or description.
3. Description: blank or one plain line. No tags needed.
4. Publish (or schedule) so it goes live between 6 and 11 AM ET.
5. Within ~1 minute, pin: Would you take a 92% pay cut to chase one more ring?
6. First frame of the video = the moment itself (already set in edit).

---

## Done when

- [ ] Short is public in the 6-11 AM ET window
- [ ] Title has no hashtags
- [ ] Pinned question is up
- [ ] Assets saved under Productions\MetaSports\2026-09-28 LeBron 92 pct pay cut\

**Tue Sep 29:** Batch 2 #2 - The Free Throw Line Lies (same loop).