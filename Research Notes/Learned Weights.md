# Learned Weights (auto-written by Tools/learn.py, 2026-11-03)

Views vs the channel's own median, Shorts 3+ days old only. **n is on every row. n under 5 = guess, do not build a rule on it.**
Ratio 1.0 = typical for the channel. Views are public counts at the date in Experiments.csv, not stayed-to-watch.

## MetaSports (NBA): n=27, median 5,897 views

| Feature | Value | n | Median views | vs channel median | Read | Engaged ratio (n) |
|---|---|---|---|---|---|---|
| lane | record42 | 2 | 24,750 | 4.20x | guess (n<5) | 0.591 (2) |
| lane | size | 1 | 9,811 | 1.66x | guess (n<5) | 0.587 (1) |
| lane | the #42 format | 2 | 8,210 | 1.39x | guess (n<5) | 0.514 (2) |
| lane | oddity | 3 | 7,144 | 1.21x | guess (n<5) | 0.563 (3) |
| lane | news | 3 | 4,986 | 0.85x | guess (n<5) | 0.536 (3) |
| lane | news explainer | 1 | 4,308 | 0.73x | guess (n<5) | 0.578 (1) |
| lane | rule | 4 | 3,331 | 0.56x | guess (n<5) | 0.565 (4) |
| lane | record | 1 | 2,670 | 0.45x | guess (n<5) | 0.581 (1) |
| lane | game oddity | 1 | 1,510 | 0.26x | guess (n<5) | 0.533 (1) |
| star in title | star named in title | 18 | 6,666 | 1.13x | typical | 0.561 (18) |
| star in title | no star | 9 | 5,607 | 0.95x | typical | 0.533 (9) |
| title shape | question | 9 | 8,411 | 1.43x | typical | 0.546 (9) |
| title shape | statement | 18 | 5,102 | 0.87x | typical | 0.561 (18) |
| length | 20-30 s | 25 | 6,541 | 1.11x | typical | 0.559 (25) |
| length | 30-45 s | 1 | 4,308 | 0.73x | guess (n<5) | 0.578 (1) |
| length | 45 s + | 1 | 1,085 | 0.18x | guess (n<5) | 0.511 (1) |
| music | no | 18 | 6,074 | 1.03x | typical | 0.561 (18) |
| freshness | evergreen | 6 | 8,478 | 1.44x | typical | 0.575 (6) |
| freshness | fresh | 10 | 5,764 | 0.98x | typical | 0.565 (10) |
| freshness | late news | 2 | 2,666 | 0.45x | guess (n<5) | 0.528 (2) |

## MetaSports FC (soccer): n=10, median 2,400 views

| Feature | Value | n | Median views | vs channel median | Read | Engaged ratio (n) |
|---|---|---|---|---|---|---|
| lane | story | 3 | 15,544 | 6.48x | guess (n<5) | 0.557 (3) |
| star in title | star named in title | 1 | 3,025 | 1.26x | guess (n<5) | 0.604 (1) |
| star in title | no star | 9 | 2,293 | 0.96x | typical | 0.554 (9) |
| title shape | statement | 9 | 2,507 | 1.04x | typical | 0.557 (9) |
| title shape | number | 1 | 2,043 | 0.85x | guess (n<5) | 0.533 (1) |
| length | 45 s + | 10 | 2,400 | 1.00x | typical | 0.556 (10) |
| freshness | evergreen | 3 | 15,544 | 6.48x | guess (n<5) | 0.557 (3) |

## One finding in plain English

- No feature has n>=5 and a clear gap yet. Everything above is a guess; keep logging.
- Best lead so far (n=3-4, a GUESS to test, not a rule): MetaSports FC (soccer): lane "story" runs 6.5x the channel median (n=3).

## For daily-run (item 15)
- Lane picks: about 70% from lanes marked ABOVE (or typical with a hit in the last 5), about 30% explicit experiments, one variable at a time.
- A lane flagged PAUSE below is skipped until the Sunday review.
- No lane has 3 flops in a row (lanes are only known for the Oct 21 tracker set; most Shorts have no lane yet, so fill `lane` in Experiments.csv).

Rows with a lane: 43 of 139 mature. Fill `lane` for new Shorts at build time.
