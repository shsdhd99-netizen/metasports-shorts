// Screenshot a web page (or just one part of it) for B-roll: Basketball Reference, ESPN, Spotrac, the NBA rulebook...
// Cookie banners, sticky headers, chat bubbles and ads are removed first.
//
//   node webshot.mjs --url "https://www.basketball-reference.com/players/j/jamesle01.html" --out shot.png
//   node webshot.mjs --url ... --selector "#per_game" --out table.png           (one element)
//   node webshot.mjs --url ... --text "Per Game" --out part.png                 (the element holding these words)
//   node webshot.mjs --url ... --mark "15 feet" --out rule.png                  (also reports where "15 feet" is,
//                                                                                so broll.py page can circle it)
//   node webshot.mjs --url ... --selector "#dpoy" --cells "tbody tr:nth-child(1) td[data-stat=award_share]" --out t.png
//                                                                               (one box around matching cells)
// Options: --width 1200 --height 1500 --scale 2 --pad 24 --wait 2500 --full --hide "css, css" --js "code"
// Prints JSON: {"file", "w", "h", "marks": [{"x","y","w","h"}]} with mark boxes in the PNG's own pixels.
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const argv = process.argv.slice(2);
const opt = (k, d) => { const i = argv.indexOf('--' + k); return i >= 0 ? (argv[i + 1] && !argv[i + 1].startsWith('--') ? argv[i + 1] : true) : d; };
const url = opt('url'), out = path.resolve(opt('out', 'shot.png'));
const W = +opt('width', 1200), H = +opt('height', 1500), SCALE = +opt('scale', 2), PAD = +opt('pad', 24), WAIT = +opt('wait', 2500);
const selector = opt('selector'), text = opt('text'), full = !!opt('full'), extraHide = opt('hide'), extraJs = opt('js');
const marks = argv.flatMap((a, i) => a === '--mark' ? [argv[i + 1]] : []);
const cellSels = argv.flatMap((a, i) => a === '--cells' ? [argv[i + 1]] : []);
if (!url) { console.error('give --url'); process.exit(2); }

const BROWSER = [process.env.BROWSER_PATH, 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
                 'C:/Program Files/Google/Chrome/Application/chrome.exe', '/opt/pw-browsers/chromium/chrome',
                 '/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/google-chrome'].find(p => p && fs.existsSync(p))
  || (fs.existsSync('/opt/pw-browsers') ? fs.readdirSync('/opt/pw-browsers').filter(d => d.startsWith('chromium-'))
      .map(d => `/opt/pw-browsers/${d}/chrome-linux/chrome`).find(p => fs.existsSync(p)) : undefined);
if (!BROWSER) { console.error('No browser found: set BROWSER_PATH'); process.exit(2); }
const LINUX = process.platform === 'linux';
const sleep = ms => new Promise(r => setTimeout(r, ms));
const port = 9300 + Math.floor(Math.random() * 600);
const prof = fs.mkdtempSync(path.join(os.tmpdir(), 'webshot-'));
const proc = spawn(BROWSER, [`--remote-debugging-port=${port}`, `--user-data-dir=${prof}`, '--headless=new', '--disable-gpu', ...(LINUX ? ['--no-sandbox', '--disable-dev-shm-usage'] : []),
  '--hide-scrollbars', '--no-first-run', '--no-default-browser-check', '--mute-audio', '--disable-notifications',
  `--window-size=${W},${H}`, 'about:blank'], { stdio: 'ignore' });

const CLEAN = `(() => {
  const kill = ${JSON.stringify(['[id*="cookie" i]', '[class*="cookie" i]', '[id*="consent" i]', '[class*="consent" i]',
    '[id*="onetrust" i]', '[class*="onetrust" i]', '.fc-consent-root', '[class*="gdpr" i]', '[id*="gdpr" i]',
    '[id^="div-gpt-ad"]', '[id*="google_ads" i]', '.adsbygoogle', '[class*="ad-slot" i]', '[class*="AdSlot" i]',
    '[class*="ad-container" i]', '[id*="taboola" i]', '[class*="taboola" i]', '[class*="outbrain" i]',
    '[aria-label*="advert" i]', '[class*="newsletter" i]', '[class*="modal" i]', '[class*="overlay" i]',
    '[class*="paywall" i]', 'iframe'])};
  const extra = ${JSON.stringify(extraHide || '')};
  for (const s of kill.concat(extra ? extra.split(',') : [])) { try { document.querySelectorAll(s.trim()).forEach(e => {
    if (e !== document.body && e !== document.documentElement && !e.querySelector('table, article h1')) e.remove(); }); } catch (_) {} }
  for (const e of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(e);
    if ((cs.position === 'fixed' || cs.position === 'sticky') && !e.closest('table')) e.style.setProperty('display', 'none', 'important');
    if (cs.position === 'sticky' && e.closest('table')) e.style.setProperty('position', 'static', 'important');
  }
  document.documentElement.style.overflow = 'visible'; document.body.style.overflow = 'visible';
  for (const t of document.querySelectorAll('table')) {  // wide tables live in sideways-scrolling boxes: open them up
    for (let p = t.parentElement; p && p !== document.body; p = p.parentElement) {
      p.style.setProperty('overflow', 'visible', 'important'); p.style.setProperty('max-width', 'none', 'important');
    }
  }
  return true; })()`;

async function main() {
  let ver;
  for (let i = 0; i < 60 && !ver; i++) { try { ver = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json(); } catch { await sleep(250); } }
  if (!ver) throw new Error('browser did not start');
  const page = (await (await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find(t => t.type === 'page');
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  let id = 0; const waiting = new Map(), listeners = [];
  ws.onmessage = ev => { const m = JSON.parse(ev.data); if (m.id && waiting.has(m.id)) { const [res, rej] = waiting.get(m.id); waiting.delete(m.id); m.error ? rej(new Error(m.error.message)) : res(m.result); } else listeners.forEach(f => f(m)); };
  const send = (method, params = {}) => new Promise((res, rej) => { const i = ++id; waiting.set(i, [res, rej]); ws.send(JSON.stringify({ id: i, method, params })); });
  const evaluate = async expr => (await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true })).result.value;

  await send('Page.enable'); await send('Runtime.enable'); await send('Network.enable');
  await send('Network.setUserAgentOverride', { userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0' });
  await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: SCALE, mobile: false });
  const loaded = new Promise(res => listeners.push(m => { if (m.method === 'Page.loadEventFired') res(); }));
  await send('Page.navigate', { url });
  await Promise.race([loaded, sleep(25000)]);
  await sleep(WAIT);
  await evaluate(CLEAN);
  if (extraJs) await evaluate(extraJs);
  await sleep(400);
  await evaluate(CLEAN);

  // region to capture, in CSS pixels of the whole document
  const region = await evaluate(`(() => {
    const sel = ${JSON.stringify(selector || '')}, txt = ${JSON.stringify(text || '')};
    let el = null;
    if (sel) el = document.querySelector(sel);
    if (el && el.tagName !== 'TABLE' && el.querySelector('table')) el = el.querySelector('table').parentElement;
    if (!el && txt) {
      const it = document.createNodeIterator(document.body, NodeFilter.SHOW_TEXT);
      let n; while ((n = it.nextNode())) { if (n.textContent.toLowerCase().includes(txt.toLowerCase())) { el = n.parentElement; break; } }
      while (el && el.getBoundingClientRect().width < 300 && el.parentElement) el = el.parentElement;
    }
    if (!el) return null;
    window.__wsRegion = el;
    el.scrollIntoView({block: 'center'});
    const r = el.getBoundingClientRect();
    const w = Math.max(r.width, el.scrollWidth || 0, ...(Array.from(el.querySelectorAll('table')).map(t => t.getBoundingClientRect().width)));
    return {x: r.left + scrollX, y: r.top + scrollY, w, h: r.height};
  })()`);
  const metrics = await send('Page.getLayoutMetrics');
  const docW = metrics.cssContentSize?.width || W, docH = metrics.cssContentSize?.height || H;
  let clip;
  if (region) clip = { x: Math.max(0, region.x - PAD), y: Math.max(0, region.y - PAD), width: Math.min(docW, region.w + 2 * PAD), height: region.h + 2 * PAD };
  else if (full) clip = { x: 0, y: 0, width: docW, height: Math.min(docH, 12000) };
  else clip = { x: 0, y: await evaluate('scrollY'), width: W, height: H };

  // boxes around every --mark phrase (first match each), relative to the clip, in PNG pixels
  const found = [];
  for (const m of marks) {
    const box = await evaluate(`(() => {
      const want = ${JSON.stringify(m)}.toLowerCase();
      const it = document.createNodeIterator(window.__wsRegion || document.body, NodeFilter.SHOW_TEXT);
      let n; while ((n = it.nextNode())) {
        const i = n.textContent.toLowerCase().indexOf(want);
        if (i < 0) continue;
        const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + want.length);
        const b = r.getBoundingClientRect(); if (!b.width) continue;
        return {x: b.left + scrollX, y: b.top + scrollY, w: b.width, h: b.height};
      } return null; })()`);
    if (box) found.push({ text: m, x: Math.round((box.x - clip.x) * SCALE), y: Math.round((box.y - clip.y) * SCALE), w: Math.round(box.w * SCALE), h: Math.round(box.h * SCALE) });
    else found.push({ text: m, missing: true });
  }
  // --cells "css": one box around every visible element matching the selector (e.g. a column of table cells)
  for (const s of cellSels) {
    const box = await evaluate(`(() => {
      const root = window.__wsRegion || document; let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
      for (const e of root.querySelectorAll(${JSON.stringify(s)})) {
        const b = e.getBoundingClientRect(); if (!b.width || !b.height) continue;
        x0 = Math.min(x0, b.left + scrollX); y0 = Math.min(y0, b.top + scrollY);
        x1 = Math.max(x1, b.right + scrollX); y1 = Math.max(y1, b.bottom + scrollY);
      } return x1 > x0 ? {x: x0, y: y0, w: x1 - x0, h: y1 - y0} : null; })()`);
    if (box) found.push({ text: s, x: Math.round((box.x - clip.x) * SCALE), y: Math.round((box.y - clip.y) * SCALE), w: Math.round(box.w * SCALE), h: Math.round(box.h * SCALE) });
    else found.push({ text: s, missing: true });
  }
  const shot = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { ...clip, scale: 1 } });
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, Buffer.from(shot.data, 'base64'));
  console.log(JSON.stringify({ file: out, w: Math.round(clip.width * SCALE), h: Math.round(clip.height * SCALE), marks: found }));
  ws.close();
}

main().catch(e => { console.error('webshot failed:', e.message); process.exitCode = 1; })
  .finally(() => { try { proc.kill(); } catch {} setTimeout(() => { try { fs.rmSync(prof, { recursive: true, force: true }); } catch {} process.exit(); }, 800); });
