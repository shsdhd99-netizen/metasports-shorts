# S05 Goalkeepers who hid a cheat sheet on their water bottle (DRAFT, awaiting approval)

- **Format:** the story format (`.claude/skills/story-short/FORMAT.md`): title read as line 1, "Back in 2018", a turn every 8-12 s, payoff on an absurd detail. No teaser or follow ask. Pauses tightened with `Tools/tighten_voice.py`.
- **Lane / theme:** records and oddities, plus the "Goalkeepers who..." series (S01, S03). Global names: Pickford, Messi, Falcao, Kane.
- **Concept (8 words):** Pickford's bottle trick, from Moscow to Messi laughing.
- **Added value:** the whole arc in one story: the 2018 bottle (and the towel he hid it under), the Euro 2020 repeat, and the 2026 semi-final bottle that Argentina found, with the one note that says nothing.
- **Copy-check, Oct 24:** `copy_check.py "Pickford water bottle cheat sheet"`: FRESH (biggest: 60K, HAGAMOS TENDENCIA; MARCA 12.7K on the 2026 bottle only). Ahmed's Goal titles: nothing on Pickford.
- **Runtime:** 66.4 s, 254 words. Voice: Alex, take 1 (passed the voice gate: HNR 8.8, jitter 2.76, shimmer 11.09).

## Voice fix, Oct 24 (no ElevenLabs key on the new account, so no re-take)
The take said "the Argentina players found his bottle". Yahoo Sports says Messi and Nicolás González found it on the pitch; Goal.com says a member of Argentina's coaching staff collected it from the pitch and handed it to Messi. "Argentina found his bottle on the pitch, and passed it to Messi" is true under both, so `Tools/word_edit.py` replaced "the Argentina players" with the word "Argentina" from the same take ("But Argentina scored", 54.58-55.05 s). Checked with local speech-to-text: "after the game, Argentina found his bottle on the pitch and passed it to Messi". The original take is in `_voice_preedit/`.

## Script lines -> sources
| Line | Source and exact wording |
|---|---|
| 2018, England v Colombia at the World Cup | The match itself (FIFA 4K broadcast, archive.org `colombia-vs-england.-2160p`): last 16, Spartak Stadium, Moscow, 3 July 2018, 1-1, England won 4-3 on penalties. |
| England had never won a World Cup shootout; lost in 1990, 1998 and 2006 | Common record: 1990 semi-final v West Germany, 1998 last 16 v Argentina, 2006 quarter-final v Portugal, all lost on penalties. The Colombia shootout was England's first World Cup shootout win. |
| Deep into stoppage time, Yerry Mina headed in an equaliser | The broadcast: the corner and Mina's header at 90+3 (scorebug "+5" on screen); Mina (13) celebrates. |
| His water bottle had notes on Colombia's takers; he covered it with a towel near Colombia's keeper | Sky Sports, "England's Jordan Pickford handed Colombia penalty information on water bottle": Pickford "covered the bottle with a towel when near Colombia goalkeeper David Ospina to keep the notes hidden". The broadcast shows Pickford holding the bottle wrapped in a towel next to Ospina at the coin toss (A16, A17). |
| England missed their third kick; Uribe hit the crossbar; Pickford saved Bacca; Dier scored | The broadcast: Henderson (England's 3rd) saved by Ospina; Uribe (Colombia's 4th) hits the bar; Bacca (Colombia's 5th) saved; Dier scores the winner. |
| Pickford dived to his left | The 4K broadcast, wide shot from behind the kicker: Pickford ends on the right of the goal as the camera sees it, which is his left, and tips the ball up with his raised arm. |
| Only one Colombian, Falcao, shot differently from what he expected | Reported Pickford quote: "Falcao is the only one who didn't go his way" (the18.com / Sky Sports coverage of the bottle). Falcao scored down the middle as Pickford dived (A28). |
| Euro 2020 final v Italy: the bottle again, two saves, England still lost | Daily Mail (via chatsports.com): "Jordan Pickford repeated his water bottle trick from the 2018 World Cup with notes about Italy's penalty takers before the Euro 2020 final shoot-out ... saving two penalties at Wembley". BBC broadcast: Pickford saves Belotti and Jorginho; Italy won 3-2 on penalties. |
| This summer, England v Argentina, World Cup semi-final; Argentina scored in the 85th and 92nd minute; no shootout | ESPN match page "England 1-2 Argentina (Jul 15, 2026)"; Sky Sports report: Gordon 55', E. Fernández 85', L. Martínez 90+2'. NPR: Messi assisted both. Mercedes-Benz Stadium, Atlanta. |
| After the game, Argentina found his bottle on the pitch and passed it to Messi | Yahoo Sports: "Lionel Messi and Nicolás González found an interesting item belonging to their opponent on the pitch"; "cameras caught Messi and González holding a water bottle that belonged to England's goalie". Goal.com: a member of the coaching staff "collected the bottle from the pitch before handing it to the captain". |
| Next to one player's name, the note reportedly just said "feel on the day" | Yahoo Sports / FourFourTwo: Thiago Almada's line read "Feel on the day". The photo of the bottle (shared on X; first posted by Argentina fitness coach Luis Martín on Instagram, since deleted) shows "ALMADA - FEEL ON THE DAY". |
| And they couldn't stop laughing | LADbible, 16 July 2026: "Argentina players laugh after discovering what was on Jordan Pickford's water bottle"; Enzo Fernández "among those seen laughing". Goal.com: "several squad members appeared amused". |

## Footage (every clip is in sources.csv; I checked every shot on `_check/sheet.jpg`)
- **2018:** archive.org `colombia-vs-england.-2160p` (FIFA 4K HDR broadcast). Only the used minutes were pulled from the 31 GB file and tone-mapped to SDR 1080p (`src/pull4k.sh`); the 480p copy was used to map moments.
- **Euro 2020 final:** archive.org `euro-2020-final` (BBC, 720p). Sections pulled with ffmpeg. The BBC Sport bug is small, top-left, and mostly outside the 9:16 crops.
- **2026 semi-final:** no footage reachable, so photos: the bottle (X posts, files `x_4536_*`, `x_4999_*`), González and Messi (TyC Sports frame, via @TouchlineX on X). Credits are on the cards.
- **Illustrative:** A38, a ball on the spot from the 2018 shootout, under "so there was no shootout" (2026).
- **Cards:** `card_shootouts`, `card_fixture`, `card_semi`, `card_bottle_full`, `card_messi2`, `card_bottle`, `feel_9x16` (Tools/story_card.py).

## Warnings for the owner
- **Copyright:** FIFA/BBC broadcast footage and press photos, as in S01-S03. A claim in some territories is possible; clips can be swapped.
- **Softness:** the Euro 2020 clips are 720p (2.7x blow-up); QA warns, no better source exists.
- **Music bed:** `eleven_story_01.mp3` is still a candidate you have not approved by ear (same as S01-S06).
