# #40 v4: new house voice (Oct 14, 2026, night)

**Status:** candidate. It replaces nothing: the old-voice versions in the parent folder stay valid and unchanged. Waiting on the owner's ear (Sound Check page, section 3; Hub, top version).

## What changed vs the ready version (one variable: the voice)
- **Voice:** Alex (ElevenLabs Voice Library, `yl2ZDV1MzN4HbQJbMihG`), eleven_multilingual_v2, speed 1.2, stability .5, similarity .75. No denoise, no stretch, pauses capped at 0.38 s (`Tools/voice_config.json`, profile "primary").
- **Pace:** 220 wpm over 23.5 s. The old voice was about 259 wpm over 20.6 s.
- **Jokic:** the script's `{Jokic|Yoki-ch}` was removed. The dictionary now says "Yokitch" (`Tools/pronunciation.json`). The recogniser hears "Yokic"; with "Yoki-ch" it heard "Yokeech".
- **Shots:**
  - All re-anchored to the new words (`anchor_shots.py`).
  - Two in-points moved so the slower read doesn't freeze footage:
    - K_wide `in` 0.4 → 0.0
    - R_close (the "No look" replay) `in` 0.95 → 0.5
- **Music and effects:** times moved onto the new words (`Tools/retime.py`; the old files are kept as `*_oldvoice.json`).
  - The swish was set by hand to R_shot's start + 1.30 s (9.57 s).
- **Mix:** a gentle voice compressor before the loudness lift (`assemble.py`, Oct 14).

## Checks (done)
- `qa_short.py`: **PASS**.
  - 23.9 s, -14.7 LUFS, peak -2.6 dBFS
  - no frozen footage
  - every clip logged and verified
  - speech band 41 dB clear of the music
- **Frames:** a 1 s sheet (`_audit/sheet_1s.jpg`) and a lone-frame flash scan both came back clean.
- **Transcript of the final audio** (whisper): every line heard right ("Yokic" for Jokic).
- **Music placement**, by isolating the music (render minus dry render):
  - the drop before "It isn't." at 14.81 s: -44.7 → -74.5 dBFS
  - the stop before "Not eighty-one.": the bed is out by 22.96 s
- **Ring twin** (`final_pointer.mp4`): the same ring as v2 (460,790 r190, 0-1.5 s). Frames checked: around the ball and hands at 0.4 s.

## Test edit T2 (not for posting): `_test_bed12/`
- The same render with the music bed at -12 LU (closer to CoachClank) instead of -20.
- QA PASS (warns: bed outside the house range); speech band 33 dB.
- A phone-speaker simulation heard every word at both levels.
- On the Sound Check page, section 4.

## Files
- `final.mp4` (plain + music) and `final_pointer.mp4` (ring + music)
- `final_dry.mp4` (no music, for the placement check)
- Hub copies are uploaded.
