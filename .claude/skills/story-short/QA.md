# QA gates for the story format

Run `python Tools/qa_short.py --folder F --video F/final_music.mp4 --full`. It must print PASS.

**The story profile** (automatic for folders under `Soccer Channel/`, or `--profile story`):
- **Length (Oct 26 overnight review):**
  - FAIL outside 50-59.9 s (what `qa_short.py` checks);
  - warn over 59.5 s (YouTube shows it as 1:00). Aim for about 230-250 words. Too long? Cut a sentence; never add one.
- **First 3 s:** warn if more than 3 shots, because the title card should hold. Our own target is stricter (Oct 26 overnight review): shot 1 at least 2.0 s, at most 2 shots in the first 3 s.
- **No loop rule:** the format ends on the payoff. Nothing after it (no teaser or follow ask), and no forced loop.
- **Footage blow-up:**
  - up to 3x is fine;
  - 3-6x is a warning (archive footage, no HD copy exists);
  - over 6x FAILS.
  - Blur-fit shots are measured on their foreground.
- **Framing (Oct 26 overnight review; QA cannot see it, so look):** wide plays at 3:4 (`"blurfit_aspect": 0.75`), never a full-width 16:9 strip over blur; full width only for a graphic to read whole.

**Hard gates (both profiles):**
- every shot has a kind;
- the voice starts at once;
- action footage in the first 3 s;
- no shot over 3.6 s;
- no footage shown twice, except a shot marked `"replay": true` (Oct 26: `cut_list.py` passes it through);
- no dead air inside the speech;
- -14 LUFS;
- no frozen or black frames;
- every clip has a sources.csv row and is marked verified (after you looked at `_check/sheet.jpg`);
- the captions match script.txt word for word.

**Footage first replaces "6+ source clips" (Oct 26 overnight review) [S]:** secure frame 1 and a proof clip for each beat, from any
number of sources. Never add a filler shot to reach a clip count. If `qa_short.py` still FAILs a soccer Short on "only N source clips"
or "one clip fills over 35%", that gate is out of date: write it in the Daily Log and flag it for the session that owns `Tools/`,
rather than padding the cut.

**The look (do it every time; QA cannot see these):**
1. Frames at 0.5, 2.4, 8, 18, 22, 39, 47, 55 and 58 s side by side:
   - the title card is readable;
   - no caption sits on light paper;
   - the payoff picture lands;
   - frame 1 shows the promise happening, and there are no emoji stickers.
2. `_check/sheet.jpg`:
   - the named person is on screen for every name;
   - no channel logo, watermark or other creator's captions;
   - nothing cropped off (half a face, half a graphic). If a graphic is cut, use blurfit.
3. Read `sources.csv`: every "illustrative" shot is marked as such in notes.md.

**Before handing off:**
- notes.md lists every claim with its source and exact quote;
- UPLOAD.md is written (title = line 1, empty description, 0-1 hashtag, 3-8 tags or none, which version);
- both DRAFT files exist.
