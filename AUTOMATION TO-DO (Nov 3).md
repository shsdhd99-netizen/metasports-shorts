# Full automation: honest read + to-do list (Tue Nov 3, 2026, 4 PM ET)

Written for the owner (phone-friendly). Either Claude account can pick up any line tagged for it. Tags:
**[YOU]** only you can do it · **[A1]** main account · **[A2]** second account · **[PC]** plain script, no Claude credits.

## 1. Honest read: can it go viral as it stands?

**Not reliably. The machine works; the aim is the problem.** What the numbers say (Outcome Log, Nov 1 to 3):

- NBA median was about 4-6K a Short through Oct 30 (now rising, see the correction below), with a 20K+ hit roughly 1 post in 10.
  Soccer: only the goalkeeper lane hits (S01 30K, S05 28K, S17 19K); every other lane is 1-3K.
- **Topic decides hits more than editing does.** The 171 Gemini reports show a channel's top and bottom Shorts are edited almost
  identically (3.77 vs 3.73 shots per 10 s). Our hits were topics (Bronny, Boozer/LeBron family story, CoachClank's 10M free-throw
  topic, goalkeepers). So the biggest lever is *which story we pick*, then the first 3 seconds, then polish.
- The retention flags (engaged ratio under 0.5) are on #76, Luka, Chuck and SGA: the openings lose people, not the middle.
- Editing still has real faults to fix (Editing Study Nov 1): subject too small in the first frame, the same shot held for 8 s,
  scorebug cut in half, captions sitting on the players, a static last 4 s. These raise the floor; they won't make a 100K by themselves.
- **CORRECTION (Nov 3, 5 PM, after pulling 31 newer commits):** the numbers above were from a stale local checkout. The cloud runs
  kept going; the Nov 2 stats check says **last-7 median 16,250 (up), three Shorts at 26-28K, S17 22.5K**. So the trend is better
  than "flat at 4-6K". The conclusion (topic decides hits; learn from data) stands.
- **The real blocker:** the Nov 2 container reset wiped the voice and Gemini keys, so the Nov 3 NBA and FC builds were skipped
  ("no voice key"). Fix: add the keys to the cloud environment settings (they survive resets), or build on the PC, where `Tools/.env`
  has them. Main account usage is **96%, resets Wed Nov 4, 1 PM ET**. Nov 3-5 slots are already scheduled on YouTube.
  See `Research Notes/Automation Options (Nov 3, 2026).md` (recommends option B now, C after two clean weeks; one builder only).

## 2. Can it learn as it automates? Yes, if learning is a script, not a mood

Today the "learn" step is prose notes a Claude run reads and interprets (daily-run section B). That's slow and forgets. The fix is a
closed loop that costs almost no credits:

1. **Log every Short with its features at build time** (lane, topic type, hook type, length, voice, music / real audio, caption
   style, number of shots in the first 3 s) into `Research Notes/Experiments.csv`.
2. **[PC] 72 hours after posting**, a script pulls views and engaged ratio (`Tools/yt_analytics.py`, already works) and writes the
   result next to the features. Never judge at day 0 (#48 had 25 views on day 0 and 14.6K on day 2).
3. **[PC] `Tools/learn.py` (to build):** compares each feature value to the channel median and writes `Research Notes/Learned Weights.md`:
   "lane X is 3.2x median (n=5)", "opening type Y is 0.6x (n=4)". It prints n every time and marks anything under n=5 as a guess.
4. **Daily research obeys the weights:** about 70% of builds from lanes that beat the median, about 30% explicit experiments.
   A lane with 3 flops in a row is paused. A hit gets 3 follow-ups in the same lane (series) while it is hot.
5. **Weekly:** Claude reads the weights, retires any rule in the Playbook that the data contradicts, and writes one line to the Lessons log.

Rule of thumb for the whole system: **anything that isn't judgment becomes a plain script on the PC** (analytics, scoring,
scheduling ready drafts, logging). Claude credits go only to research, scripting and picking. That also makes the account
switch painless, because the state lives in the repo, not in a session.

## 3. To-do list to finish automation today

Ordered. Do the top of each tag first. "Done when" is the check.

### [YOU] (about 15 minutes total)
1. **Check account 2's usage** (Settings, Usage) and tell me the weekly %. I can't see it from here. Under 50%, account 2 runs
   everything in section [A2] today; otherwise only the [PC] items run until Wed 1 PM.
2. **Confirm the cloud environment has the repo and `ELEVENLABS_API_KEY`** (Nov 1 handoff said both were still missing). With them, the
   morning runs stop depending on one open session. Done when a run's push no longer gets a 403.
3. **Wed 1 PM ET:** after the main account resets, open it and say "resume daily runs". Nothing else needed.
4. **Monday only:** the two YouTube Studio exports (Shorts tab) for "Stayed to watch". Still manual; Studio has no API for it.

### [PC] no Claude credits, can start now
5. **Daily analytics pull on a timer. DONE:** the Windows task "MetaSports analytics" runs `Tools\daily_analytics.bat` daily at
   3:20 AM and commits (last commit Nov 2 3:20). Only check that it still fires tomorrow.
6. **Auto-schedule ready drafts on a timer.** `Tools/yt_schedule.py` works (tokens are in `Tools/.env`; Nov 3-5 are already scheduled).
   Done when any DRAFT with a passing QA line and an UPLOAD.md gets scheduled by script, with the guard rails unchanged.
7. **Usage guard at the top of every run.** If weekly usage is over 90%, the run writes one "skipped, low usage" line and does only
   the zero-credit steps, instead of dying mid-build. Done when a run at 96% exits cleanly.

### [A2] fresh credits, run today (branch `account2`; read `ACCOUNT 2 - START HERE.md` first)
8. **Build `Tools/learn.py` + `Experiments.csv`** (section 2, steps 1 and 3). Backfill from `Research Notes/Posted Tracker`,
   `Outcome Log.md` and the 221 watch reports. Done when `Learned Weights.md` exists with n shown on every row and one real
   finding I can read in plain English.
9. **Finish the soccer research** (FC is on hold until it's done): ranked topics by outperformance, 20 sourced stories,
   Soccer Playbook v2, then update the soccer build skill. Files are half-written in `Research Notes/Soccer Topic Study` and
   `Soccer Script Craft`. Done when FC Playbook v2 says "goalkeeper lane first, others only as flagged experiments" or whatever the data says.
10. **Hook rebuild for the openings that lose people.** Take #76, Luka, Chuck, SGA (engaged under 0.5), compare their first 5 s
    to #75 (0.615) and #77, and write the opening rule that follows. Done when `Playbook` THE RULES has one tested opening rule
    and `script_lint.py` flags the failing pattern.
11. **Implement the top 2-4 Editing Study fixes as opt-in `assemble.py` features** (bigger subject in frame 1, no repeated shot for
    more than 3 s, scorebug kept whole, caption position off the players). Done when a `DEMO - editing upgrade` re-cut of #73
    passes `qa_short.py --full`. Never swap it onto a live Short.
12. **Pre-build 6 Shorts** from the new weights, 3 per channel, as drafts. Done when each has the full "built" file set and a line
    in `Research Notes/Account 2/Queue.md`. Voice only if credits allow (the check is in the account 2 doc).

### [A1] after Wed 1 PM reset (resumes the machine)
13. **Merge `account2`**, then run the NBA and FC daily runs under the new weights. Done when a Short builds with no 403 and no
    manual rescue.
14. **Revise S20, S09, S19** against FC Playbook v2 (S20 has a voice and a 31-shot plan but isn't rendered).
15. **Switch on the 70/30 rule in daily-run** and add the pause-after-3-flops rule. Done when the skill reads
    `Learned Weights.md` before it picks a topic.
16. **First weekly review** (Sunday): read the weights, delete any rule the data contradicts, one line in Lessons.

## 4. What I'd rather not promise

- **100K is a topic problem.** Weights will raise the *average*; a 100K comes from a story that hits an existing argument, and we
  get there by taking more well-aimed shots, not by finding a secret edit. Expect the median to climb first.
- **n is small.** About 85 Shorts total, mixed lanes. Early weights are guesses until each lane has 5+ posts; the log says so.
- **Don't change two things at once.** Change one variable per test (hook type, or music, or length), or the loop learns nothing.

## 5. Standing rules that don't change

Drafts only for anything outside the scheduler's guard rails; no keys in chat or git; no stat without a source; no promo
outro; Shorts under 59.5 s; never delete and re-upload a Short; at most 2 posts a day per channel, 6+ hours apart.
