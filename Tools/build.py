r"""One command per build stage (Nov 7, 2026; owner: "make processes more efficient, faster, and easier").

  python Tools/build.py status "<folder>"           # what is done, what is missing, the next command (zero cost)
  python Tools/build.py voice  "<folder>" [--takes 3] [--force]
        script gate (script_lint: stops on FIX, so no voice credits are spent on a script QA would fail)
        -> voice_take.py (records, checks, repairs, re-records) -> tighten_voice.py -> the lab's predicted score
  python Tools/build.py cut    "<folder>" [--verified] [--force]
        precut_lint (stops on FIX: missing anchors, no action in 3 s, overlay in the caption band, window past the source end...)
        -> cut_list.py (fills missing "len" from the anchors, cuts, writes shots.json + sources.csv with source links, draws the sheet)
  python Tools/build.py render "<folder>" [--keep-final]
        assemble.py by the channel rule (NBA: no music; FC: no music, plus a music version when music.json exists, while fc-music runs)
        -> DRAFT files named from UPLOAD.md -> cover.jpg -> qa_final.py (SHIP / FIX / HOLD) -> _hub/s.mp4 + _hub/prev.mp4 for the Hub
  python Tools/build.py all    "<folder>" --verified   # cut + render (never voice: that spends credits, so it is asked for by name;
                                                     # without --verified it stops after the cut so you LOOK at the sheet first)
Tested Nov 7 on a copy of #99 Luka: cut plan -> SHIP + Hub files in 89 s.

Every stage prints one line per step and the exact next command. Nothing is uploaded, scheduled or posted (owner rule).
The voice stage needs ELEVENLABS_API_KEY in the environment (cloud settings or Tools/.env on the PC); without it, it stops cleanly.
"""
import argparse, glob, json, os, re, subprocess, sys, time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PY = sys.executable
sys.path.insert(0, HERE)


def channel(F):
    return "fc" if "soccer channel" in os.path.abspath(F).lower().replace("\\", "/") else "nba"


def run(args, show=6, timeout=1800):
    """Run a tool; print its last lines; return (rc, output)."""
    t = time.time()
    r = subprocess.run([PY if a == "PY" else a for a in args], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
    out = (r.stdout or "") + (r.stderr or "")
    tail = [l for l in out.strip().splitlines() if l.strip()][-show:] if show else []
    name = os.path.basename(args[1]) if args[0] == "PY" else args[0]
    print(f"  [{name} {time.time() - t:.0f}s{' FAILED' if r.returncode else ''}]")
    for l in tail:
        print("    " + l[:220])
    return r.returncode, out


def env_key():
    if os.environ.get("ELEVENLABS_API_KEY"):
        return True
    p = os.path.join(HERE, ".env")  # PC: Tools/.env (never printed)
    if os.path.exists(p):
        for l in open(p, encoding="utf-8", errors="ignore"):
            if l.startswith("ELEVENLABS_API_KEY=") and l.split("=", 1)[1].strip():
                os.environ["ELEVENLABS_API_KEY"] = l.split("=", 1)[1].strip().strip('"')
                return True
    return False


def title_of(F):
    up = os.path.join(F, "UPLOAD.md")
    t = ""
    if os.path.exists(up):
        try:
            from yt_schedule import parse_card
            t = parse_card(up)[0]
        except Exception:
            t = ""
    if channel(F) == "fc" or not t or "placeholder" in t.lower():
        # FC drafts are named after the folder ("S19 Man United's ..."); NBA after the UPLOAD title
        base = os.path.basename(os.path.abspath(F))
        t = re.sub(r"^\d{4}-\d{2}-\d{2}\s+", "", base) if (channel(F) == "fc" or not t) else t
    t = re.sub(r"[^\w\s'&,.()!-]", "", t, flags=re.U)  # no emoji or path characters in a file name
    return re.sub(r"\s+", " ", t).strip()[:120]


def stage_voice(F, a):
    ch = channel(F)
    sp = os.path.join(F, "script.txt")
    if not os.path.exists(sp):
        raise SystemExit("voice: no script.txt yet (write it with the nba-short / story-short skill first)")
    if os.path.exists(os.path.join(F, "voice.mp3")) and not a.force:
        raise SystemExit("voice: voice.mp3 already exists; --force re-records it (old takes go to _voice_prev/). Next: build.py cut")
    print(f"1/4 script gate ({ch})")
    rc, out = run(["PY", os.path.join(HERE, "script_lint.py"), sp], show=0)
    for l in out.splitlines():
        if l.strip().startswith(("FIX", "WARN", "info", "PRE-VOICE")):
            print("    " + l.strip()[:220])
    if rc:
        raise SystemExit("voice: STOPPED before spending voice credits. Fix the FIX lines in script.txt, then run this again.")
    if not env_key():
        raise SystemExit("voice: no ELEVENLABS_API_KEY in the environment (cloud: environment settings; PC: Tools/.env). Stop at script + notes.")
    print("2/4 voice (voice_take.py: records, checks, repairs, re-records)")
    rc, out = run(["PY", os.path.join(HERE, "voice_take.py"), "--script", sp, "--takes", str(a.takes)], show=5, timeout=3600)
    if rc or not os.path.exists(os.path.join(F, "words.json")):
        raise SystemExit("voice: no passing take. Read voice_take.json, then retake_sentence.py --folder F --at <time> for 1-2 bad words")
    print("3/4 tighten (dead air out)")
    rc, _ = run(["PY", os.path.join(HERE, "tighten_voice.py"), "--folder", F], show=2)
    words = json.load(open(os.path.join(F, "words.json"), encoding="utf-8"))
    dur = words[-1]["end"] + 0.3
    lo, hi = (50, 59.5) if ch == "fc" else (18, 27)
    flag = "" if lo <= dur <= hi else f"  <-- outside {lo}-{hi} s: {'cut a sentence and use retake_sentence.py / tighten_voice --end-after' if dur > hi else 'add a beat'}"
    print(f"    voice runs {dur:.1f} s{flag}")
    print("4/4 predicted score")
    run(["PY", os.path.join(HERE, "lab.py"), "predict", "--folder", F], show=3)
    print(f'NEXT: write cuts_plan.json (anchors, kinds, why; no "len" needed), then: python Tools/build.py cut "{F}"')


def stage_cut(F, a):
    if not os.path.exists(os.path.join(F, "words.json")):
        raise SystemExit("cut: no words.json (voice first: build.py voice)")
    if not (os.path.exists(os.path.join(F, "cuts.json")) or os.path.exists(os.path.join(F, "cuts_plan.json"))):
        raise SystemExit("cut: no cuts_plan.json / cuts.json yet")
    print("1/2 pre-cut lint")
    rc, out = run(["PY", os.path.join(HERE, "precut_lint.py"), "--folder", F], show=25)
    if rc:
        raise SystemExit("cut: STOPPED before cutting. Fix the FIX lines in the cut plan, then run this again.")
    print("2/2 cut list (lengths from the anchors, cuts, shots.json, sources.csv, contact sheet)")
    args = ["PY", os.path.join(HERE, "cut_list.py"), "--folder", F] + (["--force"] if a.force else []) + (["--verified"] if a.verified else [])
    rc, out = run(args, show=4, timeout=3600)
    if rc:
        raise SystemExit("cut: cut_list failed (see above)")
    short = [l for l in out.splitlines() if "SHORT CLIP" in l]
    for l in short:
        print("    " + l.strip())
    if not a.verified:
        print(f'LOOK at _check/sheet.jpg (framing, the named person on screen, no logos), then: python Tools/build.py cut "{F}" --verified')
        return False
    print(f'NEXT: python Tools/build.py render "{F}"')
    return True


def fc_music_live():
    try:
        T = json.load(open(os.path.join(ROOT, "Research Notes", "Lab", "tests.json"), encoding="utf-8"))
        live = T.get("live", T.get("tests", []))
        return any(t.get("id") == "fc-music" and t.get("status", "live") == "live" for t in live)
    except Exception:
        return True


def stage_render(F, a):
    ch = channel(F)
    if not os.path.exists(os.path.join(F, "shots.json")):
        raise SystemExit("render: no shots.json (build.py cut first)")
    versions = [("no music", ["--no-music"])]
    if ch == "fc" and os.path.exists(os.path.join(F, "music.json")) and fc_music_live():
        versions.append(("music", []))
    style = ["--caption-style", "ahmed"] if ch == "fc" else []
    title = title_of(F)
    old = glob.glob(os.path.join(F, "DRAFT*.mp4"))
    made = []
    for i, (label, flags) in enumerate(versions, 1):
        print(f"{i}/{len(versions) + 2} render ({label})")
        out_name = "final_" + label.replace(" ", "") + ".mp4"
        rc, _ = run(["PY", os.path.join(HERE, "assemble.py"), "--folder", F, "--out-name", out_name] + flags + style, show=2, timeout=3600)
        src = os.path.join(F, out_name)
        if rc or not os.path.exists(src):
            raise SystemExit("render: assemble.py failed (see above)")
        made.append((label, src))
    for p in old:  # replaced by the new render (git keeps the old one in history)
        os.remove(p)
    drafts = []
    for label, src in made:
        dst = os.path.join(F, f"DRAFT - awaiting approval - {title} ({label}).mp4")
        if a.keep_final:
            import shutil
            shutil.copyfile(src, dst)
        else:
            os.replace(src, dst)
        drafts.append(dst)
    print("    " + "\n    ".join(os.path.basename(d) for d in drafts))
    if not os.path.exists(os.path.join(F, "cover.jpg")):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "0.3", "-i", drafts[0], "-frames:v", "1", "-q:v", "2", os.path.join(F, "cover.jpg")])
        print("    cover.jpg from frame 0.3 s")
    print(f"{len(versions) + 1}/{len(versions) + 2} final QA")
    rc, out = run(["PY", os.path.join(HERE, "qa_final.py"), F], show=8, timeout=3600)
    print(f"{len(versions) + 2}/{len(versions) + 2} Hub files")
    run(["PY", os.path.join(HERE, "hub_pack.py"), F, "--skip-qa"], show=1)
    prev = os.path.join(F, "_hub", "prev.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", drafts[0], "-c:v", "libx264", "-crf", "25", "-preset", "veryfast", "-vf", "scale=720:-2",
                    "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", prev])
    if os.path.exists(prev):
        print(f"    _hub/prev.mp4 {os.path.getsize(prev) / 2**20:.1f} MB (720p preview) + _hub/s.mp4 (full) to upload as Hub assets")
    m = re.search(r"VERDICT:\s*(\w+)", out)
    verdict = m.group(1) if m else "?"
    print(f"VERDICT {verdict}. LOOK at frame 1, every overlay and the last frame. NEXT: the Hub card + Post task, then commit (never post).")


def stage_status(F, a):
    ch = channel(F)
    has = lambda *n: all(os.path.exists(os.path.join(F, x)) for x in n)
    notes = open(os.path.join(F, "notes.md"), encoding="utf-8").read() if has("notes.md") else ""
    links = len(set(re.findall(r"https?://[^\s)|\]]+", notes)))
    drafts = glob.glob(os.path.join(F, "DRAFT*.mp4"))
    qa = {}
    if has("qa_final.json"):
        try:
            qa = json.load(open(os.path.join(F, "qa_final.json"), encoding="utf-8"))
        except Exception:
            qa = {}
    unverified = None
    if has("sources.csv"):
        import csv
        rows = list(csv.DictReader(open(os.path.join(F, "sources.csv"), encoding="utf-8-sig")))
        unverified = sum(1 for r in rows if not str(r.get("verified", "")).lower().startswith(("y", "t", "1")))
    steps = [
        ("script.txt", has("script.txt"), "write the script (nba-short / story-short skill)"),
        ("notes.md with 2+ source links", links >= 2, f"notes.md has {links} link(s): add the sources (claims table)"),
        ("UPLOAD.md", has("UPLOAD.md"), "write UPLOAD.md (title = line 1, tags via tags_fit.py)"),
        ("voice (voice.mp3 + words.json)", has("voice.mp3", "words.json"), f'python Tools/build.py voice "{F}"'),
        ("cut plan", has("cuts.json") or has("cuts_plan.json"), "write cuts_plan.json (anchor, kind, why per shot)"),
        ("clips + shots.json", has("shots.json") and bool(glob.glob(os.path.join(F, "clips", "*.mp4"))), f'python Tools/build.py cut "{F}"'),
        ("every clip verified", unverified == 0, f'LOOK at _check/sheet.jpg, then python Tools/build.py cut "{F}" --verified'),
        ("DRAFT render", bool(drafts), f'python Tools/build.py render "{F}"'),
        ("qa_final SHIP", qa.get("verdict") == "SHIP", f'fix: {"; ".join((qa.get("fail_list") or [])[:2]) or "run qa_final.py"}'),
    ]
    print(f"{os.path.basename(os.path.abspath(F))} ({ch.upper()})")
    nxt = None
    for name, ok, how in steps:
        print(f"  [{'x' if ok else ' '}] {name}")
        if not ok and nxt is None:
            nxt = how
    if qa:
        print(f"  QA {qa.get('verdict')} {qa.get('qa_score', '')}; predicted score {qa.get('predicted_score', '-')}")
    print("NEXT: " + (nxt or "Hub card + Post task; the queue (queue_rank.py --apply) gives it a slot"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=["status", "voice", "cut", "render", "all"])
    ap.add_argument("folder")
    ap.add_argument("--takes", type=int, default=3)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--verified", action="store_true")
    ap.add_argument("--keep-final", action="store_true", help="keep final_*.mp4 next to the DRAFT copies")
    a = ap.parse_args()
    F = os.path.abspath(a.folder)
    if not os.path.isdir(F):
        raise SystemExit(f"no folder {F}")
    t0 = time.time()
    if a.stage == "all":
        if stage_cut(F, a):  # render only after the sheet was looked at (qa_final holds unverified clips anyway)
            stage_render(F, a)
    else:
        {"status": stage_status, "voice": stage_voice, "cut": stage_cut, "render": stage_render}[a.stage](F, a)
    if a.stage != "status":
        print(f"(build.py {a.stage}: {time.time() - t0:.0f} s)")


if __name__ == "__main__":
    main()
