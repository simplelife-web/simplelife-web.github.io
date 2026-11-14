# -*- coding: utf-8 -*-
"""
Genera las páginas del Glosario económico (carpeta glosario/) a partir de
terminos1.py y terminos2.py, y actualiza sitemap.xml.

Uso (desde la raíz del repositorio):
    npm i --prefix /tmp/kt katex@0.16.11      # solo la primera vez
    KATEX=/tmp/kt/node_modules/katex python3 .github/glosario/generar.py

Las fórmulas se dibujan con KaTeX al generar, así la página no necesita
JavaScript para mostrarlas (solo katex/katex.min.css y sus fuentes).
"""
import html
import json
import os
import re
import subprocess
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
SALIDA = os.path.join(RAIZ, "glosario")
sys.path.insert(0, AQUI)

import terminos1  # noqa: E402
import terminos2  # noqa: E402
import terminos3  # noqa: E402
import terminos4  # noqa: E402
import terminos5  # noqa: E402
import terminos6  # noqa: E402
import terminos7  # noqa: E402
import terminos8  # noqa: E402
import terminos9  # noqa: E402
import terminos10  # noqa: E402
from fuentes import FUENTES, BCRP_TITULOS  # noqa: E402

BCRP_GLOSARIO = "https://www.bcrp.gob.pe/docs/Publicaciones/Glosario/Glosario-BCRP.pdf"

SITIO = "https://simplelife-web.github.io"
BASE = SITIO + "/glosario/"
REVISADO = "11 de noviembre de 2026"
REVISADO_ISO = "2026-11-11"

CATEGORIAS = [
    ("precios", "Precios e inflación"),
    ("produccion", "Producción y crecimiento"),
    ("dinero", "Dinero, bancos y tasas"),
    ("finanzas", "Finanzas personales"),
    ("trabajo", "Trabajo y pensiones"),
    ("impuestos", "Impuestos"),
    ("estado", "Estado y finanzas públicas"),
    ("comercio", "Comercio exterior"),
    ("mercados", "Mercados y empresas"),
    ("bienestar", "Pobreza y desigualdad"),
]
NOMBRE_CAT = dict(CATEGORIAS)

ORG = {"@type": "Organization", "name": "Simplelife", "url": SITIO + "/",
       "logo": SITIO + "/logo.svg", "email": "simplelifecontacto899@gmail.com"}


def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def esc(s):
    return html.escape(s, quote=True)


def texto_plano(s):
    """Quita etiquetas HTML y fórmulas para usar el texto en metadatos o en el buscador."""
    s = re.sub(r"\\\((.*?)\\\)", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(re.sub(r"\s+", " ", s)).strip()


TERMINOS = terminos1.T + terminos2.T + terminos3.T + terminos4.T + terminos5.T + terminos6.T + terminos7.T + terminos8.T + terminos9.T + terminos10.T


def _sin_barras(v):
    # En las cadenas r"..." un \" queda con la barra; en el HTML debe ser solo ".
    if isinstance(v, str):
        return v.replace('\\"', '"')
    if isinstance(v, list):
        return [_sin_barras(x) for x in v]
    if isinstance(v, tuple):
        return tuple(_sin_barras(x) for x in v)
    if isinstance(v, dict):
        return {k: _sin_barras(x) for k, x in v.items()}
    return v


TERMINOS = [_sin_barras(t) for t in TERMINOS]
TERMINOS.sort(key=lambda t: sin_tildes(t["t"]))
POR_SLUG = {t["slug"]: t for t in TERMINOS}
assert len(POR_SLUG) == len(TERMINOS), "Hay slugs repetidos"
for t in TERMINOS:
    assert t["cat"] in NOMBRE_CAT, t["slug"]
    for r in t.get("rel", []):
        assert r in POR_SLUG, (t["slug"], r)

# ---------- KaTeX: junta todas las fórmulas y las dibuja de una vez ----------
PEDIDOS = []


def pedir(tex, display):
    PEDIDOS.append((tex, display))
    return "\x00K%d\x00" % (len(PEDIDOS) - 1)


def con_formulas(texto):
    """Cambia \\( ... \\) del texto por una marca que luego se reemplaza por KaTeX."""
    return re.sub(r"\\\((.*?)\\\)", lambda m: pedir(m.group(1), False), texto)


def apilar(tex):
    """Pone una debajo de otra las partes de una fórmula separadas por \\qquad o ,\\quad (mejor en celulares)."""
    partes = [x.strip().rstrip(",") for x in re.split(r",?\\qquad|,\\quad", tex) if x.strip()]
    if len(partes) == 1:
        return tex
    return r"\begin{gathered}" + r" \\[6pt] ".join(partes) + r"\end{gathered}"


# ---------- Piezas comunes ----------
CABEZA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="icon" href="../logo.svg" type="image/svg+xml">
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:image" content="https://simplelife-web.github.io/og-imagen.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="es_PE">
<script type="application/ld+json">
{ld}
</script>
<meta property="og:title" content="{title}">
<meta property="og:site_name" content="Simplelife">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{ogtype}">
<meta property="og:url" content="{url}">
<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9798339025422593"
     crossorigin="anonymous"></script>
{extra}<link rel="stylesheet" href="estilo.css">
<script src="letra.js"></script>
<script src="formulas.js" defer></script>
</head>
<body>
<a class="saltar" href="#contenido">Ir al contenido</a>
<script src="../nav.js"></script>
<header class="top">
  <span class="brand"><a class="hoja" href="../" title="Ir al inicio de Simplelife"><img src="../logo.svg" alt="Inicio Simplelife" width="48" height="48"></a><a class="brand-txt" href="./" title="Ir al inicio del glosario"><span>Glosario <b>económico</b><small>explicado en simple · de Simplelife</small></span></a></span>
  <div class="letra" role="group" aria-label="Tamaño de letra">
    <button type="button" data-letra="-1" aria-label="Letra más pequeña">A−</button>
    <button type="button" data-letra="1" aria-label="Letra más grande">A+</button>
  </div>
</header>
<main id="contenido">
"""

PIE = """</main>
<footer>
  <p><strong>Glosario económico</strong> es contenido educativo de Simplelife, escrito con palabras sencillas. Los ejemplos con números son para practicar; las cifras oficiales están en el INEI, el BCRP, la SUNAT y la SBS. No es asesoría financiera ni legal.</p>
  <p><a href="./">Todo el glosario</a> · <a href="../">Inicio Simplelife</a> · <a href="../tramites/">Trámites</a> · <a href="../acerca.html">Acerca de</a> · <a href="../contacto.html">Contacto</a> · <a href="../privacidad.html">Privacidad</a></p>
</footer>
</body>
</html>
"""


def migas(*items):
    lista = [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]
    return {"@type": "BreadcrumbList", "itemListElement": lista}


def ld_json(graph):
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


# ---------- Página de cada término ----------
def pagina_termino(t, i):
    url = BASE + t["slug"] + ".html"
    f = t.get("formula")
    if f:
        title = "%s: qué es, fórmula y ejemplo | Glosario económico" % t["t"]
    else:
        title = "%s: qué es y ejemplo en el Perú | Glosario económico" % t["t"]
    desc = texto_plano(t["corto"])
    ld = ld_json([
        migas(("Inicio", SITIO + "/"), ("Glosario económico", BASE), (t["t"], url)),
        {"@type": "DefinedTerm", "name": t["t"], "description": desc, "url": url, "inLanguage": "es-PE",
         "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "Glosario económico de Simplelife", "url": BASE}},
        {"@type": "Article", "headline": t["t"] + ": qué es, explicado en simple", "description": desc, "inLanguage": "es-PE",
         "dateModified": REVISADO_ISO, "mainEntityOfPage": url, "image": SITIO + "/og-imagen.png", "author": ORG, "publisher": ORG},
    ])
    o = [CABEZA.format(title=esc(title), desc=esc(desc), url=url, ld=ld, ogtype="article",
                       extra='<link rel="stylesheet" href="katex/katex.min.css">\n')]
    o.append('<p class="miga"><a href="./">← Todo el glosario</a></p>\n<article>\n')
    o.append('<p class="ent">%s</p>\n' % esc(NOMBRE_CAT[t["cat"]]))
    o.append('<h1><span aria-hidden="true">%s</span> %s</h1>\n' % (t["ic"], esc(t["t"])))
    o.append('<p class="lead"><strong>En una frase:</strong> %s</p>\n\n' % con_formulas(t["corto"]))

    o.append('<section class="card">\n<h2>Explicado en simple</h2>\n')
    for p in t["simple"]:
        o.append("<p>%s</p>\n" % con_formulas(p))
    o.append("</section>\n\n")

    if f:
        o.append('<section class="card formula">\n<h2>La fórmula</h2>\n')
        o.append('<div class="ecuacion">%s</div>\n' % pedir(apilar(f["tex"]), True))
        if f.get("donde"):
            o.append('<p class="donde-t">Donde:</p>\n<ul class="donde">\n')
            for sim, sig in f["donde"]:
                o.append("<li>%s: %s</li>\n" % (pedir(sim, False), esc(sig)))
            o.append("</ul>\n")
        if f.get("calculo"):
            o.append('<p class="donde-t">Ejemplo de cálculo:</p>\n<div class="calculo">\n')
            for linea in f["calculo"]:
                o.append('<div class="ecuacion">%s</div>\n' % pedir(apilar(linea), True))
            o.append("</div>\n")
        o.append("</section>\n\n")

    o.append('<section class="card">\n<h2>Ejemplo en el Perú</h2>\n')
    for p in t["ejemplo"]:
        o.append("<p>%s</p>\n" % con_formulas(p))
    o.append("</section>\n\n")

    if t.get("herramienta"):
        texto, href = t["herramienta"]
        o.append('<p class="botones"><a class="btn" href="%s">%s →</a></p>\n\n' % (esc(href), esc(texto)))

    if t.get("ojo"):
        o.append('<section class="card ojo">\n<h2>Ten en cuenta</h2>\n<ul>')
        o.append("".join("<li>%s</li>" % con_formulas(x) for x in t["ojo"]))
        o.append("</ul>\n</section>\n\n")

    if t.get("rel"):
        o.append('<section class="rel">\n<h2>Términos relacionados</h2>\n<ul class="chips">')
        for r in t["rel"]:
            o.append('<li><a href="%s.html">%s</a></li>' % (r, esc(POR_SLUG[r]["t"])))
        o.append("</ul>\n</section>\n\n")

    ant = TERMINOS[i - 1] if i > 0 else None
    sig = TERMINOS[i + 1] if i + 1 < len(TERMINOS) else None
    o.append('<nav class="pasar" aria-label="Otros términos">')
    o.append('<a href="%s.html"><small>← Anterior</small>%s</a>' % (ant["slug"], esc(ant["t"])) if ant else "<span></span>")
    o.append('<a class="sig" href="%s.html"><small>Siguiente →</small>%s</a>' % (sig["slug"], esc(sig["t"])) if sig else "<span></span>")
    o.append("</nav>\n\n")

    fs = list(FUENTES.get(t["slug"], []))
    titulo_bcrp = t.get("bcrp") or BCRP_TITULOS.get(t["slug"])
    if titulo_bcrp:
        fs.insert(0, ("BCRP, Glosario de términos económicos: «%s» (definición redactada aquí con palabras propias)" % titulo_bcrp, BCRP_GLOSARIO))
    o.append('<section class="fuentes">\n<h2>Fuentes</h2>\n')
    if fs:
        o.append("<ul>" + "".join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (esc(u), esc(n)) for n, u in fs) + "</ul>\n")
    else:
        o.append("<p>Es un concepto de teoría económica general, que no depende de una norma ni de una cifra oficial del Perú. "
                 "Los números del ejemplo son para practicar.</p>\n")
    o.append('<p class="rev">Revisado el %s.</p>\n</section>\n' % REVISADO)
    o.append('<p class="acciones"><button type="button" class="btn sec" onclick="window.print()">Imprimir este término</button></p>\n')
    o.append("</article>\n")
    o.append(PIE)
    return "".join(o)


# ---------- Portada del glosario ----------
def pagina_indice():
    url = BASE
    title = "Glosario económico explicado en simple | Inflación, PBI, TEA, CTS y más"
    desc = ("%d conceptos de economía y finanzas explicados con palabras sencillas, con ejemplos del Perú "
            "y fórmulas: inflación, PBI, TEA, TCEA, CTS, UIT, IGV, tipo de cambio y más. Gratis.") % len(TERMINOS)
    ld = ld_json([
        migas(("Inicio", SITIO + "/"), ("Glosario económico", url)),
        {"@type": "DefinedTermSet", "name": "Glosario económico de Simplelife", "url": url, "inLanguage": "es-PE",
         "description": desc, "publisher": ORG,
         "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t["t"], "url": BASE + t["slug"] + ".html"} for t in TERMINOS]},
    ])
    o = [CABEZA.format(title=esc(title), desc=esc(desc), url=url, ld=ld, ogtype="website", extra="")]
    o.append("<h1>Glosario económico explicado en simple</h1>\n")
    o.append('<p class="lead">%d conceptos de economía y finanzas con palabras de todos los días, ejemplos del Perú y la fórmula bien explicada. '
             "Sirve para entender las noticias, tu boleta de pago, un préstamo o tus clases.</p>\n" % len(TERMINOS))
    o.append('<label class="buscar"><span>¿Qué palabra buscas?</span>\n'
             '<input type="search" id="q" placeholder="Por ejemplo: inflación, TCEA, CTS" autocomplete="off"></label>\n')
    o.append('<div class="filtros" role="group" aria-label="Filtrar por tema">')
    o.append('<button type="button" data-cat="" aria-pressed="true">Todos</button>')
    usadas = {t["cat"] for t in TERMINOS}
    for c, n in CATEGORIAS:
        if c in usadas:
            o.append('<button type="button" data-cat="%s" aria-pressed="false">%s</button>' % (c, esc(n)))
    o.append("</div>\n")
    o.append('<p id="nada" class="hidden">No encontramos esa palabra. Prueba con otra o <a href="../contacto.html">sugiérenos un término</a>.</p>\n')
    o.append('<p id="cuantos" class="cuantos" aria-live="polite"></p>\n')
    o.append('<div class="lista" id="lista">')
    for t in TERMINOS:
        b = sin_tildes(" ".join([t["t"], t.get("alias", ""), texto_plano(t["corto"]), NOMBRE_CAT[t["cat"]]]))
        o.append('<a class="tram" href="%s.html" data-cat="%s" data-b="%s">\n  <span class="ic" aria-hidden="true">%s</span>\n'
                 '  <span><small>%s</small><strong>%s</strong><span class="def">%s</span></span>\n</a>'
                 % (t["slug"], t["cat"], esc(b), t["ic"], esc(NOMBRE_CAT[t["cat"]]), esc(t["t"]), esc(texto_plano(t["corto"]))))
    o.append("</div>\n\n")
    o.append("""<section class="card">
<h2>¿Cómo está hecho este glosario?</h2>
<p>Cada término tiene una frase corta para entenderlo rápido, una explicación más completa, un ejemplo con situaciones del Perú y, cuando hace falta, su fórmula con el significado de cada letra y un cálculo paso a paso.</p>
<p>Cada página termina con sus <strong>fuentes</strong>: el Glosario de términos económicos del BCRP (que usamos como guía, explicando cada término con nuestras propias palabras), normas publicadas en El Peruano (como la Constitución o las leyes de la TCEA y de pensiones), publicaciones del INEI y la SUNAT, y notas de la agencia estatal Andina con datos del BCRP o del INEI. Los datos que cambian con el tiempo, como la UIT o el sueldo mínimo, indican su año. Los demás números son ejemplos para practicar.</p>
<p>¿Falta una palabra o encontraste un error? <a href="../contacto.html">Escríbenos</a> y la revisamos.</p>
</section>
<script>
(function(){
  var q=document.getElementById('q'), it=document.querySelectorAll('.tram'), nada=document.getElementById('nada'),
      cu=document.getElementById('cuantos'), bs=document.querySelectorAll('.filtros button'), cat='';
  function n(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}
  function filtrar(){
    var v=n(q.value.trim()), c=0;
    it.forEach(function(a){var ok=(!cat||a.dataset.cat===cat)&&(!v||a.dataset.b.indexOf(v)>-1); a.hidden=!ok; if(ok)c++;});
    nada.classList.toggle('hidden',c>0);
    cu.textContent=(v||cat)&&c?(c===1?'1 término':c+' términos'):'';
  }
  q.addEventListener('input',filtrar);
  bs.forEach(function(b){b.addEventListener('click',function(){
    cat=b.dataset.cat; bs.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');}); filtrar();
  });});
})();
</script>
""")
    o.append(PIE)
    return "".join(o)


def main():
    paginas = {"index.html": pagina_indice()}
    for i, t in enumerate(TERMINOS):
        paginas[t["slug"] + ".html"] = pagina_termino(t, i)

    env = dict(os.environ)
    res = subprocess.run(["node", os.path.join(AQUI, "katex-render.cjs")], input=json.dumps(PEDIDOS),
                         capture_output=True, text=True, env=env)
    if res.returncode != 0:
        sys.exit("Error de KaTeX:\n" + res.stderr)
    dibujos = json.loads(res.stdout)

    # Borra páginas viejas de términos que ya no existen
    for nombre in os.listdir(SALIDA):
        if nombre.endswith(".html") and nombre not in paginas:
            os.remove(os.path.join(SALIDA, nombre))
    for nombre, contenido in paginas.items():
        # Espacio que no se corta: "8 %", "S/ 20", "7 UIT" no se parten al final de una línea
        contenido = re.sub(r"(\d) (%|UIT)", "\\1\u00a0\\2", contenido)
        contenido = contenido.replace("S/ ", "S/\u00a0").replace("US$ ", "US$\u00a0")
        contenido = re.sub("\x00K(\\d+)\x00", lambda m: dibujos[int(m.group(1))], contenido)
        with open(os.path.join(SALIDA, nombre), "w", encoding="utf-8") as fh:
            fh.write(contenido)

    # sitemap.xml: quita las líneas viejas del glosario y agrega las nuevas al final
    ruta = os.path.join(RAIZ, "sitemap.xml")
    with open(ruta, encoding="utf-8") as fh:
        lineas = [l for l in fh.read().splitlines() if "/glosario/" not in l]
    fin = lineas.index("</urlset>")
    nuevas = ["  <url><loc>%s</loc><lastmod>%s</lastmod></url>" % (BASE, REVISADO_ISO)]
    nuevas += ["  <url><loc>%s%s.html</loc><lastmod>%s</lastmod></url>" % (BASE, t["slug"], REVISADO_ISO) for t in TERMINOS]
    lineas[fin:fin] = nuevas
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas) + "\n")
    print("Listo: %d términos, %d fórmulas." % (len(TERMINOS), len(PEDIDOS)))


if __name__ == "__main__":
    main()
