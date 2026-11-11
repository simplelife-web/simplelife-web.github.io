"""Robot de "Cifras al día" del Glosario económico (Simplelife).

Cada día descarga las cifras oficiales vigentes (tipo de cambio, tasa de referencia,
reservas, inflación, PBI, desempleo, cobre, oro, UIT...) y las guarda en
glosario/cifras.json. El archivo glosario/cifras.js las muestra en un recuadro
"Cifra oficial al día" dentro de cada término relacionado. Las definiciones del
glosario NO se tocan: viven en .github/glosario/ (otro generador).

Uso: python3 .github/cifras/actualizar.py   (Python 3.9 o más, sin instalar nada)
Si una fuente falla, se conserva el último dato bueno de esa cifra.
"""
import html
import json
import os
import re
import time
import urllib.request
from datetime import date, timedelta

RAIZ = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
ARCHIVO = os.path.join(RAIZ, "glosario", "cifras.json")
UA = {"User-Agent": "SimplelifeBot/1.0 (+https://simplelife-web.github.io/glosario/)"}
HOY = date.today()
MES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6, "jul": 7, "ago": 8,
       "sep": 9, "set": 9, "oct": 10, "nov": 11, "dic": 12}
SERIES = "https://estadisticas.bcrp.gob.pe/estadisticas/series/"

# ---------- Cifras del BCRP ----------
# clave: (código, diaria?, nombre que se muestra, unidad, cómo escribir el valor)
BCRP = {
    "tc": ("PD04640PD", True, "Tipo de cambio (venta, sistema bancario)", "soles por dólar", "tc"),
    "tasa_ref": ("PD12301MD", True, "Tasa de referencia del BCRP", "anual", "pct2"),
    "interbancaria": ("PD04692MD", True, "Tasa interbancaria en soles", "anual", "pct2"),
    "rin": ("PD04650MD", True, "Reservas internacionales netas", "millones de dólares", "millones"),
    "inflacion12": ("PN01273PM", False, "Inflación de los últimos 12 meses (Lima)", "", "pct2"),
    "inflacion_mes": ("PN01271PM", False, "Inflación del mes (Lima)", "", "pct2"),
    "tamn": ("PN07807NM", False, "TAMN: tasa promedio de los préstamos en soles", "efectiva anual", "pct2"),
    "tipmn": ("PN07816NM", False, "TIPMN: tasa promedio de los depósitos en soles", "efectiva anual", "pct2"),
    "pbi": ("PN01728AM", False, "Crecimiento del PBI (frente al mismo mes del año anterior)", "", "pct1"),
    "desempleo": ("PN38063GM", False, "Tasa de desempleo en Lima Metropolitana", "promedio móvil de 3 meses", "pct1"),
    "cobre": ("PD04701XD", True, "Precio del cobre (Londres)", "dólares por libra", "cobre"),
    "oro": ("PD04704XD", True, "Precio del oro (Londres)", "dólares por onza troy", "oro"),
    "embig": ("PD04709XD", True, "Riesgo país del Perú (EMBIG)", "puntos básicos", "entero"),
}
# Índice de precios sin alimentos y energía: la inflación subyacente se calcula a 12 meses.
SUBYACENTE = "PN38707PM"

# ---------- Cifras fijadas por norma ----------
# La UIT se lee de la tabla de la SUNAT. La remuneración mínima no tiene una fuente
# que se pueda leer de forma automática: se cambia aquí cuando sale un nuevo decreto.
RMV = {"valor": 1230, "desde": "2026-10-01", "norma": "Decreto Supremo 015-2026-TR",
       "enlace": "https://www.gob.pe/institucion/mtpe/normas-legales"}

# ---------- Qué cifras se muestran en cada término del glosario ----------
TERMINOS = {
    "tipo-de-cambio": ["tc"], "depreciacion-y-apreciacion": ["tc"], "tipo-de-cambio-real": ["tc", "inflacion12"],
    "dolarizacion": ["tc"], "efecto-traspaso": ["tc", "inflacion12"], "intervencion-cambiaria": ["tc", "rin"],
    "tasa-de-referencia": ["tasa_ref", "inflacion12"], "politica-monetaria": ["tasa_ref", "inflacion12"],
    "regla-de-taylor": ["tasa_ref", "inflacion12", "subyacente"], "bcrp": ["tasa_ref", "rin", "inflacion12"],
    "puntos-basicos": ["tasa_ref"], "tasa-de-interes": ["tasa_ref", "tamn", "tipmn"],
    "tasa-de-interes-interbancaria": ["interbancaria", "tasa_ref"],
    "tasa-de-interes-activa-y-pasiva": ["tamn", "tipmn"], "tasa-de-interes-real": ["tasa_ref", "inflacion12"],
    "tea": ["tamn"], "tcea": ["tamn"], "trea": ["tipmn"], "deposito-a-plazo": ["tipmn"],
    "creditos-de-consumo": ["tamn"], "credito-hipotecario": ["tamn"], "encaje-bancario": ["tasa_ref"],
    "reservas-internacionales": ["rin", "tc"], "balanza-de-pagos": ["rin"],
    "inflacion": ["inflacion12", "inflacion_mes"], "ipc": ["inflacion_mes", "inflacion12"],
    "inflacion-subyacente": ["subyacente", "inflacion12"], "poder-adquisitivo": ["inflacion12"],
    "valor-nominal-y-real": ["inflacion12"], "deflacion": ["inflacion_mes", "inflacion12"],
    "hiperinflacion": ["inflacion12"], "estanflacion": ["inflacion12", "pbi"], "expectativas": ["inflacion12", "tasa_ref"],
    "pbi": ["pbi"], "crecimiento-economico": ["pbi"], "ciclo-economico": ["pbi"], "recesion": ["pbi"],
    "brecha-del-producto": ["pbi"], "pbi-per-capita": ["pbi"],
    "tasa-de-desempleo": ["desempleo"], "pea": ["desempleo"], "subempleo": ["desempleo"],
    "terminos-de-intercambio": ["cobre", "oro"], "exportaciones-tradicionales-y-no-tradicionales": ["cobre", "oro"],
    "canon": ["cobre", "oro"], "balanza-comercial": ["cobre", "oro"],
    "riesgo-pais": ["embig"], "grado-de-inversion": ["embig"], "bono-soberano": ["embig"], "calificacion-de-riesgo": ["embig"],
    "uit": ["uit"], "impuesto-a-la-renta": ["uit"],
    "remuneracion-minima-vital": ["rmv"], "gratificacion": ["rmv"], "cts": ["rmv"],
}
# Recuadro de la portada del glosario
PORTADA = ["tc", "tasa_ref", "inflacion12", "rin", "uit", "rmv"]


def traer(url, intentos=4):
    for i in range(1, intentos + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            print(f"  intento {i}: {url} -> {e}")
            time.sleep(4 * i)
    raise RuntimeError(f"No se pudo descargar {url}")


def fecha_bcrp(nombre):
    """'10.Nov.26' -> '2026-11-10'; 'Oct.2026' -> '2026-10'."""
    nombre = str(nombre).strip()
    m = re.match(r"^(\d{1,2})\.([A-Za-z]{3})\.(\d{2})$", nombre)
    if m and m.group(2).lower() in MES:
        return "20%s-%02d-%02d" % (m.group(3), MES[m.group(2).lower()], int(m.group(1)))
    m = re.match(r"^([A-Za-z]{3})\.?\s*(\d{4})$", nombre)
    if m and m.group(1).lower() in MES:
        return "%s-%02d" % (m.group(2), MES[m.group(1).lower()])
    return None


def serie(codigo, diaria, meses=26):
    if diaria:
        rango = f"{(HOY - timedelta(days=60)).isoformat()}/{HOY.isoformat()}"
    else:
        ini = date(HOY.year - (meses // 12) - 1, 1, 1)
        rango = f"{ini.year}-{ini.month}/{HOY.year}-12"
    d = json.loads(traer(f"{SERIES}api/{codigo}/json/{rango}/esp").decode("utf-8-sig"))
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
    return d["config"]["series"][0]["name"], puntos


def enlace_bcrp(codigo, diaria):
    return f"{SERIES}{'diarias' if diaria else 'mensuales'}/resultados/{codigo}/html"


def uit():
    """Lee la tabla de la SUNAT: año, valor y norma. Devuelve la fila del año más reciente."""
    crudo = traer("https://www.sunat.gob.pe/indicestasas/uit.html")
    try:
        texto = crudo.decode("utf-8")
    except UnicodeDecodeError:
        texto = crudo.decode("latin-1")
    texto = html.unescape(re.sub(r"<[^>]+>", " ", texto))
    texto = re.sub(r"\s+", " ", texto)
    filas = re.findall(r"\b(20\d\d) ([\d.,]{4,6}) (D\.\s?S\.[^0-9]*[\d-]+-?EF)", texto)
    if not filas:
        raise RuntimeError("No se encontró la tabla de la UIT en la página de la SUNAT")
    anio, valor, norma = max(filas, key=lambda f: int(f[0]))
    valor = int(re.sub(r"[.,]", "", valor))
    if not 3000 <= valor <= 20000:
        raise RuntimeError(f"Valor de la UIT raro: {valor}")
    norma = re.sub(r"N\S*\s*", "N.° ", norma.replace("D.S.", "Decreto Supremo").replace("D. S.", "Decreto Supremo"), count=1)
    return int(anio), valor, norma.strip()


def main():
    antes = {}
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, encoding="utf-8") as f:
            antes = json.load(f).get("cifras", {})
    cifras = {}

    for clave, (cod, diaria, nombre, unidad, formato) in BCRP.items():
        try:
            oficial, pts = serie(cod, diaria)
            if not pts:
                raise RuntimeError("sin datos recientes")
            f, v = pts[-1]
            cifras[clave] = {"nombre": nombre, "valor": round(v, 6), "unidad": unidad, "formato": formato,
                             "fecha": f, "fuente": "BCRP, serie " + cod, "oficial": oficial,
                             "enlace": enlace_bcrp(cod, diaria)}
            print(f"{clave}: {v} ({f})")
        except Exception as e:  # noqa: BLE001
            print(f"aviso: {clave} ({cod}) falló: {e}")
            if clave in antes:
                cifras[clave] = antes[clave]
        time.sleep(0.5)

    try:
        oficial, pts = serie(SUBYACENTE, False)
        por_mes = dict(pts)
        f = pts[-1][0]
        a, m = int(f[:4]), int(f[5:])
        hace12 = "%d-%02d" % (a - 1, m)
        v = (por_mes[f] / por_mes[hace12] - 1) * 100
        cifras["subyacente"] = {"nombre": "Inflación sin alimentos ni energía, últimos 12 meses (Lima)", "valor": round(v, 6),
                                "unidad": "", "formato": "pct2", "fecha": f,
                                "fuente": "BCRP, serie " + SUBYACENTE + " (cálculo de Simplelife)", "oficial": oficial,
                                "enlace": enlace_bcrp(SUBYACENTE, False)}
        print(f"subyacente: {v:.2f} ({f})")
    except Exception as e:  # noqa: BLE001
        print(f"aviso: subyacente falló: {e}")
        if "subyacente" in antes:
            cifras["subyacente"] = antes["subyacente"]

    try:
        anio, valor, norma = uit()
        cifras["uit"] = {"nombre": "UIT %d" % anio, "valor": valor, "unidad": "", "formato": "soles",
                         "fecha": str(anio), "fuente": "SUNAT, " + norma,
                         "enlace": "https://www.sunat.gob.pe/indicestasas/uit.html"}
        print(f"uit: {valor} ({anio})")
    except Exception as e:  # noqa: BLE001
        print(f"aviso: UIT falló: {e}")
        if "uit" in antes:
            cifras["uit"] = antes["uit"]

    cifras["rmv"] = {"nombre": "Remuneración mínima vital", "valor": RMV["valor"], "unidad": "al mes", "formato": "soles",
                     "fecha": RMV["desde"], "desde": True, "fuente": "MTPE, " + RMV["norma"], "enlace": RMV["enlace"]}

    if len(cifras) < 10:
        raise SystemExit(f"Solo {len(cifras)} cifras: algo anda mal, no se guarda nada")

    salida = {"revisado": HOY.isoformat(),
              "nota": "Cifras oficiales vigentes. Las diarias se publican cada día hábil; las mensuales, una vez al mes.",
              "cifras": cifras,
              "terminos": {k: [c for c in v if c in cifras] for k, v in TERMINOS.items()},
              "portada": [c for c in PORTADA if c in cifras]}
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Guardado: {len(cifras)} cifras, revisado {HOY.isoformat()}.")


if __name__ == "__main__":
    main()
