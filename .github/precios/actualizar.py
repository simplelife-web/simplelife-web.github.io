"""Robot de "Precios del Perú y del mundo" (Simplelife).

Descarga datos oficiales y gratuitos y los guarda en precios/*.json.
La página solo lee esos archivos; no se conecta a ninguna fuente.

  - peru.json   BCRP (con datos del INEI): variación mensual del IPC de Lima por rubro
                y tipo de cambio.
  - mundo.json  Banco Mundial, "Pink Sheet": precios mensuales de unas 70 materias primas
                y sus índices por grupo. FAO: índice de precios de los alimentos.
  - paises.json FMI, Perspectivas de la Economía Mundial: inflación anual por país.
                Banco Mundial: nombres de países y regiones en español.

Uso: python3 .github/precios/actualizar.py   (Python 3.9 o más, sin instalar nada)
Si una fuente falla, se conserva el archivo anterior y las demás se actualizan igual.
"""
import csv, io, json, os, re, sys, time, urllib.request
from datetime import date

sys.path.insert(0, os.path.dirname(__file__))
import xlsx  # noqa: E402

RAIZ = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
CARPETA = os.path.join(RAIZ, "precios")
UA = {"User-Agent": "SimplelifeBot/1.0 (+https://simplelife-web.github.io/precios/)"}
HOY = date.today()
MES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6, "jul": 7, "ago": 8,
       "sep": 9, "set": 9, "oct": 10, "nov": 11, "dic": 12}


def traer(url, intentos=4, espera=60):
    for i in range(1, intentos + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=espera) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            print(f"  intento {i}: {url} -> {e}")
            time.sleep(4 * i)
    raise RuntimeError(f"No se pudo descargar {url}")


def k(anio, mes):
    return anio * 12 + mes - 1


def clave(n):
    return f"{n // 12}-{n % 12 + 1:02d}"


def serie_continua(puntos):
    """puntos: {indice_mes: valor} -> (desde, [valores]) con None en huecos."""
    if not puntos:
        return None, []
    a, b = min(puntos), max(puntos)
    return clave(a), [puntos.get(n) for n in range(a, b + 1)]


def fin(desde, valores):
    """Último mes con dato de una serie que empieza en 'desde' (AAAA-MM)."""
    n = k(int(desde[:4]), int(desde[5:])) + len(valores) - 1
    while valores and valores[n - k(int(desde[:4]), int(desde[5:]))] is None:
        n -= 1
    return clave(n)


def guardar(nombre, datos, minimo):
    """Escribe el JSON solo si cambió algo además de la fecha de revisión."""
    ruta = os.path.join(CARPETA, nombre)
    if os.path.exists(ruta):
        with open(ruta, encoding="utf-8") as f:
            antes = json.load(f)
        a, b = dict(antes), dict(datos)
        a.pop("revisado", None), b.pop("revisado", None)
        if a == b:
            print(f"{nombre}: sin cambios.")
            return
    if not minimo(datos):
        raise RuntimeError(f"{nombre}: datos incompletos, no se guarda nada")
    os.makedirs(CARPETA, exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")
    print(f"{nombre}: guardado.")


# ---------------------------------------------------------------- Perú (BCRP)
RUBROS = [
    # (código BCRP de variación % mensual, nombre, qué incluye)
    ("PN01271PM", "Inflación total (IPC)", "Todos los bienes y servicios de la canasta familiar de Lima Metropolitana."),
    ("PN01383PM", "Alimentos y bebidas", "Comida y bebidas que se compran para el hogar: mercado, bodega y supermercado."),
    ("PN01308PM", "Alimentos de precio volátil", "Alimentos cuyo precio sube y baja mucho, como verduras, frutas, pollo y pescado."),
    ("PN01302PM", "Comidas fuera del hogar", "Menú, restaurantes, pollerías y comida al paso."),
    ("PN01309PM", "Combustibles", "Gasolina, diésel (petróleo), gas de cocina (GLP) y GNV."),
    ("PN01310PM", "Transporte", "Pasajes urbanos e interprovinciales, taxis y pasajes aéreos."),
    ("PN01311PM", "Luz, agua y teléfono", "Tarifas de servicios públicos: electricidad, agua y telefonía."),
    ("PN01305PM", "Alquiler de vivienda", "Lo que se paga por alquilar casa o departamento."),
    ("PN01303PM", "Educación", "Pensiones de colegios, universidades e institutos, y útiles."),
    ("PN01304PM", "Salud", "Consultas médicas, medicinas, análisis y seguros de salud."),
    ("PN01298PM", "Ropa y calzado", "Prendas de vestir, zapatos y su confección o reparación."),
    ("PN01299PM", "Electrodomésticos", "Refrigeradoras, cocinas, televisores, lavadoras y similares."),
    ("PN01300PM", "Otros productos industriales", "Artículos de limpieza, aseo personal, muebles, medicinas y más."),
    ("PN01306PM", "Otros servicios", "Servicios personales y del hogar, cuidado personal, recreación, seguros y más."),
    ("PN01317PM", "Productos importados", "Parte de la canasta que viene del extranjero o depende de precios internacionales."),
    ("PN01286PM", "Precios al por mayor", "Lo que pagan comercios y empresas al comprar en grandes cantidades (no es del IPC)."),
]
TIPO_CAMBIO = ("PN01210PM", "Tipo de cambio bancario promedio (soles por dólar)")


def bcrp(codigos, desde="1992-1"):
    url = (f"https://estadisticas.bcrp.gob.pe/estadisticas/series/api/{'-'.join(codigos)}"
           f"/json/{desde}/{HOY.year}-12/esp")
    d = json.loads(traer(url).decode("utf-8-sig"))
    nombres = [s["name"] for s in d["config"]["series"]]
    puntos = [dict() for _ in codigos]
    for p in d.get("periods", []):
        m = re.match(r"^([A-Za-z]{3})\.?\s*(\d{4})$", str(p["name"]).strip())
        if not m or m.group(1).lower() not in MES:
            continue
        n = k(int(m.group(2)), MES[m.group(1).lower()])
        for i, v in enumerate(p.get("values", [])):
            try:
                x = float(str(v).replace(",", "."))
            except ValueError:
                continue
            puntos[i][n] = x
    return nombres, puntos


def peru():
    rubros = []
    for i in range(0, len(RUBROS), 8):  # de 8 en 8 para no pedir una URL enorme
        grupo = RUBROS[i:i + 8]
        nombres, puntos = bcrp([g[0] for g in grupo])
        for (cod, nom, desc), oficial, pts in zip(grupo, nombres, puntos):
            desde, vals = serie_continua(pts)
            if not vals:
                print(f"  aviso: {cod} vino vacía")
                continue
            rubros.append({"codigo": cod, "nombre": nom, "incluye": desc, "oficial": oficial,
                           "desde": desde, "var": [None if v is None else round(v, 4) for v in vals]})
        time.sleep(1)
    _, pts = bcrp([TIPO_CAMBIO[0]])
    desde, vals = serie_continua(pts[0])
    datos = {
        "fuente": "BCRP, Estadísticas (con datos del INEI)",
        "enlace": "https://estadisticas.bcrp.gob.pe/estadisticas/series/",
        "hasta": max(fin(r["desde"], r["var"]) for r in rubros),
        "revisado": HOY.isoformat(),
        "rubros": rubros,
        "tipo_cambio": {"codigo": TIPO_CAMBIO[0], "nombre": TIPO_CAMBIO[1], "desde": desde,
                        "valores": [None if v is None else round(v, 4) for v in vals]},
    }
    guardar("peru.json", datos, lambda d: len(d["rubros"]) >= 12 and len(d["tipo_cambio"]["valores"]) > 300)


# ------------------------------------------------------- Mundo (Banco Mundial)
# Nombre en inglés (como viene en el Excel) -> (nombre en español, grupo, relación con el Perú)
PRODUCTOS = {
    "Crude oil, average": ("Petróleo crudo (promedio)", "Energía", "importa"),
    "Crude oil, Brent": ("Petróleo Brent", "Energía", ""),
    "Crude oil, Dubai": ("Petróleo Dubái", "Energía", ""),
    "Crude oil, WTI": ("Petróleo WTI", "Energía", "importa"),
    "Coal, Australian": ("Carbón (Australia)", "Energía", ""),
    "Coal, South African": ("Carbón (Sudáfrica)", "Energía", ""),
    "Natural gas, US": ("Gas natural (EE. UU.)", "Energía", ""),
    "Natural gas, Europe": ("Gas natural (Europa)", "Energía", ""),
    "Liquefied natural gas, Japan": ("Gas natural licuado (Japón)", "Energía", "exporta"),
    "Natural gas index": ("Índice de gas natural", "Energía", ""),
    "Cocoa": ("Cacao", "Bebidas", "exporta"),
    "Coffee, Arabica": ("Café arábica", "Bebidas", "exporta"),
    "Coffee, Robusta": ("Café robusta", "Bebidas", ""),
    "Tea, avg 3 auctions": ("Té (promedio de 3 subastas)", "Bebidas", ""),
    "Tea, Colombo": ("Té (Colombo)", "Bebidas", ""),
    "Tea, Kolkata": ("Té (Calcuta)", "Bebidas", ""),
    "Tea, Mombasa": ("Té (Mombasa)", "Bebidas", ""),
    "Coconut oil": ("Aceite de coco", "Aceites y harinas", ""),
    "Groundnuts": ("Maní", "Aceites y harinas", ""),
    "Fish meal": ("Harina de pescado", "Aceites y harinas", "exporta"),
    "Groundnut oil": ("Aceite de maní", "Aceites y harinas", ""),
    "Palm oil": ("Aceite de palma", "Aceites y harinas", ""),
    "Palm kernel oil": ("Aceite de palmiste", "Aceites y harinas", ""),
    "Soybeans": ("Soya en grano", "Aceites y harinas", ""),
    "Soybean oil": ("Aceite de soya", "Aceites y harinas", "importa"),
    "Soybean meal": ("Harina de soya", "Aceites y harinas", "importa"),
    "Rapeseed oil": ("Aceite de colza (canola)", "Aceites y harinas", ""),
    "Sunflower oil": ("Aceite de girasol", "Aceites y harinas", ""),
    "Barley": ("Cebada", "Granos", ""),
    "Maize": ("Maíz amarillo", "Granos", "importa"),
    "Sorghum": ("Sorgo", "Granos", ""),
    "Rice, Thai 5%": ("Arroz (Tailandia, 5 % quebrado)", "Granos", ""),
    "Rice, Thai 25%": ("Arroz (Tailandia, 25 % quebrado)", "Granos", ""),
    "Rice, Thai A.1": ("Arroz (Tailandia, A.1)", "Granos", ""),
    "Rice, Viet Namese 5%": ("Arroz (Vietnam, 5 % quebrado)", "Granos", ""),
    "Wheat, US SRW": ("Trigo blando (EE. UU.)", "Granos", "importa"),
    "Wheat, US HRW": ("Trigo duro (EE. UU.)", "Granos", "importa"),
    "Banana, Europe": ("Plátano (Europa)", "Otros alimentos", "exporta"),
    "Banana, US": ("Plátano (EE. UU.)", "Otros alimentos", ""),
    "Orange": ("Naranja", "Otros alimentos", ""),
    "Beef": ("Carne de res", "Otros alimentos", ""),
    "Chicken": ("Pollo", "Otros alimentos", ""),
    "Lamb": ("Cordero", "Otros alimentos", ""),
    "Shrimps, Mexican": ("Langostinos (México)", "Otros alimentos", ""),
    "Sugar, EU": ("Azúcar (Unión Europea)", "Otros alimentos", ""),
    "Sugar, US": ("Azúcar (EE. UU.)", "Otros alimentos", ""),
    "Sugar, world": ("Azúcar (mercado mundial)", "Otros alimentos", "importa"),
    "Tobacco, US import u.v.": ("Tabaco (EE. UU.)", "Materias primas", ""),
    "Logs, Cameroon": ("Troncos de madera (Camerún)", "Materias primas", ""),
    "Logs, Malaysian": ("Troncos de madera (Malasia)", "Materias primas", ""),
    "Sawnwood, Cameroon": ("Madera aserrada (Camerún)", "Materias primas", ""),
    "Sawnwood, Malaysian": ("Madera aserrada (Malasia)", "Materias primas", ""),
    "Plywood": ("Madera contrachapada (triplay)", "Materias primas", ""),
    "Cotton, A Index": ("Algodón", "Materias primas", ""),
    "Rubber, TSR20": ("Caucho TSR20", "Materias primas", ""),
    "Rubber, RSS3": ("Caucho RSS3", "Materias primas", ""),
    "Phosphate rock": ("Roca fosfórica", "Fertilizantes", "exporta"),
    "DAP": ("Fosfato diamónico (DAP)", "Fertilizantes", ""),
    "TSP": ("Superfosfato triple (TSP)", "Fertilizantes", ""),
    "Urea": ("Urea", "Fertilizantes", "importa"),
    "Potassium chloride": ("Cloruro de potasio", "Fertilizantes", ""),
    "Aluminum": ("Aluminio", "Metales y minerales", ""),
    "Iron ore, cfr spot": ("Mineral de hierro", "Metales y minerales", "exporta"),
    "Copper": ("Cobre", "Metales y minerales", "exporta"),
    "Lead": ("Plomo", "Metales y minerales", "exporta"),
    "Tin": ("Estaño", "Metales y minerales", "exporta"),
    "Nickel": ("Níquel", "Metales y minerales", ""),
    "Zinc": ("Zinc", "Metales y minerales", "exporta"),
    "Gold": ("Oro", "Metales preciosos", "exporta"),
    "Platinum": ("Platino", "Metales preciosos", ""),
    "Silver": ("Plata", "Metales preciosos", "exporta"),
}
UNIDADES = {
    "$/bbl": "US$ por barril", "$/mt": "US$ por tonelada", "$/mmbtu": "US$ por millón de BTU",
    "$/kg": "US$ por kilo", "$/cubic meter": "US$ por metro cúbico", "cents/sheet": "centavos de US$ por plancha",
    "$/dmtu": "US$ por tonelada seca", "$/troy oz": "US$ por onza troy", "2010=100": "índice 2010 = 100",
}
# Columnas de la hoja "Monthly Indices" (2010 = 100)
INDICES = [
    (1, "Índice total de materias primas"), (2, "Energía"), (3, "No energéticos"), (4, "Agricultura"),
    (5, "Bebidas"), (6, "Alimentos"), (7, "Aceites y harinas"), (8, "Granos"), (9, "Otros alimentos"),
    (10, "Materias primas agrícolas"), (13, "Fertilizantes"), (14, "Metales y minerales"),
    (15, "Metales básicos (sin hierro)"), (16, "Metales preciosos"),
]
DESDE_MUNDO = k(1990, 1)
PINK_RESPALDO = ("https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/"
                 "related/CMO-Historical-Data-Monthly.xlsx")


def limpiar(nombre):
    return re.sub(r"\s+", " ", str(nombre or "").replace("*", "")).strip()


def num(v):
    return v if isinstance(v, float) else None


def mes_pink(v):
    m = re.match(r"^(\d{4})M(\d{2})$", str(v or "").strip())
    return k(int(m.group(1)), int(m.group(2))) if m else None


def url_pink():
    try:
        html = traer("https://www.worldbank.org/en/research/commodity-markets").decode("utf-8", "replace")
        m = re.findall(r"https://thedocs\.worldbank\.org/[^\"' ]+CMO-Historical-Data-Monthly\.xlsx", html)
        if m:
            return m[0]
    except RuntimeError as e:
        print(f"  aviso: {e}")
    return PINK_RESPALDO


def pink():
    url = url_pink()
    print(f"Pink Sheet: {url}")
    hojas = xlsx.leer(traer(url, espera=120))
    filas = hojas["Monthly Prices"]
    actualizado = next((limpiar(f[0]).replace("Updated on ", "") for f in filas[:6] if f and "Updated" in str(f[0])), "")
    cab = next(i for i, f in enumerate(filas) if f and len(f) > 5 and limpiar(f[1]).startswith("Crude oil"))
    nombres, unidades = filas[cab], filas[cab + 1]
    datos = [f for f in filas[cab + 2:] if f and mes_pink(f[0]) is not None]
    productos = []
    for j in range(1, len(nombres)):
        ing = limpiar(nombres[j])
        if not ing:
            continue
        es, grupo, peru_rel = PRODUCTOS.get(ing, (ing, "Otros", ""))
        if ing not in PRODUCTOS:
            print(f"  aviso: producto nuevo sin traducir: {ing}")
        u = limpiar(unidades[j] if j < len(unidades) else "").strip("()")
        pts = {}
        for f in datos:
            n = mes_pink(f[0])
            v = num(f[j]) if j < len(f) else None
            if n >= DESDE_MUNDO and v is not None:
                pts[n] = v
        desde, vals = serie_continua(pts)
        if len([v for v in vals if v is not None]) < 24:
            continue
        productos.append({"id": re.sub(r"[^a-z0-9]+", "-", ing.lower()).strip("-"), "nombre": es, "ingles": ing,
                          "grupo": grupo, "peru": peru_rel, "unidad": UNIDADES.get(u, u), "desde": desde, "valores": vals})
    filas = hojas["Monthly Indices"]
    indices = []
    for col, nom in INDICES:
        pts = {}
        for f in filas:
            n = mes_pink(f[0] if f else None)
            if n is not None and n >= DESDE_MUNDO and col < len(f) and num(f[col]) is not None:
                pts[n] = f[col]
        desde, vals = serie_continua(pts)
        indices.append({"nombre": nom, "desde": desde, "valores": vals})
    return url, actualizado, productos, indices


def fao():
    url = "https://www.fao.org/media/docs/worldfoodsituationlibraries/wfs-library/food_price_indices_data.csv"
    texto = traer(url).decode("utf-8-sig", "replace")
    filas = list(csv.reader(io.StringIO(texto)))
    cab = next(i for i, f in enumerate(filas) if f and f[0].strip() == "Date")
    nombres = {"Food Price Index": "Índice general de alimentos", "Meat": "Carnes", "Dairy": "Lácteos",
               "Cereals": "Cereales", "Oils": "Aceites vegetales", "Sugar": "Azúcar"}
    cols = [(j, nombres.get(c.strip(), c.strip())) for j, c in enumerate(filas[cab]) if j > 0 and c.strip()]
    series = {j: {} for j, _ in cols}
    for f in filas[cab + 1:]:
        m = re.match(r"^(\d{4})-(\d{2})$", f[0].strip()) if f else None
        if not m:
            continue
        n = k(int(m.group(1)), int(m.group(2)))
        for j, _ in cols:
            try:
                series[j][n] = float(f[j])
            except (ValueError, IndexError):
                pass
    salida = []
    for j, nom in cols:
        desde, vals = serie_continua(series[j])
        salida.append({"nombre": nom, "desde": desde, "valores": vals})
    return url, salida


def mundo():
    url, actualizado, productos, indices = pink()
    try:
        fao_url, fao_series = fao()
    except Exception as e:  # noqa: BLE001
        print(f"  aviso: FAO falló ({e}); se conserva el dato anterior")
        fao_url, fao_series = None, None
        ruta = os.path.join(CARPETA, "mundo.json")
        if os.path.exists(ruta):
            with open(ruta, encoding="utf-8") as f:
                viejo = json.load(f).get("fao") or {}
            fao_url, fao_series = viejo.get("enlace"), viejo.get("series")
    datos = {
        "fuente": "Banco Mundial, Commodity Price Data (The Pink Sheet)",
        "enlace": "https://www.worldbank.org/en/research/commodity-markets",
        "archivo": url,
        "publicado": actualizado,
        "revisado": HOY.isoformat(),
        "productos": productos,
        "indices": indices,
        "fao": {"fuente": "FAO, Índice de precios de los alimentos (2014-2016 = 100)",
                "enlace": "https://www.fao.org/worldfoodsituation/foodpricesindex/es/",
                "archivo": fao_url, "series": fao_series},
    }
    guardar("mundo.json", datos, lambda d: len(d["productos"]) >= 50)


# ------------------------------------------------------------ Países (FMI)
def paises():
    fmi = json.loads(traer("https://www.imf.org/external/datamapper/api/v1/PCPIPCH"))["values"]["PCPIPCH"]
    wb = json.loads(traer("https://api.worldbank.org/v2/es/country?format=json&per_page=400"))[1]
    info = {c["id"]: c for c in wb if c.get("region", {}).get("id") not in (None, "", "NA")}
    anios = list(range(2000, HOY.year + 3))
    lista = []
    for iso, vals in fmi.items():
        if iso not in info:
            continue  # agregados (mundo, regiones) y códigos que no son países
        fila = [None if vals.get(str(a)) is None else round(float(vals[str(a)]), 2) for a in anios]
        if all(v is None for v in fila):
            continue
        c = info[iso]
        lista.append({"iso": iso, "nombre": c["name"], "region": c["region"]["value"].strip(), "valores": fila})
    lista.sort(key=lambda p: p["nombre"])
    datos = {
        "fuente": "FMI, Perspectivas de la Economía Mundial (WEO): inflación, precios promedio al consumidor (var. % anual)",
        "enlace": "https://www.imf.org/external/datamapper/PCPIPCH@WEO",
        "revisado": HOY.isoformat(),
        "anios": anios,
        # Desde este año, las cifras son estimaciones o proyecciones del FMI.
        "proyeccion_desde": HOY.year,
        "paises": lista,
    }
    guardar("paises.json", datos, lambda d: len(d["paises"]) >= 150)


if __name__ == "__main__":
    fallas = []
    for nombre, tarea in (("Perú", peru), ("Mundo", mundo), ("Países", paises)):
        print(f"--- {nombre}")
        try:
            tarea()
        except Exception as e:  # noqa: BLE001
            print(f"ERROR en {nombre}: {e}")
            fallas.append(nombre)
    if len(fallas) == 3:
        sys.exit(1)
    if fallas:
        print("Se actualizó lo demás. Fallaron: " + ", ".join(fallas))
