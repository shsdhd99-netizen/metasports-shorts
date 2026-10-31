# #50 "Embiid Thought He'd Never Dunk Again" — Oct 17, 2026

**Status:** script v1, critic APPROVE 36/45 (just), accuracy PASS. **Not voiced:** voice credits ran out after #49 and #47 (about 1,128 characters left Oct 17; resets Nov 8). Not posted.
**Concept:** a star's own words about his body, then the proof on film. Famous name plus "never".
**Runtime:** 75 words, about 18-20 s.

## Fact check
| # | Claim as voiced | Source (date) | Status |
|---|---|---|---|
| 1 | "I thought I would never dunk again," said Friday | Bleacher Report, Oct 16 2026 https://bleacherreport.com/articles/25512215-joel-embiid-drops-hilarious-quote-after-viral-video-huge-dunk-76ers-preseason-game ; PHLY, Oct 17 2026 https://allphly.com/76ers/sixers-stars-find-their-footing-in-preseason-finale-vs-celtics/ | PASS (both have this sentence) |
| 2 | His left knee held him to 57 games over the last two seasons (19 + 38) | ESPN, May 10 2026: the left knee "cost him all but 19 games last season and helped limit him to 38 games this season" https://www.espn.com/nba/story/_/id/48737189/embiid-feeling-confident-knee-health-going-forward | PASS; "held him to" keeps ESPN's "helped limit" sense, so not every missed game is blamed on the knee |
| 3 | The Sixers' last game before the season; faked the handoff and threw it down | NBA TV on X, Oct 17 2026: "Embiid fakes the handoff and finishes with the slam" https://x.com/NBATV/status/2111258334443470894 ; SixersWire "preseason finale" | PASS |
| 4 | 27 points, the most of anyone on the floor | PHLY: "Embiid led all scorers with 27 points" | PASS |
| 5 | "I guess it's good to dunk." | BR and PHLY both open the quote with it | PASS |

- **Not used (sources disagree):** BR has "I kind of got possessed"; PHLY has "I think my mind kind of changed mid-air" at the same point.
- **"Friday"** must change after about Oct 22.

## Visual plan
**Sources in `src/`:**
- `2111255044074901716` Sixers dunk, 1920x1080, 11 s
- `2111258334443470894` NBA TV dunk, 1080x1080, 6 s (a second angle)
- `2111256451130015899` "23 points in 20 minutes", 540x720 (soft; at most 1 shot)
- `2111260356982997502` "up & over", 1080p (check the player before use)
- `2111273536941674518` NBA "69 points" highlights, 131 s, 1080x1080: Embiid buckets

| Line | Picture |
|---|---|
| "Joel Embiid thought he would never dunk again." | **frame 1:** Embiid in the air, the dunk at its peak (Sixers clip). The claim is contradicted in frame 1, so the viewer asks how |
| "He said it himself, on Friday." | the NBA highlights: Embiid jogging back, face visible |
| "His left knee held him to 57 games over the last two seasons." | Embiid walking, slow; words over footage "57 GAMES · 2 SEASONS" (the one number shown) |
| "Then… he faked the handoff," | NBA TV angle: the handoff fake, real time |
| "went up, and threw it down." | Sixers angle: the dunk, real crowd audio up 2 s (no added effect, since the crowd is the effect) |
| "27 points, the most of anyone on the floor." | 2 different Embiid buckets from the 131 s highlights |
| "So how did he explain the dunk?" | Embiid face (highlights) |
| "'I guess it's good to dunk.'" | replay of the dunk, slowed 0.75x, ends on the rim (loop) |

## Critic (self-review)
| Premise | Hook | Clarity | Progression | Payoff | Voice | Visual | Originality | Retention | Total | Accuracy |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 4 | 5 | 4 | 4 | 4 | 4 | 3 | 4 | **36/45 APPROVE (just)** | PASS |

- The payoff is a dry line, not a twist.
- The middle number line is the soft spot.
- Third Sixers-adjacent Short in a fortnight, so post it after a non-Sixers one.
