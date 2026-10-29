# #74 Why nobody shoots free throws underhand (Oct 28, 2026)

> **FACT FIX, Oct 29 (cloud review):** "Still a record." was WRONG and is cut from both DRAFT files. Bam Adebayo made 36 of 43 free throws in his 83-point game on Mar 10, 2026, the new single-game record (Wikipedia, "Bam Adebayo's 83-point game": "36 made out of a possible 43"). Cut on the shot change into U07 (video frames 358-377, audio 11.885-12.552 s); both renders are now 24.7 s. The originals are in `_pre_factfix/` (git-ignored if large). words.json / captions.srt still hold the old timing: if this Short is ever re-rendered from clips, run `Tools/word_edit.py --edit 11.885-12.552` first.
> Kept, minor: "So Wilt Chamberlain... tried it too" reads as if Wilt copied Barry; Wilt shot underhand in 1961-62, before Barry reached the NBA (1965). Cutting "So" would leave the burned caption "SO WILT CHAMBERLAIN" on screen, so it stays; don't repeat the order claim anywhere else.
**Why this topic:** owner, Oct 28: "rebuild the best nba/soccer scripts youve seen, and make your own video on the same topics".
CoachClank's "Why No One Shoots Underhand" got 10M views (Script Library, Oct 27). Our angle differs: Clank told the
Rick Barry and Shaq story; ours centres on Wilt's 100-point night and his embarrassment. The script is our own; no wording copied.
Copy-check: TAKEN by CoachClank (owner chose the topic knowingly); different angle and payoff.
**Lane:** a rule or oddity that passes the stranger test (anyone gets "the shot that works, that nobody uses").

## Claims and sources (exact words)
- Barry ~90% underhand: CBS SF, "Barry made 90 percent of the free throws he attempted over his 14-year career".
  https://www.cbsnews.com/sanfrancisco/news/warriors-legend-rick-barry-reveals-free-throw-secrets-laments-no-one-shoots-underhanded
- Wilt career .511, low of .380 in 1967-68: Wikipedia "Wilt Chamberlain": "a .511 career average, the third-lowest in NBA history,
  with a low of .380 over the 1967–68 season" (season table: 1967–68 FT% .380).
- Underhand in the 100-point game; 28 made, still the record: Wikipedia "Wilt Chamberlain": "set the NBA record, later equaled by
  Adrian Dantley, for the most free throws made in a regular season game (28) by using the underhand technique during his 1962
  100-point game" (cites NBA.com records). 28 of 32: Wikipedia "Wilt Chamberlain's 100-point game"; NBA.com/Stats on X
  ("28-32 FTM"). "Still a record" = still the record, shared with Dantley.
- Started underhand that season (McGuire's suggestion): Wikipedia "Wilt Chamberlain's 100-point game".
- Too embarrassed to keep it: Wikipedia "Wilt Chamberlain": "Chamberlain later said he was too embarrassed by the underhand
  technique to continue using it, despite it consistently giving him better results" (cites Gladwell, Revisionist History,
  "The Big Man Can't Shoot"). His autobiography line, via Gladwell: "I felt silly, like a sissy, shooting underhanded."
- Barry offered to teach Shaq; Shaq: NBC Sports headline "Shaq on free throws: 'I told Rick Barry I'd rather shoot 0% than shoot
  underhand'". https://nbcsports.com/nba/news/shaq-on-free-throws-i-told-rick-barry-id-rather-shoot-0-than-shoot-underhand
- "28 of Wilt's 100 points came from a shot he was too embarrassed to keep": 28 FT made, underhand, in the 100-point game.

## Footage (all X; see src/*_moments.json, Gemini-located)
- Rick Barry underhand FT + swish: Warriors Archive footage via @Super70sSports (1803116463382765709), 0.0-4.8 s.
- Rick Barry, shirt and tie, eyes-closed underhand FTs at a Bulls game (broadcast) via @BruceBlitz (1696185535348269383), 8-20 s.
- Wilt game footage, the "100" photo, the "Chamberlain Scores 100 Points" headline, Wilt and Rick Barry interviews:
  official @NBAHistory (837314735146164224).
- Wilt overhand FT and miss (later career, Lakers; broadcast lower third): @pitlessball (1965891614964072677).
- Shaq on ESPN's halftime desk: @MrBuckBuckNBA repost of @ESPNNBA (2028232028928274603), 16-20 s / 51-57 s.
- No video of the 100-point game exists (not televised). Never present other footage as that game; the 100 beat uses the
  photo and the headline. Not used: @overtime's "100 POINT GAME FOOTAGE" (it's the 73-point game) and creator edits.
- Licence risk: fan reposts of broadcast footage (Barry, Wilt FT, Shaq). Official: @NBAHistory, Warriors Archive.

## Build (Oct 28)
- Voice: take 3 of 3 (takes 1-2 failed the delivery and word checks). The speech check heard "Berry" for "Barry"; Gemini's
  pre-check heard no voice problems.
- Edit: 13 shots, 25.3 s; frame 1 = Barry's underhand free throw; the payoff replays it at 0.5x. Overlays 90% / 28 of 32 / 38%.
  NBA History's 480p video sits in 3:4 windows (a full 9:16 crop blew it up 4x and failed QA).
- Full QA PASS (both versions). Warnings: archive film is soft and low-resolution; no better source exists.
