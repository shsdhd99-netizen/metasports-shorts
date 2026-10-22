# S01 Goalkeepers who hid a cheat sheet in their sock (DRAFT, awaiting approval)

- **Format:** the story format from `Research Notes/Story Format Study - Ahmed (Oct 21, 2026).md`: title read as line 1, "Back in 2006", a turn every 8-12 s, payoff on a hard number and irony. No teaser (owner, Oct 22: the promo was cut).
- **Lane / theme:** records and oddities ("looks fake but is 100% real", Ahmed's Goal median 332K) plus a famous name. Ahmed's "cheating" titles are one of his strongest series (1.5M for "Teams that got caught cheating").
- **Concept (8 words):** Lehmann's sock note won a shootout, then sold for €1M.
- **Added value:** the twist most retellings skip: only two of the seven names actually took a kick, and the decisive taker (Cambiasso) was not on the list at all; the €1M sale for a hotel notepad page.
- **Copy-check, Oct 21:**
  - `copy_check.py "Lehmann penalty cheat sheet sock"`: FRESH.
  - Ahmed's Goal titles have "The cheating goalkeeper" (15K). The story behind it is unknown, and its title is different from ours.
- **Runtime:** 59.5 s after the Oct 22 re-edit (promo cut, pauses tightened; was 66.1 s). 253 words. Voice: Alex, take 2 (passed the check).

## Script lines -> sources
| Line | Source and exact wording |
|---|---|
| Germany hosted, quarterfinal vs Argentina in Berlin, 1-1 after 120 minutes, penalties | FIFA.com, "Lehmann's cheat sheet decrypts Argentina": "the Olympiastadion in Berlin on 30 June 2006 ... quarter-finals ... ended all square after 120 minutes". Wikipedia (2006 FIFA World Cup knockout stage): 1-1 a.e.t., Ayala 49', Klose 80'. The broadcast graphic in A06 shows the same. |
| His goalkeeping coach, Andreas Köpke, had studied where Argentina's players liked to shoot, and the tips ended up on a tiny page from the team hotel's notepad | FIFA.com: "It was he [Köpke] who, together with Dutch coach Huub Stevens, had sifted through a database of 13,000 previous penalty kicks to compile a series of tips for Lehmann, which became the now-iconic scrap of notebook paper bearing the letterhead of the Schlosshotel in Berlin." **Sources disagree on who physically wrote it.** Football Shirt Culture / Reuters (Dec 2006) says Köpke wrote it. FIFA quotes Lehmann: "I wrote down the names of the Argentinian players that same day, in the morning." So the script says Köpke *studied* and the tips *ended up* on the page, which is true under both versions. |
| Riquelme, left high. Heinze, left low. Even Messi was on it. | Football Shirt Culture (Reuters, Dec 18 2006) lists the note: Riquelme left high, Crespo, Heinze left low, Ayala, Messi left, Aimar, Rodríguez left. FIFA.com lists "Riquelme, Hernan Crespo, Gabriel Heinze, Ayala, Pablo Aimar and Maxi Rodriguez" as the names. |
| Tucked it into his sock, pulled it out before Argentina's kicks | Wikipedia (2006 knockout stage): a note in his sock. FIFA.com: "The notes that Lehmann consulted before every La Albiceleste spot-kick he faced". The Guardian (Oct 4 2006): "a crumpled note ... that he stuffed in his sock". |
| Only two of the players on his list took a penalty. He saved Ayala's, nearly saved Maxi Rodríguez's | FIFA.com: "of the seven players whose names had been scribbled in pencil ... only two actually took kicks. Jens ... saved Ayala's effort. He went the right way for Rodriguez's too, but it was so well hit that it found the net anyway." |
| Cambiasso's name was nowhere on that paper. He read it, nodded, put it away. Cambiasso shot, Lehmann saved it. | FIFA.com quote: "Lehmann couldn't find anything in his notes indicating where Cambiasso might put his kick ... the piece of paper played a part because Lehmann took his time and then stared at him, nodding his head as if he knew what to do." Wikipedia: Cambiasso not on the list; Lehmann pretended to read it. |
| Germany won 4-2 | BBC, Jun 30 2006, and the broadcast graphic in A33/A35: "GERMANY WINS 4-2 ON PENALTY SHOOT OUT". |
| After the game, Lehmann found the note on the dressing room floor, next to his socks | Football Shirt Culture (Reuters): Lehmann "saw it lying on the locker room floor next to my socks". |
| Months later, the boss of a German energy company bought it for one million euros, at a charity auction for children | FIFA.com: "auctioned off on famous charity television programme Ein Herz für Kinder (A Heart for Children) and bought for €1 million by Utz Claassen, the CEO of Germany energy giant EnBW." Reuters, Dec 16 2006: "raised one million euros ($1.3 million) for charity on Saturday". |
| (not said, background) it is now in the Haus der Geschichte museum in Bonn | FIFA.com: "In 2007 the businessman donated it to the museum". |

## Footage (every clip is in sources.csv with what it shows; I checked every shot on _check/sheet.jpg)
- **The shootout:** archive.org item `10d1824885631149e2a78e7348260b234e58cf54.mp4` (lbry mirror of the Argentine TV broadcast). The section 5350-6450 s was re-encoded to `src/clean.mp4`: black borders cropped, square pixels, the "vivo" channel logo blurred.
  - A01 / A17 / A28: Lehmann bends to his sock by the board between Maxi Rodríguez's kick and Borowski's. This is the real "note" moment the broadcast caught. A28 is used on "So Lehmann pulled it out anyway" (before Cambiasso). It is the same habit but an earlier kick; the broadcast did not show the pre-Cambiasso look.
- **Riquelme (A14) and Messi (A16):** archive.org `fifa-world-cup-germany-2006-all-goals`. Riquelme (#10) takes the corner in this quarterfinal. Messi (#19) is from Argentina 6-0 Serbia and Montenegro. The uploader's "RPTIMAD" watermark is cropped out.
- **Köpke (A10):** Wikimedia Commons, Julia Engel, CC BY-SA 4.0 (2018). The credit is on screen.
- **The note (A13, A19, A27, A42) is a RECREATION:** made by `assets/make_note.py`, with "recreation" printed on the page. It only shows names from the sources above, not the real handwriting.
- **Stock:** Mixkit Free License (hotel room, locker corridor, socks, power lines, euros, children, fireworks).
- **Teaser shots A43-A46:** removed Oct 22 with the promo line.

## Warnings for the owner
- **Copyright:** this is broadcast match footage (World Cup 2006, Premier League 2011) taken from archive.org mirrors. Ahmed's channels use the same kind of clips, but a claim or a block on some territories is possible. If a claim lands, we swap the clips; nothing else in the Short depends on them.
- **Picture quality:** the archive footage is 576p/368p, so it is soft at 1080x1920. Ahmed accepts this too.
- **Two versions:** with the music bed (what Ahmed does) and without. See UPLOAD.md.
