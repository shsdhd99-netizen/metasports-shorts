# QA audit (auto-written by Tools/qa_audit.py)

22 saved QA outputs; verdict counts: {'PASS': 19, 'FAIL': 3}.

| Level | Finding (normalised) | Fired | In Shorts | Read |
|---|---|---|---|---|
| warn | footage: shot # <clip>: blown up #x (#x#, crop zoom #): archive footage, accepted in the story format (Ahmed's Shorts use soft #p archive); keep faces | 180 | 5 | recurring |
| warn | footage: shot # <clip>: blown up #x (#x#, crop zoom #; house standard is a #p source, about #x): note in PACKAGE.md that no better source exists | 157 | 9 | noise or process flaw: fires in most Shorts |
| warn | footage: shot # <clip>: soft (edge contrast # vs this Short's median #): motion blur or a poor encode | 52 | 9 | noise or process flaw: fires in most Shorts |
| warn | export: the export says what the script says (#% word match after number folding); # difference(s) to listen for (speech-to-text mishears names): hear | 16 | 10 | noise or process flaw: fires in most Shorts |
| warn | hook has no number or conflict/question word in the first # words: '..' (state the question the viewer needs answered by # s) | 14 | 8 | noise or process flaw: fires in most Shorts |
| warn | footage: shot # <clip>: very busy picture (#th-percentile frame change #; top #% of our clips): fast action, a whip pan or shake; check it reads on a  | 12 | 3 | recurring |
| FIX | footage: shot # <clip>: blown up #x from its source (#x#, crop zoom #): find a #p+ source or crop less | 7 | 1 | rare |
| warn | a background bed is baked in: the house default is none since Oct # night (Library/Sound Library.md); say why in PACKAGE.md | 7 | 7 | noise or process flaw: fires in most Shorts |
| warn | music track '..' is a candidate the owner has not approved by ear | 7 | 7 | noise or process flaw: fires in most Shorts |
| warn | last shot is not the first clip (fine if the ending image serves the payoff; never add a sub-# s shot just to loop) | 6 | 5 | recurring |
| warn | export: captions on screen under # s at [#] s (too fast to read) | 6 | 4 | recurring |
| warn | export: captions on screen under # s at [#, #] s (too fast to read) | 6 | 3 | recurring |
| warn | only # shots in first # s (guideline #; shot length did not separate winners) | 5 | 4 | recurring |
| warn | footage: shot # <clip>: the clip cuts to other footage at [#] s (clip time): check the footage after the cut still matches the line (player, game, sco | 5 | 2 | rare |
| warn | shots under # s read as noise: [#] | 4 | 2 | rare |
| warn | length #s (Ahmed's Shorts run #-# s; median #-# s) | 4 | 2 | rare |
| warn | talking head #% of runtime (guideline <=#%): is every claim proven on screen? | 3 | 3 | recurring |
| warn | clips shorter than their shots (slowed/held by assemble, not looped): [('..', #, #), ('..', #, #), ('..', #, #), ('..', #, #)] | 3 | 2 | rare |
| warn | footage: source size unknown for # clip(s) (<clip>): cut new clips with broll.py cut (it logs it) or add '..' to their notes | 3 | 2 | rare |
| warn | no notes.md (needs Lane, Concept, Added value, claim -> exact source quote) | 3 | 2 | rare |
| warn | clips shorter than their shots (slowed/held by assemble, not looped): [('..', #, #)] | 3 | 2 | rare |
| warn | speech pace # wpm (guideline #-#: our old hits ran #-#, Clank'..'t drag, don't rush. Digits count as one word here) | 2 | 2 | rare |
| warn | slow hook: the first sentence ends at # s (aim for the question to be clear by about # s; one fact, no compound sentence) | 2 | 2 | rare |
| warn | two cards in a row at shots [#, #, #] (the critic flags back-to-back reading) | 2 | 1 | rare |
| warn | footage: source size unknown for # clip(s) (<clip>, <clip>): cut new clips with broll.py cut (it logs it) or add '..' to their notes | 2 | 1 | rare |
