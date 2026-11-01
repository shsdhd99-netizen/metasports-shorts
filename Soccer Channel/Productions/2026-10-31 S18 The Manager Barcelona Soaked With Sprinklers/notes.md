# S18 The manager Barcelona soaked with sprinklers just got his revenge (Oct 29, 2026; daily FC build)

> **FACT FIX, Oct 29 (cloud review):** two lines cut from both DRAFT files (no new voice), now 51.9 s:
> 1. "just like that night in 2010" was WRONG: in 2010 he ran on with his finger up (our own shot shows him standing); his Camp Nou knee slide was 2006 with Chelsea (Goal; 90min). Cut = shot M28 (video frames 1415-1458, audio 47.140-48.607 s).
> 2. "Then came Sunday." would read as tomorrow on a Saturday post. Cut (video frames 836-863, audio 27.848-28.781 s).
> words.json / captions.srt still hold the old timing: if re-rendered from clips, run Tools/word_edit.py with those two audio spans first.
> Posted title: drop "just": "The manager Barcelona soaked with sprinklers got his revenge" (Script Review - FC queue, Oct 29).

- **Lane:** comeback / revenge (311K theme) about a global name, tied to this week's match (Oct 25 Clásico).
- **Concept (8 words):** Soaked by Barcelona's sprinklers, Mourinho returns and wins.
- **Added value:** the 2010 sprinkler night and the 2026 Clásico in one story; the September sprinkler gift; the irony that Barcelona were chasing a Real Madrid record and Real Madrid stopped it.
- **Copy check:** `copy_check.py "Mourinho Camp Nou sprinklers"` FRESH; Ahmed's Goal has one Mourinho Short (unfair sackings, 668K), not this one.
- **Why not Fleetwood (idea S18 in the bank):** no usable match footage (Sky and Arsenal.com players can't be downloaded plainly; ESPN has only a studio segment). Left in the bank.
- **Music test:** S15 music, S16 none, S17 music, so S18 is the **no-music** side: post `final_nomusic.mp4`.

## Claims and sources
| Line | Source | Exact words |
|---|---|---|
| 2010: Inter knocked Barcelona out of the Champions League at Camp Nou; lost 1-0, through on aggregate | Managing Madrid (Sep 7 2026); Goal (Sep 7 2026) | "Mourinho's Inter lost 1–0 that night but advanced 3–2 on aggregate, eliminating Pep Guardiola's Barcelona" |
| Sprinted onto the pitch with his finger in the air | Goal (Sep 7 2026) | "Index finger raised, Mourinho charged onto the Camp Nou pitch and celebrated wildly with his players" |
| Ground staff turned the sprinklers on; he kept celebrating in the spray | BBC (Sep 8 2026); Managing Madrid | BBC: "the Camp Nou sprinklers were turned on while Inter were celebrating"; Managing Madrid: "Camp Nou staff turned on the sprinklers in an attempt to cut the celebrations short... Mourinho celebrating as water sprayed around him" |
| Weeks later he won the final and became Real Madrid's manager | BBC (Sep 8 2026) | "lifted the trophy after leading Inter to a 2-0 victory over Bayern Munich in the 2010 final... Days later, he was appointed Real Madrid manager" |
| He left in 2013; came back this summer | Goal/LiveScore (Sep 7 2026); The National (Oct 25 2026) | "In 2010, the now 63-year-old left Milan for Madrid and stayed there until 2013. This summer, he joined Spain's record champions for the second time." |
| In September an Italian journalist handed him a garden sprinkler with a bow | BBC (Sep 8 2026); talkSPORT | BBC: "an Italian journalist stood up and gifted him a small garden sprinkler, wrapped in a bow"; Sept 7 press conference before Real v Inter (Goal) |
| His first Clásico back, at Camp Nou, Sunday | Independent (Oct 26 2026); The National | "taking charge of the fixture for the first time since his return"; Barcelona 1-2 Real Madrid, Sun Oct 25 2026 (BBC) |
| Barcelona had won all nine league games; one more would break a 1968 Real Madrid record | BBC (Oct 25 2026) | "targeting a 10th consecutive victory to start the league season. It will surpass the mark set in 1968-69 by Real Madrid" |
| Courtois had the flu | ESPN (Oct 25 2026) | "Reserve goalkeeper Andriy Lunin had to step in for Thibaut Courtois at Camp Nou, who had the flu." |
| Vinícius was suspended | The National (Oct 25 2026) | "Mourinho will be without suspended forward Vinicius Junior" |
| Mbappé scored, Raphinha equalised, Mbappé's late winner was his 100th Real goal | BBC (41', 61', 87'); ESPN; The Athletic | "Mbappe's 87th-minute winner, the Frenchman's 100th goal for Madrid" (The Athletic). Sources differ on 87th/88th minute, so the script says "with time running out". |
| Mourinho dropped to his knees, like 2010 | BBC (Oct 26 2026); Independent | BBC: "celebrated Kylian Mbappe's late winner at Barcelona on Sunday with a trademark knee slide"; Independent: "recreating one of the most iconic moments of his managerial career" |
| The record belonged to Real Madrid; Real Madrid stopped it | BBC (Oct 25 2026) + result | as above |

## Footage
- **2026:** ESPN's public clips of the match (Oct 25 2026): highlights, both Mbappé goals, Raphinha's goal, Lunin's save; the winner clip includes Mourinho's knee slide. 720p sources (about 2.7x in the 9:16 crop; no better source).
- **2010:** archive.org "Inter Milan vs Barcelona 2010 Champions League" (full broadcast of the 2nd leg), the last 7 minutes: Mourinho's run onto the pitch and celebrations. The broadcast doesn't show the sprinkler spray itself, so M08/M09 show him celebrating on the pitch during those minutes.
- **Stock:** Mixkit 19551, a garden sprinkler, for the gift line (no usable video of the gift: the BBC and TNT videos can't be downloaded plainly).
- **Illustrative:** M10 (2010 semi celebrations for "won the final"), M11 (walking off in 2010 for "left in 2013"), M13/M14 (Mourinho at the 2026 Clásico for "in September"). Premier Sports' knee-slide video on X refused the download (403), so it is not used.

## Oct 30 check (overnight edit pass)
- The Oct 29 fact-fix re-cut was spliced straight into the DRAFT files and skipped the limiter: true peak +1.6 dBTP (no music) / +0.9 (music), a +1 dBFS sample peak at 17.7 s. Limited to -1.9 / -2.1 dBTP (audio only, picture untouched; pre-fix copies in `_check/prelimit/`, not in git).
- Gemini strict editor [S] 4.5/10. Checked against the frames and not acted on: "video-game footage" at 28 s and 40 s is ESPN's real Clásico highlights (the sponsor boards fooled it); "cut the team news" and "the ending is circular" argue with the story's own payoff. Real but unfixed (no footage): 17-21 s is two 2010 walking shots under "won the final... became Real Madrid's manager... left in 2013"; a clip of the 2010 trophy lift would be better if one turns up.
- Folder state: voice.mp3/words.json/shots here are the PRE-fix versions (54.3 s). Redo the two cuts with `Tools/word_edit.py` before any re-render.
