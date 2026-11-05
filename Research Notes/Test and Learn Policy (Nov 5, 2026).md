# Test and learn policy (owner, Nov 5, 2026)

> "You are not limited to goalkeepers on FC. Be willing to try new things and learn from errors. Goalkeeper stories are good, so keep doing them, but see what else works as well. Stick with what works, test what doesn't until it works. Keep getting more efficient. Make sure QA is improved every single day."

## 1. Lanes (topic shapes) have three states
| State | Definition | What we do |
|---|---|---|
| **PROVEN** | at least 4 Shorts with 72 h median at least 1.5x the channel median (`Tools/test_log.py status`) | keep making them: about half of builds |
| **TESTING** | anything else, including new lanes and lanes that failed | every attempt changes ONE variable from the last attempt, is logged before building, and gets a written lesson after 72 h |
| **RETIRED** | 5 attempts with at least 3 different variables changed, all under the channel median | stop, but reopen with a genuinely new idea |
Nothing is banned for ever. FC has no banned shapes. NBA's weak shapes (rule, history, news explainer, off-niche) are TEST lanes: reframe them (for example the underhand free throw won as a "watchable curiosity" but failed as a "rule") rather than skipping them.

## 2. Variables to change (one per attempt)
hook (tension-first vs result-first, action-first vs title-first, foreshadow in line 2), length (18-25 s vs 30-35 s; FC 45 vs 59 s), framing (family/kid angle, redemption, underdog, mistake), footage type (broadcast vs fan footage vs archive vs photo), caption/number style (counting number on the proof), voice pace, title opener ("When...", "the real reason..."), posting slot or posts per day. Never two at once, or the loop learns nothing.

## 3. FC test lanes to rotate (all new unless marked)
fan/kid/family stories (Soccer Topic Study: 1.53x on competitors); player redemption (missed penalty then hero); manager oddities (2 tried, 64-67% viewed: change the hook next); club sagas with a hard number payoff (7 tried, median 2K: change the footage type); records told as a chase; referee/VAR oddities; women's football; transfer oddities; lower-league/cup upsets; stadium/fan rituals; childhood/rags stories; a countdown/game device (the competitors' biggest family). Each lane gets up to 5 attempts with changed variables before a verdict.

## 4. The loop (daily)
1. `python Tools/test_log.py status` and `Tools/idea_triage.py list`.
2. Choose today's proven Short (if the gate allows) and today's test Short; name the variable (`build_gate.py --experiment`).
3. After 72 h: `test_log.py result ...` with views, stayed/engaged and one written lesson (what the data says, not what we hoped).
4. Weekly (Sunday review): lanes whose state changed, the best and worst, one rule kept and one dropped.
5. Autopilot test (owner): terminal/app sessions do not build Shorts; they improve tools, QA and analysis (`Research Notes/AUTOPILOT_TEST.txt`).

## 5. Skipped ideas
Strong ideas (gauge 80%+) that lose their slot stay as CANDIDATES (max 5 per channel, ranked, 14-day shelf life); 60-79 become one-line notes; below 60 are trashed (`Tools/idea_triage.py`).

## 6. QA and efficiency, every day
`Tools/qa_audit.py` ranks the findings that fire most; each day change ONE check (add, tighten, loosen, or move it earlier into `precut_lint.py`) and write it in `Research Notes/QA Changelog.md`. A finding that fires in most Shorts is either noise or a process flaw. `Efficiency Review (Nov 5, 2026).md` lists the larger tooling bets.
