# Proposed edits to the autopilot skill (`.claude/skills/daily-run/SKILL.md`), Nov 6, 2026
Not applied yet: waiting for the owner's OK. The PC runs this file too.

## Problems found
1. **It's 243 lines of dated layers** (Oct 24, Oct 26, Nov 1, Nov 3, Nov 4, Nov 5 overrides) that contradict each other, so each run spends time working out which rule wins:
   - "Never publish, schedule..." vs "MODE B: schedule every Short that passes QA".
   - "TikTok PAUSED (Oct 26)" vs "TikTok RESUMED (Nov 3)", in two places.
   - "goalkeeper every other day" vs "2 of every 3 posts" vs the Nov 5 "FC is NOT limited to goalkeeper stories".
   - Run times "3:17 / 4:23 AM ET, slot 7-8 AM" vs the real triggers (4:42 / 5:40 AM ET) and the 7:15 / 3:30 / 12:00 slot grid.
2. **Wrong budget:** it says "100K credits a month, about 2 Shorts a day"; the plan is 121,224 (resets the 19th), about 3 a day.
3. **The cloud build runs are mostly no-ops** (3 of the last 4 skipped: the PC owns the slot, or the queue is full), and the cloud can't download YouTube footage. They burn a session and decide nothing.
4. **No rule for paid-for drafts** (the owner's Nov 6 rule: if it already used credits, it goes out unless it would do terribly).
5. **No slot roles**, so the fresh moment and the evergreen filler compete for the same slot.
6. **The retention evidence isn't in the gates.** "Stayed 74%+" is the 3.6x lever; the 90%-of-runtime hold separates hits; editing variables don't.

## Proposed new shape (about 80 lines)
1. **Current rules, one page, no dates.** Never post outside the scheduler's guard rails; no keys; sources; under 60 s; slots 7:15 AM (planned) / 3:30 PM (last night's moment) / 12 PM FC; credits from the API (`/v1/user/subscription`), not a fixed number.
2. **Who builds what.** PC: anything needing YouTube footage and all renders. Cloud: research, copy-checks, scripts, source tables, cuts plans from ESPN/archive.org, and NBA moment builds from ESPN clips only when the PC is offline (check `BUILDER.txt` and today's Daily Log).
3. **Decision order each run:**
   - (a) a paid-for draft waiting? Slot it.
   - (b) a gap in the next 54 h? Fill it with the highest-scoring fresh idea (score card from the Two-Week Plan).
   - (c) no gap? Prep the next 2 (script + sources) and stop. One log line.
4. **Gates that matter:**
   - Premise from a proven lane (or a one-variable test).
   - Frame 1 shows the promise.
   - Pace 230-260 wpm.
   - Payoff in the last 2-3 s, held on screen, with a loop frame.
   - NBA moments go up within 20 h of the game.
5. **Learn step:** judge at 72 h on stayed %, the 90% hold ratio and views vs the channel's last 10. One lesson, tiered.
6. **Move every dated override into `Research Notes/Rule History.md`**, so the history is kept but not re-read every run.
7. **Trigger prompts:** shorten the 4 scheduled prompts to "run /daily-run nba|fc" (their text is out of date: "cross-posting paused", "8-9 AM FC slot"). This needs the session that owns the triggers.
