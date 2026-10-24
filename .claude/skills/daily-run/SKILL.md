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
- Work on branch `main-329h3w`; push there; never open or merge a PR.

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
- **Read `Research Notes/What Makes Our Shorts Go Viral (Oct 24, 2026).md` first.** Pick today's lane by rotation: no lane more than
  1 post in 3 (check the dataset's last 6 posts on this channel); a lane with 3 posts in a row below the channel median is retired
  until the Sunday review. A strong concept that got under 74% stayed may get ONE new edit (new first 3 s and frame 1, new title),
  never the same file again.
- **NBA:** last night's games: records, career highs and lows, milestones, viral moments (NBA.com, ESPN, AP, team and league
  accounts on X). Pick the story that fits THE #42 FORMAT (`Library/THE 42 FORMAT.md`: a famous star, a record that sounds bad
  or impossible, "So is he...? No.", end on the number) or a same-day number-gap story (#58, 75% stayed).
  **Only stories from the last 24 h:** #63 went out a day late and kept 58%. Run `python Tools/copy_check.py "<4-6 words>"`.
- **FC:** the next unmade story in `Soccer Channel/Idea Bank.md` that passes the hook rules in
  `Research Notes/Why S02 and S03 Underperformed (Oct 24, 2026).md`. Add 2 new vetted ideas (global star, concrete object or
  strong verb, real footage exists, sources) to the Idea Bank every day.
- Write today's research in `Research Notes/Daily Log.md`: the candidates, the pick and why, every source link.

## D. Make the Short (60-120 min)
- **NBA:** `/cloud-short` in THE #42 FORMAT: 20-30 s, the Alex voice, no music, words over footage (`Tools/overlay.py`).
  Footage: `Tools/nba_videos.py` (team sites on NBA.com), `Tools/x_clip.py` (official accounts on X), archive.org.
  Frame 1: sharp and lit, showing the claim: the moment itself or the star, whichever proves line 1 (#42 opened on the
  airball; #52's soft archive close-up kept 59%).
- **FC:** `/story-short`, 55-59.9 s, the hook rules, both versions (music and no music), `"promise"` list in cuts.json.
- **Faster tools (Oct 24):** `Tools/frame_sheet.py SRC --from A --to B --every 0.5` (contact sheet in seconds) and
  `--cuts` (scene-change times: start and end shots between them, never inside a reel's dissolve); write `cuts_plan.json`, then
  `Tools/fill_len.py F` fills every len from the anchors; in cuts.json `"speed": 0.5` slows a short close-up and `"overlay": [...]`
  burns the words over footage at cut time; after `cut_list.py`, `Tools/shot_strip.py F out.jpg` shows each shot's first, middle
  and last frame (catches dark first frames, dissolves, a player leaving the crop).
- **Gate:** `python Tools/qa_short.py --folder F --video <file> --full` must PASS (it now also fails a dark frame 1 and sound
  still ringing at the end: give the last effect a `len` and `fade` in sfx.json). Then LOOK at frame 1, every overlay and the
  last frame. Every fact has a source and its exact words in notes.md.
- **Tags:** list them most important first and run `python Tools/tags_fit.py "tag1, tag2, ..."`: it fills YouTube's box to
  490 characters by YouTube's own count (owner's rule: use the 500 limit, hard cap 490). Put the result in UPLOAD.md and the card.
- If it cannot pass today, do not ship it: Hub card `editing` with the reason. A late news Short is dropped, not posted late.

## E. Hub and schedule (10 min)
- Hubs: NBA https://claude.ai/artifact/SAWcHwuAwBxJuyBQSs8a8U, FC https://claude.ai/artifact/2UVAcbNpKq6j4YXBEF8ge3.
  Upload a 1.5 Mbps copy as an asset (Artifact publish `asset: true`), then write the card (collection `shorts`: code, name, num,
  status `ready`, slot, slotLabel, versions [{label, assetId, note}], titles, tags, postNote). Read a card before writing it and
  pin every write with `if_version`.
- Slots follow `UPLOAD SCHEDULE.md`: NBA at 11:00 AM ET (today's news Short takes today), soccer at 12:00 PM ET (the next free day).
  Keep at least 2 days of ready Shorts per channel; mark an unposted news Short older than a day `skip`.
- Commit (the `DRAFT - awaiting approval` files are kept in git) and push to `main-329h3w`. If the push is refused, pull with
  `--no-rebase`, merge (keep both sides of any doc), push again.

## F. Report (3-5 plain lines)
What was made, its slot, QA result, what you learned today, and anything only the owner can do.

## Lessons to read first
- NBA: `Research Notes/NBA Diagnosis (Oct 23, 2026).md`, `Research Notes/Studio Export Read (Oct 24, 2026).md`, `Library/THE 42 FORMAT.md`.
- FC: `Soccer Channel/START HERE.md`, `Soccer Channel/Lessons Learned.md`, `Research Notes/Why S02 and S03 Underperformed (Oct 24, 2026).md`.
