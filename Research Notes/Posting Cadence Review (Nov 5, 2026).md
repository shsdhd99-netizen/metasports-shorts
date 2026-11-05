# Why 2 NBA + 1 FC a day, and what to test (Nov 5, 2026)

**Short answer.** It is a rule we inherited, not a proven optimum: `UPLOAD SCHEDULE.md` allows up to 2 Shorts per channel per day (second only if as strong as the first, 6+ hours apart, never 3). In practice NBA often gets 2 because moments are quick to build from fresh games; FC gets 1 because each story needs a new sourced fact, 55-60 s of footage and two voice takes, and the proven premise (goalkeeper oddity) is the bottleneck. [Posting Study (Oct 26) section 1d, Idea Bank]

**What the evidence says.**
- YouTube: no daily-volume threshold unlocks reach (Sherman: "nothing in our systems ... when you hit the five video or 10 short threshold per day"); posting time is not optimized; every Short is judged by its own viewed-vs-swiped on a seed audience. [V, Growth Study]
- Our own data (Oct 26 study): NBA days with 2 posts did as well per post as 1-post days (4.1K vs 4.2K median) [S].
- Refreshed today (Oct 3 onward, public views, mixed shapes): NBA 1-post days median 7.3K (n=12), 2-post days 3.0K per post (n=32), 3+ days 6.1K (n=18). FC 1-post days 2.3K (n=12), 2-post days 15.4K (n=4). **Both are confounded by topic** (the FC hit sock Short went up on a 2-post day; many NBA 2-post days were paused-shape builds), so neither says 2 a day helps or hurts. [S, do not use as proof]
- Risk of 2 a day: a weaker second post can dilute the channel's signal ("coherence" in the feed, Sherman Dec 2024) and uses voice credits and fact-check time. Benefit: more seeds into the feed, and since views per Short are concentrated (top 10 NBA Shorts = 60% of views, top 5 FC = 84%), more at-bats raise the chance of a hit **only if each at-bat is a good one**.

**Can we do 2 a day on both channels?** Yes for NBA when there are two strong moments from the same night; for FC only when two goalkeeper-lane stories exist (not yet: 6 scripts, 3 still needing sources). Two FC Shorts a day with a non-goalkeeper second would repeat the pattern that gave 0 of 8 above 3.2K.

**What to test (one variable each):**
| Test | Design | Decide on |
|---|---|---|
| 1 vs 2 a day, NBA | 4 weeks: alternate days (1 post, 2 posts), same shape mix (approved shapes only), second post 6+ h later, both with gauge 80%+ | per-post 72 h median views, total daily views, and whether the FIRST post's 72 h views drop on 2-post days (cannibalization) |
| 2 a day, FC | only when two goalkeeper-lane stories are ready; 3 pairs | the same three numbers |
| Second-post gap | 6 h vs 9 h | first-post views; likely no effect (Posting Study) |
| Build gate | `Tools/build_gate.py`: build only with an open slot, an unpaused shape, gauge 80%+, FRESH copy-check, no other claim | share of Shorts at 15K+ (target 3 in 10 NBA) |
Minimum sample: about 12 days per arm to see a 30% difference. The test runs only on Shorts that pass the gate, so volume follows quality, not the other way round.

**Rule now (owner, Nov 5):** do not build a Short unless it is currently useful (open slot), the autopilot has not already covered it, or it rates high (gauge 80%+, unpaused shape, FRESH). Skipping is the default. The goal: channels that run themselves with high retention and millions of views.
