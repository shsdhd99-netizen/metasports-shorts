"""Put the Shorts tracker inside a channel Hub page (owner, Nov 7: "build the tracker page into the shorts hub ... all in one place").

  python Tools/hub_tracker_block.py <hub index.html> nba|fc <other hub url> <out.html>

Adds, without touching the Hub's own code: a jump bar under the header (Drafts, Performance, Coming up, Channel, To do, Ideas,
plus links to the other Hub and the both-channel tracker), a "How the Shorts are doing" section (72-h scorecard, every Short with
views / x median / verdict / stayed / engaged / avg viewed, tap a row for its retention curve vs the channel median and views
per day) and "Coming up" (scheduled uploads). Data: the Hub's db doc `tracker/current` = {asset, updated_utc}, where asset is
the id of `Research Notes/Tracker/hub_<ch>.json` uploaded to that Hub (Tools/short_tracker.py writes it; the scheduled task
"MetaSports tracker refresh" uploads it and updates the doc). Running it twice replaces the block (between the MT markers).
"""
import re, sys

TRACKER_URL = "https://claude.ai/artifact/6kpu5HUkFtCzyFNjNCTPVv"

CSS = """/*MT-CSS*/
.jump{display:flex;gap:6px;flex-wrap:wrap;position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);padding-block:6px}
.jump a{font:600 13px var(--label);letter-spacing:.04em;text-decoration:none;color:var(--fg);border:1px solid var(--line);border-radius:99px;padding:5px 11px;background:var(--card)}
.jump a.ext{color:var(--gold);border-color:var(--gold)}
.jump a:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.mt-tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:6px}
.mt-row{display:grid;grid-template-columns:1fr auto;gap:2px 10px;align-items:baseline;padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--card);cursor:pointer;text-align:left;font:inherit;color:inherit;width:100%}
.mt-row.on{border-color:var(--gold);box-shadow:0 0 0 1px var(--gold)}
.mt-row:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.mt-row .t{font-weight:600;min-width:0;overflow-wrap:anywhere}
.mt-row .v{font:26px/1 var(--display);font-variant-numeric:tabular-nums;text-align:right}
.mt-row .m{grid-column:1/-1;font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
.mt-list{display:flex;flex-direction:column;gap:6px;max-height:520px;overflow:auto;padding:2px}
.mt-sorts{display:flex;gap:6px;flex-wrap:wrap}
.mt-v{font:600 12px var(--label);letter-spacing:.06em;text-transform:uppercase;padding:2px 7px;border-radius:99px;margin-right:6px}
.mt-v.hit{background:var(--ok-bg);color:var(--ok)}.mt-v.flop{background:var(--bad-bg);color:var(--bad)}.mt-v.ok{background:var(--info-bg);color:var(--info)}.mt-v.new{background:var(--warn-bg);color:var(--warn)}
.mt-dl{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px 12px;margin:0}
.mt-dl dt{font:600 12px var(--label);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}.mt-dl dd{margin:0;font-variant-numeric:tabular-nums;font-weight:600}
.mt-chart svg{display:block;width:100%;height:auto}
.mt-chart text{font:11px system-ui,sans-serif;fill:var(--muted)}
.mt-key{display:flex;gap:14px;flex-wrap:wrap;font-size:13px;color:var(--muted)}
.mt-key span::before{content:"";display:inline-block;width:16px;height:0;border-top:2px solid var(--pitch);vertical-align:middle;margin-right:6px}
.mt-key span.med::before{border-top:2px dashed var(--muted)}
.mt-up{display:flex;flex-direction:column;gap:6px}
.mt-up div{display:flex;gap:10px;align-items:baseline;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px;min-width:0}
.mt-up b{font:800 14px var(--label);letter-spacing:.04em;color:var(--gold);white-space:nowrap}
.mt-up span{min-width:0;overflow-wrap:anywhere}
/*MT-CSS-END*/"""

JUMP = """<!--MT-JUMP-->
  <nav class="jump" aria-label="Jump to">
    <a href="#h-shorts">Drafts</a><a href="#h-perf">Performance</a><a href="#h-up">Coming up</a><a href="#h-chan">Channel</a><a href="#h-todo">To do</a><a href="#h-ideas">Ideas</a>
    <a class="ext" href="__OTHER__" target="_blank" rel="noopener">__OTHERNAME__ Hub</a><a class="ext" href="__TRACKER__" target="_blank" rel="noopener">Both channels</a>
  </nav>
<!--MT-JUMP-END-->"""

SECTIONS = """<!--MT-SECTIONS-->
  <section aria-labelledby="h-perf" id="perf-wrap">
    <h2 class="sec" id="h-perf">How the Shorts are doing<small id="mt-when">loading…</small></h2>
    <div style="display:flex;flex-direction:column;gap:10px">
      <div class="mt-tiles">
        <div class="stat"><b id="mt-med">—</b><span>Median views (72 h+)</span></div>
        <div class="stat"><b id="mt-hits">—</b><span>Hits / flops</span></div>
        <div class="stat"><b id="mt-eng">—</b><span>Median engaged</span></div>
        <div class="stat"><b id="mt-avg">—</b><span>Median avg viewed</span></div>
      </div>
      <section class="card" id="mt-detail" aria-label="Selected Short">
        <div class="top"><h2 id="mt-title">Tap a Short below</h2><span class="pill s-editing" id="mt-verdict">—</span></div>
        <dl class="mt-dl" id="mt-dl"></dl>
        <div class="field"><span class="lab">Retention</span>
          <div class="mt-key"><span>This Short</span><span class="med">Channel median</span></div>
          <div class="mt-chart" id="mt-curve"></div>
          <p class="note">Share of viewers still watching at each point. Above 1.0 means people rewatched that part. Arrives 2 to 3 days after posting.</p>
        </div>
        <div class="field"><span class="lab">Views per day</span><div class="mt-chart" id="mt-growth"></div></div>
      </section>
      <div class="mt-sorts" role="group" aria-label="Sort Shorts">
        <button class="tab" type="button" data-mt-sort="live_et" aria-pressed="true">Newest</button>
        <button class="tab" type="button" data-mt-sort="views" aria-pressed="false">Most views</button>
        <button class="tab" type="button" data-mt-sort="stayed_pct" aria-pressed="false">Stayed</button>
        <button class="tab" type="button" data-mt-sort="engaged_pct" aria-pressed="false">Engaged</button>
      </div>
      <div class="mt-list" id="mt-list" aria-live="polite"></div>
      <p class="note">Stayed to watch comes from Studio exports only (YouTube doesn't give it to apps); engaged % is the daily stand-in. Verdicts at 72 h: 2× the channel median or more is a hit, under half a flop.</p>
    </div>
  </section>

  <section aria-labelledby="h-up" id="up-wrap">
    <h2 class="sec" id="h-up">Coming up<small>scheduled, goes live by itself</small></h2>
    <div class="mt-up" id="mt-up"><p class="empty">Nothing scheduled on this channel yet.</p></div>
  </section>
<!--MT-SECTIONS-END-->"""

SCRIPT = """<!--MT-SCRIPT-->
<script>
(function(){
  var CH="__CH__", data=null, sel=null, sortKey="live_et";
  function $(id){return document.getElementById(id);}
  function el(t,c,x){var e=document.createElement(t); if(c)e.className=c; if(x!=null)e.textContent=x; return e;}
  function n(v){return v==null||v===""||(typeof v==="number"&&isNaN(v));}
  function views(v){if(n(v))return "—"; return v>=10000?new Intl.NumberFormat("en",{notation:"compact",maximumFractionDigits:1}).format(v):Math.round(v).toLocaleString("en");}
  function pct(v){return n(v)?"—":(Math.round(v*10)/10)+"%";}
  function when(s){var d=new Date(String(s).replace(" ","T")+":00"); return isNaN(d)?String(s):d.toLocaleString("en-US",{weekday:"short",month:"short",day:"numeric",hour:"numeric",minute:"2-digit"});}
  function age(h){return h<48?Math.round(h)+" h":Math.round(h/24)+" days";}
  function med(a){a=a.filter(function(x){return !n(x);}).sort(function(x,y){return x-y;}); if(!a.length)return null; var m=a.length>>1; return a.length%2?a[m]:(a[m-1]+a[m])/2;}
  var VCLS={hit:"hit",flop:"flop",ok:"ok","too new":"new"};
  function chart(box,series,o){
    box.textContent="";
    var pts=[].concat.apply([],series.map(function(s){return s.pts;}));
    if(!series[0].pts.length){box.appendChild(el("p","note",o.empty)); return;}
    var W=Math.max(box.clientWidth,280),H=190,L=44,R=8,T=8,B=22,NS="http://www.w3.org/2000/svg";
    var xs=pts.map(function(p){return +p.x;}), x0=o.x0!=null?o.x0:Math.min.apply(null,xs), x1=o.x1!=null?o.x1:Math.max.apply(null,xs); if(x1===x0)x1=x0+1;
    var y1=Math.max.apply(null,pts.map(function(p){return p.y;}))*1.1||1;
    function X(v){return L+(v-x0)/(x1-x0)*(W-L-R);} function Y(v){return T+(1-v/y1)*(H-T-B);}
    var svg=document.createElementNS(NS,"svg"); svg.setAttribute("viewBox","0 0 "+W+" "+H); svg.setAttribute("role","img"); svg.setAttribute("aria-label",o.label);
    function add(tag,at,txt){var e=document.createElementNS(NS,tag); for(var k in at)e.setAttribute(k,at[k]); if(txt!=null)e.textContent=txt; svg.appendChild(e); return e;}
    for(var i=0;i<=3;i++){var v=y1*i/3; add("line",{x1:L,x2:W-R,y1:Y(v),y2:Y(v),stroke:"var(--line)"}); add("text",{x:L-6,y:Y(v)+4,"text-anchor":"end"},o.yf(v));}
    o.xt.forEach(function(t,i){add("text",{x:X(+t),y:H-6,"text-anchor":i===0?"start":(i===o.xt.length-1?"end":"middle")},o.xf(t));});
    series.forEach(function(s){
      if(!s.pts.length)return;
      add("path",{d:s.pts.map(function(p,i){return (i?"L":"M")+X(+p.x).toFixed(1)+" "+Y(p.y).toFixed(1);}).join(""),fill:"none",stroke:s.color,"stroke-width":2,"stroke-linecap":"round","stroke-linejoin":"round","stroke-dasharray":s.dash||"none"});
      if(s.dots)s.pts.forEach(function(p){add("circle",{cx:X(+p.x),cy:Y(p.y),r:3,fill:s.color});});
    });
    var main=series[0].pts, dot=add("circle",{r:4,fill:series[0].color,visibility:"hidden"}), lab=add("text",{"text-anchor":"middle",visibility:"hidden",style:"fill:var(--fg);font-weight:600"});
    var hit=add("rect",{x:L,y:0,width:W-L-R,height:H,fill:"transparent"});
    function show(ev){var r=svg.getBoundingClientRect(), xv=x0+((ev.clientX-r.left)/r.width*W-L)/(W-L-R)*(x1-x0), best=main[0];
      main.forEach(function(p){if(Math.abs(+p.x-xv)<Math.abs(+best.x-xv))best=p;});
      dot.setAttribute("cx",X(+best.x)); dot.setAttribute("cy",Y(best.y)); dot.setAttribute("visibility","visible");
      lab.textContent=o.xf(best.x)+": "+o.yf(best.y); lab.setAttribute("x",Math.min(Math.max(X(+best.x),70),W-70)); lab.setAttribute("y",Math.max(Y(best.y)-10,12)); lab.setAttribute("visibility","visible");}
    hit.addEventListener("pointermove",show); hit.addEventListener("pointerdown",show);
    hit.addEventListener("pointerleave",function(){dot.setAttribute("visibility","hidden"); lab.setAttribute("visibility","hidden");});
    box.appendChild(svg);
  }
  function detail(){
    if(!data)return;
    var s=data.shorts.filter(function(r){return r.video_id===sel;})[0];
    if(!s)return;
    $("mt-title").textContent=s.title;
    var v=$("mt-verdict"); v.textContent=s.verdict; v.className="pill "+({hit:"s-ready",flop:"s-blocked",ok:"s-posted"}[s.verdict]||"s-editing");
    var dl=$("mt-dl"); dl.textContent="";
    [["Views",views(s.views)],["× channel median",n(s.vs_median)?"—":s.vs_median.toFixed(2)+"×"],["Stayed (Studio)",pct(s.stayed_pct)],["Engaged (API)",pct(s.engaged_pct)],
     ["Avg % viewed",pct(s.avg_viewed_pct)],["Avg view",n(s.avg_view_s)?"—":Math.round(s.avg_view_s)+" s"],["Subs gained",n(s.subs)?"—":s.subs],["Likes",n(s.likes)?"—":s.likes.toLocaleString("en")],
     ["Went live",when(s.live_et)],["Age",age(s.age_hours)],["Length",s.length_s+" s"],["API numbers as of",s.api_day||"not yet"]].forEach(function(p){
      var d=el("div"); d.appendChild(el("dt","",p[0])); d.appendChild(el("dd","",String(p[1]))); dl.appendChild(d);});
    var mine=data.retention.filter(function(r){return r.video_id===sel;}).map(function(r){return {x:r.elapsed_pct,y:r.watch_ratio};});
    var by={}; data.retention.forEach(function(r){(by[r.elapsed_pct]=by[r.elapsed_pct]||[]).push(r.watch_ratio);});
    var median=Object.keys(by).map(Number).sort(function(a,b){return a-b;}).map(function(k){return {x:k,y:med(by[k])};});
    var accent=getComputedStyle(document.documentElement).getPropertyValue("--pitch").trim()||"currentColor";
    chart($("mt-curve"),[{pts:mine,color:accent},{pts:median,color:"var(--muted)",dash:"5 4"}],{label:"Retention curve",empty:"No retention curve yet.",x0:0,x1:100,xt:[0,25,50,75,100],xf:function(v){return Math.round(v)+"%";},yf:function(v){return (Math.round(v*10)/10).toFixed(1);}});
    var day={}; data.history.filter(function(h){return h.video_id===sel;}).forEach(function(h){if(!day[h.date]||h.source==="public")day[h.date]=h;});
    var g=Object.keys(day).sort().map(function(k){return {x:new Date(k+"T12:00:00Z"),y:day[k].views};});
    var xt=g.length>1?[g[0].x,g[g.length-1].x]:g.map(function(p){return p.x;});
    chart($("mt-growth"),[{pts:g,color:accent,dots:true}],{label:"Views per day",empty:"No daily counts yet.",xt:xt,xf:function(d){return new Date(d).toLocaleDateString("en-US",{month:"short",day:"numeric",timeZone:"UTC"});},yf:views});
    Array.prototype.forEach.call(document.querySelectorAll(".mt-row"),function(b){b.classList.toggle("on",b.dataset.vid===sel);});
  }
  function render(){
    var rows=data.shorts.slice(), m=rows.filter(function(r){return r.age_hours>=72;});
    $("mt-when").textContent="updated "+data.updated_utc+" UTC";
    $("mt-med").textContent=views(med(m.map(function(r){return r.views;})));
    $("mt-hits").textContent=m.filter(function(r){return r.verdict==="hit";}).length+" / "+m.filter(function(r){return r.verdict==="flop";}).length;
    $("mt-eng").textContent=pct(med(m.map(function(r){return r.engaged_pct;})));
    $("mt-avg").textContent=pct(med(m.map(function(r){return r.avg_viewed_pct;})));
    rows.sort(function(a,b){var x=a[sortKey],y=b[sortKey]; if(n(x)&&n(y))return 0; if(n(x))return 1; if(n(y))return -1; return typeof x==="number"?y-x:String(y).localeCompare(String(x));});
    var list=$("mt-list"); list.textContent="";
    rows.forEach(function(r){
      var b=el("button","mt-row"); b.type="button"; b.dataset.vid=r.video_id;
      b.appendChild(el("span","t",r.title)); b.appendChild(el("span","v",views(r.views)));
      var meta=el("span","m"); meta.appendChild(el("span","mt-v "+(VCLS[r.verdict]||"new"),r.verdict));
      meta.appendChild(document.createTextNode(when(r.live_et)+" · stayed "+pct(r.stayed_pct)+" · engaged "+pct(r.engaged_pct)+" · avg viewed "+pct(r.avg_viewed_pct)+(n(r.vs_median)?"":" · "+r.vs_median.toFixed(2)+"× median")));
      b.appendChild(meta);
      b.addEventListener("click",function(){sel=r.video_id; detail(); $("mt-detail").scrollIntoView({behavior:"smooth",block:"start"});});
      list.appendChild(b);
    });
    if(!rows.length)list.appendChild(el("p","empty","No Shorts tracked yet."));
    if(!sel||!rows.some(function(r){return r.video_id===sel;})){var w=data.shorts.filter(function(r){return r.api_views!=null;}).sort(function(a,b){return b.live_et.localeCompare(a.live_et);})[0]||data.shorts[0]; sel=w?w.video_id:null;}
    detail();
    var up=$("mt-up"); up.textContent="";
    data.upcoming.forEach(function(u){var d=el("div"); d.appendChild(el("b","",when(u.live_et))); d.appendChild(el("span","",u.title)); up.appendChild(d);});
    if(!data.upcoming.length)up.appendChild(el("p","empty","Nothing scheduled on this channel yet."));
  }
  Array.prototype.forEach.call(document.querySelectorAll("[data-mt-sort]"),function(b){b.addEventListener("click",function(){
    sortKey=b.dataset.mtSort; Array.prototype.forEach.call(document.querySelectorAll("[data-mt-sort]"),function(o){o.setAttribute("aria-pressed",String(o===b));}); if(data)render();});});
  var lastW=0; window.addEventListener("resize",function(){var w=$("mt-curve").clientWidth; if(data&&Math.abs(w-lastW)>40){lastW=w; detail();}});
  function boot(){
    if(!window.claude||!claude.use){$("mt-when").textContent="open in the Claude app"; return;}
    claude.use("db").then(function(db){
      if(!db){$("mt-when").textContent="sign in to load"; return;}
      db.doc("tracker/current").onSnapshot(function(doc){
        var d=doc&&doc.exists?doc.data():null;
        if(!d||!d.asset){$("mt-when").textContent="no data yet"; return;}
        fetch("/_blob/"+d.asset).then(function(r){if(!r.ok)throw new Error(); return r.json();})
          .then(function(j){if(j.channel!==CH)throw new Error(); data=j; render();})
          .catch(function(){$("mt-when").textContent="could not load the numbers";});
      },function(){$("mt-when").textContent="could not load the numbers";});
    });
  }
  window.claude&&window.claude.hot&&window.claude.hot.ready?window.claude.hot.ready(boot):boot();
})();
</script>
<!--MT-SCRIPT-END-->"""


def strip(html, a, b):
    return re.sub(re.escape(a) + r".*?" + re.escape(b) + r"\n?", "", html, flags=re.S)


def main():
    src, ch, other, out = sys.argv[1:5]
    h = open(src, encoding="utf-8").read()
    if "<body>" in h[:2000]:  # a page read back from the Artifact tool carries the publish skeleton; publishing adds it again
        h = h[h.index("<body>") + len("<body>"):]
    h = re.sub(r"\s*</body>\s*</html>\s*$", "", h)
    for a, b in (("/*MT-CSS*/", "/*MT-CSS-END*/"), ("<!--MT-JUMP-->", "<!--MT-JUMP-END-->"),
                 ("<!--MT-SECTIONS-->", "<!--MT-SECTIONS-END-->"), ("<!--MT-SCRIPT-->", "<!--MT-SCRIPT-END-->")):
        h = strip(h, a, b)
    i = h.index("</style>", h.index("--display"))
    h = h[:i] + CSS + "\n" + h[i:]
    i = h.index("</header>") + len("</header>")
    jump = JUMP.replace("__OTHER__", other).replace("__OTHERNAME__", "FC" if ch == "nba" else "NBA").replace("__TRACKER__", TRACKER_URL)
    h = h[:i] + "\n" + jump + h[i:]
    i = h.index("</section>", h.index('aria-labelledby="h-shorts"')) + len("</section>")
    h = h[:i] + "\n\n" + SECTIONS + h[i:]
    h = h.rstrip()
    h = h + "\n\n" + SCRIPT.replace("__CH__", ch) + "\n"
    open(out, "w", encoding="utf-8").write(h)
    print(f"wrote {out} ({len(h)} bytes)")


if __name__ == "__main__":
    main()
