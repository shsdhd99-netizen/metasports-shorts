# S38 The goalkeeper who beat a team that practised 1,000 penalties (script only, Sat Nov 7, 2026)

**Status:** PREP: ready to voice (script + sources, not voiced, not cut). Written by the FC cloud run (no FC gap in the next 54 h). Folder date (Sat Nov 14) is a placeholder; the Two-Week Plan has "NEW keeper 1: Bounou" on Wed Nov 11.

- **Lane:** goalkeeper + penalty shootout (our proven FC lane), "versus their own" twist (Bounou played in Spain for Sevilla; Hakimi born in Madrid).
- **Concept (8 words):** Spain's thousand-penalty homework, beaten by one keeper.
- **Added value:** puts Luis Enrique's pre-match "1,000 penalties" homework next to the outcome, his own post-match line about Bounou, and the Opta record (2nd team ever to score none in a World Cup shootout), in one timeline.
- **Words:** 215 spoken; line 1 is 11 words (the limit). Expect about 52-56 s.
- **12-point rating: 11** (stranger 2: World Cup, Busquets, Hakimi; premise 2: goalkeeper-penalty lane; footage 2: FIFA's own uploads; timing 1: evergreen, international break; sources 2; originality 2: FRESH).
- **Promise words for QA:** `"promise": ["penalties", "penalty", "homework", "thousand", "shootout"]`.

## Claims (every line, with its source)
| Line | Source | Exact wording / value |
|---|---|---|
| 2022, Spain v Morocco, last 16 of the World Cup | [RFEF report, Dec 6 2022](https://rfef.es/en/noticias/report-morocco-stops-spains-world-cup-path-in-the-penalty-shootout-0-0-and-3-0) | "XXII FIFA Soccer World Cup Qatar 2022. Round of 16" |
| More than a year earlier Luis Enrique gave homework: at least 1,000 penalties with your club | [Sky Sports report](https://www.skysports.com/football/morocco-vs-spain/report/463019); [Goal, Dec 6 2022](https://www.goal.com/en/news/luis-enrique-spain-1000-penalties-training-world-cup-shootout-heartbreak/blt6882879ff7d633fa) | Sky: "Over a year ago, in many national camps we told players, 'You have homework ahead of the World Cup. You must take at least 1,000 penalties with the club'"; Goal: "Over a year ago, in one of the Spain camps, I told them they had to get here with at least 1,000 penalties taken." |
| Over a thousand passes, one shot on target | [BBC Sport, Dec 6 2022](https://www.bbc.co.uk/sport/football/63789751); Sky (Opta) | BBC: "just one shot on target from their 1,019 passes"; Sky: "Spain recorded just one shot on target across the 120 minutes" |
| Bounou kept it out; nil-nil after extra time | BBC; RFEF | 0-0 a.e.t. (so the one shot on target was saved); BBC: Olmo's drive "which Bounou pushed away" |
| Sarabia sent on in the last minute, apparently for the shootout | [AP via KOSU](https://www.kosu.org/sports/sports/2022-12-06/morocco-shocks-spain-to-become-the-first-arab-team-to-reach-the-world-cups-final-8); RFEF | AP: "Sarabia had entered the match in the final minutes of extra time, apparently for the shootout"; RFEF line-up: "Sarabia 119´" |
| He hit the post in the last play of extra time | RFEF; [AFP via Dawn](https://www.dawn.com/news/1724980) | RFEF: "Pablo Sarabia took a shot to the post in the last play of extra time"; AFP: "Pablo Sarabia clipping the outside of the post, although he might have been offside" |
| He took Spain's first kick and hit the post again | AFP (Dawn); RFEF | AFP: "Sarabia struck the post again from Spain's first penalty"; RFEF: "Sarabia, to the post" |
| Soler saved, Busquets saved by Bounou | RFEF; [CNN](https://www.cnn.com/2022/12/06/football/morocco-spain-qatar-world-cup-spt-intl/index.html) | RFEF: "Carlos Soler, to Bono ... Sergio Busquets, to Bono"; CNN: "saving efforts from Sergio Busquets and Carlos Soler" |
| Hakimi, born and raised in Madrid, chipped the winner down the middle | BBC; CNN | BBC: "Achraf Hakimi made himself a hero with a chipped winning penalty ... born and raised in Madrid no less"; CNN: "nerveless 'Panenka' penalty" |
| Morocco won 3-0, first quarter-final ever | BBC; [NPR/AP](https://www.npr.org/2022/12/06/1140967981/morocco-spain-world-cup-upset-penalties-yassine-bounou) | BBC: "reached the last eight for the first time" |
| Luis Enrique wished he could take Bounou out | AP (KOSU) | "The only thing I wished I could do was to take Bounou out and put another goalkeeper in there." |
| Bounou played his club football in Spain, for Sevilla | AP (KOSU) | "Yassine Bounou, who plays for Spanish club Sevilla" (Dec 2022) |
| Spain: only the second team ever to score none in a World Cup shootout | Sky (Opta); Goal; [Mirror](https://www.mirror.co.uk/sport/football/news/spain-enrique-morocco-worldcup-penalties-28670369); [BBC 2006](http://news.bbc.co.uk/sport2/hi/football/world_cup_2006/4991532.stm) | Sky: "they've become just the second side to not score in one after Switzerland against Ukraine in 2006" |

- **Wording choices:** "apparently just for the shootout" keeps AP's qualifier. The script never says Bounou knew Spain's takers (not sourced). "Hit the post again": the extra-time post may have been offside (AFP), so it is "the final play", not "a chance".
- **Not used:** Spain the first nation to lose four World Cup shootouts (Opta; spare line if the take runs short); 77% possession (Sky).

## Copy check
`copy_check.py "Spain 1000 penalties Bounou"`: **FRESH** (top: Highlights 807 views, euronews 644). Ahmed's Goal titles: no Bounou / 1,000 penalties match.

## Footage plan (official, verified to exist Nov 7 via `broll.py search`; cut on the PC)
| Beat | Video | Notes |
|---|---|---|
| Frame 1: Bounou saves Busquets (the promise) | FIFA `yF5mHzhRBWE` "Morocco vs Spain: Full Penalty Shootout" (6:03, 14M views) | hold 2 s+ under the title card |
| Luis Enrique on the bench / presser | FIFA full match `ci4vyd6PsNg` (138:56) | bench shots; no card for the quote (captions carry it) |
| Passing, the one shot on target, Bounou's save on Olmo | FIFA full match / `NBDAna_qxY8` | words over the play: "1,019 PASSES", "1 SHOT ON TARGET" |
| Sarabia's post in the last play of extra time, then his penalty off the post | full match (end of ET) + `yF5mHzhRBWE` | replay the post once, closer |
| Soler save, Busquets save, Hakimi's chip, celebration | `yF5mHzhRBWE`, `hwf_dyqHVA8` | payoff on Spain's empty-handed walk; overlay "0 OF 3" |
| Payoff: "second team ever to score none" | shootout end | hold 2-3 s, loop frame |

## Package draft
- **Title:** The goalkeeper who beat a team that practised 1,000 penalties
- **Alternatives:** Spain practised 1,000 penalties and scored none / The goalkeeper Spain wished they could take off
- **Pinned comment:** Was it Bounou, or did Spain's homework never stand a chance?
- **Tags (start):** yassine bounou, bono, morocco vs spain, morocco spain penalties, world cup 2022, penalty shootout, luis enrique 1000 penalties, busquets penalty, hakimi panenka, sarabia post
