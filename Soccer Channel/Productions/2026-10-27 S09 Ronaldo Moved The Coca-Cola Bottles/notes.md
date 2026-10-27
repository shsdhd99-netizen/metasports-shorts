# S09 Ronaldo moved the Coca-Cola bottles (Idea Bank S10) - SCRIPT + NOTES ONLY (Oct 27, 2026)
_Recovered Oct 27 from the FC daily run's record (its push was refused with a 403). Name clash: the research run the same morning also called the Krul idea S09; renumber one of them before posting._
Status: NOT built. `ELEVENLABS_API_KEY` is not set in the cloud environment, so no voice, footage, render or QA. Never fake a voice.
Title (line 1, 9 words): Ronaldo moved two Coca-Cola bottles, and billions disappeared.
Lane: global star + concrete object + "versus their sponsor" (conflict). Not a "Goalkeepers who..." Short (3 already out).
Copy-check: `Tools/copy_check.py` could not run (yt-dlp missing in the cloud). Ahmed CSV grep for "coca/cola": no hit. STILL TO DO before the voice.

## Claims (source; exact words)
- Date/place: press conference in Budapest on Monday June 14, 2021, the day before Portugal v Hungary (Euro 2020 opener, Group F).
  SI (Jun 16 2021): "Before speaking to the media on Monday in Budapest a day before Portugal's Euro 2020 opener against Hungary..."
  https://www.si.com/soccer/2021/06/16/coca-cola-shares-drop-four-billion-cristiano-ronaldo-snub
- Action/word: Snopes (Jun 18 2021): "he took the two Coca-Cola bottles that were left out for him, moved them out of frame to the side of the table, then held up a bottle of water and said, 'Agua.'"
  https://www.snopes.com/fact-check/ronaldo-snub-cost-coke-billions/
- Official sponsor: SI: "Coca-Cola is an official sponsor of the European Championship."
- Market value: Guardian excerpt in Snopes: "The market value of Coca-Cola went from $242bn to $238bn - a drop of $4bn." Snopes: outlets said $4-5 billion.
- Causation (the twist): Snopes: "there was no indication that this drop was entirely (or even in part) caused by Ronaldo's preference for water. In fact, Coca-Cola's stock was already falling by the time that Ronaldo snubbed Coke products." Rating: Mixture.
- Responses: Coca-Cola said everyone is entitled to their drink preferences (web search summary of IOL/others; EXACT WORDS STILL TO CHECK in the IOL or Guardian article). UEFA: "Players are offered water, alongside Coca-Cola and Coca-Cola Zero Sugar, on arrival at our press conferences." (SI)
- Next day: Portugal 3-0 Hungary, June 15, 2021, Puskas Arena. Ronaldo scored a penalty (87th, sources differ slightly) and a second in injury time; 11 Euros goals, sole record (previous 9 shared with Platini). Al Jazeera / ESPN: https://www.aljazeera.com/sports/2021/6/16/ronaldo-breaks-euro-record-as-portugal-cruise-past-hungary , https://www.espn.com/soccer/report/_/gameId/560334
- Script wording keeps "headlines said" and "Snopes found" so it is true if causation is disputed.

## Footage plan (not checked: cloud has no yt-dlp; region/licence unknown)
- Frame 1 = Ronaldo lifting the bottles off the table (the promise). Press-conference clip: UEFA/broadcaster post on X or archive.org; check with `Tools/x_clip.py`.
- Proof on footage: Snopes/Guardian headline screenshot (`webshot.mjs`) with a red circle on "$4bn"; Coca-Cola stock chart screenshot.
- Payoff: Portugal-Hungary goals (broadcast, archive.org if any). Replay the bottle move at 0.5x before the payoff.
- Fallback if no clip exists: photos only is too weak; hold the Short.

## To do when the key is set
voice_take.py (3 takes) -> tighten_voice.py (end under 59.5 s) -> footage -> cuts.json with "promise": ["bottles","coca-cola","coke","water"] -> both versions -> qa_short.py --full -> Hub card.
Tags idea (check `tags_fit.py --cap 150`): cristiano ronaldo, ronaldo coca cola, euro 2020, ronaldo agua, portugal hungary, football stories, soccer shorts
