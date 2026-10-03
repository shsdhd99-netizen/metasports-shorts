"""Has a bigger channel already told this story? Searches YouTube Shorts for free (yt-dlp).

Usage: python copy_check.py "why no one shoots underhand free throws"
Verdict: FRESH (nothing big found) / CROWDED (some versions) / TAKEN (a version already has 500K+ views)
"""
import json, re, subprocess, sys

OFFICIAL = {"NBA", "ESPN", "House of Highlights", "Bleacher Report", "NBA on ESPN", "Sports Illustrated", "ClutchPoints"}
STOP = {"the", "a", "an", "of", "in", "on", "for", "to", "not", "is", "and", "back", "why", "how", "what", "no", "one",
        "his", "he", "they", "this", "that", "with", "at", "by", "from", "nba", "shorts", "vs"}


def relevant(title, topic):
    """Same story, not just the same search: the title shares 2+ topic words, including a name if the topic has one."""
    t = title.lower()
    words = [w for w in re.findall(r"[\w']+", topic) if w.lower() not in STOP]
    names = [w for w in words if w[0].isupper() or w.isdigit()]
    hits = [w for w in words if w.lower() in t]
    return len(hits) >= min(2, len(words)) and (not names or any(n.lower() in t for n in names))


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python copy_check.py "topic"')
    topic = " ".join(sys.argv[1:])
    ents, seen = [], set()
    for query in (f"ytsearch30:{topic}", f"ytsearch30:{topic} #shorts"):  # two searches catch more of the big versions
        r = subprocess.run(["yt-dlp", "--flat-playlist", "-J", "--no-warnings", query],
                           capture_output=True, text=True, encoding="utf-8")
        try:
            found = [e for e in (json.loads(r.stdout) or {}).get("entries") or [] if e]
        except json.JSONDecodeError:
            continue
        ents += [e for e in found if e.get("id") not in seen]
        seen.update(e.get("id") for e in found)
    if not ents:
        raise SystemExit("Search failed (check your internet or update yt-dlp).")
    shorts = [e for e in ents if (e.get("duration") or 0) <= 180]
    storytellers = [e for e in shorts if (e.get("channel") or "") not in OFFICIAL and relevant(e.get("title") or "", topic)]
    storytellers.sort(key=lambda e: e.get("view_count") or 0, reverse=True)
    print(f'Copy-check: "{topic}"\n')
    print(f"{'Views':>12}  {'Channel':<26} Title")
    for e in storytellers[:10]:
        print(f"{(e.get('view_count') or 0):>12,}  {(e.get('channel') or '')[:26]:<26} {(e.get('title') or '')[:70]}")
    top = storytellers[0].get("view_count") or 0 if storytellers else 0
    big = [e for e in storytellers if (e.get("view_count") or 0) >= 100_000]
    if top >= 500_000:
        verdict = "TAKEN - a storyteller already got 500K+ on this. Skip it or find a clearly new angle."
    elif big:
        verdict = "CROWDED - some versions exist. Only do it with a sharper hook or newer footage."
    else:
        verdict = "FRESH - nobody big has told this yet. Go."
    print(f"\nVerdict: {verdict}")


if __name__ == "__main__":
    main()
