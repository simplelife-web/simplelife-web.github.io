"""Contenido de las guías «Economía peruana en simple».

Reglas:
- Texto con palabras propias, nada copiado. Toda cifra sale de los datos (D) y se
  calcula al generar, así el texto nunca queda viejo ni contradice al gráfico.
- Las frases que dependen de un dato (sube, baja, dentro o fuera de la meta) se
  eligen con condiciones, para que sigan siendo ciertas cuando cambien los datos.
- "publicar" = día (hora de Lima) en que la guía sale sola. Ritmo: martes y viernes.
- "necesita" = series que deben existir; si falta una, la guía espera.
"""
from graficos import barras, linea, mes_txt, num, ym_mas

GLOSARIO_PDF = ("BCRP, Glosario de términos económicos (definiciones redactadas aquí con palabras propias)",
                "https://www.bcrp.gob.pe/docs/Publicaciones/Glosario/Glosario-BCRP.pdf")
ANDINA_METAS = ("Andina: el BCRP y su esquema de metas de inflación (desde 2002; rango de 1 % a 3 %)",
                "https://andina.pe/agencia/noticia-bcr-peru-acumulo-27-anos-seguidos-inflacion-un-digito-974574.aspx")


# ---------- utilidades ----------
def puntos(s, desde=None):
    """[(mes, valor)] sin vacíos, opcionalmente desde un mes."""
    out = []
    for i, v in enumerate(s["v"]):
        if v is None:
            continue
        ym = ym_mas(s["x0"], i)
        if desde and ym < desde:
            continue
        out.append((ym, v))
    return out


def recorte(s, desde):
    """Serie mes a mes que empieza en 'desde' (o en su primer dato)."""
    if desde <= s["x0"]:
        return s["x0"], list(s["v"])
    k = (int(desde[:4]) - int(s["x0"][:4])) * 12 + int(desde[5:7]) - int(s["x0"][5:7])
    return desde, list(s["v"][k:])


def valor_en(s, ym):
    k = (int(ym[:4]) - int(s["x0"][:4])) * 12 + int(ym[5:7]) - int(s["x0"][5:7])
    return s["v"][k] if 0 <= k < len(s["v"]) else None


def pct(v, dec=1):
    return num(v, dec) + " %"


def card(titulo, *parrafos):
    return '<section class="card">\n<h2>%s</h2>\n%s\n</section>' % (titulo, "\n".join(
        p if p.startswith("<") else "<p>%s</p>" % p for p in parrafos))


def acumulada(var, desde, hasta):
    """Variación acumulada (%) a partir de variaciones mensuales (%), de 'desde' (excluido) a 'hasta'."""
    f = 1.0
    for ym, v in puntos(var, ym_mas(desde, 1)):
        if ym > hasta:
            break
        f *= 1 + v / 100
    return (f - 1) * 100


def indice_desde(var, base):
    """Índice = 100 en 'base' a partir de variaciones mensuales; None antes de la base."""
    x0, vals = recorte(var, base)
    out, f = [], 100.0
    for i, v in enumerate(vals):
        if i == 0:
            out.append(100.0)
            continue
        if v is None:
            out.append(None)
            continue
        f *= 1 + v / 100
        out.append(f)
    return x0, out


# ---------- 1. Inflación ----------
def inflacion(D):
    s = D["series"]["inflacion12"]
    ym, v = puntos(s)[-1]
    ym_mes, v_mes = puntos(D["series"]["inflacion_mes"])[-1]
    hace12 = valor_en(s, ym_mas(ym, -12))
    p03 = puntos(s, "2003-01")
    maximo = max(p03, key=lambda p: p[1])
    dentro = [p for p in puntos(s, "2007-01") if 1 <= p[1] <= 3]
    total07 = len(puntos(s, "2007-01"))
    dic92 = valor_en(s, "1992-12")
    if v > 3:
        estado = "Está <strong>por encima</strong> del rango meta del BCRP, que va de 1 % a 3 %."
    elif v < 1:
        estado = "Está <strong>por debajo</strong> del rango meta del BCRP, que va de 1 % a 3 %."
    else:
        estado = "Está <strong>dentro</strong> del rango meta del BCRP, que va de 1 % a 3 %."
    if hace12 is not None:
        cambio = ("Hace un año, en %s, era %s." % (mes_txt(ym_mas(ym, -12), True), pct(hace12, 2)))
    else:
        cambio = ""
    x0, vals = recorte(s, "2003-01")
    graf = linea("Inflación de los últimos 12 meses en Lima Metropolitana (%)",
                 [{"nombre": "Inflación a 12 meses", "clase": "s1", "v": vals}], x0, unidad="%", dec=2,
                 banda=(1, 3, "2007-01", "Rango meta: 1 % a 3 %"), cero=True,
                 nota="La franja verde es el rango meta del BCRP desde 2007. Cálculo propio con el índice de precios al consumidor de Lima (BCRP, serie PN38705PM).")
    cien = 100 / (1 + v / 100)
    secciones = [
        card("Qué es la inflación",
             "La inflación es la subida <strong>general</strong> de los precios. No basta con que suba el limón o el pasaje: "
             "hay inflación cuando sube el costo de casi todo lo que compra una familia. Por eso se mide con una canasta grande, "
             "con cientos de productos y servicios, desde el arroz y el menú hasta el alquiler y las pensiones del colegio.",
             "En el Perú, el INEI anota cada mes los precios de esa canasta en Lima Metropolitana y arma el "
             "<a href=\"../glosario/ipc.html\">índice de precios al consumidor (IPC)</a>. Si el índice sube 5 % en un año, "
             "quiere decir que, en promedio, la misma canasta cuesta 5 % más que doce meses antes."),
        card("Cómo va hoy",
             "En %s, la inflación de los últimos 12 meses en Lima fue de <strong>%s</strong>. %s %s"
             % (mes_txt(ym, True), pct(v, 2), estado, cambio),
             "Solo en el mes de %s, los precios variaron %s frente al mes anterior. Un mes aislado puede saltar por algo puntual "
             "(una mala cosecha, el precio del petróleo, una fiesta), por eso los economistas miran sobre todo la cifra de 12 meses."
             % (mes_txt(ym_mes, True), pct(v_mes, 2)),
             graf),
        card("Treinta años en un gráfico",
             "Hoy cuesta imaginarlo, pero a inicios de los noventa el Perú salía de una hiperinflación. Todavía en diciembre de 1992 "
             "los precios subían %s en un año, según el mismo índice del BCRP. Desde 2002, el Banco Central trabaja con "
             "<a href=\"../glosario/meta-de-inflacion.html\">metas de inflación</a>: anuncia qué inflación busca y usa sus herramientas "
             "para llegar a ella." % pct(dic92, 1),
             "Desde 2007 la meta es 2 %% al año, con un margen de un punto hacia arriba o hacia abajo (de 1 %% a 3 %%). Desde enero de 2007, "
             "la inflación de 12 meses estuvo dentro de ese rango en %d de %d meses, es decir, %s del tiempo. El pico más alto desde 2003 "
             "fue %s, en %s." % (len(dentro), total07, pct(len(dentro) / total07 * 100, 0), pct(maximo[1], 2), mes_txt(maximo[0], True))),
        card("Por qué la meta no es cero",
             "Podría parecer que lo ideal es que los precios nunca suban, pero una inflación de cero es peligrosa: con muy poco margen, "
             "un golpe a la economía puede llevar a la <a href=\"../glosario/deflacion.html\">deflación</a>, cuando la gente aplaza sus compras "
             "esperando precios más bajos y las ventas y el empleo se frenan. Además, los índices de precios suelen sobrestimar un poco la subida real "
             "del costo de vida, porque no recogen del todo las mejoras de calidad.",
             "Una inflación baja y estable, alrededor de 2 %, deja planear: los negocios pueden fijar precios, los bancos prestar a plazos "
             "largos en soles y las familias ahorrar sin ver que su dinero se derrite."),
        card("Qué significa para tu bolsillo",
             "Con una inflación de %s, lo que hace un año comprabas con S/ 100 hoy cuesta, en promedio, S/ %s. Visto al revés, "
             "tus 100 soles de hoy rinden como S/ %s de hace un año." % (pct(v, 2), num(100 + v, 2), num(cien, 2)),
             "Por eso importa que un sueldo o un ahorro crezcan <em>más</em> que la inflación: si tu depósito paga 3 %% al año y la inflación es "
             "%s, en la práctica tu dinero %s. A esa diferencia se le llama "
             "<a href=\"../glosario/tasa-de-interes-real.html\">tasa de interés real</a>."
             % (pct(v, 2), "pierde poder de compra" if v > 3 else "apenas gana poder de compra" if v < 3 else "queda igual")),
    ]
    return {
        "corto": "La inflación es cuánto suben, en promedio, los precios de lo que compra una familia. En %s fue de %s en los "
                 "últimos 12 meses en Lima. El BCRP busca que se quede entre 1 %% y 3 %% al año." % (mes_txt(ym, True), pct(v, 2)),
        "secciones": secciones,
        "recuerda": [
            "Que la inflación baje no significa que los precios bajen: significa que suben más despacio.",
            "La cifra que más se mira es la de 12 meses; la de un solo mes puede saltar por algo pasajero.",
            "Tu ahorro y tu sueldo ganan poder de compra solo si crecen más que la inflación.",
        ],
        "fuentes": [D["fuentes"]["ipc"], ANDINA_METAS, GLOSARIO_PDF],
    }


# ---------- 2. Dólar ----------
def dolar(D):
    s = D["series"]["tc"]
    ym, v = puntos(s)[-1]
    todo = puntos(s)
    maximo = max(todo, key=lambda p: p[1])
    minimo = min(todo, key=lambda p: p[1])
    hace12 = valor_en(s, ym_mas(ym, -12))
    var12 = (v / hace12 - 1) * 100 if hace12 else None
    p10 = puntos(s, ym_mas(ym, -120))
    alto10 = max(p10, key=lambda p: p[1])
    bajo10 = min(p10, key=lambda p: p[1])
    diario = D.get("cifras", {}).get("tc")
    if var12 is None:
        frase12 = ""
    elif abs(var12) < 1:
        frase12 = "Frente a hace un año (S/ %s), casi no cambió." % num(hace12, 3)
    elif var12 > 0:
        frase12 = "Frente a hace un año (S/ %s), el dólar está %s más caro: el sol se <strong>depreció</strong>." % (num(hace12, 3), pct(var12, 1))
    else:
        frase12 = "Frente a hace un año (S/ %s), el dólar está %s más barato: el sol se <strong>apreció</strong>." % (num(hace12, 3), pct(-var12, 1))
    graf = linea("Tipo de cambio promedio de cada mes (soles por dólar)",
                 [{"nombre": "Soles por dólar", "clase": "s1", "v": s["v"]}], s["x0"], unidad="", dec=3,
                 nota="Promedio mensual del tipo de cambio bancario (BCRP, serie PN01210PM).")
    hoy = ""
    if diario:
        hoy = (" El último dato diario disponible, del %s, fue S/ %s por dólar (venta)." %
               (fecha_txt(diario["fecha"]), num(diario["valor"], 3)))
    secciones = [
        card("Qué es el tipo de cambio",
             "El <a href=\"../glosario/tipo-de-cambio.html\">tipo de cambio</a> es el precio del dólar expresado en soles. Si está en 3.50, "
             "necesitas S/ 3.50 para comprar un dólar. Como cualquier precio, sale del encuentro entre quienes quieren dólares "
             "(para importar, pagar deudas o ahorrar) y quienes los ofrecen (exportadores, turistas, inversionistas que traen dinero).",
             "Cuando el dólar sube decimos que el sol se <a href=\"../glosario/depreciacion-y-apreciacion.html\">deprecia</a> (vale menos); "
             "cuando baja, que se aprecia."),
        card("Cómo va hoy",
             "En %s, el dólar costó en promedio <strong>S/ %s</strong>. %s%s" % (mes_txt(ym, True), num(v, 3), frase12, hoy),
             graf,
             "En los últimos diez años, el promedio mensual más alto fue S/ %s (%s) y el más bajo, S/ %s (%s). En toda la serie, "
             "que empieza en enero de 1995, el máximo fue S/ %s en %s y el mínimo, S/ %s en %s." % (
                 num(alto10[1], 3), mes_txt(alto10[0], True), num(bajo10[1], 3), mes_txt(bajo10[0], True),
                 num(maximo[1], 3), mes_txt(maximo[0], True), num(minimo[1], 3), mes_txt(minimo[0], True))),
        card("Qué hace subir o bajar al dólar",
             "<ul><li><strong>Los dólares que entran por exportaciones.</strong> El Perú vende al mundo cobre, oro, frutas y otros productos. "
             "Cuando sus precios suben, entran más dólares y el sol tiende a fortalecerse.</li>"
             "<li><strong>Las tasas de interés de afuera.</strong> Si en Estados Unidos las tasas suben, a los inversionistas les conviene "
             "llevar su dinero allá y salen dólares del país.</li>"
             "<li><strong>La confianza.</strong> En épocas de incertidumbre, dentro o fuera del país, empresas y familias compran dólares para "
             "protegerse, y eso empuja su precio hacia arriba.</li>"
             "<li><strong>El Banco Central.</strong> El precio del dólar lo pone el mercado, pero el BCRP puede comprar o vender dólares, o usar otros "
             "instrumentos, para evitar saltos bruscos. A eso se le llama <a href=\"../glosario/intervencion-cambiaria.html\">intervención cambiaria</a>; "
             "no busca fijar un precio, sino suavizar los movimientos.</li></ul>"),
        card("Cómo te afecta",
             "Si el dólar sube, se encarece lo importado (celulares, autos, medicinas, combustibles y parte de los alimentos), y una parte "
             "de esa subida llega a los precios en general: es el <a href=\"../glosario/efecto-traspaso.html\">efecto traspaso</a>. "
             "También pesa más una deuda en dólares si ganas en soles: una cuota de US$ 100 cuesta S/ 350 con el dólar a 3.50, "
             "pero S/ 380 si llega a 3.80.",
             "Si el dólar baja, ganan quienes importan o deben en dólares, y pierden un poco quienes reciben ingresos en dólares, como "
             "los exportadores o las familias que reciben remesas del exterior."),
    ]
    return {
        "corto": "El tipo de cambio es el precio del dólar en soles. En %s el dólar costó en promedio S/ %s. Sube o baja según "
                 "cuántos dólares entran y salen del país, y el BCRP interviene para evitar saltos bruscos." % (mes_txt(ym, True), num(v, 3)),
        "secciones": secciones,
        "recuerda": [
            "Nadie puede adivinar con seguridad el precio del dólar de mañana: desconfía de quien lo prometa.",
            "La regla más prudente es endeudarte en la misma moneda en la que ganas.",
            "Para cambiar, compara el precio de compra y de venta: la diferencia es la ganancia de quien te cambia.",
        ],
        "fuentes": [D["fuentes"]["tc"]] + ([(diario["fuente"] + ": " + diario["oficial"], diario["enlace"])] if diario else []) + [GLOSARIO_PDF],
    }


def fecha_txt(iso):
    from graficos import MESES_L
    return "%d de %s de %s" % (int(iso[8:10]), MESES_L[int(iso[5:7]) - 1], iso[:4])


# ---------- 3. ¿Qué subió más? ----------
RUBROS = [("PN01383PM", None), ("PN01302PM", None), ("PN01309PM", None), ("PN01310PM", None),
          ("PN01311PM", None), ("PN01305PM", None), ("PN01303PM", None), ("PN01304PM", None),
          ("PN01298PM", None), ("PN01299PM", None), ("PN01306PM", None)]


def subio_mas(D):
    tot = D["series"]["rubro:PN01271PM"]
    ym = puntos(tot)[-1][0]
    base = "2019-12"
    filas, filas12 = [], []
    for cod, _ in RUBROS:
        r = D["series"].get("rubro:" + cod)
        if not r or puntos(r)[-1][0] != ym:
            continue
        filas.append((r["nombre"], acumulada(r, base, ym)))
        filas12.append((r["nombre"], acumulada(r, ym_mas(ym, -12), ym)))
    filas.sort(key=lambda x: -x[1])
    filas12.sort(key=lambda x: -x[1])
    total = acumulada(tot, base, ym)
    total12 = acumulada(tot, ym_mas(ym, -12), ym)
    arriba = filas[0]
    abajo = filas[-1]
    mas_que_total = [n for n, x in filas if x > total]
    series = []
    for nombre, cod, clase in (("Todo el IPC", "PN01271PM", "s1"), ("Alimentos y bebidas", "PN01383PM", "s2"),
                               ("Comidas fuera del hogar", "PN01302PM", "s3")):
        x0, vals = indice_desde(D["series"]["rubro:" + cod], base)
        series.append({"nombre": nombre, "clase": clase, "v": vals})
    graf = linea("Cuánto subieron los precios desde diciembre de 2019 (índice: dic. 2019 = 100)", series, base,
                 unidad="", dec=1, nota="Cálculo propio: se encadenan las variaciones mensuales del IPC de Lima publicadas por el BCRP. "
                 "Un valor de 130 quiere decir que eso cuesta 30 % más que en diciembre de 2019.")
    PROM = "Todo el IPC (promedio)"
    barras1 = barras("Subida acumulada de precios por rubro, de diciembre de 2019 a %s" % mes_txt(ym),
                     sorted(filas + [(PROM, total)], key=lambda x: -x[1]), destacar=[PROM],
                     nota="La barra gris es el promedio de toda la canasta. Cálculo propio con series del BCRP.")
    barras2 = barras("Subida de precios en los últimos 12 meses (a %s)" % mes_txt(ym),
                     sorted(filas12 + [(PROM, total12)], key=lambda x: -x[1]), destacar=[PROM],
                     nota="La barra gris es el promedio de toda la canasta. Cálculo propio con series del BCRP.")
    secciones = [
        card("Una misma inflación, muchas subidas distintas",
             "Cuando se anuncia la inflación, se da un solo número. Pero ese número es un promedio: dentro de la canasta hay cosas que "
             "subieron mucho, otras poco y algunas que hasta bajaron. Por eso es común sentir que «todo está más caro» aunque la "
             "inflación oficial parezca baja: depende de en qué gasta cada familia.",
             "El BCRP publica cómo varían cada mes los precios de los principales rubros del IPC de Lima. Con esas cifras, aquí "
             "calculamos cuánto subió cada rubro desde diciembre de 2019, el último mes antes de la pandemia."),
        card("Desde antes de la pandemia",
             "De diciembre de 2019 a %s, el IPC completo subió <strong>%s</strong>. El rubro que más subió fue "
             "<strong>«%s»</strong> (%s) y el que menos, «%s» (%s). %d de los %d rubros que mostramos subieron más que el promedio."
             % (mes_txt(ym, True), pct(total, 1), arriba[0], pct(arriba[1], 1), abajo[0], pct(abajo[1], 1),
                len(mas_que_total), len(filas)),
             barras1),
        card("Comer en casa y comer fuera",
             "La comida pesa mucho en el presupuesto de las familias, sobre todo en las de menores ingresos, que gastan en ella una parte "
             "mayor de lo que ganan. El gráfico compara cómo evolucionaron los alimentos que se compran para el hogar, las comidas fuera "
             "(menú, pollería, restaurante) y el IPC completo.",
             graf),
        card("En el último año",
             "En los últimos 12 meses, hasta %s, el rubro que más subió fue «%s» (%s) y el que menos, «%s» (%s)."
             % (mes_txt(ym, True), filas12[0][0], pct(filas12[0][1], 1), filas12[-1][0], pct(filas12[-1][1], 1)),
             barras2),
        card("Cómo usar esta información",
             "Si quieres saber cuánto subió <em>tu</em> costo de vida, mira los rubros en los que más gastas. Una familia que paga alquiler "
             "y se mueve en transporte público vive la inflación distinto que una que tiene casa propia y gasta sobre todo en comida.",
             "Para comparar precios de otros años al mes exacto, usa la <a href=\"../inflacion/\">calculadora de inflación</a>; "
             "y para ver cada rubro mes a mes, la sección de <a href=\"../precios/\">precios del Perú y del mundo</a>."),
    ]
    return {
        "corto": "La inflación es un promedio: dentro de ella, unos precios suben mucho más que otros. De diciembre de 2019 a %s, "
                 "el IPC de Lima subió %s, pero el rubro «%s» subió %s." % (mes_txt(ym, True), pct(total, 1), arriba[0], pct(arriba[1], 1)),
        "secciones": secciones,
        "recuerda": [
            "El número de la inflación es un promedio ponderado: cada rubro pesa según cuánto gastan en él las familias de Lima.",
            "Que un rubro haya subido menos que el promedio no quiere decir que haya bajado.",
            "Los alimentos de precio volátil (verduras, frutas, pollo, pescado) pueden subir y bajar fuerte en pocos meses.",
        ],
        "fuentes": [D["fuentes"]["rubro:" + c] for c in ["PN01271PM"] + [c for c, _ in RUBROS] if "rubro:" + c in D["fuentes"]],
    }


GUIAS = [
    {"slug": "inflacion-en-el-peru", "publicar": "2026-11-24", "emoji": "🎈", "tema": "Precios", "minutos": 5,
     "titulo": "La inflación en el Perú: qué es, cómo va y por qué la meta es 2 %",
     "descripcion": "Qué es la inflación, cómo se mide en el Perú, cómo va hoy y por qué el BCRP busca que esté entre 1 % y 3 %. Con un gráfico de 2003 a hoy hecho con datos oficiales.",
     "necesita": ["inflacion12", "inflacion_mes"], "cuerpo": inflacion,
     "herramienta": ("../inflacion/", "Calcula cuánto valen hoy tus soles de otro año →"),
     "glosario": [("inflacion", "Inflación"), ("ipc", "IPC"), ("meta-de-inflacion", "Meta de inflación"),
                  ("inflacion-subyacente", "Inflación subyacente"), ("poder-adquisitivo", "Poder adquisitivo"),
                  ("deflacion", "Deflación"), ("bcrp", "BCRP")]},
    {"slug": "precio-del-dolar-en-el-peru", "publicar": "2026-11-24", "emoji": "💵", "tema": "Dólar", "minutos": 5,
     "titulo": "El precio del dólar en el Perú: por qué sube y por qué baja",
     "descripcion": "Qué es el tipo de cambio, cuánto cuesta hoy el dólar, qué lo hace subir o bajar y cómo te afecta. Con un gráfico desde 1995 hecho con datos del BCRP.",
     "necesita": ["tc"], "cuerpo": dolar,
     "glosario": [("tipo-de-cambio", "Tipo de cambio"), ("depreciacion-y-apreciacion", "Depreciación y apreciación"),
                  ("intervencion-cambiaria", "Intervención cambiaria"), ("efecto-traspaso", "Efecto traspaso"),
                  ("dolarizacion", "Dolarización"), ("tipo-de-cambio-informal", "Tipo de cambio informal")]},
    {"slug": "que-subio-mas-de-precio", "publicar": "2026-11-24", "emoji": "🛒", "tema": "Precios", "minutos": 4,
     "titulo": "¿Qué subió más de precio en Lima desde la pandemia?",
     "descripcion": "Comida, comer fuera, transporte, alquiler, educación y más: cuánto subió cada rubro del IPC de Lima desde diciembre de 2019 y en el último año, con gráficos propios.",
     "necesita": ["rubro:PN01271PM", "rubro:PN01383PM", "rubro:PN01302PM"], "cuerpo": subio_mas,
     "herramienta": ("../precios/", "Mira los precios de cada rubro mes a mes →"),
     "glosario": [("ipc", "IPC"), ("canasta-de-consumo", "Canasta de consumo"), ("inflacion", "Inflación"),
                  ("poder-adquisitivo", "Poder adquisitivo"), ("valor-nominal-y-real", "Valor nominal y real")]},
]
