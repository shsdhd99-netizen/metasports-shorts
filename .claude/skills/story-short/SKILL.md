---
name: story-short
description: >
  Make a 60-80 s story Short in the format of Ahmed's Goal / Ahmed's Basketball / Ahmeds Business (the network with 1.3B views):
  the title read aloud as line 1, "Back in [year], [famous name]...", a turn every 8-12 s, a hard-number or ironic payoff, and nothing
  after it (no teaser, no follow ask). A new picture every 1.1-2.1 s (real footage, stock for abstract lines), centred TikTok Sans
  captions and a quiet music bed. Built for the soccer channel (MetaSports FC) but niche-agnostic (NBA, business). Covers research
  with sources, script, ElevenLabs voice, footage (archive.org, Mixkit, screenshots), cut list, render, QA and the upload package.
  Use when the user types /story-short, asks for a soccer/football Short, a "story Short", or "a Short like Ahmed's".
  Argument: a topic, an Idea Bank number (S03...), or a number of Shorts to make.
---

# /story-short: the story format, start to finish

The owner is non-technical and often on a phone, so keep chat short and plain.

**Standing rules (owner's, never relax them):**
- Never publish, schedule or replace a public video, and never open YouTube Studio. Every output is a DRAFT awaiting approval; the owner posts.
- Never print, commit or ask for API keys. Load ElevenLabs from the environment or a key file inside the same bash command.
- Never invent a stat. Every number gets a source and its exact wording in notes.md. Keep qualifiers ("reportedly", "is said to").
- Copy what works: "do not try new things, stick with what works". Copy Ahmed's shape, never his wording or his specific stories.

Read first (they win over this file when newer):
- `Soccer Channel/START HERE.md`, `Soccer Channel/Lessons Learned.md` and `Soccer Channel/Idea Bank.md`.
- The format spec in this folder: `FORMAT.md` (with evidence tiers).
- `SCRIPT.md` (template and two worked examples), `SOURCING.md` (where pictures come from, licences) and `QA.md` (the gates).
- Moving to another Claude account: `PORTABLE.md`.

## The 9 steps (about 60-90 min a Short in the cloud)

### 1. Pick the story (10 min)
- **What wins:** a GLOBAL star, plus a small human or absurd detail, plus a twist, plus an ironic or emotional payoff with a hard number.
- **Themes by Goal median:**
  - refused / defiant: 826K
  - records and oddities: 332K
  - comeback / revenge: 311K
  - underdog: 293K
- **What flops:** obscure names and process stories.
- **Lanes, rotated (Oct 24, `Research Notes/What Makes Our Shorts Go Viral (Oct 24, 2026).md`):** the secret object (S01);
  **versus their own** (refused, betrayed, sued, rejected by their own club, country, sponsor or teammates: Ahmed's strongest
  title signal, 1.63x, n=87); a **numbered serial about one global star** ("Part 1, 2, 3...": FOOTY FACTS' Zlatan serial median
  1.4M vs 162K for one-offs); a **topical question** answered with a story ("Why did X just...?": 59% of Ahmed's Aug-Oct titles,
  as strong as his evergreen ones). At most 1 post in 3 per lane.
- **Before choosing:**
  - copy-check with `python Tools/copy_check.py "<4-6 words>"`;
  - grep Ahmed's titles: `Research Notes/Ahmed Network Data (Oct 21, 2026)/AhmedsGoal_shorts.csv`.
- **The footage test:** do not start a story unless real footage of the named person exists. Check archive.org first (SOURCING.md).

### 2. Research with sources (15 min)
- Read the sources themselves:
  - `curl -sL -A "Mozilla/5.0" <url>`;
  - the Parallel `web_fetch` / `web_search` tools;
  - X posts: `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`.
- Build a claims table, one line each: claim, source, exact quote.
- **Dates:** check every one against the source's own timeline, e.g. "the night before" vs "the day before" (S02 lesson).
- **When sources disagree** on who did what: word the line so it is true under both, and note it.

### 3. Script (10 min) -> `<folder>/script.txt`
- 260-290 words. After step 4b that runs about 60-68 s (S01: 253 words = 59.5 s; S02: 280 words = 63 s).
- Beats are in SCRIPT.md:
  1. title as line 1;
  2. "Back in..." (optional: Ahmed now opens with it in 1 of 30 October scripts; get into the story at once);
  3. turn 1 by about 15 s;
  4. 2-4 escalations ("But it got even crazier");
  5. climax;
  6. "But here's the wild part" plus the payoff number or irony. **The payoff is the last line.**
- **No promo at the end (owner, Oct 22):** no "my next video is about...", no "follow", no teaser. The owner: "that will instantly
  kill retention". Viewers swipe the moment the story is over, so the video ends on the payoff.
- **Pronunciation:** spell scores and numbers for the voice: `{6-1|six-one}`, `{1-1|one-one}`.
- **Never** end on a question.
- **The hook (Oct 24, why S02/S03 flopped: `Research Notes/Why S02 and S03 Underperformed (Oct 24, 2026).md`):**
  - line 1 says the stakes, specifically: an object you can picture or a strong human verb (hid, refused, sued, betrayed,
    rejected). A category word needs a sharp qualifier ("...for the silliest reasons"). Strongest on Ahmed's Goal: a player or club
    turning on its own side ("their own": 2.28x; conflict words 1.63x, n=87). Strong verbs 1.35x (n=107);
  - say the promised thing again by about 20 s and keep the story on it (S01: 18 s, 80% stayed; S03: 54 s, 65%);
  - one story, no more than about 10 names in the first 15 s (S03 had 11);
  - write the object and its synonyms into cuts.json as `"promise": ["sheet", "paper", "note", "sock"]` so QA can check it.
- **Title card:** write `<folder>/title_caption.txt`, the title on 1-2 lines (`\N`) with 1-2 CAPS words, e.g. `Goalkeepers who hid a\NCHEAT SHEET in their sock`.

### 4. Voice (5 min, background)
- Run `. <key file> && python Tools/voice_take.py --script "<folder>/script.txt" --takes 3` with nohup in the background.
- It records, checks and re-records.
- **Gate:** no REDO words, HNR, jitter and shimmer within limits.
- The first take often drops "Back" after the title. Take 2 usually passes.
- **Repair, don't re-record (Oct 24):** a failed take with 1-2 located word issues is fixed by `Tools/retake_sentence.py`
  (~5-10% of a full take's credits): voice_take.py now does it by itself before paying for a new take. By hand:
  `python Tools/retake_sentence.py --folder F --at <issue time>` (or `--sentence N`), then `voice_check.py --stt whisper`.
- Output: voice.mp3, words.json, captions.srt. If the length is under 58 s, add a verified beat and re-voice.

### 4b. Take out the dead air (owner, Oct 22: "make sure videos have no unnecessary pauses")
- `python Tools/tighten_voice.py --folder F` cuts every silence over 0.09 s down to 0.06 s (measured on the audio, not on the
  word timings, which swallow pauses) and trims the tail to 0.25 s after the last sound.
- `--end-after "word."` also cuts everything after that word (how the old S01 teaser was removed).
- It rewrites voice.mp3, words.json and captions.srt; originals go to `_voice_pretighten/`. Shot times come from words.json,
  so run it BEFORE the cut list. If you run it after, re-run `cut_list.py` and move the sfx.json times with the words.
- Check: `ffmpeg -i F/voice.mp3 -af silencedetect=n=-38dB:d=0.07 -f null -` shows no silence over 0.1 s except the 0.25 s tail.

### 5. Footage (20-30 min)
Sources (details in SOURCING.md):
- archive.org: full TV broadcasts and highlights;
- the 2006 World Cup "all goals" item;
- Mixkit stock: `python Tools/stock.py search <word> --sheet s.jpg`, then `stock.py get <id>`;
- web screenshots: `node Tools/webshot.mjs --url ... --out x.png`;
- Wikimedia photos: use the `thumb.wikimedia.org` host; the API is rate-limited from the cloud.

How to work:
- **Map moments:** `python Tools/broll.py sheet <file> --from A --to B --every 1 --out s.jpg`. LOOK at the sheets and write down the second ranges.
- **TV channel logos:** re-encode the used section once, with the borders cropped and the logo blurred (`delogo`), as `src/clean.mp4`. Or use `broll.py cut --delogo x,y,w,h`.
- **Uploader watermarks:** crop them out (`--zoom 1.3 --y 0.15`). A blur over a name strip looks worse.
- **Famous objects we have no photo of** (the note): make a recreation graphic labelled "recreation" on the picture (example: `assets/make_note.py`).
- **No cards (owner, Oct 26: "cut cards completely, theyre a big distraction. if added, keep brief").** Show the fact on footage: the broadcast's own graphics, words over the play, a red circle. A card only when nothing else can carry the proof, 1.5 s at most (QA fails a longer one) and never in the first 4 s. (S01, 80% stayed, had 6 cards; the rule is the owner's call, not a soccer finding.)
- **Cards and graphics** (when one is unavoidable) stay ABOVE y=890, so the centred captions (y=960) never sit on light paper. Make them as full 9:16 JPGs and use them as `still` shots.

### 6. Cut list -> `<folder>/cuts.json`, then `python Tools/cut_list.py --folder "<folder>"`
- One shot per phrase, 40-50 shots a minute. Each shot gets an `anchor` (the first words of its phrase), a `kind` and a `why`.
- **First shot:** holds about 2 s under the title card. It must SHOW the promise happening: the object or the act in the
  title (S01: the hand going into the sock). A face only when the title is about the face. Sharp and lit from the very first
  frame: no fade, wipe or someone passing the camera (S04's first 0.25 s was dark; QA now fails that), no channel logo, no scan lines.
- **Name a person, show the person.** Abstract lines get literal stock (a clock for "1 a.m.", euros for "one million euros").
- **Framing:**
  - wide shots: `"blurfit": true`;
  - faces and action: a full-frame crop with an `x` position.
- **Check the work:** the tool cuts everything, pins shots to words, warns on short clips, fills sources.csv and draws `_check/sheet.jpg`. LOOK at the sheet. Check framing, that the named person is on screen, and that no logo or burned-in text shows.
- **Verify:** fix, re-run, then run `--verified` once you have looked at every tile.

### 7. Sound, then render
- **`sfx.json`:** 3-5 effects from `Tools/sfx/catalog.json`, only where the picture shows the sound. Each one is a different file, none before 1.0 s, at least 1.5 s apart.
- **`music.json`:** `{"track": "Library/Music/eleven_story_01.mp3", "start": 0.0, "bed_lu": -20, "gap_lift": 2, "fade_out": 1.0}`. This is the Ahmed-style bed, about 20 dB under the voice.
- **Render both versions:**
  - `python Tools/assemble.py --folder F --caption-style ahmed --no-music --out-name final_nomusic.mp4`
  - `python Tools/assemble.py --folder F --caption-style ahmed --out-name final_music.mp4`

### 8. QA (must PASS) -> `python Tools/qa_short.py --folder F --video F/final_music.mp4 --full`
- Folders under `Soccer Channel/` use the story profile automatically: length 58-88 s, the title card may hold, archive blow-up up to 6x as a warning.
- Then look at frames at 0.5, 2.4, 8, 18, 22, 39, 47, 58 and 64 s, side by side. Check the title card, the captions on every card, and the payoff picture.

### 9. Package and hand off
- **`notes.md`:** lane, concept in 8 words, added value, copy-check, and a table of every line with its source and exact quote. Then the footage list (licence, what each clip is), and illustrative-shot warnings.
- **`UPLOAD.md`:** title (= line 1; plural or singular makes no difference on Ahmed's data once the era is accounted for);
  no description; 3 alternative titles; post order (one soccer Short a day); which version.
- **The draft files:** copy both renders as `DRAFT - awaiting approval - S<NN> <title> (music).mp4` and `(no music).mp4`.
- **Update** `Soccer Channel/START HERE.md`, `Lessons Learned.md` and `Idea Bank.md`.
- **Commit and push** (media is git-ignored except the DRAFT files). Report to the owner in 5-8 short lines. Never post.
