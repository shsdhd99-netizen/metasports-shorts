# Pipeline review, Oct 31 2026 (review only, no code changed)

Read: both START HERE files, the three skills, and the code of assemble, qa_short, footage_qc, deflash, voice_take, tighten_voice, cut_list, anchor_shots, fill_len, nat_sound, comfort_audit, broll (grep), yt_watch (skim). Line numbers are as of this morning's working tree. Value = time saved or quality gain per effort. Items are ranked.

## Ranked list

### 1. Render the picture once, finish twice (music + no-music) - assemble.py 418-483, 590-609
- Problem: each version re-cuts every shot (libx264 crf16 per shot), re-concats, then re-burns captions. Only the audio differs (captions are identical). On the PC the Drift path (534-609) also re-exports the whole timeline per version. Doing the two versions one after the other (required by the lock) costs 2x.
- Fix: `--both` flag (or `--out-name` list). After the shot cut + concat, write `final_nocap.mp4` once, then call `finish()` twice (music=None, then music_plan) with the second call reusing it. Cheaper variant with no new flag: at the top of ffmpeg_engine/Drift export, hash (shots.json, voice.mp3 mtime/size, every used clip mtime/size, zoom/auto-zoom args) into `_nocap.hash`; if equal and `final_nocap.mp4` exists, skip straight to `finish()`. Store `fits` in the hash file so `_render_*.json` still gets written (line 480). Line 477-478 already leaves `final_nocap.mp4` behind, so the cache file exists.
- Gain: about 45-50 % of render time for every soccer Short and every NBA music/no-music pair. Risk: low (stale cache if a clip is edited in place; the hash covers mtime and size).

### 2. Cut the shots in parallel inside one render - assemble.py 424-463
- Problem: the per-shot ffmpeg calls run one by one (40-50 shots for a story Short). They are independent and write to distinct `s###.mp4` in this render's own `RUN_TMP`, so the new lock is not involved.
- Fix: wrap the loop body in a `concurrent.futures.ThreadPoolExecutor(max_workers=min(4, os.cpu_count()))`, return `(k, out, fits_entry)` and sort by k before writing the list. Print the notes after the join so the log stays ordered.
- Gain: 2-3x on the cutting phase. Risk: low. Do not parallelise across versions (that is what the lock prevents); item 1 removes the need.

### 3. The PC renders through Drift, which silently ignores things the ffmpeg engine honours - assemble.py 530-533, 542-558
- Problem: the Drift path never reads `zooms`, so shots.json `"zoom"` (push-in, replays) and `--auto-zoom` are dropped on the PC. It has no 30-fps frame snapping (the #60 0.11 s drift bug), the clip-too-short loop (line 545-558 repeats the clip, the exact visible jump-back fixed on Oct 13 for ffmpeg), no slow/hold handling, and writes no `_render.json`, so qa_short loses its quote-lip-sync and frozen-hold checks (qa 229-239). Hundreds of RPC calls per render are also slow. Cloud and PC therefore produce different pictures from the same folder.
- Fix: make the ffmpeg engine the default everywhere (`if not os.path.exists(DRIFT) or os.environ.get("ASSEMBLE_ENGINE", "ffmpeg") == "ffmpeg":` at line 530); keep Drift behind `--engine drift` for when the owner wants `edit.drift` to tweak by hand. Both engines then give the same file.
- Gain: parity (what QA checks is what is rendered), plus speed. Risk: low-medium: confirm one render matches an earlier Drift render before switching the default.

### 4. Clean edit for the story-profile hand-off - qa_short.py 332, footage_qc.py 91-98
- Problem: qa_short computes `story` (line 49, honours `--profile` and the folder name) but calls `footage_qc.check(F)` with no profile; footage_qc re-derives it by scanning `sys.argv` (91-98), which breaks when qa_short is imported, run from a script that passes other arguments, or run with `--profile=story`.
- Exact edit:
  - qa_short.py line 332: `_, fb, fw = footage_qc.check(F, "story" if story else "nba", fin)`
  - footage_qc.py: `def check(folder, profile=None, video=None):` and `segs = segments(folder, video)`.
  - footage_qc.py `segments(folder, video=None)`: use `fin = video or os.path.join(folder, "final.mp4")`.
  - Delete the `sys.argv` lines (95-98) in `story_profile`; add `--profile` to footage_qc's own `main()` with `argparse` (`folder`, `--profile`, `--json`).
- Side bug fixed by the same edit: `segments()` measures the last shot against `final.mp4`. Soccer folders only have `final_music.mp4` / `final_nomusic.mp4`, so the last shot falls back to 2.0 s (line 82) and its sharpness, motion and flash windows are the wrong length.
- Risk: none. Gain: correct profile and last-shot duration every time.

### 5. footage_qc: three decodes plus a re-encode per shot, and a fps bug - footage_qc.py 110, 118, 125, 177-188
- Problem: per shot it decodes 4 fps at full 1080x1920 (110), then 30 fps at 96x170 (118), then re-encodes the shot to a temp file at crf12 and decodes that again for `flashes()` (177-188). Also `flashes_in` assumes 30 fps (`i / fps`, line 183) but the temp file keeps the source frame rate: 25/60 fps sources give wrong flash times and a resampled 30-fps stream can hide a one-frame flash. The same QA runs for both versions with the same clips and gives the same answer.
- Fix:
  - Split `deflash.flashes(path)` into `flash_idx(fr, ratio, floor)` that takes the decoded array, and have footage_qc pass the `small` array it already has (no temp file). Decode `small` with `fps=30` consistently so the time is `i/30`.
  - Do the Laplacian on a half-size frame (`frames(..., 4, 540, 960)`); sharpness is only compared with the Short's own median (line 142), so absolute scale does not matter.
  - Cache the result in `_audit/footage_qc.json` keyed by (shots.json, used clip mtimes); the second version's QA loads it.
- Gain: footage_qc roughly 3x faster, and flashes get correct times. Risk: low.

### 6. Flashes: frame 0 / last frame are never tested, and the finished video is never tested - deflash.py 29, qa_short.py ~190
- Problem: `for i in range(1, len(fr) - 1)` skips the first and last frame. Lessons (Oct 14: "a3's first frame") show the flash is often the first frame of a cut clip, and footage_qc starts at `max(0, t_in-0.05)` which is 0 for already-cut clips, so frame 0 is never judged. The frame 1 of the final video is what decides swipe/stay. Nothing tests the finished export for a 1-frame shot or flash at a join (rounding, held frames, Drift).
- Fix:
  - deflash.py: test index 0 with only its forward neighbours (`a=|f1-f0|`, `c=|f2-f1|`; flag when `a>floor and a>ratio*max(c,1)`), mirror for the last index; in the writer, for a flagged frame 0 use the next frame (read-ahead of one frame).
  - qa_short.py after the black-frame check: `from deflash import flashes; fl = flashes(fin); chk(not fl, "no one-frame flashes in the export", f"one-frame flash in the export at {[round(i/30,2) for i in fl]} s")`. It is one 96x170 gray decode (about 1 s).
- Gain: catches the most common "looks glitchy on phone" defect before the owner sees it. Risk: low; run it on three old finals first to check the false-positive rate (captions popping are small area, but a fast whip pan could trigger; start as a warn).

### 7. One command for the post-script chain - voice_take.py, tighten_voice.py, fill_len.py, cut_list.py, anchor_shots.py
- Problem: the recipe is voice_take -> tighten_voice -> fill_len -> cut_list -> anchor_shots -> assemble x2 -> qa x2 -> yt_watch, each with its own folder argument and exit-code check. Specifics:
  - `cut_list.py` line 88 already runs `anchor_shots.py`, so the recipe's separate anchor_shots step (START HERE section 9, story-short step 6) repeats it.
  - `tighten_voice.py` re-decodes the voice with silencedetect twice (the second at line 98 for the tail) and `voice_take.py` loads the Whisper model in a new subprocess for every take.
  - Nothing stops you running cut_list after a voice change but before tighten (stale `start` values).
- Fix: new `Tools/build_short.py --folder F [--from voice|tighten|cuts|render|qa] [--profile story|nba]`: runs the stages in order as subprocesses, stops on the first non-zero exit, skips a stage if its output is newer than its input (voice.mp3 -> words.json -> cuts.json -> shots.json -> final), refuses to run `cut_list` if `voice.mp3` is newer than `shots.json`, and writes one `_build.log`. Include the voice credit guard (`voiceover.py --check` arithmetic from START HERE section 6) so a build cannot spend past the rule. Final stage: QA on both versions, then Gemini precheck.
- Gain: removes about 6 hand-typed commands and the stale-timing class of mistake; about 5-10 min of agent turns per Short. Risk: low (thin wrapper, no change to the tools).

### 8. Windows: default encoding and /tmp - assemble.py 465, fill_len.py 38, qa_short.py 50-51, export_check.py 189
- Problem:
  - `open(...)` without `encoding=` uses cp1252 on this PC. `assemble.py:465` writes the concat list in cp1252 while ffmpeg reads UTF-8, and the list holds the folder path: a folder with "é"/"ć" (Pelé, Jokić, Mbappé) breaks the render (wrong path, or `UnicodeEncodeError` for "ć"). `fill_len.py:38` writes with `ensure_ascii=False` and no encoding: crash on a non-cp1252 name. `qa_short.py:50-51` reads shots.json/words.json with the default encoding, so "Pelé" is read as mojibake while cut_list wrote UTF-8; the name/number regexes then disagree.
  - `export_check.py:189` writes the STT wav to `/tmp`, which on Windows resolves to `C:\tmp`. That folder does not exist, so speech-to-text silently fails inside `try`, and the export-vs-script check is skipped on the PC.
- Fix:
  - Zero-code, do first: `setx PYTHONUTF8 1` (and add `set PYTHONUTF8=1` to `daily_analytics.bat`). Every `open()` then defaults to UTF-8.
  - Code: assemble.py 465 write relative names (`file 's000.mp4'`) with `encoding="utf-8"` (list sits in the same folder as the parts); fill_len.py 38 and qa_short.py 50-51 add `encoding="utf-8-sig"`; export_check.py 189 `wav = os.path.join(tempfile.gettempdir(), ...)` (or `RUN_TMP`).
- Gain: stops a whole class of PC-only failures. Risk: none.
- Cloud vs PC differences to remember: Drift only on the PC (item 3); `h264_nvenc` only on the PC with automatic x264 fallback (assemble 392, captions 349, fine); `broll.py:19` uses `C:/Windows/Fonts/arialbd.ttf`, which does not exist on Linux, so cloud text overlays rely on a fallback: use `Tools/fonts/` as assemble does for Montserrat.

### 9. QA gaps found in Lessons Learned that no check catches
Loudness/peak:
- `nat_sound.py:112` limits at 0.89 (-1 dBFS) and then AAC re-encodes; the Oct 29 S18 case peaked at +1.6 dBTP after a direct edit. assemble limits at 0.794 / 0.708 for exactly this reason. Fix: `limit=0.794`. Also `nat_sound` writes no `_render_<out>.json`, so qa on `final_live.mp4` falls back to the base render's log or none; copy `_render_<base>.json` to `_render_<out>.json`.
- qa_short true peak is a warn (line 178). A final over -1 dBTP is audible clipping on phones: make it a FAIL above -0.5 and keep the warn between -1 and -0.5.
- comfort_audit.py (loud-jump, quiet-hole, fast-cut, freeze) is not part of `--full`; the Oct 29 limiter lesson only works if someone remembers to run it. Fix: in `qa_short.py --full`, `import comfort_audit` and add the `startles()` and `holes()` findings as warns, reusing the `ebur128` output already parsed at line 171-176 (it currently ebur128-decodes the file three times: qa 171, comfort 25, export_check).
- Loudness is measured on the voice only before the music/sfx mix (assemble 362-366): a loud bed can still land the final off -14; QA catches it, but after the render. Cheap fix: after `finish()`, run `lufs(final)` and if outside +-0.7 re-run once with `lift` corrected by the difference (assemble 366), so QA no longer fails for something the renderer could fix.
Edit quality (all warns first):
- Shot 1 hold and shots in first 3 s are checked from shots.json starts, not from what the video shows; export a shot-change check from `comfort_audit.shots()` against `shots.json` to catch anchor/lead errors (a cut landing on the wrong frame).
- Face in frame: the crop `x` is hand-set; no check that a named person's face is in the 9:16 window (Z23 needed `x: 0.76`). Cheap helper: run OpenCV's Haar/DNN face detector on the `_check/sheet.jpg` tiles for `kind: face` shots and warn if none is found (cv2 is already used in footage_qc).
- Music ducking is a static 20 LU bed with gap lifts from `words.json` timings (assemble 308-323). TTS word times drift from the audio (tail lesson, Soccer Lessons line 35), so lifts can land on speech. Fix when this next causes a complaint: key the duck off the voice with `sidechaincompress` instead; not needed now.

### 10. Parallel QA and Gemini (safe ones) - qa_short.py, yt_watch.py
- Problem: QA of version A, QA of version B and the Gemini precheck run one after the other. `export_check` STT (faster-whisper small.en) runs on both versions although the voice is identical.
- Fix: after item 1, run `qa_short.py` for both versions in two processes (different `--video`, no shared writes; footage_qc cache from item 5 makes the second a read) and start `yt_watch.py <chosen DRAFT> --precheck` in the background as soon as the render exists; wait for it after QA. Run STT only on the music version (the one where music can hide words) via a `--skip-stt` flag on the other.
- Gain: about a minute or two per Short. Risk: low (CPU contention only).

## Do not do
- Do not run two `assemble.py` renders in the same folder in parallel (the lock queues them anyway) and do not parallelise voice takes (shared credit pool).
- Do not turn comfort_audit's caption-speed line into a gate (it flags nearly every 2-3 word caption, per the Oct 30 lesson).

## Suggested order of work
1. `setx PYTHONUTF8 1` and the three small encoding/`/tmp` edits (item 8): minutes.
2. Item 4 edit (profile hand-off, last-shot duration): minutes.
3. Item 9 nat_sound limiter and `_render` log copy: minutes.
4. Items 1 and 2 (render once, parallel cuts): about an hour, biggest time saving.
5. Items 5 and 6 (footage_qc speed, flash coverage).
6. Item 3 (engine default), then item 7 (`build_short.py`).

## Log.md summary (3 lines)
Pipeline review (no code changed): top wins are rendering the picture once for the music and no-music versions, cutting shots in parallel, and making the ffmpeg engine the PC default (Drift ignores zoom, loops short clips and writes no _render.json).
QA edits to make: pass the story profile and the video into footage_qc.check (qa_short.py 332), test flash frame 0 and the finished export, add limiter/true-peak and comfort_audit warns, and fix PC-only breakage (cp1252 concat list, /tmp in export_check.py:189; set PYTHONUTF8=1).
Full ranked list with line numbers: Research Notes/Account 2/Pipeline Review 2026-10-31.md.
