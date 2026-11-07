# S04 Players who got sent off in their very last game (DRAFT, rendered Oct 24, 2026)

> **STATUS (Oct 24, new account, cloud session): RENDERED, 57.9 s (under 60), music and no-music.** The voice is the recorded take, unchanged except a 0.25 s silent tail (QA wanted a tail; the pre-pad file is in `_voice_prepad/`, local only).
> - **Watch 3 resolved:** the voice check's "nothing heard" at about 51.7 s was a false alarm. A local speech-to-text pass (faster-whisper) hears every word, including both "before"s; QA's own speech check on the export: 100% word match.
> - **Watch 2 resolved:** `assets/card_goldenball.jpg` now credits "AP, AFP, CNN, 10 July 2006" (CNN's 2006 page reads: "earned 2,012 votes. Italian captain Fabio Cannavaro (1,977) was second ... Andrea Pirlo (715) was third"). New `assets/card_vote.jpg` for line 17: voting closed at midnight Sunday (AP: "Voting for the 2006 Golden Ball closed at midnight Sunday"), red card in the 110th minute, "most had voted early" (AFP).
> - **Footage:** the ABC 720p broadcast on archive.org; only the used minutes were pulled (`src/pull720.sh`), the abc logos blurred, and ESPN's "program alert" ticker cropped off the headbutt replay. Key shots: the chip off the bar (goal-line replay), Materazzi's header, Buffon's tip-over, the reverse-angle headbutt replay, Elizondo's red card (live), Zidane walking past the trophy (whole frame, both in shot), Trezeguet's kick off the bar, Grosso's winner. The opening shots (Z02-Z05, Z07, Z39) come from ABC's own 2006 montage and pre-match package.
> - **Illustrative:** Z25 (Elizondo beside another official at the touchline; the broadcast doesn't show which official); Z34 (Mixkit stock, a man reading the morning paper).
> - The fact-check table below is the Oct 23 one (no wrong lines).

## Fact check (Oct 23, 2026)

> **READ FIRST: verdict for the recorded voice**
> - **WRONG lines: none. Lines that must change: none.** All 19 claims check out, so the recorded voice can stay.
> - **Watch 1 (soft, keep):** "Most of the journalists had voted before the final was over, before the headbutt." This is supported by AFP ("most journalists submit their votes earlier") and The Set Pieces ("most of the votes had been cast before his red card"). It describes how journalists usually voted, not an official FIFA count. Some outlets claim the vote closed at half-time. That is not true for 2006 (voting stayed open until midnight), so never say "half-time".
> - **Watch 2 (card credit):** `assets/card_goldenball.jpg` says "Source: BBC Sport, 10 July 2006". news.bbc.co.uk is blocked from this session, so I could not open that page. The numbers on the card (2,012 / 1,977 / 715) match AP and AFP. Before rendering, either open the BBC page on the PC or change the credit to "AP / AFP, 10 July 2006".
> - **Watch 3 (voice, not facts):** `voice.log` says the take used still FAILS the voice gate. The check heard nothing for the second "before" ("...over, before the headbutt", about 51.7 s after tightening). There is sound at that spot (about -21 dB, the same level as the words around it), so it is probably a recognizer miss. Listen to 50.4-52.5 s before cutting. Runtime is 57.6 s, just under the 58 s story floor (SKILL.md step 4).

- **Format:** story format (`.claude/skills/story-short/FORMAT.md`). The title is read as line 1, then "Back in 2006", a turn every 8-12 s, and an ironic payoff. No teaser.
- **Lane / theme:** records and "looks fake but is real" (Ahmed's Goal median 332K). It also starts a "Players who got sent off..." series. Global star: Zidane (plus Buffon and Materazzi).
- **Concept (8 words):** Zidane's last game: red card, then the Golden Ball.
- **Added value:** most retellings stop at the headbutt. Ours adds three things:
  - the vote that mostly happened before the red card;
  - the margin: 2,012 to 1,977, only 35 points;
  - the fourth official's own words ("Horacio, Horacio, I saw it").
- **Ahmed's Goal title grep (Oct 23):** no title names Zidane. These list titles may include the headbutt itself:
  - "Dumbest red cards in football history" (509K);
  - "Legends who got kicked out of the World Cup" (1.5M);
  - "The most FAMOUS red card in history" (11K).

  The Golden Ball twist is our own angle.
- **Voice:** Alex, take 1 of 3 (all 3 flagged REDO; see Watch 3). 250 words, 57.6 s after tightening.

## Script lines -> sources
| # | Line | Source | Exact quote (under 15 words) | Verdict |
|---|---|---|---|---|
| 1 | Players who got sent off in their very last game. | TSN / Canadian Press (AP), Oct 1 2026: https://www.tsn.ca/soccer/article/twenty-years-after-his-infamous-world-cup-final-headbutt-zidane-faces-italy-again-as-france-coach/ | "Zidane never played again after the 2006 final." | CONFIRMED |
| 2 | Back in 2006, Zidane had already announced that the World Cup would be the last tournament of his career. | Mail & Guardian (AFP), Apr 26 2006: https://mg.co.za/2006-04-26-zidane-confirms-his-farewell/ | "explained his decision to retire after the World Cup finals" | CONFIRMED |
| 3 | France made it all the way to the final against Italy, in Berlin. | Wikipedia, 2006 FIFA World Cup final: https://en.wikipedia.org/wiki/2006_FIFA_World_Cup_final | "played at the Olympiastadion in Berlin, Germany, on 9 July 2006" | CONFIRMED |
| 4 | After seven minutes, Zidane stepped up to take a penalty against Gianluigi Buffon. | Same Wikipedia page. The Daily Star (AFP), Jul 10 2006: https://archive.thedailystar.net/2006/07/10/d6071001011.htm | "converted this kick in the 7th minute with a Panenka" / "with only seven minutes gone" | CONFIRMED |
| 5 | But instead of smashing it, he chipped it down the middle. | Twelve Yards (Substack): https://twelveyards.substack.com/p/when-is-a-panenka-not-a-panenka. Washington Times (AP), Jul 10 2006: https://www.washingtontimes.com/news/2006/jul/10/20060710-125151-2396r/ | "chips the ball down the middle of the goal" / "softly chipped the ball over Buffon, who dove the wrong way" | CONFIRMED |
| 6 | The ball hit the underside of the crossbar, bounced over the line, and France were winning. | Wikipedia (final): see row 3. Wikipedia (Zidane): https://en.wikipedia.org/wiki/Zinedine_Zidane | "glanced off the underside of the crossbar" / "struck the crossbar and bounced just over the goal line" | CONFIRMED. AP's 2006 report says "upright"; most sources and the footage say crossbar. |
| 7 | Twelve minutes later, Marco Materazzi headed in the equalizer. | Wikipedia (final) | "levelled the score in the 19th minute, a header from an Andrea Pirlo corner" | CONFIRMED (7' to 19' is 12 minutes) |
| 8 | The game went to extra time, and Zidane almost won it with a header, but Buffon tipped it over the bar. | Wikipedia (final). The Daily Star (AFP), see row 4 | "he tipped a Zidane header over the crossbar" (104th minute, Sagnol cross) / "spectacularly palmed over the bar by Buffon" | CONFIRMED |
| 9 | Then, in the 110th minute, Zidane and Materazzi exchanged a few words. | Goal.com: https://www.goal.com/en-us/news/who-did-zinedine-zidane-headbutt-in-the-world-cup-2006-final--why/1jhvyg4hqm70wzuf2cq44390s. Gulf News: https://gulfnews.com/sport/football/world-cup/before-france-vs-spain-zidanes-headbutt-on-materazzi-and-the-2006-world-cup-final-french-football-never-forgot-1.500607520 | "in the 110th minute" / "In the 109th minute, Zidane and Italian defender Marco Materazzi exchanged words" | CONFIRMED. Sources say 109th-110th; the red card is listed at 110'. |
| 10 | Zidane walked away. Then he turned around and headbutted Materazzi right in the chest. | Goal.com (row 9). Wikipedia (final) | "Though he initially turned away, Zidane pivoted seconds later." / "delivered a headbutt to Materazzi's chest" | CONFIRMED |
| 11 | The referee hadn't even seen it. | Wikipedia, Luis Medina Cantalejo: https://en.wikipedia.org/wiki/Luis_Medina_Cantalejo | "none of the three officials on the field saw Zinedine Zidane headbutting" | CONFIRMED |
| 12 | But the fourth official had, and Zidane was shown a red card. | Football Italia (Elizondo recalling Medina Cantalejo): https://www.football-italia.net/42269/ref-who-saw-zidane-hit-materazzi | "Horacio, Horacio, I saw it" | CONFIRMED (the fourth official's own account) |
| 13 | So one of the greatest players of all time walked off the pitch for the last time, right past the World Cup trophy. | The Set Pieces: https://thesetpieces.com/latest-posts/how-zinedine-zidanes-flawed-genius-defined-the-2006-world-cup/. TSN / AP (row 1) | "he passed the trophy by the side of the pitch" / "walked solemnly past the Jules Rimet World Cup trophy" | CONFIRMED. "Greatest of all time" is opinion. AP's "Jules Rimet" is loose wording; the trophy is the FIFA World Cup Trophy, so don't put "Jules Rimet" on screen. |
| 14 | And without him, France lost the shootout 5-3. | The Daily Star (AFP), row 4 | "rifled home the Azzurri's winning penalty to clinch a 5-3 victory" | CONFIRMED |
| 15 | Italy were world champions. | Same | (same quote) | CONFIRMED |
| 16 | The next morning, FIFA announced the best player of the whole tournament. | Mail & Guardian (Sapa-AFP), Jul 12 2006: https://mg.co.za/article/2006-07-12-blatter-zidane-may-lose-bestplayer-award. Wikipedia (final) | "announced as the winner of the prestigious award on Monday morning" / "The day after the final, Zidane was awarded the FIFA World Cup Golden Ball" | CONFIRMED |
| 17 | Most of the journalists had voted before the final was over, before the headbutt. | Mail & Guardian (AFP), row 16. The Set Pieces, row 13. Al Jazeera, Jul 12 2006: https://www.aljazeera.com/news/2006/7/12/zidane-wins-golden-ball-award | "most journalists submit their votes earlier" / "most of the votes had been cast before his red card" | CONFIRMED (soft; see Watch 1). Voting was open "until midnight Sunday" (AP preview, Himalayan Times: https://thehimalayantimes.com/sports/world-cup-2006-and-the-golden-ball-goes-to). |
| 18 | And the winner was Zinedine Zidane. | The Daily Star, Jul 11 2006: https://archive.thedailystar.net/2006/07/11/d60711041240.htm. filgoal, Jul 10 2006: https://www.filgoal.com/articles/177842 | "Zidane received 2,012 points with Italy captain Fabio Cannavaro second on 1,977 points" | CONFIRMED (Pirlo third on 715) |
| 19 | The man who got sent off in the World Cup final was named the best player of the World Cup. | Rochester Business Journal (AP), Jul 10 2006: https://rbj.net/2006/07/10/ousted-french-star-wins-top-player-award/ | "won the Golden Ball award for the tournament's best player, AP reported" | CONFIRMED |

**Sources that disagree or that I left out:**
- ModernGhana says the poll was "conducted at half time during the final". A 2006 Gazette column says "Apparently it was decided at half-time". The AP preview says voting stayed open until midnight on the day of the final; half-time was the 2002 rule. Don't use "half-time".
- Blatter said FIFA could strip the award ("It's not FIFA that decides who wins this award", filgoal, Jul 12 2006). It was never taken away. That would make a possible extra beat if the voice is ever re-recorded.

## Footage needed (one moment per line)
Source: archive.org `wc-2006-final-italy-vs-france-abc-720p-60fps-hd` (ABC, 720p). File times are from `CLOUD STATE - read this first.md`.
1. Title card: Zidane in the 2006 final (or `assets/bg_zidane.jpg`).
2. "announced... last tournament": Zidane in a France shirt at the 2006 tournament; a Real Madrid 2006 still if available.
3. "final against Italy, in Berlin": the Olympiastadion wide shot and the teams lining up.
4. "seven minutes... penalty against Buffon": about 14:30, Zidane placing the ball, Buffon on his line.
5. "chipped it down the middle": the chip itself (about 15:00).
6. "underside of the crossbar, bounced over the line": the bar-and-bounce replay; France celebrating.
7. "Materazzi headed in the equalizer": the 19' header from Pirlo's corner.
8. "extra time... header... Buffon tipped it over": about 116:05, the Zidane header and Buffon's save.
9. "exchanged a few words": the two walking together (replay angle, about 123:00).
10. "walked away... turned around and headbutted": the headbutt replays, 123:00-123:48; Materazzi down at 121:00.
11. "referee hadn't even seen it": Elizondo looking around, confused (about 125:12).
12. "fourth official had... red card": the referee with his hand to his earpiece, then the red card at 125:36.
13. "walked off... past the World Cup trophy": about 126:00. This is the key shot.
14. "lost the shootout 5-3": Trezeguet's kick hitting the bar; Grosso's winner.
15. "Italy were world champions": Cannavaro lifting the trophy.
16. "The next morning, FIFA announced...": a Golden Ball still or a newspaper card. Use stock (newspaper or morning) if nothing else is clean.
17. "Most of the journalists had voted...": the press box or journalists typing. Mark it "illustrative" if it is stock.
18-19. Payoff: `assets/card_goldenball.jpg` (fix the credit first, see Watch 2), then the last picture: Zidane walking past the trophy again, or Zidane with the Golden Ball.

**Rights:** ABC broadcast footage; same risk as S01-S03. Keep clips short, narration over them, no original commentary audio.
