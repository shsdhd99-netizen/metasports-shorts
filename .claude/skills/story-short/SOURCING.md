# Where the pictures come from (cloud-tested Oct 21, 2026)

| Need | Source | How |
|---|---|---|
| Old matches (full TV broadcasts, highlights) | archive.org | Search: `curl -s "https://archive.org/advancedsearch.php?q=title:(lehmann+argentina)&fl[]=identifier&rows=50&output=json"`. Files: `curl -s https://archive.org/metadata/<id>`. Pull one section without the whole file: `ffmpeg -ss <s> -i "https://archive.org/download/<id>/<file>" -t <len> -c copy part.mp4` |
| Every 2006 World Cup goal (player names on screen) | archive.org `fifa-world-cup-germany-2006-all-goals` (1280x720) | Scan it with remote frame grabs every 15 s (see S01) |
| Premier League 2011 | archive.org BBC Match of the Day items (640x368) | Its graphics (line-ups, "RECORD-BREAKING GAME") are proof on the footage: show them as broadcast shots, not as cards (Oct 26 overnight review: no cards) |
| Recent clips | X posts from official accounts | `python Tools/x_clip.py <links> --out src` |
| Abstract lines (fire, cash, hotel, clock, socks, police) | Mixkit (Mixkit Free License: commercial use including monetised YouTube, no attribution) | `python Tools/stock.py search <word> --sheet s.jpg`, then `python Tools/stock.py get <id> --out src/stock_<id>.mp4`. Run searches one at a time; parallel ones came back empty. Or give `cut_list.py` a `"stock": <id>` shot |
| Headlines, club pages | The article itself | For checking facts. A card only when nothing else can show the proof: 1.5 s at most, never in the first 4 s (owner, Oct 26). `node Tools/webshot.mjs --url <url> --text "<headline words>" --mark "<line>" --out x.png`, then compose a 9:16 card above y=890 (example: S02 `assets/make_cards.py`) |
| Photos of people (no footage) | Wikimedia Commons (CC licences) | The API and upload.wikimedia.org rate-limit cloud IPs (429). The page HTML works: `curl en.wikipedia.org/wiki/<Name>`, then the image on `https://thumb.wikimedia.org/wikipedia/commons/thumb/...`. Put the credit on screen ("Photo: <author> / Wikimedia Commons, CC BY-SA 4.0") |
| A famous object with no photo | A recreation | PIL graphic labelled "recreation" on the picture (S01 `assets/make_note.py`) |
| Music bed | `Library/Music/eleven_story_01.mp3` (ElevenLabs Music, 75 s, steady) | Make a new one: `python Tools/music_gen.py --prompt "..." --mood stats --seconds 75 --out Library/Music/<name>.mp3` |

## Clean-up rules
- **TV channel logos:** blur them (`--delogo x,y,w,h` on `broll.py cut`, or one clean re-encode with `crop` + `delogo`).
- **Uploader watermarks or name strips:** crop them out. A blur over text looks worse than the text.
- **Black side bars on 4:3 broadcasts:** crop them out (`cropdetect`) before cutting.
- **4:3 broadcasts** have a 16:15 pixel aspect. Scale to square pixels (768x576) in the clean re-encode.
- **Footage you can't confirm:** a shot that only illustrates (a yellow card from the same match that isn't the booking named in the script) is marked "illustrative" in sources.csv and notes.md.

## Licences and risk
- **Broadcast match footage** belongs to its broadcaster or rights holder. Ahmed's channels use it in commentary-style stories; claims or territory blocks are possible.
  - Use short excerpts, each with our narration over it, and never the original commentary audio. A play may run 3-5 s (Oct 26 overnight review).
  - Note the risk in notes.md. If a claim lands, swap the clips.
- **Mixkit:** free for YouTube, no attribution. **ElevenLabs music:** commercial use allowed on paid plans (see `Library/Music/music_library.csv`).
