// Builds a password-protected static site: everything private is AES-256-GCM encrypted (key from PBKDF2-SHA256, 250k iterations);
// the shell page asks for the password and decrypts in the browser. Free-plan friendly (no server code).
import { webcrypto as crypto } from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

const [,, srcDir, outDir, password] = process.argv;
const enc = new TextEncoder();
const salt = crypto.getRandomValues(new Uint8Array(16));
const ITER = 250000;
const baseKey = await crypto.subtle.importKey('raw', enc.encode(password), 'PBKDF2', false, ['deriveKey']);
const key = await crypto.subtle.deriveKey({ name: 'PBKDF2', salt, iterations: ITER, hash: 'SHA-256' }, baseKey, { name: 'AES-GCM', length: 256 }, false, ['encrypt']);
const b64 = (u8) => Buffer.from(u8).toString('base64');

fs.rmSync(outDir, { recursive: true, force: true });
fs.mkdirSync(path.join(outDir, 'p'), { recursive: true });

async function seal(bytes, name) {
  const iv = crypto.getRandomValues(new Uint8Array(12));
  const ct = new Uint8Array(await crypto.subtle.encrypt({ name: 'AES-GCM', iv }, key, bytes));
  const out = new Uint8Array(12 + ct.length); out.set(iv, 0); out.set(ct, 12);
  const id = Buffer.from(crypto.getRandomValues(new Uint8Array(9))).toString('hex');
  fs.writeFileSync(path.join(outDir, 'p', id + '.bin'), out);
  return id;
}
const files = {};
const priv = [
  ['index.html', 'text/html'], ['quote.html', 'text/html'],
  ['media/max-preview-vertical.mp4', 'video/mp4'], ['media/max-preview-wide.mp4', 'video/mp4'], ['media/max-poster.jpg', 'image/jpeg'],
];
for (const [rel, mime] of priv) {
  const bytes = new Uint8Array(fs.readFileSync(path.join(srcDir, rel)));
  files[rel] = { id: await seal(bytes, rel), mime };
}
// public, non-sensitive files copied as they are
for (const rel of ['thanks.html', 'demo.mp4', 'poster.jpg']) {
  if (fs.existsSync(path.join(srcDir, rel))) fs.copyFileSync(path.join(srcDir, rel), path.join(outDir, rel));
}
fs.writeFileSync(path.join(outDir, 'manifest.json'), JSON.stringify({ salt: b64(salt), iter: ITER, files }));

const shell = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>Private page</title>
<style>
body{margin:0;min-height:100vh;display:grid;place-items:center;background:#fbfaf7;color:#0f1214;font:17px/1.5 system-ui,-apple-system,Segoe UI,sans-serif;padding:20px}
.box{max-width:420px;width:100%;background:#fff;border:1px solid #e6e3dc;border-radius:18px;padding:28px;box-shadow:0 20px 50px -30px rgba(0,0,0,.35)}
h1{font-size:1.5rem;margin:0 0 6px}p{margin:0 0 14px;color:#5f666b}input{font:inherit;width:100%;padding:13px;border:1px solid #cfd2d0;border-radius:12px;box-sizing:border-box}
button{font:600 1rem system-ui;margin-top:12px;width:100%;padding:14px;border:0;border-radius:999px;background:#0f1214;color:#fff;cursor:pointer}
#err{color:#b3261e;min-height:1.3em;margin-top:10px}
</style></head><body>
<form id="gate" class="box" autocomplete="off">
  <h1>This page is private</h1>
  <p>It was made for one person. Enter the password you were sent.</p>
  <input id="pw" type="password" placeholder="Password" autofocus required>
  <button type="submit" id="go">Open</button>
  <div id="err" role="alert"></div>
</form>
<!-- Registers the real forms with Netlify at deploy time (the visible forms live in the encrypted page). -->
<form name="inputs-upload" data-netlify="true" netlify-honeypot="company2" enctype="multipart/form-data" hidden>
  <input name="photo_1" type="file"><input name="photo_2" type="file"><input name="photo_3" type="file"><input name="photo_4" type="file"><input name="photo_5" type="file">
  <input name="voice" type="file"><input name="video" type="file"><input name="links"><input name="consent" type="checkbox"><input name="contact"><input name="company2">
</form>
<form name="video-request" data-netlify="true" netlify-honeypot="company" hidden>
  <input name="topic"><input name="use"><input name="volume"><textarea name="notes"></textarea><input name="contact"><input name="company">
</form>
<form name="draft-feedback" data-netlify="true" netlify-honeypot="company3" hidden>
  <textarea name="feedback"></textarea><input name="contact"><input name="company3">
</form>
<script>
(function(){
  var f=document.getElementById('gate'), err=document.getElementById('err'), btn=document.getElementById('go');
  function b64(s){var b=atob(s),u=new Uint8Array(b.length);for(var i=0;i<b.length;i++)u[i]=b.charCodeAt(i);return u;}
  async function open(pw){
    var m=await (await fetch('manifest.json',{cache:'no-store'})).json();
    var base=await crypto.subtle.importKey('raw',new TextEncoder().encode(pw),'PBKDF2',false,['deriveKey']);
    var key=await crypto.subtle.deriveKey({name:'PBKDF2',salt:b64(m.salt),iterations:m.iter,hash:'SHA-256'},base,{name:'AES-GCM',length:256},false,['decrypt']);
    async function dec(rel){
      var buf=new Uint8Array(await (await fetch('p/'+m.files[rel].id+'.bin')).arrayBuffer());
      return new Uint8Array(await crypto.subtle.decrypt({name:'AES-GCM',iv:buf.slice(0,12)},key,buf.slice(12)));
    }
    var html=new TextDecoder().decode(await dec('index.html'));   // wrong password throws here
    var urls={};
    for (var rel in m.files){ if(rel.indexOf('media/')===0||rel==='quote.html'){ var by=await dec(rel); urls[rel]=URL.createObjectURL(new Blob([by],{type:m.files[rel].mime})); } }
    for (var r in urls){ html=html.split('"'+r+'"').join('"'+urls[r]+'"'); }
    html=html.split('href="quote.html"').join('href="'+urls['quote.html']+'"');
    document.open(); document.write(html); document.close();
  }
  f.addEventListener('submit',function(e){
    e.preventDefault(); err.textContent=''; btn.disabled=true; btn.textContent='Opening...';
    open(document.getElementById('pw').value).catch(function(){ err.textContent='That password did not work. Check it and try again.'; btn.disabled=false; btn.textContent='Open'; });
  });
})();
</script></body></html>`;
fs.writeFileSync(path.join(outDir, 'index.html'), shell);
console.log('built', Object.keys(files).length, 'private files; shell', shell.length, 'bytes');
