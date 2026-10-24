// Download a public TikTok video through the preinstalled Chromium (YouTube blocks cloud IPs; TikTok pages still play).
//   node watch_dl.mjs --url "https://www.tiktok.com/@user/video/123" --out video.mp4
// Prints JSON {title, bytes, file}. Free, no account. Works from this cloud container (tested Oct 5 2026).
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'node:fs';
const a = process.argv.slice(2); const opt = (k) => { const i = a.indexOf('--' + k); return i >= 0 ? a[i + 1] : undefined; };
const url = opt('url'), out = opt('out') || 'video.mp4';
if (!url) { console.error('give --url'); process.exit(2); }
const exe = ['/opt/pw-browsers/chromium-1194/chrome-linux/chrome', ...fs.readdirSync('/opt/pw-browsers').filter(d => d.startsWith('chromium-')).map(d => `/opt/pw-browsers/${d}/chrome-linux/chrome`)].find(p => fs.existsSync(p));
const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
const b = await chromium.launch({ executablePath: exe, args: ['--no-sandbox', '--mute-audio'], proxy });
try {
  const ctx = await b.newContext({ viewport: { width: 405, height: 720 }, userAgent: 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Mobile Safari/537.36' });
  const p = await ctx.newPage();
  await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
  let src = null;
  for (let i = 0; i < 12 && !src; i++) { await p.waitForTimeout(1500); src = await p.evaluate(() => { const v = document.querySelector('video'); return v && v.currentSrc; }); }
  if (!src) { console.error(JSON.stringify({ error: 'no video src (blocked or not a video page)', title: await p.title() })); process.exit(1); }
  const r = await ctx.request.get(src, { headers: { Referer: 'https://www.tiktok.com/' } });
  const body = await r.body(); fs.writeFileSync(out, body);
  console.log(JSON.stringify({ title: await p.title(), bytes: body.length, file: out, status: r.status() }));
} finally { await b.close(); }
