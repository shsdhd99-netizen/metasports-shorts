# Improvement backlog (Nov 3, 2026; Account 1 works this top to bottom; add dated lines, tick when done)
Tags: [Z] zero credit (PC script/doc) | [C] needs Claude credits | [O] owner decision | [V] video quality | [A] automation

## Automation
- [x] (Nov 3, PC acct 1: `**Arm:**` line or opt-in `--default-arm`; music column not logged yet) [A][Z] `schedule_ready.py`: choose between a music and a no-music DRAFT by a rule (card says `**Arm:**`, else no-music) so A/B pairs stop being skipped. Log the arm in `Experiments.csv` (`music` column).
- [x] (2026-11-05, terminal) [A][Z] `schedule_ready.py`: write skips to `Research Notes/Schedule Ready Log.md` on `--go` too (today only the count is logged), and add a `--require-approved` mode (Hub card `approved: true`) for the day the owner wants option B strictly.
- [x] (2026-11-05, terminal: Tools/hub_pack.py) [A][Z] A `Tools/hub_pack` helper that re-encodes a DRAFT under 20 MB (crf 28, 96k audio) and verifies it with `qa_short`, so every Short can go on the Hub without a manual step.
- [ ] [A][Z] Log rotation / cleanup script: delete `src/` and `clips/` of Shorts posted 7+ days ago, list first, exact folders, owner-approved (disk 27 GB free).
- [ ] [A][Z] `STATE.md` writer: `python Tools/state.py` updates weekly %, builder, last run times and open claims, so any account can read one page.
- [ ] [A][Z] Make `Tools/learn.py` judge at exactly 72 h (stamp `judged_at`), add engaged ratio and stayed % as outcome columns, and write a per-lane streak table (PAUSE after 3 flops).
- [ ] [A][C] Cloud routine health check: a third routine at 8 AM ET that reads both routines' logs, writes one STATUS line, and opens a `PC Requests.md` line for anything it cannot do.
- [ ] [A][O] Cloud keys in the environment; Publish app (OAuth); then switch on option C after two clean weeks.
- [ ] [A][Z] Cron-style lock: the timers and the cloud can both touch `Scheduled Uploads.csv`; add a git pull before and a retry after in `schedule_ready.bat` (it already pulls; add conflict handling).

## Videos (quality and growth)
- [ ] [V][C] (Growth Study, Nov 3) ONE-variable test: NBA story Shorts at 30-35 s vs our usual 18-25 s, same lane; log `length` in Experiments.csv, 4 each, judge at 72 h on viewed-vs-swiped and views.
- [ ] [V][C] (Growth Study, Nov 3) Hook + foreshadow: line 2 says what the ending is about (Hoyos). Try on 4 Shorts before making it a rule.
- [ ] [V][O] (Growth Study, Nov 3) TikTok 60 s+ versions for Creator Rewards: only once a TikTok account nears 10K followers.
- [ ] [V][C] Test ONE hook variable at a time: tension-first (no result in line 1) vs result-first, same lane, same length. The low-engagement openings (#76, Luka, Chuck, SGA) state the outcome in line 1; #75 (0.615) states a tension. n=21, a guess.
- [ ] [V][Z] Fill `lane`, `fresh`, `music`, `frame1` for every Short in `Experiments.csv` at build time. Most rows have no lane, so the learner cannot rank lanes yet. Needs about 5 per lane.
- [ ] [V][C] Editing: a closer second angle for wide plays (whole-frame shots keep the scorebug but shrink the player); caption position off the players; escalating counter (swishy style). See `Research Notes/Editing Study (Nov 1, 2026).md` section 5.
- [ ] [V][C] FC: goalkeeper lane first (4 of 4 hits). Next scripted but unvoiced: S31 (baby Messi bathed; copy check TAKEN, owner's call), S32 (Hull fan; the 1998 table line needs a second source), S30. One fan/kid experiment, one variable.
- [ ] [V][C] NBA: milestone prebuilds from `Research Notes/Account 2/Milestones.md` (LeBron passes Kidd mid-November; Curry's 5,000th three late December) so the news Short goes out the morning after.
- [ ] [V][Z] S29 footage gaps: no clean ball-throw clip. If a clean FIFA/X clip appears, re-cut with `edit_upgrade.py` style (hook zoom 1.5 on wide shots, scorebug whole, no hold over 3 s).
- [ ] [V][Z] 720p sources are blown up 2.7x (QA warns): prefer 1080p (`height<=1080`) when downloading on the PC, disk permitting.
- [ ] [V][C] Hub and TikTok/Instagram long cut (65-80 s) are in the old routine prompt; the new `CLOUD DAILY RULES.md` omits it. Decide with the owner if the long cut is still wanted.

## Data and learning
- [ ] [Z] Studio "Stayed to watch" exports weekly (owner, Monday) so the 74% line can be checked against more than the 45 Shorts that have API engaged ratio.
- [ ] [Z] Backfill `Experiments.csv` `lane` for the 77 Shorts with no lane (keyword rules in `learn.py`, then spot-check 10).
- [ ] [C] Sunday review: top 3 and bottom 3 by engaged ratio and views, one rule kept, one dropped, one line in the Lessons log.

## Risks to watch
- Two builders (cloud and PC) both building: `BUILDER.txt` and `STATE.md` claims are the only guard.
- A bad DRAFT slipping through the AM/PM timers (option C-lite): check the YouTube "Scheduled" list daily; add `HOLD` to the card; delete in the YouTube app (owner) if needed.
- Copyright claims on match footage: Studio emails are the only signal; three strikes end a channel.
- Upload tokens dying (OAuth app unpublished); preflight shows REJECTED.
- Disk full on C: (27 GB free); a render needs 1-3 GB.
- YouTube policy on repetitive Shorts: stay at 2 NBA + 1 FC a day and rotate lanes.
