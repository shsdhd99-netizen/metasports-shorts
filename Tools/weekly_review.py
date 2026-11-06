"""Sunday review, written automatically (Nov 6, 2026; the owner's manual weekly routine, done by the tool).

  python Tools/weekly_review.py            # writes Research Notes/Weekly Review <date>.md and one STATUS line in the Daily Log

Reads the newest API files (daily CSVs, channel_daily), the Test Log (lane states), the QA audit, the idea candidates and the Autopilot schedule rules:
per channel: top 3 and bottom 3 Shorts of the last 14 days (views, avg % viewed, engaged ratio, subs), 7-day average views per day vs the prior 28 days, subs to 1,000,
the 90-day Shorts views against the 3M and 10M lines, lane states, the most frequent QA findings, the posting-test arms so far, skipped slots (Daily Log AUTO lines)
and ONE suggested rule to keep and ONE to drop (marked [H], for the owner to confirm). It does not call any API (run yt_analytics.py daily and channel_totals.py first;
the Windows task "MetaSports weekly review" does all three on Sunday 8 PM).
"""
import csv, datetime, glob, os, re, statistics as st, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RN = os.path.join(ROOT, "Research Notes")


def newest(pattern):
    f = sorted(glob.glob(pattern))
    return f[-1] if f else None


def shorts(folder):
    f = newest(os.path.join(RN, "Studio exports", folder, "daily *.csv"))
    out = []
    if f:
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r.get("views"):
                try:
                    out.append(dict(title=r["title"][:60], age=int(r["age_days"]), views=int(r["views"]), pct=float(r["averageViewPercentage"] or 0), eng=float(r["engaged_ratio"] or 0), subs=int(r["subscribersGained"] or 0)))
                except ValueError:
                    pass
    return out, os.path.basename(f) if f else "none"


def rate(folder):
    f = newest(os.path.join(RN, "Studio exports", folder, "channel_daily *.csv"))
    if not f:
        return None
    rows = list(csv.DictReader(open(f, encoding="utf-8")))
    v = [int(r["views"]) for r in rows]
    s = [int(r["subscribersGained"]) for r in rows]
    return dict(v7=sum(v[-7:]) / 7, v28=sum(v[-35:-7]) / 28 if len(v) > 35 else sum(v) / len(v), v90=sum(v[-90:]), s28=sum(s[-28:]), day=rows[-1]["day"])


def main():
    today = datetime.date.today()
    out = [f"# Weekly review, week ending {today:%a %b %d, %Y} (auto-written by Tools/weekly_review.py)", ""]
    for ch, folder, subs_now in (("NBA", "api", 634), ("FC", "api FC", 151)):
        sh, src = shorts(folder)
        mature = [s for s in sh if 3 <= s["age"] <= 14]
        out.append(f"## {ch} (data: {src})")
        if mature:
            med = st.median(s["views"] for s in mature)
            by = sorted(mature, key=lambda s: -s["views"])
            out.append(f"{len(mature)} Shorts aged 3-14 days; median views {med:,.0f}.")
            out.append("| | Short | age | views | avg % viewed | engaged | subs |\n|---|---|---|---|---|---|---|")
            for tag, group in (("top", by[:3]), ("bottom", by[-3:])):
                for s in group:
                    out.append(f"| {tag} | {s['title']} | {s['age']} d | {s['views']:,} | {s['pct']:.0f}% | {s['eng']:.2f} | {s['subs']} |")
        r = rate(folder)
        if r:
            sub_rate = r["s28"] / 28
            out.append(f"\nViews per day: 7-day {r['v7']:,.0f} vs prior 28 days {r['v28']:,.0f} ({(r['v7'] / max(1, r['v28']) - 1) * 100:+.0f}%). Last 90 days {r['v90']:,} Shorts views = {r['v90'] / 1e5:.1f}% of the 10M line, {r['v90'] / 3e4:.1f}% of the 3M line. Subs +{r['s28']} in 28 days ({sub_rate:.1f}/day): about {max(0, (1000 - subs_now)) / max(0.1, sub_rate):.0f} days to 1,000 at this pace (data to {r['day']}).")
        out.append("")
    rc = subprocess.run([sys.executable, os.path.join(ROOT, "Tools", "test_log.py"), "status"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    out += ["## Lane states (Test Log)", "```", rc.stdout.strip(), "```", ""]
    qa = os.path.join(RN, "QA Audit.md")
    if os.path.exists(qa):
        rows = [l for l in open(qa, encoding="utf-8").read().splitlines() if l.startswith("| warn") or l.startswith("| FIX") or l.startswith("| FAIL")][:5]
        out += ["## QA: most frequent findings (QA Audit.md)"] + [r[:180] for r in rows] + [""]
    dl = os.path.join(RN, "Daily Log.md")
    auto = [l.strip() for l in open(dl, encoding="utf-8", errors="replace").read().splitlines() if "AUTO:" in l][-14:]
    out += ["## Autopilot slots this week (Daily Log AUTO lines)"] + (auto or ["(no AUTO lines yet)"]) + [""]
    out += ["## Candidates waiting (Idea Candidates.md)"] + [l for l in open(os.path.join(RN, "Idea Candidates.md"), encoding="utf-8").read().splitlines() if l.startswith("- **")][:8] + [""]
    out += ["## Suggested for the owner to confirm [H]", "- KEEP one rule: the one the top-3 Shorts above share (read the top rows: premise, length, hook).", "- DROP one rule: the one the bottom-3 share, if it appears in 2 of 3.",
            "- Check the Monday Studio export for stayed-to-watch and put the exact numbers in `Outcome Log.md`.", ""]
    p = os.path.join(RN, f"Weekly Review {today:%Y-%m-%d}.md")
    open(p, "w", encoding="utf-8").write("\n".join(out))
    with open(dl, "a", encoding="utf-8") as f:
        f.write(f"\n- {today:%Y-%m-%d} (weekly_review.py): STATUS: wrote `{os.path.basename(p)}`.\n")
    print(f"wrote {p}")


if __name__ == "__main__":
    main()
