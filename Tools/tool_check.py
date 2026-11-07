r"""Tool health check (Nov 7, 2026): zero cost, about 30 s. Catches the kind of break that hid for days before
(test_log.py used a Python 3.12+ f-string, so on the cloud's Python 3.11 build_gate silently skipped the lane check).

  python Tools/tool_check.py            # compile every Tools/*.py, run the self-tests and read-only smoke runs; exit 1 on any FAIL
  python Tools/tool_check.py --quick    # compile + self-tests only

1. Compile: every Tools/*.py with the running Python (the cloud runs 3.11, the PC 3.14: run it on both).
2. Self-tests: edit_lint --selftest, and the shared anchor matcher (a mid-sentence repeat must warn, a missing anchor must FIX).
3. Smoke runs on the newest built Short of each channel (read-only): script_lint, precut_lint, anchor_shots --dry-run,
   lab.py predict, build.py status, test_log.py status, next_gap.py. A non-zero exit that is a verdict (a FIX line) is fine;
   a Python traceback is a FAIL.
Run it on Sundays with the weekly review, and after editing any tool.
"""
import argparse, glob, os, subprocess, sys, time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)


def newest(pattern):
    c = sorted(d for d in glob.glob(os.path.join(ROOT, pattern)) if os.path.exists(os.path.join(d, "words.json")) and os.path.exists(os.path.join(d, "cuts.json")))
    return c[-1] if c else None


def anchors_selftest():
    from anchors import starts_for
    W = lambda s, t0=0.0: [{"word": w, "start": t0 + i * 0.3, "end": t0 + i * 0.3 + 0.25} for i, w in enumerate(s.split())]
    words = W("Luka scored forty in six of his last seven games. Last night it was fifty-three.")
    st, pr = starts_for([{"clip": "A", "anchor": "Luka"}, {"clip": "B", "anchor": "Last"}], words)
    assert any(p.startswith("WARN") and "shot B" in p for p in pr), f"mid-sentence repeat not warned: {pr}"
    st, pr = starts_for([{"clip": "A", "anchor": "Luka"}, {"clip": "B", "anchor": "Last night"}], words)
    assert not pr and abs(st[1] - (words[10]["start"] - 0.03)) < 0.01, f"clean anchors misread: {st} {pr}"
    st, pr = starts_for([{"clip": "A", "anchor": "Luka"}, {"clip": "B", "anchor": "Kobe"}], words)
    assert any(p.startswith("FIX") for p in pr), "missing anchor not FIXed"
    return "anchors: 3 cases ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    fails, oks = [], 0
    files = sorted(glob.glob(os.path.join(HERE, "*.py")))
    for f in files:
        try:
            compile(open(f, encoding="utf-8-sig").read(), f, "exec")  # syntax only: writes no .pyc
            oks += 1
        except SyntaxError as e:
            fails.append(f"COMPILE {os.path.basename(f)} line {e.lineno}: {e.msg}")
    print(f"compile: {oks}/{len(files)} ok on Python {sys.version.split()[0]}")
    try:
        print("  " + anchors_selftest())
    except AssertionError as e:
        fails.append(f"SELFTEST anchors: {e}")
    r = subprocess.run([sys.executable, os.path.join(HERE, "edit_lint.py"), "--selftest"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    (fails.append(f"SELFTEST edit_lint: {(r.stdout + r.stderr).strip().splitlines()[-1:]}") if r.returncode else print("  edit_lint --selftest ok"))
    if not a.quick:
        nba, fc = newest("Productions/MetaSports/2026-*"), newest("Soccer Channel/Productions/2026-*")
        smoke = [("test_log.py", ["status", "nba"]), ("next_gap.py", ["nba"])]
        for F in (nba, fc):
            if F:
                smoke += [("script_lint.py", [os.path.join(F, "script.txt")]), ("precut_lint.py", ["--folder", F]),
                          ("anchor_shots.py", ["--folder", F, "--dry-run"]), ("lab.py", ["predict", "--folder", F]), ("build.py", ["status", F])]
        for tool, args in smoke:
            t = time.time()
            try:
                r = subprocess.run([sys.executable, os.path.join(HERE, tool)] + args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
                out = r.stdout + r.stderr
                bad = "Traceback (most recent call last)" in out
            except subprocess.TimeoutExpired:
                out, bad = "timed out after 300 s", True
            label = f"{tool} {os.path.basename(args[-1]) if args else ''}"[:70]
            if bad:
                fails.append(f"SMOKE {label}: {[l for l in out.strip().splitlines() if l.strip()][-1][:160]}")
            else:
                print(f"  ok  {label} ({time.time() - t:.1f} s)")
    for f in fails:
        print("FAIL " + f)
    print(f"tool_check: {'FAIL' if fails else 'PASS'} ({len(fails)} problem(s), {time.time() - t0:.0f} s)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
