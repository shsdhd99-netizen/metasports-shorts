# Posting plan: how many Shorts a day on each channel (Nov 5, 2026)

Owner (Nov 5): "analysis on how much you should post on each channel a day (never over 3, especially not unless spread out)... maybe 2 a day on FC is better; we need to test, alternate new things every day, stick with what works, test what doesn't until it works." Builds on `Posting Cadence Review (Nov 5, 2026).md` (evidence on volume) and `Posting Study (Oct 26, 2026).md`. Tiers: **[V]** measured/official, **[S]** small sample, **[H]** guess.

## 1. What limits the number per day (in order)
1. **Idea quality.** Views are concentrated (NBA top 10 Shorts = 60% of views, FC top 5 = 84%) [V]. A weak extra Short adds almost nothing and can dilute the channel's signal; a strong one is another at-bat at a hit. So volume must follow ideas that pass the gate (`build_gate.py`: gauge 80%+, FRESH, proven lane or a named one-variable test).
2. **Voice credits (the hidden cap).** ElevenLabs plan: 121,224 characters a month; 67,649 left on Nov 5 (resets Nov 18) [V, preflight]. Cost per Short: NBA about 450-600 characters a take, about 0.6-1.2K with a retake; FC 1.3-1.5K characters a take, about 2-3K with retakes [S, Lessons Learned]. At 2 NBA + 1 FC a day: about 2K + 2.4K = 4.4K a day = 130K a month, **which is exactly what the plan pays for. That is the real reason for 2 NBA + 1 FC.** 3 NBA + 2 FC a day would need about 220K a month. [H arithmetic, check against the next preflight]
3. **Build and fact-check time**, which falls once the QA and tooling work lands (`Efficiency Review`).
4. **The feed**: YouTube says there is no daily threshold that unlocks reach; each Short is judged alone on viewed-vs-swiped [V, Sherman]. Volume itself is neither rewarded nor punished; fatigue and dilution are the risks.

## 2. Recommended ceilings (owner rule: never more than 3 a day per channel, 6+ hours apart)
| Channel | Default | Maximum | Slots (ET) | Condition for the extra |
|---|---|---|---|---|
| NBA | 2 | 3 | 7:15 AM, 3:30 PM (+ 9:30 PM for late games) | each passes the gate; the 3rd only for a live same-night moment or star chase |
| FC | 1 now, 2 when supply allows | 3 (not before the proven lane has 3 ready) | 12:00 PM (+ 6:00 PM, + 9:00 AM) | FC 2nd/3rd Short only from a proven lane or a lane test with a logged variable |
Never two posts less than 6 hours apart on one channel; never 3 on a day unless the first two beat the median at 72 h in the previous two weeks. [H, conservative]

## 3. The test (credit-neutral, starts Mon Nov 9, switch: `Research Notes/POSTING_TEST.txt`)
- **Design.** Alternate days: **even dates NBA 2 + FC 1 (today's pattern); odd dates NBA 1 + FC 2** (FC at 12:00 and 18:00 ET). The credit use is the same either way, so the question answered is "where does the next Short earn more views, NBA or FC?" without spending more. `next_gap.py` follows the alternation.
- **Fill rule.** A slot is built only if an idea passes the gate; an empty slot is skipped, and the day counts as run with fewer posts (record it).
- **What to log** (`Research Notes/Test Log.csv`, `Tools/test_log.py`): date, channel, posts that day, lane, the one variable changed, 72 h views, stayed/engaged, lesson.
- **Decision metrics** (read at 72 h, per channel): (a) median 72 h views per post by posts-that-day (1, 2); (b) total views per day; (c) **cannibalization**: the FIRST post's 72 h views on 2-post days vs 1-post days; (d) subs per 1K views; (e) engaged ratio.
- **Sample:** 12 days per arm (24 days, to about Dec 3) detects roughly a 30% difference in median [H]. Read early at 8 days per arm for direction only.
- **Decision rule:** pick the pattern with the higher total views per day where the 2nd post's median is at least 70% of the 1st's and cannibalization is under 20%. If FC 2-post days win, move FC to 2 a day and test 3 only after 2 weeks of clean results. If NBA 1-post days match NBA 2-post days, drop NBA to 1 and give the credits to FC.
- **Then the next test** (after the winner is set): a third slot on the winning channel for 2 weeks; then slot times (7:15 vs 9:00 AM; 12:00 vs 4:00 PM), which the Oct study suggests matter little.
- **Confounders to control:** topic (only gate-passing ideas, same lane mix on both arms), day of week (alternation across weeks balances it), game nights (NBA), big events (World Cup/Euros qualifiers for FC).

## 4. Learning rule alongside the cadence (owner: "stick with what works, test what doesn't until it works")
Each day the plan includes one proven-lane Short and, when a second slot exists, one TEST lane Short that changes ONE variable from its last attempt. `Test and Learn Policy (Nov 5, 2026).md` defines PROVEN / TESTING / RETIRED and the log. Lessons from every failed attempt are written down before the next attempt.

## 5. If more credits are possible (owner decision)
An ElevenLabs plan with more characters (or the cheaper "Flash" model if quality passes, [H] about half the credits per character, verify) would allow 3 NBA + 2 FC a day. Until then, keep the test credit-neutral.
