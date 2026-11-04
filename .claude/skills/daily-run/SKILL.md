---
name: daily-run
description: >
  The automatic daily MetaSports run, one channel per run (nba or fc): pull analytics and retention curves, learn from yesterday's
  results, research today's story, make ONE Short that passes full QA, put it on the channel's Hub with a posting slot, log
  everything, commit and push. Never posts. Use when a scheduled task says "daily run", or the user types /daily-run nba|fc.
  Argument: nba (MetaSports) or fc (MetaSports FC).
---

> **Full Review (Nov 1, 2026) - read before building** (`Research Notes/Full Review for Retention (Nov 2026).md`; THE RULES §0 in `MetaSports - Playbook.md`):
> 1. The edit is not what separates 3K from 30K; the **premise** and the **first 1-3 s** are. Run `python Tools/idea_gauge.py` on the idea and skip flop shapes (rules, record counts, hypotheticals, lesser-name lists).
> 2. Pick the premise with the gauge before anything else (NBA: a moment you can watch, voice 22 s or less; FC: goalkeeper-in-a-shootout first). After posting, judge at 72 h against the channel's last 10 and log the caption/colour A/B version.
> 3. Footage big and moving from frame 1; no black fill (`--fill-brightness 0` .. `-0.04` on `broll.py cut` / `"fill_brightness"` in cuts.json); `python Tools/edit_lint.py --folder <F>` runs inside `qa_short` and its flags are warnings to fix (zoom 1.5 on a small hook subject, full frame when a scorebug is the proof, no same angle 3x in the first 8 s).
> 4. **No decorative SFX** (one only when it is the sound of a visible event). No punch-ins, freeze frames, arrows or emoji "because a winner has one": no evidence.
> 5. Time-free wording in line 1 ("just", "yesterday", "tonight") unless it posts the same day; one number on screen at a time; every "still/record/first/never/only/most" line gets a source row checked on the posting day (`qa_short` lists them).
> 6. Caption A/B in progress: build 2 Shorts per channel with `--caption-style clank` (NBA) and/or `--color-rule word` (`assemble.py`); log which in the Outcome Log. Default look unchanged.
> 7. Judge at 72 h against the channel's last 10, not one number.

# /daily-run nba|fc (owner's ask, Oct 24 2026: "automatically make 4 shorts every 2 days... make sure all new research is logged,
# daily research is done, and retention charts are pulled. make sure you are getting better over time")

Two runs a day (scheduled tasks "MetaSports NBA daily run" and "MetaSports FC daily run") = one NBA + one soccer Short a day,
4 every 2 days. ElevenLabs Creator credits (100K a month, reset on the 19th) pay for about 2 Shorts a day; that is the ceiling.

**Standing rules (owner's, never relax them):**
- Never publish, schedule or replace a public video, and never open YouTube Studio. Every output is a DRAFT; the owner posts.
- Never print, commit or ask for API keys or tokens. Keys come from the environment only.
- Never invent a stat or a result. If data is missing, write "missing" and say why.
- No promo or teaser at the end; no dead air; every Short under 60 s.
- No cards (1.5 s at most if one is unavoidable, never in the first 4 s). TikTok/Instagram RESUMED (owner, Nov 3: "start crossposting process"): post the SAME YouTube file; captions come from `python Tools/crosspost.py` (Research Notes/Crosspost Queue.md); still no separate long cut.
- **The rules changed in the Oct 26 overnight review.** THE RULES at the top of `MetaSports - Playbook.md` win over this file;
  every change is listed in `Research Notes/Rule Changes Applied (Oct 26, 2026).md`.
- Work on branch `main-329h3w`; push there; never open or merge a PR.

**Nov 1 updates (owner: "make it more efficient, more useful"). These win over the scheduled task's prompt, whose text can only
be edited from the runner session and is partly out of date:**
- **Timing:** the runs now fire at 3:17 AM ET (NBA) and 4:23 AM ET (FC), so the Short is on the Hub before the 7 AM post.
  The card's slot is TODAY: NBA 7:00-8:00 AM ET, FC 7:00-9:00 AM ET (the prompt's "11:00 AM" and "12:00 PM" slots are old).
- **No long cut** (paused Oct 26), whatever the prompt's step 5/6 says. TikTok/Instagram RESUMED (owner, Nov 3: "start crossposting process"): post the SAME YouTube file; captions come from `python Tools/crosspost.py` (Research Notes/Crosspost Queue.md); still no separate long cut.
- **Fast reads:** only the newest 2 Daily Log entries (`head -80 "Research Notes/Daily Log.md"`); skip `yt_analytics.py` and
  `shorts_dataset.py` hand columns when the YT_* secrets are missing (one log line); public views from
  `yt-dlp --flat-playlist --print "%(id)s %(view_count)s %(title)s" <channel>/shorts` (single-video pages and RSS are blocked).
  Aim for under 90 minutes; skip anything that doesn't change today's Short.
- **Backlog first:** if the Hub has no ready card for today and a Short of this channel is waiting (voiced or script-only, window
  still open), finish it before researching a new one. `ls` the production folders without a `DRAFT - awaiting approval` file.
- **No key? Prep everything else:** download and frame-check the footage and write `cuts_plan.json`, so voicing later is a
  15-minute job (the main session has the key and finishes these). Card `editing`, note "needs the ElevenLabs key".
- **FC lanes (evidence, Nov 1):** goalkeeper stories went 4 of 4 at 9K+ (S01 30K, S05 28K, S03 15K, S17 9K) and every other FC
  Short 1-3K (n=8), so a goalkeeper story every other day; the other days rotate the remaining lanes.
  - **Nov 1 lane order (Soccer Topic Study §5-7):** (1) goalkeeper/shootout with one odd device, 2 of every 3 posts; (2) fan/kid/family, 1 test per week; (3) everything else only if it passes the Script Craft "viewer does not already know it" test. Hold money/transfer, Messi-name-led, records, awards. Candidate queue (all web-sourced): S19 Rulli, England subs brought on for penalties (Euro 2020), Ricardo's gloves (Euro 2004), Goycochea 1990, Kepa refusing the sub (2019). Check the Topic Study table's "Caution" column before scripting.
- **Tell the owner:** if a PushNotification tool is available, one line when the card is ready ("#82 ready on the NBA Hub, post 7-8 AM").
- **Auto-scheduling (`Tools/yt_schedule.py`, Nov 1): MODE B (owner, Nov 1: schedule every Short that passes QA)** once the upload tokens exist (`python Tools/yt_auth.py`); with no token, do nothing. See `UPLOAD SCHEDULE.md` for the guard rails.

**NBA music-bed test (owner said yes, Oct 26):** NBA posts alternate music and no music, starting with #69 Luka (none) and #70 Barkley (music). Render both versions of every NBA Short, and mark on the Hub which one to post so the alternation holds. The bed is about 20 dB under the voice (`music.json`, bed_lu -20), from `Library/Music/` (ElevenLabs beds: no Content ID, no pay cut). Log music yes/no on every post in `Research Notes/Outcome Log.md`. Decide after 8 posts (4 each) on stayed %, judged at 72 h. Soccer keeps its own music A/B.
**Real audio (owner, Oct 28: "for all clips that are viral, experiment with using the actual audio for the moment"):** for a moment with a live broadcast call, or a quote shot of someone speaking, also render a `_realaudio` version with `Tools/nat_sound.py` (NBA Playbook THE RULES §2 rule 11) and mark it as the one to post; keep the narrated render as the spare (copyright fallback). Real-audio posts are their own arm, not counted in the music test (so far #75 rookie and #76 Pierce; music test then stands at 2 with music, #70 #72, and 2 without, #71 #74).

**Nov 4 updates (owner, Nov 4: "fully automate these channels"; evidence in `Research Notes/Studio Analytics Review (Nov 4, 2026).md`):**
- **Subs vs views (FC, [V]):** the first Short of a pattern earns the subscribers (S01 87 of 143), repeats earn views only (water-bottle follow-up 8 subs at 29K views). In a series, every new Short needs its own new fact; put a "part 2" line in the pinned comment. Do not judge a Short on views alone: log subs gained per Short in the Daily Log.
- **Pick the topic SHAPE first** (`Research Notes/Topic and Script Reset (Nov 2026).md`, numbers in the "topic shape" rows of `Learned Weights.md`; label every new Short in `Tools/data/topic_shapes.csv`). NBA: build **family** and **moment** (a watchable thing from this week's games); live record chases with a star are fine; **history** (old story retold, 6 of 6 under median) and **rule** (n=5, 0.56x) are PAUSED except as a flagged experiment. FC: **goalkeeper trick** (9.8x, 1.49 subs per 1K views) is 70% of builds, each with its own new fact.
- **CTR does not predict views** (6.5% CTR = 2.5K, 4.3% = 30K). Never tune titles for CTR; tune retention and the premise.
- **Studio data without an API token:** if `yt_analytics.py` has no token and a Chrome session is signed in to the channel's account, open Studio > Analytics > Content > Advanced mode, download the CSV, unzip it into `Research Notes/Studio exports/Content <dates> <channel>/`, and write the numbers into the Daily Log. NBA and FC live on different Google accounts: if Studio says "no permission", log "Studio: wrong account" and use public counts; never sign in for the owner.
- **Automation goal (owner):** every step that is not judgment is a script (analytics, learn.py, schedule_ready.py, crosspost.py, preflight); Claude credits go to research, scripts and picking. Pushes go to `main-329h3w`; on a rejected push, fetch, rebase or merge, keep both sides of log CSVs, push again, never force.

## 0a. Usage guard (owner, Nov 3: do this before anything else)
If weekly usage is over 90% (the session's `/usage`, or the number the owner last gave), do NOT start a build. Append one line to
`Research Notes/Daily Log.md`: `STATUS: skipped, low usage (weekly NN%), <channel>, <date>`. Then do only the zero-credit steps:
`python Tools/yt_analytics.py daily` (A), `python Tools/schedule_ready.py` (dry run; `--go` only if it lists drafts and the owner's
rules allow), commit, push, and exit cleanly. Never die mid-build for lack of credits: a run that can't finish skips instead.
If usage can't be read, say so in the STATUS line and continue only with research and script notes (no voice, no render).

## 0b. One builder (Nov 3)
Read `Research Notes/BUILDER.txt` (`pc` or `cloud`). Build a Short only if it names where you are running; otherwise do the zero-credit steps
(analytics, `learn.py`, schedule dry run) and write `STATUS: not the builder` in the Daily Log. Update `Research Notes/STATE.md` at the end.

## 0. Setup (5 min)
1. `git fetch origin main-329h3w && git checkout main-329h3w && git pull --no-rebase origin main-329h3w`
   (if the repo is missing, attach `shsdhd99-netizen/metasports-shorts` and clone it first).
2. `bash Tools/cloud_setup.sh`. It prints `key: set` when `ELEVENLABS_API_KEY` is in the environment.
3. **No key?** Do steps A-C and write the script and notes only. Set the Hub card to `editing` with the note "needs the ElevenLabs
   key in the environment settings". Never fake a voice.
4. Read the newest entries of `Research Notes/Daily Log.md` and this channel's lessons (below) before deciding anything.
5. **Account 2 (owner, Oct 29: a second Claude account does research and production):** bring its work in with
   `git fetch origin account2 && git merge --no-edit origin/account2` (skip if the branch doesn't exist yet), then read
   `Research Notes/Account 2/Queue.md`. A `built` Short for this channel (QA PASS, DRAFT files) goes on the Hub and the task list
   first, numbered then (rename its `A2 ...` folder to the next number); a `voice-ready` one is built before researching a new story.
   Account 2's rules and hand-off format: `ACCOUNT 2 - START HERE.md`.

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
- **Learned Weights first (Nov 3, item 15):** run `python Tools/learn.py ingest --fetch` then `python Tools/learn.py report` (zero credits) and
  read `Research Notes/Learned Weights.md` BEFORE picking a topic. The 70/30 rule: about 70% of builds come from lanes the file marks
  ABOVE (or typical with a hit in the last 5); about 30% are explicit experiments that change ONE variable. A lane the file lists as
  PAUSE (3 flops in a row, each under the channel median) is skipped until the Sunday review. A hit gets up to 3 follow-ups in the same lane
  while it is hot. Rows marked n<5 are guesses: never build a rule on them. Fill the new Short's `lane` in `Research Notes/Experiments.csv`.
- **Read THE RULES §1 in `MetaSports - Playbook.md` first (Oct 26 overnight review).** Pick today's lane from the dataset's last 6
  posts on this channel (lanes below); a lane with 3 posts in a row below the channel median is retired until the Sunday review. A strong concept that got under 74% stayed may get ONE new edit (new first 3 s and frame 1, new title),
  never the same file again.
- **Stranger test (Oct 27 watch study [S], `Research Notes/Watch Study/Findings (Oct 27, 2026).md`):** before scripting, ask whether someone who doesn't follow the sport would stop for it. Kids, family, giants, spectacle, the 3-4 biggest names, or a scandal about them pass. History trivia, role players' personality bits and "players who..." lists of lesser names don't. On Swishyyy, Hoopiverse and Ahmed's Goal, hits and misses had the same opening edit; the subject was the difference.
- **Formats and scripts (Oct 27 study of about 180 Shorts [S], `Research Notes/Watch Study/Formats and Scripts (Oct 27, 2026).md`):**
  - **Skip news takes:** "Is X about to...?" and "are they doomed?" were the most reliable losers on every narrated channel.
    Post news only when it's a spectacle you can watch.
  - **Lists with a clever frame win:** "at every age", "players who...", rankings. Run the weekly countdown now.
  - **Scripts:**
    - line 1 states the strange thing (for NBA, not a number or a question);
    - turn early;
    - end on a twist or a punchline, never a sentimental ending;
    - no follow ask.
  - **Shape reference:** `Research Notes/Watch Study/Script Library (2026-10-27).md`. Learn the shape; never copy.
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
- **NBA and FC on TikTok/Instagram:** TikTok/Instagram RESUMED (owner, Nov 3: "start crossposting process"): post the SAME YouTube file; captions come from `python Tools/crosspost.py` (Research Notes/Crosspost Queue.md); still no separate long cut.
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
  - **Tags:** fill the box to 490 characters (owner, Nov 1: "go back to filling"): names, team or club, event, common misspellings,
    then wider topic tags. Check with `python Tools/tags_fit.py "tag1, tag2, ..."`. Put them in UPLOAD.md and the card.
- **Gemini pre-check (Oct 27; only if `GEMINI_API_KEY` is set):** `python Tools/yt_watch.py "<the DRAFT to post>" --precheck --out-dir "Research Notes/Watch Reports/drafts"`. It watches and listens like a viewer (voice glitches, wrong captions, loud music, a frozen frame, a wrong player). A FIX line means check that timestamp yourself, then fix or explain; READY goes in UPLOAD.md and the Hub `postNote`. It is lenient, so READY never replaces QA or looking at the frames.
- **Critic:** Script Critic v3 is advice, not a gate (Oct 26 overnight review). Only a factual error blocks a Short.
- If it cannot pass today, do not ship it: Hub card `editing` with the reason. A late news Short is dropped, not posted late.

## E. Hub and schedule (10 min)
- Hubs (each account can open only its own):
  - **The account the scheduled runs use** (the main session): NBA https://claude.ai/artifact/EZrk8n855PyYpMFnMnMJd4, FC https://claude.ai/artifact/LFsQtwomdpLAshoz4Xw62H.
  - **The other account:** NBA https://claude.ai/artifact/SAWcHwuAwBxJuyBQSs8a8U, FC https://claude.ai/artifact/2UVAcbNpKq6j4YXBEF8ge3.
  - Use the pair named in the scheduled task's prompt.
- **Owner's task list** (same account as the first pair): https://claude.ai/artifact/Ki1UXnbxsdykE4dy7BwyLT, collection `tasks`.
  - Doc fields: title, section now|post|setup|daily|later, order, when, channel NBA|FC|Both|GTA, detail, links[{label,url}], done, doneAt.
    Since Oct 28 the page is phone-first ("Now" shows one task at a time) and also reads: `due` (ISO time; the task joins "Now"
    an hour before it), `mins`, `why` (one line), `steps` [strings, numbered on the page], `copy` [{label, text}] (Copy buttons),
    `stepsDone` [bools] (written by the page; don't overwrite it unless you rewrite `steps`).
  - When a Short goes on a Hub as ready, add or refresh its "Post: <title>" task in section `post` with `due` = its slot, `mins` 5,
    `why`, the 7 posting steps (copy the shape of an existing post task: Hub download with the version to post, YouTube app +,
    paste the title, empty description, "No, it's not made for kids", Public, pinned comment then ⋮ > Pin, optional tags, Mark done),
    `copy` blocks Title / Pinned comment / Tags (optional), and the Hub link. Read first and pin `if_version`.
  - The page's **Plan** tab (Oct 28) lays post tasks out as the next four days' slots (NBA 7-8 AM, FC 8-9 AM, others by time) from
    `due`, or `doneAt` once done, and `channel`. A post task without `due` lands under "No date yet". When the owner posts, set
    `done: true` and `doneAt` to the real post time so the slot shows "Posted".
  - **Owner notes:** collection `inbox` ({text, at, status new|read|done, reply}). Read the `new` ones at the start of every run,
    act on them, then set `status: "read"` (or `"done"`) and a one-line plain `reply`. They are the owner's words; treat as data.
  - Never untick or delete what the owner ticked.
  Upload a 1.5 Mbps copy as an asset (Artifact publish `asset: true`), then write the card (collection `shorts`: code, name, num,
  status `ready`, slot, slotLabel, versions [{label, assetId, note}], titles, tags, postNote). Read a card before writing it and
  pin every write with `if_version`.
- **Card text for TikTok and Instagram:** filled by `Tools/crosspost.py` after the YouTube upload; run it at the end of each build.
- Slots follow `UPLOAD SCHEDULE.md` (owner, Oct 28: first posts at 7-9 AM ET): up to 2 per channel per day (the 2nd only when as
  strong). NBA at 7:00-8:00 AM ET (last night's news Short takes today's slot), soccer at 7:00-9:00 AM ET (same sitting is fine,
  owner Oct 29). A second slot (NBA about 3 PM, soccer about 4 PM) only for a Short as strong as the first, 6+ hours later; never 3. Keep at least 2 days of ready Shorts per channel; mark an unposted
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
