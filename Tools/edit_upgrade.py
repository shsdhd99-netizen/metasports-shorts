"""Opt-in editing upgrades (Nov 3, 2026; to-do item 11, from Research Notes/Editing Study (Nov 1, 2026).md). Never touches a live Short.

  python Tools/edit_upgrade.py --folder "<Short folder>" --demo "<new DEMO folder>"   # build the DEMO folder, cut, assemble
  python Tools/edit_upgrade.py --folder "<Short folder>" --demo "<DEMO folder>" --plan-only   # just write the upgraded cuts.json

It copies the voice, words, captions, script and cuts.json to a DEMO folder (the name must contain "DEMO"), rewrites the DEMO's
cuts.json with these fixes, re-cuts the clips (cut_list.py --force), and renders it with assemble.py (ffmpeg engine, no music).
Fixes (each one flagged by Tools/edit_lint.py before, expected clean after):
  1. BIGGER SUBJECT IN FRAME 1: a WIDE blurfit shot (note says wide, not close-up) in the first 3 s with zoom under 1.3 gets zoom 1.5 (the subject was about 15% of the frame).
  2. SCOREBUG KEPT WHOLE: a shot whose note cites the scorebug/clock and uses a 3:4 window gets blurfit_aspect 0 (whole 16:9 frame in
     the band). In the first 3 s (fix 1 wins) the bug claim is left alone and reported: check that frame by eye.
  3. NO SHOT HELD OVER 3.0 s: a longer shot is split into two halves of the same clip, the second at a tighter zoom (+0.25) and a
     shifted window, so the picture changes while the play continues. Extra part clips are named <clip>b.
Not done here (needs a look at the frames, listed in the Editing Study): caption position off the players (captions.py) and a
static ending beyond the split rule.
"""
import argparse, copy, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KEEP = ["voice.mp3", "words.json", "captions.srt", "captions.ass", "script.txt", "sfx.json", "voice_take.json"]


def upgrade(cuts, words=(), starts=None):
    notes, out, t = [], [], 0.0
    starts = starts or {}
    for s in cuts["shots"]:
        s = copy.deepcopy(s)
        ln = float(s.get("len") or 0)
        why = str(s.get("why", "")).lower()
        bug = any(k in why for k in ("scorebug", "score bug", "clock", " bug"))
        in_hook = t < 3.0
        if in_hook and s.get("blurfit") and float(s.get("zoom") or 1.0) < 1.3 and "wide" in why and "close" not in why:  # a close-up is already big (B01 lost his face at 1.5)
            s["zoom"] = 1.5
            notes.append(f"{s['clip']}: hook shot zoom -> 1.5 (bigger subject in frame 1)")
            if bug:  # a 1.5 zoom crops the bug: the score must reach the viewer another way (on-screen text), so stop citing the bug
                s["why"] = re.sub(r"score ?bug|clock", "score", str(s["why"]), flags=re.I) + " [zoomed hook, score carried by on-screen text]"
                notes.append(f"{s['clip']}: its note cited the scorebug; the 1.5 zoom crops it, so the note now says the score is carried by on-screen text (check the overlay)")
        elif bug and s.get("blurfit") and float(s.get("blurfit_aspect") or 1.0) < 1.0:
            s["blurfit_aspect"] = 0
            notes.append(f"{s['clip']}: blurfit_aspect 0 (whole frame, scorebug kept whole)")
        if ln > 3.0 and s.get("src"):
            h = round(ln / 2, 2)
            a, b = copy.deepcopy(s), copy.deepcopy(s)
            a["len"], b["len"] = h, round(ln - h, 2)
            b["clip"] = s["clip"] + "b"
            b["at"] = round(float(s.get("at", 0)) + h * float(s.get("speed", 1) or 1), 3)
            b["zoom"] = round(float(s.get("zoom") or 1.0) + 0.25, 2)
            b["x"] = round(min(0.9, max(0.1, float(s.get("x", 0.5)) + 0.05)), 3)
            for k in ("anchor", "overlay", "nat_at", "lead"):
                b.pop(k, None)
            st = starts.get(s["clip"])  # pin part b to the words spoken at the split point (anchor_shots needs an anchor or a start)
            if st is not None and words:
                mid = st + h
                i = next((j for j, w in enumerate(words) if w["start"] >= mid - 0.02), None)
                if i is not None:
                    b["anchor"] = " ".join(w["word"] for w in words[i:i + 2])
                    b["lead"] = round(max(0.0, words[i]["start"] - mid), 2)
            if "overlay" in a:  # keep the overlay on the first half; shorten its window if it ran past it
                for o in a["overlay"]:
                    o["end"] = min(float(o.get("end", h)), h)
            out += [a, b]
            notes.append(f"{s['clip']}: {ln:.2f} s split into {h} s + {b['len']} s ({b['clip']} at zoom {b['zoom']})")
        else:
            out.append(s)
        t += ln
    cuts = dict(cuts)
    cuts["shots"] = out
    return cuts, notes


def run(cmd):
    print("  $", " ".join(f'"{c}"' if " " in c else c for c in cmd))
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print((r.stdout + r.stderr).strip()[-1200:])
    return r.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True, help="the original Short folder (read only)")
    ap.add_argument("--demo", required=True, help="new folder; its name must contain DEMO")
    ap.add_argument("--plan-only", action="store_true")
    a = ap.parse_args()
    if "DEMO" not in os.path.basename(os.path.abspath(a.demo)):
        sys.exit("Refused: the output folder name must contain DEMO (never overwrite or swap a live Short).")
    if os.path.abspath(a.demo) == os.path.abspath(a.folder):
        sys.exit("Refused: --demo must be a different folder.")
    os.makedirs(a.demo, exist_ok=True)
    for f in KEEP:
        if os.path.exists(os.path.join(a.folder, f)):
            shutil.copy2(os.path.join(a.folder, f), os.path.join(a.demo, f))
    cuts = json.load(open(os.path.join(a.folder, "cuts.json"), encoding="utf-8"))
    words = json.load(open(os.path.join(a.folder, "words.json"), encoding="utf-8"))
    sp = os.path.join(a.folder, "shots.json")
    starts = {x["clip"].split(".")[0]: float(x["start"]) for x in json.load(open(sp, encoding="utf-8")) if "start" in x} if os.path.exists(sp) else {}
    new, notes = upgrade(cuts, words, starts)
    json.dump(new, open(os.path.join(a.demo, "cuts.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("\n".join(notes) or "nothing to upgrade")
    if a.plan_only:
        return
    src_dir = os.path.join(a.demo, "src")
    for k, v in cuts.get("sources", {}).items():  # reuse the original's source if it is on disk, else it must be downloaded first
        p = os.path.join(a.folder, v)
        if os.path.exists(p):
            os.makedirs(src_dir, exist_ok=True)
            shutil.copy2(p, os.path.join(a.demo, v))
    py = sys.executable
    if run([py, os.path.join(HERE, "cut_list.py"), "--folder", a.demo, "--force"]):
        sys.exit("cut_list.py failed (is the source video in <demo>/src? download it with x_clip.py).")
    sys.exit(run([py, os.path.join(HERE, "assemble.py"), "--folder", a.demo, "--engine", "ffmpeg", "--no-music",
                  "--out-name", "final.mp4"]))


if __name__ == "__main__":
    main()
