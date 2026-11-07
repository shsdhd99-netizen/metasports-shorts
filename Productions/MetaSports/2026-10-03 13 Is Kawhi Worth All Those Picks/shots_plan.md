# Shot plan: 2026-10-03 13 Is Kawhi Worth All Those Picks

Footage rows (V) need cutting on the PC (YouTube blocks downloads from the cloud). Card rows (C) are already built in `clips/`.

Cut each V clip as `clips/<name>`, 1080x1920 (`Tools/broll.py sheet` to find the moment, then `broll.py cut ... --snap`), the length shown. Then run `python Tools/assemble.py --folder <this folder>` (add `--caption-style metasports` for the ALL CAPS look). `shots.json` and `sfx.json` are already written for it.

| # | Start | Length | Clip file | What must be on screen | Where to find it |
|---|---|---|---|---|---|
| 1 | 0.00 | 2.3s | `V01_kawhi_clippers_game.mp4` | Kawhi Leonard in a Clippers jersey, a game or a dunk. First frame moving. | YouTube: NBA / Clippers Kawhi highlights |
| 2 | 2.33 | 1.9s | `V02_kawhi_raptors_media_day.mp4` | Kawhi in a Raptors jersey or at the Sept 28 media day: 'Kawhi + Scottie' post. | Raptors / NBA YouTube Sept 28 |
| 3 | 4.21 | 2.2s | `V03_kawhi_2019_title.mp4` | Kawhi with the 2019 Finals trophy / the Raptors celebrating. | NBA YouTube 2019 Finals |
| 4 | 6.41 | 1.2s | `V04_kawhi_clippers_intro.mp4` | Kawhi's Clippers introduction in 2019 (leaves Toronto). | Clippers / NBA YouTube 2019 free agency |
| 5 | 7.65 | 2.9s | `c13_c_1.mp4` | **CARD (done)** Hoops Rumors card: Raptors get Leonard; Clippers get Ingram, Dick, 2031 and 2033 firsts, seconds, 2027 swap, boxed. | built in the cloud |
| 6 | 10.58 | 2.2s | `V05_ingram_dick_raptors.mp4` | Brandon Ingram and Gradey Dick in Raptors jerseys, 1 s each (the pieces going to LA). | NBA / Raptors highlights |
| 7 | 12.78 | 0.9s | `V06_clippers_intuit_dome.mp4` | Intuit Dome exterior or Clippers court wide shot for 'But here's the twist'. | Clippers YouTube |
| 8 | 13.64 | 2.5s | `c13_b_1.mp4` | **CARD (done)** ESPN card: Clippers forfeit picks 2029 to 2033, and the 'total of 10 first-rounders' line, both boxed. | built in the cloud |
| 9 | 16.12 | 2.2s | `c13_a_1.mp4` | **CARD (done)** ESPN card: '$30 million fine and suspension for owner Steve Ballmer', boxed. | built in the cloud |
| 10 | 18.36 | 1.0s | `V07_ballmer_courtside.mp4` | Steve Ballmer courtside at a Clippers game, 1 s on his name (verify it is Ballmer). | NBA / Clippers YouTube |
| 11 | 19.39 | 1.1s | `V08_kawhi_clippers_laugh.mp4` | Kawhi in Clippers colours, low-key (the 'over how they paid Kawhi' beat). | Clippers highlights |
| 12 | 20.46 | 0.9s | `V09_kawhi_age_media_day.mp4` | Kawhi at the Raptors media day podium (35 years old). | Raptors YouTube Sept 28 |
| 13 | 21.39 | 1.4s | `V10_larry_obrien_trophy.mp4` | The Larry O'Brien trophy for 'buying a championship'. | NBA YouTube |
| 14 | 22.79 | 1.2s | `V11_kawhi_2019_loop.mp4` | Kawhi 2019 Finals shot (the Game 7 bounce or a Finals dunk), for 'paying for 2019'. Last frame can match the first for a loop. | NBA 2019 Finals |
