# S43 The goalkeeper who found out Chelsea's secret penalty plan (script only, Sat Nov 7, 2026)

**Status:** PREP: ready to voice (script + sources, not voiced, not cut). Written by the FC cloud run (no FC gap in the next 54 h). Folder date (Tue Nov 17) is a placeholder ("NEW keeper 3" in the Two-Week Plan).

- **Lane:** goalkeeper + penalty shootout (proven FC lane), odd act you can SEE: Van der Sar points to the side before Anelka's kick.
- **Concept (8 words):** Keeper spots the plan, points, saves the final.
- **Added value:** joins the economist's database (Palacios-Huerta, ESPN), the six kicks in a row to one side (ESPN, Wikipedia), the point, and Van der Sar's own later account, into one timeline; payoff is the irony that the only taker who changed side lost the final.
- **Words:** 224 spoken (Nov 7: trimmed 9 words so the pre-voice gate in script_lint.py passes: "on a rainy night", "So", "strong"); line 1 is 9 words. Expect about 55-58 s; if the take still runs 59.5 s or more, cut "Kalou scored, to his left again." next.
- **12-point rating: 11** (stranger 2: Ronaldo, Terry, a Champions League final; premise 2; footage 2: UEFA + TNT uploads; timing 1: evergreen; sources 2; originality 2: FRESH).
- **Promise words for QA:** `"promise": ["plan", "file", "left", "pointed", "database"]`.

## Claims (every line, with its source)
| Line | Source | Exact wording / value |
|---|---|---|
| 2008 Champions League final, United v Chelsea, rainy night in Moscow, 1-1 after extra time | [CNN, May 21 2008](https://www.cnn.com/2008/SPORT/football/05/21/championsleague.final/index.html); [Wikipedia: 2008 UCL final](https://en.wikipedia.org/wiki/2008_UEFA_Champions_League_final) | CNN: "finished 1-1 after a dramatic 120 minutes of action on a rainy night in Moscow" |
| Chelsea's coach was helped by economist Ignacio Palacios-Huerta, who built a database of thousands of penalties | [ESPN, May 30 2017](https://www.espn.com/soccer/story/_/id/37475605/penalty-shootouts-champions-league-other-cups-tournaments-decided-science) | "Chelsea's coach Avram Grant received help from a Spanish economist named Ignacio Palacios Huerta, who had spent years building a database of thousands of penalties." |
| Ballack, Belletti, Lampard, Ashley Cole, Terry, Kalou: all to Van der Sar's left | ESPN; Wikipedia | ESPN: "all their first six penalty-takers in the shootout kicked to Van der Sar's left"; Wikipedia: Anelka's kick came after "the six players who took their penalties before him" |
| Van der Sar got a strong hand to Cole's, it still went in | Wikipedia | "Van der Sar got a strong hand to the ball but could not keep it out" |
| Ronaldo's penalty saved; Terry slipped and hit the post | CNN; Wikipedia | CNN: "saved by Peter Cech ... Terry's dramatic miss, with the central defender seeming to slip"; Wikipedia: "his mis-hit effort struck the outside of the right post" |
| Kalou scored to his left; sudden death | Wikipedia | "Kalou then sent Van der Sar the wrong way to make it 5–5" |
| Before Anelka's kick Van der Sar pointed to his left | Wikipedia; ESPN; [Mirror, Dec 26 2020](https://www.mirror.co.uk/sport/football/news/manchester-united-chelsea-champions-league-23228638) | Wikipedia: "before his kick, Van der Sar pointed to his left"; ESPN: "Van der Sar pointed with his left hand to the left corner. 'That's where you're all putting it, isn't it?' he seemed to be saying." |
| He dived right and saved; United won 6-5 | [Guardian live, May 21 2008](https://www.theguardian.com/football/2008/may/21/championsleague.manchesterunited6); CNN | Guardian: "beaten Chelsea 6-5 on penalties after Edwin van der Sar got down low to his right and saved from Nicolas Anelka" |
| Later he said he'd heard Chelsea knew he dived right, so their players were told to shoot left | [GiveMeSport, May 21 2022](https://www.givemesport.com/88010692-edwin-van-der-sars-secret-to-saving-nicolas-anelkas-penalty-in-2008-cl-final); [JOE, Oct 2017](https://www.joe.co.uk/sport/edwin-van-der-sar-explains-how-he-saved-chelsea-penalty-in-the-champions-league-final-144387) | "Later on, I heard that Chelsea had also done their homework on me and learned that I usually dived to my right. So I think their players were told to shoot to my left, which most of them did." |
| Six followed the plan; the seventh didn't, and Chelsea lost | ESPN; [The Hard Tackle, 2015](https://thehardtackle.com/2015/football-and-statistics-helping-the-modern-manager-win/) | Hard Tackle: "Anelka did change his tactic and go to the right of the keeper and the penalty was saved" |

- **Wording choices:** the script says "helped by an economist" and "kept going the same way", and never claims Chelsea's players were given a written file (the ESPN account is "received help"; Van der Sar says "I think their players were told"). The title's "secret penalty plan" rests on Van der Sar's own words.
- **Not used:** Palacios-Huerta's other notes (Ronaldo's stutter, kick height); Van der Sar studying about 40 Lampard penalties (JOE; spare line).

## Copy check
`copy_check.py "Van der Sar Anelka pointed"`: **FRESH** (no results). Ahmed's Goal titles: no Van der Sar match. (Cech 2012 checked too: CROWDED, not used.)

## Footage plan (official, verified to exist Nov 7 via `broll.py search`; cut on the PC)
| Beat | Video | Notes |
|---|---|---|
| Frame 1: Van der Sar's point before Anelka's kick (the promise) | TNT Sports `z-QliFMvpqI` "In Full! Manchester United's Dramatic Penalty Shootout Win Over Chelsea" (4:39) | verify the point is in frame; hold 2 s+ |
| Rain in Moscow, 1-1 | UEFA `GieEKm5HI8o` highlights (2:06), `YtzHAkcjHv4` flashback (11:04) | |
| The six kicks to one side | `z-QliFMvpqI` | overlay a running tally "LEFT x1 ... x6" on the play |
| Ronaldo saved, Terry slips | `z-QliFMvpqI` / `YtzHAkcjHv4` | replay Terry's slip once |
| The point, the save, the celebration | `z-QliFMvpqI` | replay the point once, closer, before the payoff |
| Payoff | Anelka walking away / United celebrating | hold 2-3 s, loop frame |

## Package draft
- **Title:** The goalkeeper who found out Chelsea's secret penalty plan
- **Alternatives:** Chelsea had a penalty plan for Van der Sar. He spotted it / The point that won the 2008 Champions League final
- **Pinned comment:** Was the point a bluff, or did Van der Sar really read Anelka?
- **Tags (start):** edwin van der sar, van der sar anelka, anelka penalty, 2008 champions league final, man utd vs chelsea, john terry slip, penalty shootout, palacios-huerta, moscow 2008, ronaldo penalty miss
