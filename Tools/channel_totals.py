"""Channel-level totals for the monetization check (Nov 5, 2026). Read-only YouTube Analytics API (same tokens as yt_analytics.py).

  python Tools/channel_totals.py [--channel nba|fc]     (load Tools/.env first so YT_REFRESH_TOKEN[_FC] is set)

Prints, per channel: last 90 days and last 365 days by content type (Shorts vs long-form): views, watch hours, subscribers gained/lost; monthly
Shorts views for the last 6 months; and progress against the Partner Program lines (official page support.google.com/youtube/answer/72851):
1,000 subscribers AND (4,000 public long-form watch hours in 12 months OR 10,000,000 Shorts views in 90 days).
"""
import argparse, datetime, os, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yt_analytics as Y


def q(at, start, end, metrics, dims=None, extra=None):
    p = {"ids": "channel==MINE", "startDate": start, "endDate": end, "metrics": metrics}
    if dims:
        p["dimensions"] = dims
    p.update(extra or {})
    return Y.get("https://youtubeanalytics.googleapis.com/v2/reports?" + urllib.parse.urlencode(p), at)


def rows(res):
    cols = [c["name"] for c in res.get("columnHeaders", [])]
    return [dict(zip(cols, r)) for r in res.get("rows", [])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", choices=["nba", "fc"], default="nba")
    a = ap.parse_args()
    if a.channel == "fc":
        Y.REFRESH_ENV = "YT_REFRESH_TOKEN_FC"
        Y.TOKEN = Y.TOKEN.replace("yt_token.json", "yt_token_fc.json")
    at = Y.access_token()
    today = datetime.date.today() - datetime.timedelta(days=1)
    d90 = (today - datetime.timedelta(days=89)).isoformat()
    d365 = (today - datetime.timedelta(days=364)).isoformat()
    M = "views,estimatedMinutesWatched,subscribersGained,subscribersLost"
    out = {}
    for label, start in (("90 d", d90), ("365 d", d365)):
        try:
            r = rows(q(at, start, today.isoformat(), M, "creatorContentType"))
        except Exception as e:  # dimension not allowed for this channel: fall back to totals
            r = rows(q(at, start, today.isoformat(), M))
            for x in r:
                x["creatorContentType"] = "ALL"
        out[label] = r
        for x in r:
            print(f"{a.channel} {label:6} {x['creatorContentType']:>18}: views {x['views']:>10,}  watch hours {x['estimatedMinutesWatched']/60:>9,.0f}  subs +{x['subscribersGained']} -{x['subscribersLost']}")
    print("monthly Shorts views (last 6 months):")
    try:
        dd = rows(q(at, (today - datetime.timedelta(days=200)).isoformat(), today.isoformat(), "views,subscribersGained", "day", {"filters": "creatorContentType==shorts"}))
        agg = {}
        for x in dd:
            m_ = x["day"][:7]; v = agg.setdefault(m_, [0, 0]); v[0] += x["views"]; v[1] += x["subscribersGained"]
        for m_ in sorted(agg):
            print(f"   {m_}  shorts views {agg[m_][0]:>10,}  subs +{agg[m_][1]}")
    except Exception as e:
        print("   (monthly by type not available:", str(e)[:100], ")")
    sh90 = sum(x["views"] for x in out["90 d"] if x["creatorContentType"].lower() in ("shorts", "all"))
    lf365 = sum(x["estimatedMinutesWatched"] for x in out["365 d"] if x["creatorContentType"].lower() in ("videoondemand", "all")) / 60
    print(f"YPP check: Shorts views last 90 d = {sh90:,} of 10,000,000 ({sh90/1e5:.2f}%); long-form watch hours last 365 d = {lf365:,.0f} of 4,000")


if __name__ == "__main__":
    main()
