# Weekly review, week ending Fri Nov 06, 2026 (auto-written by Tools/weekly_review.py)

## NBA (data: daily 2026-11-05.csv)
18 Shorts aged 3-14 days; median views 7,434.
| | Short | age | views | avg % viewed | engaged | subs |
|---|---|---|---|---|---|---|
| top | Why NBA Players Refuse This Free Throw 😳 | 4 d | 29,241 | 119% | 0.52 | 13 |
| top | Bronny Is Shooting 100% This Season 😭 #nba | 6 d | 28,504 | 94% | 0.57 | 11 |
| top | Cameron Boozer Outshot His Dad's Whole Career 😳 #nba | 5 d | 27,231 | 117% | 0.55 | 13 |
| bottom | Caitlin Clark Did What No NBA Player Has 😳 #wnba #caitlincla | 11 d | 2,758 | 77% | 0.58 | 1 |
| bottom | All Three Williamses Got A Technical 😳 #nba | 14 d | 1,519 | 88% | 0.53 | 1 |
| bottom | Luka Just Did What Kobe Never Did 😳 #nba | 10 d | 1,336 | 153% | 0.49 | 0 |

Views per day: 7-day 23,851 vs prior 28 days 11,452 (+108%). Last 90 days 488,299 Shorts views = 4.9% of the 10M line, 16.3% of the 3M line. Subs +176 in 28 days (6.3/day): about 58 days to 1,000 at this pace (data to 2026-11-02).

## FC (data: daily 2026-11-06.csv)
13 Shorts aged 3-14 days; median views 3,113.
| | Short | age | views | avg % viewed | engaged | subs |
|---|---|---|---|---|---|---|
| top | Goalkeepers who hid a cheat sheet on their water bottle | 11 d | 29,205 | 96% | 0.55 | 8 |
| top | Goalkeepers who were subbed on just for the penalties #footb | 7 d | 23,544 | 87% | 0.62 | 36 |
| top | Goalkeepers who danced on the line to win a final | 14 d | 15,553 | 83% | 0.61 | 11 |
| bottom | Players who got sent off in their very last game | 12 d | 1,965 | 72% | 0.60 | 0 |
| bottom | Barcelona paid a fortune for the player who knocked them out | 9 d | 1,146 | 68% | 0.56 | 3 |
| bottom | Barcelona Signed Messi On A Paper Napkin | 4 d | 1,012 | 71% | 0.48 | 0 |

Views per day: 7-day 9,565 vs prior 28 days 9,290 (+3%). Last 90 days 120,771 Shorts views = 1.2% of the 10M line, 4.0% of the 3M line. Subs +162 in 28 days (5.8/day): about 147 days to 1,000 at this pace (data to 2026-11-02).

## Lane states (Test Log)
```
== nba (channel median 6,800)
  business               attempts  4  median    3422  TESTING   last variable: unknown (history before the log)
  family                 attempts  8  median    8791  TESTING   last variable: unknown (history before the log)
  history                attempts  8  median    2416  TESTING   last variable: unknown (history before the log)
  moment                 attempts  6  median    9255  TESTING   last variable: unknown (history before the log)
  news                   attempts  4  median    3818  TESTING   last variable: unknown (history before the log)
  oddity                 attempts  4  median    4494  TESTING   last variable: unknown (history before the log)
  rule                   attempts 13  median    2842  TESTING   last variable: unknown (history before the log)
  size                   attempts  2  median   15932  TESTING   last variable: unknown (history before the log)
  superlative            attempts 13  median    2758  TESTING   last variable: unknown (history before the log)
== fc (channel median 2,500)
  club story             attempts  7  median    1965  TESTING   last variable: unknown (history before the log)
  goalkeeper trick       attempts  6  median   18186  PROVEN    last variable: unknown (history before the log)
  manager                attempts  2  median    2687  TESTING   last variable: unknown (history before the log)
  player record          attempts  1  median    2051  TESTING   last variable: unknown (history before the log)
```

## QA: most frequent findings (QA Audit.md)
| warn | footage: shot # <clip>: blown up #x (#x#, crop zoom #): archive footage, accepted in the story format (Ahmed's Shorts use soft #p archive); keep faces | 180 | 5 | recurrin
| warn | footage: shot # <clip>: blown up #x (#x#, crop zoom #; house standard is a #p source, about #x): note in PACKAGE.md that no better source exists | 157 | 9 | noise or proce
| warn | footage: shot # <clip>: soft (edge contrast # vs this Short's median #): motion blur or a poor encode | 52 | 9 | noise or process flaw: fires in most Shorts |
| warn | export: the export says what the script says (#% word match after number folding); # difference(s) to listen for (speech-to-text mishears names): hear | 16 | 10 | noise or
| warn | hook has no number or conflict/question word in the first # words: '..' (state the question the viewer needs answered by # s) | 14 | 8 | noise or process flaw: fires in mo

## Autopilot slots this week (Daily Log AUTO lines)
(no AUTO lines yet)

## Candidates waiting (Idea Candidates.md)
- **92%** Klay blocked Steph in his return (#98, Sat 7:15 AM) [moment] (2026-11-06) Productions/MetaSports/2026-11-07 98/notes.md
- **83%** List 1: who has missed the most free throws in NBA history (Mon 7:15 AM) [superlative] (2026-11-06) Basketball-Reference career leaders
- **83%** Curry passes DeRozan (16th all-time scoring), when it happens [superlative] (2026-11-06) 
- **83%** LeBron passes Kidd for 3rd all-time assists, when it happens [superlative] (2026-11-06) 
- **83%** Lendeborg Part 3 after a 30+ game [family] (2026-11-06) 

## Suggested for the owner to confirm [H]
- KEEP one rule: the one the top-3 Shorts above share (read the top rows: premise, length, hook).
- DROP one rule: the one the bottom-3 share, if it appears in 2 of 3.
- Check the Monday Studio export for stayed-to-watch and put the exact numbers in `Outcome Log.md`.
