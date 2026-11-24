"""Genera la sección «Economía peruana en simple» (/guias/) de Simplelife.

- El contenido de cada guía vive en .github/guias/contenido.py (texto + gráficos).
- Las cifras se calculan aquí con datos oficiales que ya están en el sitio:
  inflacion/ipc.json, precios/peru.json, glosario/cifras.json y guias/datos.json.
- Cada guía tiene una fecha "publicar". Solo salen las guías cuya fecha ya llegó
  (hora de Lima), así se publican de a poco sin que nadie tenga que hacer nada.
- Rehace guias/*.html, la portada de la sección, sus líneas del sitemap y agrega la
  guía nueva a «Novedades» de la portada del sitio.

Uso:
  python3 .github/guias/generar.py                    (rehace todo)
  python3 .github/guias/generar.py --todas            (vista previa con todas, solo para revisar en local)
  python3 .github/guias/generar.py --revisar-enlaces  (comprueba que las fuentes abran)
"""
import html
import json
import os
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from graficos import MESES_L, mes_txt  # noqa: E402
import contenido  # noqa: E402

RAIZ = os.path.normpath(os.path.join(AQUI, "..", ".."))
SALIDA = os.path.join(RAIZ, "guias")
BASE = "https://simplelife-web.github.io/guias/"
HOY = datetime.now(timezone(timedelta(hours=-5))).date()  # Lima
LANZAMIENTO = "2026-11-24"  # las guías de este día van juntas en una sola línea de Novedades


def fecha_larga(iso):
    d = date.fromisoformat(iso[:10])
    return "%d de %s de %d" % (d.day, MESES_L[d.month - 1], d.year)


def leer(ruta):
    try:
        with open(os.path.join(RAIZ, ruta), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def contexto():
    """Junta los datos y deja listas series mes a mes: {"x0": "AAAA-MM", "v": [...]}."""
    D = {"series": {}, "fuentes": {}, "revisado": []}
    ipc = leer("inflacion/ipc.json")
    if ipc:
        idx = ipc["indice"]
        x0 = ipc["desde"]
        inf = [None] * 12 + [(idx[i] / idx[i - 12] - 1) * 100 for i in range(12, len(idx))]
        mes = [None] + [(idx[i] / idx[i - 1] - 1) * 100 for i in range(1, len(idx))]
        D["series"]["inflacion12"] = {"x0": x0, "v": inf}
        D["series"]["inflacion_mes"] = {"x0": x0, "v": mes}
        D["series"]["ipc"] = {"x0": x0, "v": idx}
        D["fuentes"]["ipc"] = ("BCRP, serie %s: %s" % (ipc["serie"], ipc["titulo"]), ipc["enlace"])
        D["revisado"].append(ipc.get("revisado", ""))
    peru = leer("precios/peru.json")
    if peru:
        for r in peru["rubros"]:
            D["series"]["rubro:" + r["codigo"]] = {"x0": r["desde"], "v": r["var"], "nombre": r["nombre"],
                                                  "incluye": r.get("incluye", ""), "oficial": r.get("oficial", "")}
            D["fuentes"]["rubro:" + r["codigo"]] = ("BCRP, serie %s: %s" % (r["codigo"], r.get("oficial", r["nombre"])),
                                                   "https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/%s/html" % r["codigo"])
        tc = peru["tipo_cambio"]
        D["series"]["tc"] = {"x0": tc["desde"], "v": tc["valores"]}
        D["fuentes"]["tc"] = ("BCRP, serie %s: %s" % (tc["codigo"], tc["nombre"]),
                              "https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/%s/html" % tc["codigo"])
        D["revisado"].append(peru.get("revisado", ""))
    cif = leer("glosario/cifras.json")
    if cif:
        D["cifras"] = cif.get("cifras", {})
        D["revisado"].append(cif.get("revisado", ""))
    dat = leer("guias/datos.json")
    if dat:
        for k, s in dat["series"].items():
            D["series"][k] = {"x0": s["desde"], "v": s["valores"], "oficial": s["oficial"], "resumen": s["resumen"]}
            D["fuentes"][k] = ("BCRP, serie %s: %s (%s)" % (s["codigo"], s["oficial"], s["resumen"]), s["enlace"])
        D["revisado"].append(dat.get("revisado", ""))
    D["revisado"] = max([r for r in D["revisado"] if r] or [HOY.isoformat()])
    return D


def ultimo(serie):
    """(mes, valor) del último dato de una serie."""
    for i in range(len(serie["v"]) - 1, -1, -1):
        if serie["v"][i] is not None:
            a, m = int(serie["x0"][:4]), int(serie["x0"][5:7]) - 1 + i
            return "%04d-%02d" % (a + m // 12, m % 12 + 1), serie["v"][i]
    return None, None


def tiene_datos(D, g):
    return all(k in D["series"] and ultimo(D["series"][k])[0] for k in g["necesita"])


CABECERA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo_seo}</title>
<link rel="icon" href="../logo.svg" type="image/svg+xml">
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url}">
<meta property="og:image" content="https://simplelife-web.github.io/og-imagen.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="es_PE">
<meta property="og:title" content="{titulo_seo}">
<meta property="og:site_name" content="Simplelife">
<meta property="og:description" content="{descripcion}">
<meta property="og:type" content="{og_tipo}">
<meta property="og:url" content="{url}">
<script type="application/ld+json">
{ld}
</script>
<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9798339025422593"
     crossorigin="anonymous"></script>
<script src="/anuncios.js" defer></script>
<link rel="stylesheet" href="estilo.css">
<script src="letra.js"></script>
<script src="grafico.js" defer></script>
</head>
<body>
<a class="saltar" href="#contenido">Ir al contenido</a>
<script src="../nav.js"></script>
<header class="top">
  <span class="brand"><a class="hoja" href="../" title="Ir al inicio de Simplelife"><img src="../logo.svg" alt="Inicio Simplelife" width="48" height="48"></a><a class="brand-txt" href="./" title="Ir al inicio de las guías"><span>Economía peruana <b>en simple</b><small>guías con datos oficiales · de Simplelife</small></span></a></span>
  <div class="letra" role="group" aria-label="Tamaño de letra">
    <button type="button" data-letra="-1" aria-label="Letra más pequeña">A−</button>
    <button type="button" data-letra="1" aria-label="Letra más grande">A+</button>
  </div>
</header>
<main id="contenido">
"""

PIE = """</main>
<footer>
  <p><strong>Economía peruana en simple</strong> son guías educativas de Simplelife, escritas con palabras sencillas por un estudiante de Economía. Los gráficos se hacen aquí mismo con datos oficiales del BCRP y se actualizan solos. No es asesoría financiera.</p>
  <p><a href="./">Todas las guías</a> · <a href="../">Inicio Simplelife</a> · <a href="../glosario/">Glosario económico</a> · <a href="../acerca.html">Acerca de</a> · <a href="../contacto.html">Contacto</a> · <a href="../privacidad.html">Privacidad</a></p>
</footer>
</body>
</html>
"""


def ld_json(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def pagina_guia(g, D, previa, siguiente):
    url = BASE + g["slug"] + ".html"
    cuerpo = g["cuerpo"](D)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://simplelife-web.github.io/"},
            {"@type": "ListItem", "position": 2, "name": "Economía peruana en simple", "item": BASE},
            {"@type": "ListItem", "position": 3, "name": g["titulo"], "item": url}]},
        {"@type": "Article", "headline": g["titulo"], "description": g["descripcion"], "inLanguage": "es-PE",
         "datePublished": g["publicar"], "dateModified": D["revisado"], "url": url,
         "image": "https://simplelife-web.github.io/og-imagen.png",
         "author": {"@type": "Person", "name": "Jhonel", "url": "https://simplelife-web.github.io/acerca.html"},
         "publisher": {"@type": "Organization", "name": "Simplelife", "url": "https://simplelife-web.github.io/",
                       "logo": {"@type": "ImageObject", "url": "https://simplelife-web.github.io/logo.svg"}}}]}
    p = [CABECERA.format(titulo_seo=html.escape(g["titulo"] + " | Economía peruana en simple"),
                         descripcion=html.escape(g["descripcion"]), url=url, og_tipo="article", ld=ld_json(ld))]
    p.append('<p class="miga"><a href="./">← Todas las guías</a></p>\n<article>\n')
    p.append('<p class="ent">%s</p>\n' % html.escape(g["tema"]))
    p.append('<h1><span aria-hidden="true">%s</span> %s</h1>\n' % (g["emoji"], html.escape(g["titulo"])))
    p.append('<p class="fecha">Publicada el <time datetime="%s">%s</time> · Datos revisados el <time datetime="%s">%s</time> · Lectura de %d minutos</p>\n' % (
        g["publicar"], fecha_larga(g["publicar"]), D["revisado"], fecha_larga(D["revisado"]), g["minutos"]))
    p.append('<p class="lead"><strong>En corto:</strong> %s</p>\n' % cuerpo["corto"])
    for i, sec in enumerate(cuerpo["secciones"]):
        p.append(sec + "\n")
        if i == 1:
            p.append('<div class="sl-anuncio" data-zona="guia-medio"></div>\n')
    if cuerpo.get("recuerda"):
        p.append('<section class="card ojo">\n<h2>Para recordar</h2>\n<ul>%s</ul>\n</section>\n' % "".join(
            "<li>%s</li>" % x for x in cuerpo["recuerda"]))
    if g.get("herramienta"):
        p.append('<p class="botones"><a class="btn" href="%s">%s</a></p>\n' % g["herramienta"])
    if g.get("glosario"):
        p.append('<section class="rel">\n<h2>Conceptos del glosario</h2>\n<ul class="chips">%s</ul>\n</section>\n' % "".join(
            '<li><a href="../glosario/%s.html">%s</a></li>' % (s, html.escape(t)) for s, t in g["glosario"]))
    nav = []
    if previa:
        nav.append('<a href="%s.html"><small>← Guía anterior</small>%s</a>' % (previa["slug"], html.escape(previa["titulo"])))
    if siguiente:
        nav.append('<a class="sig" href="%s.html"><small>Siguiente guía →</small>%s</a>' % (siguiente["slug"], html.escape(siguiente["titulo"])))
    if nav:
        p.append('<nav class="pasar" aria-label="Otras guías">%s</nav>\n' % "".join(nav))
    fuentes = []
    for f in cuerpo["fuentes"] + g.get("fuentes", []):
        if f not in fuentes:
            fuentes.append(f)
    p.append('<section class="fuentes">\n<h2>Fuentes</h2>\n<ul>%s</ul>\n' % "".join(
        '<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (html.escape(u), html.escape(t)) for t, u in fuentes))
    p.append('<p class="rev">Los gráficos y las cifras de esta guía se calculan con los datos oficiales más recientes; la última revisión fue el %s. Texto escrito con palabras propias.</p>\n</section>\n' % fecha_larga(D["revisado"]))
    p.append('<p class="acciones"><button type="button" class="btn sec" onclick="window.print()">Imprimir esta guía</button></p>\n</article>\n')
    p.append('<div class="sl-anuncio" data-zona="guia-final"></div>\n')
    p.append(PIE)
    return "".join(p)


def portada(publicadas, D):
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://simplelife-web.github.io/"},
            {"@type": "ListItem", "position": 2, "name": "Economía peruana en simple", "item": BASE}]},
        {"@type": "CollectionPage", "name": "Economía peruana en simple", "url": BASE, "inLanguage": "es-PE",
         "hasPart": [{"@type": "Article", "headline": g["titulo"], "url": BASE + g["slug"] + ".html",
                      "datePublished": g["publicar"]} for g in publicadas]}]}
    desc = ("Guías cortas y gratuitas que explican la economía del Perú con palabras sencillas: inflación, dólar, "
            "precios, tasas de interés y más, con gráficos propios hechos con datos oficiales del BCRP.")
    p = [CABECERA.format(titulo_seo="Economía peruana en simple: guías con gráficos y datos del BCRP | Simplelife",
                         descripcion=html.escape(desc), url=BASE, og_tipo="website", ld=ld_json(ld))]
    p.append('<h1>Economía peruana en simple</h1>\n')
    p.append('<p class="lead">Guías cortas para entender lo que pasa con tu bolsillo: por qué suben los precios, '
             'qué mueve al dólar o cómo te afecta lo que decide el Banco Central. Cada guía tiene gráficos hechos aquí '
             'con datos oficiales del BCRP, que se actualizan solos.</p>\n')
    p.append('<ul class="lista" id="lista">\n')
    for g in sorted(publicadas, key=lambda x: x["publicar"], reverse=True):
        p.append('<li><a class="tram" href="%s.html"><span class="ic" aria-hidden="true">%s</span><span><small>%s · %s</small>'
                 '<strong>%s</strong><span class="def">%s</span></span></a></li>\n' % (
                     g["slug"], g["emoji"], html.escape(g["tema"]), fecha_larga(g["publicar"]),
                     html.escape(g["titulo"]), html.escape(g["descripcion"])))
    p.append('</ul>\n')
    p.append('<section class="card">\n<h2>Cómo hacemos estas guías</h2>\n'
             '<p>Cada guía está escrita con palabras propias por un estudiante de Economía. Las cifras no se copian de noticias: '
             'se calculan con las series oficiales del <a href="https://estadisticas.bcrp.gob.pe/estadisticas/series/" target="_blank" rel="noopener">Banco Central de Reserva del Perú (BCRP)</a>, '
             'que a su vez usa datos del INEI y de otras fuentes oficiales. Un robot revisa los datos cada mañana y rehace los gráficos, '
             'por eso cada guía dice hasta qué fecha llegan sus datos.</p>\n'
             '<p>Si una palabra no se entiende, búscala en el <a href="../glosario/">Glosario económico</a>. '
             '¿Encontraste un error o quieres que expliquemos otro tema? <a href="../contacto.html">Escríbenos</a>.</p>\n</section>\n')
    p.append('<div class="sl-anuncio" data-zona="guias-portada"></div>\n')
    p.append(PIE)
    return "".join(p)


def actualizar_sitemap(publicadas, D):
    ruta = os.path.join(RAIZ, "sitemap.xml")
    with open(ruta, encoding="utf-8") as fh:
        lineas = [l for l in fh.read().splitlines() if "/guias/" not in l]
    fin = lineas.index("</urlset>")
    nuevas = ["  <url><loc>%s</loc><lastmod>%s</lastmod></url>" % (BASE, D["revisado"])]
    nuevas += ["  <url><loc>%s%s.html</loc><lastmod>%s</lastmod></url>" % (BASE, g["slug"], D["revisado"])
               for g in sorted(publicadas, key=lambda x: x["publicar"])]
    lineas[fin:fin] = nuevas
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas) + "\n")


def actualizar_novedades(publicadas):
    """Agrega a «Novedades» de la portada las guías publicadas en los últimos 3 días."""
    ruta = os.path.join(RAIZ, "index.html")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    m = re.search(r'(<ul class="novedades">\n)(.*?)(\s*</ul>)', texto, re.S)
    if not m:
        return
    items = re.findall(r"\s*<li>.*?</li>", m.group(2), re.S)
    nuevas = []
    for g in sorted(publicadas, key=lambda x: x["publicar"]):
        if g["publicar"] <= LANZAMIENTO or (HOY - date.fromisoformat(g["publicar"])).days > 3:
            continue
        if ("guias/%s.html" % g["slug"]) in texto:
            continue
        nuevas.insert(0, '\n      <li><time datetime="%s">%s</time>: nueva guía en <a href="guias/">Economía peruana en simple</a>: '
                         '<a href="guias/%s.html">%s</a>.</li>' % (g["publicar"], fecha_larga(g["publicar"]),
                                                                    g["slug"], html.escape(g["titulo"])))
    if not nuevas:
        return
    items = (nuevas + items)[:5]
    texto = texto[:m.start(2)] + "".join(items).lstrip("\n") + texto[m.end(2):]
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write(texto)
    print("Novedades: %d guía(s) nueva(s) en la portada" % len(nuevas))


def revisar_enlaces():
    D = contexto()
    urls = set()
    for g in contenido.GUIAS:
        for _, u in g.get("fuentes", []):
            urls.add(u)
        if tiene_datos(D, g):
            for _, u in g["cuerpo"](D)["fuentes"]:
                urls.add(u)
    malas = 0
    for u in sorted(urls):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (SimplelifeBot; +https://simplelife-web.github.io/)"})
            with urllib.request.urlopen(req, timeout=40) as r:
                print("OK  %s %s" % (r.status, u))
        except Exception as e:  # noqa: BLE001
            malas += 1
            print("MAL %s -> %s" % (u, e))
    print("%d enlaces, %d con problema" % (len(urls), malas))
    return 1 if malas else 0


def main():
    if "--revisar-enlaces" in sys.argv:
        return revisar_enlaces()
    D = contexto()
    todas = "--todas" in sys.argv
    publicadas = []
    for g in contenido.GUIAS:
        if not todas and g["publicar"] > HOY.isoformat():
            continue
        if not tiene_datos(D, g):
            print("Se salta %s: faltan datos %s" % (g["slug"], g["necesita"]))
            continue
        publicadas.append(g)
    publicadas.sort(key=lambda x: (x["publicar"], contenido.GUIAS.index(x)))
    os.makedirs(SALIDA, exist_ok=True)
    paginas = {"index.html": portada(publicadas, D)}
    for i, g in enumerate(publicadas):
        previa = publicadas[i - 1] if i > 0 else None
        siguiente = publicadas[i + 1] if i + 1 < len(publicadas) else None
        paginas[g["slug"] + ".html"] = pagina_guia(g, D, previa, siguiente)
    for nombre in os.listdir(SALIDA):
        if nombre.endswith(".html") and nombre not in paginas:
            os.remove(os.path.join(SALIDA, nombre))
    for nombre, txt in paginas.items():
        txt = re.sub(r"(\d) %", "\\1\u00a0%", txt).replace("S/ ", "S/\u00a0").replace("US$ ", "US$\u00a0")
        with open(os.path.join(SALIDA, nombre), "w", encoding="utf-8") as fh:
            fh.write(txt)
    if not todas:
        actualizar_sitemap(publicadas, D)
        actualizar_novedades(publicadas)
    pend = [g["slug"] + " (" + g["publicar"] + ")" for g in contenido.GUIAS if g not in publicadas]
    print("Listo: %d guías publicadas. En cola: %s" % (len(publicadas), ", ".join(pend) or "ninguna"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
