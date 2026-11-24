"""Robot de datos de las guías «Economía peruana en simple» (Simplelife).

Descarga series oficiales del BCRP (API pública de estadisticas.bcrp.gob.pe) y las
guarda, mes a mes, en guias/datos.json. Las series diarias se resumen en el último
dato de cada mes (tasas) o en el promedio del mes (precios).
La inflación y el tipo de cambio NO se bajan aquí: se leen de inflacion/ipc.json y
precios/peru.json, que ya actualizan otros robots.

Uso: python3 .github/guias/datos.py   (Python 3.9 o más, sin instalar nada)
Si una serie falla, se conserva la última versión buena.
"""
import json
import os
import re
import sys
import time
import urllib.request
from datetime import date

RAIZ = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
ARCHIVO = os.path.join(RAIZ, "guias", "datos.json")
UA = {"User-Agent": "SimplelifeBot/1.0 (+https://simplelife-web.github.io/guias/)"}
API = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"
WEB = "https://estadisticas.bcrp.gob.pe/estadisticas/series/"
MES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6, "jul": 7, "ago": 8,
       "sep": 9, "set": 9, "oct": 10, "nov": 11, "dic": 12}
HOY = date.today()

# clave: lista de intentos (código, "mensual" | "diaria", cómo resumir el mes, desde)
SERIES = {
    "tasa_ref": [("PD12301MD", "diaria", "ultimo", "2003-09-01")],
    "rin": [("PD04650MD", "diaria", "ultimo", "2000-01-01")],  # en millones de US$ (la mensual PN00026MM está en soles)
    "pbi": [("PN01728AM", "mensual", None, "2004-1")],
    "desempleo": [("PN38063GM", "mensual", None, "2001-1")],
    "cobre": [("PN01652XM", "mensual", None, "2000-1"), ("PD04701XD", "diaria", "promedio", "2000-01-01")],
    "embig": [("PN01129XM", "mensual", None, "2000-1")],
    "tamn": [("PN07807NM", "mensual", None, "2000-1")],
    "tipmn": [("PN07816NM", "mensual", None, "2000-1")],
}


def traer(url, intentos=4):
    for i in range(1, intentos + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            print(f"  intento {i}: {url} -> {e}")
            time.sleep(4 * i)
    raise RuntimeError(f"No se pudo descargar {url}")


def fecha_bcrp(nombre):
    nombre = str(nombre).strip()
    m = re.match(r"^(\d{1,2})\.([A-Za-z]{3})\.(\d{2})$", nombre)
    if m and m.group(2).lower() in MES:
        return "20%s-%02d-%02d" % (m.group(3), MES[m.group(2).lower()], int(m.group(1)))
    m = re.match(r"^([A-Za-z]{3})\.?\s*(\d{4})$", nombre)
    if m and m.group(1).lower() in MES:
        return "%s-%02d" % (m.group(2), MES[m.group(1).lower()])
    return None


def bajar(codigo, tipo, resumen, desde):
    hasta = HOY.isoformat() if tipo == "diaria" else f"{HOY.year}-12"
    d = json.loads(traer(f"{API}{codigo}/json/{desde}/{hasta}/esp").decode("utf-8-sig"))
    nombre = d["config"]["series"][0]["name"]
    puntos = []
    for p in d.get("periods", []):
        f = fecha_bcrp(p.get("name"))
        try:
            v = float(str(p["values"][0]).replace(",", "."))
        except (ValueError, KeyError, IndexError):
            continue
        if f:
            puntos.append((f, v))
    puntos.sort()
    if tipo == "diaria":
        meses = {}
        for f, v in puntos:
            meses.setdefault(f[:7], []).append(v)
        puntos = [(m, vs[-1] if resumen == "ultimo" else sum(vs) / len(vs)) for m, vs in sorted(meses.items())]
    if len(puntos) < 24:
        raise RuntimeError(f"{codigo}: muy pocos datos ({len(puntos)})")
    # Serie mensual continua desde el primer mes con dato (None si falta un mes)
    inicio = puntos[0][0]
    vals = dict(puntos)
    a, m = int(inicio[:4]), int(inicio[5:7])
    fin = puntos[-1][0]
    serie = []
    while True:
        k = "%04d-%02d" % (a, m)
        v = vals.get(k)
        serie.append(None if v is None else round(v, 4))
        if k == fin:
            break
        m += 1
        if m == 13:
            a, m = a + 1, 1
    return {
        "codigo": codigo, "oficial": nombre, "desde": inicio, "hasta": fin,
        "resumen": {"ultimo": "último dato del mes", "promedio": "promedio del mes"}.get(resumen, "dato mensual"),
        "enlace": f"{WEB}{'diarias' if tipo == 'diaria' else 'mensuales'}/resultados/{codigo}/html",
        "valores": serie,
    }


def main():
    try:
        with open(ARCHIVO, encoding="utf-8") as fh:
            viejo = json.load(fh)
    except (OSError, ValueError):
        viejo = {"series": {}}
    nuevo = {"fuente": "BCRP, Estadísticas (API pública)", "revisado": HOY.isoformat(), "series": {}}
    fallas = 0
    for clave, intentos in SERIES.items():
        for codigo, tipo, resumen, desde in intentos:
            try:
                nuevo["series"][clave] = bajar(codigo, tipo, resumen, desde)
                s = nuevo["series"][clave]
                print(f"OK {clave} {codigo}: {s['desde']} a {s['hasta']} ({len(s['valores'])} meses) · {s['oficial']}")
                break
            except Exception as e:  # noqa: BLE001
                print(f"FALLA {clave} {codigo}: {e}")
        else:
            fallas += 1
            if clave in viejo.get("series", {}):
                nuevo["series"][clave] = viejo["series"][clave]
                print(f"  se conserva la versión anterior de {clave}")
    if not nuevo["series"]:
        print("Ninguna serie se pudo bajar; no se cambia nada.")
        return 0
    if {k: v for k, v in nuevo.items() if k != "revisado"} == {k: v for k, v in viejo.items() if k != "revisado"}:
        print("Sin datos nuevos.")
        return 0
    with open(ARCHIVO, "w", encoding="utf-8") as fh:
        json.dump(nuevo, fh, ensure_ascii=False, separators=(",", ":"))
    print(f"Guardado {ARCHIVO} ({fallas} series con falla)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
