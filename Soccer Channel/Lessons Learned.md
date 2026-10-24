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
- **[V] S01 30K in 2 days; S02 1.2K, S03 1.4K.** S01: a singular one-person title, a secret object as the hook, 59.5 s. S02/S03: plural list titles, 63 and 71 s. n=3, so this is a lead to test, not a rule [H]. **Superseded Oct 24 (below): the title shape was not the cause.**
- **[Rule] Every Short under 60 s.** A Short over 60 s with an active copyright claim is blocked worldwide (YouTube Help, three-minute Shorts). S02/S03 got no claims, but archive broadcasts invite them.
- **[V] A bookmaker's "in our 130-year history" quote was about the payout size, not the odds** (S07). Read what the superlative measures.
- **[V] AP's play-by-play is the reliable source for which way a keeper dived** (S05 said left; he went right).
- **[V] Cutting a whole sentence from a finished render works:** cut the video on the shot-change frame and the audio at the quiet point a few ms later, by the same length, so sync holds (S06, 62.4 s to 58.8 s).

## Oct 24, 2026 (S04, S05, S07 finished in the cloud on the new account)
- **[V] Without an ElevenLabs key, most fact fixes can still be made from the take itself.** `Tools/word_edit.py` cuts words (or swaps in the same word from elsewhere in the take). S07 "William Hill" -> "Bookmakers" (taken from the last line), S05 "the Argentina players" -> "Argentina" (from "But Argentina scored"). Cut in silence or in the stop closure before k/t/p; when a piece ends inside a word, end it before the next consonant's hiss (check the high-frequency energy) or the transcriber hears "Argentina's". Check every joint with local speech-to-text (faster-whisper small.en).
- **[V] The take's own last line can be cut to end on an earlier, sourced line.** S07 now ends on "Around half of those fans had already cashed out", S05 on "feel on the day". Both are still a payoff, and both got under 60 s.
- **[V] The 2018 World Cup is on archive.org as a 31 GB 4K HDR broadcast.** Pull only the needed seconds straight off the URL and tone-map to SDR (`zscale ... tonemap=hable`), about 3 s of work per second of footage; the 480p copy maps the moments. The 720p mkv of the 2006 final seeks the same way (`src/pull720.sh`), about 2 s per second.
- **[V] A wide shot from behind the goal and the reverse angle settle a dive direction in seconds.** The 4K broadcast confirmed Pickford went to his right with his left arm up (the Oct 23 check from AP was right).
- **[V] QA's "same footage twice" also catches two moments from the same static wide camera** (S04: the penalty set-up and the run-up). Use a different camera for one of them.
- **[V] Mixkit rate-limits (429) after a few searches in a row.** Search early, then reuse ids.
- **[S] Broadcast replays can carry another network's ticker** (ESPN "program alert" under ABC's 2006 replay). Crop it with `zoom` and `y: 0`, and check the face is still in frame (Z23 needed `x: 0.76`).


## Oct 24, 2026 (why S02 and S03 flopped: `Research Notes/Why S02 and S03 Underperformed (Oct 24, 2026).md`)
- **[V] "Stayed to watch" decided it: S01 80%, S03 65%, S02 56%.** It is settled in the first second or two, so frame 1 and line 1 carry the Short.
- **[V frames, H cause] Frame 1 must show the promise happening.** S01 opened on the hand going into the sock under "hid a CHEAT SHEET in their sock". S02 opened on Balotelli's face (scan lines, channel logo) under "TROUBLE"; S03 on Dudek's face under "DANCED", with the dance at 54 s.
- **[V] The promised thing must come back by about 20 s.** S01: 18 s. S03: 54 s, after a 46 s detour through the comeback and 11 names in 15 s (72% average viewed vs S01's 94%). QA now warns on both (cuts.json `"promise"` list).
- **[H] Category hook words lose.** "Trouble" was never said again. Ahmed's titles with vague words (trouble, drama, crazy, wild): median 200K vs 277K overall (n=34).
- **[V] Title shape is neutral.** My first read ("plural 318K vs singular 217K") was an era effect: Ahmed's singular titles are all from 2024, when his channel was tiny; plural titles sit at his channel median (0.99x). Post the spoken line 1 as the title. (`Research Notes/Niche Study - Soccer Story Shorts (Oct 24, 2026).md`)
- **[V] Say the stakes, specifically.** Vague words are only weakly worse (0.87x, n=92; Ahmed's 3 "trouble" titles have a 1.0M median). Strong verbs lift (1.35x, n=107). Own-side conflict (refused, betrayed, sued, "their own") is the strongest title signal: 610K vs 313K, 1.63x time-adjusted (n=87).
- **[V] Even Ahmed's format sat at about 17K a Short for its first ~106 Shorts before jumping to 340K.** Our soccer rules are hypotheses until 20-30 Shorts.
- **[V] A dark first frame slips past blackdetect.** S04's first 0.25 s was someone passing the camera (brightness 32 of 255). QA now gates on frame 1 brightness (good frames 70-115); S04 re-cut 0.3 s later and re-rendered.
- **[H] One soccer Short a day.** S02 went out the same day as S01.
