# Auto queue (Sat Nov 07, 10:05 AM ET, next 7 days)

Auto-written by `python Tools/queue_rank.py` (daily, after `qa_sweep.py`). Every slot of the posting grid, filled from what we have, best first.
**Score** = the lab's prediction (50 = a typical Short for the channel; see `Research Notes/Lab/Study - all`). READY = built and passed QA; BUILD = prepped, needs voice + cut; IDEA = needs research; MOMENT = the 3:30 PM morning-after slot.

## NBA (MetaSports)

| Slot (ET) | What | Short | Score | QA | Why | Next step |
|---|---|---|---|---|---|---|
| Sat Nov 07 03:30 PM | **PINNED** | Luka Has Scored 40 In Six Of His Last Seven Games | 45 | 92 SHIP | topic_family_kid=no 0.88x; len_le25=yes 1.16x; script_line1_le11=no 0.80x | schedule (schedule_ready.py) |
| Sun Nov 08 07:15 AM | **EMPTY** | - | - | - | nothing ready, prepped or rated 80%+ | gap-fill builds the best new idea, or skip |
| Sun Nov 08 03:30 PM | **MOMENT** | last night's best moment | - | - | the 3:30 PM slot is the morning-after moment (Playbook N2) | research Sun 03:43 AM, build by Sun 12:00 PM |
| Mon Nov 09 07:15 AM | **IDEA** | List 1: who has missed the most free throws in NBA history ( | 46 | - | gauge 83% | research + build by Sun 11:15 AM |
| Tue Nov 10 07:15 AM | **IDEA** | Curry passes DeRozan (16th all-time scoring), when it happen | 46 | - | gauge 83% | research + build by Mon 11:15 AM |
| Tue Nov 10 03:30 PM | **MOMENT** | last night's best moment | - | - | the 3:30 PM slot is the morning-after moment (Playbook N2) | research Tue 03:43 AM, build by Tue 12:00 PM |
| Wed Nov 11 07:15 AM | **ON YOUTUBE** | The NBA Legend Who Made Up An Insult 😳 #nba | - | - | booked (Scheduled Uploads.csv) | nothing: goes live by itself |
| Thu Nov 12 07:15 AM | **IDEA** | LeBron passes Kidd for 3rd all-time assists, when it happens | 46 | - | gauge 83% | research + build by Wed 11:15 AM |
| Thu Nov 12 03:30 PM | **MOMENT** | last night's best moment | - | - | the 3:30 PM slot is the morning-after moment (Playbook N2) | research Thu 03:43 AM, build by Thu 12:00 PM |
| Fri Nov 13 07:15 AM | **IDEA** | Lendeborg Part 3 after a 30+ game | 46 | - | gauge 83% | research + build by Thu 11:15 AM |

## FC (MetaSports FC)

| Slot (ET) | What | Short | Score | QA | Why | Next step |
|---|---|---|---|---|---|---|
| Sun Nov 08 12:00 PM | **ON YOUTUBE** | The player who moved two Coca-Cola bottles at the Euros | - | - | booked (Scheduled Uploads.csv) | nothing: goes live by itself |
| Mon Nov 09 12:00 PM | **BUILD** | The Goalkeeper Who Beat A Team That Practised 1000 Penalties | 77 | - | topic_shootout=yes 1.97x; pkg_morning=no 1.09x | voice + cut by Sun 04:00 PM (lab.py assign fc --folder first) |
| Mon Nov 09 06:00 PM | **BUILD** | The Goalkeeper Who Found Out Chelsea's Secret Penalty Plan | 77 | - | topic_shootout=yes 1.97x; pkg_morning=no 1.09x | voice + cut by Sun 10:00 PM (lab.py assign fc --folder first) |
| Tue Nov 10 12:00 PM | **BUILD** | The Baby Messi Bathed Beat Him In A World Cup Final | 43 | - | topic_shootout=no 0.76x; pkg_morning=no 1.09x; feeds test fc-premise | voice + cut by Mon 04:00 PM (lab.py assign fc --folder first) |
| Wed Nov 11 12:00 PM | **BUILD (filler)** | The Hull City Fan Who Walked Home From Chile | 43 | - | topic_shootout=no 0.76x; pkg_morning=no 1.09x; feeds test fc-premise | voice + cut by Tue 04:00 PM (lab.py assign fc --folder first) |
| Wed Nov 11 06:00 PM | **BUILD (filler)** | The Goalkeeper Who Saved A Shot With A Scorpion Kick | 43 | - | topic_shootout=no 0.76x; pkg_morning=no 1.09x; feeds test fc-premise | voice + cut by Tue 10:00 PM (lab.py assign fc --folder first) |
| Thu Nov 12 12:00 PM | **BUILD (filler)** | The Goalkeeper Who Scored More Goals Than Most Strikers | 43 | - | topic_shootout=no 0.76x; pkg_morning=no 1.09x; feeds test fc-premise | voice + cut by Wed 04:00 PM (lab.py assign fc --folder first) |
| Fri Nov 13 12:00 PM | **BUILD (filler)** | The Goalkeeper Who Got The Penalty Rules Changed | 43 | - | topic_shootout=no 0.76x; pkg_morning=no 1.09x; feeds test fc-premise | voice + cut by Thu 04:00 PM (lab.py assign fc --folder first) |
| Fri Nov 13 06:00 PM | **EMPTY** | - | - | - | nothing ready, prepped or rated 80%+ | gap-fill builds the best new idea, or skip |

## Held (QA FAIL: fix first, never slotted)

- nba: Why You Can't Bet On The Opening Tip 😳 (score 37): FOOTAGE: no cuts.json / cuts_plan.json
- nba: Why The Lakers Kept Bronny Over Knecht 😳 (score 68): SCRIPT: notes.md has 1 source link(s); every Short needs at least 2 sources; 4 lint risks (first: sentence 3 s
- nba: Paul George Broke A Celtics Record And Lost 😳 (score 53): SCRIPT: notes.md has 0 source link(s); every Short needs at least 2 sources; line 1 has 10 words (rule: 11 or 
- nba: LeBron Just Answered A Knicks Fan 😳 (score 57): SCRIPT: notes.md has 0 source link(s); every Short needs at least 2 sources; line 1 has 17 words (rule: 11 or 
- nba: Two Buzzer-Beaters From 40 And 50 Feet (score 47): PACKAGE: title missing or a placeholder; 7 tags, 83 characters (fill to about 490 with Tools/tags_fit.py); no 

## Waiting with no slot this week

- none
