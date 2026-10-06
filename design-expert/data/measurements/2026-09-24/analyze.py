import re,glob,os,collections,sys
S=os.path.dirname(os.path.abspath(__file__))
def feats(t):
    f={}
    fam=re.findall(r"font-family\s*:\s*([^;}]+)",t,re.I)
    fams=[x.split(",")[0].strip(" '\"") for x in fam]
    f["fonts"]=collections.Counter(fams).most_common(4)
    f["google_fonts"]=sorted(set(re.findall(r"family=([A-Za-z+]+)",t)))
    hexes=[h.upper() for h in re.findall(r"#([0-9a-fA-F]{6})\b",t)]
    f["hex_top"]=collections.Counter(hexes).most_common(12)
    f["tailwind_hits"]=sorted(set(h for h in hexes if h in {"4F46E5","6366F1","16A34A","DCFCE7","D97706","FEF3C7","DC2626","FEE2E2","2563EB","3B82F6","0F172A","1E293B","64748B","E2E8F0","F8FAFC","F1F5F9","10B981","F59E0B","EF4444","8B5CF6"}))
    f["radius"]=collections.Counter(re.findall(r"border-radius\s*:\s*([^;}]+)",t)).most_common(6)
    f["bezier"]=collections.Counter(re.findall(r"cubic-bezier\([^)]+\)",t)).most_common(3)
    f["ease_words"]=collections.Counter(re.findall(r"\b(ease-out|ease-in-out|ease-in|ease|linear)\b",t)).most_common(3)
    f["durations"]=collections.Counter(re.findall(r"\b(\d+(?:\.\d+)?m?s)\b",t)).most_common(6)
    f["translateY"]=collections.Counter(re.findall(r"translateY\(\s*(-?\d+px)",t)).most_common(4)
    f["max_width"]=collections.Counter(re.findall(r"max-width\s*:\s*(\d+px)",t)).most_common(4)
    f["widths"]=collections.Counter(re.findall(r"width\s*:\s*(2[0-9]{2}px)",t)).most_common(3)
    f["grid_cols"]=collections.Counter(re.findall(r"grid-template-columns\s*:\s*([^;}]+)",t)).most_common(4)
    f["icons"]=sorted(set(re.findall(r"(lucide|heroicons|feather|phosphor|tabler|material-symbols|font-awesome)",t,re.I)))
    f["dark_mode"]=bool(re.search(r"prefers-color-scheme\s*:\s*dark|data-theme|\.dark\b",t))
    f["texture"]=bool(re.search(r"noise|grain|texture|feTurbulence",t,re.I))
    f["gradient"]=len(re.findall(r"linear-gradient|radial-gradient",t))
    f["serif"]=bool(re.search(r"font-family[^;]*(serif|Playfair|Fraunces|Lora|Merriweather|Newsreader|Instrument Serif|DM Serif)",t))
    f["empty_strings"]=sorted(set(re.findall(r">(No [a-z ]+yet[^<]*)<",t)))
    body=re.sub(r"<style.*?</style>|<script.*?</script>","",t,flags=re.S)
    heads=re.findall(r"<h[12][^>]*>(.*?)</h[12]>",body,re.S)
    f["h1h2"]=[re.sub(r"<[^>]+>|\s+"," ",h).strip()[:40] for h in heads][:14]
    secs=re.findall(r"<(?:section|header|nav|footer|aside|main)[^>]*(?:class|id)=\"([^\"]+)\"",body)
    f["sections"]=[s.split()[0] for s in secs][:16]
    f["cta_words"]=sorted(set(re.findall(r">(Get started[^<]*|Start free[^<]*|Book a demo[^<]*|Sign in|Log in|Try [^<]{0,20}free[^<]*)<",t,re.I)))[:6]
    f["kpi"]=len(re.findall(r"class=\"[^\"]*(stat|kpi|metric)[^\"]*\"",t,re.I))
    f["bytes"]=len(t)
    return f
for model in sorted(os.listdir(S)):
    d=os.path.join(S,model)
    if not os.path.isdir(d): continue
    print(f"\n######## {model}")
    for fpath in sorted(glob.glob(d+"/*.html")):
        t=open(fpath,errors="ignore").read()
        if len(t)<500: print(f"\n=== {os.path.basename(fpath)}: EMPTY/SHORT ({len(t)} bytes)"); continue
        f=feats(t); print(f"\n=== {os.path.basename(fpath)} ({f.pop('bytes')} bytes)")
        for k,v in f.items(): print(f"  {k}: {v}")
