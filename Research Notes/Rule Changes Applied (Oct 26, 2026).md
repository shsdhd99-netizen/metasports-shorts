# Rule Changes Applied (Oct 26, 2026)

**What this is:** the overnight review's decisions, written into the rulebooks. Owner's ask: "do a review of our playbook/rules... everything is up for debate". The decisions came from five notes in `Research Notes/` (all Oct 26, 2026): *Rules Review*, *Retention and Editing Upgrade* (RET), *Posting Study* (POST), *Similar Channels* (SIM), *Why NBA Views Dropped* (WHY).

**Tiers:** [V] measured · [S] small sample, or seen on other channels · [H] a guess to test.

**Where the rules live now:** THE RULES at the top of `MetaSports - Playbook.md` (NBA, plus the rules marked "FC too") and `Soccer Channel/Playbook.md` (FC). Every changed line in the docs says "(Oct 26 overnight review)".

**Unchanged owner rules (kept everywhere):** never post, schedule or upload (DRAFTs only); no cards (1.5 s max if one is unavoidable, never in the first 4 s); no promo, teaser or subscribe outro; no dead air; no API keys in docs; TikTok/Instagram cross-posting paused.

## 1. Editing
| File, section | Old rule → new rule | Tier (source) |
|---|---|---|
| Playbook THE RULES §2; cloud-short QUALITY FORMULA 1 + order line; nba-short steps 6 and 8; daily-run D; B-roll Guide rule 1; story-short step 1; story QA.md | "Find 6+ clips before writing, or drop it" / "six moving clips" / QA "6+ source clips" → **Footage first:** frame 1 + one proof clip per beat, any number of sources; never cut to filler for a clip count | [S] WHY §3 |
| Playbook THE RULES §2 + §5 Cuts; cloud-short OCT 26 EDITING RULES + "first 3 seconds"; daily-run D; ESS §1; Soccer Playbook rule 12; CLOUD STATE House rules | "3+ cuts in 3 s", "a new image every second", "add a cut if neighbours look alike", "typically 1-2.5 s" → **shot 1 ≥ 2.0 s; ≤ 2 shots in 3 s; ≤ 3 in 5 s; about 10-15 shots of ~2 s; no cut inside line 1** (soccer: shot 1 ≥ 2.0 s, ≤ 2 in 3 s) | [V] RET §1b (3 or fewer in 5 s: 78.4% vs 66.5%, p=0.002); WHY §2 |
| ESS §1.7; B-roll Guide §4 | "Shots up to 3.6 s" (NBA), "short cuts ≤ 2-3 s" → **a play may run 3-5 s**; caps are what QA FAILs (NBA 6 s, soccer 3.6 s) | [V] WHY §2 |
| Playbook §2 + checklist 3; cloud-short §2 + first 3 s; nba-short step 6; story-short step 3; SCRIPT.md | "number, name or stakes is the FIRST word" → **line 1 is 11 words or fewer**, one claim, done by about 3 s; never a bare number first | [V] RET §1b (72.6% vs 62.2%) |
| Playbook §2; cloud-short; nba-short; ESS §1.1; THE 42 FORMAT §2; story-short step 6 | "Frame 1 already moving or a face", 12% punch-in → **frame 1 shows the thing line 1 is about, happening**; push-in 2-5% only on a static shot | [S] RET §2b; face vs action no gap [V] |
| Playbook §2 + §5; cloud-short rule 6 + §6; ESS §1.4-1.5; B-roll Guide rule 4; story-short step 6; QA.md | (new) → **replay the key second once before the payoff** (closer and/or 0.5x), marked `"replay": true` (cut_list.py now passes it to shots.json) | [S] RET §4 change 2; untested for us |
| Playbook §2 + §5; cloud-short §4; daily-run D; ESS §1.8; B-roll Guide rule 7; story-short step 6; FORMAT.md; QA.md | Wide shots = full-width `--blurfit` → **fill the frame: crop wide plays to ~3:4** (`--blurfit-aspect 0.75` / `"blurfit_aspect": 0.75`); full width only for graphics/text read whole | [S] RET §2b (0 of 55 winners used a full-width strip) |
| Playbook §2 + checklist 10; cloud-short description + §5; ESS §1.3; B-roll Guide §3, §6; SOURCING.md | "Evidence cards for any fact line", `card.py --len 2.4`, "graphics make strong evidence cards" → **proof on the footage** (overlay words, scorebug circle); card only as last resort, 1.5 s | [V] WHY §2 (any card 66.1% vs none 72.6%); owner |
| Playbook §2; cloud-short; daily-run; ESS §1.9; Soccer Playbook 12; QA.md | (new) → **no emoji stickers** | [S] RET §2b |
| Playbook §2 + §5 Ending; cloud-short rule 6, Round 5, STORY STANDARD, §2; nba-short step 6; THE 42 FORMAT §2; B-roll Guide rule 4; Soccer Playbook table | "Last shot reuses the first clip (loop)", "last line echoes the first" → **no forced loop**: end on the payoff | [S] RET §1b; loops aren't engaged views [V YouTube] |
| Playbook §5 QA list | Oct 14 FAIL list ("fewer than 6 sources", "one clip 35%+") → current gates as of Oct 26, with `qa_short.py` as the source of truth | [V] Rules Review §5 O |

## 2. NBA lanes
| File, section | Old rule → new rule | Tier (source) |
|---|---|---|
| Playbook RULE 1 → THE RULES §1; START HERE notes; THE 42 FORMAT title + §3; daily-run C; cloud-short lanes; CLOUD STATE House rules | "Lead with THE #42 FORMAT" / "2 of every 3 moments" / "1 in 3 per lane" → **moments about half**; the other half rotates **star paradox (#42, one lane)**, **same-day news**, **weekly countdown test** ("3 times [star] did X", #3/#2/#1 corner badge via overlay.py `"x"`/`"box"`); review after 10 moment posts | [V] #42 test 1 of 3 (Rules Review §2.1); [S] SIM §4; countdown [H] |
| Playbook §1; cloud-short lanes; daily-run C | (new) → **each moment needs one fact the clip can't show**; league/team/broadcast footage, never another creator's edit as the base | [V official] Shorts Mechanics and Policy finding 3 |
| Playbook §1; daily-run C; US rule 2 | Same-day news only → **kept**: news goes up the morning after the game, or not at all | [S] #63 n=1; POST §1 |

## 3. Soccer
| File, section | Old rule → new rule | Tier (source) |
|---|---|---|
| story-short description + step 3 + step 4 + step 8; SCRIPT.md; QA.md; FORMAT.md; Soccer Playbook rule 1 + table; Soccer START HERE; daily-run D | "260-290 words, 60-68 s", "under 58 s add a beat", "60-80 s", QA "55-120 s, warn 58-88" → **ends under 59.5 s; about 230-250 words; cut a sentence, never add**; QA FAIL outside 50-59.9 s | [V official] claim rule; QA (Rules Review §2.5) |
| story-short step 7; Soccer Playbook rules 1, 6; Soccer START HERE; daily-run D | "a quiet music bed" as the format → **bed vs none is an open A/B test: render both, log which was posted** | [H] no data |

## 4. Posting and the package
| File, section | Old rule → new rule | Tier (source) |
|---|---|---|
| Playbook §3 + Oct 21 cadence + older Recipe; US rules 1, 3; daily-run E; Soccer Playbook 7 | "2 a day (late morning + 6 PM)", "4 h between posts" → **one per channel per day**; a second NBA Short only if as strong, 6+ h later; never 3 | [S] POST §1d |
| Playbook §3; US table; daily-run E; Soccer Playbook 7; Soccer START HERE | NBA 11 AM / FC 12 PM (2 min apart on Oct 25-26) → **same slots, at least 1 h apart** (FC 12:30 PM+ if NBA is 11:30) | [S] POST answers 1, 3 (1 h gap [H]) |
| Playbook §3 + workflow 10 + §9; cloud-short §2 checks; US rule 4; Soccer Playbook 13 | Read at 24/48 h, "target 70%+" → **judge at 72 h; target 74%+** | [V] POST §1g; WHY §1 |
| Playbook §3; US rule 5; cloud-short; Soccer Playbook 13 | (new) → **never re-upload** a Short | [V] YouTube (POST §3) |
| cloud-short §7; daily-run D; Playbook checklist 13; story-short step 9; Soccer Playbook 13; US "How to post" | "25-30 tags, 440-490 chars", `tags_fit.py` to 490, "about 12 tags" → **tags optional: 3-8, ~100-150 chars** (`tags_fit.py --cap 150`); never fill 500 | [V] YouTube Help; POST answer 4 |
| same files | "up to 3 hashtags" / "no hashtags" → **none or one** (#nba / #football); **description empty** | [S] POST answer 6; [V] POST §1f |
| cloud-short §0 + §7; nba-short steps 1, 7; Playbook §3 + older Title; START HERE `/titles` row; daily-run D | "4-7 words, Why/How/What opener, one emoji", title_patterns.md scoring → **short statement pointing at the moment; title wording is a small factor; no title scoring** | [V] SIM §1 (25,000 Shorts) |
| nba-short step 10; START HERE older notes | "post between 6 and 11 AM ET" → the slot in `UPLOAD SCHEDULE.md` | [S] POST answer 1 |

## 5. Critic, QA and research tools
| File, section | Old rule → new rule | Tier (source) |
|---|---|---|
| Playbook Winning Formula + workflow 4 + THE RULES §4; START HERE table; cloud-short rule 7 + STORY STANDARD; daily-run D; THE 42 FORMAT §4; ESS §6 | "Script Critic v3 must APPROVE before footage or voice", scorecard gates → **advice, not a gate; only factual-accuracy checks block** | [S] Rules Review §2.14 |
| Playbook THE RULES §5; cloud-short §1; nba-short step 2; daily-run C; story-short step 1; Soccer Playbook 14; START HERE; US "only you can do"; Soccer START HERE | (new) → **`Tools/yt_watch.py`** (Gemini watcher; needs a free `GEMINI_API_KEY` in the environment) and **`Research Notes/Competitor Watchlist.csv`** | — (tools) |
| CLOUD STATE, "House rules" section only | The Oct 3 summary (6+ clips, 3+ cuts, loop, question ending, 440-490 tags) → a pointer plus a short summary of the new rules | all of the above |

## Not changed here (for the session that owns them)
- **`Tools/`** (not edited): `qa_short.py` still FAILs soccer on "6+ clips / 35% per clip" and its docstring (L8-14) still lists the old gates; `tags_fit.py` defaults to 490 (docs now say `--cap 150`); no QA check yet for "4+ shots before 5 s" or "shot 1 under 2 s".
- **CLOUD STATE line 3** still says "Lead with THE #42 FORMAT". Only the House rules section was in scope; it now says it replaces that note.
- **`.claude/skills/titles/SKILL.md`** and `Tools/data/title_patterns.md` still score titles out of 5. They were outside this edit list.
- **Rules Review proposals the main session didn't decide** were left as they were: pace targets, sound-effect counts, the music pages (`Sound Library.md`, `Music Guide.md`), NBA length windows, the F voice twin, "Back in [year]" as the soccer opener, and the soccer shot rate.
