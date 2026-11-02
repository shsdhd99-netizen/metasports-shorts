"""Soccer Topic Study (Nov 1, 2026): which topics, title shapes and lengths outperform on soccer story/facts Shorts.

Input: raw/<channel>_shorts.tsv (id, views, duration[NA], title; newest first, from the channel's Shorts tab via
yt-dlp --flat-playlist) and raw/<channel>_uploads.tsv (id, views, duration, approx upload date, title; the
uploads playlist, which YouTube cuts at 100-200 entries for some channels, so duration/date cover the newest only).

Metrics per Short:
  ratio = views / median views of that channel's Shorts (the owner's measure; controls for channel size)
  rel   = views / median of the ~100 Shorts posted around it on the same channel (also controls for era)
  top10 = the Short is in its channel's top 10% by rel
Shorts posted in the last 7 days (or the newest 5 when the date is unknown) are left out: they haven't settled.
Non-English titles (FOOTY FACTS and Footballfacts update used to post in Indonesian) are left out.

Run: python3 -I analyze.py   (writes classified.tsv and results.txt next to this file)
"""
import csv, os, re, statistics as st, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
CUTOFF = "20261025"  # leave out Shorts posted Oct 25 or later (under 7 days live on Nov 1)

STORY = ["AhmedsGoal", "FootyFacts", "FootballfactsUpdate", "Offsideman", "411Football",
         "FootballStoriesEN", "FootballUntoldStory", "PedTalksFutbol"]
ANALYSIS = ["TheAthleticFC_Tifo", "StatmanDave"]  # presenter/stat explainers: reported separately

def W(*words):  # word-boundary alternation, case-insensitive
    return re.compile(r"(?<![a-z0-9])(" + "|".join(words) + r")(?![a-z0-9])", re.I)

KEEPERS = ["goalkeepers?", "keepers?", "goalies?", "gk", "buffon", "neuer", "casillas", "kahn", "higuita", "chilavert",
           "ceni", "courtois", "alisson", "ederson", "de gea", "dibu", "emi martinez", "emiliano martinez", "onana",
           "pickford", "lehmann", "dudek", "grobbelaar", "schmeichel", "yashin", "cech", "čech", "van der sar", "krul",
           "ter stegen", "donnarumma", "oblak", "bounou", "rulli", "kepa", "trautmann", "banks", "zoff", "campos",
           "penalty saves?", "clean sheets?", "saved? a penalty", "saves"]
MEGA = ["neymar", "mbapp[eé]", "haaland", "zlatan", "ibrahimovi[cć]", "maradona", "pel[eé]", "zidane", "beckham",
        "yamal", "salah", "harry kane", "kane", "lewandowski", "ronaldinho", "benzema", "modri[cć]", "kak[aá]",
        "thierry henry", "henry", "rooney", "bellingham", "vin[ií]cius", "vini jr", "de bruyne", "su[aá]rez", "ramos",
        "iniesta", "xavi", "cruyff", "maldini", "drogba", "kroos", "pirlo", "gerrard", "lampard", "balotelli",
        "cantona", "totti", "r9", "ronaldo naz[aá]rio", "son heung-min", "heung-min son", "van dijk", "pogba",
        "griezmann", "ag[uü]ero", "eto'?o", "robben", "rib[eé]ry", "george best", "eusebio", "eus[eé]bio", "figo",
        "kaka", "bale", "gareth bale", "neuer", "buffon", "casillas", "kahn", "saka", "palmer", "pedri", "gavi",
        "cristiano jr", "georgina"]
MANAGER = ["managers?", "coach(es)?", "head coach", "gaffer", "boss", "ferguson", "fergie", "mourinho", "guardiola",
           "pep", "klopp", "wenger", "ancelotti", "arteta", "simeone", "conte", "tuchel", "ten hag", "amorim",
           "maresca", "postecoglou", "flick", "xabi alonso", "luis enrique", "slot", "bielsa", "van gaal", "capello",
           "sacked", "fired", "tactics?", "tactical", "formation", "pressing"]
CLUBS = ["barcelona", "barca", "barça", "real madrid", "madrid", "man utd", "man united", "manchester united",
         "manchester city", "man city", "liverpool", "arsenal", "chelsea", "bayern", "juventus", "juve", "psg",
         "ac milan", "milan", "inter", "tottenham", "spurs", "dortmund", "atletico", "ajax", "napoli", "roma",
         "al nassr", "al hilal", "inter miami", "newcastle", "aston villa", "leicester", "everton", "celtic", "rangers"]

TOPICS = {
    "goalkeeper": W(*KEEPERS),
    "Messi": W("messi", "lionel messi", "leo messi"),
    "Ronaldo (Cristiano)": W("ronaldo", "cristiano", "cr7"),
    "other megastar": W(*MEGA),
    "manager/coach": W(*MANAGER),
    "referee/rules/VAR": W("referees?", "refs?", "var", "red cards?", "yellow cards?", "sent off", "offside", "rules?",
                           "laws?", "illegal", "handball", "allowed", "not allowed", "whistle", "penalty kick rule"),
    "money/transfer/contract": W("transfers?", "signed", "signing", "signs?", "contracts?", "salary", "salaries", "wages?",
                                 "paid", "pay", "pays", "million", "millions", "billion", "billions", "money", "fees?",
                                 "rich", "richest", "broke", "bankrupt", "bought", "buy", "sold", "sell", "sponsors?",
                                 "sponsorship", "bonus", "price", "cost", "costs", "expensive", "cheap", "cheapest",
                                 "earn", "earns", "earned", "net worth", "worth", "deal", "offer", "offered", "loan",
                                 "free agent", "market value", "\\$", "£", "€", "\\d+m", "dollars", "euros", "pounds"),
    "conflict/revenge/rivalry": W("revenge", "rivals?", "rivalry", "derby", "hated?", "hates", "hating", "enem(y|ies)",
                                  "betray(ed|al)?", "refused?", "refuses", "rejected", "reject", "rejection",
                                  "their own", "his own", "own (club|team|country|fans|teammates?|sponsor|coach|manager)",
                                  "feuds?", "fights?", "fought", "beef", "disrespect(ed|ful)?", "insult(ed|s)?",
                                  "humiliat\\w*", "regrets?", "regretted", "sued", "sue", "sues", "clash(ed)?",
                                  "angry", "furious", "mock(ed|ing)?", "proved .{0,20}wrong", "snub(bed)?",
                                  "didn't like", "did not like", "dislike", "vs", "versus", "against", "attack(ed)?",
                                  "punch(ed)?", "slap(ped)?", "kick(ed)? out", "banned .{0,15}fans?"),
    "secret/object/ritual/superstition": W("superstitions?", "superstitious", "rituals?", "lucky", "luck", "curse",
                                           "cursed", "secrets?", "secretly", "hid", "hidden", "hide", "hiding",
                                           "cheat sheet", "notes?", "bottles?", "boots", "socks?", "shin ?pads?",
                                           "gloves", "shirts?", "jerseys?", "tattoos?", "charm", "magic", "witch(craft)?",
                                           "voodoo", "juju", "wore", "wears?", "wearing", "underwear", "gum", "drinks?",
                                           "haircut", "hair", "hairstyle", "celebrations?", "routine", "pre-match",
                                           "armband", "napkin", "objects?", "pennants?", "mask", "headband", "kits?",
                                           "chains?", "earrings?", "cars?", "watch(es)?"),
    "fan/kid story": W("fans?", "supporters?", "ultras", "crowd", "ball ?boys?", "ball ?girls?", "mascots?",
                       "pitch invaders?", "kids?", "child", "children", "boy", "girl", "little", "young fan",
                       "spectators?", "season tickets?"),
    "World Cup/national team": W("world cups?", "euro (19|20)\\d\\d", "the euros", "euros final", "copa am[eé]rica",
                                 "afcon", "africa cup", "nations league", "international", "internationals",
                                 "national team", "nationality", "countr(y|ies)", "nations?", "brazil", "argentina",
                                 "england", "france", "germany", "spain", "portugal", "italy", "netherlands", "holland",
                                 "morocco", "croatia", "usa", "usmnt", "mexico", "japan", "south korea", "korea",
                                 "uruguay", "belgium", "colombia", "nigeria", "senegal", "ghana", "cameroon", "qatar",
                                 "iceland", "cape verde", "wales", "scotland", "ireland", "egypt", "australia",
                                 "canada", "brazilian", "argentine", "argentinian"),
    "underdog/rise": W("underdogs?", "relegat\\w*", "lower league", "non-league", "amateurs?", "small club",
                       "smallest", "tiny", "village", "minnows?", "odds", "from nothing", "rise", "rose", "nobody",
                       "unknown", "normal jobs?", "ordinary", "factory", "worked as", "miracles?", "comebacks?",
                       "shock(ed)? the world", "against all odds", "made it", "became", "from the streets",
                       "underrated", "doubted", "proved"),
    "club history/origins": W("history of", "founded", "oldest club", "nicknames?", "badges?", "crests?",
                              "called", "named", "origins?", "invented", "first ever", "where .{0,20} came from",
                              "stadiums?", "why .{0,30} (wear|called|play)"),
    "tragedy/injury/health": W("died", "dies", "death", "dead", "killed", "tragedy", "tragic", "injur\\w*",
                               "broke (his|her) \\w+", "broken", "career-ending", "cancer", "ill", "illness",
                               "disease", "heart attack", "cardiac", "collapsed?", "crash(ed)?", "accident", "war",
                               "poor", "poverty", "homeless", "cried", "crying", "tears", "sad", "heartbreak\\w*",
                               "medical", "conditions?", "disab\\w*", "blind", "deaf", "one arm", "one leg",
                               "amputee", "depression", "ended (his|their) careers?", "ruined", "💔", "🥀", "😢", "😭"),
    "crime/scandal/ban": W("arrest(ed)?", "jail(ed)?", "prison", "prisoners?", "police", "crimes?", "criminals?",
                           "scandals?", "fixing", "match-fixing", "bribe(s|d)?", "corrupt\\w*", "drugs?", "doping",
                           "cheat(ed|ing|ers?)?(?! sheet)", "fake passport", "kidnap\\w*", "gangs?", "mafia",
                           "banned", "bans?", "suspended", "suspension", "guilty", "court", "lawsuits?", "tax",
                           "investigat\\w*", "sued"),
    "funny/banter": W("funny", "funniest", "hilarious", "laugh\\w*", "jokes?", "joked", "pranks?", "troll(ed|ing|s)?",
                      "banter", "embarrass\\w*", "awkward", "weird", "weirdest", "strange", "strangest", "bizarre",
                      "ridiculous", "silly", "stupid", "dumb", "fails?", "memes?", "lol", "😂", "🤣", "💀", "🤡"),
    "record/number": W("records?", "fastest", "youngest", "oldest", "longest", "shortest", "highest", "lowest",
                       "first ever", "only (player|team|club|man|goalkeeper|keeper)", "never", "most goals",
                       "most assists", "most trophies", "in history", "of all time", "ever"),
    "family/WAGs": W("wi(fe|ves)", "girlfriends?", "wags?", "georgina", "sons?", "father", "dad", "mother", "mom",
                     "mum", "brothers?", "sisters?", "family", "daughters?", "jr", "junior", "parents", "married",
                     "wedding", "baby", "grandmother", "grandma"),
    "downfall/flop/almost": W("fell off", "fall", "downfall", "destroyed", "flops?", "flopped", "wasted", "worst",
                              "bust", "failed", "failure", "forgotten", "disappeared", "what happened to",
                              "decline", "almost", "nearly", "should have", "could have", "missed out", "lost everything"),
    "tactics/analysis/stats": W("tactics?", "tactical", "formation", "press(ing)?", "system", "midfield", "full-backs?",
                                "analysis", "stats", "statistics", "xg", "data", "clean sheets", "how .{0,25} plays?",
                                "role", "positions?", "set-pieces?", "set pieces?", "high line"),
    "debate/prediction/ranking": W("goat", "better", "best ever", "who is", "who's", "predict\\w*", "will .{0,30} win",
                                   "ranking", "ranked", "rank", "debate", "comment", "vs", "versus", "top \\d+",
                                   "tier list", "who would", "who wins"),
    "awards/Ballon d'Or/trophies": W("ballon d'?or", "awards?", "trophy", "trophies", "golden boot", "title", "titles",
                                     "champions league", "won the", "medal"),
}
# a club name in the title (not a topic family, but useful)
TOPICS["names a club"] = W(*CLUBS)
TOPICS["names a star (Messi/Ronaldo/other)"] = re.compile(
    "|".join([TOPICS["Messi"].pattern, TOPICS["Ronaldo (Cristiano)"].pattern, TOPICS["other megastar"].pattern]), re.I)

EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")
ACRONYMS = {"VAR", "PSG", "UCL", "FIFA", "UEFA", "USA", "NBA", "MLS", "AFC", "CR7", "EPL", "GOAT", "USMNT", "TV",
            "MVP", "PL", "ACL", "MSN", "BBC", "WWE", "LOL", "FC", "AC", "CF", "XI", "II", "III", "VS", "OMG", "WC"}
NUMWORD = r"(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|hundred|thousand)"
PLURAL_LEAD = re.compile(r"^((world cup|premier league|famous|football|soccer|african|english|brazilian|young|old|"
                         r"former|legendary|iconic|real|top|big|great|the)\s+){0,3}(players|teams|footballers|"
                         r"goalkeepers|managers|clubs|coaches|fans|countries|referees|strikers|defenders|legends|"
                         r"stars|moments|times|things|stadiums|kits|goals|ways|transfers|signings|celebrations|"
                         r"rules|matches|games|records|facts|reasons|teammates|brothers|siblings|rivals|nations)\b", re.I)

def shapes(t):
    s = {}
    tl = t.lower().strip()
    letters = [c for c in t if c.isalpha()]
    upper = sum(1 for c in letters if c.isupper())
    words = re.findall(r"[A-Za-z0-9'’]+", t.split("#")[0])
    s["question (? or Why/How/What/Who/Is/Did/Can...)"] = bool(re.search(r"\?", t) or re.match(
        r"^(why|how|what|who|which|where|is|are|was|were|did|does|do|can|could|would|will|should|has|have)\b", tl))
    s["starts 'Why'"] = tl.startswith("why ")
    s["starts 'How'"] = tl.startswith("how ")
    s["starts 'What/Who/Which'"] = bool(re.match(r"^(what|who|which)\b", tl))
    s["starts 'When'"] = tl.startswith("when ")
    s["'The day/night/time...'"] = bool(re.match(r"^the (day|night|time|moment|match|game|year)\b", tl))
    s["plural-led ('Players who...')"] = bool(PLURAL_LEAD.match(tl)) and not tl.startswith("the ")
    s["singular 'The X who/that...'"] = bool(re.match(r"^the\s+([\w'’-]+\s+){1,5}(who|that|which)\b", tl))
    s["superlative-led (Most/Craziest/Worst...)"] = bool(re.match(
        r"^(the )?(most|craziest|worst|best|biggest|funniest|weirdest|strangest|greatest|top|saddest|smartest|"
        r"dumbest|scariest|luckiest|unluckiest|rarest|fastest|youngest|oldest)\b", tl))
    s["number-led"] = bool(re.match(r"^(top )?(\d|" + NUMWORD + r"\b)", tl))
    first = tl.split(" ")[0] if tl else ""
    first2 = " ".join(tl.split(" ")[:2])
    s["name-led (star/club/manager first)"] = any(p.match(first2) or p.match(first) for p in
                                                  [TOPICS["names a star (Messi/Ronaldo/other)"], TOPICS["names a club"],
                                                   W("ferguson", "mourinho", "guardiola", "pep", "klopp", "wenger",
                                                     "ancelotti", "arteta", "simeone", "zidane")]) and \
        bool(re.match(r"^(" + "|".join([TOPICS["names a star (Messi/Ronaldo/other)"].pattern,
                                         TOPICS["names a club"].pattern]) + ")", tl, re.I))
    s["statement (no question)"] = not s["question (? or Why/How/What/Who/Is/Did/Can...)"]
    s["emoji"] = bool(EMOJI.search(t))
    s["hashtag"] = "#" in t
    s["ALL-CAPS title"] = len(letters) >= 8 and upper / len(letters) > 0.8
    caps_words = [w for w in words if len(w) >= 3 and w.isupper() and w not in ACRONYMS and not w.isdigit()]
    s["1+ CAPS word (title not all caps)"] = bool(caps_words) and not s["ALL-CAPS title"]
    s["'fake but real' / 'you didn't know' / 'real reason' / 'untold' framing"] = bool(re.search(
        r"fake|100% real|didn'?t know|never knew|real reason|truth|untold|nobody knows|no one knows|"
        r"behind the|story behind|the reason", tl))
    s["vague hype word (crazy/insane/wild/shocking)"] = bool(re.search(
        r"\b(crazy|craziest|insane|wild|wildest|shocking|shock|unbelievable|mind-blowing|drama|trouble)\b", tl))
    n = len(words)
    s["words: <=6"] = n <= 6
    s["words: 7-10"] = 7 <= n <= 10
    s["words: 11-14"] = 11 <= n <= 14
    s["words: 15+"] = n >= 15
    return s

INDO = W("yang", "dengan", "sepakbola", "kisah", "pemain", "ternyata", "karir", "bola", "pernah", "terkejut", "alasan",
         "untuk", "tidak", "banget", "bikin", "pake", "gara-gara", "sejarah", "klub", "baru", "dari", "ini", "itu",
         "jadi", "saat", "sang", "dia", "mulia", "gaya", "rambut", "di balik", "kantong", "tamat", "diremehkan",
         "kerempeng", "akhirnya", "malah", "aja", "sama", "kenapa", "siapa", "apa", "bisa", "sudah", "masih", "lagi",
         "juga", "hanya", "cuma", "para", "pelatih", "laga", "timnas", "liga", "tapi", "atau", "bukan", "pas", "gak",
         "nggak", "ke", "di", "dan", "wkwk", "anak", "orang", "punya", "main", "lawan", "menang", "kalah", "sampai")
OTHER = W("que", "el", "los", "las", "del", "por", "para", "como", "não", "mais", "uma", "você", "isso", "der", "die",
          "das", "und", "nicht", "ist", "ein", "ki", "ka", "ke", "hai", "aur", "kya", "mein", "nahi", "se")

def english(t):
    body = t.split("#")[0]
    if len(INDO.findall(body)) >= 2 or W("yang", "dengan", "sepakbola", "kisah", "pemain", "ternyata", "karir",
                                         "terkejut", "banget", "gara-gara", "diremehkan").search(body):
        return False
    if len(OTHER.findall(body)) >= 2:
        return False
    return True

def topics(t):
    tl = t.split("#")[0]  # hashtags are tags, not the promise
    return {k: bool(p.search(tl)) for k, p in TOPICS.items()}

def load(ch):
    rows = []
    sp = os.path.join(RAW, f"{ch}_shorts.tsv")
    up = os.path.join(RAW, f"{ch}_uploads.tsv")
    meta = {}
    if os.path.exists(up):
        for line in open(up, encoding="utf-8"):
            p = line.rstrip("\n").split("\t")
            if len(p) >= 5:
                meta[p[0]] = (p[2], p[3])
    for i, line in enumerate(open(sp, encoding="utf-8")):
        p = line.rstrip("\n").split("\t")
        if len(p) < 4 or not p[1].isdigit():
            continue
        dur, date = meta.get(p[0], ("NA", "NA"))
        rows.append({"channel": ch, "pos": i, "id": p[0], "views": int(p[1]), "title": p[3],
                     "dur": float(dur) if dur not in ("NA", "") else None, "date": date if date != "NA" else ""})
    return rows

def prep(ch):
    rows = load(ch)
    out = []
    for r in rows:
        if r["date"] and r["date"] >= CUTOFF:
            continue
        if not r["date"] and r["pos"] < 5:
            continue
        if not english(r["title"]):
            continue
        out.append(r)
    if not out:
        return []
    med = st.median(r["views"] for r in out) or 1
    vs = [r["views"] for r in out]
    for i, r in enumerate(out):
        lo, hi = max(0, i - 50), min(len(out), i + 51)
        local = st.median(vs[lo:hi]) or 1
        r["ratio"] = r["views"] / med
        r["rel"] = r["views"] / local
        r["chmed"] = med
    cut = sorted((r["rel"] for r in out), reverse=True)[max(0, len(out) // 10 - 1)]
    for r in out:
        r["top10"] = r["rel"] >= cut
        r["topics"] = topics(r["title"])
        r["shapes"] = shapes(r["title"])
    return out

def fmt(v):
    return f"{v/1e6:.1f}M" if v >= 1e6 else (f"{v/1e3:.0f}K" if v >= 1e3 else str(v))

def table(rows, keyfn, keys, title, examples=5, min_n=8, out=sys.stdout):
    by_ch = defaultdict(list)
    for r in rows:
        by_ch[r["channel"]].append(r)
    total_top = sum(1 for r in rows if r["top10"])
    res = []
    for k in keys:
        sub = [r for r in rows if keyfn(r, k)]
        if len(sub) < min_n:
            continue
        rest = [r for r in rows if not keyfn(r, k)]
        chans = []
        for ch, rs in by_ch.items():
            s = [r["rel"] for r in rs if keyfn(r, k)]
            if len(s) >= 5:
                chans.append((ch, st.median(s), len(s)))
        res.append({
            "k": k, "n": len(sub), "nch": len({r['channel'] for r in sub}),
            "med_ratio": st.median(r["ratio"] for r in sub), "med_rel": st.median(r["rel"] for r in sub),
            "rest_rel": st.median(r["rel"] for r in rest) if rest else 0,
            "hit": sum(r["top10"] for r in sub) / len(sub), "share_top": sum(r["top10"] for r in sub) / max(1, total_top),
            "share_all": len(sub) / len(rows),
            "bal": st.median(c[1] for c in chans) if chans else float("nan"),
            "up": sum(1 for c in chans if c[1] > 1.0), "nc5": len(chans),
            "ex": sorted(sub, key=lambda r: -r["rel"])[:examples],
        })
    res.sort(key=lambda d: -d["med_rel"])
    print(f"\n## {title}\n", file=out)
    print("| Category | n | channels | median views/ch-median | median time-adj | rest time-adj | in top 10% (base 10%) |"
          " share of all top-10% (vs share of all) | channel-balanced median (ch>1.0 / ch n>=5) |", file=out)
    print("|---|---|---|---|---|---|---|---|---|", file=out)
    for d in res:
        print(f"| {d['k']} | {d['n']} | {d['nch']} | {d['med_ratio']:.2f} | **{d['med_rel']:.2f}** | {d['rest_rel']:.2f} | "
              f"{d['hit']*100:.0f}% | {d['share_top']*100:.0f}% (vs {d['share_all']*100:.0f}%) | "
              f"{d['bal']:.2f} ({d['up']}/{d['nc5']}) |", file=out)
    print("\nTop examples (time-adjusted ratio, views, channel):", file=out)
    for d in res:
        ex = "; ".join(f"\"{r['title'][:80]}\" ({fmt(r['views'])}, {r['rel']:.1f}x, {r['channel']})" for r in d["ex"])
        print(f"- **{d['k']}**: {ex}", file=out)
    return res

def main():
    allrows = {}
    for ch in STORY + ANALYSIS:
        allrows[ch] = prep(ch)
    out = open(os.path.join(HERE, "results.txt"), "w", encoding="utf-8")
    print("# Soccer Topic Study: computed tables (Nov 1, 2026)\n", file=out)
    print("| Channel | Shorts pulled | English, settled (analysed) | channel median views | with duration |", file=out)
    print("|---|---|---|---|---|", file=out)
    for ch in STORY + ANALYSIS:
        raw = load(ch)
        rs = allrows[ch]
        print(f"| {ch} | {len(raw)} | {len(rs)} | {fmt(rs[0]['chmed']) if rs else '-'} | "
              f"{sum(1 for r in rs if r['dur'])} |", file=out)
    story = [r for ch in STORY for r in allrows[ch]]
    tkeys = list(TOPICS.keys())
    table(story, lambda r, k: r["topics"][k], tkeys, "Topics: 8 story/facts channels pooled", out=out)
    table([r for r in story if r["channel"] != "AhmedsGoal"], lambda r, k: r["topics"][k], tkeys,
          "Topics: story/facts channels WITHOUT Ahmed's Goal (does it hold outside Ahmed?)", examples=3, out=out)
    table(allrows["AhmedsGoal"], lambda r, k: r["topics"][k], tkeys, "Topics: Ahmed's Goal only", examples=3, out=out)
    table(allrows["FootyFacts"], lambda r, k: r["topics"][k], tkeys, "Topics: FOOTY FACTS only (English era)",
          examples=3, min_n=6, out=out)
    skeys = list(shapes("x").keys())
    table(story, lambda r, k: r["shapes"][k], skeys, "Title shapes: 8 story/facts channels pooled", examples=3, out=out)
    table([r for r in story if r["channel"] != "AhmedsGoal"], lambda r, k: r["shapes"][k], skeys,
          "Title shapes: WITHOUT Ahmed's Goal", examples=2, out=out)
    table(allrows["AhmedsGoal"], lambda r, k: r["shapes"][k], skeys, "Title shapes: Ahmed's Goal only", examples=2,
          out=out)
    ana = [r for ch in ANALYSIS for r in allrows[ch]]
    table(ana, lambda r, k: r["shapes"][k], skeys, "Title shapes: analysis channels (Tifo/The Athletic FC, Statman Dave)",
          examples=2, out=out)
    table(ana, lambda r, k: r["topics"][k], tkeys, "Topics: analysis channels (Tifo/The Athletic FC, Statman Dave)",
          examples=2, out=out)
    # duration: only Shorts with a known duration (the newest ~100-1,400 per channel)
    buckets = [("<30 s", 0, 30), ("30-44 s", 30, 45), ("45-59 s", 45, 60), ("60-74 s", 60, 75), ("75-89 s", 75, 90),
               ("90-119 s", 90, 120), ("120 s+", 120, 9999)]
    dur_rows = [r for r in story + ana if r["dur"]]
    table(dur_rows, lambda r, k: any(b[0] == k and b[1] <= r["dur"] < b[2] for b in buckets), [b[0] for b in buckets],
          "Duration buckets (all 10 channels, Shorts with a known duration)", examples=2, min_n=5, out=out)
    ah = [r for r in allrows["AhmedsGoal"] if r["dur"]]
    table(ah, lambda r, k: any(b[0] == k and b[1] <= r["dur"] < b[2] for b in buckets), [b[0] for b in buckets],
          "Duration buckets: Ahmed's Goal only", examples=2, min_n=5, out=out)
    nah = [r for r in story if r["dur"] and r["channel"] != "AhmedsGoal"]
    table(nah, lambda r, k: any(b[0] == k and b[1] <= r["dur"] < b[2] for b in buckets), [b[0] for b in buckets],
          "Duration buckets: story/facts channels without Ahmed", examples=2, min_n=5, out=out)
    # recency check: does ratio fall with position (newer = less accrued)?
    print("\n## Recency check (views / channel median by age quintile, newest first)\n", file=out)
    for ch in STORY + ANALYSIS:
        rs = allrows[ch]
        if len(rs) < 25:
            continue
        q = len(rs) // 5
        meds = [st.median(r["ratio"] for r in rs[i*q:(i+1)*q]) for i in range(5)]
        print(f"- {ch}: " + " | ".join(f"{m:.2f}" for m in meds) + "  (newest -> oldest)", file=out)
    # classified file
    with open(os.path.join(HERE, "classified.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["channel", "pos_newest_first", "id", "views", "ratio", "rel_time_adj", "top10", "duration", "date",
                    "topics", "shapes", "title"])
        for r in story + ana:
            w.writerow([r["channel"], r["pos"], r["id"], r["views"], f"{r['ratio']:.2f}", f"{r['rel']:.2f}",
                        int(r["top10"]), r["dur"] or "", r["date"],
                        ";".join(k for k, v in r["topics"].items() if v),
                        ";".join(k for k, v in r["shapes"].items() if v and not k.startswith("words")), r["title"]])
    out.close()
    print(open(os.path.join(HERE, "results.txt"), encoding="utf-8").read()[:1500])

if __name__ == "__main__":
    main()
