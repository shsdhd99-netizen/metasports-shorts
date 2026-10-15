# #21 v5: rewritten script, voice A (Alex), no music (Oct 14, 2026, night)

**Status:** candidate. Nothing in the parent folder or in `_v4/` was changed. **Twin:** `_v5_F/` is the same edit in voice F (our old voice, fixed). The owner picks the voice.

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

**Voice:** Alex, house settings. 24.7 s, 3 takes; the first went flat and the second misread "one ninety-eight".

## Checks (done)
- `qa_short.py`: PASS, -14.4 LUFS.
- **Frames:** 1 s sheet checked (`_audit/sheet_1s.jpg`).
- **Flash scan:** clean, after the re-cuts.
- **Transcript of the final audio:** every line heard right.

## QA re-run with the new checks (Oct 15, 2026): PASS, with to-dos
`qa_short.py --full` (footage_qc + export_check):
- **Hook:** fails the new hook anchor (Script Critic Log §E). The surprise is sentence 2, at about 4.8 s. **Fix: v6 with a one-sentence opening.**
- **Shot 2 (a1L):** from a 640x640 post (the NBA's tribute), so it's blown up 3.0x. Below the 1080p standard; replace it in v6.
- **Captions:** "TWENTY-SEVENTH GAME" ran about 867 px wide (over the 820 px safe width). Future renders auto-fit.
- **Soft:** a2 (shot 1, Westbrook applauding) and b4c.
- **Busy:** b1cj and a3 (a dunk montage with its own cuts; it stays on Westbrook).
- **Export speech vs script:** 98% match. The differences are speech-to-text mishearing "Nikola" and "twenty-seventh". Captions match the script word for word.
