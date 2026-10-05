"""ElevenLabs voiceover + word-timed captions for MetaSports Shorts.

Usage (from the Tools folder):
  python voiceover.py --check                       # shows your ElevenLabs characters left
  python voiceover.py --list-voices                 # lists voices in your account
  python voiceover.py --script "path\\script.txt"   # makes voice.mp3 + captions.srt next to the script
  python voiceover.py --script ... --dry-run        # checks the script, no credits used

Pronunciations: write {Giannis|YAH-nis} in the script. The voice says the right side,
captions show the left side.

Needs Tools/.env with ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID (see .env.example).
"""
import argparse, base64, json, os, re, shutil, subprocess, sys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://api.elevenlabs.io/v1"


def load_env():
    env = {}
    p = os.path.join(HERE, ".env")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"')
    for k in ("ELEVENLABS_API_KEY", "ELEVENLABS_VOICE_ID"):
        env.setdefault(k, os.environ.get(k, ""))
    return env


def call(path, key, payload=None):
    req = urllib.request.Request(API + path, method="POST" if payload is not None else "GET",
                                 headers={"xi-api-key": key, "Content-Type": "application/json"},
                                 data=json.dumps(payload).encode() if payload is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ElevenLabs error {e.code}: {e.read().decode()[:400]}")


def parse_script(raw):
    """Split into segments: (display, spoken). {A|B} means show A, say B."""
    raw = re.sub(r"\s+", " ", raw.strip())
    segs, pos = [], 0
    for m in re.finditer(r"\{([^|{}]+)\|([^{}]+)\}", raw):
        if m.start() > pos:
            segs.append((raw[pos:m.start()], raw[pos:m.start()]))
        segs.append((m.group(1).strip(), m.group(2).strip()))
        pos = m.end()
    if pos < len(raw):
        segs.append((raw[pos:], raw[pos:]))
    return segs


def words_from_alignment(al):
    """Group character timings into words: [(word, start, end)]."""
    words, cur, start, end = [], "", None, None
    for ch, s, e in zip(al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]):
        if ch.isspace():
            if cur:
                words.append((cur, start, end))
            cur, start = "", None
            continue
        if start is None:
            start = s
        cur += ch
        end = e
    if cur:
        words.append((cur, start, end))
    return words


def map_display(segs, spoken_words):
    """Swap spoken respellings back to display words for captions."""
    out, i = [], 0
    for disp, spok in segs:
        n = len(spok.split())
        chunk = spoken_words[i:i + n]
        i += n
        if not chunk:
            continue
        if disp == spok:
            out.extend(chunk)
        else:
            out.append((disp, chunk[0][1], chunk[-1][2]))
    out.extend(spoken_words[i:])
    return out


def tidy(words):
    """Glue stand-alone punctuation (".", ",", "…") onto the word before it and drop any byte-order mark."""
    out = []
    for w, s, e in words:
        w = w.replace("﻿", "")
        if not w:
            continue
        if out and not any(c.isalnum() for c in w):
            pw, ps, _ = out[-1]
            out[-1] = (pw + w, ps, e)
        else:
            out.append((w, s, e))
    return out


# Trailing function words that should not end a caption card alone when avoidable.
_DANGLING = {"the", "a", "an", "from", "of", "to", "and", "or", "but", "in", "on", "at",
             "for", "with", "by", "as", "is", "are", "was", "were", "be", "it's", "its",
             "so", "that", "this", "than", "into", "onto", "off", "not", "some", "most",
             "every", "here's", "which", "you", "see", "vs", "via"}


def to_srt(words, max_words=4, max_chars=28):
    """Chunk word timings into natural 2-4 word Clank-style phrase cards.

    Prefer intact phrases ("from 15 feet", "13 feet 9"). Never end a card on a
    dangling article/preposition alone if the next word can still fit. Keep
    sentence endings as hard breaks. Always join with a real ASCII space.
    """
    def ts(t):
        h, rem = divmod(max(t, 0), 3600)
        m, s = divmod(rem, 60)
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"

    def bare(w):
        return re.sub(r"[^A-Za-z0-9']+", "", w).lower()

    def ends_sentence(w):
        return bool(w) and w.rstrip("\"')")[-1:] in ".?!"

    def text_of(group):
        return " ".join(x[0] for x in group)

    # Greedy pack: grow until soft target, then only extend to avoid dangling ends
    # or to finish a short measure phrase / sentence.
    MEASURE_TAIL = {"feet", "foot", "inches", "inch", "9", "15", "13", "6", "18"}
    lines, i, n = [], 0, len(words)
    while i < n:
        group = [words[i]]
        i += 1
        while i < n and not ends_sentence(group[-1][0]):
            nxt = words[i]
            trial = group + [nxt]
            t = text_of(trial)
            over = len(trial) > max_words or len(t) > max_chars
            dangling = bare(group[-1][0]) in _DANGLING
            # Always pull if we would otherwise end dangling and next still fits soft hard-cap
            if dangling and len(trial) <= max_words + 1 and len(t) <= max_chars + 8:
                group.append(nxt)
                i += 1
                continue
            if over:
                break
            # Under soft size (prefer at least 2, grow toward 3)
            if len(group) < 3:
                group.append(nxt)
                i += 1
                continue
            # At 3 words: pull one more only for sentence end or measure completion
            if len(group) == 3 and (ends_sentence(nxt[0]) or bare(nxt[0]) in MEASURE_TAIL):
                group.append(nxt)
                i += 1
                break
            break
        lines.append(group)

    # Pass 2: merge orphan 1-word cards into previous; pull dangling-end + next first word
    fixed = []
    for g in lines:
        if fixed and len(g) == 1 and not ends_sentence(fixed[-1][-1][0]):
            # merge short "part." / "basket." onto previous when previous ends mid-phrase-y
            prev_last = bare(fixed[-1][-1][0])
            if prev_last in _DANGLING or prev_last in {"weird", "free", "shot", "middle", "two"}:
                if len(fixed[-1]) + 1 <= max_words + 1 and len(text_of(fixed[-1] + g)) <= max_chars + 6:
                    fixed[-1].extend(g)
                    continue
        if fixed and bare(fixed[-1][-1][0]) in _DANGLING and not ends_sentence(fixed[-1][-1][0]):
            # steal first word of this card
            if len(fixed[-1]) + 1 <= max_words + 1 and len(text_of(fixed[-1] + [g[0]])) <= max_chars + 8:
                fixed[-1].append(g[0])
                g = g[1:]
                if not g:
                    continue
        fixed.append(g)
    lines = fixed

    # Pass 3: glue orphan measure/number cards ("9.") onto previous
    glued = []
    for g in lines:
        if glued and len(g) == 1 and re.fullmatch(r"[\d]+[.!?]?", g[0][0].strip()):
            glued[-1].extend(g)
        elif glued and len(glued[-1]) >= 2 and bare(glued[-1][-1][0]) in {"free"} and bare(g[0][0]) == "throw":
            # keep "free throw" together across card boundary
            take = 1
            glued[-1].extend(g[:take])
            rest = g[take:]
            if rest:
                glued.append(rest)
        else:
            glued.append(g)
    lines = glued

    out = []
    for n_, g in enumerate(lines, 1):
        end = lines[n_][0][1] if n_ < len(lines) else g[-1][2]
        out.append(f"{n_}\n{ts(g[0][1])} --> {ts(max(end, g[-1][2]))}\n{text_of(g)}\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", help="path to a .txt/.md script (only the spoken text)")
    ap.add_argument("--voice-id")
    ap.add_argument("--model", default="eleven_multilingual_v2")
    ap.add_argument("--speed", default="auto", help="ElevenLabs native speed 0.7-1.2, or auto. Our cloned voice reads ~210 wpm at 1.1, ~238 at 1.15, ~268 at 1.2 (Oct 5 2026 lab). auto = the fastest of 1.2/1.15/1.1 that still gives a take of at least --min-secs, so no time-stretch is needed")
    ap.add_argument("--min-secs", type=float, default=22.5, help="auto speed keeps the narration at least this long (the 21-30 s sweet spot)")
    ap.add_argument("--stability", type=float, default=0.65, help="0.65 (Oct 5 2026 voice lab). 0.45 gave the glitchier takes on the cloned voice")
    ap.add_argument("--similarity", type=float, default=0.7, help="0.7 = the voice's own saved setting")
    ap.add_argument("--target-wpm", type=int, default=250, help="speed audio up to about this pace with atempo, but never more than --max-stretch (0 = off)")
    ap.add_argument("--max-stretch", type=float, default=1.08, help="time-stretching lowers voice quality (HNR -0.5..-1.1 dB at x1.2-1.4); above this we warn instead")
    ap.add_argument("--legacy", action="store_true", help="old settings (speed 1.1, stability 0.45, similarity 0.8, stretch up to x1.6)")
    ap.add_argument("--prev-text", default="", help="text spoken just before this piece (keeps tone/pace continuous across spliced pieces)")
    ap.add_argument("--next-text", default="", help="text spoken just after this piece")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list-voices", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.legacy:
        a.speed, a.stability, a.similarity, a.max_stretch = 1.1, 0.45, 0.8, 1.6
    env = load_env()
    key = env.get("ELEVENLABS_API_KEY", "")

    if a.list_voices or a.check:
        if not key:
            raise SystemExit("Add your ELEVENLABS_API_KEY to Tools/.env first (copy .env.example).")
        if a.check:
            s = call("/user/subscription", key)
            print(f"Characters used: {s.get('character_count')} of {s.get('character_limit')} (plan: {s.get('tier')})")
        if a.list_voices:
            for v in call("/voices", key).get("voices", []):
                print(f"{v['name']:<28} {v['voice_id']}  [{v.get('category', '')}]")
        return

    if not a.script:
        raise SystemExit("Give --script path")
    raw = open(a.script, encoding="utf-8-sig").read()
    segs = parse_script(raw)
    spoken = " ".join(s for _, s in segs).strip()
    n_words = len(" ".join(d for d, _ in segs).split())
    print(f"{n_words} words · {len(spoken)} characters (ElevenLabs bills ~1 credit per character)")
    print(f"At {a.target_wpm or 250} wpm that's about {n_words / (a.target_wpm or 250) * 60:.0f} seconds.")
    if a.dry_run:
        return
    voice = a.voice_id or env.get("ELEVENLABS_VOICE_ID")
    if not key or not voice:
        raise SystemExit("Missing ELEVENLABS_API_KEY or ELEVENLABS_VOICE_ID in Tools/.env")

    if str(a.speed).lower() == "auto":
        est = lambda sp: n_words / (210 + (sp - 1.1) * 580) * 60  # rough reading time of the spoken words at native speed sp
        a.speed = next((sp for sp in (1.2, 1.15) if est(sp) >= a.min_secs), 1.1)
        print(f"auto speed -> {a.speed} (about {est(a.speed):.1f} s for {n_words} words)")
    a.speed = float(a.speed)
    settings = {"stability": a.stability, "similarity_boost": a.similarity, "use_speaker_boost": True}
    if abs(a.speed - 1.0) > 1e-6:
        settings["speed"] = max(0.7, min(1.2, a.speed))
    body = {"text": spoken, "model_id": a.model, "voice_settings": settings}
    if a.prev_text:
        body["previous_text"] = a.prev_text
    if a.next_text:
        body["next_text"] = a.next_text
    res = call(f"/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128", key, body)
    out_dir = os.path.dirname(os.path.abspath(a.script))
    raw_mp3 = os.path.join(out_dir, "voice_raw.mp3")
    open(raw_mp3, "wb").write(base64.b64decode(res["audio_base64"]))
    words = words_from_alignment(res.get("alignment") or res["normalized_alignment"])
    dur = words[-1][2] if words else 0
    factor = 1.0
    if a.target_wpm and dur:
        raw_wpm = len(words) / (dur / 60)
        want = a.target_wpm / raw_wpm
        factor = max(1.0, min(a.max_stretch, want))
        print(f"Raw pace {raw_wpm:.0f} wpm; wanted x{want:.2f} stretch, using x{factor:.2f}" + ("  (script is long for this voice speed: shorten it or accept a slower read)" if want > a.max_stretch + 0.01 else ""))
    final = os.path.join(out_dir, "voice.mp3")
    # always end with 0.3 s of silence so the last word is never cut off (qa_short fails a voice that ends <0.1 s before the end)
    if shutil.which("ffmpeg"):
        stretch = f"atempo={factor:.3f}," if factor > 1.01 else ""
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw_mp3, "-filter:a", stretch + "apad=pad_dur=0.3", "-c:a", "libmp3lame", "-q:a", "0", final], check=True)
        if factor > 1.01:
            words = [(w, s / factor, e / factor) for w, s, e in words]
        else:
            factor = 1.0
    else:
        shutil.copyfile(raw_mp3, final)
        factor = 1.0
    words = tidy(map_display(segs, words))
    open(os.path.join(out_dir, "captions.srt"), "w", encoding="utf-8").write(to_srt(words))
    json.dump([{"word": w, "start": round(s, 3), "end": round(e, 3)} for w, s, e in words],
              open(os.path.join(out_dir, "words.json"), "w", encoding="utf-8"), indent=1)
    secs = words[-1][2] if words else 0
    print(f"Done: voice.mp3 ({secs:.1f}s, sped up x{factor:.2f}) + captions.srt + words.json in {out_dir}")


if __name__ == "__main__":
    main()
