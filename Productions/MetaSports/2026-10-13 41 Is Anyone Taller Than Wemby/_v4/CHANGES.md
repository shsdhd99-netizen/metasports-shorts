# #41 v4: new house voice (Oct 14, 2026, night)

**Status:** candidate. It replaces nothing (the v3 files in the parent folder are unchanged). Waiting on the owner's ear.
- **Before posting either version:** re-check Sharp's status (PACKAGE.md).

## What changed vs v3 (one variable: the voice)
- **Voice:** Alex, house settings (`Tools/voice_config.json`). 227 wpm, 23.3 s of speech (v3: 22.9 s).
- **Wembanyama:** plain spelling. The script's `{Wembanyama|wem-bun-YAH-muh}` was removed (the audition heard the respelling as "Wembun Yama"). The recogniser hears "Wimbanyama" (close).
- **Shots:** re-anchored to the new words. No footage changes were needed.
- **Music and effects:** retimed through the words (`Tools/retime.py`).
  - The bed's own decay is placed on "zero." (hit_on 22.67).
  - The whoosh is at 5.35 s, the boom at 22.64 s.

## Checks (done)
- `qa_short.py`: **PASS**. 23.6 s, -14.6 LUFS, peak -2.5 dBFS.
- **Frames:** a 1 s sheet and a flash scan are clean.
- **Transcript:** every line heard right.
- **Music:** the isolated bed holds -31 to -37 dBFS through "zero." (22.5-23.0 s), then falls to -54 at 23.1 s and -71 at 23.5 s, so the decay comes in as the answer word ends.
