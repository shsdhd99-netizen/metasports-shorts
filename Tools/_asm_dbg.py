"""Assembles a MetaSports Short in CutWire Drift (free editor), fully automatic, no window needed.

Usage (from the Tools folder):
  python assemble.py --folder "..\\Productions\\MetaSports\\2026-09-28 01 Why LeBron Took a 92 Pay Cut"
  python assemble.py --folder "..." --music "C:\\path\\to\\beat.mp3"     # optional quiet music under the voice

The folder needs voice.mp3, words.json and captions.srt (made by voiceover.py) and a "clips" folder with
your footage (videos or pictures), named in shot-list order: 01.mp4, 02.mp4, 03.jpg...
Makes: final.mp4 (1080x1920, ready to upload), edit.drift (open it in Drift to tweak), preview_1-3.jpg, storyboard.jpg.
Shot rhythm: a new shot at each sentence, kept between 1.2 and 4.5 seconds (CoachClank's biggest Shorts cut every 2-4 s).

Optional files in the folder:
  shots.json    [{"clip": "01.mp4", "start": 0.0, "in": 0.4}, ...]   cuts synced to words ("in" = start inside the clip)
  sfx.json      [{"sfx": "swish", "at": 12.85, "gain": -14}, ...]    sound effects from Tools/sfx (see sfx/catalog.json)
  emphasis.json {"red": [...], "green": [...]}                        caption colours by hand (see captions.py)
Captions are burned in the MetaSports look (captions.py) unless you pick a Drift preset with --captions.
"""
import argparse, glob, json, os, queue, subprocess, sys, threading, time, base64

DRIFT = r"C:\Program Files\Drift\drift.exe"
W, H = 1080, 1920
MEDIA = (".mp4", ".mov", ".m4v", ".webm", ".mkv", ".jpg", ".jpeg", ".png")


class Drift:
    """Minimal MCP client for Drift's headless engine (JSON-RPC over stdin/stdout)."""
    def __init__(self):
        self.p = subprocess.Popen([DRIFT, "--headless"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        self.q, self.i = queue.Queue(), 0
        threading.Thread(target=lambda: [self.q.put(l) for l in iter(self.p.stdout.readline, b"")], daemon=True).start()
        self.rpc("initialize", {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "assemble", "version": "1"}})
        self._send({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def _send(self, o):
        self.p.stdin.write((json.dumps(o) + "\n").encode())
        self.p.stdin.flush()

    def rpc(self, method, params, timeout=180):
        self.i += 1
        self._send({"jsonrpc": "2.0", "id": self.i, "method": method, "params": params})
        while True:
            r = json.loads(self.q.get(timeout=timeout).decode("utf-8", "replace"))
            if r.get("id") == self.i:
                return r

    def tool(self, name, args=None):
        content = self.rpc("tools/call", {"name": name, "arguments": args or {}}).get("result", {}).get("content", [])
        return content

    def text(self, name, args=None):
        return json.loads(" ".join(c.get("text", "") for c in self.tool(name, args) if c.get("type") == "text") or "{}")

    def apply(self, *ops):
        r = self.text("apply", {"ops": [{"tool": t, "args": a} for t, a in ops]})
        if not r.get("ok"):
            raise SystemExit(f"Drift refused a step: {json.dumps(r)[:500]}")
        return [x.get("result", {}) for x in r.get("done", [])]

    def close(self):
        try:
            self.p.stdin.close()
            self.p.wait(timeout=20)
        except Exception:
            self.p.kill()


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                         capture_output=True, text=True).stdout.strip()
    return float(out or 0)


def shot_plan(words, total):
    """Shot start times: one per sentence, merged below 1.2 s and split above 4.5 s."""
    starts, new = [], True
    for w in words:
        if new:
            starts.append(w["start"])
        new = w["word"].rstrip('"\')').endswith((".", "?", "!", "…"))
    starts = [0.0] + [s for s in starts if s > 0.05] if starts else [0.0]
    bounds = starts + [total]
    shots = [[a, b] for a, b in zip(bounds, bounds[1:]) if b - a > 0.01]
    merged = []
    for s in shots:
        if merged and s[1] - s[0] < 1.2:
            merged[-1][1] = s[1]
        else:
            merged.append(s)
    if len(merged) > 1 and merged[-1][1] - merged[-1][0] < 1.2:
        merged[-2][1] = merged.pop()[1]
    final = []
    for a, b in merged:
        n = max(1, int((b - a) // 4.5) + (1 if (b - a) % 4.5 > 0.01 and b - a > 4.5 else 0))
        step = (b - a) / n
        final += [(a + k * step, a + (k + 1) * step) for k in range(n)]
    return final


def fill(w, h):
    a = w / h
    if a > W / H:
        fw, fh = H * a, H
    else:
        fw, fh = W, W / a
    return {"w": round(fw, 1), "h": round(fh, 1), "x": round((W - fw) / 2, 1), "y": round((H - fh) / 2, 1)}


HERE = os.path.dirname(os.path.abspath(__file__))


def sfx_inputs(folder, total):
    """[(path, at, gain_db, fade, len)] from sfx.json; names refer to Tools/sfx/<name>.wav."""
    p = os.path.join(folder, "sfx.json")
    if not os.path.exists(p):
        return []
    cat = json.load(open(os.path.join(HERE, "sfx", "catalog.json"), encoding="utf-8"))
    out = []
    for e in json.load(open(p, encoding="utf-8-sig")):
        name = e["sfx"]
        path = name if os.path.isabs(name) else os.path.join(HERE, "sfx", name if name.endswith(".wav") else name + ".wav")
        if not os.path.exists(path):
            print(f"  sound effect not found, skipped: {name}")
            continue
        gain = float(e.get("gain", cat.get(name.replace(".wav", ""), {}).get("gain", -16)))
        at = float(e["at"])
        if 0 <= at < total:
            out.append((path, at, gain, float(e.get("fade", 0) or 0), float(e.get("len", 0) or 0)))
    return out


def pick_music_start(path, total):
    """Start (whole seconds) of the loudest steady stretch of the track, skipping quiet intros: mean loudness of every window."""
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "8000", "-f", "s16le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    secs = len(x) // 8000
    if secs < int(total) + 4:
        return 0.0
    db = np.array([20 * np.log10(np.sqrt(np.mean(x[i * 8000:(i + 1) * 8000] ** 2)) + 1e-6) for i in range(secs)])
    n = int(total) + 1
    best, at = -1e9, 0
    for i in range(2, secs - n):
        m = db[i:i + n].mean() - 0.5 * db[i:i + n].std()  # loud AND steady
        if m > best:
            best, at = m, i
    return float(at)


def finish(folder, raw, final, total, style, music=None, music_db=-21.0, music_start=None, hook_text=None):
    """Burn MetaSports captions and mix sound effects in one ffmpeg pass, then previews + storyboard."""
    sys.path.insert(0, HERE)
    import captions
    ass, _ = captions.build(folder, style, total)
    fx = sfx_inputs(folder, total)
    vf = captions.filter_arg(ass, folder)
    if hook_text:  # big headline in the first ~2 s (curiosity gap), pops in over 0.15 s; "|" starts a new line
        font = os.path.join(HERE, "fonts", "Montserrat-Black.ttf").replace("\\", "/").replace(":", "\\:")
        for n, line in enumerate(l.strip() for l in hook_text.split("|")):
            esc = line.replace("\\", "\\\\").replace("'", "\u2019").replace(":", "\\:").replace("%", "\\%")
            vf += (f",drawtext=fontfile='{font}':text='{esc}':fontsize=104:fontcolor=white:borderw=9:bordercolor=black"
                   f":x=(w-text_w)/2:y={int(H * 0.15) + n * 120}:enable='between(t,0,2.1)':alpha='min(1,t/0.15)'")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", raw]
    parts, labels = [], ["[0:a]"]
    for k, (path, at, gain, fade, ln) in enumerate(fx, 1):
        cmd += ["-i", path]
        trim = f"atrim=0:{ln}," if ln else ""
        fo = f"afade=t=out:st={max(0.0, (ln or 3) - fade)}:d={fade}," if fade else ""
        ms = int(round(at * 1000))
        parts.append(f"[{k}:a]{trim}{fo}aformat=sample_rates=48000:channel_layouts=stereo,volume={gain}dB,adelay={ms}|{ms}[s{k}]")
        labels.append(f"[s{k}]")
    # Shorts play at about -14 LUFS and YouTube never turns quiet uploads up: measure, then lift the whole mix
    meas = subprocess.run(["ffmpeg", "-hide_banner", "-i", raw, "-af", "ebur128", "-f", "null", "-"],
                          capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    import re as _re
    found = _re.findall(r"I:\s+(-?[\d.]+) LUFS", meas)
    lift = max(-6.0, min(18.0, -14.0 - float(found[-1]))) if found else 0.0
    # Lift the VOICE to -14 LUFS first, then mix effects and music under it. (Lifting the finished mix instead made every effect
    # louder than a quiet voice: the "vine boom ruins it" bug.) Effect gains below are therefore relative to a loud voice.
    tail = "alimiter=limit=0.891:attack=3:release=60:level=disabled"
    parts.append(f"[0:a]volume={lift:.2f}dB[vlift]")
    labels[0] = "[vlift]"
    if music:
        ms0 = pick_music_start(music, total) if music_start is None else float(music_start)
        cmd += ["-ss", f"{ms0:.2f}", "-i", music]
        mi = len(fx) + 1
        # music sits well under the voice and ducks a further few dB whenever the voice speaks; fades in and out
        parts.append(f"[{mi}:a]aformat=sample_rates=48000:channel_layouts=stereo,atrim=0:{total:.2f},afade=t=in:d=0.4,"
                     f"afade=t=out:st={max(0.0, total - 1.6):.2f}:d=1.6,volume={music_db}dB[mus0]")
        parts.append("[vlift]asplit=2[vk][vmix]")
        parts.append("[mus0][vk]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=300[mus]")
        labels = ["[vmix]"] + labels[1:] + ["[mus]"]
        tail = "loudnorm=I=-14:TP=-1.5:LRA=7,alimiter=limit=0.891:attack=3:release=60:level=disabled"  # keep the whole mix at -14 LUFS
        print(f"  music: {os.path.basename(music)} from {ms0:.0f}s, {music_db} dB under the voice")
    if len(labels) > 1:
        parts.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,{tail}[a]")
    else:
        parts.append(f"[vlift]{tail}[a]")
    amap = ["-map", "[a]", "-c:a", "aac", "-b:a", "192k"]
    fc = f"[0:v]{vf}[v]" + (";" + ";".join(parts) if parts else "")
    tmp = os.path.join(folder, "_final_tmp.mp4")
    ok = False
    for enc in (["-c:v", "h264_nvenc", "-preset", "p6", "-rc", "vbr", "-cq", "18", "-b:v", "14M", "-maxrate", "20M"],
                ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast"]):
        r = subprocess.run(cmd + ["-filter_complex", fc, "-map", "[v]", *amap, *enc, "-pix_fmt", "yuv420p",
                                  "-movflags", "+faststart", tmp], cwd=folder, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        if r.returncode == 0 and os.path.exists(tmp) and duration(tmp) > total - 0.5:
            ok = True
            break
        print(f"  final pass with {enc[1]} failed: {(r.stderr or '')[:900]}")
    if not ok:
        raise SystemExit("Could not burn captions / mix sound effects (see the error above).")
    if os.path.exists(final):
        os.remove(final)
    os.replace(tmp, final)
    print(f"  captions burned ({style}) + {len(fx)} sound effect(s), voice lifted {lift:+.1f} dB to -14 LUFS, effects mixed under it")
    for n, at in enumerate((total * 0.2, total * 0.5, total * 0.8), 1):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{at:.2f}", "-i", final, "-frames:v", "1",
                        "-q:v", "3", os.path.join(folder, f"preview_{n}.jpg")])
    try:
        subprocess.run([sys.executable, os.path.join(HERE, "storyboard.py"), "--folder", folder, "--video", final,
                        "--style", style], capture_output=True, timeout=300)
    except Exception:
        pass


def ffmpeg_engine(folder, voice, shots, clips, ins, total, a, zooms=()):
    """No Drift (Linux/cloud): trim + scale/crop each shot with ffmpeg, concat, mux the voice, then finish()."""
    tmp = os.path.join(folder, "_shots_tmp")
    os.makedirs(tmp, exist_ok=True)
    parts = []
    k = 0
    for i, (start, end) in enumerate(shots):
        clip = clips[i % len(clips)]
        offset = ins[i] if i < len(ins) else 0.0
        want = end - start
        still = clip.lower().endswith((".jpg", ".jpeg", ".png"))
        vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps=30,format=yuv420p"
        z = float(zooms[i]) if i < len(zooms) and zooms[i] else 0.0
        if not z and getattr(a, "auto_zoom", 0) and not still and not os.path.basename(clip).lower().startswith(("c", "p_")):
            z = float(a.auto_zoom)  # gentle push-in on footage so no shot ever sits still (pattern interrupt)
        if z:  # punch-in: slow push from 100% to 100+z% over the shot (shots.json "zoom": 0.12), a pattern interrupt for hooks
            vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,"
                  f"scale=w='trunc({W}*(1+{z}*t/{max(want, 0.1):.3f})/2)*2':h='trunc({H}*(1+{z}*t/{max(want, 0.1):.3f})/2)*2':eval=frame,"
                  f"crop={W}:{H},setsar=1,format=yuv420p")
        out = os.path.join(tmp, f"s{k:03d}.mp4")
        if still:
            cmd = ["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", f"{want:.3f}", "-i", clip, "-vf", vf]
        else:
            cmd = ["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{offset:.3f}", "-stream_loop", "-1", "-i", clip, "-t", f"{want:.3f}", "-vf", vf]
        r = subprocess.run(cmd + ["-an", "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", out], capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(f"ffmpeg could not cut shot {i + 1} ({os.path.basename(clip)}): {r.stderr[-300:]}")
        parts.append(out)
        k += 1
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    raw = os.path.join(folder, "final_nocap.mp4")
    inputs = ["-f", "concat", "-safe", "0", "-i", lst, "-i", voice]
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", raw], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"ffmpeg concat failed: {r.stderr[-300:]}")
    final = os.path.join(folder, a.out_name)
    if a.captions == "burn":
        finish(folder, raw, final, total, a.caption_style, music=a.music, music_db=a.music_db, music_start=a.music_start, hook_text=(a.hook_text or (open(os.path.join(folder, "hook.txt"), encoding="utf-8").read().strip() if os.path.exists(os.path.join(folder, "hook.txt")) else None)) if os.environ.get("ALLOW_HOOK_TEXT") == "1" else None)
    else:
        os.replace(raw, final)
    import shutil
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"Done: {final} ({duration(final):.1f}s)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--folder", required=True)
    ap.add_argument("--music", help="optional music file, kept quiet and ducked under the voice")
    ap.add_argument("--music-db", dest="music_db", type=float, default=-21.0, help="music level under the voice, dB (default -21)")
    ap.add_argument("--music-start", dest="music_start", type=float, default=None, help="second of the track to start from (default: loudest steady stretch)")
    ap.add_argument("--hook-text", dest="hook_text", default=None, help='DISABLED by the user on Oct 4 2026 (captions only, no big headline); ignored unless env ALLOW_HOOK_TEXT=1')
    ap.add_argument("--auto-zoom", dest="auto_zoom", type=float, default=0.0, help="slow push-in on every footage shot, e.g. 0.06")
    ap.add_argument("--out-name", dest="out_name", default="final.mp4", help="output file name inside the folder")
    ap.add_argument("--captions", default="burn", help="burn (MetaSports look, default) or a Drift preset: subtitle, caption, hormozi, one-word-color")
    ap.add_argument("--caption-style", default="metasports", help="for --captions burn: metasports (old Shorts look), clank, or karaoke (Round 5 test)")
    ap.add_argument("--no-export", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    folder = os.path.abspath(a.folder)
    voice, words_p, srt = (os.path.join(folder, f) for f in ("voice.mp3", "words.json", "captions.srt"))
    missing = [os.path.basename(p) for p in (voice, words_p, srt) if not os.path.exists(p)]
    if missing:
        raise SystemExit(f"Missing {', '.join(missing)}. Make the voiceover first: python voiceover.py --script \"{os.path.join(folder, 'script.txt')}\"")
    clips_dir = os.path.join(folder, "clips")
    os.makedirs(clips_dir, exist_ok=True)
    clips = sorted(p for p in glob.glob(os.path.join(clips_dir, "*")) if p.lower().endswith(MEDIA))
    if not clips:
        raise SystemExit(f"Put your footage in {clips_dir} (named 01, 02, 03... in shot-list order), then run this again.")
    total = duration(voice)
    plan_p = os.path.join(folder, "shots.json")  # optional: [{"clip": "01.mp4", "start": 0.0}, ...] cuts synced to words
    if os.path.exists(plan_p):
        plan = json.load(open(plan_p, encoding="utf-8"))
        starts = [float(p["start"]) for p in plan] + [total]
        shots = [(starts[i], starts[i + 1]) for i in range(len(plan)) if starts[i + 1] > starts[i]]
        clips = [os.path.join(clips_dir, p["clip"]) for p in plan]
        ins = [float(p.get("in", 0) or 0) for p in plan]
        zooms = [float(p.get("zoom", 0) or 0) for p in plan]
        missing = [os.path.basename(c) for c in clips if not os.path.exists(c)]
        if missing:
            raise SystemExit(f"shots.json names clips that aren't in the clips folder: {', '.join(missing)}")
    else:
        shots = shot_plan(json.load(open(words_p, encoding="utf-8")), total)
        ins = [0.0] * len(shots)
        zooms = []
    print(f"Voice {total:.1f}s -> {len(shots)} shots from {len(set(clips))} clips")

    if not os.path.exists(DRIFT):
        print("Drift not found: using the ffmpeg engine")
        ffmpeg_engine(folder, voice, shots, clips, ins, total, a, zooms)
        return
    d = Drift()
    try:
        d.text("new_project")
        res = d.apply(("set_project_setup", {"width": W, "height": H, "fps": 30}),
                      ("import_media", {"paths": [voice] + clips + ([os.path.abspath(a.music)] if a.music else [])}))
        assets = {os.path.normcase(os.path.basename(x["name"])): x for x in res[1]["assets"]}
        aid = lambda p: assets[os.path.normcase(os.path.basename(p))]["id"]
        track = None
        for k, (start, end) in enumerate(shots):
            clip, t = clips[k % len(clips)], start
            offset = ins[k] if k < len(ins) else 0.0
            while end - t > 0.05:
                args = {"asset": aid(clip), "at": round(t, 3)}
                if track is not None:
                    args["track"] = track
                placed = d.apply(("place_clip", args))[0]
                track = placed["track"]
                want = round(end - t, 3)
                is_still = clip.lower().endswith((".jpg", ".jpeg", ".png"))
                got = d.apply(("set_duration" if is_still else "set_trim",
                               {"clip": placed["id"], "duration": want} if is_still else
                               {"clip": placed["id"], "in": round(offset, 3), "out": round(offset + want, 3)}))[0]
                offset = 0.0  # a looped repeat starts from the top
                d.apply(("seek", {"at": round(t, 3)}), ("set_transform", dict(clip=placed["id"], **fill(placed["w"], placed["h"]))))
                t += max(0.05, float(got.get("dur", want)))
        v = d.apply(("place_clip", {"asset": aid(voice), "at": 0, "new_track": True}))[0]
        d.apply(("normalize_volume", {"clip": v["id"], "target_lufs": -14}))
        if a.music:
            m = d.apply(("place_clip", {"asset": aid(a.music), "at": 0, "new_track": True}))[0]
            d.apply(("set_duration", {"clip": m["id"], "duration": round(total, 3)}), ("set_volume", {"clip": m["id"], "value": 0.3}))
            d.apply(("duck_under", {"clip": m["id"], "over_clips": [v["id"]], "amount": 0.35, "attack": 0.1, "release": 0.3}))
        burn = a.captions == "burn"
        if not burn:
            sub = d.apply(("import_subtitle_file", {"path": srt, "at": 0}))[0]
            steps = [("apply_text_preset", {"clip": sub["id"], "preset": a.captions}),
                     ("set_duration", {"clip": sub["id"], "duration": round(total, 3)})]
            if a.captions == "subtitle":  # CoachClank look: white, bold-ish, soft shadow, no box, centred
                steps.append(("set_text", {"clip": sub["id"], "style": {
                    "boxEnabled": False, "color": "#FFFFFFFF", "fontWeight": 700, "pixelSize": 62, "outlineEnabled": False,
                    "shadowEnabled": True, "shadowColor": "#FF000000", "shadowOpacity": 0.85, "shadowBlur": 10,
                    "shadowOffsetX": 0, "shadowOffsetY": 3}}))
            styled = [r for r in d.apply(*steps) if r.get("h")]
            box_h = styled[-1]["h"] if styled else 300
            d.apply(("seek", {"at": 0}), ("set_transform", {"clip": sub["id"], "y": round((H - box_h) / 2, 1)}))
            for n, at in enumerate((total * 0.2, total * 0.5, total * 0.8), 1):
                for c in d.tool("capture", {"at": round(at, 2)}):
                    if c.get("type") == "image":
                        open(os.path.join(folder, f"preview_{n}.jpg"), "wb").write(base64.b64decode(c["data"]))
        d.apply(("save_project", {"path": os.path.join(folder, "edit.drift")}))
        if not a.no_export:
            final = os.path.join(folder, "final.mp4")
            out = os.path.join(folder, "final_nocap.mp4") if burn else final
            # NVIDIA encoder first (fast even when the PC is busy), then x264 veryfast as a fallback
            for enc in ({"video": "h264_nvenc", "rate": "bitrate", "bitrate": 14000},
                        {"video": "h264", "crf": 18, "preset": "veryfast"}):
                if os.path.exists(out):
                    os.remove(out)
                d.apply(("export_video", {"path": out, "audio": "aac", "audio_bitrate": 192, "fps": 30,
                                          "in": 0, "out": round(total, 3), **enc}))
                started, last = time.time(), -1
                while time.time() - started < 3600:
                    state = d.text("inspect", {}).get("export", {})
                    if not state.get("active"):
                        break
                    pct = int(100 * float(state.get("progress") or 0))
                    if pct // 20 != last // 20:
                        print(f"  exporting ({enc['video']}): {pct}%")
                        last = pct
                    time.sleep(2)
                if os.path.exists(out) and duration(out) > total - 0.5:
                    break
                print(f"  {enc['video']} export failed, trying the next encoder")
            if burn and os.path.exists(out) and duration(out) > total - 0.5:
                finish(folder, out, final, total, a.caption_style)
                out = final
            print(f"Done: {out} ({duration(out):.1f}s)" if os.path.exists(out) and duration(out) > 0
                  else "Export did not finish; open edit.drift in Drift and export from there.")
        print(f"Project: {os.path.join(folder, 'edit.drift')} (open it in Drift to tweak) · previews: preview_1-3.jpg")
    finally:
        d.close()


if __name__ == "__main__":
    main()
