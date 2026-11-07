# Footage + audio notes (v2)
Sources (all X posts, no uploads): NBA's 2026-27 Points of Education video (X 2104962344031772863), ThrowbackHoops "Last Shot" HD (2006556195113533776), Hater Report (1934060028732039621). Recipe: `_clips_recipe.py`. Final pass: `Tools/polish.py`.

v2 changes: 18 different shots, real HD Jordan angles (no more reused/upscaled 480p), NBA banner cropped out of league clips, player ids by jersey (Brown #7/Oubre #9, Barrett #9, Brunson #11/McCollum #3, Banchero #5).
Audio: the voice file is very quiet (-27 LUFS); v1 boosted the whole mix 13 dB so the effects drowned it. Now the voice is cleaned/levelled first, only 2 effects (swish on the ball through the net, one soft whoosh into the first ESPN card), mix -14.7 LUFS, peak -3.7 dB.
Captions: house MetaSports style (captions.py), bright red/green accents. Do not change this style.

Still not found / honest limits:
- No referee whistle/foul-signal clip reachable, so none is used (and no whistle sound).
- No Jaylen Brown in a Sixers jersey; last shot is Brown in Celtics green from the NBA video.
- Barrett's defender is identified as Mobley via ESPN's description (no number visible).
- "Feel/firm" shots (Banchero, Brunson) are examples from the NBA video, shown generically.


# v3 rebuild (Oct 5, 2026) per Critique Round 2C
Lane: rule/oddity. Concept: Jordan's push-off is legal under the new rule; Brown's is the league's example. Added value: Brown's 10 offensive fouls + $50K fine (the twist).
Changed: cut the Four-F's list/second explanation and card 1; question by 8.7 s; added Brown backstory beats and two ESPN evidence cards (headline + the 10-fouls line; headline + the $50,000 line); last line attributes the verdict to ESPN; ends on the payoff; 0.3 s voice tail; no headline text. Restored the Jordan/NBA clips from git f756001 (clips/, _clips_recipe.py; NOT committed).
Sources: ESPN push-off guidelines https://www.espn.com/nba/story/_/id/50063714/nba-issues-new-guidelines-instructs-refs-crack-push-offs (Four F's; Golliver: Jordan wouldn't be whistled; Brown forearm into Oubre's chest, then-Celtics/then-76ers); ESPN https://www.espn.com/nba/story/_/id/48689072/celtics-jaylen-brown-fined-50000-criticizing-officials (10 offensive fouls in the first round, twice the next-highest; fined $50,000 May 5, 2026). I re-read both pages Oct 5.
NOT verified: the pronunciation of the voice take by ear; whether the NBA's Brown/Oubre example clip is from the playoffs (script does not claim it); Brown b-roll is thin (S13/S17 reused). Old version: script_v1.txt, shots_v1.json, voice_v1.mp3.
