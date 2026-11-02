# A2 Ronaldo moved the Coca-Cola bottles (from S09 / Idea Bank S10) - account 2, Oct 31 2026
Status: VOICE-READY (not voiced, not built). Voice credits were sufficient; stopped because the footage test fails for the Hungary beat and there is too little press-conference footage for 40+ shots (see Footage).
Title / line 1 (9 words): Ronaldo moved two Coca-Cola bottles, and billions disappeared.
Lane: global star + concrete object + "versus their sponsor". Concept: Ronaldo's bottle moment "cost" Coke billions; the evidence says no sign it did.
Added value: the stock was already falling before the press conference started, and the tournament's own statement; the viral clip shows neither.
Copy check: `Tools/copy_check.py` not run this session. Ahmed CSV grep for coca/cola: no hit (per the S09 notes). Gemini pre-check: skipped, GEMINI_API_KEY not set.
Re-checked Oct 31 2026 by reading the sources themselves (Snopes by curl, SI and Al Jazeera by fetch, ESPN API).

## Claims table (script line, source, exact words)
| Script line | Source | Exact words |
|---|---|---|
| Press conference in Budapest, day before Portugal's Euro opener | SI, Jun 16 2021, https://www.si.com/soccer/2021/06/16/coca-cola-shares-drop-four-billion-cristiano-ronaldo-snub | "on Monday in Budapest a day before Portugal's Euro 2020 opener against Hungary". SI gives no exact date (Monday = Jun 14, inferred). Match date Jun 15 2021: ESPN API summary event 560334, header date 2021-06-15T16:00Z |
| Two Coke bottles, moved out of view, water, "Agua" | Snopes, Jun 18 2021, https://www.snopes.com/fact-check/ronaldo-snub-cost-coke-billions/ | "he took the two Coca-Cola bottles that were left out for him, moved them out of frame to the side of the table, then held up a bottle of water and said, "Agua."" |
| Coca-Cola an official sponsor | SI | "Coca-Cola is an official sponsor of the European Championship" (Guardian excerpt in Snopes: "Coca-Cola is one of the official sponsors of Euro 2020") |
| Headlines said four billion wiped off | Snopes | "The exact cost of the snub varied from outlet to outlet, but the general claim was that it cost Coca-Cola between $4 and $5 billion." |
| The Guardian reported 242bn to 238bn | Guardian excerpt quoted in Snopes | "The market value of Coca-Cola went from $242bn to $238bn - a drop of $4bn." The Guardian URL itself 404s, so the script says "The Guardian reported" and never states it as our own fact |
| Stock already falling before he sat down; no sign he caused any of it | Snopes | "there was no indication that this drop was entirely (or even in part) caused by Ronaldo's preference for water. In fact, Coca-Cola's stock was already falling by the time that Ronaldo snubbed Coke products in favor of water." Also "closed on Friday, June 11, at $56.16. At 9:30 a.m. shortly after the market opened again on Monday, the company's stock had fallen to $55.35. Ronaldo's news conference hadn't even started by this time." Rating: Mixture |
| Spokesperson: drink preferences; water, Coke, Coke Zero | SI (attributes to "a Euro 2020 spokesperson") | "is entitled to their drink preferences" and "Players are offered water, alongside Coca-Cola and Coca-Cola Zero Sugar, on arrival at our press conferences." FIXED: the old script said Coca-Cola said it; the source says the tournament spokesperson did |
| Next day Portugal 3-0 Hungary, Ronaldo twice in the last minutes | ESPN API https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.euro/summary?event=560334 (keyEvents) | "84' Goal! Hungary 0, Portugal 1. Raphael Guerreiro"; "87' Penalty - Scored Goal! Hungary 0, Portugal 2. Cristiano Ronaldo"; "90'+2' Goal! Hungary 0, Portugal 3. Cristiano Ronaldo". Al Jazeera: Portugal 3-0 Hungary. "In the last minutes" is true for 87' and 90+2' |
| Euros all-time top scorer | Al Jazeera https://www.aljazeera.com/sports/2021/6/16/ronaldo-breaks-euro-record-as-portugal-cruise-past-hungary | "sole possession of the record he previously shared with France's Michel Platini on nine" (11 goals) |
| Last line: the stock fell, no sign Ronaldo was the reason | Snopes | "While Coca-Cola's stock truly fell after this news conference, there was no indication that this drop was entirely (or even in part) caused by Ronaldo's preference for water." The old last line "nobody has proved he cost Coca-Cola a cent" was DROPPED: stronger than the source |

Conflicts: the Guardian's share prices ($56.10 to $55.22) differ from Snopes' own ($56.16 Friday close, $55.35 at 9:30). The script uses no share-price figures, only the Guardian-attributed market-value line, so it is true under both.

## Footage (footage test)
Found, in src/ (git-ignored):
- `src/footballwtf.mp4` (23 s, 720x720; archive.org item twitter-1404779519005835269, an archive of FootballWTF247's post). Bottles on the table 0-6 s, moved 8-12 s, water held up about 16.4 s. Small GOAL logo top right: crop with zoom 1.3. Best clip for frame 1 and the 0.5x replay.
- `src/guardian.mp4` (24.7 s, 720x720; archive.org item twitter-1404726298237411331, Guardian Sport post). Guardian watermark and a caption at 0-1 s, burned subtitles at 17-19 s: use 3-15 s zoomed, never frame 1. News footage, so a claim is possible; swap if one lands.
- Money line: words over the press-conference picture ("$242bn -> $238bn (Guardian)"), no card needed.
Dropped (not usable): BBC Breakfast and Sportsday Jun 15-16 2021 on archive.org (access-restricted, 401); a Russell Brand video on archive.org (third-party commentary); ESPN event 560334 has no videos; ABC News X clip (720x405 band inside a vertical post).
**Missing, so not built:** no free plain-file footage of Portugal 3-0 Hungary or Ronaldo's goals, and only about 48 s of press-conference footage for a 55 s Short of 40+ shots (it would repeat). archive.org has a fan upload of Portugal v France at Euro 2020 (item portugalvsfrancia2021, 1376x776, Ronaldo penalties): a different match, illustrative only and must be flagged; scanning it remotely took 2.7 min per sheet.
Options for the main account: (a) illustrative Ronaldo goals from the France match, flagged in sources.csv; (b) a UEFA/ESPN clip if one appears; (c) Mixkit stock (stock chart, soda, water bottle, phone scrolling) for the money beats plus one scoreline card of 1.5 s at most for Hungary, never in the first 4 s.
Cut plan: `cuts_plan.json` (plan only, not run through cut_list.py).
