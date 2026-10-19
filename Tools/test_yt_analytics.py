"""Offline test of yt_analytics.py `daily` + `report` with API-shaped FIXTURE data (not real channel numbers).
  python Tools/test_yt_analytics.py      -> prints the report and asserts the flags fire
"""
import datetime, io, os, sys, tempfile, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yt_analytics as ya

today = datetime.date.today()
d = lambda n: (today - datetime.timedelta(days=n)).isoformat() + "T15:00:00Z"
FIX = {
    "channels": {"items": [{"contentDetails": {"relatedPlaylists": {"uploads": "UUfixture"}}}]},
    "playlistItems": {"items": [{"contentDetails": {"videoId": v}} for v in ("GOOD", "SWIPED", "OLD")]},
    "videos": {"items": [
        {"id": "GOOD", "snippet": {"title": "Fixture good Short", "publishedAt": d(2)}, "contentDetails": {"duration": "PT24S"}},
        {"id": "SWIPED", "snippet": {"title": "Fixture swiped Short", "publishedAt": d(3)}, "contentDetails": {"duration": "PT22S"}},
        {"id": "OLD", "snippet": {"title": "Fixture old video", "publishedAt": d(90)}, "contentDetails": {"duration": "PT20S"}}]},
    "metrics": {"columnHeaders": [{"name": n} for n in ["video"] + ya.DAILY_METRICS.split(",")],
                "rows": [["GOOD", 25000, 14000, 22, 95.4, 7, 900, 40], ["SWIPED", 2000, 900, 17, 81.9, 1, 30, 1]]},
}
CURVES = {"GOOD": [[i / 100, 1.05 - i / 400, 0.8] for i in range(101)],
          "SWIPED": [[i / 100, (0.95 if i < 3 else 0.62) - i / 500, 0.3] for i in range(101)]}


def fake_get(url, at):
    if "/channels?" in url: return FIX["channels"]
    if "/playlistItems?" in url: return FIX["playlistItems"]
    if "/videos?" in url: return FIX["videos"]
    if "elapsedVideoTimeRatio" in url:
        vid = url.split("video%3D%3D")[-1].split("&")[0]
        return {"rows": CURVES[vid]}
    return FIX["metrics"]


tmp = tempfile.mkdtemp()
ya.get, ya.access_token, ya.API_DIR = fake_get, (lambda: "TOKEN"), tmp
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ya.daily()
out = buf.getvalue()
print(out)
assert "Fixture old video" not in out, "uploads older than the window must be skipped"
assert "SWIPED" not in out and "engaged ratio 0.45 < 0.5" in out, "the low engaged ratio must be flagged"
assert "weak start" in out and "sharp early drop" in out, "the swiped curve must be flagged"
assert out.count("FLAG") >= 3
good = out.split("Fixture good Short")[1].split("Fixture")[0] if "Fixture good" in out else ""
assert "weak start" not in good, "the good curve must not get a weak-start flag"
print("TEST PASSED (fixture data, not real numbers)")
