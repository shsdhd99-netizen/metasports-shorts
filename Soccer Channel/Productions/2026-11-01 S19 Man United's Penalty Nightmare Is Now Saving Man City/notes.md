# S19 Man United's penalty nightmare is now saving Man City (Oct 30, 2026; FC daily run, script only)

> **Status: script and notes only.** `cloud_setup.sh` printed `key: MISSING` (no `ELEVENLABS_API_KEY` in the environment), so no voice, render or QA. Nothing faked. Once voiced: check the length (186 words, expect about 50-52 s at S18's pace; if it runs over 59.5 s, cut a sentence, never add one).

- **Lane:** topical question answered with a story (this week's League Cup shootout + the 2021 final). Also fits the goalkeeper series (S01, S03, S05 = 30K, 15K, 28K), but S17 is a goalkeeper Short too, so post S19 at least one post after S18 to keep the series at most 1 in 3... it is 2 in 3 if posted right after S18 (S17 GK, S18 revenge, S19 GK). **Post after one non-goalkeeper Short** if one is ready; otherwise note the exception in the Outcome Log.
- **Concept:** the keeper who ended United's 2021 final now keeps City alive; City had already signed him once and never played him.
- **Stranger test:** Man United, Man City, a goalkeeper saving the other goalkeeper's penalty after 21 straight goals: passes (spectacle + the biggest clubs).
- **Copy check:** `copy_check.py "Rulli saved De Gea penalty"`: FRESH (top result 1.5K views).
- **Frame 1:** Rulli's dive saving De Gea's kick (2021 shootout). Line 1 names United's nightmare; the picture shows it.
- **Music test:** S15 music, S16 none, S17 music, S18 none, so S19 = **music** side.

## Claims and sources
| Line | Source | Exact words |
|---|---|---|
| 2021 Europa League final, Villarreal v Man United, 1-1 after extra time, 11-10 on penalties | AFP via [Ahram](https://english.ahram.org.eg/News/413005.aspx); [Gulf News](https://gulfnews.com/sport/football/europa-league-villarreal-down-manchester-united-in-epic-penalty-shootout-to-lift-trophy-1.1622068453381) | "Villarreal defeated Manchester United 11-10 on penalties to win their first major trophy after a 1-1 draw" |
| Every outfield player on both teams scored; down to the goalkeepers | AP via [KEYT](https://keyt.com/sports/2021/05/26/villarreal-defeats-manchester-united-in-dramatic-penalty-shootout-to-win-europa-league/) | "all 10 outfield players from both teams made their penalties in the shootout — leaving it up to the two goalkeepers to take the 11th" |
| Rulli scored, then saved De Gea's; 21 in a row before it | [SI, May 26 2021](https://www.si.com/soccer/2021/05/26/europa-league-final-villarreal-manchester-united-de-gea-penalty-kicks) | "The previous 21 in Wednesday's Europa League final had been scored"; Rulli "had scored what wound up being Villarreal's decisive kick"; "David De Gea saw his effort saved by Gero Rulli" |
| De Gea hadn't saved a penalty in five years | [SI, May 26 2021](https://www.si.com/soccer/2021/05/26/europa-league-final-villarreal-manchester-united-de-gea-penalty-kicks) | "De Gea, who has not saved one since April 2016" |
| He hadn't saved a single kick all night | follows from 11 Villarreal kicks, all scored (above) | |
| Villarreal's first major trophy | AFP (above); SI: "the first major European trophy in its history" | |
| This summer City signed Rulli as Donnarumma's backup | AP, Aug 12 2026 (headline "Man City signs Argentina international Rulli as back-up goalkeeper to Donnarumma", e.g. [Times Argus](https://www.timesargus.com/sports/pro_national_sports/man-city-signs-argentina-international-rulli-as-back-up-goalkeeper-to-donnarumma/article_73a29975-6abf-5d75-a8e0-30cffe290f45.html)); [theScore](https://www.thescore.com/news/3578653) | theScore: two-year deal |
| Oct 28 2026: holders City, at home, came from behind twice, 2-2 v Brighton; 4-3 on pens; Kovačić's saved; Rulli saved Ayari and Dunk | AP via [ClickOnDetroit](https://www.clickondetroit.com/sports/2026/10/28/man-city-wins-penalty-shootout-to-advance-in-english-league-cup/); [SI](https://www.si.com/soccer/man-city-player-ratings-vs-brighton-survive-penalties-10-28-26) | "City stayed on course to retain the title by twice coming from behind to draw 2-2 with Brighton at home... then triumph 4-3 in the shootout"; "Backup goalkeeper Gerónimo Rulli saved Brighton's last two spot kicks — from Yasin Ayari and Lewis Dunk — to rescue City, which had fallen behind in the shootout when Mateo Kovacic had the team's fourth penalty saved" |
| City had signed him in 2016; he left without playing a game | [theScore](https://www.thescore.com/news/3578653) | "spent the 2016/17 season at the Etihad without making a first team appearance" (he was loaned out; "a single game for them" = first-team game) |

**Caution:** don't say "his first game for City" (not checked whether he played earlier League Cup rounds). Don't name a fee (only one source, Eastern Eye, gives £1.7M).

## Footage (checked Oct 30)
- **2021:** UEFA's "VILLARREAL VS MAN UNITED EUROPA LEAGUE FINAL | FULL PENALTY SHOOTOUT" (YouTube X_NSB3CnHoo, 12.7M views); TNT Sports full shootout (vN5Tls-TBaI); UEFA Official Film (ANEBe331IKQ).
- **2026:** Man City "EXTENDED HIGHLIGHTS | Man City 2-2 Brighton | City go through on pens! (4-3)" (FYOQPzXc4T4, 2.2M); EFL extended highlights (e9T4cngiGaw, 1.1M).
- **Blocker:** YouTube refuses downloads from the cloud ("Sign in to confirm you're not a bot"). Download on the PC, or look for the same clips on X (`Tools/x_clip.py`: @ManCity, @Carabao_Cup, @EuropaLeague). archive.org has only BBC news bulletins of May 27 2021 (not the match).
- 2016 line: a 2016 photo/clip of Rulli in City colours if one exists; otherwise him on the City bench in 2026 (illustrative).

## Beats (for the cut plan, about 1.1-2.1 s a picture)
1. Line 1: Rulli's save on De Gea (slow 0.5x on the replay angle later) — frame 1.
2. 2021 final: walk-out / scoreboard 1-1 / the shootout kicks fast (five each, ten each).
3. Rulli scores; De Gea walks up; the save; Villarreal celebrate (replay the save once before "11-10").
4. 2026: Rulli on City's bench / warm-up; Brighton match goals; Kovačić's saved kick; Ayari save; Dunk save; City celebrate.
5. Payoff: 2016 Rulli in City colours (or caption "2016: signed by City / 0 games") — end on it, nothing after.
