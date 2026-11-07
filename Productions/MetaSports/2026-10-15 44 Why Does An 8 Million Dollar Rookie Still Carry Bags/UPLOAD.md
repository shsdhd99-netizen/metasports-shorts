# #44 Why Does An $8 Million Rookie Still Carry Bags (2026-10-15)

**DRAFT AWAITING OWNER APPROVAL. Not uploaded, not scheduled.** Video: `final.mp4` (20.7 s, voice A = Alex, no background music, no sound effects).

## Title
Why Does An $8 Million Rookie Still Carry Bags? 😭
- alts: "Cooper Flagg Still Has To Carry The Bags 😭" / "The $8 Million Rookie Who Still Carries Bags 💀"

## Tags (448 chars)
cooper flagg, cooper flagg rookie card, cooper flagg 8 million card, cooper flagg carrying bags, cooper flagg rookie duties, cooper flagg mavericks, dallas mavericks, mavericks veterans, nba rookie hazing, rookie of the year, cooper flagg macao, nba china games 2026, cooper flagg new balance, most expensive basketball card, topps debut patch card, mavericks rookie duties, nba sophomore, nba 2026-27, nba facts, nba shorts, basketball shorts, nba

## Pinned comment
His rookie card sold for $8.04 million and the vets still had him on bag duty in China. Fair rookie tax, or should the Rookie of the Year be off the hook?

## Music and sound
- No bed (house default).
- No effects: nothing on screen makes a sound worth adding.
- If you want a song, add it in the YouTube app (route A, `Library/Sound Library.md`). Start it after "carry the bags." and let it cut on "But yeah".

## Known limits (said plainly)
- **No video of the bag-carrying exists that we found.** Those lines run over Flagg on the same Macao trip and over ESPN's exact words. Nothing on screen claims to be the bag-carrying.
- **The Macao footage comes from the NBA's 720x900 post**, blown up 2.2-2.7x (house standard ~1.8x). No sharper official copy was found. Shot 7 (A1) reads a little soft.
- **Proof cards fill 33% of the runtime** (guideline 25%) because two of the claims are reported facts with no footage.
- **Timing:** "this month" and "just sold" are true through October. Post by Oct 31, or change "this month" to "this fall".

## QA (Oct 15)
`qa_short.py --full`: PASS.
- Captions match the script word for word.
- Export speech matches the script at 99% (Macao/Macau is a spelling).
- No clipping (voice peak -3.5 dBFS, export -1.8 dBFS).
- Loudness -14.4 LUFS.
- Widest caption 800 px (auto-fit).
- Every clip logged and verified in `sources.csv`.
- Voice check: CHECK, not REDO. The "dollars" REDO was the speech-to-text writing "$8 million"; the word is spoken at -19.5 dB like its neighbours, and the tool is fixed.
- Frame sheet viewed at every cut.
- **I can't hear the audio.** Listen once before approving.
