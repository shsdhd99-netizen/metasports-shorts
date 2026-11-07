# Script, editing and retention study (Nov 6, 2026, cloud)
Tiers: [V] measured on our channels; [S] small sample or a model's reading; [H] untested idea.

## 1. What decides views on our NBA channel (n=40, `Shorts Dataset.csv` via `shorts_dataset.py --report`)
- **"Stayed to watch" is the lever [V]:** Shorts with 74%+ stayed have a median of **10,436** views, against **2,912** below that (3.6x).
- **The premise beats the edit [V, small n per lane]:**
  - famous-rule paradox: 31.8K (n=1)
  - superstar record/first: 27.0K (n=1)
  - superstar "#42 format": 23.9K (n=3)
  - superstar news-number gap: 23.7K (n=1)
  - star-rookie size curiosity: 21.1K (n=1)
  - rule/policy: 2.0K (n=6), stat: 1.1K (n=2)
- **Titles:** question 5.6K vs statement 3.4K (n=20 each); the stayed % is the same, so this is [S].

## 2. Editing variables vs stayed % (36 NBA Shorts matched to their folders) [S]
| Variable | Split | Stayed % | Median views |
|---|---|---|---|
| Speech pace | <=230 wpm (n=15) / >230 (n=19) | 63.6 / **69.4** | 2,842 / **3,974** |
| Length | <=25 s (n=22) / >25 s (n=12) | 68.0 / 68.9 | **5,618** / 2,848 |
| Shots in first 3 s | <=2 (n=12) / 3+ (n=20) | 66.7 / 67.5 | 2,396 / 3,612 |
| Average shot | <=1.8 s (n=21) / >1.8 s (n=11) | 66.5 / 69.7 | 2,912 / 3,821 |
| First sentence ends | <=2.5 s (n=10) / later (n=24) | 67.3 / 69.6 | 4,324 / 3,368 |
| Face/quote share | <=30% (n=19) / more (n=13) | 66.5 / 71.1 | 2,914 / 2,842 |
| Cards | none (n=20) / some (n=12) | 68.0 / 67.3 | 2,884 / 5,688 |
**Read:** no editing variable moves "stayed" by more than about 3 points, which is inside the noise. The only consistent one is **pace: above 230 wpm** (better on both stayed and views). **Short (25 s or less)** doubles the median views without changing stayed, which suggests loops and replays. Faster cutting (1.8 s or less) did NOT help. This matches the Nov 1 Full Review: the premise and the first 1-3 s decide; the edit doesn't.

## 3. Retention curves (20 NBA Shorts with 800+ views, API `retention` files) [S]
- **The steepest drop is in the first 10% of the runtime for 16 of 20.** But that early loss is the same for hits and flops (about 21-23%).
- **The difference is the back half:** at 90% of the runtime, hits keep a 0.88 audience ratio vs 0.65 for flops; at 50%, relative retention is 0.76 vs 0.64. Hits also start at a higher ratio (1.81 vs 1.62), meaning more replays.
- **So:** (1) the feed decision ("stayed") is made on frame 1 and line 1; (2) inside the video, **the payoff and the loop separate a hit from a flop**. Keep the payoff for the last 2-3 s, hold the payoff number on screen, and end on an image that flows back into frame 1.

## 4. Competitor titles and formulas (528 Shorts, 18 channels, each Short vs its own channel's median) [S]
| Title feature | n | Median vs channel | Share at 3x+ |
|---|---|---|---|
| Starts Why/How/What | 31 | **1.41x** | 26% (vs 19%) |
| "Part N" serial | 35 | 1.03x | **34%** (vs 18%) |
| "X vs Y" | 69 | 1.05x | 25% |
| Question mark | 45 | 1.01x | 9% (fewer breakouts) |
| Opens on a pronoun (He/Bro) | 47 | 0.80x | 15% |
| Superstar name, number, emoji | 102-127 | about 1.0x | 20-24% |
**Read:** title wording is a small factor; we shouldn't tune it. Two exceptions worth testing: **a Why/How/What opener** and **numbered serials** (a recurring format the audience recognises). That fits Ahmed's Goal (Ballon d'Or explainers, 0.8-1.1M) and FOOTY FACTS' serial evidence from Oct 24.

## 5. Formulas to test next (one variable each; log in `Test Log.csv`)
1. **NBA pace:** voice at 240-260 wpm vs the current about 200-230 (two Shorts each).
2. **"Who has ___ the most in NBA history?" record lists** as a numbered serial ("Part 1, 2, 3"): our two lists did 24-25K.
3. **FC serial:** "Goalkeepers who ___, Part N", our proven lane in serial form.
4. **The end hold:** payoff number held 3 s plus a last frame that matches frame 1, vs a hard cut (watch the 90% ratio).
5. **Why/How/What title** vs a statement title on the same lane (2 vs 2).

## 6. Competitor script reports (Gemini) [S]
**Ahmed's Goal, "Why is Harry Kane's Ballon d'Or so special" (1.1M), about 70 s, human voice:**
- Line 1 is the question.
- Then an underdog ladder, one rung every 5-8 s, each with a hard detail:
  - Arsenal let him go at 8-9 for being "too chubby"
  - loaned out four times
  - 31 goals at 21
  - 267 Spurs goals and zero trophies
  - lost two Euro finals
  - mocked online
- The turn: Bayern, 73 goals in a season.
- The payoff is a stack of "firsts": the first English winner in 25 years, the first Bayern winner in 45, the first ceremony held in the UK.
**Ahmed's Goal, "Ballon d'Or ceremonies that caused the rules to be changed" (844K), 69 s, 23 shots, about 165 wpm:**
- The event: Rodri beat Vinicius by 41 points.
- The leak, then the refusal: Real Madrid skipped the whole ceremony.
- The consequence: Perez criticised the voting.
- The rule change: only the editor knew the winner, and Ronaldinho announced it live.
- The current rule is the last line.
- The edit: split screen with the creator on camera; news headlines and meme reactions.
**What we take:**
- (1) The "rejection ladder": every rung is a specific humiliation with a number.
- (2) The payoff as a "first in N years" stack.
- (3) "Club refused to show up" is our "versus their own" lane again.
- Their 69-70 s length breaks our under-60 s rule; keep ours.
The rest pending: the watcher was rate-limited (503s) this morning. Reports land in `Research Notes/Watch Reports/` for Ca6yhOHtqtM (Kane Ballon d'Or 1.1M), WjUwIj9pA5I, JCvmvhCIvSI (Ahmed's Goal), ublC4_USUXs, YGFnYenGxss (Ahmed's Basketball), keHURX3t594 (CoachClank 26M), OSWp_TgFV_M (swishyhoopz). Re-run: `python Tools/yt_watch.py https://www.youtube.com/shorts/<id>`.
