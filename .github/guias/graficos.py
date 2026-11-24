"""Gráficos propios (SVG estático) para las guías de Simplelife.

Cada gráfico sale dos veces: una versión ancha (computadora) y una angosta (celular),
para que las letras se lean bien en los dos. El archivo guias/grafico.js agrega el
cursor con el valor exacto al pasar el dedo o el mouse. Debajo de cada gráfico va una
tabla con los datos (para lectores de pantalla y para quien prefiera números).
"""
import html
import json
import math

MESES = ["ene.", "feb.", "mar.", "abr.", "may.", "jun.", "jul.", "ago.", "set.", "oct.", "nov.", "dic."]
MESES_L = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "setiembre",
           "octubre", "noviembre", "diciembre"]


def num(v, dec=1):
    """3.14159 -> '3.1'; 100302.1 -> '100 302' (espacio fino que no se corta)."""
    if v is None:
        return "—"
    neg = v < 0
    s = "%.*f" % (dec, abs(v))
    ent, _, fr = s.partition(".")
    if len(ent) > 4:  # 1500 se escribe junto; 10 000 lleva espacio
        grupos = []
        while len(ent) > 3:
            grupos.insert(0, ent[-3:])
            ent = ent[:-3]
        ent = "\u202f".join([ent] + grupos)
    s = ent
    if fr:
        s += "." + fr
    return ("−" if neg else "") + s


def mes_txt(ym, largo=False):
    a, m = int(ym[:4]), int(ym[5:7])
    return ("%s de %d" % (MESES_L[m - 1], a)) if largo else ("%s %d" % (MESES[m - 1], a))


def ym_mas(ym, n):
    a, m = int(ym[:4]), int(ym[5:7]) - 1 + n
    return "%04d-%02d" % (a + m // 12, m % 12 + 1)


def _paso_bonito(rango, objetivo):
    crudo = rango / max(objetivo, 1)
    mag = 10 ** math.floor(math.log10(crudo)) if crudo > 0 else 1
    for f in (1, 2, 2.5, 5, 10):
        if f * mag >= crudo:
            return f * mag
    return 10 * mag


def _eje_y(lo, hi, marcas):
    if hi == lo:
        hi = lo + 1
    paso = _paso_bonito(hi - lo, marcas)
    lo2 = math.floor(lo / paso) * paso
    hi2 = math.ceil(hi / paso) * paso
    ticks, t = [], lo2
    while t <= hi2 + paso / 1000:
        ticks.append(round(t, 10))
        t += paso
    return lo2, hi2, ticks, paso


def _svg_linea(series, x0, n, w, h, unidad, dec, banda, cero, fs, marcas_y, cada_anios, titulo):
    ml, mr, mt, mb = fs * 3.4, fs * 0.8, fs * 0.9, fs * 2.2
    pw, ph = w - ml - mr, h - mt - mb
    vals = [v for s in series for v in s["v"] if v is not None]
    lo, hi = min(vals), max(vals)
    if banda:
        lo, hi = min(lo, banda[0]), max(hi, banda[1])
    if cero:
        lo = min(lo, 0)
    lo, hi, ticks, paso = _eje_y(lo, hi, marcas_y)
    X = lambda i: ml + pw * i / max(n - 1, 1)  # noqa: E731
    Y = lambda v: mt + ph * (1 - (v - lo) / (hi - lo))  # noqa: E731
    p = []
    p.append('<svg class="graf" viewBox="0 0 %d %d" role="img" aria-label="%s" data-g=\'%s\'>' % (
        w, h, html.escape(titulo),
        html.escape(json.dumps({"x0": x0, "n": n, "ml": ml, "pw": pw, "mt": mt, "ph": ph, "lo": lo, "hi": hi,
                                "u": unidad, "d": dec,
                                "s": [{"n": s["nombre"], "c": s["clase"], "v": s["v"]} for s in series]},
                               separators=(",", ":")), quote=True)))
    p.append('<style>.graf text{font-size:%spx}</style>' % fs)
    if banda:
        # banda: (mínimo, máximo, desde qué mes, texto)
        i0 = 0
        if banda[2]:
            a = (int(banda[2][:4]) - int(x0[:4])) * 12 + int(banda[2][5:7]) - int(x0[5:7])
            i0 = max(0, min(n - 1, a))
        p.append('<rect class="g-banda" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>' % (
            X(i0), Y(banda[1]), X(n - 1) - X(i0), Y(banda[0]) - Y(banda[1])))
    for t in ticks:
        p.append('<line class="g-rejilla%s" x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f"/>' % (
            " g-cero" if t == 0 else "", ml, ml + pw, Y(t), Y(t)))
        p.append('<text class="g-eje" x="%.1f" y="%.1f" text-anchor="end">%s%s</text>' % (
            ml - 6, Y(t) + fs * 0.35, num(t, 0 if paso >= 1 else 1 if abs(paso * 10 - round(paso * 10)) < 1e-9 else 2), unidad if unidad == "%" else ""))
    # Marcas de años
    a0 = int(x0[:4])
    a1 = int(ym_mas(x0, n - 1)[:4])
    primero = a0 + (0 if x0[5:7] == "01" else 1)
    primero += (-primero) % cada_anios
    for a in range(primero, a1 + 1, cada_anios):
        i = (a - a0) * 12 - (int(x0[5:7]) - 1)
        if 0 <= i < n:
            p.append('<line class="g-marca" x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f"/>' % (X(i), X(i), mt + ph, mt + ph + 5))
            p.append('<text class="g-eje" x="%.1f" y="%.1f" text-anchor="middle">%d</text>' % (X(i), mt + ph + fs * 1.4, a))
    for s in series:
        d, pluma = [], "M"
        for i, v in enumerate(s["v"]):
            if v is None:
                pluma = "M"
                continue
            d.append("%s%.1f %.1f" % (pluma, X(i), Y(v)))
            pluma = "L"
        p.append('<path class="g-linea %s" d="%s"/>' % (s["clase"], "".join(d)))
        ult = max(i for i, v in enumerate(s["v"]) if v is not None)
        p.append('<circle class="g-punto %s" cx="%.1f" cy="%.1f" r="4"/>' % (s["clase"], X(ult), Y(s["v"][ult])))
    p.append('<rect class="g-toque" x="%.1f" y="%.1f" width="%.1f" height="%.1f"/>' % (ml, mt, pw, ph))
    p.append("</svg>")
    return "".join(p)


def linea(titulo, series, x0, unidad="%", dec=1, banda=None, cero=False, nota="", tabla_cada="dic", tabla_extra=None):
    """series: [{"nombre":..., "clase": "s1"|"s2"|"s3", "v": [valores mes a mes desde x0]}]."""
    n = max(len(s["v"]) for s in series)
    for s in series:
        s["v"] = list(s["v"]) + [None] * (n - len(s["v"]))
    anios = (n - 1) / 12
    ancho = _svg_linea(series, x0, n, 720, 380, unidad, dec, banda, cero, 14, 6,
                       1 if anios <= 8 else 2 if anios <= 16 else 5, titulo)
    angosto = _svg_linea(series, x0, n, 380, 300, unidad, dec, banda, cero, 13, 5,
                         2 if anios <= 8 else 5 if anios <= 25 else 10, titulo)
    leyenda = ""
    if len(series) > 1:
        leyenda = '<ul class="g-leyenda">' + "".join(
            '<li><span class="g-clave %s"></span>%s</li>' % (s["clase"], html.escape(s["nombre"])) for s in series) + "</ul>"
    # Tabla: un dato por año (diciembre, o el último mes disponible del año)
    filas = []
    ult_i = max(i for i in range(n) if any(s["v"][i] is not None for s in series))
    for i in range(n):
        ym = ym_mas(x0, i)
        if (tabla_cada == "dic" and ym.endswith("-12")) or i == ult_i:
            celdas = "".join("<td>%s%s</td>" % (num(s["v"][i], dec), " %" if unidad == "%" and s["v"][i] is not None else "")
                             for s in series)
            filas.append("<tr><th scope=\"row\">%s</th>%s</tr>" % (mes_txt(ym), celdas))
        if i == ult_i:
            break
    cab = "".join("<th scope=\"col\">%s</th>" % html.escape(s["nombre"]) for s in series)
    tabla = ('<details class="g-datos"><summary>Ver los datos del gráfico</summary><div class="g-tabla"><table>'
             '<thead><tr><th scope="col">Mes</th>%s</tr></thead><tbody>%s</tbody></table></div>'
             '<p class="nota">Un dato por año: diciembre de cada año y el último mes publicado.%s</p></details>') % (
        cab, "".join(reversed(filas)), (" " + tabla_extra) if tabla_extra else "")
    return ('<figure class="grafico"><figcaption>%s</figcaption>%s<div class="g-ancho">%s</div><div class="g-angosto">%s</div>'
            '%s%s</figure>') % (html.escape(titulo), leyenda, ancho, angosto,
                                ('<p class="g-nota">%s</p>' % nota) if nota else "", tabla)


def barras(titulo, items, unidad="%", dec=1, nota="", destacar=None):
    """Barras horizontales en HTML/CSS (se leen bien en cualquier pantalla).
    items: [(nombre, valor)] ya ordenados."""
    hi = max(max(v for _, v in items), 0)
    lo = min(min(v for _, v in items), 0)
    rango = (hi - lo) or 1
    filas = []
    for nombre, v in items:
        izq = (min(v, 0) - lo) / rango * 100
        anc = abs(v) / rango * 100
        filas.append(
            '<li%s><span class="b-nombre">%s</span><span class="b-pista"><span class="b-barra%s" style="left:%.2f%%;width:%.2f%%"></span></span>'
            '<span class="b-valor">%s%s</span></li>' % (
                ' class="b-dest"' if destacar and nombre in destacar else "", html.escape(nombre),
                " b-neg" if v < 0 else "", izq, max(anc, 0.6), ("+" if v > 0 else ""), num(v, dec) + (" %" if unidad == "%" else unidad)))
    return '<figure class="grafico barras"><figcaption>%s</figcaption><ul class="b-lista">%s</ul>%s</figure>' % (
        html.escape(titulo), "".join(filas), ('<p class="g-nota">%s</p>' % nota) if nota else "")
