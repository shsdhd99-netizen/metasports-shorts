# S03 Goalkeepers who danced on the line to win a final (DRAFT, awaiting approval)

- **Format:** the story format (`.claude/skills/story-short/FORMAT.md`): title read as line 1, "Back in 2005", a turn every 8-12 s, payoff on a hard number and irony. No teaser or follow ask (owner, Oct 22). Pauses tightened with `Tools/tighten_voice.py`.
- **Lane / theme:** comeback (Ahmed's Goal theme median 311K) plus the "Goalkeepers who..." series started by S01. Global names: Gerrard, Maldini, Pirlo, Kaká, Shevchenko.
- **Concept (8 words):** Dudek copied Grobbelaar's wobbly legs and won Istanbul.
- **Added value:** the link most retellings skip: Dudek also had a book on about 100 Milan penalties (his own words, Guardian 2025), Carragher pushed the Grobbelaar dance on him, Grobbelaar's own "spaghetti" line, and the irony that the hero of Istanbul played only 12 more games for Liverpool.
- **Copy-check, Oct 22:** `copy_check.py "Dudek spaghetti legs Istanbul"`: FRESH. Ahmed's Goal titles: nothing on Dudek, Istanbul or Grobbelaar ("The BEST half time speech EVER", 14K, is a different angle).
- **Runtime:** 70.7 s (71.3 s raw, 0.5 s of pauses cut). 267 words. Voice: Alex, take 2 (passed the check: HNR 8.6, jitter 2.9, shimmer 10.8).

## Script lines -> sources
| Line | Source and exact wording |
|---|---|
| 2005, Liverpool v AC Milan, Champions League final, Istanbul | Wikipedia, "2005 UEFA Champions League final": played 25 May 2005, Atatürk Olympic Stadium, Istanbul. The stadium screen in C30 reads "Istanbul". |
| Milan had Maldini, Pirlo, Kaká and Shevchenko | Wikipedia line-ups: all four started for Milan. |
| Maldini scored inside the first minute | Wikipedia: "Milan scored within the first minute of the match after captain Paolo Maldini volleyed in an Andrea Pirlo free kick". The stadium screen in C30: "MALDINI 1'". |
| By half-time, Milan were winning 3-0 | Wikipedia: "Hernán Crespo added two more goals before half-time to make it 3–0". The Guardian (2025): "a 3-0 half-time deficit". |
| Six minutes: Gerrard header, Šmicer from distance, Alonso's penalty saved and the rebound scored | Wikipedia: Gerrard "lofted a header past Dida"; "Šmicer beat Dida with a long-range shot"; "Alonso's penalty was saved, but he scored from the rebound". Stadium screen: 54' Gerrard, 56' Šmicer, 60' Xabi Alonso. Ancelotti: "We had six minutes of madness". |
| Three minutes from the end of extra time, Shevchenko had two shots from right in front of goal, and Dudek saved both | Wikipedia: "in the 117th minute (three minutes from penalties) ... Dudek saved, only for it to rebound back out to Shevchenko, who again shot from under 3 yards, which Dudek saved again". (The first effort was a header; "two shots" is how Wikipedia and UEFA describe it.) |
| In 2011, a UEFA poll voted it the greatest moment in Champions League history | Wikipedia: "In a 2011 poll conducted by UEFA.com, Dudek's double save from Shevchenko in the 117th minute was voted the greatest Champions League moment of all time". |
| Dudek had studied about a hundred of Milan's penalties; his goalkeeping coach was ready to signal left or right | The Guardian, May 23 2025 (Dudek interview): "I had watched maybe 100 of their penalties and I had a book on them ... I asked my goalkeeping coach, José Ochotorena, to help me. I said to him: 'When you see their players coming, look at their name in my book and raise the hand left or right.'" |
| Carragher jumped on his back: do what Bruce Grobbelaar did | liverpoolfc.com, "Dudek thanks Carra for Istanbul advice" (Dudek): "Suddenly Jamie Carragher jumped on my back, pushing me and telling me 'put them under pressure, do something on the line like Grobbelaar.'" The Guardian (2025): "He said: 'You should do something like Bruce Grobbelaar did with the spaghetti legs'". |
| In 1984, Liverpool won the same trophy on penalties, against Roma, in Rome; Grobbelaar wobbled his legs on the line | Wikipedia, "1984 European Cup final": 30 May 1984, Stadio Olimpico, Rome; Liverpool won 4-2 on penalties. UEFA.com (May 24 2009): "Grobbelaar, employing his 'spaghetti legs' stance, forced Bruno Conti and Francesco Graziani to miss". The European Cup and the Champions League are the same trophy. |
| "I'm in Rome, the national dish is spaghetti, so I'll do spaghetti legs." | UEFA.com, "Grobbelaar reflects on 1984 shoot-out" (May 24 2009), Grobbelaar's own words. |
| Two Roma players missed | UEFA.com (2009): Conti and Graziani missed. ESPN (2021): "Liverpool won after misses by Bruno Conti and Francesco Graziani." |
| Serginho blasted Milan's first penalty over the bar | The Guardian (2025): "after Serginho had blazed Milan's first over the bar". Wikipedia: "shot over the crossbar after attempts from Dudek to distract him". |
| Dudek saved Pirlo's; Shevchenko had to score to keep Milan alive; Dudek saved it | Wikipedia: "Andrea Pirlo was next for Milan, and his penalty was saved by Dudek"; "Shevchenko ... then had to score to keep Milan in the shootout ... Dudek ... blocked the shot". Liverpool won 3-2 on penalties. |
| That summer, Liverpool signed a new goalkeeper, Pepe Reina | Wikipedia (Pepe Reina): "signed by Liverpool from Villarreal in July 2005". liverpoolfc.com: "brought in from Villarreal in July 2005 to demote a 'keeper who had won the Champions League a few weeks earlier – Jerzy Dudek – to the bench." |
| In the two years that followed, the hero of Istanbul played just twelve games | liverpoolfc.com (Jerzy Dudek profile): "the Poland international was restricted to just 12 appearances in the two years that followed." LFChistory.net: 2005-06: 6, 2006-07: 6 (all competitions). Wikipedia adds that he lost his place "following an arm injury", so the script does not say Reina alone caused it. |

## Footage (every clip is in sources.csv; I checked every shot on _check/sheet.jpg)
- **2005 final:** archive.org items `UclFinal2005AcMilanVsLiverpoolFcHdtv720p` (720p goal clips: Maldini, Crespo, Gerrard, Alonso, Shevchenko's 117th-minute chance) and `UEFAChampionsLeagueFinal2005ACMilanVsLiverpoolFCSecondHalf` (720p German SAT.1 broadcast: first half, second half, extra time, the shootout, the celebration). Only the needed sections were downloaded (`src/`).
  - C35-C37: the broadcast caught Carragher with Dudek right before the shootout (CARRAGHER 23 on screen).
  - C49: Dudek moving on his line as Serginho waits (the dance itself is filmed wide; there is no close-up of it).
  - The SAT.1 logo sits in the top-right corner of the broadcast and is mostly cropped out by the 9:16 crop.
- **1984 final:** archive.org `blob-roma-liverpool-1984` (RAI footage in a "Blob" montage), 27:00-29:55. The "blob" and "profondo giallorosso" marks at the bottom are cropped out (zoom 1.2, top-aligned). C40: the trophy close-up; C44-C45: Grobbelaar interviewed with the trophy.
- **Pepe Reina (C60):** Wikimedia Commons, `File:Pepe_Reina.JPG`, Agnieszka Mieszczak, CC BY 2.0. The credit is on the card.
- **Stats card (C62):** made by `assets/make_cards.py` from the LFChistory.net season table.
- **Stock:** Mixkit Free License (notebook 42655, spaghetti 24463).

## Warnings for the owner
- **Copyright:** broadcast footage (2005 SAT.1, 1984 RAI) from archive.org. Same kind of clips as S01/S02 and Ahmed's channels; a claim on some territories is possible. If one lands, the clips can be swapped.
- **The double save "two shots":** the first was a header. Wikipedia and UEFA call them two efforts; if a commenter argues, that's fine.
- **Two versions:** with the music bed and without. See UPLOAD.md.
