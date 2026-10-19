# Tools Guide

> ## Oct 19, 2026: official NBA clips without YouTube
> - **New `nba_videos.py`**: searches NBA.com's public content index (what the 30 team sites read) and downloads official clips at 1280x720.
>   - `search --player 201935 --q "step back"` (all team sites), `--team <id>`, `--game 0022401063`, `--grep "block|denies"`, `--max-len 30`.
>   - `get <mp4 url> --out src/x.mp4`.
>   - Per-play team clips include the misses and blocks that highlight packages skip. #48's frame 1 (Robinson denies Harden from three) came from the Knicks site this way.
>   - 720p, so about a 2.7x blow-up in 9:16. On the PC, prefer a 1080p YouTube copy of the same play when there is one.
> - **`overlay.py`** now runs on Linux too (Liberation Sans Bold when Windows Arial isn't there; override with `OVERLAY_FONT`).

> ## Oct 14, 2026 (evening) changes: footage logs, music, matching (each tested on the ready Shorts)
> - **New `footage_lib.py`** (guide: `Library/B-roll Sourcing Guide.md`):
>   - `log <folder>`: creates/refreshes `sources.csv`, one row per clip with the line it sits under.
>   - `match <folder> --src <dirs>`: finds the post and second each clip came from (0.80+ match; 0.70-0.80 "probable").
>   - `sheet <folder>`: contact sheets of the used part of each clip (`_audit/clips/`).
>   - `verify <folder> <clip> "what it shows"`: records that you looked.
>   - `index` / `search <words>`: the library of every clip (`Library/footage_library.csv`).
> - **`x_clip.py`** writes `<out>/downloads.csv` (account, date, post text). **`broll.py cut`** writes the clip's `sources.csv` row.
> - **New `music_gen.py`:** generates a licensed instrumental bed with ElevenLabs Music and logs it in `Library/Music/music_library.csv`. Needs `. key.sh` in the same command. Plan: 17 generated minutes a month, 2 requests at once.
> - **`assemble.py`:**
>   - Reads the folder's `music.json`: `bed_lu` measured against the voice, gap lifts, `drops`, `hit`/`hit_on`, `align_end`.
>   - `--no-music` renders the dry version.
>   - Renders other than `final.mp4` write `_render_<name>.json`.
>   - Music renders limit at -3 dBFS.
> - **`qa_short.py`:**
>   - music licence and level checks, plus the speech-band margin (FAIL under 12 dB)
>   - source-log and verification checks (FAIL once a log exists)
>   - pace guideline 200-265 wpm
>   - FAIL when a "quote" shot was slowed or held by the editor (lips drift from the real audio; found by the critic on #38)
> - **Music tests:** `Library/Music/tests/mix_test.py` (bed level vs the recogniser, phone simulation).
> - **Voice part 2:** `Research Notes/Voice Audition (Oct 14, 2026)/emphasis_test.py` (number emphasis and pauses).

> ## Oct 14, 2026 changes (cloud; each tested on real Shorts)
> - **`qa_short.py`:** rules re-graded by evidence (Rules Audit, Oct 14).
>   - Now warnings, not FAILs: length 15-35 s (the hard limit is 12-60 s), 3 cuts in 3 s, average shot, talking head, b-roll and card shares, two cards in a row, the loop.
>   - New FAIL: dead air inside the speech (a word gap over 0.6 s).
>   - New warnings: the same clip shown twice anywhere (over 0.3 s overlap; the last-shot loop, cards and shots marked `"replay": true` are exempt), a slow hook (first sentence ends after 3.5 s), a naked number opening.
> - **`captions.py`:** no lone word on its own card (e.g. "THE BEST PASS / OF HIS NBA CAREER."). New per-shot option in `shots.json`: `"cap_y": 1305` moves that shot's captions (pixels of 1920; default 1185) off a face.
> - **`voice_check.py`:** ordinals match their digits ("twenty-seventh" = "27th"); no more false REDOs.
> - **Script braces:** `{810|eight hundred and ten}` shows "810" in captions and forces the spoken words.
> - **Voice audition kit:** `Research Notes/Voice Audition (Oct 14, 2026)/audition.py` (same script, many voices, phone simulation, measured). Needs `. key.sh` in the same command.
> - **How a Short is built now:** `MetaSports - Playbook.md`, Creative System v3 (§5 editing playbook and QA lists, §9 per-batch loop).

> ## Oct 13, 2026 changes (cloud; all tested on real Shorts)
> - **`assemble.py`:** no more accidental clip loops.
>   - A shot longer than its clip used to replay the clip. That happened in 22 of 27 folders.
>   - Now a small gap slows the clip (≤1.33x), a big gap holds the last frame and prints a WARNING, and every render writes `_render.json`.
>   - The final mix limiter ceiling is now -2 dBFS.
> - **`qa_short.py`:** new checks.
>   - FAILs: clip replays (old renders), frozen holds over 0.5 s, frozen footage over 0.6 s, black frames.
>   - Warns: true peak above -1 dBTP; a card in the first 4 s.
>   - Spelled-out numbers now count in the hook check.
>   - `--video` variants use the folder's render log.
> - **`voice_fx.py`:** pause trimming now cuts only inside measured silence. It used to cut syllables ("198" came out as "190").
>   - CLI: `python voice_fx.py in.mp3 out.mp3 [words.json]`.
> - **`voice_check.py`:** heights such as 7'5" / "seven-foot-five" no longer raise false REDOs.
> - **New `pointer.py`:** red circle (and optional arrow) on the detail for the frame-1 A/B test.
>   - `python pointer.py final.mp4 final_pointer.mp4 --x 500 --y 640 --r 280 --t0 0 --t1 1.1 [--arrow from-left]`
> - **New `critic_v2.md`:** the independent pre-publication review rubric. It judges the premise first and gives a verdict, not a score.
> - **`rate_short.py`** (the Oct 5 0-100 craft score) predicted views backwards (rho −0.63). Use it only to catch defects, never to order posts.
> - **Voice lineup generator:** `Research Notes/Voice Lineup (Oct 13, 2026)/gen_lineup.py`, for a loudness-matched, same-script comparison.
> - **How a Short is built now:** the per-batch loop in `MetaSports - Playbook.md`, Strict Short Formula §11.

There are two ways to use everything here:
- **Easiest:** type a command in Claude (the Code tab, opened on this folder) and Claude runs the tools for you.
- **By hand:** open the `Tools` folder, click the address bar, type `cmd`, press Enter, then paste a command from below.

## YouTube Analytics API (per-video stats without vidIQ or Metricool; set up once on the PC)
`Tools/yt_analytics.py` reads your channel's per-video numbers with Google's official API. Access is **read-only**: it can't upload, edit or post.
- **Setup, about 10 minutes, once:**
  1. Go to https://console.cloud.google.com, make a new project, and under "APIs & Services → Library" enable **YouTube Analytics API** and **YouTube Data API v3**.
  2. Under "OAuth consent screen", pick **External** and add your own Google account as a **test user**.
  3. Under "Credentials → Create credentials → OAuth client ID", pick **Desktop app**, then **Download JSON**. Save it as `Tools\client_secret.json`. Git ignores it; never commit it or paste it in chat.
  4. Run `python Tools\yt_analytics.py auth`. A browser opens: sign in with the channel's account and allow read-only access. The token is saved outside the project, in `%USERPROFILE%\.metasports\yt_token.json`.
- **Every time:** `python Tools\yt_analytics.py pull --from 2026-09-16`
  - It writes `Research Notes\Studio exports\api <from> to <to>.csv` with, per video: views, average view duration, average % viewed, watch minutes, likes, shares, subscribers gained, length and publish date.
  - Add `--engaged` to also request engaged views; it's skipped if the API refuses.
- **What it can't give:** Studio's "Stayed to watch (%)". Keep exporting the Studio "Content" table for that (Studio → Analytics → Advanced mode → Export → CSV), and drop the file in chat.
- **Status:** written and checked offline in the cloud (Oct 15). It hasn't run against your channel yet, because that needs your one-time sign-in on the PC.

## Newest changes (Oct 15, 2026)
- **`qa_short.py --full` is now the full gate.** It adds the two checks below. Standards and calibration: `Library/Editing and Sound Standards.md` §6.
- **`footage_qc.py` (new):** per shot, using only the seconds each shot uses:
  - blow-up from the source (from `sources.csv`: warn over 2.0x, FAIL over 3.0x)
  - softness vs the Short's own median
  - the same footage under another file name
  - one-frame flashes
  - busy picture and push-ins over 4%/s
  - the source's own internal cuts (check the footage after them)
  - `python Tools/footage_qc.py "<folder>" --json`
- **`export_check.py` (new):** the export against the approved script and timeline:
  - captions = `script.txt` word for word (FAIL otherwise)
  - every word captioned while said
  - caption band and width (at most 820 px, clear of the like/comment column)
  - local speech-to-text of the export vs the script (free, faster-whisper)
  - picture and sound the same length, 1080x1920
  - clipping in the voice and the export
  - `python Tools/export_check.py "<folder>"`; `--no-stt` skips the speech check
- **`captions.py`:** a caption card wider than 820 px now shrinks to fit (it used to reach 867 px).
- **`vendor/watch/` (owner-supplied, Oct 15; MIT):** scene-change frames with timestamps for any video file or URL. It's a fast way to find the right seconds in a long source.
  - `python Tools/vendor/watch/scripts/watch.py "<file or URL>" --engine local --max-frames 40`
  - YouTube URLs work on the PC, not from the cloud.
  - Never with cookies. No Gemini engine without the owner's OK.
  - See `Tools/vendor/watch/README_METASPORTS.md`.
- **`voice_check.py`:** "$8 million" and "won 98" are no longer false REDOs (the recogniser's dollar sign and "one" homophone).
- **`script_lint.py`:** a hook check on line 1 (number-led, list-like, no absolute or curious claim word, too long), from the Studio export finding that stayed-to-watch tracks views.

## Newest changes (Oct 14, 2026, late night)
- **`script_critic.md` (new): Script Critic v3, the strict pre-production gate.**
  - 10 categories; APPROVE needs 36+/45, with premise, hook and payoff each 4+. Accuracy is pass/fail.
  - Every verdict and rewrite goes in `Research Notes/Script Critic Log.md`.
- **`script_lint.py` (new):** objective script risks: length at 225 wpm, first-sentence timing, stacked numbers, jargon, cadence, repeated words, untested names.
  - `python Tools/script_lint.py "<folder>/script.txt"`
- **`deflash.py` (new):** finds and replaces one-frame flashes in a clip; the original is kept.
  - `python Tools/deflash.py clips/x.mp4 clips/x_df.mp4`; `--check` lists them only.
- **`voice_take.py`:** rejects flat takes (pitch-variety gate per voice: `pitch_sd_min` in `voice_config.json`).
- **`qa_short.py`:** no warning for a dry render (no background music is the house default); warns when a bed is baked in.
- **Voice:**
  - The `voice_config.json` default is A (Alex) until the owner picks A or F.
  - `-- --voice backup` makes F (pham v2, fixed).
  - `pham_v3_test` is the new clone: tested, not adopted.

## Newest changes (Oct 14, 2026, night)
- **`voice_config.json` + `pronunciation.json` (new):** one place for the house voice (Alex), the backup (our clone, fixed) and name respellings. `voiceover.py` and `voice_take.py` read them; `voice_take.py`'s quality gate is per voice.
- **`voiceover.py`:**
  - TTS is no longer denoised (it was removing the s/t/f detail).
  - `max_pause` caps silences between words (0.38 s), silence only.
  - New options: `--voice`, `--style`, `--max-pause`, `--no-dictionary`.
- **`assemble.py`:** a gentle compressor on the voice before the lift to -14 LUFS, so a dynamic voice doesn't come out quiet.
- **`retime.py` (new):** after re-voicing the same script, moves `music.json` / `sfx.json` times onto the new words. Usage: `python retime.py --old "<old folder>" --new "<new folder>"`. The old files are kept as `*_oldvoice.json`.
- **A re-voiced build lives in a `_v4/` subfolder** (`clips` symlinked to the parent's), so the posted-ready files are never overwritten.

## Your commands (type them in Claude)

| Type this | What you get |
|---|---|
| `/nba-short` | Here's what it does, step by step: <br>1. Finds last night's hottest NBA moments. You pick one. <br>2. Checks that no big channel already posted it. <br>3. Writes a verified script (22–40s for a story, 15–25s for a quick moment) plus 5 scored titles. <br>4. Saves it ready for the voice. |
| `/nba-short Giannis iguana` | The same, for a moment you already have in mind |
| `/voiceover` | `voice.mp3` + word-timed `captions.srt` for your newest script (`/voiceover 3` = Batch 2 script #3) |
| `/assemble` | **The finished Short, made for you:** <br>• Claude finds the B-roll itself (official NBA, team and news footage). <br>• It cuts each shot as its words are spoken. <br>• It edits the Short in the free Drift editor into `final.mp4`, ready to upload. |
| `/titles` + topic | 10 titles scored against real view data (either channel) |
| `/thumbnail` + text | 3 commentary thumbnails for Test & Compare, or a MetaSports cover |
| `/commentary-script` + topic | 8 titles, 3 thumbnail ideas and a beat sheet with [YOUR STORY] gaps. The first time, it asks your 5 lane questions. |
| `/channel-check` | How MetaSports did lately, in plain English, logged every time |

**A MetaSports Short from start to finish:**
1. `/nba-short`
2. `/voiceover`
3. `/assemble`. Claude finds and cuts the B-roll. To use your own clips instead, put them in the Short's `clips` folder first.
4. Watch `final.mp4`, then upload it between 6 and 11 AM ET.

**Where your work goes:**
- `Productions\MetaSports\<date> <title>\` gets script.txt, notes.md (the shot list), voice.mp3, captions.srt, clips\, final.mp4 and edit.drift.
- `Productions\Commentary\<date> <title>\` gets plan.md and thumb_A/B/C.png.

---

## 1. ElevenLabs setup (2 minutes, once)

1. **Get your key.** On elevenlabs.io, click your profile (bottom left) → **API Keys** → **Create**. Allow **Text to Speech**, **Voices (read)** and **User (read)**, then copy the key.
2. **Make the settings file.** Open **Notepad** and paste these two lines, with your key after the first `=`:
   ```
   ELEVENLABS_API_KEY=paste-your-key-here
   ELEVENLABS_VOICE_ID=
   ```
   Then choose **File → Save as**. Set "Save as type" to **All files**, name it `.env`, and save it inside the `Tools` folder.
3. **Pick the voice.** Type `/voiceover list voices` in Claude, or run `python voiceover.py --list-voices`. Copy the ID of your MetaSports voice after `ELEVENLABS_VOICE_ID=` and save.
   - **Picking by ear:** make the same 2 sentences in 3 candidate voices and keep the one that sounds most like a hype sports narrator at speed.
   - Nobody can see which voice CoachClank uses, so trust your ears.
4. **Never paste the key into a chat.** It stays in that file on your PC.

**Settings (updated Oct 14, 2026, night; nothing to touch):**
- **The voice and every setting live in `Tools/voice_config.json`**, which overrides `ELEVENLABS_VOICE_ID` in `.env`.
  - House voice ("primary"): **Alex** (ElevenLabs Voice Library), eleven_multilingual_v2, speed 1.2, stability 0.5, similarity 0.75. About 220-230 words a minute.
  - No denoise, no stretch. Pauses longer than 0.38 s are shortened (silence only).
  - **Backup:** `-- --voice backup` (our clone, fixed settings).
  - Old renders: `clone_legacy`.
- **Change the voice only in that file**, only after an audition and the owner's ear (`Research Notes/Voice Audition (Oct 14, 2026)/README.md`).
- **Make a take:** `. key.sh && python voice_take.py --script "<folder>/script.txt"`. It tries up to 3 takes against the voice's own quality gate. For exactly one take (a cap, or a test): `--takes 1`.
- **Comparing two voices on the same script:** `py -3 Tools/voice_ab.py "<folder A>" "<folder B>" --labels Alex,pham` (read-only, no credits): real pace, pauses, loudness spread, numbers against other words, and the last word's alignment against its audible length. Run `voice_check.py` on each folder too.
- **On the owner's PC, run the voice tools with `py -3`** (Python 3.14), not plain `python` (3.12). Only 3.14 has `faster-whisper` (the free speech check) and `scipy`, and `praat-parselmouth` (the HNR/jitter/pitch gate) was added to it on Oct 15, 2026 (user site, from PyPI, `--no-deps`). `voiceover.py --check` and `x_clip.py` need only the standard library and work with either. The first whisper run downloads its "small" model (about 460 MB) to `~/.cache/huggingface`.

**Hard names:** add them to `Tools/pronunciation.json` (for example `"Jokic": "Yokitch"`). The voice says the respelling; captions show the name. Don't respell inside scripts. Numbers still work inline: `{92%|ninety-two percent}`. Never respell Wembanyama.

**Cost:** about 1 credit per character. A 25-second Short is about 500 characters per take. `python voiceover.py --check` shows what's left.

**Heads-up:** ElevenLabs' **free plan** requires credit and doesn't allow commercial use. A channel you plan to monetize needs a paid plan.

---

## 2. Thumbnails and covers (free, on your PC)

`/thumbnail` does this for you. If you want to run it by hand, here are the commands:
```
py -3.14 thumb.py --bg "gameplay.png" --text "SPECTATOR\nMODE" --cutout "character.png" --variants 3 --out "thumb.png"
py -3.14 thumb.py --shape short --bg "frame.png" --text "53 YEARS" --out "cover.png"
```
- **Free cutouts:** open the image in **Paint → Remove background**, then save it as PNG.
- **Test & Compare (commentary videos):** in YouTube Studio on a computer, open the video → Thumbnail → **Test & Compare** → upload A, B and C. YouTube keeps the one people watch longest.
- The data behind every title and thumbnail rule is in `Tools\data\title_patterns.md`.

---

## 3. Drift: the free CapCut alternative (installed, and Claude edits in it)

**Drift 0.6.0 is installed** from the official page (github.com/CutWire-Studios/Drift). The download was checked against the official fingerprint.

**Automatic edit: `/assemble`**
- It opens Drift in the background (no window) and lays the voice on the timeline.
- It cuts your clips to a new shot at every sentence. Each shot lasts 1.2–4.5 seconds, which matches CoachClank's biggest Shorts (a new shot every 2–4 seconds).
- It fills the 9:16 screen and adds centered white captions with a soft shadow.
- It exports `final.mp4` at 1080 × 1920 and saves `edit.drift`, so you can open the project and tweak it.
- Tested on Sep 27: a sample Short built and exported in about 6 seconds.

**B-roll: Claude finds it** with `Tools\broll.py`:
1. It searches official channels (NBA, the teams, ESPN, local news). It never uses other creators' Shorts.
2. It looks at a contact sheet of stills to pick clean moments with no burned-in captions.
3. It downloads only the seconds it needs, in up to 1080p. Each clip starts exactly where its camera shot begins.
4. It crops the clip to fill 9:16. A light zoom cuts off tickers and score bugs.
5. It writes `shots.json`, so each shot starts on the exact word. Players appear the moment their names are said.

**Your own clips instead?** Put them in the Short's `clips` folder, named `01`, `02`, `03`… in shot-list order.

**Footage and copyright:** NBA and broadcast clips can get a Content ID claim. The Short usually stays up, but the claimant may share or take the ad money. Under 60 seconds is safest. This is how the whole niche works; the risk is yours to weigh.

**Live editing (optional):** Claude can change the project while you watch it in Drift.
1. Open Drift, go to **Settings → Agent access**, and turn it on. Also switch on **Start agent on startup** so it stays on.
2. Ask Claude something like "make the captions bigger" or "swap shot 3 for shot 5".

If Claude ever says `drift-live` failed to connect, that only means Drift isn't open (or Agent access is off). Nothing is broken.

**By hand:** `python assemble.py --folder "<the Short's folder>"`
- Add `--music "<song.mp3>"` for quiet background music, ducked under the voice.
- Add `--captions hormozi` for bold highlighted captions instead of the clean ones.

---

## 4. Or edit in DaVinci Resolve (free, already installed)

Use this for more control:
1. **Vertical project.** Choose **File → Project Settings → Master Settings**. Set Timeline resolution to 1920 × 1080 HD, tick **Use vertical resolution**, and pick 30 fps. Save.
2. **Import.** Drag `voice.mp3` and your clips into the Media Pool.
   - The voice goes on audio track 1 and the clips on video track 1.
   - Follow the shot list in `notes.md`: one shot per sentence, a new shot every 2–4 seconds.
   - Scale every clip up until it **fills** the vertical frame (Inspector → Zoom). No black bars.
   - Put the moment on screen from the very first frame.
3. **Captions.** Choose **File → Import → Subtitle…** and pick `captions.srt`. Drag it onto the timeline; it arrives already timed to the voice.
   - To style it: click the subtitle track, go to **Inspector → Track**, and choose white, bold, a soft shadow, no box and a medium size, centered in the middle of the screen.
   - That's the CoachClank look: small enough that the footage stays the star.
4. **Music (optional).** Keep it quiet, well under the voice (about −25 dB).
5. **Deliver.**
   - Pick MP4 / H.264 and 1080 × 1920.
   - Under **Subtitle Settings**, tick Export Subtitle and choose **Burn into video**.
   - Click Add to Render Queue → Render All.

**Claude can drive Resolve too.** Open Resolve → **Workspace → Scripts → CursorBridge**, then ask Claude. The first time, test it together with Claude.

---

## 5. Free research tools (Claude runs these inside the commands)

| Tool | What it does |
|---|---|
| `fresh_moments.py` | Finds the hottest new NBA clips from House of Highlights, NBA, Bleacher Report and ClutchPoints, compared with each channel's normal, plus the top headlines. It skips clips that aren't about the NBA and saves to `Tools\data\fresh_moments.md`. |
| `broll.py` | B-roll finder and cutter: `search`, then `sheet` (contact sheet), then `cut` (a clean 1080×1920 clip; `--snap` starts on a camera cut; `--zoom` crops off tickers). `still` turns a picture into a slow-zoom clip. |
| `copy_check.py "topic"` | Tells you FRESH / CROWDED / TAKEN. It runs two searches and only counts videos about the same story. |
| `channel_check.py` | Compares your last 7 Shorts with your normal and flags WINNERs (make a follow-up) and FLOPs (check for a claim or restriction). It shows the days since your last upload and logs everything to `Tools\data\channel_log.csv`. |

**If something breaks:**
- A yt-dlp error means YouTube changed something. Ask Claude to update yt-dlp.
- ElevenLabs error 401 means the key is wrong; make a new one and paste it into `.env`.
- If `assemble.py` says "Missing voice.mp3", make the voiceover first.


## Daily retention, automatically (Oct 19, 2026)
**What you get every morning, without screenshots:** for every upload in the last 30 days:
- views, engaged views, engaged ratio, average % viewed, average view duration, subscribers
- for Shorts under 14 days old, the **retention curve** (100 points)

It flags:
- an engaged ratio under 0.50 (likely under 60% stayed)
- a weak start (under 0.70 still watching at 10% of the runtime)
- a sharp early drop

**What it can't get:** Studio's exact "Stayed to watch". The API doesn't have it. Export Studio → Content → Shorts once a week (30 s) and drop the zip in chat or in `Research Notes/Studio exports/`.

**One-time setup (owner, on the PC, about 10 minutes):**
1. Do the "YouTube Analytics API" steps above (Google Cloud project, the two APIs, the OAuth consent screen with yourself as a test user, a Desktop OAuth client saved as `Tools/client_secret.json`).
2. `python Tools/yt_analytics.py auth`: sign in with the channel's Google account and allow **read-only** access.
3. Check it: `python Tools/yt_analytics.py daily` should print a table of your last 30 days.
4. Pick how it runs every day:
   - **A. From the PC** (simplest): `schtasks /create /sc daily /st 09:00 /tn "MetaSports analytics" /tr "\"C:\path\to\project\Tools\daily_analytics.bat\""`. The PC must be on at 09:00. It pushes the CSVs to git, and the cloud routine reads them.
   - **B. From the cloud** (works with the PC off):
     - open the cloud environment's settings (the environment menu in the session title bar → Edit)
     - add three secrets: `YT_CLIENT_ID` and `YT_CLIENT_SECRET` (from `Tools/client_secret.json`), and `YT_REFRESH_TOKEN` (from `%USERPROFILE%\.metasports\yt_token.json`, the `refresh_token` field)
     - **never paste them into chat or commit them**
     - a new cloud session picks them up, and the daily routine then runs `yt_analytics.py daily` itself
5. Test the parser offline any time: `python Tools/test_yt_analytics.py` (fixture data, not real numbers).
