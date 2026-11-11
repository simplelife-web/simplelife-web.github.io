import json, re, urllib.request, io, subprocess, sys
subprocess.run([sys.executable,"-m","pip","install","-q","openpyxl"])
import openpyxl
UA={"User-Agent":"SimplelifeBot/1.0 (+https://simplelife-web.github.io/)"}
def get(u,t=90):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=t) as r: return r.read()
    except Exception as e: print("ERR",u,e); return None
b=get("https://www.worldbank.org/en/research/commodity-markets")
if b:
    for m in sorted(set(re.findall(rb'[^"\' ]*CMO[^"\' ]*\.xlsx', b))): print("link", m.decode())
x=get("https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Historical-Data-Monthly.xlsx")
if x:
    wb=openpyxl.load_workbook(io.BytesIO(x),read_only=True,data_only=True)
    print("sheets", wb.sheetnames)
    ws=wb["Monthly Prices"]
    rows=list(ws.iter_rows(values_only=True))
    for i,r in enumerate(rows[:8]): print(i, r)
    for r in rows[-3:]: print(r)
    ws=wb["Monthly Indices"] if "Monthly Indices" in wb.sheetnames else None
    if ws:
        rows=list(ws.iter_rows(values_only=True))
        for i,r in enumerate(rows[:12]): print("IDX",i, r)
        print(rows[-1])
b=get("https://api.worldbank.org/v2/country/all/indicator/FP.CPI.TOTL.ZG?format=json&per_page=400&date=2023:2025")
if b:
    d=json.loads(b); print(d[0]); print(d[1][:3])
b=get("https://www.imf.org/external/datamapper/api/v1/PCPIPCH?periods=2025,2026")
print("IMF", b[:600] if b else None)
b=get("https://www.imf.org/external/datamapper/api/v1/countries")
print("IMFc", b[:300] if b else None)
