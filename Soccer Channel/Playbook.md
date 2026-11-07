# Soccer channel playbook v3 (Nov 7, 2026): rules that earn their place

The owner approved the Theory Ranking on Nov 7. These rules win for FC.
- The shared rules: THE RULES at the top of `MetaSports - Playbook.md` (O1-O10 owner rules, S1-S2, E1-E7, P1-P5, Q1-Q3). They also apply here.
- Old playbook, word for word: `Research Notes/Rule History - Soccer Playbook before Nov 7 rewrite.md`.
- Evidence: `Research Notes/Theory Ranking and Rules Challenge (Nov 7, 2026).md`.
- Live tests and scores: `Research Notes/Lab/Scoreboard.md`.

Tiers: **[V]** measured on our channel, **[S]** small sample or competitors, **[O]** owner rule, **[H]** house style.

## F1 What to make
- **The proven lane: a famous penalty shootout + one odd act, by the keeper OR the takers.** [V]
  - The six we made all got 8.6K-29K (median 19.6K). Every other FC Short is under 3.8K (n=10).
  - It's the shootout, not the goalkeeper. The England subs (no keeper trick) got 12K. A goalkeeper story with no shootout moment (S27) got 1.3K. A club story about penalties (S19) got 3.8K.
  - Check: lab `topic_shootout`.
- **Each shootout Short is a different famous shootout, with its own new sourced fact.** Never a sequel of a trick already shown.
  - Ready to voice: S38 Bounou v Spain 2022, S43 Van der Sar v Chelsea 2008.
  - Sources to mine: World Cup, Euros and Champions League finals and knockouts.
- **A famous moment beats a famous name.** Our hits name Lehmann, Krul and Kepa; the Messi napkin Short got 1.0K. (The old "global names only" rule is scrapped.) [V]
- **New premises: one a week, as the live test `fc-premise`.** Ideas: a star's relative with a twist, "kept his promise", a one-mistake chain, bargain scouting, fans beat the club. Each needs two sources and a FRESH copy-check. [S]
- **About half or more of FC builds stay in the shootout lane** until a new premise wins its test.

## F2 Script (Ahmed's Goal shape) [S]
- Line 1 is the spoken title (11 words or fewer), then "Back in...". A turn by about 15 s, 2-4 escalations, then the payoff number or irony as the last line.
- No question and no promo at the end [O].
- **190-240 words, under 59.5 s after `tighten_voice.py`** [O]. If it runs long, cut a sentence; never add one.
- Pace about 226-233 wpm (Ahmed's 230) [S].
- Every number has its source and exact wording in notes.md; keep qualifiers. When sources disagree, write the line so it's true under both [O].
- Style v3 moves (a misread by 8 s, "what nobody knew" by 15 s, a reason for every "no") are queued as the test `fc-style-v3`.

## F3 Opening
- Frame 1 shows the moment line 1 is about: sharp and lit, held about 2 s or more under the title card [H].
- **Live test `fc-opener`:** action-first (the title on screen only; line 1 is the first story sentence) vs title-first (the control), on shootout Shorts. `lab.py assign fc` says which arm is next.

## F4 Ending
- The payoff is the last line, held on screen about 2-3 s [S].
- A natural loop is the queued test `fc-loop`; never add a shot just to loop.

## F5 Picture, sound, captions
- One shot per phrase, about 1.1-2.1 s each (Ahmed's rate; house style, not a gate) [H].
- Wide plays at 3:4 over blur; real footage of the named person when the name is spoken; stock only for abstract lines; a recreation is labelled "recreation" [O/H].
- Captions `--caption-style ahmed` (centred, white, 2-3 words) [H].
- No cards [O], no emoji, no decorative SFX [S].
- **Music: the live test `fc-music`.** Render the music and no-music versions while it runs. The uploaded file name logs the arm automatically (`Scheduled Uploads.csv`), so the Hub card only needs to say which one to post.
- Real audio when the key moment has a famous live English call (`Tools/nat_sound.py`, commentary bed at -26).

## F6 Posting and the package
- **12 PM ET** is the FC grid slot (`next_gap.py`). Up to 3 a day, 6+ h apart, only if each is as strong [O, Nov 5].
- Title = the spoken line 1. "The goalkeeper who..." is the series control.
- Description empty. No hashtag or #football. Tags filled to about 490 by `tags_fit.py` (a warning, never a fail) [O].
- Pinned comment optional: a source line or "Part 2" [V YouTube].
- Judge at 72 h (the lab reads it 5-8 days after go-live). FC stand-in for "stayed": avg % viewed 85%+ (hits 83-96%, flops 64-82%) [V].
- Never re-upload [O].

## How to make one
The steps live in the skill, `.claude/skills/story-short/SKILL.md` (format: `FORMAT.md`). Where it disagrees with this file, this file wins.
Run `python Tools/lab.py assign fc --folder "<folder>"` before writing the script, and follow every arm it prints.
