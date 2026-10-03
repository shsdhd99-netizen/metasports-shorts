"""Writes the user-facing kit for a finished cut into the deliverable folder:
UPLOAD_KIT.txt, TITLE_AND_DESCRIPTION.txt, EDIT_NOTES_v4.txt, CUTLIST_v4.txt  (numbers come from the edl + qa json, never typed by hand)
usage: python write_kit.py <deliverable_dir>"""
import sys, os, json, shutil
sys.path.insert(0, "D:/OBS/ClaudeWork/commentary_v3/tools")
from make_kit import build, mmss
W = "D:/OBS/ClaudeWork/commentary_v3"
out = sys.argv[1]
edl = json.load(open(W + "/edl/edl_v4.json"))
qa = json.load(open(W + "/qa/v4/qa_final.json"))
spots, chap = build(W + "/edl/final_words_v4.json")
ov = json.load(open(W + "/edl/overrides_v4.json")) if os.path.exists(W + "/edl/overrides_v4.json") else {}
n_cuts = len(edl["joins"]); removed = sum(j["b"] - j["a"] for j in edl["joins"]); total = edl["total_seconds"]
skipped = sum(1 for v in ov.values() if v.get("skip"))
L = qa["loudness"]; cl = qa["clicks"]
dur = mmss(total)

kit = f"""UPLOAD KIT - v4 (final_v4.mp4, {dur})
==========================================================================================
Drag final_v4.mp4 onto the YouTube Studio upload box (carnage channel). Claude fills in everything below
(private first, you publish). Thumbnails are in this folder.

1) TEST & COMPARE (title + thumbnail, 3 options - put option A first; if the test is inconclusive YouTube keeps option 1)
   A (favourite)  title: you can't be proud of a fake life
                  thumbnail: thumb_A_was_it_worth_it.jpg   (defeated Belfort, "WAS IT WORTH IT?")
   B              title: i realized time isn't promised
                  thumbnail: thumb_B_it_goes_fast.jpg      (stressed Belfort, "IT GOES FAST")
   C              title: nobody's living for themselves
                  thumbnail: thumb_C_stop_performing.jpg   (no face, "STOP PERFORMING")
   - v4 has no cold open: the story just runs from "So when I was younger...". The promise in the title is paid off by the
     "if you die tomorrow" section at {next((c[0] for c in chap if 'died' in c[1]), '0:50')}.
   - Don't change the title or thumbnail during the test (it stops the test). It can take up to 2 weeks; "inconclusive" is normal.
   - C has no movie still: keep it as the fallback if a still ever gets a takedown.
   - No profanity in titles/thumbnails on purpose.

2) DESCRIPTION - see TITLE_AND_DESCRIPTION.txt

3) PINNED COMMENT (post it yourself right after publishing, then pin it)
   if you died tomorrow, would you actually be proud of what you're doing right now? be honest

4) SETTINGS
   - Made for kids: No.   Altered or synthetic content: No (nothing here is AI).
   - Tags: valorant, valorant commentary, commentary, storytime.
   - Chapters: none, and untick "Allow automatic chapters" (one continuous story).
   - Ad suitability: answer honestly - frequent profanity in the video only (none in title/thumbnail); the vaping part is cautionary.
     Wait for Checks to finish before publishing.
   - End screen: 1 video + subscribe over the last ~15-20 s.
   - Publish once Checks clear; early evening ET is a fine default. Don't delete and re-upload.

5) OPTIONAL IMAGE SPOTS (exact times on final_v4.mp4; the video ships clean without them)
""" + "\n".join(f"   {t}  \"{p}\" -> {w}" for t, p, w, _ in spots) + """

6) AFTER PUBLISHING
   - First 24 h: check the monetization icon is green, reply to early comments, leave the test alone.
"""
open(out + "/UPLOAD_KIT.txt", "w", encoding="utf-8").write(kit)

desc = open("C:/Users/Admin/Downloads/commentary_edit/v3/TITLE_AND_DESCRIPTION.txt", encoding="utf-8").read()
head = desc[:desc.index("OPTIONAL CHAPTERS")]
rest = desc[desc.index("PINNED COMMENT"):]
chapters = "OPTIONAL CHAPTERS (times recomputed for v4; skip them and untick \"Allow automatic chapters\" if you prefer)\n" + \
           "------------------------------------------------------------------------------------------\n" + \
           "\n".join(f"{t} {n}" for t, n in chap) + \
           "\n\n------------------------------------------------------------------------------------------\n"
open(out + "/TITLE_AND_DESCRIPTION.txt", "w", encoding="utf-8").write(head + chapters + rest)

notes = f"""EDIT NOTES - v4 (final_v4.mp4) - built 2026-09-30
==========================================================================================
{dur} | 1920x1080 60 fps H.264 | AAC 320k stereo | voice only, gameplay muted | no captions, no music, no effects.

WHAT CHANGED VS v3 (your feedback)
- No cold open. The video starts on the gameplay and your first word ("So when I was younger...") and the story just runs.
- Background footage kept, same match and order as before, starting on the live round.
- All vocal errors and the major slip-ups cut: every um/uh, stutter, false start and restart, the abandoned sentences, and two tangents
  (the "uploaded on that channel" aside and the "I got way off topic / yapping for five minutes" aside, plus the "separate video / uploading"
  tangent and one failed sentence). {n_cuts} cuts in total, {removed:.0f} s removed (raw 13:10 -> {dur}). Full list with the exact words: CUTLIST_v4.txt.
- Cuts: placed only in real gaps or dips and checked by transcribing the spliced audio again (an ASR pass that keeps um/uh), blended with
  pitch-aligned 10 ms crossfades. {skipped} removal(s) skipped where no clean cut existed (a tiny stutter left in beats a bad splice).
- Dead air over ~0.9 s shortened to a natural 0.35-0.45 s breath.

SOUND
- Same studio chain you approved (EQ, de-esser, 2-stage compression, limiter) applied to the full 48 kHz recording BEFORE cutting.
- Loudness of the actual file: {L['integrated_LUFS']:.1f} LUFS integrated (YouTube's reference is -14, so it plays at the level you hear here),
  true peak {L['true_peak_dBTP']:.1f} dBTP, loudness range {L['LRA']:.1f} LU (very even: no loud/quiet jumps, so no volume riding on TV or headphones).
  Short-term loudness 5th / 50th / 95th percentile / max: {L.get('short_term_LUFS_p5_p50_p95_max')}.
- Dual-mono stereo (same signal both ears): comfortable on headphones, no phase issues on TV soundbars.

CHECKS RUN ON THE FINISHED FILE
- decode errors: {len(qa['decode_errors'])}; black frames: {len(qa['black'])}; frozen video: {len(qa['freeze'])}; audio clipping: {qa['voice_clipped_samples']} samples.
- click check at all {cl['cuts']} cuts vs random positions in the voice: {len(cl['cuts_above_threshold'])} above the 99.5th-percentile threshold.
- full re-transcription of the finished audio (um/uh/false starts kept visible): see qa_asr summary in the final report.

NOT DONE / YOUR CALL
- Images: not inserted (optional; exact spots + times are in UPLOAD_KIT.txt section 5).
- Thumbnails use Wolf of Wall Street stills (your call); thumbnail C has none, as a fallback.

Working files (not needed to upload): D:\\OBS\\ClaudeWork\\commentary_v3 (edit list, scripts, QA). Pipeline notes: tools\\README.md there.
"""
open(out + "/EDIT_NOTES_v4.txt", "w", encoding="utf-8").write(notes)
shutil.copy(W + "/edl/cutlist_v4.txt", out + "/CUTLIST_v4.txt")
print("kit written to", out)
