# Test scoreboard (Sat Nov 07, 2026)

Auto-written by `python Tools/lab.py score` (daily). Metric: views at 72 h (read on day 5-8: the API runs ~2 days behind). **Score** = chance a B Short beats an A Short (50 = no difference; 70+ = B is winning, 30- = A is winning). A test decides at 6+ per arm with p <= 0.2; at 12 per arm with no winner it closes as NO DIFFERENCE.

| Test | Question | A (control) | B (new) | Score | p | Avg % viewed A / B | Status | Next |
|---|---|---|---|---|---|---|---|---|
| `nba-lists` | Are record lists a hit lane we can repeat? | every other NBA Short: 5,629 (n=49) | 'Who has ___ the most in NBA history?' list: 23,952 (n=3) | 78 | 0.12 | 98% vs 96% | **RUNNING** | needs 3 more (+11 waiting for 72 h) |
| `nba-opener` | Do Why/How/What/Who titles get more views? | title opens on a name or noun: - (n=0) | title opens with Why/How/What/Who: - (n=0) | - | - | - | **RUNNING** | needs 6 more (+2 waiting for 72 h) |
| `nba-cadence` | Does a second post on the same day cost views per post? | a 1-post day: - (n=0) | a 2+-post day: - (n=0) | - | - | - | **RUNNING** | needs 8 more (+2 waiting for 72 h) |
| `fc-premise` | Can a new premise (a star's relative, kept his promise, one-mistake chain, bargain scouting, fans beat the club) match our shootout Shorts? | penalty-shootout Shorts: 24,230 (n=4) | a new non-shootout premise: - (n=0) | - | - | - | **RUNNING** | needs 5 more (+5 waiting for 72 h) |
| `fc-opener` | Does opening on the action keep more viewers than reading the title first? | title-first (the spoken title is line 1): - (n=0) | action-first (the title on screen only; line 1 is the first story sentence): - (n=0) | - | - | - | **RUNNING** | needs 6 more |
| `fc-music` | Does the quiet music bed help? | no music: 1,085 (n=1) | quiet music bed: 3,337 (n=1) | 100 | - | 71% vs 64% | **RUNNING** | needs 5 more (+7 waiting for 72 h) |

## Shorts in each live test

- `nba-lists`: A: Jokic Was Drafted During A Taco Be (-), The NBA Banned Dennis Rodman's Jer (-), His Teammates Talked A Rookie Into (-), This Rookie Told Luka He Sucks 😭 (-), The NBA Legend Who Made Up An Insu (-), The WNBA Minimum Is Now Bigger Tha (-); B: Who Has Missed The Most Shots In N (25,627), Who Has Missed The Most Threes In  (23,952), Who Has Lost The Most Games In NBA (5,607)
- `nba-opener`: A: The NBA Legend Who Made Up An Insu (-), The WNBA Minimum Is Now Bigger Tha (-); B: none yet
- `nba-cadence`: A: The NBA Legend Who Made Up An Insu (-), The WNBA Minimum Is Now Bigger Tha (-); B: none yet
- `fc-premise`: A: Goalkeepers who hid a cheat sheet  (27,637), Goalkeepers who were subbed on jus (20,822), The England subs brought on only f (-), Goalkeepers who took their gloves  (-), The goalkeeper who refused to be s (-), The goalkeeper who says Spain were (-); B: The player who moved two Coca-Cola (-)
- `fc-opener`: A: none yet; B: none yet
- `fc-music`: A: Barcelona Signed Messi On A Paper  (1,085), Goalkeepers who took their gloves  (-), The goalkeeper who only played bec (-), The Ballon d'Or winner who missed  (-), The goalkeeper who says Spain were (-); B: Man United's Penalty Nightmare Is  (3,337), The England subs brought on only f (-), The goalkeeper who refused to be s (-), The player who moved two Coca-Cola (-)

## Queue (starts when a live test of the same channel closes)

- `nba-loop` (nba): Does a natural loop add views (replays count since Mar 2025)?
- `nba-countup` (nba): Do counting numbers on the footage hold viewers better?
- `nba-foreshadow` (nba): Does a foreshadow in line 2 keep viewers to the payoff?
- `nba-countdown` (nba): Is a weekly superstar countdown a hit lane?
- `fc-loop` (fc): Does a natural loop add views on 55 s stories?
- `fc-style-v3` (fc): Do the PureBusiness script moves keep more viewers?

## Decided

- none yet
