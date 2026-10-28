# Soccer channel playbook (Oct 21, 2026; rules updated in the Oct 26 overnight review)

**How to make a Short:** the step-by-step lives in the skill, `.claude/skills/story-short/SKILL.md`, so one copy stays current. The format itself, with evidence, is in `.claude/skills/story-short/FORMAT.md`.

**Oct 26 overnight review:** the owner asked for a full review ("everything is up for debate"). Changed rules say so, with an evidence tier ([V] measured, [S] small sample or seen on other channels, [H] a guess) and a source. The shared rules are THE RULES at the top of `MetaSports - Playbook.md` (those marked "FC too"). Every change: `Research Notes/Rule Changes Applied (Oct 26, 2026).md`.

## Channel rules (on top of the skill)
1. **Copy what works.** Ahmed's Goal shape: title as line 1, "Back in...", a turn every 8-12 s, a payoff number as the last line; a new picture every 1.1-2.1 s; centred TikTok Sans captions. Change nothing else until our own numbers say so (`Outcome Log.md`).
   - **Length (Oct 26 overnight review):** under 60 s; the Short must end before 59.5 s after tightening. Aim for about 230-250 words. If it runs long, cut a sentence; never add one. [V official] a Short over 1 minute with a claim can be blocked; `qa_short.py` FAILs 60 s or more. Source: `Research Notes/Rules Review (Oct 26, 2026).md` §2 item 5.
   - **Music (Oct 26 overnight review):** a quiet bed vs none is an open A/B test. Render both (rule 6). [H] No data yet: nobody logged which version was posted.
   - **Real audio (owner, Oct 28):** when the key moment has a live English call on usable footage, also render a real-audio version (NBA Playbook THE RULES §2 rule 11, `Tools/nat_sound.py`): the narration pauses and the call plays. S17 Krul: "...and Krul has saved it!". Keep the commentary bed low (`--bed-db -26`) so two English voices never compete. S07 Loch Ness is left out of the music test: which version went up is unknown.
2. **Global names only.** Messi, Ronaldo, Beckham, Zidane, Balotelli, Lehmann at a World Cup... Obscure names flop on Ahmed's channel (27-41K vs 276K median).
3. **One story per Short**, even though the title sounds like a list. When a title works, reuse it as a series with a new story ("Goalkeepers who..." is our first series).
4. **Every number sourced** in notes.md with its exact wording. Keep qualifiers. When sources disagree, write the line so it is true under both.
5. **Real footage of the named person** on screen when the name is spoken. Stock is only for abstract lines. A recreation is labelled "recreation" on the picture.
6. **Two renders per Short:** with the music bed (Ahmed's way) and without. The owner picks until the numbers decide. Log which one was posted in the Hub card and `Outcome Log.md`, or the A/B can't be read.
7. **Cadence (owner, Oct 28):** one Short a day at 8-9 AM ET, 1 hour after the NBA post (a 2nd, when as strong, about 4 PM). [S] `Research Notes/Posting Study (Oct 26, 2026).md`. Ahmed runs 2 a day; his medians fell at 3.
8. **Never post.** Drafts only; the owner uploads.
9. **No promo at the end** (owner, Oct 22: "that will instantly kill retention"). No "my next video", no "follow". The video stops on the payoff.
10. **No dead air** (owner, Oct 22). Run `Tools/tighten_voice.py` on every voice before the cut list.
11. **No cards** (owner, Oct 26). If one is unavoidable: 1.5 s at most, never in the first 4 s. The proof goes on the footage.
12. **Editing (Oct 26 overnight review; THE RULES §2 in `MetaSports - Playbook.md`, "FC too"):**
    - **Footage first:** before writing, secure frame 1 and one clip that proves each beat, from any number of sources. Never add filler to reach a clip count. [S]
    - **Frame 1 shows the promise happening** (the object or the act in the title). The spoken title is 11 words or fewer. [V] NBA data
    - **Shot 1 holds at least 2.0 s** under the title card; at most 2 shots in the first 3 s. [V] NBA data; our 3 posted Shorts all had 2.
    - **Replay the key moment once before the payoff** when the footage has it (closer and/or 0.5x, `"replay": true`). [S]
    - **Fill the frame:** wide plays cropped to about 3:4 over the blur (`"blurfit_aspect": 0.75`); full-width blur-fit only for a graphic to read whole. [S]
    - **No emoji stickers. No forced loop.** [S]
    - The soccer shot rate (a new picture every 1.1-2.1 s) stays Ahmed's way; the NBA "10-15 shots" rule doesn't apply to a 60 s story.
13. **Posting and the package (Oct 26 overnight review) [V/S] `Research Notes/Posting Study (Oct 26, 2026).md`:**
    - Title = the spoken line 1, a short statement. Title wording is a small factor: no title scoring.
    - No hashtag or one (#football). Description empty.
    - Tags optional: 3-8 relevant tags, about 100-150 characters (names, club, event, common misspellings). Never fill the 500 characters.
    - Judge a Short at 72 hours (S03 had 1.4K views at 10 h and 14.5K by day 3). Never re-upload a Short.
14. **Research tools (Oct 26 overnight review):** `Research Notes/Competitor Watchlist.csv` (the channels we watch, soccer included) and `Tools/yt_watch.py` (Gemini watches a Short; needs a free `GEMINI_API_KEY` in the environment settings).
15. **TikTok and Instagram cross-posting is paused** (owner, Oct 26: YouTube first).

## Differences from the NBA channel (on purpose)
| | NBA (MetaSports) | Soccer (this channel) |
|---|---|---|
| Length | 20-45 s, by lane | Under 60 s, ending before 59.5 s; about 230-250 words (Oct 26 overnight review) |
| Lanes | Moments about half; star paradox (THE #42 FORMAT), same-day news and a weekly countdown rotate (Oct 26) | One story per Short; lanes in the skill, at most 1 in 3 each |
| Opening | Frame 1 = what line 1 is about; line 1 of 11 words or fewer; shot 1 at least 2 s; at most 2 shots in 3 s and 3 in 5 s (Oct 26) | Title read aloud; first picture holds at least 2 s under a title card |
| Captions | House style (white Montserrat caps) | `--caption-style ahmed` (TikTok Sans, white, centred, 2-3 words) |
| Music | None by default (owner, Oct 14) | Bed vs none: an open A/B test; render both (Oct 26) |
| Ending | Payoff, then stop. No forced loop (Oct 26) | Payoff is the last line. No teaser or follow ask (owner, Oct 22) |
| Slot | 7-8 AM ET (Oct 28) | 8-9 AM ET, 1 hour after NBA (Oct 28) |
| QA | `qa_short.py` (nba profile) | `qa_short.py` (story profile, automatic under `Soccer Channel/`) |
