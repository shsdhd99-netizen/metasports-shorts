---
name: daily-run
description: >
  The automatic daily MetaSports run, one channel per run (nba or fc): pull analytics and retention curves, learn from yesterday's
  results, research today's story, make ONE Short that passes full QA, put it on the channel's Hub with a posting slot, log
  everything, commit and push. Never posts. Use when a scheduled task says "daily run", or the user types /daily-run nba|fc.
  Argument: nba (MetaSports) or fc (MetaSports FC).
---

# /daily-run nba|fc (owner's ask, Oct 24 2026: "automatically make 4 shorts every 2 days... make sure all new research is logged,
# daily research is done, and retention charts are pulled. make sure you are getting better over time")

Two runs a day (scheduled tasks "MetaSports NBA daily run" and "MetaSports FC daily run") = one NBA + one soccer Short a day,
4 every 2 days. ElevenLabs Creator credits (100K a month, reset on the 19th) pay for about 2 Shorts a day; that is the ceiling.

**Standing rules (owner's, never relax them):**
- Never publish, schedule or replace a public video, and never open YouTube Studio. Every output is a DRAFT; the owner posts.
- Never print, commit or ask for API keys or tokens. Keys come from the environment only.
- Never invent a stat or a result. If data is missing, write "missing" and say why.
- No promo or teaser at the end; no dead air; every Short under 60 s.
- No cards (1.5 s at most if one is unavoidable, never in the first 4 s). TikTok and Instagram cross-posting is paused.
- **The rules changed in the Oct 26 overnight review.** THE RULES at the top of `MetaSports - Playbook.md` win over this file;
  every change is listed in `Research Notes/Rule Changes Applied (Oct 26, 2026).md`.
- Work on branch `main-329h3w`; push there; never open or merge a PR.

**NBA music-bed test (owner said yes, Oct 26):** NBA posts alternate music and no music, starting with #69 Luka (none) and #70 Barkley (music). Render both versions of every NBA Short, and mark on the Hub which one to post so the alternation holds. The bed is about 20 dB under the voice (`music.json`, bed_lu -20), from `Library/Music/` (ElevenLabs beds: no Content ID, no pay cut). Log music yes/no on every post in `Research Notes/Outcome Log.md`. Decide after 8 posts (4 each) on stayed %, judged at 72 h. Soccer keeps its own music A/B.

## 0. Setup (5 min)
1. `git fetch origin main-329h3w && git checkout main-329h3w && git pull --no-rebase origin main-329h3w`
   (if the repo is missing, attach `shsdhd99-netizen/metasports-shorts` and clone it first).
2. `bash Tools/cloud_setup.sh`. It prints `key: set` when `ELEVENLABS_API_KEY` is in the environment.
3. **No key?** Do steps A-C and write the script and notes only. Set the Hub card to `editing` with the note "needs the ElevenLabs
   key in the environment settings". Never fake a voice.
4. Read the newest entries of `Research Notes/Daily Log.md` and this channel's lessons (below) before deciding anything.

## A. Data and retention (10 min)
- Analytics run 48-72 h behind: score a Short only once it is 72 h old; before that, use live view counts.
- NBA: `python Tools/yt_analytics.py daily`. FC: `python Tools/yt_analytics.py --channel fc daily`.
  This writes the per-Short metrics and the retention curves (`retention <date>.csv`, 100 points a Short) for Shorts under 14 days
  old, then prints flags. It needs the secrets `YT_CLIENT_ID`, `YT_CLIENT_SECRET` and `YT_REFRESH_TOKEN` (NBA) or
  `YT_REFRESH_TOKEN_FC` (FC). Without them, log "analytics: no token" and use the newest Studio export instead.
- New Studio exports (the owner's weekly zip) go in `Research Notes/Studio exports/`. "Stayed to watch" exists only there.
- Fill a posted Short's Hub `results` only where the owner has not; never overwrite numbers the owner typed.
- **The dataset (Oct 24 audit):** `python Tools/shorts_dataset.py --report` merges every export and API file into
  `Research Notes/Shorts Dataset.csv`. For each newly posted Short fill its hand columns: lane, star, fresh (same-day / late
  news / evergreen), frame1, music, captions, folder. Every rule change must cite this table (n and medians), not one Short.

## B. Learn (10 min): getting better every day
- For each Short 2-7 days old, compare its numbers and retention curve with the rules: frame 1, the promise, the turn timing,
  length, freshness. Where the curve drops (the report's flags), look at the frames at that second and name the cause.
- A pattern seen on 3 or more Shorts becomes a lesson with an evidence tier ([V] measured / [S] seen / [H] guess):
  NBA in `Research Notes/Lessons Learned (running log).md`, FC in `Soccer Channel/Lessons Learned.md`.
  A lesson that is a rule also goes into the skill (`cloud-short`, `story-short`) or a QA check (`Tools/qa_short.py`).
- **Sundays:** the weekly review. Rank the week's Shorts by stayed % and views; top 3 and bottom 3, each with a reason;
  one rule to keep, one to drop. Update the Hub's `channel/stats` insights and `UPLOAD SCHEDULE.md` if the best times moved.

## C. Research (20 min): logged with sources
- **Read THE RULES §1 in `MetaSports - Playbook.md` first (Oct 26 overnight review).** Pick today's lane from the dataset's last 6
  posts on this channel (lanes below); a lane with 3 posts in a row below the channel median is retired until the Sunday review. A strong concept that got under 74% stayed may get ONE new edit (new first 3 s and frame 1, new title),
  never the same file again.
- **NBA lanes (Oct 26 overnight review) [S] `Research Notes/Similar Channels (Oct 26, 2026).md` §4:**
  - **About half are moments:** last night's funny, odd or skilful thing you can watch (game, bench, warm-up, fan, kid, mascot,
    broadcast desk), narrated: who, what, the reaction or payoff. Each moment needs **one fact the clip can't show** (YouTube's
    originality rule [V official]). Footage from the league, teams and broadcasters on X or NBA.com, never another creator's edit.
  - **The other half rotates:** the **star paradox** (THE #42 FORMAT, `Library/THE 42 FORMAT.md`: now one lane, not the lead; its
    test ended 1 of 3 at 74%+ [V]); **same-day news** with a number gap about a household name (#58, 75% stayed); and the
    **weekly countdown test** (one a week: "3 times [star] did X", a #3 / #2 / #1 corner badge with `Tools/overlay.py` `"x"` and
    `"box"`, the best one last) [H].
  - **Review the split after 10 moment posts** (stayed % and 72 h views vs the channel median) and log the result in the Daily Log.
  - **Same-day news or not at all:** only stories from the last 24 h; news goes up the morning after the game. #63 went out a day
    late and kept 58%. Run `python Tools/copy_check.py "<4-6 words>"`.
- **Research tools (both channels, Oct 26 overnight review):** check `Research Notes/Competitor Watchlist.csv` (the channels we
  watch) for new hits in our lanes. `python Tools/yt_watch.py <link>` has Gemini watch a Short and writes a report to
  `Research Notes/Watch Reports/`; it needs a free `GEMINI_API_KEY` in the environment (without it, log "watcher: no key" and use
  `Tools/yt_sheet.py` frames). Tier its numbers [S].
- **FC:** the next unmade story in `Soccer Channel/Idea Bank.md` that passes the hook rules in
  `Research Notes/Why S02 and S03 Underperformed (Oct 24, 2026).md`. Add 2 new vetted ideas (global star, concrete object or
  strong verb, real footage exists, sources) to the Idea Bank every day.
- Write today's research in `Research Notes/Daily Log.md`: the candidates, the pick and why, every source link.

## D. Make the Short (60-120 min)
- **NBA (Oct 26 overnight review editing rules; Playbook THE RULES §2):** `/cloud-short` in today's lane, 20-30 s, the Alex voice, no music.
  - **Footage first:** frame 1 and one proof clip per beat, from any number of sources; never filler to reach a clip count.
  - **Frame 1 shows what line 1 is about, happening. Line 1 is 11 words or fewer.**
  - **Hold the opening:** shot 1 at least 2.0 s; at most 2 shots in the first 3 s and 3 in the first 5 s; about 10-15 shots of about 2 s.
  - **Replay the key second once before the payoff** (closer and/or `"speed": 0.5`, marked `"replay": true`).
  - **Fill the frame:** wide plays `"blurfit": true, "blurfit_aspect": 0.75` (3:4); full-width blur-fit only for a graphic to read whole.
  - **Proof on the footage** (`"overlay"`, `broll.py circle`), no cards, no emoji stickers, no forced loop: end on the payoff.
  Footage: `Tools/nba_videos.py` (team sites on NBA.com), `Tools/x_clip.py` (official accounts on X), archive.org.
  Frame 1: sharp and lit, showing the claim: the moment itself or the star, whichever proves line 1 (#42 opened on the
  airball; #52's soft archive close-up kept 59%).
- **FC:** `/story-short`, ending under 59.5 s (about 230-250 words; if it runs long, cut a sentence, never add one), the hook
  rules, both versions (music and no music: an open A/B test; log which one the owner posts), `"promise"` list in cuts.json.
  Frame 1 shows the promise; shot 1 at least 2.0 s; wide plays at 3:4; replay the key moment when the footage has it (Oct 26 overnight review).
  **PAUSED (owner, Oct 26: "skip the cuts for other apps, id rather be successful on yt first"): no long cuts until the owner says so.** Was:
  **Plus the TikTok/Instagram long cut (Oct 25):** in `<folder>/long/`, the same script with one or two extra sourced beats,
  re-voiced whole, 65-80 s (never under 62 s: TikTok pays only over 1 minute), music version only, `qa_short.py --long --full`
  PASS, saved as `DRAFT - awaiting approval - SNN <title> (TikTok-IG long, music).mp4`. Card version label "TikTok-IG long".
- **NBA on TikTok/Instagram: PAUSED** (owner, Oct 26: YouTube first). No TikTok cuts until the owner says so.
- **Faster tools (Oct 24):** `Tools/frame_sheet.py SRC --from A --to B --every 0.5` (contact sheet in seconds) and
  `--cuts` (scene-change times: start and end shots between them, never inside a reel's dissolve); write `cuts_plan.json`, then
  `Tools/fill_len.py F` fills every len from the anchors; in cuts.json `"speed": 0.5` slows a short close-up and `"overlay": [...]`
  burns the words over footage at cut time; after `cut_list.py`, `Tools/shot_strip.py F out.jpg` shows each shot's first, middle
  and last frame (catches dark first frames, dissolves, a player leaving the crop).
  Oct 26: `"blurfit_aspect": 0.75` crops a wide play to a 3:4 window over blur (`broll.py --blurfit-aspect`); `"replay": true` now
  passes from cuts.json into shots.json, so QA accepts a deliberate replay; an overlay line takes `"x": "left"|"right"` and `"box"`.
- **Gate:** `python Tools/qa_short.py --folder F --video <file> --full` must PASS (it now also fails a dark frame 1 and sound
  still ringing at the end: give the last effect a `len` and `fade` in sfx.json). Then LOOK at frame 1, every overlay and the
  last frame. Every fact has a source and its exact words in notes.md.
- **Package (Oct 26 overnight review; [V] `Research Notes/Posting Study (Oct 26, 2026).md`):**
  - **Title:** a short statement pointing at the moment; no hashtag or one (#nba / #football). Title wording is a small factor:
    no title scoring.
  - **Description:** empty.
  - **Tags (optional):** 3-8 relevant tags, about 100-150 characters (names, team, event, common misspellings). Never fill the 500
    characters. Check with `python Tools/tags_fit.py --cap 150 "tag1, tag2, ..."`. Put them in UPLOAD.md and the card.
- **Critic:** Script Critic v3 is advice, not a gate (Oct 26 overnight review). Only a factual error blocks a Short.
- If it cannot pass today, do not ship it: Hub card `editing` with the reason. A late news Short is dropped, not posted late.

## E. Hub and schedule (10 min)
- Hubs: NBA https://claude.ai/artifact/SAWcHwuAwBxJuyBQSs8a8U, FC https://claude.ai/artifact/2UVAcbNpKq6j4YXBEF8ge3.
  Upload a 1.5 Mbps copy as an asset (Artifact publish `asset: true`), then write the card (collection `shorts`: code, name, num,
  status `ready`, slot, slotLabel, versions [{label, assetId, note}], titles, tags, postNote). Read a card before writing it and
  pin every write with `if_version`.
- **Card text for TikTok and Instagram: PAUSED** with cross-posting (owner, Oct 26). Leave the `tiktok` and `instagram` fields empty.
- Slots follow `UPLOAD SCHEDULE.md` (Oct 26 overnight review): up to 2 per channel per day (Oct 26; the 2nd only when as strong). NBA at 11:00 AM ET (today's news
  Short takes today), soccer at 12:00 PM ET (the next free day), at least 1 hour after the NBA slot. A second NBA slot (6 PM) only
  for a Short as strong as the first, 6+ hours later; never 3. Keep at least 2 days of ready Shorts per channel; mark an unposted
  news Short older than a day `skip`. Never re-slot or re-upload a posted Short; judge it at 72 h.
- Commit (the `DRAFT - awaiting approval` files are kept in git) and push to `main-329h3w`. If the push is refused, pull with
  `--no-rebase`, merge (keep both sides of any doc), push again.

## F. Report (3-5 plain lines)
What was made, its slot, QA result, what you learned today, and anything only the owner can do.

## Lessons to read first
- Both: `Research Notes/Rule Changes Applied (Oct 26, 2026).md` and THE RULES at the top of `MetaSports - Playbook.md`.
- NBA: `Research Notes/Retention and Editing Upgrade (Oct 26, 2026).md`, `Research Notes/Why NBA Views Dropped (Oct 26, 2026).md`,
  `Research Notes/Studio Export Read (Oct 24, 2026).md`, `Library/THE 42 FORMAT.md`.
- FC: `Soccer Channel/START HERE.md`, `Soccer Channel/Lessons Learned.md`, `Research Notes/Why S02 and S03 Underperformed (Oct 24, 2026).md`.
