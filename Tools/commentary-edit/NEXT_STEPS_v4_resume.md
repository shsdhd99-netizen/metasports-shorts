# v4 status (2026-09-30 ~23:58) - resume point

Stopped by Claude Code's low-memory guard (16 GB RAM: the verified join search and the draft video render were running at the same time,
alongside the desktop apps). Do NOT run two heavy jobs together. Resume one step at a time, in this order:

1. (optional, ~5 min, GPU+RAM) re-verify the 7 parked cuts: remove their `skip` entries from edl/overrides_v4.json (keys are in edl/skips_pending.json),
   `python edl/build_v4.py`, then
   `python tools/join_search.py "keys:426-428,1434-1436,1624-1626,1752-1754,1986-1990,1797-1803,1908-1913"`.
   Anything that still does not read cleanly is marked skip again (the original speech stays in; a tiny stutter beats a bad splice).
   Skipping this step is safe: the build below works with the 7 left as skips (35 verified cuts applied).
2. `python edl/build_v4.py`            -> audio/voice_v4_pregain.wav, edl/edl_v4.json, edl/final_words_v4.json, edl/cutlist_v4.txt
3. `python tools/render_voice.py audio/voice_v4_pregain.wav audio/voice_v4.wav`   (draft check: -14.0 LUFS stereo-equivalent, TP -2.0 dBTP, LRA 3.2)
4. `python tools/render_video.py audio/voice_v4.wav build/final_v4.mp4 build/video_plan.json`   (ffmpeg only; ~5 min)
5. AFTER the render finished (not during): `python tools/asr_check.py audio/voice_v4.wav qa/asr_v4_final.json` (pieces; GPU) then
   `python tools/qa_asr_diff.py qa/asr_v4_final.json` ; and `python tools/qa_final.py build/final_v4.mp4 audio/voice_v4.wav edl/edl_v4.json qa/v4`
6. `python tools/write_kit.py C:\Users\Admin\Downloads\commentary_edit\v4` (needs qa/v4/qa_final.json), copy final_v4.mp4 there,
   `powershell -File <scratchpad>\stage_upload.ps1` (Explorer + Brave side by side, Studio upload box open on carnage).
7. User drags final_v4.mp4 onto Studio; Claude then fills title/description/thumbnail/settings (private), asks before publishing.

Nothing has been uploaded or published. final_v3.mp4 and all older files are untouched.
