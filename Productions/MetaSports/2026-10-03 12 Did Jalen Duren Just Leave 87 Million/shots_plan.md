# Shot plan: 2026-10-03 12 Did Jalen Duren Just Leave 87 Million

Footage rows (V) need cutting on the PC (YouTube blocks downloads from the cloud). Card rows (C) are already built in `clips/`.

Cut each V clip as `clips/<name>`, 1080x1920 (`Tools/broll.py sheet` to find the moment, then `broll.py cut ... --snap`), the length shown. Then run `python Tools/assemble.py --folder <this folder>` (add `--caption-style metasports` for the ALL CAPS look). `shots.json` and `sfx.json` are already written for it.

| # | Start | Length | Clip file | What must be on screen | Where to find it |
|---|---|---|---|---|---|
| 1 | 0.00 | 2.5s | `V01_duren_pistons_dunk.mp4` | Jalen Duren (Pistons #0, home blue or white) finishing a dunk, from 2025-26 highlights. First frame already moving. | YouTube: NBA / Detroit Pistons Duren highlights |
| 2 | 2.46 | 2.0s | `c12_c_1.mp4` | **CARD (done)** ClickOnDetroit card: 'A reported weight clause...' boxed. | built in the cloud |
| 3 | 4.47 | 1.8s | `V02_pistons_front_office_langdon.mp4` | Trajan Langdon at Pistons media day (Sept 28) or any Pistons front-office shot. | Detroit Pistons / NBA YouTube media day |
| 4 | 6.28 | 2.0s | `c12_a_1.mp4` | **CARD (done)** ClickOnDetroit card: five-year, $200 million fully guaranteed, boxed. | built in the cloud |
| 5 | 8.23 | 1.7s | `V03_duren_close_up.mp4` | Duren close-up, smiling or on the bench (the player 'wanting the max'). | Pistons highlights |
| 6 | 9.92 | 1.5s | `c12_b_1.mp4` | **CARD (done)** ClickOnDetroit card: 'Duren sought a five-year, $287 million maximum contract... $87 million lower', boxed. | built in the cloud |
| 7 | 11.39 | 2.2s | `V04_empty_pistons_media_day.mp4` | Pistons media day with Duren absent (podium, teammates), 2 s. | Pistons YouTube media day Sept 28 |
| 8 | 13.61 | 1.4s | `V05_shams_deadline_graphic.mp4` | Any clip of the deadline/Shams report (ESPN NBA Today on Oct 1 where Shams lays out the 3 options) for 'midnight Thursday'. | ESPN / NBA Today YouTube Oct 1 |
| 9 | 15.03 | 2.2s | `c12_c_2.mp4` | **CARD (done)** ClickOnDetroit card: weight-clause line (this is the line spoken here; same card as the 2.46 flash). | built in the cloud |
| 10 | 17.26 | 1.4s | `V06_duren_walking_off.mp4` | Duren trudging off the court after a loss or a frown. | Pistons 2026 playoffs highlights |
| 11 | 18.70 | 2.6s | `V07_duren_playoff_action.mp4` | Duren in a 2026 playoff game for 2.5 s (quiet series). | NBA playoffs highlights, Pistons first-round series |
| 12 | 21.29 | 1.4s | `V08_pistons_one_seed_graphic.mp4` | Pistons as the No. 1 seed (standings graphic or banner). | NBA YouTube |
| 13 | 22.68 | 1.5s | `c12_a_2.mp4` | **CARD (done)** ClickOnDetroit card again, with the box on '$200 million', for 'he signed the two hundred million'. | built in the cloud (reused card, the line matches) |
| 14 | 24.17 | 2.0s | `V09_duren_all_nba_highlight.mp4` | Duren All-Star / All-NBA highlight: block or poster dunk. | Duren 2025-26 highlights |
| 15 | 26.14 | 1.9s | `c12_b_2.mp4` | **CARD (done)** The $287M-vs-$87M-lower card again for 'eighty-seven million left on the table'. | built in the cloud (reused card) |
| 16 | 28.02 | 1.3s | `V10_duren_shrug.mp4` | Duren looking at the camera or shrugging, 1.2 s. End here (the closing question needs a face). | Pistons media / highlights |
