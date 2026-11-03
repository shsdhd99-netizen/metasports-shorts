# Learned Weights (auto-written by Tools/learn.py, 2026-11-03)

Views vs the channel's own median, Shorts 3+ days old only. **n is on every row. n under 5 = guess, do not build a rule on it.**
Ratio 1.0 = typical for the channel. Views are public counts at the date in Experiments.csv, not stayed-to-watch.

## MetaSports (NBA): n=27, median 6,700 views

| Feature | Value | n | Median views | vs channel median | Read |
|---|---|---|---|---|---|
| lane | record42 | 2 | 24,000 | 3.58x | guess (n<5) |
| lane | size | 1 | 9,800 | 1.46x | guess (n<5) |
| lane | the #42 format | 2 | 7,800 | 1.16x | guess (n<5) |
| lane | oddity | 3 | 7,100 | 1.06x | guess (n<5) |
| lane | news | 3 | 5,000 | 0.75x | guess (n<5) |
| lane | news explainer | 1 | 4,300 | 0.64x | guess (n<5) |
| lane | rule | 4 | 3,300 | 0.49x | guess (n<5) |
| lane | record | 1 | 2,600 | 0.39x | guess (n<5) |
| lane | game oddity | 1 | 1,500 | 0.22x | guess (n<5) |
| star in title | star named in title | 18 | 6,750 | 1.01x | typical |
| star in title | no star | 9 | 5,600 | 0.84x | typical |
| title shape | question | 9 | 8,400 | 1.25x | typical |
| title shape | statement | 18 | 5,500 | 0.82x | typical |
| length | 20-30 s | 25 | 6,800 | 1.01x | typical |
| length | 30-45 s | 1 | 4,300 | 0.64x | guess (n<5) |
| length | 45 s + | 1 | 3,400 | 0.51x | guess (n<5) |
| music | no | 18 | 6,150 | 0.92x | typical |
| freshness | evergreen | 6 | 8,450 | 1.26x | typical |
| freshness | fresh | 10 | 5,850 | 0.87x | typical |
| freshness | late news | 2 | 2,650 | 0.40x | guess (n<5) |

## MetaSports FC (soccer): n=10, median 2,800 views

| Feature | Value | n | Median views | vs channel median | Read |
|---|---|---|---|---|---|
| lane | story | 3 | 15,000 | 5.36x | guess (n<5) |
| star in title | star named in title | 1 | 3,200 | 1.14x | guess (n<5) |
| star in title | no star | 9 | 2,500 | 0.89x | typical |
| title shape | statement | 9 | 3,100 | 1.11x | typical |
| title shape | number | 1 | 2,000 | 0.71x | guess (n<5) |
| length | 45 s + | 10 | 2,800 | 1.00x | typical |
| freshness | evergreen | 3 | 15,000 | 5.36x | guess (n<5) |

## One finding in plain English

- No feature has n>=5 and a clear gap yet. Everything above is a guess; keep logging.
- Best lead so far (n=3-4, a GUESS to test, not a rule): MetaSports FC (soccer): lane "story" runs 5.4x the channel median (n=3).

## For daily-run (item 15)
- Lane picks: about 70% from lanes marked ABOVE (or typical with a hit in the last 5), about 30% explicit experiments, one variable at a time.
- A lane flagged PAUSE below is skipped until the Sunday review.
- No lane has 3 flops in a row (lanes are only known for the Oct 21 tracker set; most Shorts have no lane yet, so fill `lane` in Experiments.csv).

Rows with a lane: 43 of 139 mature. Fill `lane` for new Shorts at build time.
