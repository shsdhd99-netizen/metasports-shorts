# S05 Goalkeepers who hid a cheat sheet on their water bottle (DRAFT, rendered Oct 24, 2026)

> **STATUS (Oct 24, new account, cloud session): FIXED AND RENDERED, 59.7 s, QA PASS (music and no-music).**
> No ElevenLabs key on this account, so every fix below is a cut or a splice from the same take (`Tools/word_edit.py`); the original take is in `_voice_preedit_v1/` (git-ignored, local only).
> 1. **"dived to his left" -> "Pickford dived, threw up his arm, and saved it."** Cut "to his left," (31.735-32.28 s). I checked the 4K broadcast frame by frame: the wide shot from behind Bacca and the reverse angle from behind Pickford both show him diving to his RIGHT with his left arm up (AP/Daily Star were right). The picture now shows exactly that (A22 live, A22b reverse angle).
> 2. **"the Argentina players found" -> "Argentina found"** (spliced "Argentina" from 54.58-55.05 s of the same take). True whether staff or players picked it up.
> 3. **"And they couldn't stop laughing." cut.** The Short now ends on "...the note reportedly just said, feel on the day." over a close-up of that line on the bottle. Ending on the absurd note is a stronger payoff than the laugh line anyway.
> 4. **Falcao sentence cut** ("Afterwards, Pickford said only one Colombian, Radamel Falcao, had shot differently from what he expected.") to get under 60 s (new rule: a claimed Short over 60 s is blocked worldwide). It was true (The FA, Pickford's own words), just the least needed beat.
> - Every joint checked with local speech-to-text: "Pickford dived, threw up his arm, and saved it. Eric Dier scored..." / "...and passed it to Messi. Next to one player's name, the note reportedly just said feel on the day."
> - Footage: 2018 from the FIFA 4K HDR broadcast (only the used minutes pulled and tone-mapped to 1080p, `src/pull4k.sh`); Euro 2020 final from the BBC 720p broadcast; 2026 from the photos in `assets/` (credits on the cards). Every shot is in `sources.csv` and was checked on `_check/sheet.jpg`. A38 (a ball on the 2018 penalty spot under "so there was no shootout") is illustrative.
> - The fact-check table below is the Oct 23 one; the rows marked WRONG / NEEDS REWORDING are the lines fixed above.

## Fact check (Oct 23, 2026)

> **READ FIRST: 1 WRONG line, 2 to reword. Fix before cutting footage.**
> 1. **WRONG (line 11): "Pickford dived to his left, threw up his arm, and saved it."** He went to his **right** and saved it with his **left** hand.
>    - AP play-by-play: Bacca hit a rising ball "to Pickford's right"; Pickford "beat the ball away with his left hand thrust high".
>    - The Daily Star: "leapt to his right and got a strong left hand".
>    - **Cheapest fix (no new voice):** cut the words "to his left," from `voice.mp3`, 31.755-32.307 s in the current `words.json`. The line becomes "Pickford dived, threw up his arm, and saved it." Then shift the later word times in `words.json` and `captions.srt` back by about 0.55 s.
>    - **Or re-voice the line:** "Pickford dived to his right, threw up his left hand, and saved it."
> 2. **NEEDS REWORDING (line 19): "the Argentina players found his bottle on the pitch, and passed it to Messi."** Sources disagree on who found it.
>    - **Staff:** ThePrint ("backroom staff"), Goal ("coaching staff collected it... handed it to Messi"), and crhoy, which names the masseur, Marcelo D'Andrea.
>    - **Players:** AAP ("stumbled upon the bottle"), FourFourTwo and People.
>    - **Fix that is true under both (a cut, no new voice):** remove "the" (59.138-59.208 s) and "players" (59.614-59.823 s). The line becomes "And after the game, Argentina found his bottle on the pitch, and passed it to Messi."
> 3. **NEEDS REWORDING, minor (last line): "And they couldn't stop laughing."** "Couldn't stop" is not in any source.
>    - AAP: Messi and his teammates "laughed as they studied the notes".
>    - Goal: Enzo Fernández was "seen laughing".
>    - ThePrint: they "shared a chuckle".
>    - People: Messi "appeared to look confused".
>    - **Suggested re-voice of the last sentence only:** "And they burst out laughing." It is the last line, so splice at about 65.0 s. Or accept it as an exaggeration if the owner prefers; the other lines are all sourced.
>
> Everything else is CONFIRMED. If you re-voice rather than cut, record all three fixes in one take (about 1,700 credits, `Tools/voice_take.py`).

- **Format:** story format. The title is read as line 1, then "Back in 2018", a turn every 8-12 s, and an ironic payoff. No teaser.
- **Lane / theme:** records and "looks fake but is real" (332K), plus the "Goalkeepers who..." series (S01, S03). Global names: Messi, Pickford, Falcao.
- **Concept (8 words):** Pickford's penalty cheat sheet, from Bacca to Messi.
- **Added value:** four details beyond the usual "Messi found the bottle" clip:
  - the towel he used to hide the bottle from Ospina;
  - Pickford's own line that Falcao was the only taker who went the other way;
  - the bottle again in the Euro 2020 final;
  - the "feel on the day" note found by Argentina in 2026.
- **Ahmed's Goal title grep (Oct 23):** nothing on Pickford, the water bottle or a "cheat sheet".
- **Voice:** Alex, take 1, passed the gate (HNR 8.8, jitter 2.76, shimmer 11.09). 256 words, 66.4 s after tightening.

## Script lines -> sources
| # | Line | Source | Exact quote (under 15 words) | Verdict |
|---|---|---|---|---|
| 1 | Goalkeepers who hid a cheat sheet on their water bottle. | Sky Sports, Jul 5 2018: https://www.skysports.com/football/news/12016/11426736/englands-jordan-pickford-handed-colombia-penalty-information-on-water-bottle | "was handed a drinks bottle that had information about Colombia's penalty takers" | CONFIRMED |
| 2 | Back in 2018, England played Colombia at the World Cup, | ESPN match report, Jul 3 2018: https://www.espn.com/soccer/report?gameId=498147 | (Colombia 1-1 England, round of 16, Jul 3 2018) | CONFIRMED |
| 3 | and England had never won a World Cup penalty shootout. | The42: https://the42.ie/4107086 | "a first ever in the World Cup" | CONFIRMED |
| 4 | They lost in 1990, in 1998, and in 2006. | ESPN (row 2) | "the 1990, 1998 and 2006 World Cups ended in shootout losses" | CONFIRMED |
| 5 | Then, deep into stoppage time, Yerry Mina headed in an equalizer for Colombia. | ESPN (row 2) | "headed in a corner in the third minute of stoppage time" | CONFIRMED (93rd minute) |
| 6 | It went to penalties again. | ESPN (row 2) | (same report) | CONFIRMED |
| 7 | But England's goalkeeper, Jordan Pickford, had a secret. His water bottle had notes on it, showing where each Colombian player liked to shoot. | Sky Sports (row 1) | "detailed where the Colombian players preferred to put their penalties" | CONFIRMED |
| 8 | And when he walked past Colombia's keeper, he covered it with a towel. | Sky Sports photo caption (row 1). El Espectador: https://www.elespectador.com/especial-mundial-rusia-2018/una-botella-el-secreto-de-los-ingleses-en-los-penaltis-ante-colombia | "covered the bottle with a towel when near Colombia goalkeeper David Ospina" / "cubrió la botella con una toalla" | CONFIRMED ("when near" covers "walked past") |
| 9 | England missed their third kick. | AP via Fox Sports, Jul 3 2018: https://www.foxsports.com/stories/soccer/the-world-cup-penalty-shootout-between-england-and-colombia. ITV: https://itv.com/news/2018-07-03/world-cup-2018-england-v-colombia | "Jordan Henderson saw his spot-kick saved by goalkeeper David Ospina" | CONFIRMED (Kane, Rashford, then Henderson) |
| 10 | But then Mateus Uribe smashed Colombia's next one onto the crossbar. | AP (row 9). CBC: https://amp.cbc.ca/sports/soccer/worldcup/england-edge-colombia-on-penalties-to-reach-quarter-finals-1.4732427 | "struck the underside of the crossbar and bounced out to safety" / "blasted the ball into the bar" | CONFIRMED |
| 11 | And when Carlos Bacca stepped up, Pickford dived to his left, threw up his arm, and saved it. | AP (row 9). The Daily Star: https://www.thedailystar.net/fifa-world-cup-2018/pickford-gets-the-upper-hand-1600075. Reuters via Onmanorama: https://www.onmanorama.com/sports/football/2018/07/04/pickford-the-hero-as-england-s-penalty-curse-ends.html | "Carlos Bacca hit a rising ball to Pickford's right." / "leapt to his right and got a strong left hand" / "shoot his left arm up to paw away Bacca's high shot" | **WRONG.** The dive was to his right; the left arm is right. Fix: see READ FIRST 1. |
| 12 | Eric Dier scored, and England had finally won a World Cup shootout. | AP (row 9). The42 (row 3) | "placed his shot low toward the left corner" | CONFIRMED (4-3 on penalties) |
| 13 | Afterwards, Pickford said only one Colombian, Radamel Falcao, had shot differently from what he expected. | The FA, Jul 3 2018 (Pickford): https://www.thefa.com/news/2018/jul/03/england-colombia-player-reaction-030718. Sky Sports (row 1) | "Falcao was really the only one who didn't go his way." | CONFIRMED (his own words) |
| 14 | So Pickford kept the trick. In the Euro 2020 final against Italy, he had his bottle again, | Open (Italy), Jul 14 2021: https://www.open.online/2021/07/14/euro-2020-rigori-arma-segreta-portiere-inglese-jordan-pickford-borraccia-appunti-su-come-calcia-ogni-giocatore-italiano | "Sulla borraccia di Pickford erano presenti tutti i nomi degli Azzurri" | CONFIRMED. Second-tier source: the photo is by Kevin Quigley (EURO20 Newspapers), and a Daily Mail headline says the same. |
| 15 | and he saved two penalties, but England still lost. | Football365: https://www.football365.com/news/england-1-1-italy-2-3-pens-three-lions-beaten-on-penalties. CNBC: https://www.cnbc.com/2021/07/11/italy-beats-england-in-a-shootout-at-the-euro-2020-soccer-championship.html | "Jordan Pickford denied Andrea Belotti and Jorginho" / "in a 3-2 shootout defeat" | CONFIRMED |
| 16 | This summer, England played Argentina in the World Cup semi-final, | GV Wire (Reuters), Jul 15 2026: https://gvwire.com/2026/07/15/holders-argentina-beat-england-2-1-to-set-up-world-cup-final-against-spain/ | "Holders Argentina beat England 2-1 to set up World Cup final against Spain" (headline) | CONFIRMED (Atlanta, Jul 15 2026). "This summer" will date the video; fine for 2026. |
| 17 | and Pickford had the bottle ready one more time. | FourFourTwo, Jul 16 2026: https://www.fourfourtwo.com/person/player/argentina-players-discover-jordan-pickfords-penalty-cheat-sheet-on-water-bottle | "Argentina's players spotted it on the pitch following the full-time whistle" | CONFIRMED (the bottle lists every Argentina taker) |
| 18 | But Argentina scored in the 85th and the 92nd minute, so there was no shootout. | GV Wire (Reuters), row 16 | Enzo Fernández 85th, Lautaro Martínez 92nd: "stoppage-time goal" | CONFIRMED (England led through Gordon, 55') |
| 19 | And after the game, the Argentina players found his bottle on the pitch, and passed it to Messi. | ThePrint: https://theprint.in/sport/fifa-world-cup-2026/argentina-england-goalkeeper-jordan-pickford-penalty-cheat-sheet-fifa-world-cup/2988042/. Goal: https://www.goal.com/en/lists/video-lionel-messi-inspects-jordan-pickford-penalty-notes-argentina-england-world-cup/blt480ecf2b212d285e. AAP: https://www.countrynews.com.au/aap-soccer/message-in-a-bottle-argentina-find-pickfords-notes/. crhoy: https://crhoy.com/deportes/la-botella-de-pickford-con-apuntes-que-acabo-en-manos-de-messi-y-desato-risas | "Quien la encontró fue el masajista de la Albiceleste" / "stumbled upon the bottle after the final whistle" | **NEEDS REWORDING.** Staff or players: sources disagree. Cut "the" and "players" (READ FIRST 2). |
| 20 | Next to one player's name, the note reportedly just said, feel on the day. | FourFourTwo (row 17). Sportbible, Jul 16 2026: https://www.sportbible.com/football/football-news/fifa-world-cup/lionel-messi-argentina-jordan-pickford-water-bottle-368523-20260716 | Almada: "FEEL ON THE DAY" / "simply read 'feel on the day'" | CONFIRMED (Thiago Almada; the photo in `assets/card_bottle.jpg` shows it) |
| 21 | And they couldn't stop laughing. | AAP (row 19). Goal (row 19). Yahoo / People: https://sports.yahoo.com/articles/lionel-messi-discovers-england-goalie-172816509.html | "Messi and his teammates laughed as they studied the notes" / "seen laughing" | **NEEDS REWORDING (minor).** "Couldn't stop" overstates it; use "burst out laughing" (READ FIRST 3). |

## Footage needed (one moment per line)
Sources: archive.org 2018 Colombia v England (4K) and `euro-2020-final` (BBC 720p), as listed in `CLOUD STATE - read this first.md`. The 2026 photos are in `assets/` (X posts via @FabrizioRomano and @TouchlineX, TyC Sports pictures).
1. Title card: `assets/bottle_crop.jpg` or `card_bottle.jpg` (the bottle itself).
2. "Back in 2018, England played Colombia": the line-ups or the anthem, Moscow, Spartak Stadium.
3. "never won a World Cup shootout": a graphic card (England's World Cup shootouts: 0 wins).
4. "1990, 1998, 2006": a quick shot of each loss if archive.org has it (Waddle 1990, Batty 1998, Carragher 2006); otherwise one card with three years.
5. "Mina headed in an equalizer": the 93' header.
6. "went to penalties again": players gathering in the centre circle.
7. "water bottle had notes": Pickford drinking from the bottle before the shootout; zoom in on the writing if it is visible.
8. "covered it with a towel": Pickford with the towel on the bottle near Ospina. Use the broadcast shot if it exists; if not, mark the shot "illustrative".
9. "England missed their third kick": Ospina saving from Henderson.
10. "Uribe... onto the crossbar": the bar hit.
11. "Bacca... saved it": the save. **The picture must show him going to his own right** (the left of the screen from behind the goal); it must not match the old wording.
12. "Dier scored": Dier's penalty and England's celebration.
13. "Falcao shot differently": Falcao's penalty (Colombia's first kick).
14. "Euro 2020 final... bottle again": Pickford with the bottle at Wembley.
15. "saved two penalties, but England still lost": the Belotti save, the Jorginho save, then Italy celebrating.
16. "This summer... semi-final": the England v Argentina 2026 semi-final. No archive.org copy, so use X clips (`Tools/x_clip.py`) or a card.
17. "bottle ready one more time": `assets/x_4999_*.jpg` (the bottle on the pitch).
18. "85th and 92nd minute": Enzo's strike and Lautaro's header (X clips or card), with the minutes on a card.
19. "found his bottle... passed it to Messi": `assets/card_messi.jpg` (its caption, "Argentina staff hand Messi the bottle", matches the fixed line).
20. "feel on the day": `assets/card_bottle.jpg` (Almada boxed in red).
21. Payoff: Argentina players laughing over the bottle (TyC Sports clip via X). This is the last picture.

**Rights:** broadcast clips (2018, 2021) and X photos and clips (2026). Keep clips short, with narration over them; credit the photos on the card.
