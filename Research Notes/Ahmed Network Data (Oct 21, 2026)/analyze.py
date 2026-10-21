import json,glob,re,statistics as st,collections,datetime,difflib,os,sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CH=['AhmedsBasketball','AhmedsGoal','AhmedsBusiness']
def load(h):
    e=[x for x in json.load(open(f'full_{h}.json'))['entries'] if x]
    # sampled dates -> interpolate by index (list is newest first)
    anchors={}
    for f in glob.glob(f'samp_{h}/*.info.json'):
        d=json.load(open(f)); anchors[d['id']]=d
    idx={x['id']:i for i,x in enumerate(e)}
    pts=sorted((idx[k],datetime.datetime.strptime(v['upload_date'],'%Y%m%d')) for k,v in anchors.items() if k in idx and v.get('upload_date'))
    for i,x in enumerate(e):
        x['i']=i; x['v']=x.get('view_count') or 0
        if pts:
            lo=max([p for p in pts if p[0]<=i],default=pts[0],key=lambda p:p[0]); hi=min([p for p in pts if p[0]>=i],default=pts[-1],key=lambda p:p[0])
            if hi[0]==lo[0]: x['date']=lo[1]
            else: x['date']=lo[1]+(hi[1]-lo[1])*((i-lo[0])/(hi[0]-lo[0]))
    return e,anchors
LAB=[('underdog / rejected',r"reject|nobody wanted|no chance|overlook|discovered|undrafted|regular jobs|normal jobs|weren't their|never wanted|cut |doubted|said would fail|nobody believed|unknown"),
('refused / defiant',r"refus|forced their way|threat|demand|wouldn't|walked out|quit"),
('money / business',r"money|contract|paid|rich|million|billion|salary|fined|broke |cheap|price|deal|bought|sold"),
('records / oddities / fake-but-real',r"record|fake but|never happen|scoreline|stat|only \d|weird|strange|crazi|silliest|ridiculous|absurd|unbelievable"),
('relationships / family',r"friend|father|son|childhood hero|teammate|enem|brother|rival|wife|mom|dad"),
('downfall / destroyed',r"lost it all|destroy|ruin|fail|collaps|worst|fell |downfall|regret|killed|erased|dying|mistake|betray"),
('comeback / revenge / glow-up',r"comeback|revenge|brought .* back|became legend|became (big|star)|better|saved|turned|instantly got better|accidentally found"),
('iconic numbers / history',r"jersey|shirt number|iconic|trophy|logo|mascot|nickname"),
('what happens / explainers',r"^what |^why |^how ")]
def labels(t):
    t=t.lower(); return [n for n,p in LAB if re.search(p,t)] or ['other']
def caps(t): return len([w for w in re.findall(r"[A-Za-z']+",t) if len(w)>=3 and w.isupper() and w not in ('NBA','CEO','CEOS','MLS','NFL','UEFA','FIFA','WWE')])
out={}
for h in CH:
    if not os.path.exists(f'full_{h}.json'): continue
    e,anch=load(h); v=[x['v'] for x in e]
    r={'n':len(e),'sum':sum(v),'median':st.median(v),'mean':st.mean(v),'p1m':sum(1 for a in v if a>=1e6),'p100k':sum(1 for a in v if a>=1e5),'u10k':sum(1 for a in v if a<1e4)}
    # chronological deciles
    ch=list(reversed(e)); k=max(1,len(ch)//10); dec=[]
    for j in range(0,len(ch),k):
        seg=ch[j:j+k]; d0=seg[0].get('date'); d1=seg[-1].get('date')
        dec.append((d0.strftime('%Y-%m-%d') if d0 else '?', d1.strftime('%Y-%m-%d') if d1 else '?', len(seg), st.median([x['v'] for x in seg])))
    r['deciles']=dec
    # monthly uploads (interpolated)
    m=collections.Counter(x['date'].strftime('%Y-%m') for x in e if x.get('date')); r['per_month']=dict(sorted(m.items()))
    mv=collections.defaultdict(list)
    for x in e:
        if x.get('date'): mv[x['date'].strftime('%Y-%m')].append(x['v'])
    r['median_by_month']={k:int(st.median(a)) for k,a in sorted(mv.items())}
    # labels
    L=collections.defaultdict(list)
    for x in e:
        for l in labels(x['title']): L[l].append(x['v'])
    r['labels']=sorted(((l,len(a),int(st.median(a)),sum(1 for q in a if q>=1e6)) for l,a in L.items()),key=lambda z:-z[2])
    # caps / length
    cp=[x['v'] for x in e if caps(x['title'])>0]; nc=[x['v'] for x in e if caps(x['title'])==0]
    r['caps']=(len(cp),int(st.median(cp)) if cp else 0,len(nc),int(st.median(nc)) if nc else 0)
    wl=collections.defaultdict(list)
    for x in e: wl[min(len(x['title'].split())//3*3,15)].append(x['v'])
    r['words']={k:(len(a),int(st.median(a))) for k,a in sorted(wl.items())}
    # duplicates
    D=collections.defaultdict(list)
    for x in e: D[re.sub(r'\W+',' ',x['title'].lower()).strip()].append(x)
    dups=[(k,sorted(a,key=lambda x:-x['i'])) for k,a in D.items() if len(a)>1]
    r['dups']=[(k,[(x['v'],x['date'].strftime('%Y-%m-%d') if x.get('date') else '?') for x in a]) for k,a in dups]
    r['top']=[(x['v'],x['date'].strftime('%Y-%m-%d') if x.get('date') else '?',x['title']) for x in sorted(e,key=lambda x:-x['v'])[:20]]
    # durations from samples
    du=[d.get('duration') for d in anch.values() if d.get('duration')]
    r['dur']=(len(du),min(du) if du else None,st.median(du) if du else None,max(du) if du else None)
    lk=[(d.get('like_count') or 0)/(d.get('view_count') or 1) for d in anch.values() if d.get('view_count')]
    r['like_rate']=st.median(lk) if lk else None
    out[h]=(r,e)
for h,(r,e) in out.items():
    print(f"\n######## {h}: n={r['n']} sum={r['sum']:,} median={r['median']:,.0f} mean={r['mean']:,.0f} >=1M:{r['p1m']} >=100K:{r['p100k']} <10K:{r['u10k']}")
    print(" durations (sample n, min, median, max):",r['dur'],"like rate median:",r['like_rate'])
    print(" deciles (oldest->newest):"); [print("   ",d) for d in r['deciles']]
    print(" uploads per month:",r['per_month'])
    print(" median by month:",r['median_by_month'])
    print(" labels (name, n, median, >=1M):"); [print("   ",l) for l in r['labels']]
    print(" CAPS words in title (n, median) vs none (n, median):",r['caps'])
    print(" title words bucket:",r['words'])
    print(" duplicates:",len(r['dups'])); [print("   ",d) for d in r['dups'][:15]]
    print(" top 20:"); [print("   ",t) for t in r['top']]
# cross-channel twins
def norm(s):
    s=s.lower()
    s=re.sub(r"\b(nba|football|soccer|world cup|premier league|basketball|players?|teams?|companies|company|brands?|ceos?|people|businesses|the|in|of|history|who|that|their|own|ever|all time)\b",' ',s)
    return re.sub(r'\W+',' ',s).strip()
names=list(out)
for a in range(len(names)):
    for b in range(a+1,len(names)):
        A,B=out[names[a]][1],out[names[b]][1]; pairs=[]
        Bn=[(norm(y['title']),y) for y in B]
        for x in A:
            nx=norm(x['title']); best=None;br=0
            for ny,y in Bn:
                r_=difflib.SequenceMatcher(None,nx,ny).ratio()
                if r_>br: br,best=r_,y
            if br>=0.8: pairs.append((br,x,best))
        print(f"\n== twins {names[a]} vs {names[b]}: {len(pairs)} (of {len(A)})")
        first_a=sum(1 for _,x,y in pairs if x.get('date') and y.get('date') and x['date']<y['date'])
        first_b=sum(1 for _,x,y in pairs if x.get('date') and y.get('date') and y['date']<x['date'])
        print(f"   {names[a]} first: {first_a}, {names[b]} first: {first_b}")
        hit_a=[(x['v'],y['v']) for _,x,y in pairs]
        both=sum(1 for p,q in hit_a if p>=out[names[a]][0]['median']*2 and q>=out[names[b]][0]['median']*2)
        onlya=sum(1 for p,q in hit_a if p>=out[names[a]][0]['median']*2 and q<out[names[b]][0]['median']*2)
        onlyb=sum(1 for p,q in hit_a if p<out[names[a]][0]['median']*2 and q>=out[names[b]][0]['median']*2)
        print(f"   pairs where both beat 2x their channel median: {both}; only {names[a]}: {onlya}; only {names[b]}: {onlyb}")
        for r_,x,y in sorted(pairs,key=lambda z:-(z[1]['v']+z[2]['v']))[:12]:
            print(f"   {x['v']:>9,} {x['date'].strftime('%y-%m-%d') if x.get('date') else '?'} {x['title'][:55]} || {y['v']:>9,} {y['date'].strftime('%y-%m-%d') if y.get('date') else '?'} {y['title'][:55]}")
