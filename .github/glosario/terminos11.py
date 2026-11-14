# -*- coding: utf-8 -*-
# Términos del glosario (parte 11): novena tanda. Desarrollo, historia
# económica, comercio internacional, economía conductual, trabajo, política
# social y tributación de empresas en el Perú. Redactado con palabras propias.

T = []

# --- Historia y pensamiento económico --------------------------------------

T.append(dict(
slug="mano-invisible", t="Mano invisible", cat="mercados", ic="🫳",
alias="mano invisible Adam Smith La riqueza de las naciones interés propio",
corto="Es la idea de Adam Smith de que, en un mercado libre, cada persona buscando su propio beneficio termina, sin proponérselo, ayudando al bienestar de todos.",
simple=[
r"En <em>La riqueza de las naciones</em> (1776), Adam Smith explicó que el panadero no hornea por bondad, sino para ganarse la vida; aun así, gracias a él la gente tiene pan. Los precios guían esas decisiones individuales como si una «mano invisible» las coordinara.",
r"La idea funciona bien con <a href='competencia-perfecta.html'>competencia</a>, pero falla cuando hay <a href='monopolio.html'>monopolios</a>, <a href='externalidad.html'>externalidades</a> o <a href='informacion-asimetrica.html'>información asimétrica</a>. Allí suele justificarse la intervención del Estado.",
],
ejemplo=[
r"Cuando sube el precio del palto porque mucha gente lo pide, más agricultores lo siembran, sin que nadie se los ordene: los precios coordinan la producción.",
],
rel=["oferta-y-demanda", "competencia-perfecta", "externalidad", "libre-competencia"],
))

T.append(dict(
slug="destruccion-creativa", t="Destrucción creativa", cat="produccion", ic="💥",
alias="destrucción creativa Schumpeter innovación emprendedor",
corto="Es el proceso por el que las innovaciones reemplazan a productos, empresas y empleos antiguos, impulsando el crecimiento aunque cause pérdidas en el camino.",
simple=[
r"Joseph Schumpeter describió el capitalismo como un proceso en el que el <strong>emprendedor</strong> innova y desplaza lo viejo: los autos reemplazaron a las carretas y los celulares a las cabinas públicas.",
r"Ese cambio eleva la <a href='productividad.html'>productividad</a>, pero deja perdedores, como los trabajadores de los sectores que desaparecen. Por eso importan la capacitación y la protección social.",
],
ejemplo=[
r"Las aplicaciones de taxi cambiaron el negocio de las empresas de radiotaxi tradicionales, pero crearon nuevas formas de trabajo y de servicio.",
],
rel=["productividad", "productividad-total-de-factores", "tipos-de-desempleo", "crecimiento-economico"],
))

T.append(dict(
slug="costo-de-transaccion", t="Costos de transacción", cat="mercados", ic="🤝",
alias="costos de transacción Coase derechos de propiedad contratos",
corto="Son los costos de hacer un intercambio, aparte del precio: buscar información, negociar, firmar contratos y hacer que se cumplan.",
simple=[
r"Ronald Coase mostró que estos costos explican por qué existen las empresas: a veces es más barato hacer algo dentro de una organización que contratarlo en el mercado cada vez.",
r"También explican el valor de tener <strong>derechos de propiedad</strong> claros y una justicia rápida: si cuesta mucho hacer cumplir un contrato, se hacen menos negocios.",
],
ejemplo=[
r"Comprar un terreno sin título inscrito obliga a verificar documentos, pagar abogados y asumir el riesgo de juicios: son costos de transacción que frenan la inversión.",
],
rel=["informalidad", "mano-invisible", "informacion-asimetrica", "garantia"],
))

T.append(dict(
slug="paradoja-del-ahorro", t="Paradoja del ahorro", cat="produccion", ic="🐖",
alias="paradoja de la frugalidad paradoja del ahorro Keynes demanda agregada",
corto="Dice que si todos intentan ahorrar más al mismo tiempo durante una crisis, el gasto cae, los ingresos bajan y al final el ahorro total puede no aumentar.",
simple=[
r"Para una familia, ahorrar más es prudente. Pero si todas lo hacen a la vez, las empresas venden menos, despiden trabajadores y los ingresos caen. Lo que es bueno para uno puede ser malo para todos.",
r"Es una idea de Keynes que ayuda a entender por qué en las recesiones se recomienda que el Estado sostenga la <a href='demanda-agregada.html'>demanda</a> con una <a href='politica-anticiclica.html'>política anticíclica</a>.",
],
ejemplo=[
r"En una crisis, si todos dejan de comer fuera para ahorrar, los restaurantes pierden ventas y sus trabajadores pierden ingresos, y ellos también terminan gastando menos.",
],
rel=["ahorro", "demanda-agregada", "multiplicador-keynesiano", "ley-de-say"],
))

T.append(dict(
slug="patron-oro", t="Patrón oro", cat="dinero", ic="🥇",
alias="patrón oro convertibilidad respaldo en oro sistema monetario",
corto="Es un sistema monetario en el que el valor de la moneda está atado a una cantidad fija de oro y se puede cambiar por él.",
simple=[
r"Bajo el <strong>patrón oro</strong>, el banco emisor solo puede crear dinero si tiene oro que lo respalde. Eso limita la inflación, pero también impide aumentar el dinero cuando la economía lo necesita.",
r"Fue común en el siglo XIX y comienzos del XX. Muchos economistas creen que mantenerlo agravó la <a href='gran-depresion.html'>Gran Depresión</a>, y los países lo fueron abandonando. Hoy el dinero es fiduciario: vale por la confianza y por ley.",
],
ejemplo=[
r"Si un país tiene 1000 kilos de oro y fija que cada kilo respalda 1 millón de su moneda, no podría emitir más de 1000 millones sin conseguir más oro.",
],
rel=["bretton-woods", "dinero", "curso-legal", "gran-depresion"],
))

T.append(dict(
slug="bretton-woods", t="Acuerdos de Bretton Woods", cat="dinero", ic="🏔️",
alias="Bretton Woods 1944 FMI Banco Mundial tipos de cambio fijos dólar oro",
corto="Son los acuerdos de 1944 que crearon el FMI y el Banco Mundial, y un sistema de tipos de cambio fijos atados al dólar, que a su vez estaba atado al oro.",
simple=[
r"Al final de la Segunda Guerra Mundial, 44 países se reunieron en Bretton Woods (Estados Unidos) para ordenar la economía mundial. Las monedas se fijaron al dólar, y el dólar se podía cambiar por oro a 35 dólares la onza.",
r"El sistema terminó en 1971, cuando Estados Unidos dejó de cambiar dólares por oro. Desde entonces, la mayoría de monedas importantes flota, aunque el FMI y el <a href='banco-mundial.html'>Banco Mundial</a> siguen existiendo.",
],
ejemplo=[
r"Bajo Bretton Woods, un banco central extranjero que tenía dólares podía pedir a Estados Unidos que se los cambiara por oro al precio fijo.",
],
rel=["patron-oro", "organismos-multilaterales", "banco-mundial", "regimen-cambiario"],
))

T.append(dict(
slug="gran-depresion", t="Gran Depresión", cat="produccion", ic="🏚️",
alias="Gran Depresión crac de 1929 crisis de los años treinta",
corto="Fue la crisis económica mundial más grave del siglo XX: empezó con la caída de la bolsa de Nueva York en 1929 y duró buena parte de los años treinta.",
simple=[
r"La producción y el comercio mundial se desplomaron, miles de bancos quebraron y el desempleo alcanzó niveles altísimos en muchos países. Los precios cayeron (<a href='deflacion.html'>deflación</a>), lo que hacía más pesadas las deudas.",
r"La crisis cambió la forma de pensar la economía: impulsó las ideas de Keynes sobre el papel del Estado para sostener la demanda y la creación de seguros de depósitos y supervisión bancaria. El Perú también la sufrió por la caída de sus exportaciones.",
],
ejemplo=[
r"Al caer la demanda de Estados Unidos y Europa, bajaron fuertemente los precios de materias primas como el cobre y el azúcar, y países exportadores como el Perú vieron caer sus ingresos.",
],
rel=["recesion", "deflacion", "patron-oro", "paradoja-del-ahorro"],
))

T.append(dict(
slug="industrializacion-por-sustitucion-de-importaciones", t="Industrialización por sustitución de importaciones (ISI)", cat="comercio", ic="🏗️",
alias="ISI sustitución de importaciones CEPAL industrialización protección arancelaria",
corto="Es una estrategia de desarrollo que busca producir dentro del país lo que antes se importaba, protegiendo a la industria local con aranceles altos y otras barreras.",
simple=[
r"Fue muy aplicada en América Latina entre los años cincuenta y setenta, inspirada en ideas de la CEPAL. Se usaron <a href='arancel.html'>aranceles</a> altos, cuotas, crédito barato y empresas públicas para crear industrias nacionales.",
r"Logró industrializar en parte la región, pero muchas industrias quedaron poco competitivas y dependientes de la protección. Con las crisis de deuda de los ochenta se abandonó y se pasó a modelos más abiertos.",
],
ejemplo=[
r"En el Perú de los años setenta, con aranceles muy altos, se armaban localmente productos como autos y electrodomésticos que antes se importaban, aunque a precios elevados.",
],
rel=["proteccionismo", "tesis-prebisch-singer", "apertura-comercial", "consenso-de-washington"],
))

T.append(dict(
slug="tesis-prebisch-singer", t="Tesis de Prebisch-Singer", cat="comercio", ic="⚖️",
alias="Prebisch-Singer deterioro de los términos de intercambio centro periferia CEPAL",
corto="Sostiene que, a largo plazo, los precios de las materias primas tienden a caer frente a los de los productos industriales, perjudicando a los países que exportan recursos naturales.",
simple=[
r"Raúl Prebisch y Hans Singer plantearon, hacia 1950, que los países de la «periferia» (exportadores de materias primas) perdían frente a los del «centro» (exportadores de manufacturas): con el tiempo debían vender más cobre o café para comprar la misma maquinaria.",
r"Esta idea sustentó la <a href='industrializacion-por-sustitucion-de-importaciones.html'>industrialización por sustitución de importaciones</a>. La evidencia es debatida, porque los precios de las materias primas tienen ciclos muy largos.",
],
ejemplo=[
r"Si un país necesita exportar 10 toneladas de café para comprar un tractor y años después necesita 15, sus <a href='terminos-de-intercambio.html'>términos de intercambio</a> se deterioraron.",
],
rel=["terminos-de-intercambio", "industrializacion-por-sustitucion-de-importaciones", "materias-primas", "maldicion-de-los-recursos"],
))

T.append(dict(
slug="consenso-de-washington", t="Consenso de Washington", cat="estado", ic="📋",
alias="Consenso de Washington Williamson reformas de mercado liberalización privatización",
corto="Es el conjunto de diez recomendaciones de política económica que se promovieron en América Latina desde fines de los ochenta: disciplina fiscal, apertura, privatizaciones y desregulación.",
simple=[
r"El economista John Williamson le puso ese nombre en 1989 a las reformas que recomendaban instituciones con sede en Washington, como el FMI y el <a href='banco-mundial.html'>Banco Mundial</a>. Incluían controlar el déficit, liberalizar el comercio y las finanzas, privatizar empresas públicas y proteger los derechos de propiedad.",
r"Ayudaron a estabilizar economías golpeadas por la <a href='hiperinflacion.html'>hiperinflación</a> y la deuda, pero también se les critica por no reducir lo suficiente la pobreza ni la desigualdad.",
],
ejemplo=[
r"Las reformas peruanas de los años noventa, como la apertura comercial, la independencia del BCRP y la privatización de empresas públicas, siguieron en buena parte esa agenda.",
],
rel=["reformas-estructurales", "privatizacion", "apertura-comercial", "hiperinflacion"],
))

T.append(dict(
slug="reformas-estructurales", t="Reformas estructurales", cat="estado", ic="🔩",
alias="reformas estructurales reformas de segunda generación productividad institucional",
corto="Son cambios profundos en las reglas de la economía, como en el mercado laboral, los impuestos, la justicia o la educación, que buscan elevar el crecimiento a largo plazo.",
simple=[
r"A diferencia de la política monetaria o fiscal, que mueve la economía en el corto plazo, las <strong>reformas estructurales</strong> cambian cómo funciona la economía: facilitan formar empresas, mejoran la competencia o hacen más eficiente al Estado.",
r"Sus beneficios suelen tardar años en verse y pueden tener costos iniciales para algunos grupos, por eso son difíciles de aprobar políticamente.",
],
ejemplo=[
r"Simplificar los trámites para abrir un negocio, reducir la informalidad o mejorar la calidad de la educación pública son ejemplos de reformas estructurales que elevan la <a href='productividad.html'>productividad</a>.",
],
rel=["consenso-de-washington", "productividad", "crecimiento-potencial", "informalidad"],
))

T.append(dict(
slug="privatizacion", t="Privatización", cat="estado", ic="🔑",
alias="privatización venta de empresas públicas concesiones Proinversión",
corto="Es la venta o el traspaso al sector privado de empresas o servicios que estaban en manos del Estado.",
simple=[
r"Se privatiza esperando que una gestión privada sea más eficiente, que el Estado reciba ingresos y que entre inversión. Puede hacerse vendiendo la empresa o dando una <strong>concesión</strong> por varios años.",
r"Para que funcione, debe haber buena regulación: si se pasa un monopolio público a uno privado sin control, los usuarios pueden terminar pagando más.",
],
ejemplo=[
r"En los años noventa, el Perú privatizó empresas de telefonía, electricidad y minería; los servicios regulados quedaron bajo la supervisión de organismos como Osiptel u Osinergmin.",
],
rel=["empresa-publica", "consenso-de-washington", "asociaciones-publico-privadas", "monopolio"],
))

# --- Desarrollo --------------------------------------------------------------

T.append(dict(
slug="capital-humano", t="Capital humano", cat="trabajo", ic="🎓",
alias="capital humano educación salud habilidades retorno de la educación",
corto="Son los conocimientos, habilidades y salud de las personas, que les permiten producir más y ganar más; se acumula con educación, experiencia y buena alimentación.",
simple=[
r"Igual que una máquina, una persona capacitada produce más. Por eso la educación y la salud se ven como una <strong>inversión</strong>: cuestan hoy y rinden en el futuro con mejores ingresos.",
r"El capital humano es una de las <a href='fuentes-de-crecimiento.html'>fuentes del crecimiento</a> de largo plazo. Muchos estudios estiman que cada año adicional de estudios se asocia con un aumento del ingreso, aunque medir el efecto causal tiene dificultades de <a href='endogeneidad.html'>endogeneidad</a>.",
],
ejemplo=[
r"Un técnico que aprende a operar maquinaria moderna puede producir mucho más y ganar un mejor sueldo que antes de capacitarse.",
],
rel=["fuentes-de-crecimiento", "productividad", "productividad-total-de-factores", "bono-demografico"],
))

T.append(dict(
slug="productividad-total-de-factores", t="Productividad total de factores (PTF)", cat="produccion", ic="⚙️",
alias="PTF residuo de Solow productividad multifactorial eficiencia tecnología",
corto="Es la parte del crecimiento que no se explica por usar más capital o más trabajo, sino por usarlos mejor: tecnología, organización y eficiencia.",
simple=[
r"Si un país produce más solo porque tiene más trabajadores y más máquinas, no se volvió más eficiente. La <strong>PTF</strong> mide lo que queda: cuánto más se produce con los mismos recursos.",
r"Por eso se le llama el «residuo de Solow». A largo plazo, es lo que explica la mayor parte de la diferencia de ingresos entre países ricos y pobres.",
],
formula=dict(
tex=r"g_Y=g_A+\alpha\,g_K+(1-\alpha)\,g_L",
donde=[(r"g_Y", "crecimiento del PBI"), (r"g_A", "crecimiento de la PTF"), (r"g_K,\ g_L", "crecimiento del capital y del trabajo"), (r"\alpha", "participación del capital")],
calculo=[r"g_A=4-0.4\times5-0.6\times2=4-2-1.2=0.8\,\%"],
),
ejemplo=[
r"Si el PBI creció 4 %, el capital 5 % y el trabajo 2 %, con \(\alpha=0.4\) la PTF creció alrededor de 0.8 %.",
],
rel=["fuentes-de-crecimiento", "modelo-de-solow", "productividad", "capital-humano"],
))

T.append(dict(
slug="curva-de-kuznets", t="Curva de Kuznets", cat="bienestar", ic="🔁",
alias="curva de Kuznets U invertida desigualdad desarrollo curva ambiental",
corto="Es la hipótesis de que la desigualdad primero sube y luego baja a medida que un país se desarrolla, formando una «U invertida».",
simple=[
r"Simon Kuznets observó que, al empezar a industrializarse, unos pocos se benefician primero y la desigualdad aumenta; luego, con más educación y políticas sociales, disminuye.",
r"La evidencia reciente es mixta: en muchos países ricos la desigualdad volvió a subir desde los años ochenta. Existe también una versión <strong>ambiental</strong>: la contaminación subiría y luego bajaría con el desarrollo.",
],
ejemplo=[
r"Si un país pasa de un <a href='coeficiente-de-gini.html'>Gini</a> de 0.40 a 0.50 en su etapa de industrialización y luego baja a 0.35 al volverse rico, seguiría la forma de la curva de Kuznets.",
],
rel=["coeficiente-de-gini", "distribucion-del-ingreso", "crecimiento-economico", "desarrollo-sostenible"],
))

T.append(dict(
slug="trampa-del-ingreso-medio", t="Trampa del ingreso medio", cat="produccion", ic="🪤",
alias="trampa del ingreso medio países de ingreso medio estancamiento",
corto="Es cuando un país deja de ser pobre pero no logra volverse rico: su crecimiento se estanca porque ya no compite con salarios bajos ni todavía con innovación.",
simple=[
r"Al principio, un país crece pasando gente del campo a la ciudad y aprovechando salarios bajos. Pero cuando los salarios suben, necesita aumentar su <a href='productividad.html'>productividad</a> e innovar para seguir creciendo.",
r"Si no mejora su educación, sus instituciones y su tecnología, queda «atrapado» en un nivel de ingreso medio por décadas. Corea del Sur es un ejemplo de país que logró salir de esa situación.",
],
ejemplo=[
r"Muchos países latinoamericanos alcanzaron ingresos medios hace décadas, pero no han logrado cerrar la brecha con los países ricos.",
],
rel=["productividad", "capital-humano", "reformas-estructurales", "crecimiento-potencial"],
))

T.append(dict(
slug="maldicion-de-los-recursos", t="Maldición de los recursos naturales", cat="comercio", ic="⛏️",
alias="maldición de los recursos paradoja de la abundancia rentismo",
corto="Es la observación de que muchos países ricos en recursos naturales crecen menos o tienen más conflictos que otros sin esa riqueza.",
simple=[
r"Las causas posibles son varias: la <a href='enfermedad-holandesa.html'>enfermedad holandesa</a>, la <a href='volatilidad.html'>volatilidad</a> de los precios de las materias primas, la búsqueda de rentas y la corrupción, o descuidar otros sectores y la educación.",
r"No es un destino: países como Noruega o Chile han manejado sus recursos con reglas fiscales y fondos de ahorro. Lo que importa es la calidad de las instituciones.",
],
ejemplo=[
r"Si un gobierno gasta todo el dinero del <a href='canon.html'>canon</a> en años de precios altos y luego no tiene cómo sostener ese gasto cuando bajan, sufre un síntoma típico de esta «maldición».",
],
rel=["enfermedad-holandesa", "materias-primas", "canon", "fondo-de-estabilizacion-fiscal"],
))

T.append(dict(
slug="desarrollo-sostenible", t="Desarrollo sostenible y ODS", cat="bienestar", ic="🌍",
alias="desarrollo sostenible Objetivos de Desarrollo Sostenible ODS Agenda 2030 Informe Brundtland",
corto="Es el desarrollo que satisface las necesidades de hoy sin poner en riesgo que las futuras generaciones satisfagan las suyas; la ONU lo organiza en 17 Objetivos de Desarrollo Sostenible.",
simple=[
r"La definición más conocida viene del Informe Brundtland (1987). Une tres dimensiones: crecimiento económico, inclusión social y cuidado del ambiente.",
r"En 2015, los países de la ONU aprobaron la <strong>Agenda 2030</strong> con 17 ODS, como el fin de la pobreza, el hambre cero, la educación de calidad y la acción por el clima.",
],
ejemplo=[
r"Una minera que invierte en tratar el agua que usa y en capacitar a la población local intenta compatibilizar su negocio con el desarrollo sostenible.",
],
rel=["economia-circular", "externalidad", "impuesto-al-carbono", "indice-de-desarrollo-humano"],
))

T.append(dict(
slug="economia-circular", t="Economía circular", cat="bienestar", ic="♻️",
alias="economía circular reciclaje reutilización residuos economía lineal",
corto="Es un modelo de producción que busca reutilizar, reparar y reciclar los materiales para reducir los residuos, en lugar de «extraer, usar y botar».",
simple=[
r"La economía tradicional es <strong>lineal</strong>: se extraen recursos, se fabrican productos y, al final, se botan. La <strong>circular</strong> diseña los productos para que duren más y sus materiales vuelvan a usarse.",
r"Reduce la presión sobre los recursos naturales y la contaminación, y puede crear negocios nuevos, como la reparación, el alquiler o el reciclaje.",
],
ejemplo=[
r"Una empresa de bebidas que recoge sus botellas usadas y las convierte en nuevas botellas aplica economía circular.",
],
rel=["desarrollo-sostenible", "externalidad", "impuesto-al-carbono", "materias-primas"],
))

T.append(dict(
slug="impuesto-al-carbono", t="Impuesto al carbono", cat="impuestos", ic="🌫️",
alias="impuesto al carbono precio del carbono emisiones de CO2 mercado de carbono",
corto="Es un impuesto sobre las emisiones de dióxido de carbono que busca que los contaminadores paguen el daño que causan al clima.",
simple=[
r"Las emisiones de CO₂ son una <a href='externalidad.html'>externalidad negativa</a>: quien quema combustibles no paga el daño del cambio climático. Un impuesto por tonelada emitida hace que contaminar cueste.",
r"Una alternativa son los <strong>mercados de carbono</strong>, donde se fija un límite de emisiones y las empresas compran y venden permisos.",
],
ejemplo=[
r"Si un impuesto cobra 50 dólares por tonelada de CO₂, una fábrica que emite 1000 toneladas al año pagaría 50 mil dólares, lo que la anima a cambiar a energías más limpias.",
],
rel=["externalidad", "desarrollo-sostenible", "economia-circular", "tributo"],
))

T.append(dict(
slug="pobreza-multidimensional", t="Pobreza multidimensional", cat="bienestar", ic="🧭",
alias="pobreza multidimensional IPM índice de pobreza multidimensional privaciones",
corto="Mide la pobreza no solo por el ingreso, sino por carencias en educación, salud y condiciones de vida, como agua, electricidad o vivienda.",
simple=[
r"La <a href='pobreza-monetaria.html'>pobreza monetaria</a> mira si el gasto alcanza para una canasta básica. La <strong>multidimensional</strong> revisa varias privaciones a la vez: niños fuera de la escuela, desnutrición, falta de agua potable, piso de tierra, etc.",
r"Un hogar se considera pobre multidimensional si acumula suficientes privaciones. El índice más conocido lo elaboran la Universidad de Oxford y el PNUD.",
],
ejemplo=[
r"Una familia puede tener un ingreso por encima de la línea de pobreza, pero vivir sin agua potable ni desagüe: no es pobre monetaria, pero sí tiene privaciones importantes.",
],
rel=["pobreza-monetaria", "indice-de-desarrollo-humano", "mapa-de-pobreza", "focalizacion"],
))

# --- Comercio internacional --------------------------------------------------

T.append(dict(
slug="globalizacion", t="Globalización", cat="comercio", ic="🌐",
alias="globalización integración mundial comercio internacional flujos de capital",
corto="Es la creciente conexión entre las economías del mundo a través del comercio, la inversión, la tecnología, las migraciones y la información.",
simple=[
r"Hoy un celular puede diseñarse en un país, fabricarse con piezas de diez países y venderse en todo el mundo. Esa integración bajó precios y sacó a millones de personas de la pobreza, sobre todo en Asia.",
r"También tiene costos: algunas industrias y trabajadores pierden frente a la competencia externa, y las crisis se contagian más rápido entre países.",
],
ejemplo=[
r"Las uvas y los arándanos peruanos llegan a supermercados de Europa, Estados Unidos y Asia gracias a la globalización del comercio.",
],
rel=["cadenas-globales-de-valor", "apertura-comercial", "omc", "proteccionismo"],
))

T.append(dict(
slug="cadenas-globales-de-valor", t="Cadenas globales de valor", cat="comercio", ic="⛓️",
alias="cadenas globales de valor cadenas de suministro fragmentación de la producción",
corto="Son las redes en las que distintas etapas de la producción de un bien se hacen en varios países, cada uno aportando una parte del valor.",
simple=[
r"Un producto ya no se fabrica entero en un solo lugar: el diseño, las materias primas, las piezas, el ensamblaje y la venta pueden estar en países distintos.",
r"Para un país, integrarse en etapas de mayor <a href='valor-agregado.html'>valor agregado</a> (diseño, tecnología, servicios) suele ser más rentable que quedarse solo en la extracción de materias primas.",
],
ejemplo=[
r"El cobre peruano puede refinarse en China, convertirse en cables en Vietnam y terminar dentro de un auto armado en México.",
],
rel=["globalizacion", "valor-agregado", "ventaja-competitiva", "exportaciones-e-importaciones"],
))

T.append(dict(
slug="ventaja-competitiva", t="Ventaja competitiva", cat="comercio", ic="🏆",
alias="ventaja competitiva Porter diamante de Porter diferenciación liderazgo en costos",
corto="Es lo que permite a una empresa o país superar a sus competidores de forma sostenida, ya sea por costos más bajos o por un producto diferente y valorado.",
simple=[
r"A diferencia de la <a href='ventaja-comparativa.html'>ventaja comparativa</a>, que surge de los recursos disponibles, la <strong>ventaja competitiva</strong> se construye: con innovación, calidad, marca, logística o capacitación.",
r"Michael Porter la estudió a nivel de empresas y de países; su «diamante» señala factores como la demanda local exigente, las industrias de apoyo y la rivalidad entre empresas.",
],
ejemplo=[
r"La gastronomía peruana logró una ventaja competitiva internacional gracias a su identidad, la formación de cocineros y la promoción, no solo por tener buenos insumos.",
],
rel=["ventaja-comparativa", "ventaja-absoluta", "cadenas-globales-de-valor", "productividad"],
))

T.append(dict(
slug="modelo-heckscher-ohlin", t="Modelo de Heckscher-Ohlin", cat="comercio", ic="🧱",
alias="Heckscher-Ohlin dotación de factores comercio internacional",
corto="Es una teoría del comercio que dice que cada país exporta los bienes que usan mucho el factor que tiene en abundancia, ya sea trabajo, capital o tierra.",
simple=[
r"Un país con mucha mano de obra y poco capital tenderá a exportar bienes que requieren mucho trabajo, como confecciones; uno con mucho capital exportará bienes intensivos en maquinaria y tecnología.",
r"Amplía la idea de <a href='ventaja-comparativa.html'>ventaja comparativa</a> de Ricardo, explicando de dónde viene. También predice que el comercio favorece a los dueños del factor abundante.",
],
ejemplo=[
r"El Perú, con abundantes recursos minerales, exporta sobre todo bienes intensivos en esos recursos, como cobre y oro.",
],
rel=["ventaja-comparativa", "ventaja-absoluta", "apertura-comercial", "materias-primas"],
))

T.append(dict(
slug="proteccionismo", t="Proteccionismo", cat="comercio", ic="🧱",
alias="proteccionismo barreras comerciales guerra comercial aranceles",
corto="Es la política de proteger a los productores nacionales de la competencia extranjera con aranceles, cuotas u otras barreras a las importaciones.",
simple=[
r"Se defiende para cuidar empleos, industrias nacientes o sectores estratégicos. Pero suele encarecer los productos para los consumidores y reducir la competencia y la <a href='productividad.html'>productividad</a>.",
r"Cuando varios países se responden con aranceles cada vez más altos, se produce una <strong>guerra comercial</strong> que reduce el comercio mundial.",
],
ejemplo=[
r"Si un país pone un arancel de 25 % a los autos importados, los autos nacionales pueden subir su precio sin perder clientes, y el comprador paga más.",
],
rel=["arancel", "barreras-al-comercio", "cuotas-de-importacion", "apertura-comercial"],
))

T.append(dict(
slug="cuotas-de-importacion", t="Cuotas de importación", cat="comercio", ic="🔢",
alias="cuota de importación contingente arancelario restricción cuantitativa",
corto="Son límites a la cantidad de un producto que se puede importar en un periodo.",
simple=[
r"A diferencia de un <a href='arancel.html'>arancel</a>, que encarece el producto, una cuota fija directamente cuánto puede entrar. Una vez alcanzado el límite, ya no se puede importar más, sin importar el precio.",
r"Las normas de la <a href='omc.html'>OMC</a> limitan su uso. Una variante es el <strong>contingente arancelario</strong>: una cantidad entra con arancel bajo y lo que excede paga un arancel mayor.",
],
ejemplo=[
r"Si un país solo permite importar 10 000 toneladas de azúcar al año, el precio interno subirá si la demanda supera esa cantidad.",
],
rel=["proteccionismo", "arancel", "barreras-al-comercio", "omc"],
))

T.append(dict(
slug="omc", t="OMC (Organización Mundial del Comercio)", cat="comercio", ic="🏛️",
alias="OMC Organización Mundial del Comercio GATT solución de controversias",
corto="Es la organización internacional que fija las reglas del comercio entre países y resuelve sus disputas comerciales.",
simple=[
r"Se creó en 1995, sucediendo al GATT, y el Perú es miembro desde su fundación. Sus miembros negocian la reducción de aranceles y se comprometen a no discriminar entre socios comerciales.",
r"Si un país cree que otro rompe las reglas, puede llevar el caso al sistema de <strong>solución de controversias</strong> de la OMC.",
],
ejemplo=[
r"Si un país pone de un día para otro un arancel muy alto solo a los productos de otro país, este puede reclamar ante la OMC.",
],
rel=["organismos-multilaterales", "arancel", "salvaguardia-y-antidumping", "globalizacion"],
))

T.append(dict(
slug="incoterms", t="Incoterms", cat="comercio", ic="📦",
alias="Incoterms FOB CIF EXW términos de comercio internacional Cámara de Comercio Internacional",
corto="Son términos estándar del comercio internacional que indican quién paga el transporte, el seguro y los trámites, y en qué punto pasa el riesgo del vendedor al comprador.",
simple=[
r"Los publica la Cámara de Comercio Internacional y se revisan cada cierto tiempo. Los más usados son <strong>FOB</strong> (el vendedor entrega la mercancía a bordo del barco en el puerto de origen) y <strong>CIF</strong> (el vendedor paga además el flete y el seguro hasta el puerto de destino).",
r"Las estadísticas de comercio suelen medir las exportaciones a valor FOB y las importaciones a valor CIF.",
],
ejemplo=[
r"Si un exportador peruano vende uvas en condición FOB Callao, su responsabilidad termina cuando la carga está a bordo del barco en el Callao; desde allí, flete y riesgos corren por cuenta del comprador.",
],
rel=["exportaciones-e-importaciones", "credito-documentario", "drawback", "balanza-comercial"],
))

T.append(dict(
slug="drawback", t="Drawback", cat="comercio", ic="↩️",
alias="drawback restitución de derechos arancelarios exportación SUNAT",
corto="Es un beneficio para los exportadores que les devuelve una parte de los aranceles pagados por los insumos importados que usaron para fabricar lo que exportan.",
simple=[
r"La idea es que los exportadores no pierdan competitividad por haber pagado aranceles en sus insumos. En el Perú existe un régimen simplificado de restitución que devuelve un porcentaje del valor FOB exportado, con requisitos y topes fijados por norma.",
r"Lo administra la SUNAT. Sus críticos señalan que puede funcionar como un subsidio a la exportación.",
],
ejemplo=[
r"Una empresa que importa tela, fabrica polos y los exporta puede solicitar el drawback para recuperar parte de los derechos que pagó al importar la tela.",
],
rel=["arancel", "exportaciones-e-importaciones", "subsidio", "zonas-francas"],
))

T.append(dict(
slug="zonas-francas", t="Zonas francas y zonas económicas especiales", cat="comercio", ic="🛃",
alias="zona franca ZOFRATACNA CETICOS zona económica especial beneficios tributarios",
corto="Son áreas de un país con reglas aduaneras y tributarias especiales, como no pagar aranceles ni ciertos impuestos, para atraer inversión y actividad económica.",
simple=[
r"Las empresas instaladas allí pueden importar insumos sin pagar aranceles, procesarlos y reexportarlos, o venderlos al resto del país pagando los impuestos al salir de la zona.",
r"En el Perú existen, por ejemplo, la Zona Franca de Tacna (ZOFRATACNA) y los CETICOS. Su efecto depende de si atraen actividades nuevas o solo trasladan las que ya existían.",
],
ejemplo=[
r"Una empresa puede ensamblar productos en una zona franca con piezas importadas sin aranceles y exportarlos a otros países.",
],
rel=["arancel", "drawback", "exoneracion-tributaria", "inversion-extranjera-directa"],
))

# --- Economía conductual -----------------------------------------------------

T.append(dict(
slug="economia-del-comportamiento", t="Economía del comportamiento", cat="mercados", ic="🧠",
alias="economía conductual behavioral economics Kahneman Thaler sesgos",
corto="Es la rama que estudia cómo decide realmente la gente, con sus sesgos y emociones, en lugar de suponer que siempre actúa de forma perfectamente racional.",
simple=[
r"Une economía y psicología. Muestra que las personas postergan el ahorro, temen más perder que ganar, se dejan influir por cómo se presentan las opciones y siguen a la mayoría.",
r"Daniel Kahneman (2002) y Richard Thaler (2017) recibieron el Premio Nobel de Economía por estas investigaciones. Sus ideas se usan para diseñar mejores políticas públicas.",
],
ejemplo=[
r"Mucha gente se inscribe en un gimnasio en enero con un plan anual y deja de ir en marzo: sobreestima su fuerza de voluntad futura.",
],
rel=["aversion-a-la-perdida", "sesgo-del-presente", "efecto-ancla", "nudge"],
))

T.append(dict(
slug="aversion-a-la-perdida", t="Aversión a la pérdida", cat="mercados", ic="😣",
alias="aversión a la pérdida teoría prospectiva Kahneman Tversky",
corto="Es la tendencia a sentir una pérdida con más fuerza que una ganancia del mismo tamaño.",
simple=[
r"Perder S/ 100 duele más de lo que alegra ganar S/ 100. Los estudios de Kahneman y Tversky sugieren que una pérdida pesa aproximadamente el doble que una ganancia equivalente.",
r"Por eso muchos inversionistas se aferran a acciones que bajaron esperando «recuperar», y venden demasiado rápido las que subieron.",
],
ejemplo=[
r"Una tienda que dice «evita perder tu descuento de S/ 20» suele convencer más que una que dice «gana S/ 20 de descuento».",
],
rel=["economia-del-comportamiento", "efecto-ancla", "toma-de-ganancias", "sesgo-del-presente"],
))

T.append(dict(
slug="sesgo-del-presente", t="Sesgo del presente", cat="mercados", ic="🍬",
alias="sesgo del presente descuento hiperbólico procrastinación gratificación inmediata",
corto="Es la tendencia a dar mucho más valor a lo que obtenemos ahora que a lo que obtendremos después, aunque después sea mejor.",
simple=[
r"Por este sesgo postergamos el ahorro, la dieta o el estudio: el sacrificio es hoy y el beneficio, lejano. Luego nos arrepentimos.",
r"Explica por qué ayudan los mecanismos de compromiso, como el ahorro automático, los aportes obligatorios a pensiones o las metas con fecha fija.",
],
ejemplo=[
r"Si te ofrecen S/ 100 hoy o S/ 110 en una semana, quizá prefieras los S/ 100 hoy; pero entre S/ 100 en un año o S/ 110 en un año y una semana, casi todos esperan la semana extra.",
],
rel=["economia-del-comportamiento", "nudge", "ahorro", "presupuesto-personal"],
))

T.append(dict(
slug="efecto-ancla", t="Efecto ancla", cat="mercados", ic="⚓",
alias="efecto ancla anclaje sesgo cognitivo precio de referencia",
corto="Es la tendencia a dejarse influir demasiado por el primer número que vemos al hacer una estimación o tomar una decisión.",
simple=[
r"Si una casaca aparece «antes S/ 400, ahora S/ 200», el S/ 400 actúa como <strong>ancla</strong> y los S/ 200 parecen baratos, aunque la casaca valga menos.",
r"Las anclas influyen en negociaciones de sueldo, precios de viviendas y hasta en las expectativas de inflación.",
],
ejemplo=[
r"En una negociación, quien propone primero una cifra alta suele lograr un acuerdo más cercano a esa cifra.",
],
rel=["economia-del-comportamiento", "aversion-a-la-perdida", "expectativas", "nudge"],
))

T.append(dict(
slug="nudge", t="Nudge (empujoncito)", cat="mercados", ic="👉",
alias="nudge empujón arquitectura de decisiones opción por defecto Thaler Sunstein",
corto="Es un cambio pequeño en cómo se presentan las opciones que lleva a las personas a decidir mejor, sin prohibir nada ni cambiar los incentivos económicos.",
simple=[
r"Richard Thaler y Cass Sunstein popularizaron la idea. Un ejemplo clásico es la <strong>opción por defecto</strong>: si te inscriben automáticamente en un plan de ahorro y tú puedes salirte, muchos más terminan ahorrando que si tuvieran que inscribirse por su cuenta.",
r"Se usa en salud, ahorro, impuestos y ambiente. Lo importante es que la persona conserve su libertad de elegir.",
],
ejemplo=[
r"Una carta de la autoridad tributaria que dice «9 de cada 10 vecinos ya pagaron su impuesto» suele aumentar los pagos a tiempo.",
],
rel=["economia-del-comportamiento", "sesgo-del-presente", "efecto-ancla", "afp-y-onp"],
))

# --- Trabajo y política social -----------------------------------------------

T.append(dict(
slug="salario-de-eficiencia", t="Salario de eficiencia", cat="trabajo", ic="💪",
alias="salario de eficiencia productividad rotación esfuerzo",
corto="Es la idea de que a una empresa le conviene pagar más que el salario de mercado, porque así sus trabajadores se esfuerzan más y renuncian menos.",
simple=[
r"Pagar un poco más reduce la rotación (y los costos de contratar y capacitar), atrae mejores postulantes y motiva a cuidar el empleo. Así, el sueldo más alto se compensa con mayor productividad.",
r"Esta teoría ayuda a explicar por qué los salarios no bajan aunque haya desempleo, y por qué puede haber desempleo involuntario.",
],
ejemplo=[
r"Una empresa de reparto que paga por encima del promedio puede tener menos renuncias y repartidores más cuidadosos con los pedidos.",
],
rel=["tasa-natural-de-desempleo", "productividad", "remuneracion-minima-vital", "monopsonio"],
))

T.append(dict(
slug="monopsonio", t="Monopsonio", cat="trabajo", ic="🧲",
alias="monopsonio comprador único poder de mercado en el empleo",
corto="Es un mercado con un solo comprador; en el trabajo, ocurre cuando un único empleador domina una zona y puede pagar sueldos más bajos.",
simple=[
r"El <a href='monopolio.html'>monopolio</a> es un solo vendedor; el <strong>monopsonio</strong> es un solo comprador. Si en un pueblo casi todos trabajan para la misma empresa, los trabajadores tienen pocas alternativas y aceptan sueldos menores.",
r"En estos casos, un salario mínimo moderado puede aumentar tanto los sueldos como el empleo, algo que no ocurre en un mercado competitivo.",
],
ejemplo=[
r"Una gran agroexportadora que es la única fuente de empleo en un valle tiene poder para fijar los sueldos de la zona.",
],
rel=["monopolio", "remuneracion-minima-vital", "salario-de-eficiencia", "negociacion-colectiva"],
))

T.append(dict(
slug="negociacion-colectiva", t="Negociación colectiva", cat="trabajo", ic="🗣️",
alias="negociación colectiva sindicato convenio colectivo pliego de reclamos",
corto="Es cuando los trabajadores, organizados en un sindicato, negocian juntos con el empleador sus sueldos y condiciones de trabajo.",
simple=[
r"En lugar de que cada trabajador negocie por su cuenta, el sindicato presenta un <strong>pliego de reclamos</strong> y se llega a un <strong>convenio colectivo</strong> que se aplica a todos.",
r"Puede mejorar los sueldos y equilibrar el poder frente a empleadores grandes. Si se exige más de lo que permite la productividad, puede afectar el empleo.",
],
ejemplo=[
r"Los trabajadores de una minera negocian con la empresa un aumento salarial anual y mejores condiciones de seguridad para todo el personal.",
],
rel=["monopsonio", "remuneracion-minima-vital", "empleo-formal-e-informal", "salario-de-eficiencia"],
))

T.append(dict(
slug="transferencias-condicionadas", t="Transferencias monetarias condicionadas", cat="bienestar", ic="🧒",
alias="transferencias condicionadas programa Juntos programas sociales corresponsabilidad",
corto="Son programas sociales que entregan dinero a familias pobres a cambio de que cumplan compromisos, como llevar a sus hijos al colegio y a sus controles de salud.",
simple=[
r"Buscan aliviar la pobreza hoy y, a la vez, mejorar el <a href='capital-humano.html'>capital humano</a> de los niños para que tengan más oportunidades en el futuro.",
r"En el Perú, el programa <strong>Juntos</strong> sigue este modelo. Ejemplos conocidos en otros países son Bolsa Família en Brasil y Prospera en México.",
],
ejemplo=[
r"Una madre que recibe el apoyo se compromete a que sus hijos asistan a la escuela y a los controles de salud; si cumple, sigue recibiendo la transferencia.",
],
rel=["focalizacion", "pobreza-monetaria", "capital-humano", "pension-no-contributiva"],
))

T.append(dict(
slug="pension-no-contributiva", t="Pensión no contributiva", cat="bienestar", ic="👴",
alias="pensión no contributiva Pensión 65 adultos mayores pobreza extrema",
corto="Es una pensión que el Estado entrega a adultos mayores en pobreza que nunca aportaron a un sistema de pensiones.",
simple=[
r"La mayoría de trabajadores informales no aporta a una <a href='afp-y-onp.html'>AFP ni a la ONP</a>, así que llega a la vejez sin pensión. Las pensiones no contributivas se financian con impuestos generales.",
r"En el Perú, el programa <strong>Pensión 65</strong> entrega una subvención periódica a personas de 65 años o más en situación de pobreza extrema.",
],
ejemplo=[
r"Un agricultor de 70 años que trabajó toda su vida de manera informal puede recibir Pensión 65 si cumple los requisitos de pobreza extrema.",
],
rel=["afp-y-onp", "transferencias-condicionadas", "focalizacion", "empleo-formal-e-informal"],
))

T.append(dict(
slug="focalizacion", t="Focalización del gasto social", cat="bienestar", ic="🎯",
alias="focalización SISFOH clasificación socioeconómica filtración subcobertura",
corto="Es el esfuerzo por dirigir los programas sociales a quienes realmente los necesitan, usando información sobre la situación de cada hogar.",
simple=[
r"Una mala focalización tiene dos errores: <strong>filtración</strong> (reciben el apoyo hogares que no lo necesitan) y <strong>subcobertura</strong> (quedan fuera hogares que sí lo necesitan).",
r"En el Perú, el Sistema de Focalización de Hogares (SISFOH) asigna una clasificación socioeconómica que usan varios programas sociales.",
],
ejemplo=[
r"Si un programa de alimentación llega a familias de ingresos altos y no a otras en pobreza, tiene problemas de focalización.",
],
rel=["transferencias-condicionadas", "pension-no-contributiva", "pobreza-multidimensional", "mapa-de-pobreza"],
))

T.append(dict(
slug="estado-de-bienestar", t="Estado de bienestar", cat="estado", ic="🏥",
alias="estado de bienestar protección social seguridad social universal",
corto="Es un modelo en el que el Estado garantiza a todos servicios y protecciones básicas, como salud, educación, pensiones y seguro de desempleo, financiados con impuestos.",
simple=[
r"Se desarrolló sobre todo en Europa después de la Segunda Guerra Mundial. Los países nórdicos son el ejemplo más citado, con altos impuestos y amplia cobertura social.",
r"Su financiamiento exige una alta <a href='presion-tributaria.html'>presión tributaria</a>, algo difícil en países con mucha <a href='informalidad.html'>informalidad</a> como el Perú.",
],
ejemplo=[
r"En un estado de bienestar, quien pierde su empleo recibe un seguro de desempleo por varios meses mientras busca otro trabajo.",
],
rel=["presion-tributaria", "renta-basica-universal", "pension-no-contributiva", "politica-fiscal"],
))

T.append(dict(
slug="renta-basica-universal", t="Renta básica universal", cat="bienestar", ic="🪪",
alias="renta básica universal ingreso básico incondicional",
corto="Es la propuesta de que el Estado pague a todas las personas un monto fijo periódico, sin condiciones y sin importar si trabajan o no.",
simple=[
r"Sus defensores dicen que reduce la pobreza, simplifica los programas sociales y protege frente a la automatización. Sus críticos señalan que es muy cara y que podría desincentivar el trabajo.",
r"Se han hecho experimentos en varios países, pero ninguno la aplica a toda su población de forma permanente.",
],
ejemplo=[
r"En una prueba piloto, un grupo de personas recibe un monto mensual durante dos años para estudiar cómo cambian su empleo, su salud y su bienestar.",
],
rel=["estado-de-bienestar", "transferencias-condicionadas", "pobreza-monetaria", "politica-fiscal"],
))

# --- Empresas y tributación en el Perú -----------------------------------------

T.append(dict(
slug="mype", t="MYPE (micro y pequeña empresa)", cat="produccion", ic="🏪",
alias="MYPE mipyme microempresa pequeña empresa REMYPE",
corto="Son las micro y pequeñas empresas; en el Perú se clasifican según sus ventas anuales medidas en UIT.",
simple=[
r"Según la ley peruana, una <strong>microempresa</strong> vende hasta 150 <a href='uit.html'>UIT</a> al año y una <strong>pequeña empresa</strong>, más de 150 y hasta 1700 UIT.",
r"Las MYPE dan empleo a la mayoría de trabajadores del país, pero muchas son informales y tienen baja productividad. Al inscribirse en el registro REMYPE pueden acceder a un régimen laboral especial.",
],
ejemplo=[
r"Con una UIT de S/ 5500, una bodega que vende S/ 500 mil al año (unas 91 UIT) sería una microempresa.",
],
rel=["uit", "regimen-mype-tributario", "informalidad", "nuevo-rus"],
))

T.append(dict(
slug="ruc", t="RUC (Registro Único de Contribuyentes)", cat="impuestos", ic="🔢",
alias="RUC registro único de contribuyentes SUNAT número de RUC 10 20",
corto="Es el número de 11 dígitos con el que la SUNAT identifica a las personas y empresas que realizan actividades por las que deben pagar impuestos.",
simple=[
r"Lo necesitas para emitir <a href='comprobantes-de-pago.html'>comprobantes de pago</a>, como facturas o recibos por honorarios. Las personas naturales suelen tener un RUC que empieza con 10 y las empresas, uno que empieza con 20.",
r"Tener RUC es el primer paso para formalizarse. Luego se elige un régimen tributario, como el <a href='nuevo-rus.html'>Nuevo RUS</a>, el <a href='regimen-especial-de-renta.html'>RER</a>, el <a href='regimen-mype-tributario.html'>RMT</a> o el régimen general.",
],
ejemplo=[
r"Una diseñadora que trabaja como independiente saca su RUC para emitir recibos por honorarios electrónicos a sus clientes.",
],
rel=["comprobantes-de-pago", "regimen-mype-tributario", "nuevo-rus", "rentas-de-cuarta-y-quinta-categoria"],
))

T.append(dict(
slug="regimen-mype-tributario", t="Régimen MYPE Tributario (RMT)", cat="impuestos", ic="🧾",
alias="RMT régimen MYPE tributario impuesto a la renta pequeñas empresas",
corto="Es un régimen del impuesto a la renta para micro y pequeñas empresas con ingresos netos de hasta 1700 UIT al año, con tasas menores que el régimen general.",
simple=[
r"Paga <strong>10 %</strong> sobre la utilidad anual hasta 15 <a href='uit.html'>UIT</a> y <strong>29.5 %</strong> sobre el exceso. En el régimen general, toda la utilidad paga 29.5 %.",
r"Además, los pagos a cuenta mensuales son más bajos para empresas pequeñas. Permite emitir todo tipo de comprobantes, incluidas facturas.",
],
formula=dict(
tex=r"\begin{aligned}\text{Impuesto}={}&10\,\%\times\min(U,\ 15\,\text{UIT})\\&+29.5\,\%\times\max(U-15\,\text{UIT},\ 0)\end{aligned}",
calculo=[r"0.10\times82\,500+0.295\times17\,500", r"=8250+5162.5=13\,412.5"],
),
ejemplo=[
r"Con una UIT de S/ 5500, 15 UIT son S/ 82 500. Una empresa con utilidad de S/ 100 000 pagaría S/ 8250 por el primer tramo y S/ 5162.50 por el resto: S/ 13 412.50 en total.",
],
rel=["mype", "impuesto-a-la-renta", "regimen-especial-de-renta", "uit"],
))

T.append(dict(
slug="regimen-especial-de-renta", t="Régimen Especial de Renta (RER)", cat="impuestos", ic="📄",
alias="RER régimen especial del impuesto a la renta 1.5 %",
corto="Es un régimen simplificado del impuesto a la renta para negocios pequeños, que pagan una cuota mensual de 1.5 % de sus ingresos netos.",
simple=[
r"En el <strong>RER</strong> no se calcula la utilidad: se paga cada mes el 1.5 % de los ingresos netos, y ese pago es definitivo. Está pensado para negocios con ingresos y compras anuales de hasta S/ 525 000 que no realicen ciertas actividades excluidas.",
r"Permite emitir facturas, a diferencia del <a href='nuevo-rus.html'>Nuevo RUS</a>. También se paga el <a href='igv.html'>IGV</a> aparte.",
],
formula=dict(
tex=r"\text{Cuota mensual}=1.5\,\%\times\text{Ingresos netos del mes}",
calculo=[r"0.015\times30\,000=450\ \text{soles}"],
),
ejemplo=[
r"Una ferretería que vende S/ 30 000 netos en un mes paga S/ 450 de impuesto a la renta en el RER.",
],
rel=["nuevo-rus", "regimen-mype-tributario", "impuesto-a-la-renta", "ruc"],
))

T.append(dict(
slug="comprobantes-de-pago", t="Comprobantes de pago", cat="impuestos", ic="🧾",
alias="factura boleta de venta recibo por honorarios comprobante electrónico SUNAT",
corto="Son los documentos que prueban una venta o un servicio, como la boleta, la factura o el recibo por honorarios; en el Perú los regula la SUNAT.",
simple=[
r"La <strong>boleta de venta</strong> se entrega sobre todo a consumidores finales. La <strong>factura</strong> se emite a empresas y permite usar el IGV pagado como <a href='credito-fiscal.html'>crédito fiscal</a>. El <strong>recibo por honorarios</strong> lo emiten los trabajadores independientes.",
r"Hoy la mayoría se emite de forma electrónica. Pedir tu comprobante ayuda a reducir la <a href='evasion-y-elusion-tributaria.html'>evasión</a>, porque así la venta queda registrada.",
],
ejemplo=[
r"Una empresa que compra útiles de oficina pide factura para usar el IGV de esa compra como crédito fiscal; una persona que compra para su casa recibe boleta.",
],
rel=["credito-fiscal", "igv", "ruc", "evasion-y-elusion-tributaria"],
))

T.append(dict(
slug="detracciones", t="Detracciones (SPOT)", cat="impuestos", ic="🏦",
alias="detracciones SPOT sistema de pago de obligaciones tributarias Banco de la Nación",
corto="Es un sistema en el que el comprador de ciertos bienes y servicios descuenta un porcentaje del pago y lo deposita en una cuenta del vendedor en el Banco de la Nación, que solo sirve para pagar impuestos.",
simple=[
r"El <strong>SPOT</strong> busca asegurar que los vendedores de sectores con alta evasión tengan fondos para pagar sus impuestos. El porcentaje depende del bien o servicio.",
r"El dinero de esa cuenta solo puede usarse para pagar tributos; si sobra durante un tiempo, el contribuyente puede pedir que se libere.",
],
ejemplo=[
r"Si una empresa contrata un servicio sujeto a detracción por S/ 10 000 y la tasa aplicable es 12 %, paga S/ 8800 al proveedor y deposita S/ 1200 en la cuenta de detracciones del proveedor en el Banco de la Nación.",
],
rel=["igv", "banco-de-la-nacion", "evasion-y-elusion-tributaria", "comprobantes-de-pago"],
))
