# Critique Round 1: verdicts (Oct 4, 2026)
Critic report: `Critique Round 1 (Oct 4, 2026).md`. Each point judged on evidence, not to please. ACCEPT = changed. PARTLY = changed in part. REJECT/DEFER = reason given.

| # | Critique | Verdict | What I did / why |
|---|---|---|---|
| 1 | Hooks are news statements; gate regex is weak | PARTLY | Replaced regex with a warn (number or conflict/question word in first 8 words). Counter-argument holds that strong frame 0 + headline carry the first second, so I did NOT rewrite finished hooks; the 24 h Viewed-vs-swiped on #14-#18 will decide. Future rule: name the question the viewer needs answered by 1.5 s. |
| 2 | #18 wrong uniforms, Maxey punchline unexplained | ACCEPT (verified in frames) | Remade #18: Lakers shots replaced with Sixers-uniform LeBron cuts from the media-day clip, Maxey named and set up ("whose car broke down that day"), "$8M" caption bug fixed. |
| 3 | #15/#16 and #11/#14/#17 share footage and ending shape | ACCEPT | Rule: one Short per story family per week; closer must vary. Advice to user: post only one of #15/#16 first (recommend #16), hold the other a few days. |
| 4 | Rule lane evidence is evergreen listicles, not news explainers | PARTLY | True; the 2.5x is observational. Next batch is balanced: rule-news AND evergreen 'Why/How' oddities (our own channel's hits). No lane is "proven" for us until our analytics exist. |
| 5 | Gate is circular, docs disagree with code | ACCEPT | Gate described as a hygiene check, not quality. Docs fixed to match code. Outcome log started (`Outcome Log.md`), mandatory columns gate metrics vs 24 h viewed%. |
| 6 | Cutting too fast (1.2-1.5 s) vs Clank 2-4.7 s | DEFER (test) | No evidence either way. Not changing the house pace blindly. Running a same-script A/B (#17 karaoke variant is the caption test; a slower cut is next). Min-shot warn added (<0.6 s). |
| 7 | Identity and word-picture sync unverified; #13 off-by-one | ACCEPT | #13 re-synced to words (my own cut-away edit had caused part of it). Process rule: after assembling, check the shot under every spoken name. |
| 8 | #15/#16 weak stories, no turn | PARTLY | Warn exists. Not remaking; they are announcement stories, so they post after the others and one at a time. Lesson logged: every script needs a turn and an arguable ending. |
| 9 | Third-party clips, rights risk, no notes.md | ACCEPT | notes.md now a warn in the gate; backfilled for #14-#18. Rule: at least one non-official visual per Short when possible; keep under 60 s. |
| 10 | Overclaims | ACCEPT | #13 now says "to acquire and retain" (the source's words) and its timing fixed. #12 is already posted (not touched). Rule: claim -> exact source quote table in notes.md. |
| 11 | Quote audio 2-3 dB quieter than narration | ACCEPT | splice_voice now normalises quotes to -16 LUFS (was -18) and pads a tail. Takes effect on new Shorts; #18 rebuilt with it. |
| 12 | 'PROVEN' labels over-claim (n=8..52, survivors) | ACCEPT | Relabelled as OBSERVED in the skill; hard gates kept only for things with a mechanism (no filler open, loudness, cut-off voice, dead air). |
| 13 | Captions on faces / untested house style | PARTLY | Made a `karaoke` variant of #17 so the user can A/B the same Short. House style stays default until data. |
| 14 | Loop tail clips the last word | ACCEPT | Hard fail if the voice ends under 0.1 s before the video end; splice pads 0.3 s; #13 and #14 repaired. |
| 15 | 2/day plan is a risk with no data | NOTED, not changed | The user chose 2/day; I will state the risk: read Viewed-vs-swiped on the first few posts before posting many more of one recipe. |

Rule for the future: a critic pass before each batch of 3+ Shorts, verdicts logged here, nothing changed without evidence or a verified defect.
