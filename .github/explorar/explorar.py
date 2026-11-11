# Exploración temporal (se borra antes de publicar): imprime nombres de series y enlaces.
import json, re, urllib.request, concurrent.futures as cf
UA={"User-Agent":"SimplelifeBot/1.0 (+https://simplelife-web.github.io/)"}
def get(u,t=40):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=t) as r: return r.read()
    except Exception as e: return None
def bcrp(code, freq):
    rng = "2024-1/2025-12" if freq=="M" else ("2024-1-1/2024-1-31" if freq=="D" else "2023/2025")
    b=get(f"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{code}/json/{rng}/esp")
    if not b: return None
    try:
        d=json.loads(b.decode("utf-8-sig")); s=d["config"]["series"][0]["name"]; p=d.get("periods",[])
        return f"{code}\t{s}\t{p[-1]['name'] if p else ''}={p[-1]['values'][0] if p else ''}"
    except Exception: return None
codes=[]
codes+= [f"PN{n:05d}PM" for n in range(38700,38900)]
codes+= [f"PN{n:05d}PM" for n in range(1270,1400)]
codes+= [f"PN{n:05d}XM" for n in range(1640,1720)]
codes+= [f"PN{n:05d}PM" for n in range(39000,39100)]
with cf.ThreadPoolExecutor(10) as ex:
    for r in ex.map(lambda c: bcrp(c,"M"), codes):
        if r: print("BCRP", r, flush=True)
for u in ["https://www.worldbank.org/en/research/commodity-markets"]:
    b=get(u); print("WB page", u, bool(b))
    if b:
        for m in sorted(set(re.findall(rb'https?://[^"\' ]+\.xlsx', b))): print("  xlsx", m.decode())
for u in ["https://api.worldbank.org/v2/country/all/indicator/FP.CPI.TOTL.ZG?format=json&per_page=3&date=2024",
          "https://www.imf.org/external/datamapper/api/v1/PCPIPCH/PER",
          "https://www.fao.org/worldfoodsituation/foodpricesindex/en/",
          "https://fred.stlouisfed.org/graph/fredgraph.csv?id=PCOPPUSDM"]:
    b=get(u); print("URL", u, (b[:300] if b else None))
b=get("https://www.fao.org/worldfoodsituation/foodpricesindex/en/")
if b:
    for m in sorted(set(re.findall(rb'[^"\' ]+\.(?:csv|xlsx)', b))): print("  fao", m.decode())
