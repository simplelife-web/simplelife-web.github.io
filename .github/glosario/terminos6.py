# -*- coding: utf-8 -*-
# Términos del glosario (parte 6): cuarta tanda tomada de la lista del
# Glosario de Términos Económicos del BCRP. Las definiciones están
# redactadas con palabras propias; el campo "bcrp" guarda el nombre exacto
# del término en ese glosario para citarlo como fuente.

T = []

T.append(dict(
slug="ahorro-financiero", t="Ahorro financiero", cat="finanzas", ic="🏦",
bcrp="Ahorro financiero", alias="ahorro en el sistema financiero depósitos fondos",
corto="Es el ahorro que la gente guarda dentro del sistema financiero, como depósitos, fondos mutuos o fondos de pensiones, y no «debajo del colchón».",
simple=[
r"No todo el <a href='ahorro.html'>ahorro</a> es igual. Si guardas billetes en casa o compras ladrillos, ahorras, pero ese dinero no circula. Cuando lo depositas en un banco, lo pones en un fondo o aportas a una AFP, se vuelve <strong>ahorro financiero</strong>.",
r"Es importante porque los bancos y fondos lo prestan o lo invierten en empresas y proyectos. Mientras más ahorro financiero hay, más crédito puede haber para la economía.",
],
ejemplo=[
r"Una familia que deja de guardar S/ 3000 en una lata y los pone en un depósito a plazo convierte ese dinero en ahorro financiero: gana intereses y el banco puede prestarlo.",
],
rel=["ahorro", "deposito-de-ahorro", "intermediacion-financiera", "bancarizacion"],
))

T.append(dict(
slug="balanza-de-servicios", t="Balanza de servicios", cat="comercio", ic="✈️",
bcrp="Balanza de servicios", alias="exportación de servicios turismo fletes seguros",
corto="Registra lo que un país vende y compra al exterior en servicios: turismo, transporte, seguros, comunicaciones y otros.",
simple=[
r"Además de bienes, los países comercian <strong>servicios</strong>. Cuando un turista extranjero gasta en Cusco, el Perú exporta un servicio. Cuando una empresa peruana paga fletes a una naviera extranjera o seguros a una aseguradora de afuera, importa servicios.",
r"La balanza de servicios es parte de la <a href='balanza-en-cuenta-corriente.html'>cuenta corriente</a>. En el Perú suele tener déficit, porque se pagan muchos fletes y seguros por las importaciones y exportaciones.",
],
ejemplo=[
r"Si el Perú recibe US$ 4000 millones por turismo y otros servicios, pero paga US$ 6000 millones en fletes, seguros y servicios empresariales, su balanza de servicios tiene un déficit de US$ 2000 millones.",
],
formula=dict(
tex=r"\text{Balanza de servicios}=X_{\text{servicios}}-M_{\text{servicios}}",
calculo=[r"4000-6000=-2000\ \text{millones de US\$}"],
),
rel=["balanza-en-cuenta-corriente", "balanza-comercial", "balanza-de-pagos", "exportaciones-tradicionales-y-no-tradicionales"],
))

T.append(dict(
slug="barreras-al-comercio", t="Barreras al comercio", cat="comercio", ic="🚧",
bcrp="Barreras al comercio", alias="barreras arancelarias no arancelarias proteccionismo cuotas",
corto="Son medidas que dificultan o encarecen el comercio entre países, como los aranceles, las cuotas o los trámites excesivos.",
simple=[
r"Las <strong>barreras arancelarias</strong> son impuestos a las importaciones (<a href='arancel.html'>aranceles</a>). Las <strong>no arancelarias</strong> son todo lo demás: cuotas que limitan cuánto se importa, licencias, normas técnicas o sanitarias muy exigentes, o trámites lentos.",
r"Algunas tienen razones válidas, como proteger la salud. Otras se usan para proteger a productores locales de la competencia, lo que suele subir los precios para los consumidores.",
],
ejemplo=[
r"Para exportar arándanos a algunos países, los productores peruanos deben cumplir protocolos sanitarios estrictos. Aunque no paguen arancel, esos requisitos funcionan como una barrera no arancelaria.",
],
rel=["arancel", "apertura-comercial", "salvaguardia-y-antidumping", "zona-de-libre-comercio"],
))

T.append(dict(
slug="circulante", t="Circulante", cat="dinero", ic="💵",
bcrp="Billetes y monedas en circulación", alias="billetes y monedas efectivo en manos del público",
corto="Son los billetes y monedas que están en manos de la gente y de las empresas, fuera de los bancos.",
simple=[
r"El BCRP es el único que puede emitir billetes y monedas en el Perú. Los que están en tu billetera o en la caja de una bodega forman el <strong>circulante</strong>.",
r"Es la parte más líquida del dinero. Su demanda sube en fechas como Navidad o Fiestas Patrias y baja cuando la gente usa más pagos digitales.",
],
ejemplo=[
r"En diciembre, cuando la gente cobra la gratificación y hace compras navideñas, aumenta el circulante. En enero, buena parte de esos billetes vuelve a los bancos.",
],
rel=["agregados-monetarios", "base-monetaria", "dinero", "curso-legal"],
))

T.append(dict(
slug="canasta-de-consumo", t="Canasta de consumo", cat="precios", ic="🧺",
bcrp="Canasta de consumo", alias="canasta familiar canasta del IPC ponderaciones",
corto="Es la lista de bienes y servicios que compra una familia típica, con el peso que tiene cada uno en su gasto. Sirve para calcular el IPC.",
simple=[
r"Para medir la inflación, el INEI no mira un solo precio, sino una <strong>canasta</strong> de alimentos, transporte, vivienda, educación, salud y otros gastos. Cada producto tiene un <strong>peso</strong> según cuánto gastan en él las familias, que se obtiene de encuestas de presupuestos familiares.",
r"Por eso, si sube mucho un producto que pesa poco en la canasta, el <a href='ipc.html'>IPC</a> casi no se mueve. Cada cierto tiempo se actualiza la canasta para reflejar nuevos hábitos de consumo.",
],
ejemplo=[
r"Con números de ejemplo: si los alimentos pesan 25 % en la canasta y suben 8 %, aportan unos 2 puntos a la inflación (0.25 × 8 %).",
],
formula=dict(
tex=r"\pi\approx\sum_i w_i\,\pi_i",
donde=[(r"w_i", "peso del rubro i en la canasta"), (r"\pi_i", "variación de precio del rubro i")],
calculo=[r"0.25\times 8\ \%=2\ \text{puntos}"],
),
rel=["ipc", "inflacion", "costo-de-vida", "poder-adquisitivo"],
herramienta=("Mira cómo cambian los precios por rubro", "../precios/"),
))

T.append(dict(
slug="cobertura", t="Cobertura de riesgos", cat="finanzas", ic="☂️",
bcrp="Cobertura", alias="hedging cubrirse protección contra riesgos",
corto="Es tomar una posición financiera que compensa las pérdidas que podría causar un riesgo, como una subida del dólar o una caída de precios.",
simple=[
r"Cubrirse es como comprar un seguro: aceptas un pequeño costo hoy para no sufrir una gran pérdida mañana. Se hace con contratos como <a href='contrato-forward.html'>forwards</a>, <a href='contrato-de-futuro.html'>futuros</a>, <a href='opcion.html'>opciones</a> o <a href='swaps.html'>swaps</a>.",
r"La cobertura no busca ganar dinero, sino reducir la incertidumbre. Si el riesgo no ocurre, quizá «perdiste» el costo de cubrirte, pero dormiste tranquilo.",
],
ejemplo=[
r"Un exportador de café sabe que cobrará US$ 100 000 en seis meses. Si teme que el dólar baje, vende esos dólares hoy con un forward. Así sabe exactamente cuántos soles recibirá.",
],
rel=["riesgo-cambiario", "contrato-forward", "contrato-de-futuro", "opcion"],
))

T.append(dict(
slug="colocaciones", t="Colocaciones", cat="dinero", ic="📤",
bcrp="Colocaciones", alias="créditos otorgados préstamos cartera de créditos",
corto="Es el dinero que los bancos y otras entidades financieras han prestado a sus clientes.",
simple=[
r"En el lenguaje bancario, <strong>captar</strong> es recibir depósitos y <strong>colocar</strong> es prestar. Las colocaciones son el total de préstamos vigentes: a empresas, a personas, hipotecarios y de consumo.",
r"Que crezcan las colocaciones suele indicar que hay más actividad económica. Pero si crecen demasiado rápido y sin cuidado, puede subir la <a href='cartera-morosa.html'>morosidad</a> más adelante.",
],
ejemplo=[
r"Si un banco tiene S/ 50 000 millones en préstamos vigentes y S/ 1500 millones están atrasados, sus colocaciones totales son S/ 50 000 millones y su morosidad es 3 %.",
],
formula=dict(
tex=r"\text{Morosidad}=\frac{\text{Cartera atrasada}}{\text{Colocaciones totales}}\times 100",
calculo=[r"\frac{1500}{50\,000}\times 100=3\ \%"],
),
rel=["cartera-morosa", "intermediacion-financiera", "sistema-financiero", "creditos-de-consumo"],
))

T.append(dict(
slug="compania-de-seguros", t="Compañía de seguros", cat="finanzas", ic="🛡️",
bcrp="Compañía de seguros", alias="aseguradora prima siniestro póliza",
corto="Es una empresa que, a cambio de un pago llamado prima, se compromete a cubrir las pérdidas si ocurre un hecho incierto, como un accidente o una enfermedad.",
simple=[
r"La aseguradora junta las primas de muchas personas. Como no todas sufren un accidente al mismo tiempo, con ese fondo paga a quienes sí lo sufren. Es una forma de repartir el riesgo entre muchos.",
r"El documento que fija las condiciones es la <strong>póliza</strong>, y el hecho cubierto es el <strong>siniestro</strong>. En el Perú, las aseguradoras están supervisadas por la <a href='sbs.html'>SBS</a>.",
],
ejemplo=[
r"El SOAT es un seguro obligatorio: cada dueño de vehículo paga una prima y, si hay un accidente de tránsito, la aseguradora cubre los gastos médicos de las víctimas hasta el límite fijado.",
],
rel=["sbs", "sistema-financiero", "cobertura", "afp-y-onp"],
))

T.append(dict(
slug="condonacion-de-deuda", t="Condonación de deuda", cat="estado", ic="🕊️",
bcrp="Condonación de la deuda", alias="perdón de deuda alivio de deuda",
corto="Es cuando un acreedor perdona total o parcialmente una deuda, de modo que el deudor ya no tiene que pagarla.",
simple=[
r"Condonar significa perdonar. Entre países, suele ocurrir cuando un país muy pobre no puede pagar y sus acreedores, a menudo gobiernos u organismos internacionales, deciden aliviar su carga para que pueda invertir en salud o educación.",
r"Tiene un costo: el acreedor pierde ese dinero, y si se perdona con frecuencia puede incentivar que otros no paguen. Por eso suele venir con condiciones.",
],
ejemplo=[
r"A finales de los años noventa e inicios de los 2000, varios países muy endeudados de África y de América Latina recibieron alivio de deuda de organismos como el Banco Mundial y el FMI.",
],
rel=["deuda-externa", "club-de-paris", "banco-mundial", "organismos-multilaterales"],
))

T.append(dict(
slug="consumo-intermedio", t="Consumo intermedio", cat="produccion", ic="⚙️",
bcrp="Consumo intermedio", alias="insumos bienes intermedios",
corto="Son los bienes y servicios que las empresas usan y gastan para producir otros bienes, como la harina en una panadería.",
simple=[
r"Una panadería compra harina, gas, electricidad y bolsas. Todo eso se «consume» en el proceso de hacer pan: es <strong>consumo intermedio</strong>.",
r"No se cuenta directamente en el <a href='pbi.html'>PBI</a>, porque ya está incluido en el precio del producto final. Por eso el PBI se calcula con el <a href='valor-agregado.html'>valor agregado</a>: producción menos consumo intermedio.",
],
ejemplo=[
r"Si una fábrica de muebles vende S/ 100 000 y gastó S/ 60 000 en madera, pintura y electricidad, su consumo intermedio es S/ 60 000 y su valor agregado, S/ 40 000.",
],
formula=dict(
tex=r"VA=\text{Producción}-\text{Consumo intermedio}",
calculo=[r"100\,000-60\,000=40\,000\ \text{soles}"],
),
rel=["valor-agregado", "pbi", "cuentas-nacionales", "bienes-de-capital-y-de-consumo"],
))

T.append(dict(
slug="costo-de-vida", t="Costo de vida", cat="precios", ic="🏠",
bcrp="Costo de vida", alias="lo que cuesta vivir gastos básicos",
corto="Es cuánto dinero necesita una persona o familia para pagar sus gastos habituales: comida, vivienda, transporte, salud y otros.",
simple=[
r"Cuando se dice que «sube el costo de vida», se habla de que los precios de lo que compramos a diario aumentan. La medida oficial para seguirlo es el <a href='ipc.html'>IPC</a>, que refleja una <a href='canasta-de-consumo.html'>canasta de consumo</a> típica.",
r"El costo de vida también varía entre ciudades: vivir en un distrito céntrico de Lima no cuesta lo mismo que vivir en una ciudad pequeña, sobre todo por el alquiler.",
],
ejemplo=[
r"Si una familia gastaba S/ 3000 al mes y los precios suben 5 % en el año, para comprar lo mismo necesitará unos S/ 3150. Si sus ingresos no suben igual, pierde <a href='poder-adquisitivo.html'>poder adquisitivo</a>.",
],
rel=["ipc", "inflacion", "poder-adquisitivo", "canasta-de-consumo"],
herramienta=("Calcula cuánto valen hoy tus soles de otro año", "../inflacion/"),
))

T.append(dict(
slug="credito-refinanciado", t="Crédito refinanciado y reprogramado", cat="finanzas", ic="🔧",
bcrp="Crédito refinanciado", alias="refinanciación reprogramación reestructuración de deudas",
corto="Es un préstamo al que se le cambian las condiciones (plazo, cuota o tasa) porque el deudor tiene problemas para pagar.",
simple=[
r"Si no puedes pagar tus cuotas, el banco puede <strong>refinanciar</strong> tu deuda: alargar el plazo, bajar la cuota o juntar varias deudas en una. Eso te da aire, pero normalmente pagas más intereses en total.",
r"Para la SBS, un crédito refinanciado indica más riesgo y queda registrado así. Distinto es una <strong>reprogramación</strong> general, como las que se hicieron en la pandemia, que se aplicó a muchos clientes por una situación excepcional.",
],
ejemplo=[
r"Debes S/ 10 000 a 12 meses con cuotas de S/ 950 y pierdes tu trabajo. El banco te refinancia a 24 meses con cuotas de S/ 520. Pagas menos cada mes, pero más intereses en total.",
],
ojo=["Antes de aceptar una refinanciación, pide el nuevo cronograma y compara la TCEA y el total que pagarás."],
rel=["creditos-de-consumo", "central-de-riesgos", "cartera-morosa", "tcea"],
))

T.append(dict(
slug="capital-de-trabajo", t="Capital de trabajo", cat="mercados", ic="🔄",
bcrp="Crédito para capital de trabajo", alias="crédito de capital de trabajo activo corriente pasivo corriente",
corto="Es el dinero que un negocio necesita para operar día a día: comprar mercadería, pagar sueldos y servicios mientras cobra sus ventas.",
simple=[
r"Un negocio puede ser rentable y aun así quedarse sin efectivo: compra hoy, vende la próxima semana y cobra en un mes. Para cubrir ese tiempo necesita <strong>capital de trabajo</strong>.",
r"Contablemente se mide como lo que la empresa tiene a corto plazo (caja, cuentas por cobrar, inventario) menos lo que debe a corto plazo. Cuando falta, se pide un <strong>crédito de capital de trabajo</strong>, de plazo corto.",
],
ejemplo=[
r"Una bodega quiere llenar su almacén para diciembre. Pide un crédito de capital de trabajo de S/ 15 000 a 6 meses, compra la mercadería y lo devuelve con las ventas de fin de año.",
],
formula=dict(
tex=r"\text{Capital de trabajo}=\text{Activo corriente}-\text{Pasivo corriente}",
calculo=[r"40\,000-25\,000=15\,000\ \text{soles}"],
),
rel=["balance-general", "liquidez", "linea-de-credito", "riesgo-de-liquidez"],
))

T.append(dict(
slug="curso-legal", t="Curso legal", cat="dinero", ic="⚖️",
bcrp="Curso legal", alias="moneda de curso legal obligatoria aceptación",
corto="Es la característica de una moneda que, por ley, debe ser aceptada para pagar deudas dentro de un país.",
simple=[
r"En el Perú, la moneda de curso legal es el <strong>sol</strong>. Eso significa que nadie puede negarse a recibir soles en buen estado para cancelar una deuda en el país.",
r"El dólar circula mucho, pero no es de curso legal: se usa porque las partes lo acuerdan. Los billetes y monedas los emite solo el <a href='bcrp.html'>BCRP</a>.",
],
ejemplo=[
r"Si debes S/ 200 a una tienda, puedes pagar con billetes o monedas de soles y la tienda debe aceptarlos. En cambio, no está obligada a recibir dólares.",
],
rel=["dinero", "circulante", "bcrp", "dolarizacion"],
))

T.append(dict(
slug="deposito-de-ahorro", t="Depósito de ahorro", cat="finanzas", ic="🐷",
bcrp="Depósito de ahorro", alias="cuenta de ahorros libre disponibilidad",
corto="Es el dinero que guardas en una cuenta de ahorros: puedes sacarlo cuando quieras y te paga un interés, aunque suele ser bajo.",
simple=[
r"La cuenta de ahorros es el producto bancario más común. A diferencia del <a href='deposito-a-plazo.html'>depósito a plazo</a>, no tienes que dejar el dinero un tiempo fijo, pero a cambio la tasa de interés es menor.",
r"En el Perú, los depósitos de personas en entidades supervisadas por la SBS están protegidos por el Fondo de Seguro de Depósitos hasta un monto máximo, que se actualiza cada cierto tiempo.",
],
ejemplo=[
r"Si tienes S/ 2000 en una cuenta que paga 1 % anual (TREA), al año ganas unos S/ 20. Si la inflación es 2 %, en términos reales tu ahorro pierde poder de compra.",
],
ojo=["Mira la TREA, que ya incluye comisiones: es la tasa que de verdad recibirás."],
rel=["trea", "deposito-a-plazo", "ahorro-financiero", "tasa-de-interes-real"],
))

T.append(dict(
slug="deuda-interna", t="Deuda interna", cat="estado", ic="🏠",
bcrp="Deuda interna", alias="deuda doméstica deuda en soles",
corto="Es la deuda que el Estado tiene con acreedores del propio país, normalmente en moneda nacional.",
simple=[
r"El Estado puede financiarse vendiendo bonos a bancos, AFP y otros inversionistas locales. Esa es la <strong>deuda interna</strong>, distinta de la <a href='deuda-externa.html'>deuda externa</a>, que se tiene con acreedores del exterior.",
r"Tener más deuda en soles reduce el riesgo cambiario: si el dólar sube, la deuda en soles no se encarece. Por eso el Perú ha buscado financiarse cada vez más en su propia moneda.",
],
ejemplo=[
r"Cuando el MEF coloca <a href='bono-soberano.html'>bonos soberanos</a> en soles que compran las AFP peruanas, aumenta la deuda interna del Estado.",
],
rel=["deuda-publica", "deuda-externa", "bono-soberano", "descalce-de-monedas"],
))

T.append(dict(
slug="devengado", t="Gasto devengado", cat="estado", ic="✅",
bcrp="Devengado", alias="ejecución presupuestal compromiso girado",
corto="Es el momento en que el Estado reconoce que debe pagar algo porque ya recibió el bien o el servicio. Se usa para medir cuánto del presupuesto se ejecutó.",
simple=[
r"El gasto público pasa por etapas: primero se <strong>compromete</strong> (se firma el contrato), luego se <strong>devenga</strong> (se recibe la obra, el bien o el servicio y se reconoce la obligación de pagar) y al final se <strong>gira</strong> (se paga).",
r"Cuando las noticias dicen que una municipalidad «solo ejecutó 40 % de su presupuesto de inversión», normalmente se refieren al gasto devengado.",
],
ejemplo=[
r"Un gobierno regional tiene S/ 100 millones para obras. Si a fin de año ha devengado S/ 65 millones, su ejecución presupuestal es 65 %.",
],
formula=dict(
tex=r"\text{Ejecución}=\frac{\text{Devengado}}{\text{Presupuesto}}\times 100",
calculo=[r"\frac{65}{100}\times 100=65\ \%"],
),
rel=["presupuesto-publico", "inversion-publica", "politica-fiscal", "gobierno-general"],
))

T.append(dict(
slug="distribucion-del-ingreso", t="Distribución del ingreso", cat="bienestar", ic="🍰",
bcrp="Distribución del ingreso", alias="desigualdad reparto de la riqueza quintiles deciles",
corto="Es la forma en que el ingreso total de un país se reparte entre sus habitantes: si se concentra en pocos o se reparte de manera más pareja.",
simple=[
r"Dos países con el mismo <a href='pbi-per-capita.html'>PBI per cápita</a> pueden vivir de forma muy distinta si en uno el ingreso está muy concentrado. Para medirlo se divide la población en grupos (por ejemplo, quintiles o deciles) y se ve qué parte del ingreso recibe cada uno.",
r"El indicador más usado es el <a href='coeficiente-de-gini.html'>coeficiente de Gini</a>. Los impuestos progresivos y los programas sociales pueden mejorar la distribución.",
],
ejemplo=[
r"Con números de ejemplo: si el 20 % más rico recibe el 50 % del ingreso y el 20 % más pobre solo el 5 %, el grupo de arriba recibe 10 veces más que el de abajo.",
],
formula=dict(
tex=r"\text{Razón de quintiles}=\frac{\text{Ingreso del 20\,\% más rico}}{\text{Ingreso del 20\,\% más pobre}}",
calculo=[r"\frac{50}{5}=10"],
),
rel=["coeficiente-de-gini", "pobreza-monetaria", "indice-de-desarrollo-humano", "impuesto-directo-e-indirecto"],
))

T.append(dict(
slug="estabilidad-monetaria", t="Estabilidad monetaria", cat="dinero", ic="⚓",
bcrp="Estabilidad monetaria", alias="estabilidad de precios finalidad del BCRP",
corto="Es que el valor del dinero se mantenga estable en el tiempo, es decir, que la inflación sea baja y predecible. Es la finalidad del BCRP.",
simple=[
r"La Constitución dice que la finalidad del <a href='bcrp.html'>BCRP</a> es preservar la estabilidad monetaria. En la práctica, eso significa mantener la inflación baja, dentro de su <a href='meta-de-inflacion.html'>meta</a>.",
r"¿Por qué importa? Con precios estables, la gente puede ahorrar, planificar y endeudarse a largo plazo en soles. Cuando no hay estabilidad, como en la <a href='hiperinflacion.html'>hiperinflación</a> de fines de los ochenta, el ahorro se destruye y la economía se paraliza.",
],
ejemplo=[
r"Gracias a la estabilidad monetaria de las últimas décadas, hoy es común tomar un crédito hipotecario en soles a 20 años, algo impensable cuando la inflación era de miles por ciento.",
],
rel=["bcrp", "meta-de-inflacion", "inflacion", "politica-monetaria"],
))

T.append(dict(
slug="estados-financieros", t="Estados financieros", cat="mercados", ic="📑",
bcrp="Estados financieros", alias="balance estado de resultados flujo de efectivo",
corto="Son los informes que muestran la situación y los resultados de una empresa: qué tiene, qué debe, cuánto ganó y cómo se movió su dinero.",
simple=[
r"Los principales son tres. El <a href='balance-general.html'>balance general</a> (o estado de situación financiera) es una foto de activos, pasivos y patrimonio. El <strong>estado de resultados</strong> muestra ingresos, gastos y utilidad de un periodo. El <strong>estado de flujos de efectivo</strong> muestra de dónde entró y a dónde salió el dinero.",
r"Los usan los dueños, los bancos para decidir si prestan, la SUNAT para los impuestos y los inversionistas para valorar la empresa.",
],
ejemplo=[
r"Antes de darle un préstamo a una mype, la caja municipal le pide sus estados financieros para ver si gana dinero y si tendrá efectivo para pagar las cuotas.",
],
rel=["balance-general", "rentabilidad", "patrimonio", "capital-de-trabajo"],
))

T.append(dict(
slug="patrimonio", t="Patrimonio", cat="mercados", ic="🧱",
bcrp="Patrimonio", alias="patrimonio neto capital propio riqueza",
corto="Es lo que realmente te pertenece: el valor de todo lo que tienes menos todo lo que debes.",
simple=[
r"En una empresa, el patrimonio es el aporte de los dueños más las utilidades que han guardado. En una persona, es su riqueza neta: casa, ahorros y bienes, menos préstamos y deudas.",
r"Si las deudas superan a los bienes, el patrimonio es negativo, una señal de <a href='insolvencia.html'>insolvencia</a>.",
],
ejemplo=[
r"Tienes un departamento de S/ 250 000, ahorros por S/ 20 000 y un crédito hipotecario pendiente de S/ 150 000. Tu patrimonio es S/ 120 000.",
],
formula=dict(
tex=r"\text{Patrimonio}=\text{Activos}-\text{Pasivos}",
calculo=[r"270\,000-150\,000=120\,000\ \text{soles}"],
),
rel=["balance-general", "estados-financieros", "insolvencia", "apalancamiento"],
))

T.append(dict(
slug="expectativas-racionales", t="Expectativas racionales y adaptativas", cat="precios", ic="🧠",
bcrp="Expectativas racionales", alias="expectativas adaptativas formación de expectativas",
corto="Son dos formas de explicar cómo la gente prevé el futuro: mirando el pasado (adaptativas) o usando toda la información disponible (racionales).",
simple=[
r"Con <strong>expectativas adaptativas</strong>, la gente supone que el futuro se parecerá al pasado reciente: si la inflación fue 5 % el año pasado, espera 5 % este año, y corrige poco a poco cuando se equivoca.",
r"Con <strong>expectativas racionales</strong>, la gente usa toda la información disponible, incluidas las decisiones y anuncios del banco central. Por eso un banco central creíble puede bajar la inflación más rápido: si la gente le cree, ajusta precios y sueldos de inmediato.",
],
ejemplo=[
r"Si el BCRP anuncia que hará lo necesario para volver a su meta y tiene buena reputación, las empresas no suben tanto sus precios, porque esperan que la inflación baje.",
],
rel=["expectativas", "meta-de-inflacion", "politica-monetaria", "reporte-de-inflacion"],
))

T.append(dict(
slug="garantia", t="Garantía", cat="finanzas", ic="🔐",
bcrp="Garantía", alias="colateral aval fianza garantía mobiliaria",
corto="Es un bien o compromiso que respalda una deuda: si el deudor no paga, el acreedor puede cobrar con ella.",
simple=[
r"Las garantías bajan el riesgo para quien presta, y por eso suelen permitir tasas más bajas. Pueden ser <strong>reales</strong>, como una <a href='hipoteca.html'>hipoteca</a> sobre una casa o una garantía sobre un vehículo, o <strong>personales</strong>, como un aval o una fianza, en las que otra persona se compromete a pagar si tú no lo haces.",
r"Ser aval es serio: si el deudor no paga, el banco puede cobrarte a ti.",
],
ejemplo=[
r"Un préstamo vehicular suele tener como garantía el mismo auto. Si dejas de pagar, la entidad puede ejecutar la garantía y quedarse con el vehículo para cubrir la deuda.",
],
rel=["hipoteca", "riesgo-de-credito", "credito-hipotecario", "tasa-de-interes"],
))

T.append(dict(
slug="hipoteca", t="Hipoteca", cat="finanzas", ic="🏡",
bcrp="Hipoteca", alias="garantía hipotecaria inmueble en garantía",
corto="Es una garantía sobre una casa o terreno: el inmueble respalda una deuda y, si no se paga, el acreedor puede pedir su venta para cobrar.",
simple=[
r"Mucha gente usa «hipoteca» como sinónimo de crédito para vivienda, pero en realidad es la <strong>garantía</strong>. Con la hipoteca, sigues siendo dueño y vives en la casa, pero esta queda inscrita en Registros Públicos como respaldo de la deuda.",
r"Cuando terminas de pagar, debes pedir que se levante la hipoteca para que el inmueble quede libre de cargas.",
],
ejemplo=[
r"Compras un departamento con un <a href='credito-hipotecario.html'>crédito hipotecario</a>. El banco inscribe una hipoteca sobre él. Si dejas de pagar por mucho tiempo, puede iniciar un proceso para rematarlo y cobrar lo que se le debe.",
],
rel=["credito-hipotecario", "garantia", "tasa-fija-y-variable", "tcea"],
))

T.append(dict(
slug="fondo-de-estabilizacion-fiscal", t="Fondo de Estabilización Fiscal", cat="estado", ic="🛟",
bcrp="Fondo de estabilización fiscal", alias="FEF ahorro fiscal fondo anticíclico",
corto="Es un fondo en el que el Estado peruano ahorra en épocas de buenos ingresos para poder gastar cuando vienen tiempos difíciles.",
simple=[
r"Cuando los precios de los metales están altos, el Estado recauda más de lo normal. En lugar de gastarlo todo, una parte puede ir al <strong>Fondo de Estabilización Fiscal (FEF)</strong>.",
r"En una crisis, cuando caen los ingresos, el Estado puede usar ese ahorro para mantener el gasto sin endeudarse tanto. Es una herramienta de <a href='politica-anticiclica.html'>política anticíclica</a>.",
],
ejemplo=[
r"Funciona como el ahorro de emergencia de una familia: en los meses de buen sueldo se guarda una parte, y si un mes no hay ingresos, se usa sin tener que pedir prestado.",
],
rel=["politica-anticiclica", "politica-fiscal", "deficit-fiscal", "deuda-publica"],
))

T.append(dict(
slug="impuesto-de-promocion-municipal", t="Impuesto de Promoción Municipal (IPM)", cat="impuestos", ic="🏘️",
bcrp="Impuesto de Promoción Municipal – IPM", alias="IPM 2 % IGV 18 % Foncomun",
corto="Es un impuesto de 2 % que se cobra junto con el IGV. Por eso, en el precio pagas 18 %: 16 % de IGV y 2 % de IPM.",
simple=[
r"Cuando ves «IGV 18 %» en una boleta, en realidad son dos impuestos: el <a href='igv.html'>IGV</a> de 16 % y el <strong>Impuesto de Promoción Municipal</strong> de 2 %. Los dos los recauda la SUNAT al mismo tiempo.",
r"Lo recaudado por el IPM se destina al <a href='foncomun.html'>Fondo de Compensación Municipal (Foncomun)</a>, que se reparte entre las municipalidades del país.",
],
ejemplo=[
r"Si compras algo de S/ 100 sin impuestos, pagas S/ 16 de IGV y S/ 2 de IPM: S/ 118 en total.",
],
formula=dict(
tex=r"\text{Precio final}=\text{Valor de venta}\times(1+0.16+0.02)",
calculo=[r"100\times 1.18=118\ \text{soles}"],
),
rel=["igv", "foncomun", "tributo", "base-imponible"],
))

T.append(dict(
slug="foncomun", t="Foncomun", cat="estado", ic="🏛️",
bcrp="Fondo de Compensación Municipal – Foncomun", alias="Fondo de Compensación Municipal municipalidades transferencias",
corto="Es un fondo que reparte dinero entre las municipalidades del Perú, dando más a las más pobres y alejadas.",
simple=[
r"Se financia principalmente con el <a href='impuesto-de-promocion-municipal.html'>Impuesto de Promoción Municipal</a> (el 2 % que se cobra junto con el IGV). El dinero se reparte con criterios como población, pobreza y ruralidad.",
r"Para muchas municipalidades pequeñas, el Foncomun es una de sus principales fuentes de ingresos, porque recaudan muy poco por sí mismas.",
],
ejemplo=[
r"Una municipalidad rural de la sierra que casi no cobra impuestos prediales puede pagar parte de sus gastos y obras gracias a las transferencias del Foncomun.",
],
rel=["impuesto-de-promocion-municipal", "gobierno-general", "canon", "presupuesto-publico"],
))

T.append(dict(
slug="fuentes-de-crecimiento", t="Fuentes de crecimiento", cat="produccion", ic="🌱",
bcrp="Fuentes de crecimiento", alias="contabilidad del crecimiento productividad total de factores PTF",
corto="Es descomponer el crecimiento del PBI para ver cuánto se debe a más trabajadores, a más capital y a mayor productividad.",
simple=[
r"Un país puede crecer porque trabaja más gente, porque tiene más máquinas e infraestructura (capital) o porque usa todo eso de forma más eficiente (<a href='productividad.html'>productividad</a>). La <strong>contabilidad del crecimiento</strong> separa esas tres fuentes.",
r"Lo que no se explica por trabajo ni por capital se atribuye a la <strong>productividad total de factores (PTF)</strong>: mejor tecnología, organización o instituciones. Es la fuente de crecimiento más duradera.",
],
ejemplo=[
r"Con números de ejemplo: si el PBI crece 4 %, el capital aporta 1.5 puntos y el trabajo 1 punto, entonces la productividad aportó 1.5 puntos.",
],
formula=dict(
tex=r"g_Y=\alpha\,g_K+(1-\alpha)\,g_L+g_{PTF}",
donde=[(r"g_Y", "crecimiento del PBI"), (r"g_K,\ g_L", "crecimiento del capital y del trabajo"), (r"\alpha", "participación del capital"), (r"g_{PTF}", "crecimiento de la productividad")],
calculo=[r"4\ \%=1.5+1+g_{PTF}\ \Rightarrow\ g_{PTF}=1.5\ \text{puntos}"],
),
rel=["productividad", "crecimiento-economico", "crecimiento-potencial", "formacion-bruta-de-capital"],
))

T.append(dict(
slug="fusion-y-adquisicion", t="Fusiones y adquisiciones", cat="mercados", ic="🧩",
bcrp="Fusión y adquisición", alias="M&A compra de empresas absorción concentración",
corto="Una fusión es cuando dos empresas se unen en una sola. Una adquisición es cuando una empresa compra a otra.",
simple=[
r"Las empresas se fusionan o compran otras para crecer más rápido, entrar a nuevos mercados, bajar costos o quedarse con tecnología o marcas.",
r"Si la unión deja a una empresa con demasiado poder en un mercado, puede perjudicar a los consumidores con precios más altos. Por eso, en el Perú, ciertas fusiones grandes necesitan la autorización previa del Indecopi para proteger la <a href='libre-competencia.html'>libre competencia</a>.",
],
ejemplo=[
r"Si dos cadenas de farmacias se unen y juntas controlan la mayor parte del mercado de una ciudad, el regulador revisa si la operación podría subir los precios de los medicamentos.",
],
rel=["libre-competencia", "monopolio", "accion", "capitalizacion-bursatil"],
))

T.append(dict(
slug="gasto-corriente-y-de-capital", t="Gasto corriente y gasto de capital", cat="estado", ic="🧾",
bcrp="Gastos corrientes", alias="gasto público inversión pública sueldos bienes y servicios",
corto="El gasto corriente paga el funcionamiento del Estado, como sueldos y servicios. El gasto de capital crea obras y bienes duraderos, como carreteras o colegios.",
simple=[
r"El <strong>gasto corriente</strong> se repite cada año: sueldos de maestros y médicos, pensiones, materiales, luz, agua, intereses de la deuda. El <strong>gasto de capital</strong> aumenta el patrimonio del Estado: construir hospitales, comprar equipos o hacer carreteras.",
r"La Constitución no permite cubrir gastos permanentes con préstamos, y los economistas prefieren que, si el Estado se endeuda, sea para invertir en obras que aumenten la capacidad de crecer.",
],
ejemplo=[
r"Pagar el sueldo de los médicos de un hospital es gasto corriente. Construir un nuevo hospital es gasto de capital.",
],
rel=["inversion-publica", "presupuesto-publico", "politica-fiscal", "deficit-fiscal"],
))

T.append(dict(
slug="gobierno-general", t="Gobierno general", cat="estado", ic="🏛️",
bcrp="Gobierno general", alias="gobierno central regional local sector público",
corto="Es el conjunto de todas las entidades del Estado que prestan servicios públicos: gobierno nacional, gobiernos regionales y municipalidades.",
simple=[
r"En las estadísticas fiscales del Perú, el <strong>gobierno general</strong> incluye al <strong>gobierno central</strong> (ministerios y organismos nacionales), los <strong>gobiernos regionales</strong> y los <strong>gobiernos locales</strong> (municipalidades), además de entidades como EsSalud.",
r"Se distingue de las empresas públicas, como Petroperú, que venden bienes o servicios en el mercado. Si sumas ambos, obtienes el <strong>sector público no financiero</strong>.",
],
ejemplo=[
r"Cuando el MEF informa el <a href='deficit-fiscal.html'>déficit fiscal</a>, suele referirse al sector público no financiero, que incluye al gobierno general.",
],
rel=["presupuesto-publico", "deficit-fiscal", "foncomun", "canon"],
))

T.append(dict(
slug="impulso-fiscal", t="Impulso fiscal", cat="estado", ic="💪",
bcrp="Impulso fiscal", alias="estímulo fiscal posición fiscal",
corto="Mide si la política fiscal de un año está empujando la economía (gastando más o cobrando menos) o frenándola, comparada con el año anterior.",
simple=[
r"El déficit fiscal cambia por dos razones: por decisiones del gobierno y por el ciclo económico (en una recesión se recauda menos aunque nadie cambie nada). El <strong>impulso fiscal</strong> intenta medir solo la parte que viene de decisiones de política.",
r"Si es positivo, la política fiscal es expansiva: estimula la demanda. Si es negativo, es contractiva: la enfría.",
],
ejemplo=[
r"Con números de ejemplo: si el déficit estructural pasa de 1 % a 2 % del PBI, el impulso fiscal es de 1 punto del PBI: el gobierno está estimulando la economía.",
],
formula=dict(
tex=r"\text{Impulso fiscal}_t=\text{Déficit estructural}_t-\text{Déficit estructural}_{t-1}",
calculo=[r"2\ \%-1\ \%=1\ \text{punto del PBI}"],
),
rel=["politica-fiscal", "politica-anticiclica", "deficit-fiscal", "resultado-primario"],
))

T.append(dict(
slug="precios-al-por-mayor", t="Precios al por mayor", cat="precios", ic="📦",
bcrp="Precio al por mayor o precio mayorista", alias="índice de precios al por mayor IPM mayorista productor",
corto="Son los precios a los que se venden los productos en grandes cantidades entre empresas, antes de llegar al consumidor final.",
simple=[
r"Antes de llegar a la tienda, los productos pasan por fabricantes, importadores y distribuidores. El <strong>índice de precios al por mayor</strong> mide cómo cambian esos precios en las primeras etapas de la cadena.",
r"Suele adelantarse al <a href='ipc.html'>IPC</a>: si los insumos y productos al por mayor suben, es probable que esos aumentos lleguen después a los consumidores.",
],
ejemplo=[
r"Si sube mucho el precio del trigo importado y el de la harina al por mayor, es probable que unos meses después suba el precio del pan en las panaderías.",
],
rel=["ipc", "inflacion", "efecto-traspaso", "inflacion-importada"],
))

T.append(dict(
slug="inflacion-sin-alimentos-y-energia", t="Inflación sin alimentos y energía", cat="precios", ic="🔍",
bcrp="Inflación sin alimentos y energía", alias="inflación core tendencial BCRP",
corto="Es la inflación calculada sin los precios de alimentos y energía, que suben y bajan mucho por choques como el clima o el petróleo.",
simple=[
r"Los precios de los alimentos dependen mucho del clima y los de los combustibles, del petróleo mundial. Si el BCRP reaccionara a cada salto de esos precios, cambiaría sus tasas a cada rato. Por eso sigue de cerca la inflación <strong>sin alimentos y energía</strong>, que muestra mejor la tendencia.",
r"Es una forma de medir la <a href='inflacion-subyacente.html'>inflación subyacente</a>. Si esta se mantiene alta por varios meses, es señal de que la inflación se está extendiendo a muchos precios.",
],
ejemplo=[
r"Según Andina, en abril de 2026 la inflación sin alimentos y energía subió de 3.7 % a 4.4 % en doce meses, por encima del rango meta del BCRP.",
],
rel=["inflacion-subyacente", "inflacion", "meta-de-inflacion", "choques-de-oferta-y-demanda"],
))

T.append(dict(
slug="inflacion-importada", t="Inflación importada", cat="precios", ic="🚢",
bcrp="IPC importado", alias="IPC importado precios importados",
corto="Es la parte de la inflación que viene de productos importados o de precios internacionales, como el petróleo, el trigo o el maíz.",
simple=[
r"El Perú importa combustibles, trigo, maíz amarillo, aceites y muchos productos. Si esos productos suben en el mundo o si el dólar sube, los precios en el Perú también suben. Esa es la <strong>inflación importada</strong>.",
r"El BCRP no puede controlar los precios internacionales, pero vigila que esas subidas no se contagien a otros precios (el <a href='efecto-traspaso.html'>efecto traspaso</a>).",
],
ejemplo=[
r"En 2022, la subida mundial del petróleo y del trigo tras la guerra en Ucrania encareció los combustibles y el pan en el Perú, aunque la causa no estuviera en la economía peruana.",
],
rel=["efecto-traspaso", "tipo-de-cambio", "inflacion", "terminos-de-intercambio"],
))

T.append(dict(
slug="ingresos-tributarios", t="Ingresos tributarios y no tributarios", cat="impuestos", ic="💰",
bcrp="Ingresos tributarios", alias="recaudación ingresos del Estado regalías",
corto="Los ingresos tributarios vienen de impuestos. Los no tributarios vienen de otras fuentes, como regalías, tasas o utilidades de empresas públicas.",
simple=[
r"Los <strong>ingresos tributarios</strong> son lo que el Estado recauda por impuestos: <a href='impuesto-a-la-renta.html'>impuesto a la renta</a>, <a href='igv.html'>IGV</a>, impuesto selectivo, aranceles y otros. Son la principal fuente de dinero del Estado.",
r"Los <strong>no tributarios</strong> incluyen <a href='regalias.html'>regalías</a> mineras y petroleras, pagos por concesiones, multas, rentas de propiedades y utilidades de empresas estatales.",
],
ejemplo=[
r"En el Perú, el impuesto a la renta y el IGV juntos representan la mayor parte de los ingresos tributarios del gobierno central.",
],
rel=["presion-tributaria", "tributo", "regalias", "presupuesto-publico"],
))

T.append(dict(
slug="integracion-economica", t="Integración económica", cat="comercio", ic="🧷",
bcrp="Integración económica", alias="etapas de integración mercado común unión aduanera",
corto="Es el proceso por el que varios países eliminan barreras entre sus economías, desde bajar aranceles hasta compartir moneda.",
simple=[
r"Se suelen distinguir etapas. En una <a href='zona-de-libre-comercio.html'>zona de libre comercio</a> se eliminan los aranceles entre los miembros. En una <strong>unión aduanera</strong>, además, se pone un arancel común frente al resto del mundo. En un <strong>mercado común</strong> también circulan libremente trabajadores y capitales. En una <a href='union-monetaria.html'>unión monetaria</a> se comparte la moneda.",
r"Mientras más profunda es la integración, más beneficios comerciales hay, pero cada país cede más decisiones propias.",
],
ejemplo=[
r"La <a href='comunidad-andina.html'>Comunidad Andina</a> tiene libre comercio entre sus miembros; la Unión Europea llegó mucho más lejos, hasta tener una moneda común en la zona euro.",
],
rel=["zona-de-libre-comercio", "comunidad-andina", "union-monetaria", "euro"],
))

T.append(dict(
slug="inversion-publica", t="Inversión pública", cat="estado", ic="🏗️",
bcrp="Inversión pública", alias="obras públicas gasto de capital Invierte.pe",
corto="Es el gasto del Estado en obras y bienes duraderos, como carreteras, hospitales, colegios o sistemas de agua.",
simple=[
r"La inversión pública aumenta la capacidad de un país para producir y mejora la calidad de vida. A diferencia del gasto corriente, deja algo que dura muchos años.",
r"En el Perú, los proyectos pasan por un sistema de programación y evaluación (Invierte.pe) y los ejecutan el gobierno nacional, los gobiernos regionales y las municipalidades. Un problema frecuente es la baja ejecución: se asigna presupuesto, pero las obras se retrasan o se paralizan.",
],
ejemplo=[
r"Una carretera nueva que une una zona agrícola con un puerto baja los costos de transporte y permite que los productores vendan más y a mejor precio.",
],
rel=["gasto-corriente-y-de-capital", "inversion", "devengado", "asociaciones-publico-privadas"],
))

T.append(dict(
slug="libre-competencia", t="Libre competencia", cat="mercados", ic="🏁",
bcrp="Libre competencia", alias="competencia Indecopi cárteles concertación",
corto="Es la situación en la que muchas empresas compiten por los clientes, lo que empuja a bajar precios y mejorar la calidad.",
simple=[
r"Cuando las empresas compiten, tienen que ofrecer mejores productos y precios para no perder clientes. Si en cambio se ponen de acuerdo para fijar precios o repartirse el mercado (un <strong>cártel</strong>), los consumidores pagan de más.",
r"En el Perú, el Indecopi vigila la libre competencia: investiga y sanciona acuerdos entre competidores y abusos de posición dominante, como los de un <a href='monopolio.html'>monopolio</a>.",
],
ejemplo=[
r"El Indecopi ha sancionado a empresas que se pusieron de acuerdo para fijar precios, como en el caso de un cártel del pavo en 2022.",
],
rel=["monopolio", "oferta-y-demanda", "fusion-y-adquisicion", "punto-de-equilibrio"],
))

T.append(dict(
slug="materias-primas", t="Materias primas (commodities)", cat="comercio", ic="🪨",
bcrp="Materias primas", alias="commodities productos básicos metales petróleo",
corto="Son productos básicos, casi iguales sin importar quién los produce, como el cobre, el oro, el petróleo o el trigo. Sus precios se fijan en mercados internacionales.",
simple=[
r"Un kilo de cobre es casi igual si viene del Perú, de Chile o del Congo. Por eso su precio no lo decide cada productor, sino la oferta y la demanda mundial, en bolsas como la de Londres o Nueva York.",
r"El Perú exporta sobre todo materias primas (minerales, harina de pescado, algunos agroproductos), por lo que su economía depende mucho de sus precios. Cuando suben, mejoran los <a href='terminos-de-intercambio.html'>términos de intercambio</a>; cuando caen, el país recibe menos dólares.",
],
ejemplo=[
r"Si el precio del cobre sube 20 %, las mineras peruanas ganan más, pagan más impuesto a la renta y crece el <a href='canon.html'>canon</a> que reciben las regiones productoras.",
],
rel=["terminos-de-intercambio", "exportaciones-tradicionales-y-no-tradicionales", "canon", "ciclo-economico"],
herramienta=("Mira los precios del cobre, el oro y otros productos", "../precios/"),
))

T.append(dict(
slug="organismos-multilaterales", t="Organismos multilaterales", cat="comercio", ic="🌐",
bcrp="Organismos multilaterales", alias="FMI Banco Mundial BID CAF instituciones internacionales",
corto="Son instituciones formadas por muchos países para cooperar en temas económicos, como el FMI, el Banco Mundial, el BID o la CAF.",
simple=[
r"Estos organismos prestan dinero, dan asistencia técnica y publican estudios. El FMI apoya la estabilidad financiera; el <a href='banco-mundial.html'>Banco Mundial</a> y el BID financian proyectos de desarrollo; la CAF es un banco de desarrollo de América Latina.",
r"Como tienen buena calificación, prestan a tasas más bajas que el mercado. A cambio, suelen pedir condiciones o estudios técnicos de los proyectos.",
],
ejemplo=[
r"Un gobierno puede financiar un programa de agua potable rural con un préstamo del BID a largo plazo, a una tasa más baja que la de un banco privado.",
],
rel=["banco-mundial", "deuda-externa", "club-de-paris", "condonacion-de-deuda"],
))

T.append(dict(
slug="pbi-nominal-y-real", t="PBI nominal, PBI real y deflactor", cat="produccion", ic="🔢",
bcrp="PBI nominal", alias="PBI a precios corrientes constantes deflactor del PBI",
corto="El PBI nominal usa los precios de cada año; el PBI real usa precios de un año base para medir solo cuánto más se produjo. El deflactor relaciona ambos.",
simple=[
r"Si un año se produce lo mismo pero los precios suben 5 %, el <strong>PBI nominal</strong> sube 5 %, aunque el país no produjo más. Para saber si la economía creció de verdad, se usa el <strong>PBI real</strong>, a precios constantes.",
r"El <strong>deflactor del PBI</strong> es un índice de precios de todo lo que se produce en el país: sale de dividir el PBI nominal entre el real.",
],
ejemplo=[
r"Con números de ejemplo: si el PBI nominal es S/ 1 100 000 millones y el real (a precios del año base) es S/ 1 000 000 millones, el deflactor es 110: los precios están 10 % por encima del año base.",
],
formula=dict(
tex=r"\text{Deflactor}=\frac{PBI_{\text{nominal}}}{PBI_{\text{real}}}\times 100",
calculo=[r"\frac{1\,100\,000}{1\,000\,000}\times 100=110"],
),
rel=["pbi", "valor-nominal-y-real", "crecimiento-economico", "inflacion"],
))

T.append(dict(
slug="prepago", t="Prepago", cat="finanzas", ic="⏩",
bcrp="Prepago", alias="pago anticipado adelanto de cuotas amortizar antes",
corto="Es pagar todo o parte de un préstamo antes de lo previsto, para ahorrar intereses.",
simple=[
r"Al prepagar, reduces el capital que debes y, con ello, los intereses futuros. Puedes elegir entre <strong>reducir el monto de la cuota</strong> o <strong>reducir el número de cuotas</strong> (el plazo).",
r"En el Perú, el Código de Protección y Defensa del Consumidor te da derecho a pagar por adelantado, total o parcialmente, sin penalidades ni comisiones.",
],
ejemplo=[
r"Si debes S/ 8000 a 2 % mensual y prepagas S/ 2000, dejas de pagar intereses sobre esos S/ 2000: unos S/ 40 menos de intereses solo en el mes siguiente.",
],
ojo=["Si puedes, elige reducir el plazo: normalmente ahorras más intereses que si solo bajas la cuota."],
rel=["amortizacion", "tcea", "creditos-de-consumo", "credito-hipotecario"],
))

T.append(dict(
slug="puntos-porcentuales", t="Puntos porcentuales", cat="precios", ic="📐",
bcrp="Puntos porcentuales", alias="pp diferencia de porcentajes",
corto="Es la diferencia simple entre dos porcentajes. Si la tasa pasa de 4 % a 5 %, sube 1 punto porcentual, pero 25 % en términos relativos.",
simple=[
r"Es fácil confundirse. Si el desempleo pasa de 4 % a 5 %, sube <strong>1 punto porcentual</strong> (la resta), pero en términos relativos sube <strong>25 %</strong> (porque 1 es la cuarta parte de 4).",
r"Los economistas usan «puntos porcentuales» para evitar ese malentendido. Para cambios muy pequeños, en finanzas se usan los <a href='puntos-basicos.html'>puntos básicos</a>: 1 punto porcentual = 100 puntos básicos.",
],
ejemplo=[
r"Si el BCRP sube su tasa de 4.25 % a 4.50 %, la sube 0.25 puntos porcentuales, que son 25 puntos básicos.",
],
formula=dict(
tex=r"\Delta_{\text{pp}}=p_1-p_0\qquad \Delta_{\%}=\frac{p_1-p_0}{p_0}\times 100",
calculo=[r"5-4=1\ \text{pp}\qquad \frac{5-4}{4}\times 100=25\ \%"],
),
rel=["puntos-basicos", "tasa-de-referencia", "tasa-de-desempleo", "inflacion"],
))

T.append(dict(
slug="regalias", t="Regalías", cat="estado", ic="⛏️",
bcrp="Regalías", alias="regalía minera pago por explotar recursos naturales",
corto="Son pagos que hacen las empresas al Estado por explotar recursos naturales que pertenecen a la Nación, como los minerales o el petróleo.",
simple=[
r"La Constitución dice que los recursos naturales son patrimonio de la Nación. Por eso, quien los extrae paga una compensación: las <strong>regalías</strong>. Son distintas de los impuestos, porque se pagan por usar un recurso que no es renovable.",
r"En el Perú, las mineras pagan una regalía minera calculada según su utilidad operativa, y las petroleras y gasíferas pagan regalías según sus contratos. Una parte va a las regiones donde se extraen esos recursos.",
],
ejemplo=[
r"El dinero de las regalías del gas de Camisea es una fuente importante de ingresos para Cusco, la región donde se encuentra el yacimiento.",
],
rel=["canon", "ingresos-tributarios", "materias-primas", "gobierno-general"],
))

T.append(dict(
slug="sistema-de-pagos", t="Sistema de pagos", cat="dinero", ic="📲",
bcrp="Sistema de pago", alias="pagos digitales transferencias interbancarias billeteras interoperabilidad",
corto="Es el conjunto de reglas, entidades y tecnologías que permiten mover dinero de una persona o empresa a otra: transferencias, tarjetas, billeteras digitales.",
simple=[
r"Cada vez que pagas con tarjeta, haces una transferencia o usas una billetera digital, intervienen bancos, cámaras de compensación y el banco central, que liquida los pagos grandes entre bancos.",
r"El <a href='bcrp.html'>BCRP</a> regula y vigila los sistemas de pagos del Perú para que sean seguros y eficientes. También impulsó la <strong>interoperabilidad</strong>, para que billeteras digitales de distintas entidades puedan enviarse dinero entre sí.",
],
ejemplo=[
r"Cuando envías dinero desde tu billetera digital a alguien que usa otra billetera de otro banco, la operación funciona gracias a las reglas de interoperabilidad del sistema de pagos.",
],
rel=["bcrp", "bancarizacion", "dinero", "circulante"],
))

T.append(dict(
slug="tasa-de-dependencia", t="Tasa de dependencia", cat="trabajo", ic="👨‍👩‍👧",
bcrp="Tasa de dependencia económica", alias="razón de dependencia demográfica bono demográfico",
corto="Compara cuántas personas en edades dependientes (niños y adultos mayores) hay por cada 100 personas en edad de trabajar.",
simple=[
r"Los niños y los adultos mayores suelen depender de lo que producen las personas en edad de trabajar. La <strong>tasa de dependencia</strong> mide esa carga.",
r"Cuando baja (hay muchos jóvenes adultos y pocos dependientes), el país vive un <strong>bono demográfico</strong>: una oportunidad para ahorrar e invertir. Cuando la población envejece, la tasa sube y se presionan las pensiones y la salud.",
],
ejemplo=[
r"Con números de ejemplo: si en un país hay 25 millones de personas de 15 a 64 años, 8 millones de menores de 15 y 3 millones de 65 años a más, la tasa de dependencia es 44: hay 44 dependientes por cada 100 personas en edad de trabajar.",
],
formula=dict(
tex=r"TD=\frac{P_{0\text{-}14}+P_{65+}}{P_{15\text{-}64}}\times 100",
calculo=[r"\frac{8+3}{25}\times 100=44"],
),
rel=["pea", "tasa-de-actividad", "afp-y-onp", "pbi-per-capita"],
))

T.append(dict(
slug="tasa-de-descuento", t="Tasa de descuento", cat="finanzas", ic="➗",
bcrp="Tasa de descuento", alias="costo de oportunidad del capital tasa de actualización redescuento",
corto="Es la tasa que se usa para traer al presente el valor de dinero futuro. Mientras más alta, menos vale hoy un sol que llegará mañana.",
simple=[
r"Un sol hoy vale más que un sol dentro de un año, porque puedes invertirlo. Para comparar montos de distintas fechas, se descuentan con una tasa: la <strong>tasa de descuento</strong>. Es la base del <a href='valor-presente-y-valor-futuro.html'>valor presente</a> y del <a href='van.html'>VAN</a>.",
r"En los bancos centrales, la palabra también se usa para la tasa que cobran a los bancos por prestarles dinero de corto plazo.",
],
ejemplo=[
r"Si te prometen S/ 1100 dentro de un año y tu tasa de descuento es 10 %, ese pago vale hoy S/ 1000.",
],
formula=dict(
tex=r"VP=\frac{VF}{(1+r)^n}",
donde=[(r"VP", "valor presente"), (r"VF", "valor futuro"), (r"r", "tasa de descuento"), (r"n", "número de periodos")],
calculo=[r"\frac{1100}{1.10}=1000\ \text{soles}"],
),
rel=["valor-presente-y-valor-futuro", "van", "tir", "costo-de-oportunidad"],
))

T.append(dict(
slug="tasa-libor-y-sofr", t="Tasa LIBOR y SOFR", cat="dinero", ic="🌍",
bcrp="Tasa LIBOR a tres meses", alias="LIBOR SOFR tasa de referencia internacional",
corto="La LIBOR fue durante décadas la principal tasa de referencia internacional para préstamos en dólares. Desde 2023 fue reemplazada sobre todo por la SOFR.",
simple=[
r"La <strong>LIBOR</strong> era el promedio de las tasas a las que grandes bancos de Londres decían que se prestarían entre ellos. Muchos créditos a tasa variable en el mundo, incluso en el Perú, se fijaban como «LIBOR más un margen».",
r"Tras escándalos de manipulación, se decidió dejar de usarla. Para el dólar, su reemplazo principal es la <strong>SOFR</strong>, que se basa en operaciones reales de préstamos garantizados con bonos del Tesoro de EE. UU. Los contratos en dólares que usaban LIBOR pasaron a usar SOFR u otras referencias.",
],
ejemplo=[
r"Un crédito corporativo en dólares que antes cobraba «LIBOR + 3 %» ahora suele cobrar «SOFR + un margen ajustado».",
],
rel=["tasa-de-fondos-federales", "tasa-fija-y-variable", "swaps", "prima-de-riesgo"],
))

T.append(dict(
slug="tasa-de-fondos-federales", t="Tasa de fondos federales (Fed)", cat="dinero", ic="🇺🇸",
bcrp="Tasa de fondos federales", alias="tasa de la Fed Reserva Federal fed funds",
corto="Es la tasa de interés de referencia de la Reserva Federal de Estados Unidos (la Fed). Sus cambios afectan a casi todas las economías del mundo.",
simple=[
r"Es la tasa a la que los bancos de EE. UU. se prestan dinero de un día para otro, y la Fed fija un rango objetivo para ella. Funciona como la <a href='tasa-de-referencia.html'>tasa de referencia</a> del BCRP, pero para el dólar.",
r"Como el dólar es la moneda más usada del mundo, cuando la Fed sube su tasa, los inversionistas prefieren activos en dólares y suelen salir de las <a href='economias-emergentes.html'>economías emergentes</a>. Eso tiende a depreciar monedas como el sol y a encarecer la deuda en dólares.",
],
ejemplo=[
r"Cuando la Fed subió con fuerza sus tasas en 2022 para frenar la inflación en EE. UU., muchas monedas de países emergentes se debilitaron y sus bancos centrales también tuvieron que subir tasas.",
],
rel=["tasa-de-referencia", "economias-emergentes", "tipo-de-cambio", "tasa-libor-y-sofr"],
))
