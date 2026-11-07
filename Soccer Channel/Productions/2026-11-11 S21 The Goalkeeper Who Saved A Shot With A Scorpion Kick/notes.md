# S21 Higuita scorpion kick (script Nov 4, PC account 1; NOT voiced, NOT built)
Topic shape: goalkeeper trick (Topic and Script Reset, Nov 2026). New fact (line 2): the first time he tried it in a real match.

| Line | Source (checked Nov 4, 2026) |
|---|---|
| England 0-0 Colombia, friendly, Wembley, 6 Sep 1995; Redknapp's debut (1st cap) | englandstats.com match 714; RSSSF England results 1995 |
| Idea came while filming a soda advert with children | BBC Sport, 6 Sep 2025, "The legend of El Loco" |
| Practised in training and warm-ups; first shown in a match at Wembley | BBC Sport 2025 ("his party trick in training and warm-up routines"; "After first displaying it at Wembley"); Britannica ("debuted his signature move") |
| "For years": Higuita, "the ball that I had been waiting for five years" | Goal.com, 6 Jul 2012 (Mundo Deportivo interview) |
| Redknapp's miscued cross drifted to him | BBC 2025 ("miscued effort"); Daily Mail 2015 ("Redknapp crossed"). theScore calls it a lob attempt, so "miscued" covers both. |
| Commentator thought the whistle had gone; England coach Bryan Robson laughing on the bench | BBC 2025 (Martin Tyler quote; Robson "could be seen laughing on the bench") |
| Linesman's flag up for offside, play continued | Daily Mail 2015; BBC 2025 ("the linesman put his flag up - but play continued") |

Footage: the save is widely on YouTube (Sky broadcast). Find a clean upload before building. Run `copy_check.py` (famous topic).

## Style v3 rewrite (cloud, Nov 5): `script.txt` (old one in `script_v2_old.txt`)
- Line 1 is a name + verb + object (no "The goalkeeper who..."); the misread at about 8 s ("wasn't showing off; waiting five years"); the hidden fact = the offside flag; the last line ties back to line 1.
- No new facts: every line maps to the table above. "Waiting for that ball for five years" = the Goal.com 2012 quote ("the ball that I had been waiting for five years"). "Referee missed it" = BBC/Daily Mail "flag up, play continued".
- About 180 words, so 171 words; at our voice speed that may run under the 50 s floor. If it does, add back ONE sourced line from the old script ("The game was a friendly, and Robson's side were already laughing about it" is NOT sourced, so instead use: "England against Colombia, a friendly, at Wembley.").
- Title (line 1): "René Higuita saved a shot at Wembley with his heels"
