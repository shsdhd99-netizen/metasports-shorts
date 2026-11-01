# S20 Barcelona signed Messi on a paper napkin (built Oct 31, 2026, Account 2; DRAFTS, nothing posted)

- **Lane:** secret object (the napkin) about the biggest name in the sport. Not a goalkeeper Short.
- **Concept in 8 words:** A napkin signed Messi; Barcelona later couldn't keep him.
- **Added value:** the 2021 mirror (the club that signed him on a napkin could not register his new contract) and the napkin's 2024 price. The napkin story alone is well known (copy check: `copy_check.py "Messi napkin contract"` FRESH, top 738 views).
- **Length:** 227 words, voice 56.5 s after `tighten_voice.py` (ends before 59.5 s). First take passed the voice gate (HNR 8.4, jitter 2.83, shimmer 10.63).
- **Music test:** S17 music, S18 none, S19 music, so S20 = no-music side. Both rendered.
- **Re-verified Oct 31:** NPR/OPB, 90min, SI 2012, Al Jazeera and AP/WJLA were re-read. Changes from the first script: "sporting director" dropped (the napkin says "technical secretary", Lacueva "technical director", Minguella "football advisor"); "two of Messi's agents" became "two of the men behind the move" (Minguella is a transfer adviser, Gaggioli an agent); the "ten or twelve years" line is attributed ("According to one of the men who brought him there"); "A formal contract followed" is true under both accounts (NPR: Gaspart "formally confirmed the agreement with a more orthodox-looking contract" that night; SI: junior contract signed March 2001). "Couldn't afford to register" became "financial and structural obstacles stopped it" (Barcelona's own words).

## Claims and sources
| Line | Source | Exact words |
|---|---|---|
| Rosario kid, growth hormone treatment, about $1,000 a month, Newell's and River both wanted him, neither could afford it | [SI, Feb 6 2012 (Balagué extract)](https://www.si.com/soccer/2012/02/06/barca-extract) | "although coveted by both Newell's Old Boys and River Plate... neither club can afford the approximate $1000 per month across two years for the growth hormone treatment"; opening "Rosario, Argentina, 2000". The figure is "approximate", so the script keeps "Reportedly" |
| Went to Barcelona for a trial, the club was slow | SI 2012; [90min](https://www.90min.com/lionel-messi-contract-napkin-sells-staggering-amount-auction) | SI: "a player taking trials at Barça, a certain Leo Messi"; 90min: Messi "had been on trial with Barca", "the club's lack of movement in offering a contract" |
| "According to one of the men who brought him there, Barcelona said it would be ten or twelve years before they saw the benefit" | SI 2012 (Minguella) | "Barça were not too interested. They said, 'It will be 10 or 12 years before we see the benefit'." |
| His father was reportedly tired of waiting | 90min; SI | 90min: father Jorge "had reportedly grown frustrated"; SI: "Jorge Messi was tired of being messed about" |
| 14 December (2000), Barcelona's Carles Rexach, lunch at a tennis club, two of the men behind the move | [NPR via OPB, May 18 2024](https://opb.org/article/2024/05/18/napkin-securing-lionel-messi-s-first-contract-fetches-nearly-1-million-at-auction); 90min; SI | NPR: "The napkin is dated Dec. 14, 2000", lunch at the Pompeia Tennis Club, Rexach "wrote and signed" it; 90min: "transfer advisor Josep Minguella and ... Horacio Gaggioli" present; SI: "In Barcelona on the 14th of December 2000 and in the presence of Mr Minguella" |
| He agreed, "regardless of any dissenting opinions", to sign the player Lionel Messi | NPR; 90min | "hereby agrees, under his responsibility and regardless of any dissenting opinions, to sign the player Lionel Messi" |
| Messi was thirteen | NPR; 90min; AP | NPR: "was just 13 years old"; 90min: "aged only 13"; AP (WJLA): arrived "as a 13-year-old". **Conflict:** SI's extract opens "Leo Messi is 12 years old" (Rosario, 2000). Born 24 June 1987 (general knowledge, not in these sources), so 13 in Dec 2000 |
| A formal contract followed | NPR; SI | see above (Gaspart that night; junior contract March 2001) |
| All-time top scorer, 672 goals | [AP via WJLA, Aug 8 2021](https://wjla.com/news/nation-world/messi-breaks-down-says-he-wasnt-ready-to-leave-barcelona-08-08-2021); [Al Jazeera, Aug 5 2021](https://www.aljazeera.com/sports/2021/8/5/messi-to-leave-barcelona-due-to-financial-structural-obstacles) | AP: "all-time leading scorer with 672 goals" (778 appearances); Al Jazeera: "Barcelona's all-time leading scorer, with 672 goals in 778 appearances" |
| 2021: Barcelona said they had agreed a new contract; financial and structural obstacles stopped it | Barcelona statement, Aug 5 2021 (Al Jazeera) | "Although an agreement has been reached between FC Barcelona and Leo Messi... it cannot be formalised due to economic and structural obstacles" (first-pass quote: "financial and structural obstacles (Spanish La Liga regulations)") |
| Messi cried at his goodbye; said he was not ready to leave | AP (WJLA) | headline "Messi breaks down, says he wasn't ready to leave Barcelona"; he "cried profusely as he stepped up to the podium at the Camp Nou" |
| Three years later the napkin sold at auction for 762,400 pounds, almost a million dollars | NPR | sold by Bonhams "for 762,400 British pounds (about $968,600)"; starting bid 300,000 pounds; article dated May 18 2024 |
| "Money problems pushed Messi out of Barcelona" | Barcelona statement; AP headline | the club's own words: "economic and structural obstacles"; a summary, not a quote |

**Cautions kept in the script:** Barcelona did not sell the napkin (sold on behalf of agent Gaggioli); the napkin is not a full contract (Gaspart's contract followed); only "two of the men behind the move" at the lunch (NPR also lists Messi and his father; 90min lists Minguella and Gaggioli); no "there was no paper" claim; the diagnosis is only "growth hormone treatment".
**Title line:** "Barcelona signed Messi on a paper napkin" is how NPR and most outlets put it; the body makes clear a formal contract followed.

## Footage list (every shot is in `sources.csv`)
| Clip | Source | Licence / status |
|---|---|---|
| N01, N22, N35, N38 (napkin, circled words, sold price, final) | `assets/make_napkin.py`: a **RECREATION**, labelled "recreation" on the picture. The real napkin is only a licensed Bonhams/AP photo, not used. Wording is the NPR/90min translation | own graphic; **illustrative, flagged** |
| N02, N09, N13, N23, N26, N27, N28 (Messi at Barcelona) | archive.org `la.liga.d34.real.madrid.vs.fc.barcelona.1st.half.1080i.hdtv`, "highlights" file (854x480): Real Madrid 2-6 Barcelona, 2 May 2009 | fan upload of a broadcast (the repo already uses these); **illustrative: 2009, not 2000 or the record years** |
| N32, N33, N37 (Messi in tears) | X post https://twitter.com/footballontnt/status/1424315098378739713 (Football on TNT Sports, Aug 8 2021, 23 s, 720x720) via `Tools/x_clip.py` | third-party copyrighted clip; logged in `src/downloads.csv`; a claim is possible |
| N03, N24 (kids' football) | Mixkit 6652 | free licence; **illustrative, not Messi** |
| All other shots (syringe 20834, vial 33734, bill counter 45703, crowd 9585, cash 47517/47005, ball 738, stadium 14190/30312/4262, paper and signing 23115/241, path 48514, restaurant 29050, meal 32457, tennis 877, writing 16139, gavel 47687/46820, bills 24061) | Mixkit stock | free licence, commercial use OK; **illustrative for abstract lines** |

**Dropped:** BBC Sportsday / News at Ten recordings of the 2021 farewell on archive.org (`BBCNEWS_20210808_173000_Sportsday`) return 401 (access-restricted); no workaround tried. Rexach and Minguella have no footage, so their lines run on stock.

## Pitfalls hit (for the main account to file)
- `qa_short.py` export check downmixes with `-ac 1` (unnormalised sum), so a dual-mono mix limited at -2 dBFS reads as clipped (+0.9 dBFS). The no-music render failed until the final audio was re-limited (`alimiter=limit=0.68`); loudness stayed -14.1 LUFS. Suggested tool fix: normalise the downmix in `export_check.pcm`, or use limit 0.68 in `assemble.py`'s no-music tail.
- `assemble.py --out-name` was ignored (output is always `final.mp4`); copied by hand.
- The `cut_list.py` contact sheet and `stock.py --sheet` fail on this PC (fontconfig/drawtext); `_check/mysheet.jpg` was made with Pillow.
- archive.org items flagged access-restricted return 401 on the download URL although `/metadata` lists the files.
