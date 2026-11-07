# What on the to-do list actually matters, and what we should just wait for (Nov 5, 2026)

Question (owner, leaving Nov 5): "start research on what actually matters on the to-do list, or if we just need to wait." Method: every open item scored on (a) does it change views, subs or retention within 30 days, (b) does it protect against damage or lost money, (c) how long it takes, (d) is anything blocked on data that cannot exist yet. Tiers: **[V]** measured, **[S]** small sample, **[H]** judgement.

## 1. Verdict in four lines
1. **Act on five small things now** (all under 10 minutes, all about damage control): fix S28's title before Fri 12:00 PM ET, delete/hide the old "unknown" S27, pin the comment on the new S27, listen to #95 before Fri 3:30 PM, and send Max the site password.
2. **Everything about growth is a "wait for data" problem.** The tests (lane tests, 1-vs-2-a-day, length, hook) need 72 hours per Short and 8-12 days per arm. The first honest reads are about **Nov 17**, the full read about **Dec 3**. Nothing we change this week can be judged before then, so more changes now add noise, not learning. [H, from the sample sizes in the Posting Plan]
3. **The only growth lever we can pull today is idea quality** (the build gate and test-lane queue), and that is already running through the autopilot.
4. **Most of the long to-do list is housekeeping** (removing old items, archiving shortcuts, optional keys) and can wait or be dropped without changing a single view.

## 2. Item by item
| Item | Moves views/subs? | Protects against loss? | Time | Verdict |
|---|---|---|---|---|
| Fix S28 title (`wN54kSw6Sic`, goes public Fri 12:00 PM) | no | **yes: a public "unknown" title kills that Short's start** | 3 min | **DO NOW** |
| Delete/hide old "unknown" S27 (`6-9L9sJhc1s`) | slightly (duplicate content, wrong title) | **yes** | 2 min | **DO NOW** |
| Pin comment on the new S27 | small (comments help the feed a little) | no | 1 min | do after 2 PM |
| Listen to #95 before Fri 3:30 PM | no | **yes: a flawed scheduled Short** | 1 min | **DO** |
| Send Max the site password | **money** (Max is the only near-term revenue) | no | 1 min | **DO** |
| Ask Max for better photos/audio | **money** (quality of the paid product) | no | 5 min | do this week |
| Studio export (Mon) for both channels | **yes: gives "stayed to watch", the metric YouTube uses** | no | 5 min | do Monday; the first export after Nov 9 starts the test baseline |
| NBA Studio sign-in | yes (same metric, for NBA) | no | 5 min | do with the Monday export |
| Check FC S26 average % viewed (Sat/Sun) | settles the repetition question | no | 2 min | do Sat/Sun; waits on the API lag (2 days) |
| Friend-price decision for Max | money | no | 2 min | **DO** (it blocks Max) |
| Cloud keys (6 YouTube values) | no: the PC autopilot already runs everything | slightly (redundancy) | 10 min | **WAIT / skip** unless the PC is off often |
| Bigger ElevenLabs plan | only if the posting test shows more posts win | no | 5 min | **WAIT** until the Nov 17 read |
| Cancel Dreamina before Dec 3 | no | $15 | 2 min | do the week of Nov 23 (reminder exists) |
| Warriors-Heat result for #97 | no (autopilot will decide through the gate) | no | 1 min | optional |
| Remove old "waiting NBA Shorts", archive old shortcuts | no | no | 5 min | **drop/ignore** |
| Direction decision (case studies) | no (policy is already set and running) | no | 20 min | **WAIT**; reading is optional |
| TikTok/Instagram 60 s cut | no (need 10K followers) | no | - | **WAIT** |
| `--require-approved` scheduling | no | maybe (stops unreviewed uploads) | 1 min | optional; the title incident shows a human check on titles is worth it, see 4 |
| #96 Porzingis | no | risk (health topic) | - | **skip** (gate says no until footage and angle are clear) |

## 3. Why waiting is correct for growth [S/H]
- A Short's fate is mostly decided in its first 72 hours, and the API lags 1-2 days; reading earlier is noise (#48 had 25 views on day 0 and 14.6K on day 2). [V, Posting Study]
- Our measured spread is huge (NBA median 7K, top 10 Shorts = 60% of views; FC top 5 = 84%), so with n of 3-4 per arm nothing is distinguishable from luck. A 30% difference in medians needs about 12 posts per arm. [H]
- The channels are young (FC 15 days, NBA restarted Oct 3) and growing without any change (NBA 7-day average up 60% in a month), so before/after comparisons would credit our changes for natural growth.
- **Changing the plan every few days destroys the experiment.** The plan (gate, test lanes, alternating cadence) is set; let it run to Nov 17.

## 4. What the "unknown" incident says about the to-do list
A single silent bug (an empty title) cost more than any item on the growth list could add this week. That says: **spend the waiting time on guardrails, not on building more**. Done today: title parse fix, placeholder-title refusal, read-back check, `title_audit.py` in the health page. Next guardrails worth building (autopilot test is on, so tools only): (1) a pre-upload checklist printout for the owner (title, tags, slot, QA line) so a human sees it; (2) a post-scheduling title/tags audit every morning (done: `state.py`); (3) a refusal when two uploads of the same story are within 24 hours.

## 5. What to do during the wait (all tool/analysis work, no builds)
1. Daily: `python Tools/state.py`, one QA change (`QA Changelog.md`), `title_audit.py`.
2. Build the efficiency bets that save the most per Short (jersey/face check, one-command `build_short.py`).
3. Prepare the test-lane queue (below) so the autopilot has vetted premises ready.
4. Watch the replacement S27 (`Research Notes/Replacement S27 Check.md`, a background log every 30 minutes today).

## 6. FC test lanes: what the competitor data says (4,884 Shorts, `Soccer Topic Study (Nov 1, 2026)/classified.tsv`, re-cut Nov 5)
Median view vs each channel's own median, and the share of Shorts that reach 2x or more (the hit rate):
| Lane | n | median | hit rate (2x+) | read |
|---|---|---|---|---|
| goalkeeper (our proven lane) | 87 | 1.30 | 34% | confirmed |
| tactics / analysis / stats | 156 | 1.23 | 33% | works for analysis channels; test a "stat device" version |
| family / WAGs | 124 | 1.11 | 34% | the biggest untested lane with a real hit rate |
| fan / kid story | 156 | 0.94 | 31% | median is flat, but the HIT RATE is high: outliers carry it |
| manager / coach | 379 | 1.07 | 26% | we tried 2 (64-67% viewed): change the hook, not the lane |
| conflict / revenge | 386 | 1.03 | 25% | average |
| underdog / rise | 272 | 0.95 | 24% | weak |
| record / number | 253 | 0.97 | 22% | weak |
| referee / rules / VAR | 128 | 0.96 | 23% | weak |
| awards, club names, "names a star" | many | 0.96-1.00 | 19-25% | star or club names do not help |
**Reading [S]:** apart from goalkeepers, no lane has a clearly higher median; what differs is the hit rate. So the plan is not "find another lane that always works", it is to **test premises, not topics**. The top non-goalkeeper outliers share patterns we can copy as premises, not as stolen stories:
- **A famous person's relative with a twist** (Haaland's dad's career-ending foul 91x; Yamal's little brother as Spain's mascot 51x; Tevez's lesson to his daughter 28x).
- **Fans beat the club** ("fans force team to change the kit" 45x; fans' message to Iran at the World Cup 23x).
- **A banned or forbidden thing you can see** ("skills FIFA bans as insults" 56x).
- **A rejected player's revenge** (World Cup players rejected by their own country 23x).
**First five test premises to queue (each must pass the gate and a copy-check, one variable changed per attempt):** (1) a star's relative with an odd football twist; (2) fans vs a club decision; (3) a banned skill or rule you can show; (4) a rejected-then-revenge World Cup story; (5) a stat device (one number that reframes a match). Order by gauge score; keep goalkeeper stories about half of builds.

## 7. Decision calendar (what we are waiting for)
| Date | Read | Decision |
|---|---|---|
| Fri Nov 6 | S28 title fixed? #95 live | none |
| Sat-Sun Nov 7-8 | S26 average % viewed (API) | repetition hypothesis alive/dead |
| Mon Nov 9 | Studio exports; posting test starts | baseline |
| ~Nov 17 | first read of the alternating 1-vs-2 test (about 8 days per arm), lane tests so far | continue, or move credits; ElevenLabs plan decision |
| Nov 18 | credits reset | |
| ~Dec 3 | full read (about 12 days per arm) | set posts per day per channel; try a third slot |
| Dec 3 | Dreamina renewal | cancel if not needed |
| Jan 31, 2027 | accept YouTube's new partner terms | |
