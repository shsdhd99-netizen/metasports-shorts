# QA gates for the story format

Run `python Tools/qa_short.py --folder F --video F/final_music.mp4 --full`. It must print PASS.

**The story profile** (automatic for folders under `Soccer Channel/`, or `--profile story`):
- **Length:**
  - FAIL outside 55-120 s;
  - warn outside 58-88 s.
- **First 3 s:** warn if more than 3 shots, because the title card should hold.
- **No loop rule:** the format ends on the payoff or the teaser.
- **Footage blow-up:**
  - up to 3x is fine;
  - 3-6x is a warning (archive footage, no HD copy exists);
  - over 6x FAILS.
  - Blur-fit shots are measured on their full-width foreground.

**Hard gates (both profiles):**
- every shot has a kind;
- the voice starts at once;
- action footage in the first 3 s;
- no shot over 3.6 s;
- 6+ source clips;
- no footage shown twice;
- no dead air inside the speech;
- -14 LUFS;
- no frozen or black frames;
- every clip has a sources.csv row and is marked verified (after you looked at `_check/sheet.jpg`);
- the captions match script.txt word for word.

**The look (do it every time; QA cannot see these):**
1. Frames at 0.5, 2.4, 8, 18, 22, 39, 47, 58 and 64 s side by side:
   - the title card is readable;
   - no caption sits on light paper;
   - the payoff picture lands.
2. `_check/sheet.jpg`:
   - the named person is on screen for every name;
   - no channel logo, watermark or other creator's captions;
   - nothing cropped off (half a face, half a graphic). If a graphic is cut, use blurfit.
3. Read `sources.csv`: every "illustrative" shot is marked as such in notes.md.

**Before handing off:**
- notes.md lists every claim with its source and exact quote;
- UPLOAD.md is written;
- both DRAFT files exist.
