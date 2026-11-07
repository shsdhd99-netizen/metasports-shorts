# PC handoff, Sat Nov 7, 2026 (written by CLOUD at 10:30 PM ET Fri)
Read with `HANDOFF - latest.md`, `TEAM HANDOFF.md` and `TEAM BOARD.md`. Labels: A1 = Builder, A3 = Prep + Review (own repo copy), CLOUD = the app.
Start: `bash Tools/claude_acct.sh 1` (A1) in one Git Bash window and `bash Tools/claude_acct.sh 3` (A3) in a second. They run side by side; never run A1 and A2 together.

## What changed overnight (read first)
- **Fixed a bug (CLOUD, pushed):** `queue_rank.py` and `schedule_ready.py` offered Shorts that were **already live** (posted by hand, so missing from Scheduled Uploads.csv): #78 Rodman wrestling, #77 Bronny, #80 Warriors score (= #90), S16, S17, S18, Boozer. Both tools now check the newest API daily files of both channels and refuse a title that matches a live video. **Those five "HOLD" Shorts are live: don't fix them.** Their cards now start with "LIVE ON YOUTUBE".
- #92 went out Fri 7:30 PM (scheduler), so **#79 Two Buzzer-Beaters moved to Sun 7:15 AM** (built; arm = real audio, no music; QA PASS line present).
- S30 Kane went out Fri 7:30 PM, so **Mon 12 PM FC is open: S21 Higuita goes there.**

## A1 (Builder): in this order
1. [ ] **#98 Klay blocked Steph in his return**, for **Sat 7:15 AM ET** (deadline: uploaded by about 5 AM). Sources are in its notes.md (AP x2 + NBA.com); clip at `src/espn.mp4` (block at 16.5-18.0 s). 22-25 s, 240-260 wpm, payoff held at the end, real-audio version if the call works. Then `qa_final.py` must say SHIP, then `schedule_ready.py` dry run, then `--go`. If it can't make 7:15, use Sat 3:30 PM.
2. [ ] **Sat 3:30 PM NBA:** the CLOUD research run (3:43 AM ET) names Friday night's best moment in `Research Notes/Daily Research/2026-11-07.md`. The 6:45 AM gap-fill builds it. Skip the slot if nothing rates 10+.
3. [ ] **S21 Higuita** (Style v3 test) for **Mon Nov 9, 12 PM ET**. If it runs under 50 s, add back the one sourced line named in notes.md.
4. [ ] **Check the Sun 7:15 AM upload** of #79 happens at the 6:30 PM Sat scheduler run (`Research Notes/Schedule Ready Log.md`).
5. [ ] After each build: `python Tools/team.py done "<task>: <folder>"` and `python Tools/team.py say A3 "DRAFT pushed: <folder>, please review"`.

## A3 (Prep + Review): background, while you work
1. [ ] **Review** #98 Klay as soon as A1 pushes it (REVIEW.md: GO/FIX), then S21.
2. [ ] **72-h judgments due:** #86 Kobe and #88 Iguodala (posted Nov 4), then #89 Taco Bell and #90 Warriors (Nov 5) on Sunday. `test_log.py result` + one lesson each.
3. [ ] **Prep, soonest slot first** (`PREP: ready to voice` + sources + footage plan):
   - NBA List 1 "Who has missed the most free throws in NBA history?" (Mon 7:15 AM; Basketball-Reference FTA minus FT);
   - FC keeper: Bounou and Spain's 2022 shootout (Tue 12 PM);
   - S41 "The goalkeeper who only became a legend because Arsenal's keeper got hurt" (Leno -> Emi Martinez; could replace S36);
   - N1 "Steph Curry's bad ankles are why the Warriors got Kevin Durant";
   - S39 Leicester bargains;
   - cuts plans for S22 Ceni and S31.
4. [ ] **Research Requests (PC ask):** add the two-source premises for Sunday night to `Research Notes/Research Requests (Nov 6, 2026).md`, with at least one FC premise rated 10+.

## Background jobs (zero voice credits; start them in a spare Git Bash window and leave them running)
```
cd ~/Documents/metasports-shorts
python Tools/watch_study.py --channels @PureBusinesshorts --name PureBusiness --top 6 --bottom 6
for id in -XSMRt6rlUE 9xsDtud2YSU XYy8PewUmUw XfleAlOhhEc keHURX3t594 YGFnYenGxss OSWp_TgFV_M; do python Tools/yt_watch.py "https://www.youtube.com/shorts/$id"; done
python Tools/shorts_dataset.py --report > "Research Notes/Shorts Dataset report (Nov 7).txt"
python Tools/learn.py ingest --fetch && python Tools/learn.py report
```
What they are:
- **The PureBusiness top-vs-bottom study:** the cloud run hit Gemini 503s; cached reports are reused.
- **Breakout watches** (from the vidIQ sweeps): Mbappe "kept his promise" 16M, Declan Rice promise 12.8M, "Tim Duncan was almost a Magic" 3.6M, AwayDays butterfly effects, CoachClank 26M, Ahmed's Basketball "scores that look fake", swishyhoopz Klay.
- Refreshes of the dataset and the learning weights.
When done: `git add "Research Notes/Watch Reports" "Research Notes/Watch Study" ...` (paths only), commit, push, and `python Tools/team.py say CLOUD "background jobs done"`.

## Answers to the PC's asks (Nov 6 evening)
- **daily-run rewrite:** reads cleanly from the cloud. Every tool it names exists, `queue_rank.py` and `preflight` run here, and preflight is **OK**: the cloud has the YouTube keys now, so the "BLOCKED" note is out of date.
- **Research Requests:** assigned to A3 (above).
- **Style tests:** agreed, one variable per Short. Add from tonight's reviews:
  - the loop ending (unfinished last line into line 1), as a 2-vs-2 test only;
  - superstar countdowns (TikTok review);
  - "almost / one decision" stories.
