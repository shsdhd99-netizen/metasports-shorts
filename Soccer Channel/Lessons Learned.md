# Lessons learned (soccer channel)

**Evidence tiers:** [V] measured, [S] seen a few times, [H] my reading.

## Oct 21, 2026 (S01 and S02)
- **[V] Check every date in the script against the source's own timeline.**
  - S02 v2 said "the night before the derby"; the fire was just before 1 a.m. on Saturday, and the derby was on Sunday.
  - It also said "two days after"; the safety campaign went out the next day (mancity.com is dated Mon 24 Oct).
  - Both were caught before rendering, by reading the sources' own dates.
- **[V] Sources can disagree on who did what. Word the line so it is true under both versions.**
  - FIFA says Lehmann wrote the names himself; Reuters says Köpke wrote the note.
  - So the script says Köpke "studied" and the tips "ended up on" the page.
- **[V] The first take often drops "Back" after the title line.**
  - It happened on S01 and S02 (v1 and v2): the voice check heard nothing at about 2 s.
  - The second take was fine both times. Budget for 2 takes (about 3K credits a Short).
- **[V] Story-format length:** 260-275 words with the Alex voice at native speed gives 63-68 s. 194 words gave only 46 s.
- **[V] White captions on a cream graphic are hard to read.**
  - Keep every card and graphic above y=890, so the centred captions (y=960) sit on the dark fill.
  - `make_note.py` and `make_cards.py` assert this.
- **[V] Archive footage (2006 broadcast at 576p, 2011 BBC at 368p) has no HD copy.**
  - The story QA profile allows up to 6x blow-up as a warning, because Ahmed accepts soft archive.
  - Use full-frame crops for faces and action; put wide shots over a blurred fill (`--blurfit`).
- **[S] The famous match moments are on archive.org as full TV broadcasts or highlights.**
  - Search: `advancedsearch.php?q=title:(...)`.
  - The 2006 "all goals" video covers every World Cup goal, which is useful for player names.
  - Mixkit covers the abstract lines: fire, cash, hotel, clocks.
- **[H] A recreated graphic (the note) is the honest way to show a famous object we have no photo of.** Label it "recreation" on the picture itself.

## Oct 22, 2026 (owner feedback on S01/S02, and S03)
- **[Owner rule] No promo or teaser at the end.** "That will instantly kill retention." The video stops on the payoff. S01's "my next video... follow if..." outro was cut (66.1 s -> 59.5 s).
- **[Owner rule] No unnecessary pauses.** voiceover.py's word-timing trim left 0.5-0.7 s tails and breath gaps, because TTS word timings swallow the pauses. `Tools/tighten_voice.py` measures the silence on the audio itself (silencedetect at -38 dB) and cuts it.
  - Soccer setting: pauses over 0.09 s cut to 0.06 s.
  - NBA setting (real-audio quotes): pauses over 0.25 s cut to 0.12 s.
  - Tail: 0.25 s.
- **[V] The last word's TTS end time runs past the real sound** (S02: by 0.2 s). QA then reads the tail as cut off. tighten_voice now ends the last word where its sound ends.
- **[V] cut_list.py only cuts missing clips.** After changing a shot in cuts.json, delete that clip (or use `--force`), or the old cut stays.
- **[S] archive.org has the 2005 final in 720p** (the SAT.1 broadcast, split into halves, extra time, penalties and celebration), and the 1984 final (RAI). Use ffmpeg `-ss ... -t ... -c copy` straight off the URL to take only the needed minutes. The disk allowance is small, and big files need several minutes to download.
- **[S] archive.org returns 5XX when many seeks hit it at once.** Keep URL contact sheets to 2-3 parallel requests.
- **[S] A fact the source gives as a person's own words beats a summary.** S03's best details (Dudek's book on 100 Milan penalties, Carragher "jumped on my back", Grobbelaar's "spaghetti" line) all came from first-person interviews: the Guardian 2025, liverpoolfc.com and UEFA.com 2009.

## Oct 23-24, 2026 (first results, fact-check)
- **[V] S01 30K in 2 days; S02 1.2K, S03 1.4K.** S01: a singular one-person title, a secret object as the hook, 59.5 s. S02/S03: plural list titles, 63 and 71 s. n=3, so this is a lead to test, not a rule [H].
- **[Rule] Every Short under 60 s.** A Short over 60 s with an active copyright claim is blocked worldwide (YouTube Help, three-minute Shorts). S02/S03 got no claims, but archive broadcasts invite them.
- **[V] A bookmaker's "in our 130-year history" quote was about the payout size, not the odds** (S07). Read what the superlative measures.
- **[V] AP's play-by-play is the reliable source for which way a keeper dived** (S05 said left; he went right).
- **[V] Cutting a whole sentence from a finished render works:** cut the video on the shot-change frame and the audio at the quiet point a few ms later, by the same length, so sync holds (S06, 62.4 s to 58.8 s).
