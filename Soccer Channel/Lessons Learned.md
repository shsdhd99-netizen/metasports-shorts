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
