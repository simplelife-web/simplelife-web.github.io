# -*- coding: utf-8 -*-
# Términos del glosario (parte 1): precios, producción, dinero y bancos.
# Matemática en el texto: \( ... \). Fórmulas grandes: campo "formula".
# Campos: slug, t (término), cat, ic (emoji), corto, simple [párrafos], (fuentes: fuentes.py)
# ejemplo [párrafos], formula {tex, donde [(símbolo, significado)], calculo [líneas TeX]},
# ojo [puntos], rel [slugs], fuente (texto, url), alias (palabras para el buscador),
# herramienta (texto, url) opcional.


T = []

T.append(dict(
slug="inflacion", t="Inflación", cat="precios", ic="🎈",
alias="subida de precios carestia costo de vida",
corto="Es la subida general y sostenida de los precios. Con inflación, el mismo dinero alcanza para comprar menos cosas.",
simple=[
r"La inflación es el aumento <strong>general</strong> y <strong>sostenido</strong> de los precios de una economía. General quiere decir que no sube solo el pollo o solo el pasaje, sino la mayoría de bienes y servicios. Sostenido quiere decir que no es un salto de un día, sino una tendencia que dura meses.",
r"Cuando hay inflación, tu dinero pierde <strong>poder de compra</strong>: con los mismos 100 soles te llevas menos cosas del mercado que antes. Por eso la inflación golpea más a quienes viven de un sueldo fijo o tienen sus ahorros guardados en efectivo.",
r"En el Perú, la inflación se mide con el <a href=\"ipc.html\">índice de precios al consumidor (IPC)</a>, que calcula el INEI cada mes. El Banco Central de Reserva del Perú (BCRP) tiene como meta mantener la inflación anual entre <strong>1 % y 3 %</strong>, es decir, una inflación baja y estable.",
],
ejemplo=[
r"A fines de los años ochenta, el Perú vivió una <strong>hiperinflación</strong>: según el Banco Mundial, en 1990 los precios subieron más de 7000 % en el año. Los precios cambiaban de un día a otro y la gente corría a gastar su sueldo apenas lo cobraba. En cambio, desde 2002 el BCRP trabaja con metas de inflación, y el Perú suma más de 25 años seguidos con inflación anual de un solo dígito.",
r"Un ejemplo de bolsillo: si un menú costaba S/ 12.00 el año pasado y hoy cuesta S/ 12.60, su precio subió 5 %. Si casi todo sube parecido, la inflación del año fue de alrededor de 5 %.",
],
formula=dict(
tex=r"\pi_t=\frac{IPC_t-IPC_{t-1}}{IPC_{t-1}}\times 100",
donde=[(r"\pi_t", "inflación del periodo, en porcentaje"), (r"IPC_t", "índice de precios de este periodo"), (r"IPC_{t-1}", "índice de precios del periodo anterior")],
calculo=[r"IPC_{2025}=100,\quad IPC_{2026}=103", r"\pi=\frac{103-100}{100}\times 100=3\ \%"],
),
ojo=["Que la inflación baje no significa que los precios bajen: significa que suben más despacio. Cuando los precios bajan de verdad, se llama deflación.",
     "Un poco de inflación (alrededor de 2 % al año) se considera normal y sano para la economía."],
rel=["ipc", "deflacion", "poder-adquisitivo", "tasa-de-interes-real", "bcrp", "politica-monetaria"],
herramienta=("Calcula cuánto valen hoy tus soles de otro año", "../inflacion/"),
))

T.append(dict(
slug="ipc", t="Índice de precios al consumidor (IPC)", cat="precios", ic="🛒",
alias="ipc indice de precios canasta inei",
corto="Es un número que resume cuánto cuesta una canasta de bienes y servicios que compran las familias. Sirve para medir la inflación.",
simple=[
r"El IPC es como el «precio promedio» de todo lo que compra una familia típica: alimentos, pasajes, alquiler, luz, agua, educación, salud, ropa y más. Cada producto pesa según cuánto gastan en él los hogares; por ejemplo, la comida pesa más que los pasajes de avión.",
r"El IPC no está en soles: es un <strong>índice</strong>. Se elige un año base al que se le da el valor 100, y los demás meses se comparan con él. Si hoy el IPC es 110, la canasta cuesta 10 % más que en el año base.",
r"En el Perú lo calcula el <strong>INEI</strong> cada mes, con precios que recoge en mercados, tiendas y servicios. El dato más conocido es el de Lima Metropolitana, pero también hay un IPC a nivel nacional.",
],
ejemplo=[
r"Supón que la canasta de una familia limeña costaba S/ 2000 en el año base y hoy cuesta S/ 2180. El IPC de hoy sería 109: la canasta está 9 % más cara que en el año base.",
],
formula=dict(
tex=r"IPC_t=\frac{\sum_{j} p_{j,t}\,q_{j,0}}{\sum_{j} p_{j,0}\,q_{j,0}}\times 100",
donde=[(r"p_{j,t}", "precio de hoy del producto j"), (r"p_{j,0}", "precio del producto j en el año base"), (r"q_{j,0}", "cantidad del producto j que compraba la familia en el año base")],
calculo=[r"IPC=\frac{2180}{2000}\times 100=109"],
),
ojo=["Esta fórmula es la idea básica de un índice de precios con canasta fija (índice de Laspeyres). Como los hábitos de gasto cambian, cada cierto tiempo el INEI actualiza la canasta con nuevas encuestas a los hogares."],
rel=["inflacion", "deflacion", "poder-adquisitivo", "valor-nominal-y-real"],
herramienta=("Usa el IPC para actualizar montos de otros años", "../inflacion/"),
))

T.append(dict(
slug="deflacion", t="Deflación", cat="precios", ic="📉",
alias="baja de precios caida de precios desinflacion",
corto="Es la caída general y sostenida de los precios. Parece buena noticia, pero suele venir con menos ventas, menos producción y menos empleo.",
simple=[
r"La deflación es lo contrario de la <a href=\"inflacion.html\">inflación</a>: la mayoría de precios <strong>baja</strong> durante varios meses seguidos. Se ve en el IPC cuando la variación anual es negativa.",
r"¿Por qué preocupa si todo está más barato? Porque cuando la gente espera que los precios sigan bajando, <strong>posterga sus compras</strong>. Las empresas venden menos, producen menos y contratan menos. Además, las deudas pesan más, porque se pagan con soles que «valen más».",
r"No hay que confundirla con la <strong>desinflación</strong>, que es cuando la inflación baja (por ejemplo, de 8 % a 3 %): ahí los precios siguen subiendo, solo que más despacio.",
],
ejemplo=[
r"Que un mes baje el precio del limón por una buena cosecha no es deflación: es el cambio de un solo producto. Habría deflación si, mes tras mes, bajaran a la vez los alimentos, los servicios, la ropa y casi todo lo demás.",
],
formula=dict(
tex=r"\pi_t<0",
donde=[(r"\pi_t", "inflación anual medida con el IPC")],
calculo=[r"IPC_{2025}=100,\quad IPC_{2026}=99", r"\pi=\frac{99-100}{100}\times 100=-1\ \%\ \Rightarrow \text{deflación}"],
),
rel=["inflacion", "ipc", "recesion", "politica-monetaria"],
))

T.append(dict(
slug="poder-adquisitivo", t="Poder adquisitivo", cat="precios", ic="👛",
alias="poder de compra sueldo real salario real",
corto="Es la cantidad de bienes y servicios que puedes comprar con tu dinero. Si los precios suben más que tu sueldo, tu poder adquisitivo baja.",
simple=[
r"El poder adquisitivo no mide cuántos soles tienes, sino <strong>qué puedes hacer con ellos</strong>. Un sueldo de S/ 2000 rinde mucho si los precios están bajos y rinde poco si están altos.",
r"Por eso los economistas hablan de <strong>sueldo real</strong>: es el sueldo de siempre, pero «limpio» de inflación. Si tu sueldo sube 3 % y la inflación es 5 %, en realidad puedes comprar menos que antes, aunque cobres más soles.",
],
ejemplo=[
r"Ana ganaba S/ 2000 en 2025. En 2026 le subieron a S/ 2060 (3 % más), pero la inflación del año fue 5 %. Su sueldo real cayó: con S/ 2060 compra lo que antes compraba con unos S/ 1962.",
],
formula=dict(
tex=r"\text{Sueldo real}=\frac{\text{Sueldo nominal}}{IPC}\times 100",
donde=[(r"\text{Sueldo nominal}", "lo que dice tu boleta, en soles de hoy"), (r"IPC", "índice de precios del mismo periodo (año base = 100)")],
calculo=[r"\frac{2060}{105}\times 100\approx 1962\ \text{soles de 2025}"],
),
rel=["inflacion", "ipc", "valor-nominal-y-real", "remuneracion-minima-vital"],
herramienta=("Calcula cuánto valen hoy tus soles de otro año", "../inflacion/"),
))

T.append(dict(
slug="valor-nominal-y-real", t="Valor nominal y valor real", cat="precios", ic="⚖️",
alias="precios corrientes precios constantes deflactar",
corto="El valor nominal está en soles de cada año; el valor real quita el efecto de la inflación para comparar de forma justa entre años.",
simple=[
r"Un valor <strong>nominal</strong> (o «a precios corrientes») es el que ves escrito: tu sueldo, el precio de una casa o el PBI en soles de ese año. Un valor <strong>real</strong> (o «a precios constantes») es ese mismo monto después de quitarle la inflación.",
r"Comparar valores nominales de años distintos engaña, porque los soles de 2010 no compran lo mismo que los de 2026. Para comparar bien, se pasa todo a soles de un mismo año. A eso se le llama <strong>deflactar</strong>.",
],
ejemplo=[
r"Si el PBI nominal del Perú crece 7 % en un año y los precios suben 3 %, la producción de verdad (el PBI real) creció más o menos 4 %. El resto fue solo subida de precios.",
],
formula=dict(
tex=r"\text{Valor real}=\frac{\text{Valor nominal}}{\text{Índice de precios}}\times 100",
donde=[(r"\text{Índice de precios}", "IPC u otro índice, con el año base igual a 100")],
calculo=[r"g_{\text{real}}\approx g_{\text{nominal}}-\pi=7\ \%-3\ \%=4\ \%"],
),
rel=["inflacion", "ipc", "pbi", "poder-adquisitivo", "tasa-de-interes-real"],
))

T.append(dict(
slug="pbi", t="Producto bruto interno (PBI)", cat="produccion", ic="🏭",
alias="pbi pib producto interno bruto produccion economia tamaño",
corto="Es el valor de todos los bienes y servicios finales que se producen dentro de un país en un periodo, normalmente un año.",
simple=[
r"El PBI es la medida más usada del <strong>tamaño de una economía</strong>. Suma el valor de todo lo que se produce en el país: cobre, mangos, arándanos, cemento, clases, consultas médicas, viajes en combi y mucho más.",
r"Solo se cuentan bienes y servicios <strong>finales</strong>, para no contar dos veces lo mismo. Por ejemplo, la harina que usa una panadería ya está incluida en el precio del pan.",
r"«Interno» quiere decir que se cuenta lo producido <strong>dentro del Perú</strong>, aunque la empresa sea extranjera. En el Perú, el INEI calcula el PBI y el BCRP publica sus proyecciones.",
],
ejemplo=[
r"Una forma de calcularlo es por el lado del <strong>gasto</strong>: sumar lo que gastan las familias (consumo), las empresas (inversión), el Estado (gasto público) y lo que compran otros países (exportaciones), y restar lo que compramos de fuera (importaciones).",
],
formula=dict(
tex=r"PBI=C+I+G+(X-M)",
donde=[(r"C", "consumo de las familias"), (r"I", "inversión de empresas (maquinaria, edificios, existencias)"), (r"G", "gasto del Estado"), (r"X", "exportaciones"), (r"M", "importaciones")],
calculo=[r"C=650,\ I=200,\ G=150,\quad X=280,\ M=250", r"PBI=650+200+150+(280-250)=1030"],
),
ojo=["Los números del ejemplo son inventados para practicar; las cifras oficiales están en el INEI y el BCRP.",
     "El PBI mide producción, no bienestar: no cuenta el trabajo de casa no pagado ni cómo se reparte el ingreso."],
rel=["pbi-per-capita", "crecimiento-economico", "recesion", "valor-nominal-y-real", "balanza-comercial"],
))

T.append(dict(
slug="pbi-per-capita", t="PBI per cápita", cat="produccion", ic="🧍",
alias="pbi por persona ingreso por habitante",
corto="Es el PBI dividido entre la población: cuánto produce el país, en promedio, por cada habitante.",
simple=[
r"Comparar el PBI de China con el de Uruguay no dice mucho, porque China tiene muchísima más gente. El PBI per cápita (<em>por cabeza</em>) corrige eso y permite comparar el nivel de vida promedio entre países o entre años.",
r"Es un <strong>promedio</strong>: si unos pocos ganan muchísimo y la mayoría gana poco, el promedio puede verse alto aunque la mayoría no lo sienta. Por eso conviene mirarlo junto con medidas de desigualdad como el <a href=\"coeficiente-de-gini.html\">coeficiente de Gini</a>.",
],
ejemplo=[
r"Si un país produce 1030 mil millones de soles al año y tiene 34 millones de habitantes, su PBI per cápita es de unos S/ 30 300 por persona al año.",
],
formula=dict(
tex=r"PBI_{pc}=\frac{PBI}{\text{Población}}",
donde=[(r"PBI_{pc}", "PBI por habitante")],
calculo=[r"\frac{1\,030\,000\,000\,000}{34\,000\,000}\approx 30\,294\ \text{soles}"],
),
rel=["pbi", "crecimiento-economico", "coeficiente-de-gini", "pobreza-monetaria"],
))

T.append(dict(
slug="crecimiento-economico", t="Crecimiento económico", cat="produccion", ic="🌱",
alias="crecimiento del pbi tasa de crecimiento",
corto="Es el aumento de la producción de un país de un año a otro. Se mide con la variación del PBI real.",
simple=[
r"Cuando se dice «la economía creció 3 %», se habla del aumento del <a href=\"pbi.html\">PBI</a> <strong>real</strong>, es decir, de la producción sin contar la subida de precios.",
r"A largo plazo, un país crece cuando tiene más trabajadores, más máquinas e infraestructura (capital) y, sobre todo, cuando aprende a producir mejor (productividad), gracias a la educación, la tecnología y las buenas instituciones.",
],
ejemplo=[
r"Entre los años 2002 y 2013 el Perú creció rápido, impulsado por los altos precios de los minerales y la inversión. En 2020, por la pandemia, el PBI peruano cayó 11.12 % según el INEI, la peor caída en tres décadas, y en 2021 se recuperó con fuerza.",
],
formula=dict(
tex=r"g_t=\frac{PBI_t-PBI_{t-1}}{PBI_{t-1}}\times 100",
donde=[(r"g_t", "tasa de crecimiento del año t, en %"), (r"PBI_t", "PBI real del año t")],
calculo=[r"PBI_{t-1}=500,\ PBI_t=515", r"g=\frac{515-500}{500}\times 100=3\ \%"],
),
rel=["pbi", "pbi-per-capita", "recesion", "ciclo-economico", "inversion"],
))

T.append(dict(
slug="recesion", t="Recesión", cat="produccion", ic="🌧️",
alias="crisis economica caida del pbi depresion",
corto="Es una caída de la actividad económica que dura varios meses. Una regla práctica: dos trimestres seguidos con el PBI cayendo.",
simple=[
r"En una recesión el país produce menos que antes: las empresas venden menos, invierten menos y despiden personal, y las familias ganan y gastan menos.",
r"Una regla práctica muy usada dice que hay recesión cuando el <a href=\"pbi.html\">PBI</a> cae <strong>dos trimestres seguidos</strong> frente al trimestre anterior. No es una ley: muchos economistas miran además el empleo, las ventas y la producción.",
r"Si la caída es muy profunda y larga, se habla de <strong>depresión</strong>, como la Gran Depresión de los años treinta.",
],
ejemplo=[
r"Según el INEI, en 2023 el PBI peruano cayó 0.55 %; bajaron sobre todo la manufactura, la construcción, la pesca y el agro. En 2020, con la pandemia, la caída fue mucho más fuerte: 11.12 %.",
],
rel=["ciclo-economico", "crecimiento-economico", "pbi", "tasa-de-desempleo", "politica-fiscal"],
))

T.append(dict(
slug="ciclo-economico", t="Ciclo económico", cat="produccion", ic="🎢",
alias="auge expansion contraccion boom",
corto="Son las subidas y bajadas de la economía alrededor de su tendencia: épocas de auge seguidas de épocas de enfriamiento.",
simple=[
r"La economía no crece en línea recta. Pasa por etapas: <strong>expansión</strong> (más producción y empleo), <strong>auge o pico</strong>, <strong>contracción</strong> (la economía se enfría) y <strong>valle o fondo</strong>, desde donde vuelve a subir.",
r"Los gobiernos y los bancos centrales intentan suavizar estos ciclos: en épocas malas bajan tasas o gastan más, y en épocas de auge hacen lo contrario para que la economía no se «recaliente».",
],
ejemplo=[
r"En el Perú, el ciclo depende mucho de los precios de los minerales. Cuando el cobre y el oro suben de precio, entran más dólares, crecen la inversión y el empleo; cuando bajan, la economía se enfría.",
],
rel=["recesion", "crecimiento-economico", "politica-monetaria", "politica-fiscal", "terminos-de-intercambio"],
))

T.append(dict(
slug="tasa-de-interes", t="Tasa de interés", cat="dinero", ic="💯",
alias="interes precio del dinero tasa",
corto="Es el precio del dinero: lo que pagas por usar dinero prestado, o lo que te pagan por prestarlo o ahorrarlo.",
simple=[
r"Si pides un préstamo, la tasa de interés es lo que pagas de más por usar un dinero que no es tuyo. Si ahorras en un banco, es lo que el banco te paga por usar tu dinero. Se expresa como un porcentaje por un periodo: por año, por mes, etc.",
r"Las tasas de los préstamos son más altas que las de los ahorros: esa diferencia (el <em>spread</em>) cubre los costos del banco, el riesgo de que no le paguen y su ganancia.",
r"En el Perú, por la Ley 29888, los bancos deben informarte la <a href=\"tea.html\">TEA</a>, la <a href=\"tcea.html\">TCEA</a> (si te prestan) y la <a href=\"trea.html\">TREA</a> (si ahorras).",
],
ejemplo=[
r"Si prestas S/ 1000 a una tasa de 10 % al año, al final del año te deben devolver S/ 1100: los S/ 1000 más S/ 100 de interés.",
],
formula=dict(
tex=r"\text{Interés}=\text{Capital}\times i",
donde=[(r"i", "tasa de interés del periodo, en decimal (10 % = 0.10)")],
calculo=[r"1000\times 0.10=100\ \text{soles}"],
),
rel=["interes-simple", "interes-compuesto", "tea", "tcea", "trea", "tasa-de-referencia", "tasa-de-interes-real"],
))

T.append(dict(
slug="interes-simple", t="Interés simple", cat="dinero", ic="➕",
alias="interes lineal",
corto="Es el interés que se calcula siempre sobre el monto inicial. Los intereses ganados no generan nuevos intereses.",
simple=[
r"Con interés simple, cada periodo ganas (o pagas) lo mismo, porque el interés se calcula siempre sobre el <strong>capital inicial</strong>. Es fácil de calcular, pero en la vida real los bancos casi siempre usan el <a href=\"interes-compuesto.html\">interés compuesto</a>.",
],
ejemplo=[
r"Le prestas S/ 2000 a un familiar al 5 % anual simple, por 3 años. Cada año gana S/ 100, así que al final te devuelve S/ 2300.",
],
formula=dict(
tex=r"M=C\,(1+i\,n)",
donde=[(r"M", "monto final"), (r"C", "capital inicial"), (r"i", "tasa por periodo, en decimal"), (r"n", "número de periodos")],
calculo=[r"M=2000\,(1+0.05\times 3)=2300\ \text{soles}"],
),
rel=["interes-compuesto", "tasa-de-interes", "valor-presente-y-valor-futuro"],
))

T.append(dict(
slug="interes-compuesto", t="Interés compuesto", cat="dinero", ic="❄️",
alias="capitalizacion bola de nieve",
corto="Es el interés que se suma al capital y genera más intereses. Es el «efecto bola de nieve» del ahorro (y de las deudas).",
simple=[
r"Con interés compuesto, al final de cada periodo los intereses se <strong>suman al capital</strong> (se «capitalizan»). El periodo siguiente ganas intereses sobre un monto mayor. Por eso el dinero crece cada vez más rápido.",
r"Funciona igual para las deudas: si no pagas tu tarjeta, los intereses se suman a la deuda y empiezan a generar sus propios intereses.",
r"Una regla rápida es la <strong>regla del 72</strong>: divide 72 entre la tasa anual y sabrás, más o menos, en cuántos años se duplica tu dinero. Al 6 % anual, se duplica en unos 12 años.",
],
ejemplo=[
r"Depositas S/ 1000 en un plazo fijo que paga 6 % al año, por 3 años. No es S/ 1180 (como con interés simple), sino S/ 1191.02, porque cada año ganas intereses sobre los intereses anteriores.",
],
formula=dict(
tex=r"M=C\,(1+i)^{n}",
donde=[(r"M", "monto final"), (r"C", "capital inicial"), (r"i", "tasa por periodo, en decimal"), (r"n", "número de periodos")],
calculo=[r"M=1000\,(1+0.06)^{3},\quad M=1000\times 1.191016=1191.02\ \text{soles}"],
),
rel=["interes-simple", "tea", "trea", "valor-presente-y-valor-futuro", "ahorro"],
))

T.append(dict(
slug="tea", t="Tasa efectiva anual (TEA)", cat="dinero", ic="📅",
alias="tea tem tasa mensual tasa anual",
corto="Es la tasa de interés que realmente pagas o ganas en un año, contando que los intereses se capitalizan.",
simple=[
r"La TEA es la forma estándar de expresar una tasa en el Perú. «Efectiva» quiere decir que ya incluye el efecto del <a href=\"interes-compuesto.html\">interés compuesto</a> durante todo el año.",
r"Muchas veces necesitas la tasa <strong>mensual</strong> (TEM), por ejemplo para una cuota. Ojo: no basta con dividir la TEA entre 12, porque los intereses se capitalizan cada mes. Hay que usar la fórmula de equivalencia.",
r"La TEA solo mide el interés. Para saber cuánto te cuesta de verdad un préstamo, con comisiones y seguros, mira la <a href=\"tcea.html\">TCEA</a>.",
],
ejemplo=[
r"Una tarjeta de crédito con TEA de 60 % no cobra 5 % al mes (60 ÷ 12), sino casi 4 % mensual efectivo, que capitalizado durante 12 meses da exactamente 60 % al año.",
],
formula=dict(
tex=r"TEM=(1+TEA)^{1/12}-1",
donde=[(r"TEM", "tasa efectiva mensual"), (r"TEA", "tasa efectiva anual, en decimal")],
calculo=[r"TEM=(1+0.60)^{1/12}-1\approx 0.0399=3.99\ \%", r"TEA=(1+TEM)^{12}-1"],
),
rel=["tcea", "trea", "interes-compuesto", "tasa-de-interes"],
))

T.append(dict(
slug="tcea", t="Tasa de costo efectivo anual (TCEA)", cat="dinero", ic="🏷️",
alias="tcea costo del credito prestamo tarjeta comisiones",
corto="Es el costo total de un crédito en un año: incluye los intereses, las comisiones y los gastos, como los seguros.",
simple=[
r"La TCEA es la tasa que debes mirar para <strong>comparar préstamos y tarjetas</strong>. A diferencia de la <a href=\"tea.html\">TEA</a>, no solo cuenta el interés: también suma comisiones, el seguro de desgravamen y otros cobros obligatorios.",
r"En el Perú, la Ley 29888 obliga a los bancos y financieras a mostrar la TCEA de forma clara en toda oferta de crédito, incluso si te la dan de palabra. La Superintendencia de Banca, Seguros y AFP (SBS) supervisa que lo cumplan. Entre dos ofertas, la que tiene <strong>menor TCEA</strong> es la más barata.",
r"Técnicamente, según la ley, la TCEA es la tasa que iguala el valor actual de todas las cuotas que pagarás con el monto que realmente recibiste del préstamo.",
],
ejemplo=[
r"El banco A te ofrece un préstamo con TEA de 25 % y el banco B con TEA de 23 %. Parece mejor el B, pero si cobra un seguro y comisiones altas, su TCEA puede ser 30 % y la del A, 27 %. En ese caso, el A es más barato.",
],
formula=dict(
tex=r"P=\sum_{k=1}^{n}\frac{c_k}{(1+TCEM)^{k}},\qquad TCEA=(1+TCEM)^{12}-1",
donde=[(r"P", "monto que recibes del préstamo"), (r"c_k", "cuota total del mes k (con intereses, comisiones y seguros)"), (r"n", "número de cuotas mensuales"), (r"TCEM", "tasa de costo efectivo mensual")],
),
ojo=["Los intereses moratorios y las penalidades por atraso no entran en la TCEA: si te atrasas, pagarás más."],
rel=["tea", "tasa-de-interes", "valor-presente-y-valor-futuro", "tir"],
))

T.append(dict(
slug="trea", t="Tasa de rendimiento efectivo anual (TREA)", cat="dinero", ic="🐷",
alias="trea ahorro plazo fijo rendimiento cuenta de ahorros",
corto="Es lo que realmente gana tu ahorro en un año, después de restar comisiones y gastos de la cuenta.",
simple=[
r"La TREA es la hermana de la <a href=\"tcea.html\">TCEA</a>, pero para los <strong>ahorros</strong>. Te dice cuánto crece tu dinero en un año después de descontar las comisiones de mantenimiento y otros cobros. La Ley 29888 obliga a los bancos a informarla en sus ofertas de cuentas y depósitos.",
r"Si la cuenta cobra comisiones y tienes poco dinero, la TREA puede ser incluso <strong>negativa</strong>: tu saldo baja en vez de subir. Para comparar cuentas y depósitos a plazo, elige la de <strong>mayor TREA</strong>.",
],
ejemplo=[
r"Dejas S/ 5000 en un depósito a plazo fijo por un año con TREA de 5 %. Al final del año tendrás S/ 5250. Si otro banco ofrece TREA de 6 %, tendrías S/ 5300.",
],
formula=dict(
tex=r"M=C\,(1+TREA)",
donde=[(r"C", "monto depositado"), (r"M", "monto al cabo de un año, ya sin comisiones")],
calculo=[r"M=5000\,(1+0.05)=5250\ \text{soles}"],
),
rel=["tea", "interes-compuesto", "ahorro", "tasa-de-interes-real"],
))

T.append(dict(
slug="tasa-de-interes-real", t="Tasa de interés real", cat="dinero", ic="🔍",
alias="ecuacion de fisher tasa nominal tasa real",
corto="Es la tasa de interés después de descontar la inflación. Mide cuánto crece de verdad tu poder de compra.",
simple=[
r"La tasa que te ofrece el banco es <strong>nominal</strong>: dice cuántos soles más tendrás. Pero si los precios también suben, parte de esa ganancia se la come la <a href=\"inflacion.html\">inflación</a>. La tasa <strong>real</strong> mide lo que ganas en cosas que puedes comprar.",
r"La relación entre ambas se llama <strong>ecuación de Fisher</strong>, por el economista Irving Fisher. Cuando las tasas son bajas, basta con restar: tasa real ≈ tasa nominal − inflación.",
],
ejemplo=[
r"Tu depósito rinde 5 % al año y la inflación es 2 %. Tu tasa real es casi 3 %: con el dinero del depósito puedes comprar 3 % más cosas que hace un año. Si la inflación fuera 6 %, tu tasa real sería negativa: aunque tengas más soles, compras menos.",
],
formula=dict(
tex=r"1+r=\frac{1+i}{1+\pi}\quad\Longrightarrow\quad r\approx i-\pi",
donde=[(r"r", "tasa de interés real"), (r"i", "tasa de interés nominal"), (r"\pi", "inflación")],
calculo=[r"r=\frac{1.05}{1.02}-1\approx 0.0294=2.94\ \%"],
),
rel=["inflacion", "tasa-de-interes", "trea", "valor-nominal-y-real", "tasa-de-referencia"],
))

T.append(dict(
slug="bcrp", t="Banco Central de Reserva del Perú (BCRP)", cat="dinero", ic="🏛️",
alias="bcrp banco central reserva emisor del sol",
corto="Es la institución que cuida el valor del sol: controla la inflación, emite los billetes y monedas y administra las reservas internacionales.",
simple=[
r"El BCRP es el <strong>banco central</strong> del Perú. No atiende al público ni da préstamos a las personas: su trabajo es mantener la <strong>estabilidad monetaria</strong>, es decir, que el sol conserve su valor y la inflación sea baja.",
r"Según la Constitución (artículo 84), su finalidad es <strong>preservar la estabilidad monetaria</strong> y es una institución <strong>autónoma</strong>. Además, tiene prohibido financiar al Tesoro Público: no puede prestarle dinero al Gobierno (solo puede comprar bonos del Tesoro en el mercado secundario, con un límite que fija su ley).",
r"La Constitución le encarga regular la moneda y el crédito del sistema financiero, administrar las <strong>reservas internacionales</strong>, emitir billetes y monedas e informar periódicamente al país sobre las finanzas nacionales. Para regular el crédito usa, sobre todo, la <a href=\"tasa-de-referencia.html\">tasa de referencia</a>.",
],
ejemplo=[
r"Cada mes, el Directorio del BCRP anuncia si sube, baja o mantiene la tasa de referencia, según cómo vea la inflación. Además, publica gratis estadísticas como el tipo de cambio, las tasas de interés y el PBI.",
],
rel=["politica-monetaria", "tasa-de-referencia", "inflacion", "encaje-bancario", "tipo-de-cambio"],
))

T.append(dict(
slug="tasa-de-referencia", t="Tasa de referencia", cat="dinero", ic="🎯",
alias="tasa de politica monetaria tasa del bcrp tasa de interes de referencia",
corto="Es la tasa de interés que fija el BCRP como guía para las tasas de los préstamos entre bancos. Es su principal herramienta contra la inflación.",
simple=[
r"La tasa de referencia es la meta que el BCRP fija para la tasa de interés a la que los bancos se prestan dinero entre sí de un día para otro (la tasa interbancaria). A partir de ella se mueven, poco a poco, las tasas de los préstamos y los ahorros.",
r"Si la <a href=\"inflacion.html\">inflación</a> sube demasiado, el BCRP <strong>sube</strong> la tasa: los créditos se encarecen, la gente y las empresas gastan menos y los precios se calman. Si la economía está débil y la inflación baja, la <strong>baja</strong> para animar el crédito y el gasto.",
],
ejemplo=[
r"En abril de 2020, por la pandemia, el BCRP bajó su tasa a 0.25 %, la más baja de su historia, para abaratar el crédito. Entre 2021 y 2023, cuando la inflación superó con creces la meta, la subió varias veces seguidas; cuando la inflación volvió al rango de 1 % a 3 %, empezó a bajarla. El valor actual se publica en la nota de prensa del programa monetario de cada mes.",
],
rel=["bcrp", "politica-monetaria", "tasa-de-interes", "inflacion", "tasa-de-interes-real"],
))

T.append(dict(
slug="politica-monetaria", t="Política monetaria", cat="dinero", ic="🎛️",
alias="politica monetaria expansiva contractiva metas de inflacion",
corto="Son las decisiones del banco central sobre las tasas de interés y la cantidad de dinero para mantener la inflación baja y estable.",
simple=[
r"La política monetaria la hace el <a href=\"bcrp.html\">BCRP</a>. Su herramienta principal es la <a href=\"tasa-de-referencia.html\">tasa de referencia</a>; también usa el <a href=\"encaje-bancario.html\">encaje</a> y compra o vende dólares para evitar saltos bruscos del tipo de cambio.",
r"Es <strong>expansiva</strong> cuando baja tasas para que haya más crédito y gasto, y <strong>contractiva</strong> cuando las sube para frenar la inflación.",
r"Desde 2002 el Perú usa un esquema de <strong>metas explícitas de inflación</strong>: el BCRP anuncia una meta y orienta sus decisiones a cumplirla. Desde 2007, esa meta es un rango de entre 1 % y 3 % al año.",
],
ejemplo=[
r"Durante la pandemia de 2020, el BCRP bajó su tasa de referencia a 0.25 %, la más baja de su historia, y apoyó programas como Reactiva Perú para que las empresas pudieran conseguir préstamos y no cortar la cadena de pagos.",
],
rel=["bcrp", "tasa-de-referencia", "politica-fiscal", "encaje-bancario", "inflacion"],
))

T.append(dict(
slug="encaje-bancario", t="Encaje bancario", cat="dinero", ic="🔒",
alias="encaje reservas bancarias multiplicador bancario",
corto="Es la parte de los depósitos que los bancos no pueden prestar y deben guardar en sus bóvedas o en el BCRP.",
simple=[
r"Cuando depositas dinero, el banco no lo guarda todo: presta una parte a otras personas. El encaje es la porción que <strong>sí debe guardar</strong>, para tener siempre efectivo y devolver el dinero a quien lo pida.",
r"El BCRP fija la tasa de encaje. Si la sube, los bancos tienen menos para prestar; si la baja, pueden prestar más. Además, aplica encajes adicionales a los créditos en dólares para reducir poco a poco la <a href=\"dolarizacion.html\">dolarización</a> del crédito, que es más riesgoso para quien gana en soles.",
],
ejemplo=[
r"Si la tasa de encaje fuera 10 % y depositas S/ 1000, el banco guarda S/ 100 y puede prestar S/ 900. Ese préstamo vuelve a depositarse en algún banco, que guarda 10 % y presta el resto, y así sucesivamente. Así se «multiplica» el dinero en la economía.",
],
formula=dict(
tex=r"m=\frac{1}{e}",
donde=[(r"m", "multiplicador bancario (versión simple)"), (r"e", "tasa de encaje, en decimal")],
calculo=[r"m=\frac{1}{0.10}=10,\quad 1000\times 10=10\,000\ \text{soles (máximo)}"],
),
ojo=["Es una versión de libro de texto: en la realidad la gente también guarda efectivo y los bancos no prestan todo, así que el multiplicador es menor."],
rel=["bcrp", "politica-monetaria", "dolarizacion", "tasa-de-interes"],
))

T.append(dict(
slug="dolarizacion", t="Dolarización", cat="dinero", ic="💵",
alias="desdolarizacion dolares ahorro en dolares credito en dolares",
corto="Es el uso del dólar en lugar de la moneda nacional para ahorrar, prestar o poner precios dentro de un país.",
simple=[
r"Después de la hiperinflación de los ochenta, muchos peruanos dejaron de confiar en la moneda nacional y se pasaron al dólar para ahorrar, prestar y fijar precios de casas o autos. A eso se le llama dolarización.",
r"La dolarización es un riesgo cuando alguien <strong>gana en soles y debe en dólares</strong>: si el dólar sube, su deuda en soles crece de golpe. Por eso el BCRP ha impulsado la <strong>desdolarización</strong>, con encajes adicionales que encarecen prestar en dólares.",
r"Con la inflación baja de las últimas décadas, el sol recuperó la confianza de la gente y hoy los peruanos usan mucho más el sol que en los años noventa.",
],
ejemplo=[
r"Pedro gana S/ 3000 y tiene un crédito hipotecario con cuota de US$ 500. Con el dólar a S/ 3.50, paga S/ 1750 al mes. Si el dólar sube a S/ 4.00, la cuota pasa a S/ 2000, aunque su sueldo siga igual.",
],
rel=["tipo-de-cambio", "depreciacion-y-apreciacion", "encaje-bancario", "bcrp"],
))

T.append(dict(
slug="tipo-de-cambio", t="Tipo de cambio", cat="dinero", ic="💱",
alias="precio del dolar compra venta cambio de moneda",
corto="Es el precio de una moneda expresado en otra. En el Perú, normalmente es cuántos soles cuesta un dólar.",
simple=[
r"Si el tipo de cambio es 3.50, necesitas S/ 3.50 para comprar un dólar. En las casas de cambio y los bancos verás dos precios: el de <strong>compra</strong> (lo que te pagan por tus dólares) y el de <strong>venta</strong> (lo que te cobran por darte dólares). La venta siempre es un poco más alta: esa diferencia es su ganancia.",
r"En el Perú el tipo de cambio es <strong>flexible</strong>: lo fijan la oferta y la demanda de dólares. El BCRP no fija un precio, pero interviene en el mercado para «atenuar la volatilidad»: por ejemplo, en 2021, con la incertidumbre política, ofreció más de US$ 10 000 millones para calmar la subida del dólar.",
],
ejemplo=[
r"Quieres comprar US$ 200 y la casa de cambio vende a S/ 3.52: pagarás S/ 704. Si al día siguiente vendes esos US$ 200 a un precio de compra de S/ 3.48, recibirás S/ 696.",
],
formula=dict(
tex=r"\text{Soles}=\text{Dólares}\times TC,\qquad \text{Dólares}=\frac{\text{Soles}}{TC}",
donde=[(r"TC", "tipo de cambio en soles por dólar")],
calculo=[r"200\times 3.52=704\ \text{soles}"],
),
rel=["depreciacion-y-apreciacion", "dolarizacion", "bcrp", "balanza-comercial"],
))

T.append(dict(
slug="depreciacion-y-apreciacion", t="Depreciación y apreciación del sol", cat="dinero", ic="↕️",
alias="devaluacion revaluacion sube el dolar baja el dolar",
corto="El sol se deprecia cuando pierde valor frente al dólar (el dólar sube) y se aprecia cuando gana valor (el dólar baja).",
simple=[
r"Si el dólar pasa de S/ 3.50 a S/ 3.80, necesitas más soles para comprar un dólar: el sol se <strong>depreció</strong>. Si baja de S/ 3.80 a S/ 3.60, el sol se <strong>apreció</strong>.",
r"A quién le conviene depende de cada uno. Una depreciación ayuda a los <strong>exportadores</strong> (reciben dólares que valen más soles) y perjudica a quien <strong>importa</strong> o tiene <strong>deudas en dólares</strong>. Además, encarece productos importados como el combustible o los celulares.",
r"Con tipo de cambio flexible se dice depreciación o apreciación. Las palabras <strong>devaluación</strong> y revaluación se usan cuando un gobierno con tipo de cambio fijo cambia el precio oficial.",
],
ejemplo=[
r"Un exportador de palta vende un contenedor por US$ 30 000. Con el dólar a S/ 3.50 recibe S/ 105 000; si el dólar sube a S/ 3.80, recibe S/ 114 000 por la misma fruta.",
],
formula=dict(
tex=r"\%\Delta TC=\frac{TC_{\text{hoy}}-TC_{\text{antes}}}{TC_{\text{antes}}}\times 100",
donde=[(r"TC", "tipo de cambio en soles por dólar")],
calculo=[r"\frac{3.80-3.50}{3.50}\times 100\approx 8.6\ \%\ \Rightarrow\ \text{el sol se depreció}"],
),
rel=["tipo-de-cambio", "dolarizacion", "balanza-comercial", "terminos-de-intercambio"],
))
