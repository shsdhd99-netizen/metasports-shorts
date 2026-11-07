# #21 v5: rewritten script, voice F (pham v2, fixed settings), no music (Oct 14, 2026, night)

**Status:** candidate. Nothing in the parent folder or in `_v4/` was changed. **Twin:** `_v5/` is the same edit in voice A (Alex). The owner picks the voice.

## Why
The v3.1 script failed Script Critic v3 (30/45, REWRITE):
- it opened on a number, not a person
- it was an 11-sentence fact chain, averaging 5.5 words a sentence

The rewrite scored 39/45 (APPROVE). See `Research Notes/Script Critic Log.md`, C1.

## What changed
**Script:**
- Opens on two stars and a deadline: "Russell Westbrook needed eighteen seasons… Nikola Jokic could take it before Christmas."
- Down to 6 voiced numbers, one per sentence.
- New payoff: last Christmas's 56-16-15 (NBA: the first 55-15-15 game ever), then "This Christmas, the record could already be his."

**Footage** (every new clip logged in `sources.csv` and checked by eye):
- `xmasface` (ESPN post, Jokic on Christmas 2025)
- `xmasgame2` (the Christmas game, NBA Christmas scorebug)
- `c_xmas56`: our proof card over the real game
- `b7M`: the Houston post, re-cut to skip a one-frame flash in b7L
- `b6j` and `b2` on split lines

**Sound:** no background music (new house rule) and no effects.

**Voice:** pham v2 at speed 1.1, stability 0.5, no denoise (`voice_config.json` "backup"). 25.8 s, the first take passed. One shot re-anchored ("five hundred fewer") so nothing freezes.

## Checks (done)
- `qa_short.py`: PASS, -14.4 LUFS.
- **Frames:** 1 s sheet checked (`_audit/sheet_1s.jpg`).
- **Flash scan:** clean, after the re-cuts.
- **Transcript of the final audio:** every line heard right.
