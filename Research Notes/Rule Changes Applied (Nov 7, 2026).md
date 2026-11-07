# Rule changes applied (Sat Nov 7, 2026)

Owner, Nov 7: "approve all, scrap what should be scrapped and tweak rules to properly be updated and used. refine rules to actually be useful and help you learn and make better videos instead of existing. auto run and log tests yourself with a score on them. make sure you can also do this same study for editing, etc."

- **Proposal:** `Research Notes/Theory Ranking and Rules Challenge (Nov 7, 2026).md` (R1-R15, A/B/C lists).
- **New rules:**
  - THE RULES (Nov 7) at the top of `MetaSports - Playbook.md`;
  - `Soccer Channel/Playbook.md` v3.
- **Old text, word for word:**
  - `Research Notes/Rule History - Playbook THE RULES before Nov 7 rewrite.md`;
  - `Research Notes/Rule History - Soccer Playbook before Nov 7 rewrite.md`.

## 1. The new system: the lab (`Tools/lab.py`)
**Daily (`python Tools/lab.py auto`):**
- measures every Short since the restart (84 today; 53 linked to their production folders), across topic, script, edit, package and length;
- scores the live tests;
- writes:
  - `Research Notes/Lab/Scoreboard.md`;
  - `Research Notes/Lab/Study - all (<date>).md`, with a **Rule check** that says whether the data still backs each rule.

**How tests work:**
- **Limit:** at most 3 live per channel (`Research Notes/Lab/tests.json`); the rest queue.
- **Assigning:** `lab.py assign <ch> --folder F` gives the next Short its arms and writes the card's `**Arms:**` line. `build_gate.py` prints the arms on every BUILD, and accepts a live lane test as the "one variable".
- **Detection:** arms are read from the files (the title, the script, cuts/shots, the uploaded file name), so a test can't go unlogged again.
- **Score:** the chance a B Short beats an A Short (50 = no difference).
  - It decides at 6+ per arm with p 0.2 or less.
  - At 12 per arm with no winner, it closes as NO DIFFERENCE.
  - A decided test names the rule it changes. The next run edits that rule, and the next queued test starts.
- **The metric:** views at 72 h, read 5-8 days after go-live. The API runs about 2 days behind (England subs showed 5.3K on day 3 and 12K on day 4).

**On demand:** `lab.py study --part edit|script|package|topic|length` runs the same study for any part. `next_arm.py` now calls the lab.

**Live tests (Nov 7):**

| Channel | Test | What it compares |
|---|---|---|
| NBA | `nba-lists` | record lists as a lane (currently score 82, n=3) |
| NBA | `nba-opener` | Why/How/What/Who titles vs other titles |
| NBA | `nba-cadence` | 1 vs 2 posts a day |
| FC | `fc-premise` | new non-shootout premises vs shootout Shorts |
| FC | `fc-opener` | action-first vs title-first opening |
| FC | `fc-music` | music bed vs none |

**Queued:** `nba-loop`, `nba-countup`, `nba-foreshadow`, `nba-countdown`, `fc-loop`, `fc-style-v3`.

## 2. Rules changed (R1-R15)
| # | Change | Where |
|---|---|---|
| R1 | "3+ shots in the first 3 s" deleted | daily-run skill; `precut_lint.py`; `qa_short.py` |
| R2 | One tag rule: `tags_fit.py` fills to about 490. A short list is a WARN, never a FAIL (zero tags still fails, because the scheduler needs them). | Playbook O8; `qa_portions.py` (card and live); NBA/FC build prompts; skills |
| R3 | FC slot is 12 PM ET everywhere | Soccer Playbook F6; FC build prompt |
| R4 | Up to 3 a day, 6+ h apart | Playbook P2; `UPLOAD SCHEDULE.md` |
| R5 | Pinned comment optional (a source line or "Part 2"); no debate questions | Playbook P4; `qa_portions.py`, `qa_final.py`; prompts; skills; UPLOAD SCHEDULE |
| R6 | Ending: payoff held about 2-3 s (QA warns under 1.8 s); a natural loop is a queued test | Playbook E6; `qa_short.py` |
| R7 | Title: short and searchable, a statement or Why/How/What (test `nba-opener`) | Playbook P1; UPLOAD SCHEDULE |
| R8 | "Global names only" scrapped: a famous moment beats a famous name | Soccer Playbook F1 |
| R9 | NBA music alternation dropped (no music). FC music is the auto-logged test `fc-music`. | Playbook E7; Soccer F5; NBA prompt |
| R10 | Tests go through the lab (max 3 live per channel, auto-logged, scored) | `lab.py`, `tests.json`; Test and Learn Policy; daily-run skill; `build_gate.py`; `next_arm.py` |
| R11 | Lints removed: one source over 35%, same source back-to-back, cut counts in 3/5 s | `edit_lint.py`, `precut_lint.py`, `qa_short.py` |
| R12 | NBA length: 20-25 s target; QA warns outside 18-27 s | Playbook S3; `qa_short.py` |
| R13 | FC lane renamed: a famous penalty shootout + one odd act (keeper or takers) | Soccer F1; prompts; skills |
| R14 | NBA lanes reordered: family/kid/rookie, last night's moment, lists and star chases | Playbook N2; skills |
| R15 | Stand-ins written down: FC avg % viewed 85%+; NBA is read on views until the Studio export | Playbook Q2; Soccer F6 |

**Also scrapped (C list):**
- the average-shot, 6-clip, talking-head and b-roll share guidelines (`qa_short.py`);
- the 30-35 s NBA length test;
- the caption-style A/B (parked);
- title micro-tuning;
- optimising the posting hour;
- Script Critic scores.

## 3. Where the lab overruled the proposal (same day)
- **A8 "NBA pace over 230 wpm" was NOT added.** The lab re-check, on 24 linked NBA Shorts, found the opposite direction (4.0K over 230 wpm vs 7.1K, p 0.39). No pace target; the voice_take default stays.
- **The first Rule check (Nov 7):**
  - **SUPPORTED:** line 1 at 11 words or fewer (NBA: 7.1K vs 4.0K); NBA family/kid/rookie (10.5K vs 4.7K, p 0.03); NBA 25 s or less (7.1K vs 3.0K).
  - **NOT SHOWN yet:** shot 1 at 2 s+, payoff held. Both kept as cheap house style.
  - **SCRAP STANDS:** cut counts, one-source share, question titles, pinned comment.
  - **REVISIT:** NBA posts before 10 AM ET (7.6K vs 5.0K, p 0.17). The grid already has a 7:15 AM slot; nothing to change yet, and the lab keeps watching it.

## 4. Checked after the change
- `qa_short.py`, `qa_portions.py`, `qa_final.py`, `precut_lint.py` and `edit_lint.py --selftest` all run.
- **#99 Luka:** `qa_final` SHIP. The new "payoff held" warning correctly flags its 0.8 s last shot.
- `build_gate.py fc --shape "club story"` now passes as the `fc-premise` test and prints the arms.
- `lab.py assign` writes only builder-controlled arms. Lane tests and the cadence test are detected, not planned.
