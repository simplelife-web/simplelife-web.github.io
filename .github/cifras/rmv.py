"""Busca en el diario oficial El Peruano los decretos que cambian la
Remuneración Mínima Vital (RMV, el sueldo mínimo) y lee el monto nuevo y
desde cuándo rige.

Cada día baja los cuadernillos de Normas Legales (ordinarios "NL" y
extraordinarios "EX") que aparecen en busquedas.elperuano.pe, los pasa a texto
con pdftotext (paquete poppler-utils) y busca un Decreto Supremo del sector
Trabajo (…-TR) que mencione la Remuneración Mínima Vital con un monto en soles.
"""
import re
import subprocess
import tempfile
import unicodedata
import urllib.request

PORTADA = "https://busquedas.elperuano.pe/"
UA = {"User-Agent": "SimplelifeBot/1.0 (+https://simplelife-web.github.io/glosario/)"}
MESES = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
         "septiembre": 9, "setiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}


def _plano(s):
    """Sin tildes, en minúsculas y con espacios simples (para buscar sin fallar)."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"-\s*\n\s*", "", s)  # palabras cortadas al final de la línea
    return re.sub(r"\s+", " ", s).lower()


def _monto(txt):
    """'1 300,00' o '1,300.00' o '1300' -> 1300."""
    txt = txt.strip().rstrip(".,")
    m = re.match(r"^(\d{1,2})[ .,]?(\d{3})(?:[.,](\d{2}))?$", txt)
    if m:
        return int(m.group(1) + m.group(2))
    return None


def buscar_en_texto(texto, actual):
    """Devuelve [{valor, desde, norma}] de los decretos -TR que fijan una RMV nueva.

    actual: la RMV vigente; solo se aceptan montos razonables (entre 90 % y 150 % de ella).
    """
    t = _plano(texto)
    hallados = []
    cabeceras = list(re.finditer(r"decreto supremo\s*n[^0-9]{0,4}(\d{3}-\d{4}-tr)\b", t))
    for i, cab in enumerate(cabeceras):
        fin = cabeceras[i + 1].start() if i + 1 < len(cabeceras) else min(len(t), cab.end() + 15000)
        seg = t[max(0, cab.start() - 600):fin]  # la sumilla va justo antes del número
        if "remuneracion minima vital" not in seg:
            continue
        montos = []
        for m in re.finditer(r"remuneracion minima vital", seg):
            ventana = seg[m.start():m.start() + 700]
            for a in re.finditer(r"s/\s?(\d[\d .,]{2,10}\d)", ventana):
                v = _monto(a.group(1))
                if v and actual * 0.9 <= v <= actual * 1.5:
                    montos.append(v)
        if not montos:
            continue
        valor = max(montos)
        desde = None
        f = re.search(r"a partir del?\s+(\d{1,2})\s*[o°º]?\s+de\s+([a-z]+)\s+(?:de|del)\s+(?:ano\s+)?(\d{4})", seg)
        if f and f.group(2) in MESES:
            desde = "%s-%02d-%02d" % (f.group(3), MESES[f.group(2)], int(f.group(1)))
        hallados.append({"valor": valor, "desde": desde, "norma": "Decreto Supremo N.° " + cab.group(1).upper()})
    return hallados


def traer(url, timeout=180):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def pdf_a_texto(datos):
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(datos)
        f.flush()
        r = subprocess.run(["pdftotext", f.name, "-"], capture_output=True, timeout=300)
    return r.stdout.decode("utf-8", "replace")


def dispositivos(fechas, max_paginas=15):
    """Normas de esas fechas (AAAAMMDD), ediciones ordinaria (NL) y extraordinaria (EX), cuya
    sumilla menciona la Remuneración Mínima Vital. Devuelve [(código, url_pdf, sumilla)]."""
    hallados = {}
    for f in fechas:
        for tipo in ("NL", "EX"):
            vistos_pag = set()
            for pag in range(max_paginas):
                url = f"{PORTADA}?fechaIni={f}&fechaFin={f}&tipoPublicacion={tipo}&ci=ONLY&start={pag * 20}"
                try:
                    html = traer(url, 60).decode("utf-8", "replace").replace('\\"', '"')
                except Exception as e:  # noqa: BLE001
                    print(f"  aviso: no se pudo abrir {url}: {e}")
                    break
                pdfs = list(re.finditer(r'/api/archivo/file/[^"\s]+?/\*/(\d+-\d+)\.PDF', html))
                nuevos = [m for m in pdfs if m.group(1) not in vistos_pag]
                if not nuevos:
                    break
                previo = 0
                for m in pdfs:
                    contexto = html[max(previo, m.start() - 1500):m.start()]
                    previo = m.end()
                    vistos_pag.add(m.group(1))
                    if "remuneracion minima vital" in _plano(contexto):
                        hallados[m.group(1)] = (m.group(1), PORTADA.rstrip("/") + m.group(0),
                                                re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", contexto))[-300:])
            print(f"  El Peruano {f} {tipo}: {len(vistos_pag)} normas revisadas")
    return list(hallados.values())


def revisar(actual, fechas):
    """Busca decretos nuevos de la RMV en El Peruano en esas fechas. Devuelve [{valor, desde, norma, pdf}]."""
    salida = []
    for codigo, url, _ in dispositivos(fechas):
        try:
            texto = pdf_a_texto(traer(url))
        except Exception as e:  # noqa: BLE001
            print(f"  aviso: no se pudo leer {url}: {e}")
            continue
        for h in buscar_en_texto(texto, actual):
            h["pdf"] = url
            salida.append(h)
    return salida


if __name__ == "__main__":
    # Prueba: python3 rmv.py 1130 20260928 [más fechas]
    import sys
    print(revisar(int(sys.argv[1]), sys.argv[2:]))
