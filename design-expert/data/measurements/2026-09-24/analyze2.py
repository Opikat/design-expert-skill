import re,glob,os,collections
S=os.path.dirname(os.path.abspath(__file__))
def root_vars(t):
    m=re.search(r":root\s*\{(.*?)\}",t,re.S); v={}
    if m:
        for k,val in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);",m.group(1)): v[k]=val.strip()
    return v
def resolve(val,v,depth=0):
    if depth>4: return val
    return re.sub(r"var\((--[\w-]+)\)",lambda m: resolve(v.get(m.group(1),m.group(0)),v,depth+1),val)
for model in sorted(d for d in os.listdir(S) if d.startswith("claude-")):
    print(f"\n######## {model}")
    for fp in sorted(glob.glob(f"{S}/{model}/*.html")):
        t=open(fp,errors="ignore").read(); v=root_vars(t); name=os.path.basename(fp)
        print(f"\n=== {name}")
        fams=set()
        for raw in re.findall(r"font-family\s*:\s*([^;}]+)",t):
            r=resolve(raw,v); fams.add(re.sub(r"\s+"," ",r)[:70])
        print("  font-family:",sorted(fams)[:6])
        keys=[k for k in v if re.search(r"font|serif|sans|mono|display",k)]
        print("  font vars:",{k:v[k][:50] for k in keys})
        bg=[(k,v[k]) for k in v if re.search(r"^--(bg|paper|canvas|surface|ink|text|fg|accent|primary|brand)\b",k)]
        print("  palette vars:",bg[:8])
        tr=set(re.sub(r"\s+"," ",x.strip()) for x in re.findall(r"transition\s*:\s*([^;}]+)",t)); print("  transitions:",sorted(tr)[:6])
        an=set(re.sub(r"\s+"," ",x.strip())[:60] for x in re.findall(r"animation\s*:\s*([^;}]+)",t)); print("  animations:",sorted(an)[:4])
        print("  body font-size:",re.findall(r"body\s*\{[^}]*?font-size\s*:\s*([^;]+)",t,re.S)[:1], " letter-spacing on headings:", sorted(set(re.findall(r"letter-spacing\s*:\s*(-?[\d.]+(?:px|em))",t)))[:4])
        body=re.sub(r"<style.*?</style>|<script.*?</script>","",t,flags=re.S)
        if "marketing" in name:
            secs=re.findall(r"<(section|header|nav|footer)\b[^>]*?(?:class=\"([^\"]*)\"|id=\"([^\"]*)\")?",body)
            print("  order:",[ (a+":"+(b or c or "")).strip(":") for a,b,c in secs][:16])
            print("  kicker/eyebrow/badge in hero:",bool(re.search(r"class=\"[^\"]*(eyebrow|kicker|badge|pill|tag)[^\"]*\"",body[:6000])))
            print("  logo strip:",bool(re.search(r"trusted by|logos|logo-?strip|used by",body,re.I))," testimonial:",bool(re.search(r"testimonial|quote",body,re.I))," faq:",bool(re.search(r"faq|<details",body,re.I))," pricing tiers:",len(re.findall(r"class=\"[^\"]*(?:tier|plan)[^\"]*\"",body))," popular badge:",bool(re.search(r"popular|recommended",body,re.I))," dark cta band:",bool(re.search(r"class=\"[^\"]*(cta|final|closing)[^\"]*\"",body)))
            print("  hero h1:",re.sub(r"<[^>]+>|\s+"," ",(re.findall(r"<h1[^>]*>(.*?)</h1>",body,re.S) or [""])[0]).strip()[:90])
            print("  browser chrome mock:",bool(re.search(r"chrome|window-?bar|dots|traffic",body,re.I))," screenshot/mock:",bool(re.search(r"mock|screenshot|preview|app-window",body,re.I)))
        if "dashboard" in name:
            print("  sidebar:",re.findall(r"grid-template-columns\s*:\s*(\d+px|var\(--sidebar\)) 1fr",t)[:1], resolve("var(--sidebar)",v) if "--sidebar" in v else "", " topbar h:",re.findall(r"(?:topbar|header)[^{]*\{[^}]*?height\s*:\s*(\d+px)",t)[:1])
            print("  greeting:",re.findall(r"Good (?:morning|afternoon|evening)[^<]{0,20}",body)[:1]," stat cards:",len(re.findall(r"class=\"(?:stat|kpi|metric)(?:-card)?\"",body))," table cols:",[re.sub(r"<[^>]+>","",x).strip() for x in re.findall(r"<th[^>]*>(.*?)</th>",body,re.S)][:8])
            print("  search+bell+avatar:",bool(re.search(r"search",body,re.I)),bool(re.search(r"bell|notif",body,re.I)),bool(re.search(r"avatar",body,re.I))," status badges:",bool(re.search(r"badge|status|pill|chip",body,re.I))," sparkline/chart:",bool(re.search(r"<svg|chart",body,re.I))," empty state:",bool(re.search(r"No [a-z]+ yet|Nothing here|empty",body)))
        if "diagram" in name:
            print("  svg texts:",[re.sub(r"<[^>]+>","",x).strip()[:28] for x in re.findall(r"<text[^>]*>(.*?)</text>",t,re.S)][:22])
            print("  layers/bands:",len(re.findall(r"<rect[^>]*(?:rx|ry)=",t))," arrows:",bool(re.search(r"<marker|arrow",t,re.I))," vertical stack?:",len(set(re.findall(r"<rect[^>]*\by=\"(\d+)",t))))
