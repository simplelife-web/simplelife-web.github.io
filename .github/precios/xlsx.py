"""Lector mínimo de archivos .xlsx con la biblioteca estándar de Python (sin instalar nada)."""
import io, re, zipfile
import xml.etree.ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}


def _col(ref):
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group(0):
        n = n * 26 + ord(ch) - 64
    return n - 1


def leer(contenido):
    """Devuelve {nombre_hoja: [filas]} con valores de texto o número."""
    z = zipfile.ZipFile(io.BytesIO(contenido))
    compartidos = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            compartidos.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    libro = ET.fromstring(z.read("xl/workbook.xml"))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    destino = {r.get("Id"): r.get("Target") for r in rels}
    hojas = {}
    for h in libro.find("m:sheets", NS):
        rid = h.get("{%s}id" % NS["r"])
        ruta = destino[rid].lstrip("/")
        if not ruta.startswith("xl/"):
            ruta = "xl/" + ruta
        filas = []
        for fila in ET.fromstring(z.read(ruta)).iter("{%s}row" % NS["m"]):
            valores = []
            for c in fila.findall("m:c", NS):
                i = _col(c.get("r"))
                while len(valores) < i:
                    valores.append(None)
                v = c.find("m:v", NS)
                t = c.get("t")
                if t == "s" and v is not None:
                    val = compartidos[int(v.text)]
                elif t == "inlineStr":
                    val = "".join(x.text or "" for x in c.iter("{%s}t" % NS["m"]))
                elif v is not None and v.text is not None:
                    try:
                        val = float(v.text)
                    except ValueError:
                        val = v.text
                else:
                    val = None
                valores.append(val)
            filas.append(valores)
        hojas[h.get("name")] = filas
    return hojas
