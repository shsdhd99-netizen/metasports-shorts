# Commentary edit pipeline (faceless voice-over on muted gameplay)

Built for the carnage channel (long-form commentary). Same steps for every future video; only the raw recording,
the removal list and the gameplay plan change. Everything heavy lives on D:\OBS\ClaudeWork\<video>\ (C: is small).

## Inputs
- voice: the raw recording(s), one continuous monologue (here 1.mkv + 2.mkv).
- gameplay: one long muted-able recording (here `C:\Users\Admin\Videos\2026-09-26 00-19-08.mkv`).
- `build/video_plan.json`: which gameplay seconds to use, in order (last entry `null` = fill to the voice length).

## Steps (what was run for "time isnt promised", v4)
1. **Source audio**: decode both files to one 48 kHz float mono wav (`src/src_48k.wav`); keep a 16 kHz copy for ASR only.
   Never run the voice chain on the 16 kHz copy (that was the "this isn't crisp" bug).
2. **Words + timing**: CrisperWhisper verbatim (keeps um/uh/false starts) + wav2vec2 forced alignment -> `asr/work/fa_LV60K.json`.
3. **Studio voice chain on the whole source before cutting** (`audio/render_v3_voice.py` PRE): highpass 70, EQ -3 dB@350 +2.5@2k
   +1.5@3.5k, deesser, -2 dB@8k, 4:1 + 2.5:1 compression, +19 dB, limiter .66, lowpass 18.5k. -> `audio/enh_full_v2chain.wav`.
4. **Read the indexed transcript** (`edl/review.txt`) and list every removal in `edl/build_v4.py` as `rm(first, last, "expected words", reason)`:
   um/uh, stutters, false starts, restarts, abandoned sentences, off-topic asides. The builder asserts the words match, so an index typo can't cut the wrong thing.
5. **Build** `python edl/build_v4.py`: cut points sit in real silence / dips, 10 ms crossfades, pauses > ~0.9 s shortened, waveform-aligned splices
   in voiced speech. Writes `audio/voice_v4_pregain.wav`, `edl/edl_v4.json`, `edl/final_words_v4.json`, `edl/cutlist_v4.txt`.
6. **ASR-verified join search** `python tools/join_search.py auto` (GPU): for cuts that are not in real silence, tries the deepest dips around the
   intended boundary, transcribes each spliced snippet verbatim and keeps the variant that reads exactly as intended. Writes `edl/overrides_v4.json`
   (build_v4.py picks it up; `skip` = keep the original speech when no clean cut exists). Re-run step 5 afterwards.
7. **Loudness** `python tools/render_voice.py audio/voice_v4_pregain.wav audio/voice_v4.wav`: dual-mono delivery at -14.0 LUFS integrated
   (YouTube's reference level; it never boosts quieter files), true peak <= -1.6 dBTP.
8. **Video** `python tools/render_video.py audio/voice_v4.wav <out>/final_v4.mp4 build/video_plan.json`: muted gameplay, 1080p60, h264_nvenc, AAC 320k.
9. **QA** `python tools/qa_final.py <mp4> audio/voice_v4.wav edl/edl_v4.json <qa dir>` (loudness of the real file, decode errors, black/freeze,
   click score at every cut vs random positions, frame sheet) and `python tools/asr_check.py audio/voice_v4.wav qa/asr_final.json` then
   `python tools/qa_asr_diff.py qa/asr_final.json` (leftover fillers / fragments, mismatches next to cuts). Fix and re-render until clean.
10. **Kit**: `python tools/make_kit.py edl/final_words_v4.json` gives image-spot and optional chapter timestamps for the final cut.

## Gotchas learned the hard way
- GPU (RTX 3060, 12 GB) is shared with the desktop: a single 12-minute CrisperWhisper call filled VRAM and never finished. `asr_check.py` uses 150 s pieces.
- RAM is 16 GB and shared with browsers etc.: never run the ASR / join search and the ffmpeg video render at the same time (Claude Code's low-memory guard killed both
  once, at 2026-09-30 23:56). One heavy job at a time; killed jobs must only be restarted when the user asks.
- Run long jobs with the Bash tool's `run_in_background` (a plain `nohup ... &` dies when the tool call ends), and give them a timeout.
- ffmpeg mono->stereo upmix loses 3 dB per channel; the mux uses `pan=stereo|c0=c0|c1=c0`. Dual-mono stereo = mono + 3.01 LU.
- CTC forced-alignment times of short fragments (wh-, s-, I) can be 0.3 s off; never trust them for cut points without the dip search + ASR check.
- Upload: the Chrome extension cannot attach multi-GB files (10 MB cap); the user drags the mp4 onto Studio, then Claude fills title/description/thumbnail/settings.
  Long-form -> carnage channel; Shorts -> MetaSports. Upload as private, ask before publishing.
