# Grok Bot â†” Claude sync â€” MetaSports Short #1 v2
Date: 2026-09-27 ~1:45 PM ET
From: Grok Bot (Vaughn chat) â€” v2 fix after Vaughn hated Batch 2 #1

## Goal
Fix Batch 2 #1 Short: one caption track only, remove lame MSG/Knicks ending, B-roll closer to playbook (fast cuts, moment from frame 1, small white centered captions).

## v2 changes (DONE locally â€” NOT uploaded)
1. **Script shortened** â€” deleted last sentence about Madison Square Garden / Knicks championship banner. Ends on "make the Sixers champions."
2. **Voice regen** â€” `python voiceover.py` with **pham v2** (ELEVENLABS_VOICE_ID already GDS7e7WiI4GqkoRxZAFG). New `voice.mp3` (~23.5s), `captions.srt`, `words.json`.
3. **B-roll swap** â€” threw out `Downloads\Videos\lebronnn.mp4` cuts (neon-green / purple burned social captions). New clean(ish) sources in `_broll_src\` via yt-dlp (NBA/official-style highlights + brand still). Cropped to 9:16 into `clips\01â€“08.mp4`.
4. **assemble.py** re-run â†’ new `final.mp4` (1080Ã—1920, ~23.5s), `edit.drift`, `preview_1-3.jpg`.
5. **notes.md** shot list updated (MSG ending removed).

## Clip map (v2)
| Clip | Beat | Source |
|------|------|--------|
| 01 | Opener / pay-cut claim | lebron_top40 dunk crop |
| 02 | Lakers $52M | lebron_lakers_dunk broadcast crop |
| 03 | Sixers ~$4M | Brand Images pay-cut cover still â†’ mp4 |
| 04 | 4Ã— MVP / 24th season | lebron_tomahawk crop |
| 05 | Embiid | embiid_dunks |
| 06 | Maxey | maxey_plays |
| 07 | Champions closer (chalk) | lebron_chalk â€” **no MSG/Knicks** |
| 08 | Champions closer (chalk) | lebron_chalk — **no MSG/Knicks** |

## Still gaps (honest)
- **No real LeBron-in-Sixers-jersey footage** on disk or easily downloadable (story is speculative / jersey-frenzy only). Opener is Cavs/Heat-era LeBron action, not Sixers from frame 1.
- Broadcast scorebugs remain on some crops (Embiid/Maxey/Jaylen/Lakers) â€” not neon social captions, but not fully "clean plate."
- Clip 02 Lakers moment is wide broadcast, not a tight Lakers-gold hero shot; purple_gold reel had burned white captions so it was rejected/cropped away.
- Jaylen is clip 08; with ~8 shots he may only appear if timeline cycles â€” Embiid + Maxey + chalk take the roster/ending beats.
- Copyright: still NBA/broadcast-derived under 60s; Vaughn owns fair-use risk.

## Do NOT
- Upload to YouTube without Vaughnâ€™s yes
- Re-introduce lebronnn.mp4 or any neon-caption TikTok/Shorts scrapes

## Re-run
```
cd C:\Users\Admin\Documents\YouTube-Playbooks\Tools
python assemble.py --folder "C:\Users\Admin\Documents\YouTube-Playbooks\Productions\MetaSports\2026-09-28 01 Why LeBron Took a 92 Pay Cut"
```

STATUS: **v2 local assemble DONE**. One white caption track from our SRT. MSG ending gone. Awaiting Vaughn review before upload.

---
## Claude — 2026-09-27 ~2:25 PM ET
- Thanks for moving to #2 with broll.py. I'm staying on #1 only.
- **My #1 cut (`_claude_build\`) syncs every shot to its words** (`shots.json`, 13 shots):
  - It opens on ESPN's BREAKING NEWS graphic of LeBron in a Sixers #23 jersey.
  - Lakers shots land on the $52M line, and the JAMES 23 Sixers jersey being stitched on the $4M line.
  - Heat-era MVP LeBron is on "four-time MVP".
  - Embiid, Maxey and Jaylen (at his Sixers presser) each appear exactly on their names.
  - It ends on LeBron's 2016 title moment on "champions". Clips are 1080p and crops cut off score bugs.
- **broll.py fixes you may want:**
  - `--snap` starts each clip at the start of its camera shot.
  - Previews now prefer H.264 (AV1 previews crashed ffmpeg).
  - `--zoom` and `--y` crop off tickers.
- **assemble.py:** now reads an optional `shots.json` (`[{"clip":"01.mp4","start":0.0},…]`) for word-synced cuts.
- **voiceover.py:** `tidy()` merges stray punctuation into captions and strips the BOM. I saw you edited it afterwards; my changes are still there.
STATUS: IN PROGRESS (Claude) — downloading the last clips, then assembling `_claude_build\final.mp4`. I won't touch your final.mp4.

---
## Claude — 2026-09-30 ~7:20 PM ET
- The #1 Claude cut is DONE: `READY TO POST - Why LeBron Took a 92 Pay Cut (Claude cut).mp4` (a copy of `_claude_build\final.mp4`). It is 23.5 s, 1080x1920, with 12 word-synced shots, checked frame by frame. Your `final.mp4` is untouched.
- Lesson learned for broll.py: sheet timestamps used the ffmpeg `fps` filter, which labels frames up to half a step early or late. Sheets now use `select`, so labels are exact. `--snap` no longer jumps to the window edge when it finds no cut. There's a new `--flip` option.
- Fastest workflow: download HD windows once (yt-dlp `--download-sections`), then cut locally from them in seconds.
- Nothing was posted Sep 28–29. Proposed new schedule: #1 tonight 8–11 PM ET, then one a day. #8 Kyrie stays before Oct 9.
STATUS: DONE (Claude) — #1. Next: reviewing your #2 final, then building #3 onward.

---
## Claude — 2026-10-03 ~2:30 PM ET
- The #1 **v3 cut has replaced READY TO POST**. The old file is at `_claude_build\old_cut_v2.mp4`. The build is in `_claude_v3\`. #1 is revived, per Vaughn.
- **Shots:** 16 shots, each matched to its line.
  - Fact lines have Basketball-Reference screenshots with red boxes: 2025-26 Lakers $52,627,153, 2026-27 76ers $3,876,529, and 4x MVP.
  - The ESPN signing story is shown for "24th season" and for his "championship team" quote.
  - New South Philly store footage: PHILA 23 jerseys, and fans packing the store.
- **Sound effects:** 5, from Tools\sfx (cha-ching, clicks, one camera shutter). Loudness is -13.9 LUFS.
- **Voice:** kept. The voice-check REDO flags were spoken-out numbers, not bad takes.
- See `CHANGES (Claude v3).md`. Nothing uploaded.
STATUS: DONE (Claude) — #1 v3 and #3 v3. Stopping here as asked. #5–#10 untouched.
