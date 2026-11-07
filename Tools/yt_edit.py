"""Edit your own YouTube videos from the terminal (Nov 6, 2026). Needs the one-time sign-in: python Tools/yt_manage_auth.py nba|fc

  python Tools/yt_edit.py fc show <video_id>
  python Tools/yt_edit.py fc title <video_id> "New title"
  python Tools/yt_edit.py fc tags <video_id> "tag one, tag two, ..."            (keeps the title; tags capped at 490 characters)
  python Tools/yt_edit.py fc privacy <video_id> private|unlisted|public
  python Tools/yt_edit.py fc publish-at <video_id> "2026-11-07 12:00"           (ET; the video must be private; 20 min to 30 days ahead)
  python Tools/yt_edit.py fc delete <video_id> <video_id>                        (the id twice; deletes for good; nothing else is ever deleted by name)

Rules built in: a title may not be empty/"unknown"/"untitled"; titles are 100 characters at most; `delete` needs the exact id typed twice; every change is
appended to Research Notes/Edit Log.md with the old and the new value. Sign-in note: while the Google Cloud app is in "Testing" the token dies after 7 days.
Make it permanent once: console.cloud.google.com > APIs & Services > OAuth consent screen > Audience (or Publishing status) > "Publish app" > Confirm;
then run yt_manage_auth.py again for each channel.
"""
import datetime, json, os, sys, urllib.parse, urllib.request
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "Tools"))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ET = ZoneInfo("America/New_York")


def env():
    d = {}
    for l in open(os.path.join(ROOT, "Tools", ".env"), encoding="utf-8"):
        if "=" in l and not l.lstrip().startswith("#"):
            k, v = l.strip().split("=", 1); d[k] = v
    return d


def token(ch):
    e = env(); key = "YT_MANAGE_TOKEN" if ch == "nba" else "YT_MANAGE_TOKEN_FC"
    if not e.get(key):
        sys.exit(f"No edit sign-in yet for {ch}: run  python Tools/yt_manage_auth.py {ch}")
    data = urllib.parse.urlencode({"client_id": e["YT_CLIENT_ID"], "client_secret": e["YT_CLIENT_SECRET"], "refresh_token": e[key], "grant_type": "refresh_token"}).encode()
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=data), timeout=60))["access_token"]
    except urllib.error.HTTPError as ex:
        sys.exit(f"The edit sign-in for {ch} no longer works ({ex.code}); run yt_manage_auth.py {ch} again (tokens die after 7 days while the app is in Testing).")


def call(url, at, method="GET", body=None):
    req = urllib.request.Request(url, method=method, data=(json.dumps(body).encode() if body is not None else None),
                                 headers={"Authorization": "Bearer " + at, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read(); return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as ex:
        sys.exit(f"YouTube refused ({ex.code}): {ex.read().decode(errors='replace')[:300]}")


def get(vid, at):
    items = call("https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode({"part": "snippet,status", "id": vid}), at).get("items", [])
    if not items:
        sys.exit(f"No video {vid} on this channel.")
    return items[0]


def log(ch, vid, what, old, new):
    p = os.path.join(ROOT, "Research Notes", "Edit Log.md")
    with open(p, "a", encoding="utf-8") as f:
        if os.path.getsize(p) == 0 if os.path.exists(p) else True:
            pass
        f.write(f"- {datetime.datetime.now(ET):%Y-%m-%d %H:%M} ET {ch} {vid} {what}: {old!r} -> {new!r}\n")


def put(v, at):
    sn = v["snippet"]
    body = {"id": v["id"], "snippet": {"title": sn["title"], "categoryId": sn["categoryId"], "description": sn.get("description", ""), "tags": sn.get("tags", [])},
            "status": {"privacyStatus": v["status"]["privacyStatus"], **({"publishAt": v["status"]["publishAt"]} if v["status"].get("publishAt") else {}),
                       "selfDeclaredMadeForKids": v["status"].get("selfDeclaredMadeForKids", False)}}
    return call("https://www.googleapis.com/youtube/v3/videos?part=snippet,status", at, "PUT", body)


def main():
    a = sys.argv[1:]
    if len(a) < 3 or a[0] not in ("nba", "fc"):
        sys.exit(__doc__)
    ch, cmd, vid = a[0], a[1], a[2]
    at = token(ch)
    if cmd == "show":
        v = get(vid, at); print(json.dumps({"title": v["snippet"]["title"], "tags": len(v["snippet"].get("tags", [])), "privacy": v["status"]["privacyStatus"], "publishAt": v["status"].get("publishAt")}, ensure_ascii=False)); return
    if cmd == "delete":
        if len(a) < 4 or a[3] != vid:
            sys.exit("delete needs the exact video id typed twice.")
        v = get(vid, at); call("https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode({"id": vid}), at, "DELETE")
        log(ch, vid, "DELETED", v["snippet"]["title"], None); print("deleted", vid); return
    v = get(vid, at)
    if cmd == "title":
        t = a[3].strip()
        if not t or t.lower() in ("unknown", "untitled", "none") or len(t) > 100:
            sys.exit("Refused: empty/placeholder title or over 100 characters.")
        old = v["snippet"]["title"]; v["snippet"]["title"] = t; put(v, at); log(ch, vid, "title", old, t); print("title set:", t)
    elif cmd == "tags":
        tags = [x.strip() for x in a[3].split(",") if x.strip()]
        while len(",".join(tags)) > 490:
            tags.pop()
        old = len(v["snippet"].get("tags", [])); v["snippet"]["tags"] = tags; put(v, at); log(ch, vid, "tags", old, len(tags)); print(len(tags), "tags set")
    elif cmd == "privacy":
        if a[3] not in ("private", "unlisted", "public"):
            sys.exit("privacy must be private, unlisted or public")
        old = v["status"]["privacyStatus"]; v["status"]["privacyStatus"] = a[3]; v["status"].pop("publishAt", None); put(v, at); log(ch, vid, "privacy", old, a[3]); print("privacy:", a[3])
    elif cmd == "publish-at":
        when = datetime.datetime.strptime(a[3], "%Y-%m-%d %H:%M").replace(tzinfo=ET); now = datetime.datetime.now(ET)
        if not (now + datetime.timedelta(minutes=20) <= when <= now + datetime.timedelta(days=30)):
            sys.exit("The time must be 20 minutes to 30 days ahead.")
        old = v["status"].get("publishAt"); v["status"]["privacyStatus"] = "private"
        v["status"]["publishAt"] = when.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"); put(v, at); log(ch, vid, "publishAt", old, a[3]); print("scheduled", a[3], "ET")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
