"""Schedule an approved DRAFT on YouTube with the official Data API, so it goes live by itself at its slot (Nov 1, 2026).

OFF until the owner turns it on. It does nothing without an upload token that only the owner can make (below), and the standing
rule in the skills is still "never publish or schedule": a run may use this only for a Short the owner has approved
(Hub card `approved: true`, or the owner's own words in chat), and only after the owner says auto-scheduling is on.

Why it's possible now: Google's videos.insert reference (last updated 2026-10-15) says "Videos uploaded from unverified API
projects are not restricted to private viewing mode", and uploads have their own quota bucket ("100 calls per day ... 1 unit").
Before that, uploads from a personal (unaudited) Google project were locked private.

What it does, and what it never does:
  - Uploads the file as PRIVATE with a publish time (status.publishAt), so YouTube makes it public at the slot. Until then the
    owner can see it in the YouTube app (Library > Your videos > Scheduled), change it or delete it. It never posts right away.
  - Title, tags (the card's 490-character line), empty description, category Sports, "not made for kids".
  - Refuses: a file whose name doesn't start with "DRAFT", a slot less than 20 minutes away or more than 30 days away, and any
    file it has already scheduled once (Research Notes/Scheduled Uploads.csv): never re-upload a Short.
  - Can't pin the comment (the API has no pin), can't edit or delete videos (its scope is youtube.upload only).

  python Tools/yt_schedule.py --channel nba --file "<DRAFT ....mp4>" --title "..." --tags "a, b, c" --at "2026-11-02 07:15"
      -> dry run: prints what it would send. Add --go to upload. --at is US Eastern time.

ONE-TIME SETUP (owner, about 5 minutes per channel, no PC needed; same Google app as Tools/yt_analytics.py):
  1. https://developers.google.com/oauthplayground -> gear icon -> "Use your own OAuth credentials" -> the client ID and secret.
  2. "Input your own scopes": https://www.googleapis.com/auth/youtube.upload
  3. Authorize APIs -> sign in -> pick the channel -> "Exchange authorization code for tokens".
  4. In the cloud environment's settings add the refresh token as YT_UPLOAD_TOKEN (MetaSports) or YT_UPLOAD_TOKEN_FC
     (MetaSports FC), plus YT_CLIENT_ID and YT_CLIENT_SECRET if they aren't there yet. Never paste a token in chat or in git.
     The Google app must be published ("Publish app" on the OAuth consent screen) or the token dies after 7 days.
Standard library only.
"""
import argparse, csv, datetime, hashlib, json, os, sys, urllib.error, urllib.parse, urllib.request
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LOG = os.path.join(ROOT, "Research Notes", "Scheduled Uploads.csv")
TOKEN_URL = "https://oauth2.googleapis.com/token"
UPLOAD_URL = "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status"
ENV = {"nba": "YT_UPLOAD_TOKEN", "fc": "YT_UPLOAD_TOKEN_FC"}
ET = ZoneInfo("America/New_York")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()[:16]


def already(digest):
    if not os.path.exists(LOG):
        return None
    for row in csv.DictReader(open(LOG, encoding="utf-8")):
        if row.get("sha") == digest:
            return row
    return None


def access_token(channel):
    refresh = os.environ.get(ENV[channel])
    cid, csec = os.environ.get("YT_CLIENT_ID"), os.environ.get("YT_CLIENT_SECRET")
    if not (refresh and cid and csec):
        sys.exit(f"Auto-scheduling is off: {ENV[channel]}, YT_CLIENT_ID and YT_CLIENT_SECRET must all be in the environment "
                 "(setup steps at the top of this file). Nothing was uploaded.")
    data = urllib.parse.urlencode({"client_id": cid, "client_secret": csec, "refresh_token": refresh,
                                   "grant_type": "refresh_token"}).encode()
    with urllib.request.urlopen(urllib.request.Request(TOKEN_URL, data=data, method="POST"), timeout=30) as r:
        return json.load(r)["access_token"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", choices=["nba", "fc"], required=True)
    ap.add_argument("--file", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--tags", default="", help="comma-separated (the card's line from tags_fit.py)")
    ap.add_argument("--at", required=True, help='publish time, US Eastern: "YYYY-MM-DD HH:MM"')
    ap.add_argument("--go", action="store_true", help="really upload (default: dry run)")
    a = ap.parse_args()

    name = os.path.basename(a.file)
    if not name.startswith("DRAFT"):
        sys.exit("Refused: only a 'DRAFT - awaiting approval' file can be scheduled.")
    if not os.path.exists(a.file):
        sys.exit(f"No such file: {a.file}")
    when = datetime.datetime.strptime(a.at, "%Y-%m-%d %H:%M").replace(tzinfo=ET)
    now = datetime.datetime.now(ET)
    if not (now + datetime.timedelta(minutes=20) <= when <= now + datetime.timedelta(days=30)):
        sys.exit(f"Refused: the slot must be 20 minutes to 30 days from now (it is {when:%a %b %d %H:%M} ET).")
    tags = [t.strip() for t in a.tags.split(",") if t.strip()]
    if len(a.title) > 100:
        sys.exit("Refused: YouTube titles are 100 characters at most.")
    digest = sha(a.file)
    prev = already(digest)
    if prev:
        sys.exit(f"Refused: this exact file was already scheduled ({prev['video_id']}, {prev['publish_et']}). Never re-upload.")

    body = {"snippet": {"title": a.title, "description": "", "tags": tags, "categoryId": "17"},
            "status": {"privacyStatus": "private", "publishAt": when.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                       "selfDeclaredMadeForKids": False}}
    size = os.path.getsize(a.file)
    print(f"{'UPLOAD' if a.go else 'DRY RUN'}: {a.channel} | {name} ({size / 1e6:.1f} MB)")
    print(f"  title: {a.title}\n  tags: {len(tags)} | goes public {when:%a %b %d, %H:%M} ET (private until then)")
    if not a.go:
        print("Nothing sent. Add --go to schedule it.")
        return

    at = access_token(a.channel)
    req = urllib.request.Request(UPLOAD_URL, data=json.dumps(body).encode(), method="POST", headers={
        "Authorization": f"Bearer {at}", "Content-Type": "application/json; charset=UTF-8",
        "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            session = r.headers["Location"]
        with open(a.file, "rb") as f:
            put = urllib.request.Request(session, data=f.read(), method="PUT", headers={"Content-Type": "video/mp4"})
        with urllib.request.urlopen(put, timeout=600) as r:
            vid = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"YouTube refused it ({e.code}): {e.read().decode(errors='replace')[:400]}")
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["scheduled_utc", "channel", "video_id", "publish_et", "title", "file", "sha"])
        w.writerow([datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M"), a.channel, vid["id"], f"{when:%Y-%m-%d %H:%M}",
                    a.title, os.path.relpath(a.file, ROOT), digest])
    print(f"Scheduled: https://youtube.com/shorts/{vid['id']} goes public {when:%a %b %d %H:%M} ET. "
          "Pin the comment in the YouTube app after it goes live.")


if __name__ == "__main__":
    main()
