# Opening night deep dive (games of Oct 20, 2026; read Oct 21, 14:00-16:00 UTC)

Owner's ask: "do a deep dive on the best/biggest stories of last night, then make 2 shorts for the best stories."

**How stories were ranked:**
- Reach on X: likes and replies on the main post of each moment, read with the syndication API.
- What the big outlets led with: CBS overreactions, CBS grades, NBA.com takeaways, SI, IBTimes, ClutchPoints.
- Whether YouTube already has it: `copy_check.py`.
- vidIQ was out of credits after one call. That call's NBA Shorts trend list from Oct 20 had no opening-night moment in its top 40 yet.

## Results
| Game | Final | Key lines (ESPN box) |
|---|---|---|
| Celtics at Pistons | DET 121-113 | Paul George 38 (most in a Celtics debut); Pistons came back from 22 down with a 23-0 run; Tatum 6-for-23 |
| 76ers at Knicks | PHI 106-100 | Maxey 28, Brown 19, LeBron 14-9-7, Embiid 13 on 4-15; Brunson 21 on 6-19. The Knicks raised their first banner in 53 years before tip-off. |
| Thunder at Spurs | OKC 116-104 | SGA 32; McCain 20 on 7-9; Wembanyama 12 points on 1-13, with 13 rebounds and 6 blocks. Fox flagrant 1; four technicals. |

## The stories, ranked
| # | Story | Reach (main post) | YouTube | Our Short |
|---|---|---|---|---|
| 1 | LeBron's Sixers debut at MSG on ring night | NBA arrival 9,047 likes; chalk toss 9,634; postgame 6,803 | FRESH | #62 (the chant + Rich Paul) |
| 2 | Fox throws Chet to the floor; scuffle; Wemby and all three Williamses get technicals | BrickCenter 5,413; Hoop Central 4,298 | CROWDED (old Vassell-Chet clip) | #63 |
| 3 | Paul George's 38-point Celtics debut, still a loss | ESPN 3,717 | TAKEN | #61 |
| 4 | **Wemby's worst shooting night of his career (1-13)** | Legion Hoops 2,725 likes / 130 replies; CBS led its overreactions with it | FRESH | **#64 (new)** |
| 5 | **LeBron answers a Knicks fan ("I'm from Ohio, baby")** | BrickCenter 2,764 likes / **244 replies** (most replies of any post checked); ClutchPoints, IBTimes | FRESH | **#65 (new)** |
| 6 | "We don't want you" chant at LeBron | Barstool 1,747 | CROWDED (tiny posts) | in #62 |
| 7 | Pistons' 23-0 run vs the Celtics | in recaps | FRESH | in #61 |
| 8 | SGA 32 and MVP talk; McCain 20 on 7-9 | NBC overreactions headline | McCain CROWDED | not made |
| 9 | Silver: LeBron's Fanatics helicopter "perfectly appropriate" (Pablo Torre looking into it) | CBS story | not checked | not made (a cap technicality, which fails our premise test) |
| 10 | Dylan Harper left with an apparent ankle injury | SleeperSpurs 4 likes | | not made (no update found) |

## Why these two
- **#64, Wemby's 1-for-13:** a record story about the biggest young star, and it fits THE #42 FORMAT: an accusation, the count, the paradox ("the first unanimous DPOY ever"), the old record and the flip. The career-low claim was checked against every one of his ESPN game logs. On 10+ shots, his next-worst game is 3-13 as a rookie.
- **#65, LeBron vs the Knicks fan:** the most-replied post of the night, in LeBron's own words. The receipts come from the play-by-play: he spoke with the Sixers down six, then scored three straight baskets in 73 seconds for the first lead since the first quarter, and assisted Brown's buzzer three.
- Neither had been told on YouTube.

## Overlap to manage when posting
- #62 and #65 are the same game, and both end on 106-100 / ring night. Post one, or space them a day apart.
- #63 and #64 both mention Wemby's 1-for-13. Space them a few hours apart.

## New footage source found today
ESPN's game summary API (`site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=<id>`, key `videos`) lists every game clip ESPN posted with direct 1280x720 MP4 links. That gave us the 3rd-quarter LeBron lob, Brown's buzzer three, the full recap and the Maxey reel. NBA.com's per-play videos (stats.nba.com) time out from the cloud, and cdn.nba.com live data returns 403.
