# S17 Goalkeepers who were subbed on just for the penalties (story, 51.9 s)

- **Lane:** the goalkeeper series. Goalkeeper stories are 3 for 3 on the channel: S01 30K, S05 27K, S03 15K; everything else is 1.7-2.8K [S, n=9].
- **Twist (our angle):** four days later, in the semi-final, Van Gaal had no substitutes left and lost on penalties.
- **Music side** (S16 was no music) → post `final_music.mp4`. Gemini pre-check: READY.
- Was "S09 (Krul)" in the idea bank (name clash). Now S17; the Coca-Cola Short becomes S18 if built.

## Claims → source
- 0-0 after 120 minutes; Krul came on at the end of extra time; saved Ruiz and Umana; 4-3. AP via Al Jazeera, AFP via Peninsula Qatar and Gulf News (2014).
- "We said nothing to Jasper" (Van Gaal); Krul "has saved only two out of 20 penalties during his career with Newcastle"; "a better reach"; "twice dived low to his left". Gulf News/AFP.
- Krul told the takers he knew where they would shoot: ABC/ESPN "Tim Krul defends shootout antics".
- Semi v Argentina, Jul 9 2014, 0-0, penalties (FIFA World Cup on X). Van Gaal: "I had already used three substitutes" (ABC "Louis Van Gaal defends sub decisions"). Cillessen saved none; Argentina won 4-2.

Footage: FIFA World Cup on X 1809180258051977400 (official); TyC Sports via an X repost (2075213076782014852) for the semi.
The "didn't save a single penalty" line plays over Cillessen from the quarter-final, because no semi footage of him was downloadable.

## Oct 30 re-edit (overnight edit pass)
- The three semi-final shots (K19, K20, K24, TyC Sports broadcast via an X repost) showed TyC's logo, its pink "¿ENTRÓ O NO ENTRÓ?" banner, the @tycsports handle and a trophy bug. All blurred with `broll.py --delogo` (four boxes, now supported) in all three versions; picture otherwise unchanged. Real-audio version re-rendered (`assemble.py --folder _realaudio --caption-style ahmed --out-name final_music_voice.mp4`, then `nat_sound.py --burst 32.91-36.91 --tail 0.5 --bed-db -26`). Note: `_realaudio/cuts.json` sources are relative to `_realaudio/`; link `src` there (`ln -s ../src _realaudio/src`) before running nat_sound, or the live audio comes out silent.
- Gemini strict editor [S]: 4.5 → 6.2. Not changed, on purpose: its advice to drop the plural "Goalkeepers who..." title (our three best soccer Shorts use it) and to cut "Back in 2014" (Ahmed's format). Still weak, no fix available: the substitution-board clip appears three times (open, "But this time...", the callback) because the only other semi-final footage is the TyC clip; the two wide pitch shots at 2 s and 6 s look alike.
- Full QA PASS (all three), Gemini precheck READY (real audio).
