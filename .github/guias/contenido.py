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



# ---------- utilidades para las guías en cola ----------
def extremos(s, desde=None):
    p = puntos(s, desde)
    return max(p, key=lambda x: x[1]), min(p, key=lambda x: x[1])


def fuente_cifra(D, clave):
    c = D.get("cifras", {}).get(clave)
    return [(c["fuente"] + ": " + c["oficial"], c["enlace"])] if c else []


def promedio_12(s):
    p = puntos(s)[-12:]
    return sum(v for _, v in p) / len(p)


# ---------- 4. Tasa de referencia ----------
def tasa_ref(D):
    s = D["series"]["tasa_ref"]
    ym, v = puntos(s)[-1]
    inf = D["series"]["inflacion12"]
    ym_i, v_i = puntos(inf)[-1]
    alto, bajo = extremos(s)
    hace12 = valor_en(s, ym_mas(ym, -12))
    cambios = 0
    previo = None
    for m, x in puntos(s, ym_mas(ym, -12)):
        if previo is not None and abs(x - previo) > 1e-9:
            cambios += 1
        previo = x
    real = v - v_i
    x0 = s["x0"]
    _, vi = recorte(inf, x0)
    graf = linea("Tasa de referencia del BCRP e inflación a 12 meses (%)",
                 [{"nombre": "Tasa de referencia", "clase": "s1", "v": s["v"]},
                  {"nombre": "Inflación a 12 meses", "clase": "s2", "v": vi[:len(s["v"])]}], x0, unidad="%", dec=2, cero=True,
                 nota="Tasa: último dato de cada mes (BCRP, serie PD12301MD). Inflación: cálculo propio con el IPC de Lima (BCRP, serie PN38705PM).")
    if hace12 is None or abs(v - hace12) < 1e-9:
        frase = "Es la misma tasa que hace un año."
    elif v > hace12:
        frase = "Hace un año estaba en %s, así que hoy está más alta." % pct(hace12, 2)
    else:
        frase = "Hace un año estaba en %s, así que hoy está más baja." % pct(hace12, 2)
    secciones = [
        card("Qué es",
             "La <a href=\"../glosario/tasa-de-referencia.html\">tasa de referencia</a> es la tasa de interés que el Banco Central de Reserva "
             "del Perú (BCRP) fija como guía para los préstamos de un día entre bancos. No es la tasa que te cobra tu banco, pero es el punto "
             "de partida: cuando el BCRP la mueve, poco a poco se mueven también las tasas de los créditos y de los depósitos.",
             "El Directorio del BCRP la revisa una vez al mes, en fechas que anuncia con anticipación, y publica un comunicado que explica su decisión."),
        card("Cómo va hoy",
             "A %s, la tasa de referencia está en <strong>%s</strong>. %s En los últimos doce meses, el BCRP la cambió %d %s."
             % (mes_txt(ym, True), pct(v, 2), frase, cambios, "vez" if cambios == 1 else "veces"),
             graf,
             "Desde %s, la tasa más alta fue %s (%s) y la más baja, %s (%s)."
             % (mes_txt(x0, True), pct(alto[1], 2), mes_txt(alto[0], True), pct(bajo[1], 2), mes_txt(bajo[0], True))),
        card("Por qué sube o baja",
             "La tarea principal del BCRP es cuidar que la inflación se quede entre 1 % y 3 % al año. La tasa de referencia es su herramienta "
             "principal para eso:",
             "<ul><li><strong>Si la inflación amenaza con pasarse de la meta</strong>, el BCRP sube la tasa. Los créditos se encarecen, la gente "
             "y las empresas piden menos préstamos y gastan menos, y eso le quita presión a los precios.</li>"
             "<li><strong>Si la economía está débil y la inflación baja</strong>, el BCRP baja la tasa. Los créditos se abaratan, se anima el gasto "
             "y la inversión, y la economía se reactiva.</li></ul>",
             "Como las decisiones tardan varios meses en sentirse, el BCRP no mira solo la inflación de hoy sino la que espera para los "
             "próximos meses; por eso las <a href=\"../glosario/expectativas.html\">expectativas</a> pesan tanto."),
        card("La tasa real",
             "Una forma sencilla de saber si la tasa «aprieta» o «afloja» es restarle la inflación. A %s la tasa es %s y la inflación de 12 meses "
             "(%s) es %s, así que la tasa real calculada de esta manera es de %s. %s"
             % (mes_txt(ym, True), pct(v, 2), mes_txt(ym_i, True), pct(v_i, 2), pct(real, 2),
                "Cuando es negativa, prestar en soles rinde menos que la subida de los precios, y eso tiende a impulsar el gasto."
                if real < 0 else "Cuando es positiva, ahorrar en soles le gana a la subida de los precios, y eso tiende a frenar el gasto."),
             "Los economistas suelen usar la inflación esperada en vez de la pasada, pero la idea es la misma: lo que importa es la "
             "<a href=\"../glosario/tasa-de-interes-real.html\">tasa de interés real</a>."),
        card("Cómo llega a tu bolsillo",
             "Cuando la tasa de referencia sube, con el tiempo suben las tasas de tarjetas, préstamos personales, créditos vehiculares e hipotecarios "
             "nuevos, y también lo que pagan los depósitos a plazo. Cuando baja, ocurre lo contrario. Los créditos que ya tienes a tasa fija no "
             "cambian: el efecto se ve en los créditos nuevos."),
    ]
    return {
        "corto": "La tasa de referencia es la tasa de interés que fija el BCRP para guiar a todas las demás. A %s está en %s. "
                 "El BCRP la sube para frenar la inflación y la baja para animar la economía." % (mes_txt(ym, True), pct(v, 2)),
        "secciones": secciones,
        "recuerda": [
            "No es la tasa que te cobra tu banco, pero la empuja hacia arriba o hacia abajo.",
            "Sus efectos tardan meses en llegar a los precios.",
            "Los créditos que ya tienes a tasa fija no cambian cuando el BCRP mueve la tasa.",
        ],
        "fuentes": [D["fuentes"]["tasa_ref"], D["fuentes"]["ipc"]] + fuente_cifra(D, "tasa_ref") + [GLOSARIO_PDF],
    }


# ---------- 5. Reservas internacionales ----------
def reservas(D):
    s = D["series"]["rin"]
    ym, v = puntos(s)[-1]
    alto, bajo = extremos(s)
    hace10 = valor_en(s, ym_mas(ym, -120))
    tc = D.get("cifras", {}).get("tc")
    graf = linea("Reservas internacionales netas del Perú (millones de dólares)",
                 [{"nombre": "Reservas internacionales netas", "clase": "s1", "v": s["v"]}], s["x0"], unidad="", dec=0, cero=True,
                 nota="Dato de fin de cada mes (BCRP, serie %s)." % D["fuentes"]["rin"][0].split("serie ")[1].split(":")[0])
    secciones = [
        card("Qué son",
             "Las <a href=\"../glosario/reservas-internacionales.html\">reservas internacionales netas</a> (RIN) son los dólares y otros activos "
             "seguros del exterior (como oro, bonos de otros países y depósitos en bancos extranjeros) que tiene el BCRP. Son, en pocas palabras, "
             "el ahorro en moneda extranjera del país."),
        card("Cuánto tiene el Perú",
             "A %s, las reservas internacionales netas sumaban <strong>US$ %s millones</strong>, es decir, unos US$ %s mil millones.%s"
             % (mes_txt(ym, True), num(v, 0), num(v / 1000, 1),
                (" Hace diez años, en %s, eran US$ %s millones." % (mes_txt(ym_mas(ym, -120), True), num(hace10, 0))) if hace10 else ""),
             graf,
             "El nivel más alto de la serie fue US$ %s millones, en %s." % (num(alto[1], 0), mes_txt(alto[0], True))),
        card("Para qué sirven",
             "<ul><li><strong>Para calmar al dólar.</strong> Si el dólar sube de golpe, el BCRP puede vender parte de sus dólares para evitar "
             "saltos bruscos (<a href=\"../glosario/intervencion-cambiaria.html\">intervención cambiaria</a>).</li>"
             "<li><strong>Como seguro ante crisis.</strong> Si de pronto salen capitales del país o caen los precios de lo que exportamos, "
             "las reservas permiten seguir pagando compromisos en dólares sin que la economía se paralice.</li>"
             "<li><strong>Para dar confianza.</strong> Un país con reservas altas es visto como más seguro, y eso ayuda a que pague tasas "
             "de interés más bajas cuando se endeuda.</li></ul>",
             "En el Perú importan especialmente porque una parte de los créditos y depósitos todavía está en dólares "
             "(<a href=\"../glosario/dolarizacion.html\">dolarización</a>): si el dólar saltara sin control, muchas familias y empresas "
             "con deudas en dólares tendrían problemas."),
        card("Lo que no son",
             "Las reservas no son una «caja» que el Gobierno pueda gastar en obras o en bonos: pertenecen al BCRP, que es autónomo, y "
             "su papel es respaldar la estabilidad de la moneda. Tampoco son todo ganancia: una parte corresponde a depósitos en dólares "
             "que los bancos y el sector público mantienen en el BCRP."),
    ]
    return {
        "corto": "Las reservas internacionales son el ahorro en dólares y otros activos seguros que guarda el BCRP. A %s sumaban unos "
                 "US$ %s mil millones y sirven para calmar al dólar y proteger al país en una crisis." % (mes_txt(ym, True), num(v / 1000, 1)),
        "secciones": secciones,
        "recuerda": [
            "Las reservas son del BCRP, no del Gobierno: no se usan para gasto público.",
            "Sirven como seguro: lo ideal es no tener que usarlas en grande.",
            "Pesan más en países con muchos créditos en dólares, como el Perú.",
        ],
        "fuentes": [D["fuentes"]["rin"]] + fuente_cifra(D, "rin") + [GLOSARIO_PDF],
    }


# ---------- 6. Crecimiento del PBI ----------
def pbi(D):
    s = D["series"]["pbi"]
    ym, v = puntos(s)[-1]
    prom = promedio_12(s)
    alto, bajo = extremos(s)
    negativos = sum(1 for _, x in puntos(s)[-12:] if x < 0)
    graf = linea("Crecimiento de la producción nacional frente al mismo mes del año anterior (%)",
                 [{"nombre": "Variación a 12 meses", "clase": "s1", "v": s["v"]}], s["x0"], unidad="%", dec=1, cero=True,
                 nota="BCRP, serie PN01728AM (con datos del INEI). La línea oscura marca el cero: debajo, la economía produjo menos que un año antes.")
    secciones = [
        card("Qué es el PBI",
             "El <a href=\"../glosario/pbi.html\">producto bruto interno (PBI)</a> es el valor de todo lo que se produce en el país en un periodo: "
             "minerales, cosechas, edificios, ropa, servicios de transporte, comercio, salud, todo. Cuando el PBI crece, en general hay más "
             "ventas, más empleo y más ingresos."),
        card("Cómo va hoy",
             "En %s, la producción nacional fue <strong>%s</strong> %s que en el mismo mes del año anterior. En promedio, en los últimos doce "
             "meses publicados, cada mes produjo %s %s que un año antes%s."
             % (mes_txt(ym, True), pct(abs(v), 1), "mayor" if v >= 0 else "menor", pct(abs(prom), 1), "más" if prom >= 0 else "menos",
                (" (en %d de esos meses la variación fue negativa)" % negativos) if negativos else ""),
             graf,
             ("La caída más fuerte de la serie fue de %s, en %s%s. " % (
                 pct(bajo[1], 1), mes_txt(bajo[0], True),
                 ", cuando la cuarentena por la pandemia paralizó gran parte de la economía" if "2020-03" <= bajo[0] <= "2020-12" else ""))
             + ("El salto más alto, %s en %s, fue sobre todo un rebote: se comparaba con meses en los que casi todo estaba cerrado."
                % (pct(alto[1], 1), mes_txt(alto[0], True)) if "2021-03" <= alto[0] <= "2021-12" else
                "El salto más alto fue %s, en %s." % (pct(alto[1], 1), mes_txt(alto[0], True)))),
        card("Cómo leer este dato",
             "El INEI publica la producción de cada mes con unas seis semanas de retraso, y la compara con el mismo mes del año anterior para "
             "que no influyan las temporadas (en algunos meses siempre se pesca o se cosecha más). Un solo mes puede moverse por algo puntual, "
             "como una huelga, un fenómeno climático o una fiesta: por eso conviene mirar varios meses seguidos.",
             "Cuando la producción cae durante un tiempo prolongado se habla de <a href=\"../glosario/recesion.html\">recesión</a>."),
        card("Crecer no es lo mismo que estar mejor",
             "El PBI mide cuánto se produce, no cómo se reparte. Para saber si a una persona promedio le va mejor hay que mirar el "
             "<a href=\"../glosario/pbi-per-capita.html\">PBI por habitante</a>, y para saber si a la mayoría le llega, también el empleo, "
             "los sueldos y la pobreza. Aun así, sin crecimiento es muy difícil que mejoren esos otros indicadores."),
    ]
    return {
        "corto": "El PBI mide todo lo que produce el país. En %s, la producción fue %s %s que un año antes. "
                 "Aquí explicamos cómo leer este dato y qué dice el gráfico desde 2004." % (mes_txt(ym, True), pct(abs(v), 1), "mayor" if v >= 0 else "menor"),
        "secciones": secciones,
        "recuerda": [
            "El dato mensual se compara con el mismo mes del año anterior, no con el mes previo.",
            "Un mes aislado puede engañar: mira la tendencia de varios meses.",
            "Más PBI no garantiza que a todos les vaya mejor, pero ayuda.",
        ],
        "fuentes": [D["fuentes"]["pbi"], GLOSARIO_PDF],
    }


# ---------- 7. Desempleo en Lima ----------
def desempleo(D):
    s = D["series"]["desempleo"]
    ym, v = puntos(s)[-1]
    alto, bajo = extremos(s)
    hace12 = valor_en(s, ym_mas(ym, -12))
    pre = valor_en(s, "2019-12")
    graf = linea("Tasa de desempleo en Lima Metropolitana (%)",
                 [{"nombre": "Tasa de desempleo", "clase": "s1", "v": s["v"]}], s["x0"], unidad="%", dec=1, cero=True,
                 nota="Promedio móvil de tres meses (BCRP, serie PN38063GM, con datos de la encuesta de empleo del INEI).")
    secciones = [
        card("Qué mide",
             "La <a href=\"../glosario/tasa-de-desempleo.html\">tasa de desempleo</a> es el porcentaje de personas que buscan trabajo activamente "
             "y no lo encuentran, dentro de la <a href=\"../glosario/pea.html\">población económicamente activa (PEA)</a>: quienes trabajan más "
             "quienes buscan trabajo. Quien no busca (por ejemplo, porque estudia o se cansó de buscar) no cuenta como desempleado.",
             "En Lima Metropolitana, el INEI la calcula cada mes con una encuesta a hogares. Para que el dato no salte demasiado, se publica "
             "como promedio de tres meses."),
        card("Cómo va hoy",
             "En el trimestre que termina en %s, la tasa de desempleo en Lima fue de <strong>%s</strong>.%s%s"
             % (mes_txt(ym, True), pct(v, 1),
                (" Un año antes era %s." % pct(hace12, 1)) if hace12 is not None else "",
                (" Antes de la pandemia, en diciembre de 2019, era %s." % pct(pre, 1)) if pre is not None else ""),
             graf,
             "El punto más alto de la serie fue %s, en %s, durante la pandemia." % (pct(alto[1], 1), mes_txt(alto[0], True))
             if alto[0] >= "2020-03" and alto[0] <= "2021-12" else
             "El punto más alto de la serie fue %s, en %s." % (pct(alto[1], 1), mes_txt(alto[0], True))),
        card("Poco desempleo no siempre es buen empleo",
             "La tasa de desempleo puede verse baja aunque falte trabajo de calidad, porque en el Perú muchas personas no pueden darse el lujo de no "
             "trabajar: si no encuentran un empleo formal, se las arreglan con trabajos por su cuenta, a veces de pocas horas o con poco ingreso.",
             "Por eso, además del desempleo, conviene mirar el <a href=\"../glosario/subempleo.html\">subempleo</a> y la "
             "<a href=\"../glosario/informalidad.html\">informalidad</a>, que muestran cuántos trabajan sin beneficios o ganan menos de lo necesario."),
    ]
    return {
        "corto": "La tasa de desempleo dice qué parte de quienes buscan trabajo no lo encuentra. En Lima fue de %s en el trimestre que "
                 "termina en %s. Pero un desempleo bajo no siempre significa empleo de calidad." % (pct(v, 1), mes_txt(ym, True)),
        "secciones": secciones,
        "recuerda": [
            "Solo cuenta como desempleado quien busca trabajo y no lo encuentra.",
            "El dato de Lima es un promedio de tres meses.",
            "Para ver la calidad del empleo, mira también el subempleo y la informalidad.",
        ],
        "fuentes": [D["fuentes"]["desempleo"], GLOSARIO_PDF],
    }


# ---------- 8. Cobre ----------
def cobre(D):
    s = D["series"]["cobre"]
    ym, v = puntos(s)[-1]
    alto, bajo = extremos(s, "2005-01")
    hace12 = valor_en(s, ym_mas(ym, -12))
    var12 = (v / hace12 - 1) * 100 if hace12 else None
    # La serie del BCRP viene en centavos de dólar por libra
    graf = linea("Precio del cobre en Londres (centavos de dólar por libra)",
                 [{"nombre": "Cobre", "clase": "s1", "v": s["v"]}], s["x0"], unidad="", dec=0, cero=True,
                 nota="Promedio de cada mes (BCRP, serie %s)." % D["fuentes"]["cobre"][0].split("serie ")[1].split(":")[0])
    secciones = [
        card("Por qué el cobre importa tanto",
             "El Perú es uno de los mayores productores de cobre del mundo y el cobre es uno de los productos que más vende al exterior. "
             "Por eso, lo que pasa con su precio en el mercado internacional se siente aquí: cuando sube, entran más dólares, las mineras "
             "pagan más impuestos y crece el <a href=\"../glosario/canon.html\">canon</a> que reciben las regiones productoras.",
             "Al revés, cuando el precio cae, entran menos dólares y se recauda menos. Por eso los economistas siguen de cerca los "
             "<a href=\"../glosario/terminos-de-intercambio.html\">términos de intercambio</a>: la relación entre los precios de lo que el "
             "Perú vende y de lo que compra."),
        card("Cómo va hoy",
             "En %s, el cobre se vendió en promedio a <strong>%s centavos de dólar por libra</strong> (unos US$ %s por libra).%s"
             % (mes_txt(ym, True), num(v, 0), num(v / 100, 2),
                ("" if var12 is None else " Frente a un año antes está %s %s." % (pct(abs(var12), 1), "más caro" if var12 >= 0 else "más barato"))),
             graf,
             "Desde 2005, el promedio mensual más alto fue %s centavos (%s) y el más bajo, %s centavos (%s)."
             % (num(alto[1], 0), mes_txt(alto[0], True), num(bajo[1], 0), mes_txt(bajo[0], True))),
        card("Qué mueve su precio",
             "El cobre se usa en cables, motores, construcción y aparatos electrónicos, así que su precio sube cuando la economía mundial crece "
             "y baja cuando se enfría. Pesa mucho lo que pasa en China, el mayor comprador del mundo. También influyen la oferta (huelgas, "
             "minas nuevas o que cierran) y, en los últimos años, la demanda para autos eléctricos y redes de energía."),
        card("Cómo te afecta",
             "Un cobre caro suele traer más dólares al país, lo que tiende a abaratar el dólar, y más recursos para el Estado y las regiones. "
             "Un cobre barato hace lo contrario. Por eso el precio de un metal que casi nadie compra directamente termina influyendo en el "
             "<a href=\"precio-del-dolar-en-el-peru.html\">precio del dólar</a> y en el presupuesto público."),
    ]
    return {
        "corto": "El cobre es clave para la economía peruana: cuando su precio sube, entran más dólares y más impuestos. En %s costó en "
                 "promedio %s centavos de dólar por libra en Londres." % (mes_txt(ym, True), num(v, 0)),
        "secciones": secciones,
        "recuerda": [
            "El precio del cobre lo fija el mercado mundial, no el Perú.",
            "Un cobre caro suele fortalecer al sol; uno barato, debilitarlo.",
            "El canon minero que reciben las regiones depende de las ganancias de las mineras, y por eso del precio de los metales.",
        ],
        "fuentes": [D["fuentes"]["cobre"]] + fuente_cifra(D, "cobre") + [GLOSARIO_PDF],
    }


# ---------- 9. Riesgo país ----------
def riesgo(D):
    s = D["series"]["embig"]
    ym, v = puntos(s)[-1]
    alto, bajo = extremos(s)
    hace12 = valor_en(s, ym_mas(ym, -12))
    graf = linea("Riesgo país del Perú: diferencial EMBIG (puntos básicos)",
                 [{"nombre": "Riesgo país (EMBIG Perú)", "clase": "s1", "v": s["v"]}], s["x0"], unidad="", dec=0, cero=True,
                 nota="Promedio de cada mes (BCRP, serie PN01129XM). 100 puntos básicos = 1 punto porcentual.")
    secciones = [
        card("Qué es",
             "El <a href=\"../glosario/riesgo-pais.html\">riesgo país</a> mide cuánto más interés le piden los inversionistas al Perú, comparado "
             "con Estados Unidos, por prestarle dinero. Se calcula con los bonos del Gobierno peruano en dólares: si rinden 1.5 puntos más que "
             "los bonos del Tesoro de Estados Unidos, el riesgo país es de 150 <a href=\"../glosario/puntos-basicos.html\">puntos básicos</a>.",
             "El indicador más usado es el EMBIG, que elabora el banco JP Morgan y publica el BCRP."),
        card("Cómo va hoy",
             "En %s, el riesgo país del Perú fue de <strong>%s puntos básicos</strong>, en promedio.%s"
             % (mes_txt(ym, True), num(v, 0), (" Un año antes era %s." % num(hace12, 0)) if hace12 is not None else ""),
             graf,
             "Desde %s, el punto más alto fue %s puntos básicos (%s) y el más bajo, %s (%s)."
             % (mes_txt(s["x0"], True), num(alto[1], 0), mes_txt(alto[0], True), num(bajo[1], 0), mes_txt(bajo[0], True))),
        card("Por qué sube o baja",
             "Sube cuando los inversionistas ven más peligro de que el país tenga problemas para pagar o de que su economía se complique: "
             "crisis mundiales, caídas fuertes de los precios de los metales, ruido político o cuentas fiscales que empeoran. Baja cuando "
             "la confianza mejora. Las crisis globales suelen subir el riesgo país de todos los países emergentes a la vez."),
        card("Cómo te afecta",
             "Un riesgo país bajo abarata el crédito para el Gobierno y para las grandes empresas que se financian afuera, y con el tiempo "
             "eso se refleja en las tasas de interés dentro del país. Un riesgo país alto hace lo contrario y puede espantar inversiones. "
             "Las <a href=\"../glosario/calificacion-de-riesgo.html\">calificaciones de riesgo</a> y el "
             "<a href=\"../glosario/grado-de-inversion.html\">grado de inversión</a> miden algo parecido, pero con la opinión de agencias especializadas."),
    ]
    return {
        "corto": "El riesgo país mide cuánto más interés piden los inversionistas para prestarle al Perú que a Estados Unidos. "
                 "En %s fue de %s puntos básicos (unos %s puntos porcentuales)." % (mes_txt(ym, True), num(v, 0), num(v / 100, 2)),
        "secciones": secciones,
        "recuerda": [
            "100 puntos básicos equivalen a 1 punto porcentual de interés extra.",
            "Las crisis mundiales suben el riesgo país de todos los emergentes, no solo del Perú.",
            "Un riesgo país bajo ayuda a que el crédito sea más barato.",
        ],
        "fuentes": [D["fuentes"]["embig"], GLOSARIO_PDF],
    }


# ---------- 10. Tasas de los bancos ----------
def tasas(D):
    a = D["series"]["tamn"]
    p = D["series"]["tipmn"]
    ym, va = puntos(a)[-1]
    ymp, vp = puntos(p)[-1]
    x0 = max(a["x0"], p["x0"])
    _, av = recorte(a, x0)
    _, pv = recorte(p, x0)
    graf = linea("Tasas promedio de los bancos en soles (% efectivo anual)",
                 [{"nombre": "Préstamos (TAMN)", "clase": "s1", "v": av}, {"nombre": "Depósitos (TIPMN)", "clase": "s2", "v": pv}],
                 x0, unidad="%", dec=2, cero=True, nota="BCRP, series PN07807NM y PN07816NM. Promedios de todo el sistema bancario.")
    secciones = [
        card("Dos tasas muy distintas",
             "Los bancos ganan sobre todo con la diferencia entre lo que cobran por prestar y lo que pagan por los depósitos. El BCRP publica "
             "cada mes dos promedios de todo el sistema: la <strong>TAMN</strong>, tasa activa promedio en soles (lo que cobran por los préstamos), "
             "y la <strong>TIPMN</strong>, tasa pasiva promedio (lo que pagan por los depósitos).",
             "En %s, la TAMN fue <strong>%s</strong> y la TIPMN, <strong>%s</strong>. La diferencia es de %s puntos."
             % (mes_txt(ym, True), pct(va, 2), pct(vp, 2), num(va - vp, 2)),
             graf),
        card("Por qué tanta diferencia",
             "La TAMN es un promedio de muchos tipos de crédito, desde préstamos baratos a grandes empresas hasta tarjetas de crédito y "
             "microcréditos con tasas muy altas. La TIPMN incluye cuentas de ahorro que casi no pagan nada y depósitos a plazo que pagan más. "
             "Además, el banco debe cubrir el riesgo de que algunos no paguen, sus costos de operación y el "
             "<a href=\"../glosario/encaje-bancario.html\">encaje</a>, y obtener una ganancia.",
             "Por eso estos promedios sirven para ver tendencias, pero no para saber cuánto te cobrarán a ti: eso depende del tipo de "
             "crédito, del plazo y de tu historial."),
        card("Qué mirar antes de pedir o ahorrar",
             "<ul><li>Para un préstamo, compara la <a href=\"../glosario/tcea.html\">TCEA</a>, que incluye comisiones y seguros, no solo la "
             "<a href=\"../glosario/tea.html\">TEA</a>.</li>"
             "<li>Para un depósito, compara la <a href=\"../glosario/trea.html\">TREA</a>, que descuenta comisiones.</li>"
             "<li>Revisa que la entidad esté supervisada por la SBS y, si es un depósito, que esté cubierta por el Fondo de Seguro de Depósitos.</li></ul>"),
    ]
    return {
        "corto": "Los bancos cobran mucho más por prestar que lo que pagan por los depósitos. En %s, la tasa promedio de los préstamos en "
                 "soles fue %s y la de los depósitos, %s." % (mes_txt(ym, True), pct(va, 2), pct(vp, 2)),
        "secciones": secciones,
        "recuerda": [
            "La TAMN y la TIPMN son promedios: tu tasa real depende del producto y de tu historial.",
            "Para comparar préstamos usa la TCEA; para comparar depósitos, la TREA.",
            "Las tasas del sistema siguen, con retraso, a la tasa de referencia del BCRP.",
        ],
        "fuentes": [D["fuentes"]["tamn"], D["fuentes"]["tipmn"], GLOSARIO_PDF],
    }


GUIAS = [
    {"slug": "inflacion-en-el-peru", "publicar": "2026-11-23", "emoji": "🎈", "tema": "Precios", "minutos": 5,
     "titulo": "La inflación en el Perú: qué es, cómo va y por qué la meta es 2 %",
     "descripcion": "Qué es la inflación, cómo se mide en el Perú, cómo va hoy y por qué el BCRP busca que esté entre 1 % y 3 %. Con un gráfico de 2003 a hoy hecho con datos oficiales.",
     "necesita": ["inflacion12", "inflacion_mes"], "cuerpo": inflacion,
     "herramienta": ("../inflacion/", "Calcula cuánto valen hoy tus soles de otro año →"),
     "glosario": [("inflacion", "Inflación"), ("ipc", "IPC"), ("meta-de-inflacion", "Meta de inflación"),
                  ("inflacion-subyacente", "Inflación subyacente"), ("poder-adquisitivo", "Poder adquisitivo"),
                  ("deflacion", "Deflación"), ("bcrp", "BCRP")]},
    {"slug": "precio-del-dolar-en-el-peru", "publicar": "2026-11-23", "emoji": "💵", "tema": "Dólar", "minutos": 5,
     "titulo": "El precio del dólar en el Perú: por qué sube y por qué baja",
     "descripcion": "Qué es el tipo de cambio, cuánto cuesta hoy el dólar, qué lo hace subir o bajar y cómo te afecta. Con un gráfico desde 1995 hecho con datos del BCRP.",
     "necesita": ["tc"], "cuerpo": dolar,
     "glosario": [("tipo-de-cambio", "Tipo de cambio"), ("depreciacion-y-apreciacion", "Depreciación y apreciación"),
                  ("intervencion-cambiaria", "Intervención cambiaria"), ("efecto-traspaso", "Efecto traspaso"),
                  ("dolarizacion", "Dolarización"), ("tipo-de-cambio-informal", "Tipo de cambio informal")]},
    {"slug": "que-subio-mas-de-precio", "publicar": "2026-11-23", "emoji": "🛒", "tema": "Precios", "minutos": 4,
     "titulo": "¿Qué subió más de precio en Lima desde la pandemia?",
     "descripcion": "Comida, comer fuera, transporte, alquiler, educación y más: cuánto subió cada rubro del IPC de Lima desde diciembre de 2019 y en el último año, con gráficos propios.",
     "necesita": ["rubro:PN01271PM", "rubro:PN01383PM", "rubro:PN01302PM"], "cuerpo": subio_mas,
     "herramienta": ("../precios/", "Mira los precios de cada rubro mes a mes →"),
     "glosario": [("ipc", "IPC"), ("canasta-de-consumo", "Canasta de consumo"), ("inflacion", "Inflación"),
                  ("poder-adquisitivo", "Poder adquisitivo"), ("valor-nominal-y-real", "Valor nominal y real")]},
    {"slug": "tasa-de-referencia-del-bcrp", "publicar": "2026-11-27", "emoji": "🏦", "tema": "Banco Central", "minutos": 5,
     "titulo": "La tasa de referencia del BCRP: qué es y cómo llega a tu bolsillo",
     "descripcion": "Qué es la tasa de referencia del Banco Central, cómo va hoy, por qué sube o baja y cómo afecta a tus créditos y ahorros. Con un gráfico desde 2003.",
     "necesita": ["tasa_ref", "inflacion12"], "cuerpo": tasa_ref,
     "glosario": [("tasa-de-referencia", "Tasa de referencia"), ("politica-monetaria", "Política monetaria"),
                  ("tasa-de-interes-interbancaria", "Tasa interbancaria"), ("tasa-de-interes-real", "Tasa de interés real"),
                  ("expectativas", "Expectativas"), ("bcrp", "BCRP")]},
    {"slug": "reservas-internacionales-del-peru", "publicar": "2026-12-01", "emoji": "🛟", "tema": "Banco Central", "minutos": 4,
     "titulo": "Las reservas internacionales del Perú: el colchón de dólares del país",
     "descripcion": "Qué son las reservas internacionales netas, cuánto tiene el Perú, para qué sirven y para qué no. Con un gráfico hecho con datos del BCRP.",
     "necesita": ["rin"], "cuerpo": reservas,
     "glosario": [("reservas-internacionales", "Reservas internacionales"), ("intervencion-cambiaria", "Intervención cambiaria"),
                  ("dolarizacion", "Dolarización"), ("balanza-de-pagos", "Balanza de pagos"), ("bcrp", "BCRP")]},
    {"slug": "crecimiento-de-la-economia-peruana", "publicar": "2026-12-04", "emoji": "📈", "tema": "Producción", "minutos": 4,
     "titulo": "¿Cuánto crece la economía peruana? El PBI explicado mes a mes",
     "descripcion": "Qué es el PBI, cuánto creció la producción del Perú en el último mes y en el último año, y cómo leer el dato sin confundirse. Con un gráfico desde 2004.",
     "necesita": ["pbi"], "cuerpo": pbi,
     "glosario": [("pbi", "PBI"), ("crecimiento-economico", "Crecimiento económico"), ("recesion", "Recesión"),
                  ("ciclo-economico", "Ciclo económico"), ("pbi-per-capita", "PBI per cápita")]},
    {"slug": "desempleo-en-lima", "publicar": "2026-12-08", "emoji": "💼", "tema": "Empleo", "minutos": 4,
     "titulo": "El desempleo en Lima: qué mide y qué no te dice",
     "descripcion": "Qué es la tasa de desempleo, cómo va en Lima Metropolitana y por qué un desempleo bajo no siempre significa buen empleo. Con un gráfico propio.",
     "necesita": ["desempleo"], "cuerpo": desempleo,
     "glosario": [("tasa-de-desempleo", "Tasa de desempleo"), ("pea", "PEA"), ("subempleo", "Subempleo"),
                  ("informalidad", "Informalidad"), ("empleo-formal-e-informal", "Empleo formal e informal")]},
    {"slug": "precio-del-cobre-y-el-peru", "publicar": "2026-12-11", "emoji": "⛏️", "tema": "Comercio exterior", "minutos": 4,
     "titulo": "El precio del cobre y por qué mueve la economía peruana",
     "descripcion": "Por qué el cobre es tan importante para el Perú, cuánto cuesta hoy, qué mueve su precio y cómo llega al dólar y al presupuesto. Con un gráfico propio.",
     "necesita": ["cobre"], "cuerpo": cobre,
     "glosario": [("terminos-de-intercambio", "Términos de intercambio"), ("canon", "Canon"), ("materias-primas", "Materias primas"),
                  ("exportaciones-tradicionales-y-no-tradicionales", "Exportaciones tradicionales y no tradicionales")]},
    {"slug": "riesgo-pais-del-peru", "publicar": "2026-12-15", "emoji": "🌡️", "tema": "Finanzas", "minutos": 4,
     "titulo": "El riesgo país del Perú: qué es y por qué te importa",
     "descripcion": "Qué es el riesgo país (EMBIG), cómo va el del Perú, qué lo hace subir o bajar y cómo afecta al crédito. Con un gráfico hecho con datos del BCRP.",
     "necesita": ["embig"], "cuerpo": riesgo,
     "glosario": [("riesgo-pais", "Riesgo país"), ("puntos-basicos", "Puntos básicos"), ("bono-soberano", "Bono soberano"),
                  ("grado-de-inversion", "Grado de inversión"), ("calificacion-de-riesgo", "Calificación de riesgo")]},
    {"slug": "tasas-de-interes-de-los-bancos", "publicar": "2026-12-18", "emoji": "💳", "tema": "Finanzas", "minutos": 4,
     "titulo": "¿Por qué los bancos cobran tanto y pagan tan poco? Las tasas en soles",
     "descripcion": "Cuánto cobran en promedio los bancos por prestar y cuánto pagan por los depósitos en soles, por qué hay tanta diferencia y qué mirar antes de decidir.",
     "necesita": ["tamn", "tipmn"], "cuerpo": tasas,
     "herramienta": ("../prestamos/", "Simula tu préstamo o tu ahorro →"),
     "glosario": [("tasa-de-interes-activa-y-pasiva", "Tasa activa y pasiva"), ("tea", "TEA"), ("tcea", "TCEA"), ("trea", "TREA"),
                  ("encaje-bancario", "Encaje bancario")]},
]
