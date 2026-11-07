"""S07 cards (run from the Short's folder): python assets/make_cards.py
Stat cards via Tools/story_card.py; the betting slip (a recreation) is drawn here. Everything stays above y=890."""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "Tools")
FONTS = os.path.join(T, "..", "Soccer Channel", "Brand", "fonts")
F = lambda n, s: ImageFont.truetype(os.path.join(FONTS, n), s)


def card(out, bg, *args):
    subprocess.run([sys.executable, os.path.join(T, "story_card.py"), "--bg", bg, "--out", out, *args], check=True)


card("assets/card_escape.jpg", "assets/bg_newc.jpg", "--title", "LEICESTER CITY 2014-15", "--sub", "Premier League",
     "--row", "*Christmas Day|20th of 20", "--row", "Last 9 games|7 wins", "--row", "Final position|14th",
     "--foot", "Source: Premier League table (Wikipedia, 2014-15 Leicester City season)")
card("assets/card_odds.jpg", "assets/bg_ranieri.jpg", "--title", "TO WIN THE PREMIER LEAGUE", "--sub", "Leicester City, before the 2015-16 season",
     "--big", "5,000-1", "--foot", "Source: AP, ESPN (bookmakers' pre-season price)")
card("assets/card_elvis.jpg", "assets/bg_ranieri.jpg", "--title", "MORE LIKELY THAN LEICESTER", "--sub", "Bookmakers' odds, 2015",
     "--row", "*Elvis found alive|2,000-1", "--row", "Leicester win the league|5,000-1", "--foot", "Source: Associated Press, 30 April 2016")
card("assets/card_greece.jpg", "assets/bg_ranieri.jpg", "--title", "GREECE 0-1 FAROE ISLANDS", "--sub", "Euro 2016 qualifier, 14 November 2014",
     "--big", "Ranieri out the next day", "--foot", "Source: AFP, UEFA.com")
card("assets/card_mancity.jpg", "assets/bg_trophy.jpg", "--title", "MAN CITY 1-3 LEICESTER", "--sub", "Etihad Stadium, 6 February 2016",
     "--row", "Robert Huth|3'", "--row", "Riyad Mahrez|48'", "--row", "Robert Huth|60'", "--row", "Sergio Agüero (City)|87'",
     "--foot", "Source: Eurosport, Sports Mole match reports")
card("assets/card_bet50.jpg", "assets/bg_trophy.jpg", "--title", "ONE FAN'S BET", "--sub", "Ladbrokes, Leicester to win the league at 5,000-1",
     "--row", "Stake|£50", "--row", "*Would have paid|£250,000", "--foot", "Source: Ladbrokes, via Fox Sports and PokerNews")
card("assets/card_ladbrokes.jpg", "assets/bg_trophy.jpg", "--title", "LADBROKES", "--sub", "Bets on Leicester at 5,000-1",
     "--row", "*Bets taken|47", "--row", "Settled early|24", "--foot", "Source: Ladbrokes officials, via ESPN (May 2016)")


def blurred(path):
    b = Image.open(path).convert("RGB")
    b = b.resize((max(1080, int(b.width * 1920 / b.height)), 1920))
    x = (b.width - 1080) // 2
    return Image.eval(b.crop((x, 0, x + 1080, 1920)).filter(ImageFilter.GaussianBlur(28)), lambda v: int(v * 0.42))


# the betting slip (no photo of the real slip is reachable): a recreation, labelled on the picture
f = blurred("assets/bg_newc.jpg"); d = ImageDraw.Draw(f)
d.rounded_rectangle([140, 90, 940, 800], radius=10, fill=(246, 244, 236))
d.text((180, 125), "BETTING SLIP", font=F("Poppins-700.ttf", 52), fill=(30, 30, 30))
d.line([180, 200, 900, 200], fill=(150, 150, 150), width=3)
y = 230
for k, v in [("Selection", "Leicester City"), ("Market", "Premier League winner 2015/16"), ("Stake", "£1.00"), ("Odds", "2000/1")]:
    d.text((180, y), k, font=F("Poppins-600.ttf", 34), fill=(110, 110, 110))
    d.text((440, y), v, font=F("Poppins-600.ttf", 34) if len(v) < 22 else F("Poppins-600.ttf", 28), fill=(25, 25, 25)); y += 70
hand = ImageFont.truetype(os.path.join(T, "..", "Soccer Channel", "Productions", "2026-10-21 S01 Goalkeepers Who Hid A Cheat Sheet", "assets", "Caveat.ttf"), 120) \
    if os.path.exists(os.path.join(T, "..", "Soccer Channel", "Productions", "2026-10-21 S01 Goalkeepers Who Hid A Cheat Sheet", "assets", "Caveat.ttf")) else F("Poppins-700.ttf", 90)
d.text((200, 545), "Pigs might fly!", font=hand, fill=(200, 20, 30))
d.rounded_rectangle([140, 820, 470, 870], radius=8, fill=(229, 28, 36))
d.text((158, 826), "RECREATION", font=F("Poppins-700.ttf", 32), fill=(255, 255, 255))
f.save("assets/slip_recreation.jpg", quality=92)

print("cards done")
