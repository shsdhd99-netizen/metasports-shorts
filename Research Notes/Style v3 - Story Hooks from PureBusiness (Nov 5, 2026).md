# Style v3: story scripts and editing, learned from @PureBusinesshorts (Nov 5, 2026)
Evidence: Gemini watched 7 of their Shorts (Dyson, McAfee, Bacardi, YETI, Koenigsegg, Johnnie Walker + 1), tier [S]; channel median about 142K views over its last 60 Shorts.
The full top-vs-bottom study stopped (Gemini overloaded, 503s); re-run it later with `python Tools/watch_study.py --channels @PureBusinesshorts --name PureBusiness --top 6 --bottom 6` (cached reports are reused).
This is a HYPOTHESIS style to A/B, not a proven rule. THE RULES in the Playbook still win.

## Script: the 7 moves they use every time
1. **Line 1 = a named person + a hard verb + the object, as a plain fact.** "Fidel Castro seized the Bacardi distillery in 1960." "Roy and Ryan Siders kept destroying their coolers." No question, no "the X who..." label, no "back in".
2. **A misread in the first 10 s.** "He wasn't being generous. He was building the market." / "He thought he'd taken everything." The viewer's first guess is wrong, so they stay to learn why.
3. **"What he didn't know..."** One hidden fact that flips the story (the yeast, the bag money). That's the turn, by about 12 s.
4. **Stacked negatives make the odds feel bigger:** "No degree, no factory, no investors, no experience." Three or four, short.
5. **Every "no" gets its reason:** "Hoover turned him down. They made too much money selling bags." The reason is the interesting part.
6. **Escalation by dated steps** (1994... 2002... 2010), each one bigger, one number each.
7. **The last line is short, quiet and in the present tense, tied to line 1:** "The bats are still there." "The company still carries his name." No question, no promo. That's the loop.
Length 50-62 s, about 160-190 wpm (slower than ours). They still hold attention because every sentence is a new fact.

## Editing
- 4-5 cuts in the first 5 s (about 1 s each), then 2-2.5 s shots. Average 1.6-2.5 s.
- **Line 1's words are on screen in big text while it's spoken** (the name in caps in 0-3 s).
- **A literal picture for every phrase:** the clogged bag, the dirty carpet patch, the rep waving no.
- **Numbers animate:** counters (5,000 to 5,127) and a rising bar for the payoff ($20B). The number sits on the scene, never on a card.
- Logos and labels inside the scene for each company or rival named.
- Quiet upbeat music from 0 s; 2-word ALL CAPS pop-in captions, centred.
- One consistent visual world all the way through (theirs: stick figures on photo cutouts; ours: real game footage, same grade, same caption style).

## Our version (MetaSports v3), for NBA and FC story Shorts
- Line 1: [Name] + [verb: banned, refused, seized, hid, sued, beat] + [object]. Plain fact, 11 words or fewer.
- By 8 s: the misread ("He wasn't being lazy. He was...").
- By 15 s: "What nobody knew..." / "But here's what they missed..."
- Each rejection or obstacle gets its one-line reason.
- Payoff number animated on footage (`counter` overlay, to build: an ffmpeg drawtext ramp).
- Last line: short, present tense, echoes line 1 ("He still has the napkin." / "The number is still banned.").
- Edit: 4-5 cuts in the first 5 s, then about 2 s; name on screen at 0-3 s; a rival's logo or face at the "no" beat.
- A/B: the next 4 story Shorts in v3 vs our last 4; judge by Viewed % and average % viewed in Studio.

## Nov 6 correction from our own FC data
Our 4 best FC Shorts (15-29K) all open "The goalkeeper who..." / "Goalkeepers who...". So for FC keep that title frame and use the v3 moves only inside the script (the misread, the hidden fact, a reason for each "no", the short echo at the end). S21 is the one test of the name-first opener.
