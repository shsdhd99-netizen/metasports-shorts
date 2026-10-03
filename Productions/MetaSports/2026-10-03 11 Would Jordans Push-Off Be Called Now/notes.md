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
