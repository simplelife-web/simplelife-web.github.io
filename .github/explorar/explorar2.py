import json, re, urllib.request, sys, concurrent.futures as cf
sys.path.insert(0, ".github/precios")
import xlsx
UA={"User-Agent":"SimplelifeBot/1.0 (+https://simplelife-web.github.io/)"}
def get(u,t=120):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=t) as r: return r.read()
    except Exception as e: print("ERR",u,e); return None
x=get("https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Historical-Data-Monthly.xlsx")
if x:
    h=xlsx.leer(x); print("sheets", list(h))
    for name in h:
        rows=h[name]; print("=== ",name, len(rows))
        for i,r in enumerate(rows[:12]): print(i, r)
        for r in rows[-2:]: print(r)
b=get("https://www.fao.org/media/docs/worldfoodsituationlibraries/wfs-library/food_price_indices_data.csv")
if b: t=b.decode("utf-8","replace").splitlines(); print("FAO", len(t)); print("\n".join(t[:8])); print("\n".join(t[-3:]))
b=get("https://api.worldbank.org/v2/es/country?format=json&per_page=400")
if b: d=json.loads(b); print(d[0]); print(d[1][:3])
b=get("https://www.imf.org/external/datamapper/api/v1/PCPIPCH?periods=2024,2025,2026")
print("IMF", b[:400] if b else None)
def bcrp(code):
    b=get(f"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{code}/json/2025-1/2026-12/esp",40)
    if not b: return None
    try:
        d=json.loads(b.decode("utf-8-sig")); s=d["config"]["series"][0]["name"]; p=d.get("periods",[])
        return f"{code}\t{s}\t{p[0]['name'] if p else ''}…{p[-1]['name'] if p else ''}={p[-1]['values'][0] if p else ''}"
    except Exception: return None
codes=[f"PN{n:05d}PM" for n in range(1196,1270)]+["PN38705PM","PN01271PM","PN01309PM"]
with cf.ThreadPoolExecutor(10) as ex:
    for r in ex.map(bcrp, codes):
        if r: print("BCRP", r, flush=True)
