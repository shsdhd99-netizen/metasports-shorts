# Soccer channel playbook (Oct 21, 2026)

**How to make a Short:** the step-by-step lives in the skill, `.claude/skills/story-short/SKILL.md`, so one copy stays current. The format itself, with evidence, is in `.claude/skills/story-short/FORMAT.md`.

## Channel rules (on top of the skill)
1. **Copy what works.** Ahmed's Goal shape: title as line 1, "Back in...", a turn every 8-12 s, a payoff number, a teaser; 60-80 s; a new picture every 1.1-2.1 s; centred TikTok Sans captions; a quiet bed. Change nothing until our own numbers say so (`Outcome Log.md`).
2. **Global names only.** Messi, Ronaldo, Beckham, Zidane, Balotelli, Lehmann at a World Cup... Obscure names flop on Ahmed's channel (27-41K vs 276K median).
3. **One story per Short**, even though the title sounds like a list. When a title works, reuse it as a series with a new story ("Goalkeepers who..." is our first series).
4. **Every number sourced** in notes.md with its exact wording. Keep qualifiers. When sources disagree, write the line so it is true under both.
5. **Real footage of the named person** on screen when the name is spoken. Stock is only for abstract lines. A recreation is labelled "recreation" on the picture.
6. **Two renders per Short:** with the music bed (Ahmed's way) and without. The owner picks until the numbers decide.
7. **Cadence:** 1 a day to start (the ElevenLabs Creator plan fits about 30 a month); Ahmed runs 2 a day. Never more than 2 a day: their medians fell at 3.
8. **Never post.** Drafts only; the owner uploads.

## Differences from the NBA channel (on purpose)
| | NBA (MetaSports) | Soccer (this channel) |
|---|---|---|
| Length | 20-45 s (THE #42 FORMAT) | 60-80 s (Ahmed's story format) |
| Opening | Number or name in the first words; 3 cuts in 3 s | Title read aloud; first picture holds about 2 s under a title card |
| Captions | House style (karaoke/clank) | `--caption-style ahmed` (TikTok Sans, white, centred, 2-3 words) |
| Music | None by default (owner, Oct 14) | Quiet bed about 20 dB under the voice (Ahmed's way), plus a no-music version |
| Ending | Payoff, then the last frame loops to the first | Payoff, then an optional next-video teaser |
| QA | `qa_short.py` (nba profile) | `qa_short.py` (story profile, automatic under `Soccer Channel/`) |
