# Soccer Topic Study (Nov 1, 2026)

Owner: "research and develop on soccer videos just like NBA." FC Shorts were on hold until this was done. Data and code: `Soccer Topic Study (Nov 1, 2026)/` (`analyze.py`, `classified.tsv`, `results.txt`; every competitor number below is in `results.txt`).
Evidence tiers: [V] measured on a large sample, [S] small sample or one channel, [H] a guess.

## 1. What was measured
10 soccer Shorts channels, 4,885 Shorts in `classified.tsv`. Each Short's views are divided by its own channel's median and adjusted for age ("time-adj"; 1.00 = a normal Short for that channel). A topic "wins" only if it is above 1.0 pooled, still above 1.0 without Ahmed's Goal (the biggest channel), and above 1.0 in most single channels.

## 2. Topics ranked by outperformance (8 story/facts channels pooled; ex-Ahmed in brackets)
| Rank | Topic | n | time-adj (ex-Ahmed) | Holds in channels | Read |
|---|---|---|---|---|---|
| 1 | tactics/analysis/stats | 41 | 1.37 (1.52) | 3 of 3 | Real, but mostly from analysis channels (PedTalks, Tifo); not our format [S] |
| 2 | **goalkeeper** | 67 | **1.30 (1.29)** | 3 of 4 | Above 1.0 in every cut AND matches our own channel [V] |
| 3 | conflict/revenge/rivalry | 311 | 1.12 (1.03) | 4 of 7 | Mild; fades without Ahmed |
| 4 | fan/kid story | 117 | 1.11 (1.08) | 4 of 5 (channel-balanced 1.53) | Best untested lane for us [S] |
| 5 | family/WAGs | 116 | 1.11 (1.11) | 3 of 5 | Holds without Ahmed |
| 6 | debate/ranking | 157 | 1.10 (1.04) | 4 of 7 | Ranking lists; not our format |
| 7 | World Cup/national team | 351 | 1.05 (1.08) | 4 of 7 | Steady; helps a goalkeeper story |
| - | manager/coach | 168 | 1.00 (1.15) | 3 of 6 | Helps only without Ahmed |
| Bottom | Messi 0.87, money/transfer 0.87, tragedy/injury 0.88, awards 0.92, club names 0.97, "names a star" 1.00 (0.96) | | | | **Naming a famous player or club does not help.** Messi and transfer-fee stories are below average. |

**Takeaway [V]:** the topic is not "a famous star". It is a situation with a person in it (a goalkeeper in a shootout, a kid, a family member). Star-name titles are flat to negative once Ahmed's channel is removed.

## 3. Our own channel (12 Shorts, `fc_track.py`, Nov 1 16:50 UTC)
| Short | Views | Topic |
|---|---|---|
| S01 cheat sheet in his sock (Lehmann) | 30.3K | goalkeeper, penalty shootout |
| S05 cheat sheet on a water bottle (Pickford) | 29.0K | goalkeeper, penalty shootout |
| S17 subbed on just for penalties (Krul) | 16.6K at 54 h | goalkeeper, penalty shootout |
| S03 danced on the line (Dudek) | 15.0K | goalkeeper, penalty shootout |
| S08 Hand of God shirt | 3.2K | star, object, money |
| S16 Fabregas "stop scoring" | 3.0K | manager, news |
| S07 Loch Ness odds | 2.5K | odds |
| S06 Lewandowski 5 goals | 2.1K | record |
| S04 Zidane red card | 2.0K | star, sent off |
| S18 Mourinho sprinklers | 2.0K at 25 h | manager, revenge |
| S02 derby trouble (Balotelli) | 1.8K | star, scandal |
| S15 Coutinho transfer | 1.1K | money, transfer |

**Every goalkeeper-in-a-shootout Short is 15-30K; every other Short is 1-3K [V, n=12].** That gap (10x+) is much larger than competitors' 1.3x goalkeeper edge, so something else is working inside our goalkeeper Shorts (see Script Craft). Caution: 4 hits, same format, same few days. The competitor data says "goalkeeper" is the safest topic, not a guarantee.

## 4. Title shapes (8 channels pooled)
| Shape | n | time-adj | Read |
|---|---|---|---|
| starts "When..." | 77 | **1.44** | Best. The story is already happening [S] |
| "real reason / you didn't know / untold / the truth" | 64 | **1.37** | Works; 1.71 in Ahmed alone |
| starts "What/Who/Which" | 114 | 1.20 | "What happened to North Korea after the World Cup?" 9.4M |
| 11-14 words | 315 | 1.06 | Titles of 6 words or fewer are 0.95: shorter is not better |
| plural "Players who..." | 864 | 1.02 | Neutral. Our "Goalkeepers who..." wins because of topic, not shape |
| name-led (star/club first) | 277 | 0.93 | Below average |
| number-led | 69 | 0.91 | Below average |
| superlative-led (Most/Worst/Craziest) | 405 | 0.88 | Below average |
| vague hype word (crazy/insane/wild) | 225 | 0.86 | Below average |
| "The day/night/time..." | 14 | 0.62 | Avoid |

**Duration [V]:** under 45 s underperforms badly (0.25-0.61x); 45-59 s is fine (1.08); 120 s+ is highest (1.33) but only Ahmed and PedTalks do it, and our rule is under 60 s. Keep 45-59 s.
**Recency check:** the newest fifth of most channels is BELOW their own median (FootyFacts and PedTalks are exceptions). Do not copy volume.

## 5. What the study says to do
1. **Make goalkeeper stories the series**: one person, one device, a shootout. Aim 2 of every 3 FC posts at this until the numbers drop.
2. **Test fan/kid and family stories** (1.53 channel-balanced) as the second lane: a little brother, a baby Messi once bathed.
3. **Stop leading with star names.** Lead with the odd thing ("...cheat sheet in his sock"); the star goes in line 2.
4. **Title tests:** try "When..." and "The real reason..." openers on non-goalkeeper stories.
5. **Hold:** money/transfer (S15-type), Messi-name-led, awards, records, anything number-led.

## 6. Candidate stories (web-checked Nov 1, source links)
Lane: GK = goalkeeper/shootout, FK = fan/kid/family, OT = other.

| # | Story (one oddity) | Lane | Sources | Caution |
|---|---|---|---|---|
| 1 | **Ricardo took his gloves off to save a penalty, then scored the winner** (Portugal v England, Euro 2004, 6-5) | GK | [Wikipedia](https://en.wikipedia.org/wiki/Ricardo_(footballer,_born_1976)), [FourFourTwo](https://www.fourfourtwo.com/features/people-probably-werent-happy-with-me-ricardo-on-breaking-english-hearts-twice), [Sky: Vassell](https://skysports.com/football/news/19692/12012521/darius-vassell-on-englands-golden-generation-and-his-penalty-miss-at-euro-2004) | Sources differ on WHICH kick the gloves came off for; write it true under both |
| 2 | **Goycochea only played because Pumpido broke his leg, then made 4 shootout saves** (Italia 90) | GK | [Wikipedia](https://en.wikipedia.org/wiki/Sergio_Goycochea), [FIFA](https://inside.fifa.com/en/news/behind-the-world-cup-record-sergio-goycochea-2863542) | Injury came 11 min into game 2 vs USSR; saves vs Yugoslavia and Italy |
| 3 | **The England subs brought on only for penalties** (Rashford, Sancho, Euro 2020 final) | GK | [FourFourTwo](https://fourfourtwo.com/news/gianluigi-donnarumma-shines-as-shoot-out-hero-key-moments-from-euro-2020-final-1626041842000), [SI](https://www.si.com/soccer/2021/07/11/italy-england-euro-final-video-highlights-updates-kane-chiellini) | Mirror of S17: the trick backfired. Donnarumma saved Sancho and Saka; Rashford hit the post |
| 4 | **Kepa refused to be subbed for the shootout** (Carabao Cup final, Feb 2019) | GK | [Sky](https://www.skysports.com/football/news/11668/11647428/watch-kepa-arrizabalaga-defies-furious-chelsea-boss-maurizio-sarri-in-carabao-cup-final), [Eurosport](https://www.eurosport.co.uk/football/kepa-arrizabalaga-fined-by-chelsea-for-cup-final-antics_sto7161908/story.shtml), [SI](https://www.si.com/soccer/2019/09/05/kepa-arrizabalaga-not-proud-refusing-come-carabao-cup-final-shootout) | Fined one week's wages; City won 4-3 on pens. Why Sarri wanted Caballero is not sourced yet |
| 5 | **Dibu Martinez threw the ball away from Tchouameni** (2022 final shootout) | GK | [90min](https://www.90min.com/posts/emi-martinez-best-moments-penalty-shithousery-ranked), [Irish Examiner](https://www.irishexaminer.com/sport/soccer/arid-41031272.html), [Football365](https://www.football365.com/news/france-lodge-official-complaint-martinez-argentina-fresh-taunt-tchouameni) | France lodged a formal complaint; stick to documented acts |
| 6 | **Bono saved Spain's penalties; Spain missed all three** (WC 2022 R16, Morocco 3-0 on pens) | GK | [Guardian](https://www.pressreader.com/usa/the-guardian-usa/20221207/282291029267324), [The National](https://thenationalnews.com/fifa-world-cup-2022/2022/12/08/from-montreal-to-seville-via-casablanca-bonos-journey-to-morocco-world-cup-hero) | Sarabia hit the post; Bono saved Soler and Busquets. One outlet says he saved the first three: wrong |
| 7 | **Barthez got his head kissed before every match** (Blanc, 1998); Blanc was suspended for the final and Barthez kept a clean sheet | GK / ritual | [Esquire ME](https://www.esquireme.com/news/what-s-it-like-towin-the-world-cup), [Wikipedia](https://en.wikipedia.org/wiki/Fabien_Barthez) | The ritual began 5 years before 1998 (Barthez); France beat Brazil 3-0 |
| 8 | **Howard's 16 saves**, a World Cup record, in a loss (USA v Belgium 2014) | GK | [Guinness](https://guinnessworldrecords.com/world-records/117157-most-saves-in-a-football-soccer-fifa-world-cup-match), [FIFA](https://www.fifa.com/news/behind-the-world-cup-record-tim-howard-2868575) | Previous record 13 (Quiroga, 1978); the "tracked since" year differs by outlet |
| 9 | **Trautmann played the last ~15 minutes of the 1956 FA Cup final with a broken neck** | GK | [Wikipedia](https://Wikipedia.com/wiki/1956_FA_Cup_final), [Flashscore](https://www.flashscore.fi/news/football-fa-cup-flashback-the-incredible-story-of-trautmann-s-broken-neck-in-fa-cup-final/YgEF3BaM/), [NBC](https://nbcsports.com/soccer/news/the-life-of-bert-trautmann-broken-neck-prisoner-of-war-man-city-legend) | Minutes vary (15-17); X-ray 3 days later; 1956 footage is scarce |
| 10 | **Chilavert scored a hat-trick, all penalties** (Velez 6-1 Ferro, 28 Nov 1999) | GK | [Guinness](https://www.guinnessworldrecords.com/world-records/73511-most-goals-scored-by-a-goalkeeper-in-one-game), [Planet Football](https://www.planetfootball.com/nostalgia/jose-luis-chilavert-hat-trick-penalties-velez-sarsfield-ferril-paraguay) | "First ever" is disputed: skip that claim |
| 11 | **Banks' save from Pele** (1970); Banks missed the quarter-final ill | GK | [FourFourTwo](https://www.fourfourtwo.com/news/gordon-banks-a-world-cup-winner-who-denied-pele-save-century) | Famous save, short old footage |
| 12 | **Higuita's scorpion kick**: Redknapp later called it a bad cross, not a shot | GK | [Goal](https://www.goal.com/en/news/higuita-reveals-inspiration-behind-famous-scorpion-kick-save/blt713451d2aed0c0f7), [Tribune](https://tribune.com.pk/story/952194/scorpion-kick-legend-rene-higuita-recreates-the-moment-on-20th-anniversary) | Redknapp's words are paraphrased in sources; no quotation marks |
| 13 | **Szczesny retired in August 2024, then joined Barcelona** when Ter Stegen tore his patella tendon | GK | [ESPN](https://global.espn.com/football/story/_/id/41437458/barcelona-sign-wojciech-szczesny-ter-stegen-injury), [CFJC](https://cfjctoday.com/?p=989198) | The smoking-in-the-shower story did NOT verify: leave out. Check his Nov 2026 status first |
| 14 | **Rulli scored and saved the 11-10 Europa final; now City's shootout hero** | GK | scripted (S19) | Best of the backlog |
| 15 | **Lamine Yamal's little brother Keyne** on the pitch after the Euro 2024 final | FK | [Getty](https://gettyimages.fi/detail/uutiskuva/lamine-yamal-of-spain-with-his-brother-keyne-yamal-after-the-uutiskuva/2162084477), [Tribune](https://tribune.ie/?p=23433) | "Mascot" is NOT supported: do not say it |
| 16 | **The baby Messi once bathed is now Barcelona's star** (Yamal, 2007 charity photo) | FK | [NTN24](https://www.ntn24.com/noticias-deportes/la-tierna-fotografia-con-la-que-lamine-yamal-recordo-cuando-lionel-messi-lo-bano-siendo-un-bebe-500886), [FMT](https://fmtv5.freemalaysiatoday.com/category/highlight/2024/07/14/from-a-messi-bubble-bath-and-mascot-to-bubbly-phenom) | Check the 2007 date and current shirt number; the 2016 Barca mascot walk-out is a separate fact |
| 17 | **Barcelona signed Messi on a paper napkin** (S20) | OT, object | scripted | Object hook, no shootout: a test of "object beats star" |
| 18 | **Ronaldo moved two Coke bottles** (S09) | OT | scripted | Star-and-brand: weakest lane |
| 19 | Hand of God shirt (S08), already posted: 3.2K | OT | n/a | Proof that object + star + money is not enough |
| 20 | Backlog, not re-verified: Henry, Ronaldinho, Lampard, Cantona, Balotelli (`Idea Bank.md`). Pele's laces needs a better source | OT | `Idea Bank.md` | Each only after the footage test |

Items 1-13 and 15-16 were checked by web search on Nov 1; 14, 17, 18 are existing scripts; 19-20 are not new research.

## 7. Order to make them
1. S19 Rulli (ready, pure goalkeeper lane). 2. #3 England subs for penalties. 3. #1 Ricardo. 4. #2 Goycochea. 5. #4 Kepa. Then one fan/kid test (#16). S20 after; S09 held.
