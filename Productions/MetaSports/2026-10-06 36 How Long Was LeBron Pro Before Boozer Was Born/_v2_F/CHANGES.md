# #36 v2: rewritten script, voice F (pham v2, fixed settings), no music (Oct 14, 2026, night)

**Status:** candidate. The v1 files in the parent folder are unchanged. **Twin:** `_v2/` is the same edit in voice A (Alex).
- **Still needs the owner's OK:** the rookie-LeBron shots (l2bg at 0-1.6 s, k2bg_df at 5.5-7.7 s) come from an unofficial fan account (NBACobwebs), as in v1.

## Why
The v1 script scored 32/45 (REWRITE) under Script Critic v3:
- it used the known viral "played before he was born" template
- our own angle, Carlos Boozer, was buried at 75%
- it dumped dates

The rewrite scored 38/45 (APPROVE). See `Research Notes/Script Critic Log.md`, C2.

## What changed
**Script:** opens with "LeBron's teammate from his rookie year now has a son in the NBA" and ends with "Two generations of Boozers. One LeBron."

**Footage:**
- The same v1 clips, remapped to the new lines.
- Added: d4 (Cameron at Duke), b2 (Summer League), e1bg (LeBron in the 2007 playoffs).
- 4 clips cleaned of one-frame washed-out flashes with the new `Tools/deflash.py` (a1, c_34, e1bg, k2bg). The originals are kept.
- First `sources.csv` for this Short (`_v2/sources.csv`): every clip described from a frame-by-frame look, with post-level sources from notes.md.

**Sound:** no music, no effects.

**Voice:** Alex, 21.6 s (`_v2_F`: pham v2 fixed, 20.7 s).

## Checks (done)
- `qa_short.py`: PASS (-14.3 LUFS; F -14.4).
- **Flash scan:** clean.
- **Frames:** 1 s sheet checked.
- **Transcripts:** every line heard right. "Boozer" comes back as "Buzer", which is how it's said.
