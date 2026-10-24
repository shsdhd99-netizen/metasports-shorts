# #21 v4: new house voice and the footage it needed (Oct 14, 2026, night)

**Status:** candidate. It replaces nothing (v3.1 in the parent folder is unchanged). Waiting on the owner's ear.
- **Before posting either version:** post before Denver's first game (the 198 changes).

## What changed vs v3.1
**1. Voice:** Alex, house settings.
- 23.0 s instead of the old voice's rushed 16.8 s.
- `{Jokic|Yoki-ch}` was removed; the dictionary says "Yokitch".
- The number respellings ({1,301|…}, {810|…}) are kept.
- The voice gate passes under Alex's own limits (shimmer 11.6 ≤ 12.5; see `voice_config.json`).

**2. Footage** (forced by the 6 s longer read; every new clip comes from a post already in the log, re-downloaded with `x_clip.py` into `_v4/src/`, not in git):
- `a1L` = tribute post 0.2-2.8 s (OKC, Wizards, Rockets): replaces a1 under "Westbrook needed 1,301 games".
- `b7L` = Houston post 1.9-4.2 s: one continuous angle (b7 crossed the post's internal cut).
- `b12L` = media-day post 4.6-7.1 s: one continuous walk.
- **Line 1 split:**
  - `b1cj` (b1c trimmed to 0-1.6 s, before its one-frame flash) runs through "Nikola Jokic has 198".
  - `b6j` (b6 trimmed to 0-1.17 s, before the pan to a coach): Jokic #15 under "triple-doubles".
- **"About one every two"** now sits on `b8`: Jokic's own lower third, "JOKIC 32 PTS".
- All new clips are in `_v4/sources.csv`, marked verified after a frame-by-frame look.

**3. Mix:** a voice compressor before the loudness lift. Without it this render came out at -15.6 LUFS, a QA fail.

## Checks (done)
- `qa_short.py`: **PASS**.
  - 23.0 s, -14.9 LUFS, peak -2.7 dBFS
  - no frozen footage
  - no footage shown twice (apart from the deliberate loop shot)
  - every clip logged and verified
- **Frames:** a 1 s sheet is checked. The flash scan's two flagged frames at 2.27 s were a camera pan inside b6, which is why b6 was trimmed.
- **Transcript:** every line heard right.
- **Music:** the isolated bed breaks at 21.0-21.2 s (-45 dBFS), then the re-entry hit lands at 21.4 s (-29.5 dBFS) on "Four games to spare."
