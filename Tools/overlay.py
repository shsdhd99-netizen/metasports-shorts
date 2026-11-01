"""Words/numbers over real footage (no static card, no picture).

Usage:
  python overlay.py --in clips/S7.mp4 --out clips/S7o.mp4 --spec spec.json
spec.json is a list of lines:
  {"text": "50.7%", "size": 190, "color": "orange", "y": 300, "start": 0.0, "end": 1.5, "sub": "LeBron"}
- y is the TOP of the text in a 1920-high frame. Keep text above y=1000 (captions sit at about 55-65% of the height)
  or below y=1300.
- "sub" is an optional small white label above the number.
- Text pops in (0.12 s fade) and out (0.12 s fade); thick black outline keeps it readable on any footage.
- Oct 26 2026 (countdown format): "x": "left" | "right" | a pixel number puts the text in a corner instead of the centre,
  and "box": "0xFDB927" draws a solid badge behind it (e.g. {"text": "#3", "size": 120, "x": "left", "y": 230, "box": "0xFDB927",
  "color": "black", "start": 0, "end": 9}) for a visible 3-2-1 counter.
Needs ffmpeg with drawtext. Font: Windows Arial Bold.
"""
import argparse, json, os, subprocess, tempfile

FONT = "C\\:/Windows/Fonts/arialbd.ttf"
if not os.path.exists("C:/Windows/Fonts/arialbd.ttf"):  # cloud/Linux: Liberation Sans Bold has Arial's metrics
    FONT = os.environ.get("OVERLAY_FONT", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf")
COL = {"white": "white", "orange": "0xFF7A28", "grey": "0xC8D2E6", "red": "0xFF4A3A", "green": "0x4CD07D"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--spec", required=True)
    a = ap.parse_args()
    lines = json.load(open(a.spec, encoding="utf-8-sig"))
    tmp = tempfile.mkdtemp()
    filt = []
    for i, ln in enumerate(lines):
        st, en = float(ln.get("start", 0)), float(ln["end"])
        fade = 0.12
        alpha = f"if(lt(t,{st}),0,if(lt(t,{st + fade}),(t-{st})/{fade},if(lt(t,{en - fade}),1,if(lt(t,{en}),({en}-t)/{fade},0))))"
        for key, size_default, color_default, dy in (("sub", 62, "white", -(ln.get('size', 160) * 0.62 + 20)), ("text", ln.get("size", 160), ln.get("color", "white"), 0)):
            if key not in ln:
                continue
            tf = os.path.join(tmp, f"t{i}{key}.txt")
            open(tf, "w", encoding="utf-8").write(ln[key])
            size = ln.get("subsize", size_default) if key == "sub" else size_default
            color = COL.get(ln.get("subcolor", "white"), "white") if key == "sub" else COL.get(color_default, color_default)
            y = int(ln.get("y", 300) + dy)
            tfp = tf.replace("\\", "/").replace(":", "\\:")
            xs = ln.get("x", "center")
            xe = {"left": "70", "right": "w-text_w-70", "center": "(w-text_w)/2"}.get(xs, str(xs))
            box = (f":box=1:boxcolor={COL.get(ln['box'], ln['box'])}@0.92:boxborderw={max(14, size // 6)}:borderw=0") if ln.get("box") and key == "text" \
                else f":borderw={max(5, size // 22)}:bordercolor=black"
            filt.append(
                f"drawtext=fontfile='{FONT}':textfile='{tfp}':expansion=none:fontsize={size}:fontcolor={color}{box}:"
                f"x={xe}:y={y}:alpha='{alpha}'")
    vf = ",".join(filt) if filt else "null"
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.src, "-vf", vf, "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", "-r", "30", "-an", a.out],
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr[-800:])
    print("wrote", a.out)


if __name__ == "__main__":
    main()
