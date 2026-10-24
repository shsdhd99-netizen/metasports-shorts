# NBA viral topics + what Ahmed's Basketball teaches (Oct 23, 2026)

**Owner's ask:** the most viral NBA topics right now, and what to learn from Ahmed's Basketball (part of the ~1.3B-view "Ahmed" Shorts network) so our picks fit a story format that works.

**What this file holds:**
1. Ahmed's Basketball by the numbers (computed today from the CSV), compared with Ahmed's Goal, and the 10 lessons that transfer.
2. 12 ranked topic candidates: 6 timely (opening week of 2026-27) and 6 evergreen story-format. Each has a title in Ahmed's style, a premise, why it should travel, sourced facts with short exact quotes, and a footage plan.
3. My top 3 picks.

**Evidence tiers:**
- [V] computed from the data, or stated in the source with the quote shown;
- [S] one secondary source, or a summary rather than a verbatim line;
- [W] weak, conflicting or unverifiable. Don't voice it without a fresh check.

**Rules kept:**
- THE #42 FORMAT is still RULE 1 (`Library/THE 42 FORMAT.md`). The Ahmed 60-75 s story format stays a **test-once** with the owner's OK (Playbook, Oct 21 section).
- Every fact below has a source URL. Quotes are under 15 words and were pulled with a "copy verbatim" fetch. Spot-check punctuation (curly vs straight apostrophes) in a browser before using a quote on screen.
- No Ahmed wording or story is copied. Titles below use generic templates in our own words.

**Inputs read:**
- `Research Notes/Ahmed Network Data (Oct 21, 2026)/` (both CSVs, `analysis_output.txt`, `analyze.py`)
- `Story Format Study - Ahmed (Oct 21, 2026).md`
- `Ahmed's Network and a Second Channel (Oct 21, 2026).md`
- `Tools/data/title_patterns.md`
- the 8 Ahmed transcripts in `Competitor Script Breakdown (Oct 15, 2026)/transcripts/ahmed.txt`
- `Library/THE 42 FORMAT.md`
- `MetaSports - Playbook.md` (RULE 1, the Oct 21-22 sections, the Winning Formula)
- `Trends Since Restart`, `Opening Night Deep Dive`
- the queue and idea banks (checked for duplicates)

---

## 1. Ahmed's Basketball by the numbers

**Method:**
- A Python pass over `AhmedsBasketball_shorts.csv` (1,175 Shorts) and `AhmedsGoal_shorts.csv` (1,365 Shorts), public view counts as of Oct 21, 2026.
- **Dates are approximate.** The CSVs have no dates, so I interpolated by list position between the anchors printed in `analysis_output.txt` (decile boundaries and the dated top 20). Monthly and half-year figures are rough.
- **Views are lifetime totals,** so the newest Shorts are undercounted.

### 1.1 Headline numbers [V]
| | **Ahmed's Basketball** | Ahmed's Goal |
|---|---|---|
| Shorts | 1,175 | 1,365 |
| Total views | 373.8M | 735.2M |
| **Median** | **159,000** | 276,000 |
| 25th / 75th percentile | 78,000 / 347,000 | 142,000 / 586,000 |
| **Top-decile cutoff (90th pct)** | **about 650,000** (the 117th-best Short has 653,000) | 1,200,000 |
| **Median of the top decile** | **1,000,000** | 2,000,000 |
| Top decile's share of all views | 46.8% | 46.3% |
| 1M+ Shorts | 68 (5.8%) | 187 (13.7%) |
| 100K+ Shorts | 792 (67%) | 1,124 (82%) |
| Runtime (sample of 75 / 73 Shorts) | 58-105 s, **median 70 s** | 58-167 s, median 76 s |
| Approx. median since Apr 21, 2026 | 120,000 (n=356) | |
| Approx. median, last 90 days | **74,500** (n=152) | 241,500 (n=150) |
| Half-year medians | 2025-H1 216K → 2025-H2 114K → 2026-H1 233K → **2026-H2 77K** | |

**What the table says:**
- Half of all Basketball views come from the top 10% of Shorts. The format is a lottery with a high floor (67% reach 100K).
- **The NBA version is decaying right now:** a 74.5K median over the last 90 days, half the all-time median. The format is no guarantee on NBA.

### 1.2 Top 25 Shorts by views [V]
Dates are interpolated (±a few weeks).

| # | Views | ~Date | Title | Theme |
|---|---|---|---|---|
| 1 | 7,100,000 | 2025-07 | DRAFT PICKS THAT WERE SUPPOSED TO BE BAD BUT WERE INCREDIBLE | draft / underdog |
| 2 | 4,600,000 | 2025-12 | NBA SCORES THAT LOOK FAKE BUT ARE 100% REAL | fake-but-real |
| 3 | 4,500,000 | 2026-05 | NBA players who got to play alongside their CHILDHOOD HERO | relationships |
| 4 | 4,200,000 | 2025-01 | WORST Draft Picks in NBA HISTORY | draft / downfall |
| 5 | 4,100,000 | 2026-04 | NBA PLAYERS WHO HAD NO CHANCE OF GOING PRO BUT STILL DID | underdog |
| 6 | 3,900,000 | 2025-05 | NBA scores that look FAKE but are 100% REAL | fake-but-real |
| 7 | 3,900,000 | 2025-04 | NBA Players who just suddenly DISAPPEARED | downfall |
| 8 | 3,700,000 | 2026-03 | NBA PLAYERS WHO MADE HISTORY BUT NO ONE TALKS ABOUT IT | records |
| 9 | 3,700,000 | 2026-01 | NBA CONTRACTS THAT CHANGED HOW PLAYERS PLAYED | money (the exception) |
| 10 | 3,700,000 | 2025-12 | CRAZIEST WAYS THAT NBA PLAYERS WERE SCOUTED | underdog / oddity |
| 11 | 3,700,000 | 2025-02 | WORST Moments in Basketball HISTORY | worst-in-history |
| 12 | 3,300,000 | 2025-07 | AWFUL TEAMS THAT BECAME NBA CHAMPIONS | underdog |
| 13 | 2,900,000 | 2026-03 | NBA PLAYERS WHO HADN'T PLAYED IN YEARS BUT CAME BACK AND SHOCKED EVERYONE | comeback |
| 14 | 2,900,000 | 2025-06 | NBA teams that ALMOST signed STARS before they were BIG Episode 3 | almost / what-if |
| 15 | 2,900,000 | 2025-02 | Moments that made every fan ARGUE | debate |
| 16 | 2,600,000 | 2026-01 | CRAZIEST WAYS THAT NBA PLAYERS GOT CUT | underdog / oddity |
| 17 | 2,400,000 | 2025-09 | STRANGEST RETIREMENTS IN NBA HISTORY | oddity |
| 18 | 2,400,000 | 2025-03 | Things that will NEVER Happen AGAIN in the NBA | records |
| 19 | 2,200,000 | 2026-05 | Iconic jersey numbers that ALMOST weren't WORN | iconic numbers / almost |
| 20 | 2,200,000 | 2026-03 | THINGS THAT ONLY ONE NBA PLAYER HAS EVER MANAGED TO DO | records |
| 21 | 2,100,000 | 2026-04 | MOST ONE SIDED TRADES IN NBA HISTORY | trades |
| 22 | 2,100,000 | 2026-02 | NBA TEAMS THAT WEREN'T SUPPOSED TO BE AS GOOD AS THEY WERE | underdog |
| 23 | 2,000,000 | 2026-03 | FRIENDS THAT WENT PRO IN THE NBA TOGETHER | relationships |
| 24 | 2,000,000 | 2025-12 | NBA PLAYERS WHO COULD'VE HAD BETTER CAREERS BUT SACRIFICED FOR THEIR TEAM | relationships / loyalty |
| 25 | 1,900,000 | 2026-03 | HIGH SCHOOL TEAMMATES WHO WON AN NBA CHAMPIONSHIP TOGETHER | relationships |

**The mix:**
- About a third are underdog or draft stories ("supposed to be bad", "no chance", "awful teams").
- 5 are records or "fake but real".
- 4 are relationships.
- Only 1 is money, and **none is refused/defiant**.

**The top Shorts since late April 2026** (the current audience) lean the same way:
- childhood hero (4.5M)
- jersey numbers that almost weren't worn (2.2M)
- best career endings (1.8M)
- weren't the college star (1.4M)
- went pro with friends (1.4M)
- refused to celebrate against their old team (1.0M)
- lost their star but found a better one (1.0M)

### 1.3 Title templates [V]
Medians, with the multiple of the channel median in brackets.

| Template | Basketball n | Basketball median | Goal median |
|---|---|---|---|
| "**…that look fake but are 100% real**" | 14 | **396,500 (2.49x)** | 779,000 (2.82x) |
| "Worst / Best / Biggest … (in NBA history)" | 125 | 195,000 (1.23x) | 161,000 (0.58x) |
| "Episode N" series titles | 117 | 175,000 (1.10x) | 278,500 (1.01x) |
| "Craziest / Strangest / Silliest …" | 121 | 159,000 (1.00x) | 259,500 (0.94x) |
| "**(NBA) players who / that …**" | 389 | 149,000 (0.94x) | 311,000 (1.13x) |
| "Things that …" | 66 | 146,500 (0.92x) | 359,000 (1.30x) |
| "Teams that / who …" | 114 | 138,500 (0.87x) | 259,000 (0.94x) |
| "Coaches / refs / owners / fans …" | 19 | 108,000 (0.68x) | 321,000 (1.16x) |
| "**The player who …**" (singular) | **0** | none | 1 Short, 2,200 |
| "**Back in …**" | **0** | none | 0 |

**The title is plural and list-sounding; the Short tells one story.**
- "The player who…" and "Back in…" never appear in titles. "Back in [year], [name]…" is the **script's** second sentence: 12 of 19 transcripts (Story Format Study).
- First two words: "players who" (n=72) has a 238K median, against 165K for "nba players" (n=256) and **77K for "basketball players"** (n=59).
- Title length:
  - 5-7 words: about 170-178K
  - 9-12 words: about 138-150K
  - 13-14 words: 81-117K
  - the median title is 8 words, the same in the top decile.
- CAPS: titles with some CAPS words have a 204K median, against 91K with none. Inside Jan-Jun 2026 only (roughly age-matched) the gap shrinks: 231-251K vs 173K. [S]
  - This conflicts with our own data (`title_patterns.md`: CAPS hurt on CoachClank) and the owner's style. **Not a lesson to act on.**

### 1.4 Theme buckets (title keywords; a Short can sit in several) [V]
| Theme | Basketball n | **Basketball median (x channel)** | ≥1M | In top decile | Goal median (x) |
|---|---|---|---|---|---|
| Legends / GOAT | 21 | 255,000 (1.60x) | 2 | 2 | 306,500 (1.11x) |
| **Draft / picks** | 63 | **235,000 (1.48x)** | 4 | 7 | n/a |
| Jersey / numbers / iconic | 12 | 218,500 (1.37x) | 2 | 2 | 670,000 (2.43x) |
| Trouble / banned / suspended / cheating | 36 | 198,500 (1.25x) | 2 | 3 | 268,000 (0.97x) |
| **Almost / what-if** | 59 | **195,000 (1.23x)** | 5 | 10 | 269,000 (0.97x) |
| Downfall / disappeared / worst | 109 | 188,000 (1.18x) | 9 | 14 | 186,500 (0.68x) |
| Loyalty / trades | 62 | 177,500 (1.12x) | 6 | 6 | 374,000 (1.36x) |
| Underdog / rejected / no chance | 67 | 170,000 (1.07x) | **11** | 13 | 363,000 (1.32x) |
| Rivalries / enemies / feuds / hated | 51 | 170,000 (1.07x) | 3 | 8 | 353,000 (1.28x) |
| Comeback / revenge | 29 | 162,000 (1.02x) | 1 | 2 | 311,000 (1.13x) |
| Records / oddities / fake-but-real | 164 | 151,000 (0.95x) | **12** | 15 | 312,000 (1.13x) |
| **Refused / defiant** | 39 | **147,000 (0.92x)** | 2 | 3 | **610,000 (2.21x)** |
| Relationships / family / heroes | 135 | 127,000 (0.80x) | 8 | 15 | 226,000 (0.82x) |
| Injury / health | 31 | 104,000 (0.65x) | 1 | 2 | 222,500 (0.81x) |
| **Money / contracts** | 78 | **93,000 (0.58x), lowest** | 3 | 4 | 271,000 (0.98x) |

**Notes:**
- The keyword lists are broader than the Oct 21 `analyze.py` labels, so a few numbers differ from that table. For example, refused/defiant was n=26 at 102.5K there; it is n=39 at 147K here. **Both versions agree on the two points that matter:**
  1. **Refused/defiant is soccer's best theme but only middling on NBA.**
  2. **Money is NBA's worst.** Our own data agrees: contract Shorts have a 2.8K median (Trends Since Restart).
- **Word-level lift in the top decile** (base rate 10%):
  - Above the base rate: "signed" 38%, "pro" 32%, "strangest" 30%, "career" 27%, "scores" 27%, "retired" 27%, "fake" 21%, "rejected" 21%, "hated" 21%, "betrayed" 22%.
  - 0%, the losers: "legends", "money", "unstoppable", "instantly", "insane", "enemies".

### 1.5 Which players appear most in the top decile
**This can't be computed from the data we hold, and I'm saying so plainly.**
- **Titles almost never name a player:** 11 of 1,175 (0.9%), 124K median. In the top decile only 2 do:
  - "Players that Kobe Bryant HATED the MOST" (850K)
  - "WORST Trades … Episode Magic" (1.0M)
- The star sits in the **script's first 3-10 s and on the cover frame**, not in the title.
- **Transcripts couldn't be pulled today:**
  - `yt-dlp` gets 403 from the cloud proxy;
  - WebFetch of youtube.com/shorts returns an empty page.

**Proxy evidence [S, n=8]:** the 8 Basketball transcripts on file (Oct 15).

| Band | Short (views) | Who it's about |
|---|---|---|
| Top 5 | Cavs spend everything, lose him anyway (783K) | LeBron and Shaq |
| | 2K cheat codes (557K) | Josh Smith |
| | Players who became insanely good (460K) | Dale Ellis |
| | Weren't good in real life but unstoppable in 2K (456K) | Kobe's 2K10 Lakers and Shannon Brown |
| | Shoes that almost destroyed Nike (390K) | Curry |
| Median band | (80K) | Durant's pay cut, a money story |
| Bottom 2 | Owners who got fined (21K) | Warriors owner Joe Lacob and Ben Simmons, a rules technicality |
| | Saddest moments (10.5K) | Reggie Lewis, 1993, a tragedy |

- **Reading [H]:** a global name in the first sentence, or a world everyone knows (NBA 2K, Nike), plus an ironic payoff wins. Owners, rules technicalities and old tragedies lose.
- The Goal study found the same: global star + small absurd human detail + twist + payoff.
- **To finish this properly on the PC:** pull captions for the 117 top-decile IDs in the CSV (`Tools/watch_short.py` or YouTube captions) and count the names.

### 1.6 Length and pace [V on samples]
- **Runtime:** median 70 s (58-105 s, n=75). Every Short runs past 60 s, probably for TikTok's 1-minute payout rule [H].
- **Pace:** the 783K LeBron/Shaq Short is 285 words in 66 s, about **258 wpm**, with 7 numbers (one every ~9 s). The network range is 228-282 wpm (n=7).
- **Ours for comparison:** THE #42 FORMAT is about 75 words, 22-25 s, about 195 wpm.

### 1.7 Series and reuse [V]
- **Reuse:** 102 concepts were posted 2+ times. **First airing median 208K; later airings 145K (about 0.7x).**
  - Examples: "Things that may never happen again" ran 25 times; "Worst trades" 16 times.
- **Reuse rarely beats the original.** "NBA scores that look FAKE" is the exception: 3.9M first, 4.6M on a later airing.

### 1.8 Basketball vs Goal: soccer hits don't carry over [V]
- For 32 of Goal's top-60 Shorts I found a Basketball title twin (title match ≥0.8). The twin almost always did 5-100x fewer views:
  - "…got in trouble for the silliest reasons": 5.9M soccer vs **12K-142K** NBA
  - "…refused to play in matches": 4.7M vs **77K**
  - "…best after changing positions": 5.7M vs 78K
  - "…retired way too young": 4.2M vs 28K
- **Templates that work on both:**
  - "…look fake but are 100% real" (2.5x / 2.8x)
  - "Clubs/teams who betrayed their own players" (3.9M / 710K)
- **Lesson:** pick NBA templates from NBA data, not from soccer's.

---

## 2. The 10 lessons that transfer to MetaSports
1. **Title formula: plural and list-sounding, one story inside, 5-9 words.**
   - "[NBA players / legends / teams] who [did a surprising, slightly absurd thing]", or "[NBA X] that look fake but are 100% real" (the strongest NBA template, 2.5x).
   - Avoid "Basketball players…" (77K median) and 13+ word titles (81-117K). [V]
2. **Line 1 = the title, read aloud word for word** (19 of 19 scripts).
   - For MetaSports this only fits the story-format **test**. In our #42 and Structure A Shorts, line 1 stays one absolute, curious claim about a named star (our hook gate, 73%+ stayed).
   - **Both put the promise in the first 3 s.** [V]
3. **Name a global star by about 4-10 s:** "Back in [year], [star] [stakes]."
   - Ahmed's titles hide the name; his scripts never do.
   - His losers (owner, technicality, old tragedy) lack a household name. That's our premise test too. [S]
4. **Turn every 8-12 s, escalating:** "But…", "There was just one problem", "But it got stranger", with 2-4 escalations.
   - The climax lands about 50-60 s in. In a 25 s Short, compress this to one turn ("So is he [bad]? No." / "But the craziest part…"). [V]
5. **End on a hard number or an irony, then stop.**
   - No question and no call to action, which matches the owner's Oct 22 rule (no promo, no dead air).
   - Ahmed's best payoffs are ironic reversals: "finished dead last… but a cheat code in 2K". [V]
6. **Pick NBA themes from NBA data:**
   - **Draft / "supposed to be bad" (1.48x)**, **almost / what-if (1.23x)**, worst/best-in-history (1.23x), trouble/banned (1.25x), "fake but real" (2.49x).
   - **Money is the worst (0.58x)**: two independent sources now. Refused/defiant only works on NBA when the star is huge and the stakes are a record or a title. [V]
7. **A small, human, slightly absurd detail beats a big abstract one** (Goal top tier: a £1.19 donut, fake grass, a shirt number).
   - NBA versions: $845 of jerseys, a wrestling show during the Finals, a cab fare.
   - **The detail is the hook; the star is the reach.** [S]
8. **Length:** Ahmed's band is 60-75 s at about 230-260 wpm, about 260-300 words.
   - Ours is 22-33 s, and our data shows no length effect inside that band.
   - **Don't stretch #42-format Shorts.** Use 60-75 s only for the one story-format test. [V]
9. **Series:** a winning title can carry a new story, but expect about 0.7x on repeats.
   - Our version: when a #42-format accusation beats the median, reuse its frame with a new star (already in the Playbook). [V]
10. **Volume doesn't buy views:**
    - Their medians fell when they went from about 2 to about 3 a day (Jul-Sep 2026).
    - The NBA channel's last-90-day median is 74.5K, about half its all-time median.
    - Keep 2 a day. Don't treat the Ahmed format as a cure; it is decaying on NBA too. [V]

---

## 3. Topic candidates (ranked)
**Ranking criteria:**
- star power: a casual fan knows the name;
- a theme that wins on Ahmed's NBA data and ours;
- a small absurd or human detail;
- a checkable number;
- footage we can actually get;
- freshness on YouTube.

**Duplicate check (Oct 23):** none of the 12 is in `Productions/`, the Production Queue, or the idea banks.
- Excluded as already told by us:
  - **Jokic drafted during a Taco Bell ad** (posted Dec 2025, 29K)
  - **Wemby's Shaolin training** (inside #35)
  - LeBron at MSG (#62/#65)
  - the Fox/Chet scuffle (#63)
  - Wemby's 1-for-13 (#64)
- **YouTube saturation is unchecked:** the cloud can't reach YouTube today. Run `copy_check.py` on the PC before scripting any of these.

| Rank | Topic | Type | Theme (Ahmed NBA median) | Star power | Window / risk |
|---|---|---|---|---|---|
| **1** | **SGA ended the longest 20-point streak ever by asking to come out** | timely (Oct 22) | records + refused (fake-but-real 2.49x; refused 0.92x) | SGA, Wilt, Jordan | post by Oct 25; nobody else in the NBA history comparison is near it |
| **2** | **Rodman skipped a Finals practice for a wrestling show** | evergreen | trouble 1.25x + rivalries 1.07x | Rodman, Jordan, Hogan, Malone | told in The Last Dance (2020); best story-format test |
| **3** | **Jordan invented "Nice game, Mike" to destroy LaBradford Smith** | evergreen | rivalries / "hated" (21% top-decile rate) + fake-but-real | Jordan | widely told since 2020; works in both formats |
| 4 | Edwards' 45 ruins Giannis' record Heat debut | timely (Oct 21) | records + rivalry | Edwards, Giannis, Jordan, Wilt, LeBron | post by Oct 24 |
| 5 | LeBron banned over $845 of jerseys, then scored 52 | evergreen | trouble 1.25x + comeback | LeBron | "silliest reasons" flopped on Ahmed NBA; LeBron fatigue on our channel |
| 6 | Rookie Giannis ran to a game because he'd wired his money home | evergreen (timely bridge) | underdog 1.07x + family | Giannis | sources conflict on details |
| 7 | Luka cried at his tribute, then dropped 45 on the team that traded him | evergreen | comeback/revenge + trades 1.12x | Luka | heavily covered in 2025 |
| 8 | LeBron's biggest comeback in 24 years came against the team he spurned | timely (Oct 22) | comeback + rivalry | LeBron | 4th LeBron/Sixers story in 3 days |
| 9 | Haliburton's first game in 486 days | timely (Oct 21) | comeback (Ahmed's 2.9M "came back and shocked everyone") | mid | post by Oct 24 |
| 10 | Kobe was a Charlotte Hornet for about a week | evergreen | almost / what-if 1.23x | Kobe | very widely told |
| 11 | Ben Simmons' comeback ended in practice | timely (Oct 18) | downfall 1.18x | Simmons | sad; handle with care |
| 12 | The Bucks still pay Lillard $113M while he stars for Portland | timely (Oct 21) | money 0.58x (weakest) | Lillard | needs the irony to carry it |

**Footage and copyright, for every topic:**
- **NBA game footage is copyrighted** by the NBA and its broadcast partners. Archive broadcasts and documentaries (The Last Dance: ESPN/Netflix; WCW footage: WWE) belong to their owners.
- **Where Ahmed-style channels typically get it:** short re-cut clips from YouTube re-uploads of broadcasts and highlights (the NBA's, teams', House of Highlights), TikTok, Instagram and X reposts, archive.org broadcasts, press photos, and stock or meme clips for abstract lines. Narration runs over everything; they accept the claim risk and sometimes leave other creators' captions burned in (Story Format Study).
- **Our rules are stricter** (`Library/B-roll Sourcing Guide.md`): official sources first, no other creators' overlays, every clip logged in `sources.csv`, and no AI footage of real players.
- **Our tools:**
  - `Tools/nba_videos.py`: official team-site clips, about 2014 on, works in the cloud.
  - `Tools/x_clip.py`: official X accounts.
  - The ESPN game-summary API: it worked Oct 21, but **the proxy rejected it on Oct 23**, so use the PC.
  - archive.org: **also rejected from the cloud today**, so use the PC.
  - `Tools/stock.py` (Mixkit) for abstract lines.
  - Wikimedia Commons photos, with the credit on screen.

---

### #1 (timely) SGA ended the longest 20-point streak in NBA history by asking to come out
- **Working title (line 1):** "NBA superstars who ended their own record on purpose."
  - Our own title option: "SGA Ended His Own Record On Purpose".
- **Line 2:** "On Thursday night, Shai Gilgeous-Alexander was three points from extending a streak nobody in NBA history had ever reached."
- **Premise:** SGA had scored 20+ in 141 straight regular-season games, smashing Wilt's 126 and doubling Jordan's best (72). Stuck on 17 with 1:43 left in a decided game, he **asked to be subbed out** because Denver had pulled its starters.
- **Why it should travel:**
  - A record nobody else is near; Ahmed's NBA records/fake-but-real lane (2.49x on "fake but real"; "things only one player has done" 2.2M).
  - A refusal with a reason (soccer's top theme, 2.21x; NBA 0.92x unless the stakes are huge, and here they are).
  - Two all-time names for scale (Wilt, Jordan).
  - A human payoff in his own words, which is our best ending type (Winning Formula #5).
  - Fresh: Oct 22.
- **Format fit:** a natural **Structure A** (moment + hidden detail), and close to THE #42 FORMAT:

  | #42 beat | SGA version |
  |---|---|
  | accusation | "SGA just failed to score 20 for the first time in two years." |
  | count | "141." |
  | old record | "The old record was Wilt's: 126." |
  | turn | "So did he choke? No." |
  | proof | he asked out at 1:43 because Denver had subbed |
  | flip | "Jordan's best streak was 72." |

  The critic decides whether the "flip" counts.

| Key fact | Source | Exact quote |
|---|---|---|
| The streak was 141 regular-season games of 20+ | [ClutchPoints](https://clutchpoints.com/nba/oklahoma-city-thunder/thunder-news-shai-gilgeous-alexanders-record-141-game-20-point-streak-snapped-win-nuggets) | "snapped his NBA-record streak of 141 straight regular-season games" |
| It passed Wilt's 126 (tied Mar 9, 2026) | same | "tying Wilt Chamberlain's longtime mark of 126 straight 20-point games" |
| It began Nov 1, 2024 | same | "The run began on Nov. 1, 2024" |
| He scored 17 in a 96-84 win | same | "scored 17 points in the Thunder's 96-84 home win over the Denver Nuggets" |
| He asked out after Denver's timeout at 1:43 | [Bleacher Report](https://bleacherreport.com/articles/25519316-sga-reacts-historic-20-point-game-streak-ending-always-treat-game-respect) | "after the Nuggets called a timeout 1:43 remaining in the fourth." |
| His reason, in his words | same | "I feel like you always treat the game with respect." |
| His coach's version | [NBA.com](https://www.nba.com/news/takeaways-nuggets-thunder-2026-27) | "He asked out at the end." |
| Jordan's best run was 72 | [CBS Sports](https://www.cbssports.com/nba/news/shai-gilgeous-alexander-20-point-streak-record-may-never-be-broken/) | "The most consecutive 20-point games Michael Jordan ever logged was 72." |
| AP framing | [AP via ABC News](https://abcnews.com/Sports/wireStory/thunder-overcome-sgas-shooting-woes-beat-nuggets-96-137500101) | "failed to score 20 points for the first time in 141 games" |

- **Footage plan:**
  - The 25-footer that took him to 17 and SGA walking to the bench: Thunder team-site clips via `nba_videos.py`, or the ESPN game-summary clips from the PC.
  - The record-breaking game: March 12, 2026 vs Boston, via [6abc/AP](https://6abc.com/post/shai-gilgeous-alexander-scores-20-points-127th-straight-game-breaking-wilt-chamberlains-record/18708622/).
  - Wilt: still photos only. Identifiable Wilt film is blocked for us (see #43).
  - Jordan: a photo or a licensed-source clip.
  - Frame 1: a missed shot from his 0-fer first half, or the walk to the bench.
- **Weak / check:**
  - [W] First half: 0-for-6 (Basketnews) vs "missed all seven shots" (AP). Say "no field goal in the first half".
  - [W] A forum claims he missed games during the streak. The streak counts games played, regular season only, so don't claim "every game for two years".
  - [S] Wilt's streak reportedly ended when he was ejected for "abusive language" ([News4JAX/AP](https://www.news4jax.com/sports/2026/03/10/inside-the-numbers-shai-gilgeous-alexander-ties-wilt-chamberlains-20-point-streak-record/)). It would make a nice mirror; verify before using.
  - Don't call SGA "reigning MVP" without a fresh check.

### #2 (evergreen) Rodman skipped an NBA Finals practice to go to a wrestling show with Hulk Hogan
- **Working title:** "NBA players who skipped practice in the Finals for the weirdest reasons."
- **Line 2:** "Back in 1998, Dennis Rodman's Bulls were two wins from a sixth title, and Rodman wasn't at practice."
- **Premise:** The day after Game 3 of the 1998 Finals, Rodman flew to Detroit for WCW Monday Nitro with Hulk Hogan. He was fined $10,000, then grabbed 14 rebounds in a Game 4 win. A month later he wrestled the man he was guarding in the Finals, Karl Malone.
- **Why it should travel:**
  - Trouble/banned (1.25x).
  - A rivalry that leaves the sport (rivalries 1.07x; "hated" 21% top-decile rate).
  - A small absurd detail (the fine, the wrestling ring).
  - Three global names (Rodman, Jordan, Hogan) plus Malone.
  - An ironic payoff: he got punished, played great, then fought his Finals opponent for real.
  - **Lots of escalation beats, which makes it the best candidate for the one 60-75 s story-format test.**

| Key fact | Source | Exact quote |
|---|---|---|
| He flew to Detroit for WCW Nitro with Hogan | [The Comeback](https://amp.thecomeback.com/nba/that-time-dennis-rodman-skipped-a-1998-nba-finals-practice-to-attend-a-wcw-event-then-had-14-rebounds-shut-down-karl-malone-in-game-4.html) | "flying to Detroit to appear at a WCW Nitro wrestling event with Hulk Hogan" |
| The NBA fined him $10K; the Bulls fined him too | same | "Rodman was fined $10,000 by the NBA" |
| 14 rebounds in Game 4 | same | "pulling down 14 rebounds" |
| The Bulls won Game 4 | [Wikipedia: 1998 NBA Finals](https://en.wikipedia.org/wiki/1998_NBA_Finals) | "Chicago won Game 4 in a close game, 86–82." |
| July 12, 1998: Rodman and Hogan beat Malone in the ring | same | "Rodman and Hollywood Hogan would defeat Malone and Diamond Dallas Page" |
| Jordan's reaction | The Comeback | "Dennis comes with a lot of baggage." |

- **Footage plan:**
  - The 1998 Finals Game 3/4 broadcast (NBC; archive.org from the PC): Rodman boxing out Malone, a Game 4 rebound.
  - Press photos of Rodman at Nitro and at Bash at the Beach 1998.
  - **WCW footage is WWE-owned and aggressively claimed:** use photos, or hold any clip to 1-2 s.
  - Stock for "skipped practice" (an empty gym, a plane).
  - Frame 1: Rodman in the Finals.
- **Weak / check:**
  - [W] "Reportedly seen at a downtown Hooters" is reportage only; skip it.
  - [W] The Bulls' fine amount is undisclosed.
  - Saturation: The Last Dance (2020) covered it; run the copy-check.

### #3 (evergreen) Jordan made up "Nice game, Mike" to destroy a player who'd scored 37 on him
- **Working title:** "NBA legends who made up an insult just to destroy someone."
- **Line 2:** "Back in 1993, a backup guard named LaBradford Smith scored 37 points on Michael Jordan."
- **Premise:** After Smith's 37, Jordan told teammates Smith had said "Nice game, Mike." He promised to score 37 in the first half of the rematch the next night, got 36 by half and 47 in all, and later admitted the line never happened.
- **Why it should travel:**
  - The biggest name in the sport.
  - Rivalries/hated (Ahmed's "Players that Kobe Bryant HATED the MOST": 850K).
  - "Sounds fake but is 100% real", with a twist on top: the insult itself was fake.
  - A hard number payoff (36 in a half).
  - Works as a 25-30 s **Structure B** or as the story test.

| Key fact | Source | Exact quote |
|---|---|---|
| Smith scored 37 in a Bullets loss | [CBS Sports](https://www.cbssports.com/nba/news/michael-jordan-vs-labradford-smith-a-look-at-the-bulls-legends-revenge-against-an-imaginary-opponent/) | "a 37-point masterpiece that still resulted in a loss for his Washington Bullets" |
| The line Jordan claimed | same | "Nice game, Mike." |
| 36 in the first half of the rematch | same | "He finished just short, at 36." |
| 47 for the game | same | "He finished with "only" 47 for the game" |
| Jordan invented it | same | "Jordan made up the entire exchange." |

- **Footage plan:**
  - Jordan vs the Bullets, March 1993: broadcast clips if found on archive.org or the NBA's YouTube (PC).
  - Smith photos.
  - **The Last Dance episode 8 interview is ESPN/Netflix property:** a quote card with the source on screen is safer than the clip.
  - Stock for "made it up" (a pen, a whisper).
  - Frame 1: Jordan's face or a Jordan jumper vs Washington.
- **Weak / check:**
  - The exact dates (back-to-back in March 1993): confirm on Basketball-Reference.
  - Smith's own account, per [WDRB](https://www.wdrb.com/sports/bozich-what-did-labradford-smith-really-say-to-michael-jordan/article_8060177a-93b8-11ea-a8d5-0b5f232ec2c9.html), is not read yet.
  - Saturation: told widely since 2020.

### #4 (timely) Anthony Edwards' 45 ruined Giannis' record Heat debut
- **Working title:** "NBA players who got trash-talked from the bench and made the whole team pay."
- **Line 2:** "On opening night, Giannis Antetokounmpo played his first game for Miami, and someone on Miami's bench started talking."
- **Premise:**
  - Giannis scored 35, the most ever in a Heat debut, passing LeBron's 31 from 2010.
  - Edwards, fuelled by a Heat player trash-talking from the bench, scored 45 in a 131-106 rout.
  - It made Edwards only the third player with multiple 40-point openers, after Wilt and Jordan.
- **Why it should travel:**
  - Two of the biggest current stars, plus Jordan and Wilt for scale.
  - Rivalry and revenge, and a record.
  - The irony: Giannis broke LeBron's record and lost by 25.
  - Fresh (Oct 21).

| Key fact | Source | Exact quote |
|---|---|---|
| Edwards 45 and 10 | [Sportando](https://sportando.basketball/en/anthony-edwards-joins-chamberlain-and-jordan-with-another-40-point-season-opener/) | "Anthony Edwards opened the season with 45 points and 10 rebounds" |
| Only Wilt (4) and Jordan (3) have more 40-point openers | same | "Chamberlain had four 40-point openers, while Jordan had three." |
| His previous: 41 last season | same | "He scored 41 points in last season’s opener against Portland" |
| The trash talk | [Yahoo Sports](https://sports.yahoo.com/articles/anthony-edwards-joins-michael-jordan-161110394.html) | "a Heat player talking trash from the bench" |
| Edwards, in his words | same | "I think that was pretty much the reason why I was super intense tonight." |
| Giannis' Heat debut record | [ClutchPoints](https://clutchpoints.com/nba/nba-stories/heat-overreactions-giannis-antetokounmpo-nasty-bucks-deja-vu-timberwolves-beatdown) | "surpassing LeBron James' 31-point debut in 2010." |
| Final score | [BVM Sports](https://bvmsports.com/2026/10/22/giannis-calls-out-heat-effort-after-131-106-loss-to-wolves/) | "131-106 Loss to Wolves" |

- **Footage plan:**
  - Timberwolves and Heat team-site clips (`nba_videos.py`): Edwards' threes, Giannis' dunks.
  - The bench exchange if a broadcast clip shows it (ESPN API, PC).
  - LeBron's 2010 Heat debut photo.
  - Frame 1: Edwards pointing at the Heat bench, if it exists, or a made three.
- **Weak / check:**
  - [W] The trash-talking Heat player is **unnamed** in every source read. Don't guess a name.
  - The 9-for-17 from three is from BVM only [S].

### #5 (evergreen) LeBron was banned from high school basketball over $845 of jerseys, then scored 52
- **Working title:** "NBA legends who got banned for the silliest reasons."
- **Line 2:** "Back in 2003, LeBron James was the most famous high school player in America, and two free jerseys got him banned."
- **Premise:** A Cleveland store gave him Gale Sayers and Wes Unseld throwbacks in exchange for photos on its wall. Ohio ruled him ineligible for the rest of the season; a judge cut it to a short suspension; his first game back he scored 52.
- **Why it should travel:**
  - Trouble/banned (1.25x).
  - An absurd small number ($845).
  - Comeback payoff (52).
  - The biggest active name.
  - **Caution:** the "silliest reasons" template did 5.9M on soccer but only 142K and 12K on Ahmed's NBA channel, and LeBron is in 31% of our new Shorts.

| Key fact | Source | Exact quote |
|---|---|---|
| The jerseys and their value | [ESPN, Feb 2003](https://www.espn.com/nba/news/2003/0203/1503500.html) | "accepting two free sports jerseys worth a combined $845 from a clothing store" |
| Whose jerseys | same | "the Cleveland store gave James the Gale Sayers and Wes Unseld jerseys for free" |
| Why | same | "in exchange for James posing for pictures to be displayed on the walls" |
| The school didn't fight it | same | "not contest James' exclusion for the remainder of the season" |
| First game back: 52 | [Rivals, Feb 9 2003](https://basketballrecruiting.rivals.com/news/lebron-erupts-for-52-as-svsm-rips-westchester) | "erupting for 52 points on Saturday night" |

- **Footage plan:**
  - St. Vincent-St. Mary games from 2002-03, which were nationally televised; re-uploads exist, so it's a PC search, and the broadcaster owns them.
  - Press photos of LeBron in throwbacks.
  - A recreation card of the two jerseys, labelled "recreation", like S01's note.
  - Frame 1: high school LeBron dunking.
- **Weak / check:**
  - [W] Games missed: Rivals says a "one game suspension", while [ESPN Feb 14](https://www.espn.com/nba/news/2003/0214/1509074.html) says the judge ordered him to sit "another game". Say "a short suspension".
  - Skip the Hummer investigation; it's a separate story.

### #6 (evergreen, with a timely bridge) Rookie Giannis ran to an NBA game because he'd wired his money home
- **Working title:** "NBA superstars who were broke in their rookie season."
- **Line 2:** "Back in 2013, Giannis Antetokounmpo had an NBA contract and couldn't afford a taxi."
- **Premise:** On a game day he wired money to his family in Athens and hit his ATM limit. He started running the roughly two miles to the arena in the cold until strangers recognised him and drove him there.
  - **Payoff:** 13 years later he scored the most points ever in a Heat debut (#4).
- **Why it should travel:**
  - A global star plus the most human detail on this list (cab fare).
  - Underdog (1.07x; "had no chance of going pro" 4.1M) with family.
  - Ties into this week's news.

| Key fact | Source | Exact quote |
|---|---|---|
| He was wiring money to his family | [SI (Bucks Zone)](https://www.si.com/nba/bucks/old-school/rookie-giannis-antetokounmpo-run-to-milwaukee-bucks-arena-he-couldnt-afford-a-taxi) | "wanted to wire some money to his family in Athens" |
| ATM limit | same | "he discovered he had reached his limit." |
| He ran | same | "decided to run the two or so miles to the Bradley," |
| Strangers drove him | same | "the couple dropped him off at the arena's front door." |
| Driver's recollection of his words [S] | [Channel3000](https://www.channel3000.com/my-long-lost-son-milwaukee-woman-recalls-time-she-gave-cashless-and-carless-giannis-antetokounmpo-a-ride-to-arena-during-his-rookie-season/) | "My credit card doesn't work and I've sent all my money to my parents!" |
| Payoff: Heat debut record | [ClutchPoints](https://clutchpoints.com/nba/nba-stories/heat-overreactions-giannis-antetokounmpo-nasty-bucks-deja-vu-timberwolves-beatdown) | "surpassing LeBron James' 31-point debut in 2010." |

- **Footage plan:**
  - Rookie-year Giannis (2013-14 Bucks clips; team-site archive may not reach that far, so try NBA YouTube on the PC).
  - The Bradley Center exterior (Wikimedia).
  - Stock: a snowy street, a taxi, an ATM.
  - Oct 21 Heat-debut clips for the payoff.
  - Frame 1: skinny rookie Giannis.
- **Weak / check:**
  - [W] **The sources conflict.** SI says December 2013 and a couple (one later identified as a writer's aunt); Channel3000 says November 2013, a UW-Milwaukee professor and her boyfriend, 18°F.
  - Don't name the drivers or the month. Say "a couple of strangers" and "his rookie winter".

### #7 (evergreen) Luka cried at his tribute video, then scored 45 on the team that traded him
- **Working title:** "NBA players who destroyed the team that traded them."
- **Line 2:** "Back in February 2025, Dallas traded Luka Doncic in the middle of the night."
- **Premise:** In his first game back in Dallas (Apr 9, 2025) he cried through the Mavericks' tribute video, then scored 45 on 16-for-28 as the crowd cheered him over the home team. Nine months later the GM who traded him was fired as fans chanted "Fire Nico!"
- **Why it should travel:**
  - Comeback/revenge with trades (1.12x; Ahmed's "most one-sided trades" 2.1M; "refused to celebrate against their old team" 1.0M).
  - A global star.
  - An emotional detail (the tears) and a hard number (45).

| Key fact | Source | Exact quote |
|---|---|---|
| He cried at the tribute | [SI (Mavs)](https://www.si.com/nba/mavericks/onsi/news/luka-doncic-first-game-back-dallas-mavericks-called-one-best-revenge-games-ever-) | "him crying on the bench as the team played a tribute video" |
| 45 on 16/28 | same | "Doncic scored 45 points on an efficient 16/28 shooting" |
| The crowd chose him | same | "cheering louder for him than they were for the home team" |
| Result | [NBC DFW/AP](https://www.nbcdfw.com/news/sports/dallas-mavericks/luka-doncic-scores-45-points-in-dallas-return-as-lakers-clinch-playoff-spot-with-112-97-win/3813405/) | "Lakers clinch playoff spot with 112-97 win" |
| The GM was fired | [Al Jazeera](https://www.aljazeera.com/sports/2025/11/12/nico-harrison-fired-from-mavericks-nine-months-after-luka-doncic-trade) | "nine months after his trade of Luka Doncic" |
| Dallas' start | same | "The Mavericks have limped out of the blocks to a 3-8 record." |

- **Footage plan:**
  - Mavericks and Lakers team-site clips (Apr 9, 2025) via `nba_videos.py`: the tribute video on the big screen, Luka on the bench, his makes.
  - Nov 2025 crowd footage only if it's an official clip.
  - Frame 1: Luka wiping his eyes.
- **Weak / check:**
  - The "Fire Nico!" chants were at a **Nov 2025 game vs Milwaukee**, not at Luka's return. Keep them separate.
  - Trade date: Feb 1 (SI) vs Feb 2 (Al Jazeera). Say "February 2025".

### #8 (timely) LeBron's biggest comeback in 24 seasons came against the team he chose not to rejoin
- **Working title:** "NBA legends who beat their old team in the craziest way."
- **Line 2:** "On Thursday, LeBron James played his first home game for Philadelphia, against the Cleveland team he'd turned down in July."
- **Premise:** The Sixers trailed Cleveland by 29 in the first half and won 114-106. It was the largest comeback of LeBron's career and Philly's largest of the play-by-play era, with his daughter celebrating her 12th birthday courtside next to Allen Iverson.
- **Why it should travel:**
  - Comeback/revenge.
  - The biggest name.
  - A human detail (Zhuri's birthday next to Iverson).
  - **Risk:** our 4th LeBron-Sixers story in 3 days (#62, #65, #10). Space it out.

| Key fact | Source | Exact quote |
|---|---|---|
| 29 down, won 114-106 | [Philadelphia Inquirer](https://www.inquirer.com/sixers/lebron-james-sixers-home-debut-largest-comeback-cavaliers-20261023.html) | "rally from a 29-point first-half deficit to win, 114-106" |
| His biggest comeback ever | same | "in the largest comeback of James’ historic 24-year career." |
| He chose Philly over Cleveland | same | "When James picked the Sixers’ loaded roster over another Cavaliers reunion" |
| Zhuri and Iverson | same | "who celebrated her 12th birthday by sitting courtside next to Allen Iverson." |
| LeBron on the crowd | same | "Got the boos. That was amazing. We deserved it." |
| Franchise context | [The Big Lead](https://www.thebiglead.com/76ers-comeback-another-major-lebron-james-milestone/) | "the franchise’s largest comeback win in the play-by-play era" |

- **Footage plan:**
  - Sixers team-site clips (`nba_videos.py`): the third-quarter run, LeBron's 10-point quarter.
  - The Zhuri/Iverson courtside shot (official Sixers X).
  - Frame 1: the scoreboard at -29.
- **Weak / check:**
  - The play-by-play era starts in 1996-97 (Big Lead) or 1997-98 (Yahoo). Don't state the year.
  - **Skip the same-night Trump anthem story:** it's political and a brand risk.
  - Also from this game: Harden (now a Cav) vs Maxey shove, "I love him, and he loves me." ([Fadeaway World](https://fadeawayworld.net/nba/philadelphia-76ers/james-harden-and-tyrese-maxey-shove-each-other-in-viral-heated-moment-at-76ers-cavaliers-game)). Usable as a beat, not its own Short.

### #9 (timely) Haliburton's first game in 486 days, after tearing his Achilles in Game 7 of the Finals
- **Working title:** "NBA players who missed a year and a half and came back like nothing happened."
- **Line 2:** "Back in June 2025, Tyrese Haliburton tore his Achilles in the first quarter of Game 7 of the NBA Finals."
- **Premise:** 486 days later, in his first game back, he scored 23 with 12 assists, 16 of them in the fourth quarter, in a 3-point win. He wore a Triple H-style jacket for the walk in and cried seeing Pacers fans celebrate.
- **Why it should travel:**
  - The direct NBA analogue of Ahmed's 2.9M "hadn't played in years but came back and shocked everyone" (comeback).
  - The Game 7 stakes are huge.
  - **Weaker star power** than #1-#8.

| Key fact | Source | Exact quote |
|---|---|---|
| The injury | [Andscape](https://andscape.com/features/tyrese-haliburton-injury-return-2026-pacers-achilles-debut) | "tore his right Achilles tendon in the first quarter of Game 7." |
| 486 days | [NBA.com live blog](https://www.nba.com/news/live-updates-nba-games-top-moments-stats-scores-2026-27-season) | "Tyrese Haliburton arrives for his first game back in 486 days!" |
| 23 and 12 | Andscape | "Haliburton scored 23 points and had 12 assists" |
| 16 in the 4th | same | "scored 16 of his 23 points in the fourth quarter" |
| Tears | same | "brought to tears of joy after seeing Pacers fans celebrating" |
| The jacket | same | "similar to the one worn by Triple H" |

- **Footage plan:**
  - The 2025 Finals Game 7 injury (official NBA clip; handle the injury moment briefly and respectfully).
  - Pacers team-site clips from Oct 21: fourth-quarter buckets, his arrival walk.
  - Frame 1: the arrival walk in the jacket.

### #10 (evergreen) Kobe Bryant was a Charlotte Hornet for about a week
- **Working title:** "NBA legends who almost played for a completely different team."
- **Line 2:** "Back in 1996, the Charlotte Hornets drafted a 17-year-old named Kobe Bryant."
- **Premise:** Charlotte took Kobe 13th in a prearranged trade with the Lakers for Vlade Divac. The deal nearly died when Divac threatened to retire rather than report to Charlotte. Kobe said he'd have played for the Hornets.
- **Why it should travel:**
  - Almost/what-if (1.23x; Ahmed's "teams that ALMOST signed stars" 2.9M and "almost drafted Hall of Famers" 1.5M).
  - A global star.
  - **Very widely told**, so it needs a fresh angle (the Divac threat).

| Key fact | Source | Exact quote |
|---|---|---|
| Drafted 13th by Charlotte | [WBTV](https://www.wbtv.com/2020/01/26/kobe-bryant-was-hornet-week-hes-greatest-charlotte-athlete-who-never-was/) | "The Charlotte Hornets drafted Bryant 13 picks into the ’96 draft." |
| Traded for Divac | same | "Bass dealt Bryant to the Lakers in a prearranged deal for center Vlade Divac." |
| Divac nearly killed it | same | "Divac threatened to retire as a player rather than report to the Hornets." |
| Kobe would have gone | same | "I’d be a Hornet," |
| Lakers' side | [CBS Sports](https://www.cbssports.com/nba/news/kobe-bryant-death-hornets-gm-says-trade-that-sent-nba-legend-to-lakers-in-1996-draft-almost-never-happened) | "where the deal was actually in jeopardy." |

- **Footage plan:**
  - The 1996 draft broadcast (Kobe in the Hornets cap is the frame 1), on the NBA's YouTube or archive.
  - Divac Lakers and Hornets photos.
- **Weak / check:**
  - [W] **Myth to avoid:** "Kobe threatened to play in Italy". WBTV reports the opposite. It was only floated pre-draft to scare teams off.

### #11 (timely) Ben Simmons' comeback ended in practice, three days before the season
- **Working title:** "NBA No. 1 picks whose comeback ended before it started."
- **Line 2:** "Back in 2016, Ben Simmons was the first pick in the NBA draft."
- **Premise:** The 2016 No. 1 pick, Rookie of the Year and three-time All-Star, waived by Brooklyn in 2025 and out all of last season, signed a one-year comeback deal with Sacramento. He tore his Achilles in practice on Oct 18.
- **Why it should travel:**
  - Downfall/disappeared (1.18x; Ahmed's "suddenly DISAPPEARED" 3.9M).
  - A widely known name.
  - **Sensitive:** an injury, and his history includes mental-health absences. Tell it with respect, no mockery.

| Key fact | Source | Exact quote |
|---|---|---|
| The injury | [KSL/AP](https://www.ksl.com/article/51637913/kings-guard-ben-simmons-tears-his-achilles-tendon-in-practice) | "Ben Simmons tore his right Achilles tendon in practice on Sunday" |
| No. 1 pick | same | "Simmons was the first overall pick by Philadelphia in 2016" |
| Peak | same | "three-time All-Star and Rookie of the Year" |
| The fall | same | "averaging 5.9 points, 5.8 rebounds and 5.8 assists" (with the Nets and Clippers) |
| The comeback deal | same | "Simmons had signed a one-year deal with Sacramento this summer" |
| His words [S] | same | "This injury is another chapter in my journey, not the end of my story." |

- **Footage plan:**
  - 2017-18 Sixers ROY highlights (team-site archive).
  - Kings preseason clips, official.
  - No injury footage exists (practice).
  - Frame 1: rookie Simmons in transition.

### #12 (timely) The Bucks still pay Damian Lillard $113 million while he stars for Portland
- **Working title:** "NBA teams still paying a player who plays for someone else."
- **Line 2:** "Back in April 2025, Damian Lillard tore his Achilles in a playoff game for Milwaukee."
- **Premise:** Milwaukee waived him and stretched the $113M it owed him over five seasons. He signed back with Portland for 3 years and $42M, sat out a season, and in his first game back the Blazers won by 41. He now has the most points ever in a Portland uniform.
- **Why it should travel:**
  - An ironic detail (a team paying a rival's star).
  - A homecoming.
  - **But money is the weakest NBA theme (0.58x)** on both channels. Only make it if the irony leads, not the cap mechanics (premise test: "never a technicality").

| Key fact | Source | Exact quote |
|---|---|---|
| The injury | [Andscape](https://andscape.com/features/damian-lillard-portland-trail-blazers-2026-injuries-contract-interview/) | "he suffered a torn left Achilles tendon on April 27, 2025, during Game 4" |
| Bucks' stretch | same | "opted to pay the remaining $113 million owed to him over five seasons" |
| Portland deal | same | "Lillard returned to Portland shortly after, signing a three-year, $42 million contract." |
| First game back | [NBA.com live blog](https://www.nba.com/news/live-updates-nba-games-top-moments-stats-scores-2026-27-season) | "Trail Blazers 124, Suns 83" |
| Franchise record | same | "That's 19,379 points for Damian Lillard in a Portland uniform — most all-time" |

- **Footage plan:**
  - Blazers team-site clips from Oct 21 (`nba_videos.py`).
  - The April 2025 Game 4 vs Indiana (team-site).
  - Frame 1: Lillard's first bucket back.

### Considered, not ranked
| Story | Reason left out |
|---|---|
| **LaMelo's four-step travel** that the refs admitted, "He takes four steps after gathering the ball and travels." ([Bleacher Report](https://bleacherreport.com/articles/25519084-nba-refs-call-out-lamelo-balls-travel-after-viral-video-t-wolves-opener-vs-heat)) | Rule lane, all-or-nothing for us; viral but thin |
| Walker Kessler 12-for-12, the first Lakers center with a perfect 12+ attempt night "since Wilt Chamberlain in 1969" ([NBA.com](https://www.nba.com/news/live-updates-nba-games-top-moments-stats-scores-2026-27-season)) | Kessler isn't a casual-fan name |
| **Ty Jerome 45** (old career high 33; the 24th pick in 2019 whose rights were traded twice) ([Yahoo](https://sports.yahoo.com/articles/grizzlies-ty-jerome-stuns-nba-134440608.html), [Wikipedia](https://en.wikipedia.org/wiki/Ty_Jerome)) | A great underdog arc but a niche name. Our premise test says no |
| Klay Thompson's 2,900th three, 4th ever (NBA.com) | Small |
| No. 1 pick AJ Dybantsa out with an ankle injury ([Newsweek](https://www.newsweek.com/sports/nba/wizards-get-devastating-aj-dybantsa-injury-news-before-nba-opener-12595468)) | **Watch his debut:** that night's Short could be timely |
| Trump vs LeBron over the anthem ([Al Jazeera](https://www.aljazeera.com/sports/2026/10/22/trump-says-nba-star-lebron-james-disrespected-us-national-anthem)) | Political; skip |
| Evergreen: Shaq's only career three; Jordan's "love of the game" clause ([SI](https://www.si.com/nba/2015/08/25/nba-contracts-bill-russell-wilt-chamberlain-michael-jordan-magic-johnson-celtics-lakers-bulls)); Iverson's rookie 40-point run | Not verified this session; good bank items |

---

## 4. My top 3 picks
1. **SGA asked out of his own record (#1). Make it now, in our proven format.**
   - It's the freshest big story of the week (Oct 22), and its hook is a record that sounds wrong: 141, against Wilt's 126 and Jordan's 72.
   - It carries the reason Ahmed's top Shorts and our breakouts share: a famous name, one checkable number, and a human twist in the star's own words.
   - It maps onto Structure A, nearly onto THE #42 FORMAT, so it needs no new format.
   - Footage is official and recent.
   - Post by Oct 24-25: our views arrive in week 1.
2. **Rodman's Finals wrestling detour (#2). Make it the one Ahmed-style 60-75 s test.**
   - It has the most escalation of any candidate: skipped practice, the $10K fine, 14 rebounds and a win, then wrestling his Finals opponent, Malone. That is exactly what the story format needs to fill 70 s with a turn every 10 s.
   - Four household names, and trouble/rivalry themes that clear Ahmed's NBA median.
   - Check the 1998 broadcast on the PC first; keep WCW to photos.
3. **Jordan's invented "Nice game, Mike" (#3). Make it as an evergreen for an evening slot.**
   - The biggest name in basketball, a "sounds fake but is 100% real" twist with a second twist (the insult was fake), and a hard payoff (36 in a half).
   - It also fits our 25-30 s Structure B, so it works whichever format the test favours.
   - Run `copy_check.py` first: The Last Dance made it well known.

**Runner-up if a second timely slot opens:** #4, Edwards vs Giannis. Post it by Oct 24, before it goes stale.

## 5. Open items
- On the PC, pull captions for Ahmed's 117 top-decile Basketball Shorts (IDs in the CSV) to answer "which stars appear most". The cloud can't reach YouTube today.
- Run `copy_check.py` on every pick before scripting.
- Re-verify the [W] items listed under each topic before voicing.
