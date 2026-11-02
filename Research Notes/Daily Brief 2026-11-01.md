# Daily brief, Sun Nov 1 2026 (YouTube Analytics API pulls, both channels)

Source: `Tools/yt_analytics.py daily`, raw CSVs in `Research Notes/Studio exports/api/` and `api FC/` (retention curves included). "Engaged ratio" stands in for Studio's "stayed to watch" (not available by API).

## Today's uploads (all scheduled via yt_schedule, mode B)
| Channel | Short | Public (ET) | Link |
|---|---|---|---|
| NBA | #82 Wemby blocked a three, point 40 (v2) | 1:00 PM | https://youtube.com/shorts/bW9XjIjY4Gg (live, 27 views at 1:05 PM) |
| FC | S19 Man United's penalty nightmare | 2:00 PM | https://youtube.com/shorts/BOsvemp6eTE |
| NBA | #84 LeBron is 40 assists behind Kidd | 6:30 PM | https://youtube.com/shorts/Viv9BG01pt0 |
| NBA | #83 Flagg vs LeBron rookie year | Mon 3:30 PM | https://youtube.com/shorts/ypyY6KpZ7is |
Pin the comment on each once live (the API can't): #82 "Block, sprint, dunk: point 40 in five seconds. Is Wemby already the best two-way player in the league?"; S19 "Best goalkeeper in a shootout right now?"; #84 "Is LeBron the best passing forward ever?"; #83 "Better rookie year: Flagg or LeBron?".

## NBA (47 uploads in the window)
- Top: #42 "Who Has Missed The Most Shots" 25.6K (16 d), "This Kid Felt Every Free Throw" 23.9K (4 d, still climbing), "Most Threes Missed" 23.9K, "The Lakers Just Saved Bronny" 23.7K (19 subs: the best subscriber converter in the top group), "How Tall Is Cooper Flagg Really" 22.0K.
- Flagg Shorts keep working (22.0K height, 10.5K bags): supports #83.
- Flagged by engaged ratio under 0.5 (likely under 60% stayed): Lost The Most Games 0.49, Chuck test 0.46, Kawhi picks 0.44, Bad Boys Pistons 0.47, Luka/Kobe 0.49, big men underhand 0.47. All of these also fail the gauge's flop shapes (rules, record numbers, hypotheticals): consistent with the idea-gauge note.
- Newly posted and too young to judge: Boozer 0, Bronny 100% 0 (age 2 d, API lags), #74 free throws.

## FC (13 uploads)
- The three goalkeeper hits: water bottle 28.5K (96.5% viewed), sock 28.2K (**86 subscribers**, 92.9% viewed), danced 15.5K (82.9%, best engaged ratio 0.608). Everything else 1-3K, with lower average viewed (63-80%).
- All three hits are flagged "sharp early drop at 2-3% of runtime" (about the first 1.5 s: the title line spoken as line 1). They still hold 83-97% average viewed, so the dip is not fatal, but it is the cheapest thing to test: open S19-type Shorts on the action sentence instead of the plural title line? [H, not tested; needs the retention CSV and an A/B on the next two goalkeeper Shorts].
- The sock Short alone brought 86 of the channel's ~130 subscribers: goalkeeper stories convert subscribers, not just views.

## Research done today (all committed)
Soccer Topic Study, Soccer Script Craft, FC Playbook v2, Editing Study + `Tools/edit_lint.py`, Idea Gauging + `Tools/idea_gauge.py`, Third Channel Feasibility (recommendation: not now), Rodman/music scoring, tool fixes, Jokic prebuild, Milestones, Footage Sources, Competitors 2026-11-01, GTA 6 plan.

## Open items for the owner
1. Pin the four comments above as each goes live.
2. Run `python Tools/yt_auth.py` again only if a scheduled upload ever errors (tokens are saved for both channels).
3. Decide: third channel (research says no), GTA plan, and approving voicing of the Jokic script near the record night.
4. ElevenLabs reset date conflict in the repo (Nov 8 vs Nov 19): check your account page; about 80K characters remain.
