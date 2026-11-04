# Topic and Script Reset (Nov 4, 2026)

One page: which topic shapes to build, which to pause, and why. Numbers are public view counts (yt-dlp, Nov 4 afternoon) and the
YouTube Analytics API pull of Nov 4 (subs gained, engaged ratio). Topic shapes were labelled by hand on Nov 4 for every Short since
Oct 3 (`Tools/data/topic_shapes.csv`, read by `Tools/learn.py`, which now prints a "topic shape" row and subs per 1K views in
`Learned Weights.md`). Only Shorts 3+ days old count. **n under 5 is a guess.** Rule: about 70% of builds from shapes above the
median, about 30% experiments that change one thing.

## NBA (MetaSports Clips): era median 6,800 views (n=32 mature)
| Topic shape | n | Median views | vs median | Subs / 1K views | Call |
|---|---|---|---|---|---|
| **family** (Bronny, the Boozers, LeBron vs his son) | 4 | 25,000 | 3.7x | 0.52 | **BUILD** (guess, but every one of the 4 beat the median) |
| **moment** (a watchable thing that happened this week: Bones fake throw 18K, kid free throws 24K, rookie OT hero 10K) | 5 | 7,650 | 1.1x | 0.26 | **BUILD** (typical median, the most recent hits) |
| **superlative / record chase** ("most missed in history" 25K and 23K; LeBron 40 behind Kidd 8.8K) | 9 | 5,600 | 0.8x | 0.36 | KEEP for live chases with a star; drop "did what no one has" trivia |
| rule (why X isn't allowed / banned) | 5 | 3,800 | **0.56x, BELOW** | 0.46 | **PAUSE** (learn.py flag: last 3 under median) |
| **history** (an old story retold: Chuck test 3.4K, Rodman wrestling 3.4K; younger ones Kobe G7 1.4K, Jokic parade 1.2K, Iguodala 0.8K) | 3 mature + 3 young | 3,500 | 0.51x | 0.40 | **PAUSE**: 6 of 6 under the median, all with low engaged ratio |
| news explainer (trades, LeBron's team) | 3 | 4,300 | 0.63x | 0.40 | experiment only |

Exceptions worth one experiment each: the underhand free throw (rule shape, 29K) won because it is a *watchable curiosity about
something players do now* ("Why NBA Players Refuse This Free Throw"); the same topic as a "rule" title (big men underhand, 1.9K) lost.
The channel's older era (Nov 2025 - Feb 2026, 25-80K a Short) was dominated by that shape: "NBA Players Are Doing THIS" 80K,
"Why NBA Players Stopped Shooting Underhand" 73K, "Is It Possible To Dunk Without Jumping?" 55K, "The Most 200 IQ Play" 53K.
**New experiment lane: "watchable curiosity"** (something you can see players do, asked as a why/how question).

**Warning, already scheduled:** Thu 7:15 AM Jokic Taco Bell (history), Thu 3:30 PM Warriors shot-clock first (superlative/history)
and Fri 7:15 AM Rodman No. 69 (rule/history) are all in paused shapes. They stay (scheduled and approved), but expect 1-4K; do not
read their result as a sign the channel is dying. The Fri 3:30 PM gap (built Thu 6:45 AM by the gap-fill) should be a **moment** or
**family** story from Wednesday night's games.

## FC (MetaSports FC): era median 2,500 views (n=13 mature)
| Topic shape | n | Median views | vs median | Subs / 1K views | Call |
|---|---|---|---|---|---|
| **goalkeeper trick** (sock cheat sheet 30K, water bottle 29K, penalty-only subs 23.6K, dancing on the line 15.6K) | 4 | 24,500 | **9.8x** | **1.49** | **BUILD** 70% |
| club story (Loch Ness odds, Messi napkin, Maradona's shirt) | 6 | 2,000 | 0.8x | 1.25 | experiment only |
| manager (stop scoring, sprinklers) | 2 | 2,700 | 1.1x | 0.37 | pause (64-67% viewed) |
Studio (Nov 4 FC export): the first Short of a pattern earns the subs (sock 87 subs; water-bottle sequel 8 at the same views). So each
new goalkeeper Short needs **its own new fact**, not a repeat of cheat sheets or penalty subs. Young ones to judge on Fri: England
penalty subs (5.6K, 1 day), gloves off (2.3K, same day).

## Script rules this adds (no new rules beyond the data)
1. Pick the shape first (table above), then the story. A great history story is still a history story.
2. NBA line 1 names the star or the family link and shows the moment in frame 1 (the family and moment hits all did).
3. FC: every goalkeeper script states, in line 2, what is new this time ("the first keeper to ..."), so it is not a sequel.
4. Re-run `python Tools/learn.py` every Sunday; a shape moves to BUILD or PAUSE only at n>=5.
