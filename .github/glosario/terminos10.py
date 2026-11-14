# -*- coding: utf-8 -*-
# Términos del glosario (parte 10): octava tanda. Finanzas personales,
# contabilidad básica, estadística y econometría, y algunos términos del
# Glosario del BCRP (campo "bcrp"). Todo está redactado con palabras propias.

T = []

# --- Finanzas personales ---------------------------------------------------

T.append(dict(
slug="presupuesto-personal", t="Presupuesto personal", cat="finanzas", ic="📒",
alias="presupuesto familiar regla 50 30 20 control de gastos",
corto="Es el plan de cuánto vas a ganar, gastar y ahorrar en un mes, para que el dinero alcance y te sobre algo.",
simple=[
r"Se anotan todos los ingresos del mes y luego los gastos, separados en <strong>necesidades</strong> (alquiler, comida, pasajes), <strong>gustos</strong> (salidas, suscripciones) y <strong>ahorro</strong>.",
r"Una guía muy usada es la regla <strong>50-30-20</strong>: 50 % para necesidades, 30 % para gustos y 20 % para ahorro o pagar deudas. No es una ley, solo un punto de partida que cada uno adapta.",
],
formula=dict(
tex=r"\text{Ahorro}=\text{Ingresos}-\text{Gastos}",
calculo=[r"2000\times20\,\%=400\ \text{soles al mes}"],
),
ejemplo=[
r"Con un ingreso de S/ 2000, la regla 50-30-20 sugiere S/ 1000 para necesidades, S/ 600 para gustos y S/ 400 para ahorrar.",
],
rel=["fondo-de-emergencia", "ahorro", "sobreendeudamiento", "costo-de-vida"],
))

T.append(dict(
slug="fondo-de-emergencia", t="Fondo de emergencia", cat="finanzas", ic="🛟",
alias="fondo de emergencia colchón financiero ahorro para imprevistos",
corto="Es un ahorro guardado solo para imprevistos, como perder el trabajo o una enfermedad, para no tener que endeudarte.",
simple=[
r"Se suele recomendar juntar el equivalente a <strong>3 a 6 meses</strong> de tus gastos básicos. Debe estar en un lugar seguro y fácil de retirar, como una cuenta de ahorros, no en inversiones que puedan caer.",
r"Tenerlo evita recurrir a préstamos caros o a la tarjeta de crédito cuando algo sale mal.",
],
formula=dict(
tex=r"\text{Fondo meta}=\text{Gastos básicos mensuales}\times\text{Meses}",
calculo=[r"1200\times4=4800\ \text{soles}"],
),
ejemplo=[
r"Si tus gastos básicos son S/ 1200 al mes y quieres cubrir 4 meses, tu meta es S/ 4800.",
],
rel=["presupuesto-personal", "deposito-de-ahorro", "liquidez", "prestamos-gota-a-gota"],
))

T.append(dict(
slug="regla-del-72", t="Regla del 72", cat="finanzas", ic="⏳",
alias="regla del 72 duplicar dinero interés compuesto tiempo",
corto="Es un truco para calcular rápido en cuántos años se duplica tu dinero: divides 72 entre la tasa de interés anual.",
simple=[
r"Con <a href='interes-compuesto.html'>interés compuesto</a>, el dinero crece sobre lo ya ganado. La <strong>regla del 72</strong> da una aproximación muy buena del tiempo que tarda en duplicarse.",
r"También sirve al revés: con 6 % de <a href='inflacion.html'>inflación</a> anual, los precios se duplican en unos 12 años.",
],
formula=dict(
tex=r"\text{Años para duplicar}\approx\frac{72}{\text{Tasa anual en \%}}",
calculo=[r"\frac{72}{8}=9\ \text{años}"],
),
ejemplo=[
r"Si un depósito paga 8 % anual, tu dinero se duplicaría en unos 9 años. El cálculo exacto da 9.01 años.",
],
rel=["interes-compuesto", "tea", "inflacion", "valor-presente-y-valor-futuro"],
))

T.append(dict(
slug="itf", t="ITF (impuesto a las transacciones financieras)", cat="impuestos", ic="🔖",
alias="ITF impuesto a las transacciones financieras bancarización 0.005",
corto="Es un pequeño impuesto que se cobra en el Perú por muchos movimientos de dinero en los bancos, como depósitos y retiros.",
simple=[
r"La tasa del ITF es de <strong>0.005 %</strong>: por cada S/ 1000 que se mueven, se cobran 5 céntimos. Lo retiene el propio banco.",
r"Además de recaudar, ayuda a la SUNAT a ver los movimientos financieros. Algunas operaciones están exoneradas, como las transferencias entre cuentas del mismo titular en una misma entidad y ciertos abonos en cuentas de sueldo, pensión o CTS.",
],
formula=dict(
tex=r"\text{ITF}=\text{Monto}\times0.005\,\%",
calculo=[r"10\,000\times0.00005=0.50\ \text{soles}"],
),
ejemplo=[
r"Si depositas S/ 10 000 en una cuenta, el ITF es de S/ 0.50.",
],
rel=["bancarizacion", "tributo", "impuesto-directo-e-indirecto", "evasion-y-elusion-tributaria"],
))

T.append(dict(
slug="fondo-de-seguro-de-depositos", t="Fondo de Seguro de Depósitos", cat="finanzas", ic="🛡️",
alias="FSD seguro de depósitos protección del ahorro cobertura",
corto="Es el fondo que devuelve a los ahorristas su dinero, hasta un tope, si quiebra el banco, la caja o la financiera donde lo tenían.",
simple=[
r"Las entidades miembros aportan al <strong>Fondo de Seguro de Depósitos</strong>. Si una de ellas quiebra, el fondo paga a cada persona sus depósitos hasta un monto máximo de cobertura, que se actualiza cada tres meses.",
r"Cubre principalmente depósitos de personas naturales y pequeñas empresas, como cuentas de ahorro, a plazo y la CTS. Por eso conviene ahorrar en entidades supervisadas y que sean miembros del fondo.",
],
ejemplo=[
r"Si una caja quiebra y tenías ahorros por debajo del tope de cobertura, el fondo te devuelve todo; si tenías más, recuperas hasta el tope.",
],
ojo=["Antes de ahorrar en una entidad nueva, revisa en la web del Fondo de Seguro de Depósitos si es miembro y cuál es la cobertura vigente."],
rel=["quiebra-bancaria", "sbs", "deposito-de-ahorro", "cajas-municipales"],
))

T.append(dict(
slug="seguro-de-desgravamen", t="Seguro de desgravamen", cat="finanzas", ic="📃",
alias="seguro de desgravamen préstamo hipotecario fallecimiento invalidez",
corto="Es un seguro que paga la deuda pendiente de un préstamo si el deudor fallece o queda inválido, para que su familia no herede la deuda.",
simple=[
r"Los bancos suelen exigirlo en préstamos hipotecarios, vehiculares y personales. Se paga como parte de la cuota o como un cargo aparte.",
r"Su costo cambia mucho entre entidades. Por eso conviene comparar la <a href='tcea.html'>TCEA</a>, que ya incluye los seguros obligatorios, y preguntar si puedes presentar un seguro propio.",
],
ejemplo=[
r"Si una persona con un crédito hipotecario fallece, el seguro de desgravamen cancela el saldo pendiente y la vivienda queda libre de deuda para su familia.",
],
rel=["credito-hipotecario", "tcea", "compania-de-seguros", "creditos-de-consumo"],
))

T.append(dict(
slug="pago-minimo", t="Pago mínimo de la tarjeta", cat="finanzas", ic="⚠️",
alias="pago mínimo pago total tarjeta de crédito revolvente",
corto="Es el monto más pequeño que puedes pagar de tu tarjeta de crédito para no caer en mora, pero el resto de la deuda sigue generando intereses.",
simple=[
r"Si debes S/ 2000 y solo pagas el mínimo, el saldo que queda sigue cobrando la tasa de interés de la tarjeta, que suele ser alta. La deuda baja muy lento.",
r"Para no pagar intereses en compras normales, lo ideal es pagar el <strong>total del mes</strong> antes de la fecha límite.",
],
ejemplo=[
r"Con una deuda de S/ 2000 y una tasa anual alta, pagar solo el mínimo cada mes puede hacer que tardes años en terminar de pagar y que los intereses sumen más de lo que compraste.",
],
ojo=["Pagar solo el mínimo es la forma más cara de usar una tarjeta: úsalo solo en emergencias."],
rel=["tarjetas-de-credito-y-debito", "tea", "sobreendeudamiento", "interes-compuesto"],
))

T.append(dict(
slug="billetera-digital", t="Billetera digital", cat="finanzas", ic="📲",
alias="billetera digital Yape Plin pagos con el celular dinero electrónico",
corto="Es una aplicación del celular que permite enviar, recibir y pagar dinero al instante, solo con un número de celular o un código QR.",
simple=[
r"En el Perú, las billeteras digitales más conocidas son Yape y Plin. Permiten pagar en bodegas, mercados y negocios pequeños sin efectivo, y han ayudado a la <a href='bancarizacion.html'>bancarización</a>.",
r"El BCRP regula y vigila estos pagos como parte del <a href='sistema-de-pagos.html'>sistema de pagos</a>, y ha impulsado que distintas billeteras puedan enviarse dinero entre sí.",
],
ejemplo=[
r"Un vendedor de un mercado puede cobrar con un código QR impreso y recibir el pago en su cuenta al instante, sin manejar vuelto.",
],
ojo=["Nunca compartas el código de verificación que te llega por SMS, aunque te digan que es para «devolverte» un pago."],
rel=["sistema-de-pagos", "bancarizacion", "banca-electronica", "dinero"],
))

T.append(dict(
slug="prestamos-gota-a-gota", t="Préstamos «gota a gota»", cat="finanzas", ic="🚨",
alias="gota a gota préstamo informal usura extorsión prestamista informal",
corto="Son préstamos informales que se pagan en cuotas diarias, con intereses altísimos y cobros con amenazas; son ilegales y peligrosos.",
simple=[
r"Los prestamistas «gota a gota» dan dinero rápido y sin requisitos, pero cobran cuotas diarias que, llevadas a una tasa anual, pueden superar varias veces lo que cobra un banco. Por eso se relacionan con la <a href='usura.html'>usura</a>.",
r"Si alguien se atrasa, suelen recurrir a amenazas y extorsión. Las alternativas formales, como cajas municipales, cooperativas supervisadas o microcréditos, son más seguras.",
],
ejemplo=[
r"Te prestan S/ 1000 y debes pagar S/ 50 diarios durante 24 días: al final pagas S/ 1200 en menos de un mes, un 20 % de interés mensual.",
],
ojo=["Si te amenazan por una deuda, denúncialo a la Policía. Antes de pedir un préstamo, verifica en la web de la SBS que la entidad esté autorizada."],
rel=["usura", "sobreendeudamiento", "cajas-municipales", "sbs"],
))

T.append(dict(
slug="esquema-ponzi", t="Esquema Ponzi o piramidal", cat="finanzas", ic="🔺",
alias="esquema Ponzi pirámide estafa financiera captación ilegal rentabilidad garantizada",
corto="Es una estafa que promete ganancias altas y seguras, pero paga a los primeros inversionistas con el dinero de los nuevos, hasta que colapsa.",
simple=[
r"No hay un negocio real detrás: el dinero de los que entran después se usa para pagar a los que entraron antes. Mientras entre gente nueva, parece funcionar.",
r"Cuando dejan de llegar nuevos inversionistas, el esquema se cae y la mayoría pierde su dinero. Captar ahorros del público sin autorización de la <a href='sbs.html'>SBS</a> es ilegal en el Perú.",
],
ejemplo=[
r"Una «inversión» que promete 10 % mensual garantizado y te pide traer amigos para ganar más tiene todas las señales de un esquema piramidal.",
],
ojo=["Desconfía de rentabilidades altas «garantizadas»: en finanzas, más ganancia siempre significa más riesgo."],
rel=["rentabilidad", "sbs", "criptomonedas", "riesgo-de-mercado"],
))

T.append(dict(
slug="criptomonedas", t="Criptomonedas", cat="dinero", ic="🪙",
alias="criptomoneda bitcoin blockchain cripto activos virtuales",
corto="Son monedas digitales que funcionan con una red de computadoras (blockchain) sin un banco central; su precio puede subir y bajar muchísimo.",
simple=[
r"La más conocida es el bitcoin. Sus registros se guardan en una <strong>cadena de bloques</strong> (blockchain) compartida, lo que permite enviar valor sin intermediarios.",
r"En el Perú no son <a href='curso-legal.html'>moneda de curso legal</a>: nadie está obligado a aceptarlas. Su <a href='volatilidad.html'>volatilidad</a> es muy alta, y muchas estafas usan su nombre para atraer víctimas.",
],
ejemplo=[
r"El precio de una criptomoneda puede caer 30 % o más en pocas semanas, algo muy raro en el sol o el dólar.",
],
ojo=["Invierte solo lo que podrías perder por completo, y nunca compartas tus claves privadas."],
rel=["dinero", "curso-legal", "volatilidad", "esquema-ponzi"],
))

T.append(dict(
slug="rentas-de-cuarta-y-quinta-categoria", t="Rentas de cuarta y quinta categoría", cat="impuestos", ic="👔",
alias="cuarta categoría quinta categoría recibo por honorarios planilla rentas de trabajo",
corto="Son las dos formas de ingreso por trabajo para el impuesto a la renta en el Perú: la cuarta es por trabajo independiente y la quinta, por trabajo en planilla.",
simple=[
r"Si emites <strong>recibos por honorarios</strong> como trabajador independiente, tus ingresos son de <strong>cuarta categoría</strong>. Si estás en planilla, con contrato y boleta de pago, son de <strong>quinta categoría</strong>.",
r"Ambas se suman como «rentas de trabajo» y tienen una deducción de 7 <a href='uit.html'>UIT</a> al año antes de calcular el <a href='impuesto-a-la-renta.html'>impuesto a la renta</a>. En planilla, el empleador retiene el impuesto cada mes; con recibos, la retención depende de los montos que fija la SUNAT.",
],
ejemplo=[
r"Una diseñadora que trabaja en planilla de lunes a viernes y además hace trabajos por recibo los fines de semana tiene ingresos de quinta y de cuarta categoría a la vez.",
],
rel=["impuesto-a-la-renta", "uit", "base-imponible", "empleo-formal-e-informal"],
))

T.append(dict(
slug="tipo-de-cambio-informal", t="Tipo de cambio informal", cat="mercados", ic="🧥",
bcrp="Tipo de cambio informal", alias="cambistas tipo de cambio paralelo cambio en la calle mercado paralelo",
corto="Es el precio del dólar en el mercado no regulado, como el de los cambistas de la calle.",
simple=[
r"En el Perú, el tipo de cambio de los cambistas suele estar muy cerca del interbancario, porque el mercado de dólares es libre. En países con <a href='control-cambiario.html'>control de cambios</a>, en cambio, el dólar «paralelo» puede ser mucho más caro que el oficial.",
r"Una gran diferencia entre el tipo de cambio oficial y el informal suele ser señal de restricciones o de desconfianza en la moneda.",
],
ejemplo=[
r"Si el dólar interbancario está en S/ 3.70, un cambista podría comprarte a S/ 3.68 y venderte a S/ 3.72: esa diferencia es su ganancia.",
],
ojo=["Al cambiar en la calle, prefiere cambistas autorizados (con chaleco y credencial municipal) y revisa los billetes en el momento."],
rel=["tipo-de-cambio", "tipo-de-cambio-bancario", "diferencial-cambiario", "control-cambiario"],
))

T.append(dict(
slug="sobreendeudamiento", t="Sobreendeudamiento", cat="finanzas", ic="🏋️",
alias="sobreendeudamiento deudas excesivas carga de deuda reprogramación",
corto="Es cuando una persona o empresa debe más de lo que puede pagar con sus ingresos, y las cuotas le impiden cubrir sus gastos básicos.",
simple=[
r"Suele empezar con varias tarjetas, préstamos de consumo y pagos mínimos que se acumulan. Cuando las cuotas superan una parte importante del ingreso, cualquier imprevisto lleva a atrasos.",
r"Una señal de alerta es que las cuotas de todas tus deudas pasen de un tercio de tu ingreso. En ese caso conviene dejar de endeudarse, ordenar las deudas y conversar con las entidades para reprogramar.",
],
formula=dict(
tex=r"\text{Carga de deuda}=\frac{\text{Cuotas mensuales}}{\text{Ingreso mensual}}\times100",
calculo=[r"\frac{900}{2000}\times100=45\,\%"],
),
ejemplo=[
r"Si ganas S/ 2000 y pagas S/ 900 de cuotas al mes, tu carga de deuda es 45 %: estás en zona de riesgo.",
],
rel=["capacidad-de-endeudamiento", "pago-minimo", "central-de-riesgos", "presupuesto-personal"],
))

# --- Contabilidad y análisis financiero ------------------------------------

T.append(dict(
slug="depreciacion-contable", t="Depreciación contable", cat="finanzas", ic="🔧",
bcrp="Vida útil económica", alias="depreciación de activos vida útil desgaste línea recta",
corto="Es el registro del desgaste de una máquina, un vehículo o un local a lo largo de su vida útil, repartiendo su costo entre varios años.",
simple=[
r"Si una empresa compra una máquina que durará 5 años, no registra todo su costo como gasto el primer año: lo reparte entre los 5 años de <strong>vida útil</strong>.",
r"El método más simple es el de <strong>línea recta</strong>: el mismo monto cada año. La depreciación reduce la utilidad contable, pero no es una salida de dinero en ese año.",
],
formula=dict(
tex=r"\text{Depreciación anual}=\frac{\text{Costo}-\text{Valor residual}}{\text{Vida útil}}",
calculo=[r"\frac{50\,000-5000}{5}=9000\ \text{soles por año}"],
),
ejemplo=[
r"Una camioneta cuesta S/ 50 000, durará 5 años y al final valdrá S/ 5000: se deprecian S/ 9000 cada año.",
],
rel=["estado-de-resultados", "consumo-de-capital-fijo", "ebitda", "balance-general"],
))

T.append(dict(
slug="ebitda", t="EBITDA", cat="finanzas", ic="📊",
alias="EBITDA utilidad operativa antes de depreciación y amortización flujo operativo",
corto="Es la ganancia de una empresa antes de restar intereses, impuestos, depreciación y amortización; muestra cuánto genera su operación.",
simple=[
r"Sus siglas en inglés significan utilidad antes de intereses, impuestos, depreciación y amortización. Al quitar esos rubros, permite comparar el desempeño operativo de empresas con distinta deuda o distinta antigüedad de sus activos.",
r"Se usa mucho para medir cuántas veces la deuda supera lo que genera la empresa (deuda/EBITDA). Pero no es dinero libre: la empresa igual tendrá que pagar intereses, impuestos y reponer sus máquinas.",
],
formula=dict(
tex=r"\begin{aligned}\text{EBITDA}={}&\text{Utilidad operativa}\\&+\text{Depreciación}+\text{Amortización}\end{aligned}",
calculo=[r"800+150+50=1000\ \text{mil soles}"],
),
ejemplo=[
r"Si una empresa tiene una utilidad operativa de S/ 800 mil, S/ 150 mil de depreciación y S/ 50 mil de amortización, su EBITDA es S/ 1 millón.",
],
rel=["estado-de-resultados", "depreciacion-contable", "margen-de-utilidad", "covenant"],
))

T.append(dict(
slug="margen-de-utilidad", t="Margen de utilidad", cat="finanzas", ic="✂️",
alias="margen bruto margen operativo margen neto rentabilidad sobre ventas",
corto="Es el porcentaje de cada sol vendido que se convierte en ganancia; puede medirse antes o después de los gastos y los impuestos.",
simple=[
r"El <strong>margen bruto</strong> resta solo el costo de lo vendido. El <strong>margen operativo</strong> resta también los gastos de administración y de ventas. El <strong>margen neto</strong> resta todo, incluidos intereses e impuestos.",
r"Comparar márgenes ayuda a ver si un negocio es eficiente, aunque lo normal varía mucho entre sectores: un supermercado vive con márgenes pequeños; una empresa de software, con márgenes grandes.",
],
formula=dict(
tex=r"\text{Margen neto}=\frac{\text{Utilidad neta}}{\text{Ventas}}\times100",
calculo=[r"\frac{60}{1000}\times100=6\,\%"],
),
ejemplo=[
r"Si una tienda vende S/ 1 millón al año y su utilidad neta es S/ 60 mil, su margen neto es 6 %: gana 6 céntimos por cada sol vendido.",
],
rel=["estado-de-resultados", "roe-y-roa", "rentabilidad", "ebitda"],
))

T.append(dict(
slug="roe-y-roa", t="ROE y ROA", cat="finanzas", ic="🎯",
alias="ROE rentabilidad sobre patrimonio ROA rentabilidad sobre activos",
corto="El ROE mide cuánto ganan los accionistas sobre el dinero que pusieron; el ROA, cuánto rinde la empresa sobre todos sus activos.",
simple=[
r"El <strong>ROE</strong> divide la utilidad neta entre el <a href='patrimonio.html'>patrimonio</a>. El <strong>ROA</strong> la divide entre los activos totales.",
r"Si el ROE es mucho mayor que el ROA, la empresa usa bastante deuda (<a href='apalancamiento.html'>apalancamiento</a>): eso multiplica las ganancias en buenos tiempos, pero también las pérdidas en los malos. Son indicadores clave para analizar bancos.",
],
formula=dict(
tex=r"ROE=\frac{\text{Utilidad neta}}{\text{Patrimonio}},\qquad ROA=\frac{\text{Utilidad neta}}{\text{Activos totales}}",
calculo=[r"ROE=\frac{2}{10}=20\,\%;\quad ROA=\frac{2}{100}=2\,\%"],
),
ejemplo=[
r"Un banco gana S/ 2 millones con S/ 100 millones de activos y S/ 10 millones de patrimonio: su ROA es 2 % y su ROE, 20 %.",
],
rel=["rentabilidad", "apalancamiento", "patrimonio", "margen-de-utilidad"],
))

# --- Estadística y econometría ---------------------------------------------

T.append(dict(
slug="media-mediana-y-moda", t="Media, mediana y moda", cat="bienestar", ic="📏",
alias="promedio media aritmética mediana moda medidas de tendencia central",
corto="Son tres formas de resumir un conjunto de datos con un solo valor «típico»: el promedio, el valor del medio y el más repetido.",
simple=[
r"La <strong>media</strong> es el promedio: sumas todo y divides entre la cantidad de datos. La <strong>mediana</strong> es el valor que queda justo al medio cuando ordenas los datos. La <strong>moda</strong> es el valor que más se repite.",
r"Con ingresos, la mediana suele representar mejor a la persona típica, porque unos pocos ingresos muy altos suben mucho la media.",
],
formula=dict(
tex=r"\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i",
calculo=[r"\frac{1+1+2+3+18}{5}=5"],
),
ejemplo=[
r"Si cinco personas ganan 1, 1, 2, 3 y 18 mil soles, la media es 5 mil, la mediana 2 mil y la moda 1 mil. La mediana describe mejor a la mayoría.",
],
rel=["varianza-y-desviacion-estandar", "percentiles-y-quintiles", "distribucion-del-ingreso", "promedio-movil"],
))

T.append(dict(
slug="varianza-y-desviacion-estandar", t="Varianza y desviación estándar", cat="bienestar", ic="↔️",
alias="varianza desviación estándar dispersión desviación típica",
corto="Miden qué tan dispersos están los datos alrededor del promedio: si son parecidos entre sí o muy distintos.",
simple=[
r"La <strong>varianza</strong> promedia las distancias al cuadrado de cada dato respecto a la media. La <strong>desviación estándar</strong> es su raíz cuadrada, y tiene la ventaja de estar en las mismas unidades que los datos.",
r"En finanzas, la desviación estándar de los rendimientos se usa como medida de riesgo o <a href='volatilidad.html'>volatilidad</a>.",
],
formula=dict(
tex=r"s^{2}=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^{2},\qquad s=\sqrt{s^{2}}",
calculo=[r"\text{datos }2,4,6:\ s^{2}=\frac{4+0+4}{2}=4,\ s=2"],
),
ejemplo=[
r"Dos fondos rinden en promedio 6 % al año, pero uno tiene desviación estándar de 2 % y el otro de 15 %: el segundo es mucho más arriesgado.",
],
rel=["media-mediana-y-moda", "coeficiente-de-variacion", "volatilidad", "distribucion-normal"],
))

T.append(dict(
slug="coeficiente-de-variacion", t="Coeficiente de variación", cat="bienestar", ic="➗",
alias="coeficiente de variación dispersión relativa CV",
corto="Es la desviación estándar dividida entre la media; permite comparar la dispersión de datos con distintos tamaños o unidades.",
simple=[
r"Una desviación de S/ 100 es mucho para sueldos de S/ 500, pero poco para sueldos de S/ 10 000. El <strong>coeficiente de variación</strong> corrige eso expresando la dispersión como porcentaje de la media.",
r"En estadísticas oficiales también se usa para juzgar la precisión de una estimación: un coeficiente alto indica que la cifra es poco confiable.",
],
formula=dict(
tex=r"CV=\frac{s}{\bar{x}}\times100",
calculo=[r"\frac{300}{1500}\times100=20\,\%"],
),
ejemplo=[
r"Si los sueldos de una empresa promedian S/ 1500 con una desviación estándar de S/ 300, el coeficiente de variación es 20 %.",
],
rel=["varianza-y-desviacion-estandar", "media-mediana-y-moda", "muestra-y-poblacion", "intervalo-de-confianza"],
))

T.append(dict(
slug="distribucion-normal", t="Distribución normal", cat="bienestar", ic="🔔",
alias="distribución normal campana de Gauss gaussiana regla 68 95 99.7",
corto="Es la forma de campana que siguen muchos datos: la mayoría cerca del promedio y cada vez menos a medida que te alejas.",
simple=[
r"En una distribución normal, cerca del <strong>68 %</strong> de los datos está a una desviación estándar de la media, cerca del <strong>95 %</strong> a dos y cerca del <strong>99.7 %</strong> a tres.",
r"Es la base de muchas pruebas estadísticas. Pero cuidado: en finanzas, las caídas extremas ocurren más seguido de lo que predice la normal («colas gruesas»).",
],
formula=dict(
tex=r"z=\frac{x-\mu}{\sigma}",
donde=[(r"\mu", "media"), (r"\sigma", "desviación estándar"), (r"z", "cuántas desviaciones estándar se aleja x de la media")],
calculo=[r"\frac{16-12}{2}=2"],
),
ejemplo=[
r"Si las notas de un curso tienen media 12 y desviación estándar 2, una nota de 16 está a 2 desviaciones por encima: solo alrededor del 2.5 % sacaría esa nota o más.",
],
rel=["varianza-y-desviacion-estandar", "intervalo-de-confianza", "prueba-de-hipotesis", "ley-de-los-grandes-numeros"],
))

T.append(dict(
slug="muestra-y-poblacion", t="Muestra y población", cat="bienestar", ic="🧪",
alias="muestra población muestreo aleatorio encuesta representativa",
corto="La población es todo el grupo que quieres estudiar; la muestra es la parte que realmente observas para sacar conclusiones sobre el todo.",
simple=[
r"Preguntar a todos los peruanos es un <a href='censo.html'>censo</a>. Lo habitual es encuestar una <strong>muestra</strong> bien elegida, por ejemplo unas decenas de miles de hogares, para estimar cómo es la <strong>población</strong>.",
r"Para que la muestra represente bien al todo, debe elegirse al azar. Una muestra mal hecha produce <a href='sesgo-de-seleccion.html'>sesgo</a>, por grande que sea.",
],
ejemplo=[
r"La Encuesta Nacional de Hogares del INEI entrevista a una muestra de hogares para estimar la pobreza, el empleo y el ingreso de todo el país.",
],
rel=["censo", "sesgo-de-seleccion", "intervalo-de-confianza", "ley-de-los-grandes-numeros"],
))

T.append(dict(
slug="ley-de-los-grandes-numeros", t="Ley de los grandes números", cat="bienestar", ic="🎰",
alias="ley de los grandes números probabilidad promedio muestral",
corto="Dice que, al repetir muchas veces un experimento al azar, el promedio de los resultados se acerca cada vez más al valor esperado.",
simple=[
r"Si lanzas una moneda 10 veces, puede salir cara 7 veces. Si la lanzas 10 000 veces, la proporción de caras estará muy cerca de 50 %.",
r"Por eso las aseguradoras pueden calcular bien sus costos: no saben quién tendrá un accidente, pero con muchos clientes el promedio es muy predecible.",
],
ejemplo=[
r"Un casino puede perder con un jugador una noche, pero con millones de apuestas su ganancia promedio es casi segura.",
],
rel=["muestra-y-poblacion", "distribucion-normal", "compania-de-seguros", "diversificacion"],
))

T.append(dict(
slug="percentiles-y-quintiles", t="Percentiles, deciles y quintiles", cat="bienestar", ic="🪜",
alias="percentil decil quintil cuartil distribución del ingreso",
corto="Dividen los datos ordenados en partes iguales: los quintiles en 5 grupos, los deciles en 10 y los percentiles en 100.",
simple=[
r"Si ordenas a todos los hogares de menor a mayor ingreso y los separas en cinco grupos del mismo tamaño, obtienes <strong>quintiles</strong>. El quintil 1 es el 20 % más pobre; el quintil 5, el 20 % más rico.",
r"Estas divisiones se usan para medir la desigualdad: por ejemplo, comparar cuánto ingreso recibe el decil más rico frente al más pobre.",
],
ejemplo=[
r"Si tu nota está en el percentil 90, superaste al 90 % de los estudiantes que dieron el examen.",
],
rel=["media-mediana-y-moda", "distribucion-del-ingreso", "coeficiente-de-gini", "curva-de-lorenz"],
))

T.append(dict(
slug="correlacion", t="Correlación", cat="bienestar", ic="🔗",
alias="correlación coeficiente de correlación de Pearson correlación no implica causalidad",
corto="Mide si dos variables tienden a moverse juntas y con qué fuerza; va de −1 a +1.",
simple=[
r"Una correlación cercana a <strong>+1</strong> indica que, cuando una sube, la otra también; cercana a <strong>−1</strong>, que cuando una sube, la otra baja; cerca de <strong>0</strong>, que no hay relación lineal clara.",
r"Ojo: <strong>correlación no implica causalidad</strong>. Las ventas de helados y los ahogamientos suben juntos en verano, pero uno no causa el otro: ambos dependen del calor.",
],
formula=dict(
tex=r"r=\frac{\operatorname{Cov}(x,y)}{s_x\,s_y}",
calculo=[r"\frac{12}{4\times5}=0.6"],
),
ejemplo=[
r"Si la covarianza entre años de estudio e ingreso es 12, y sus desviaciones estándar son 4 y 5, la correlación es 0.6: positiva y moderada.",
],
rel=["regresion-lineal", "endogeneidad", "coeficiente-de-determinacion", "beta-y-capm"],
))

T.append(dict(
slug="regresion-lineal", t="Regresión lineal", cat="bienestar", ic="📐",
alias="regresión lineal modelo lineal pendiente intercepto econometría",
corto="Es un método para estimar cómo cambia una variable cuando cambia otra, ajustando una recta a los datos.",
simple=[
r"Por ejemplo, para saber cuánto aumenta el sueldo por cada año adicional de estudio, se reúnen datos de muchas personas y se busca la recta que mejor los representa. La <strong>pendiente</strong> de esa recta responde la pregunta.",
r"Se puede incluir más de una variable explicativa (regresión múltiple) para «controlar» por otros factores, como la experiencia o la región.",
],
formula=dict(
tex=r"y_i=\beta_0+\beta_1x_i+u_i",
donde=[(r"\beta_0", "intercepto"), (r"\beta_1", "pendiente: cambio en y por cada unidad de x"), (r"u_i", "error: todo lo que no explica x")],
calculo=[r"\hat{y}=500+120\times11=1820"],
),
ejemplo=[
r"Si la recta estimada es sueldo = 500 + 120 × años de estudio, a una persona con 11 años de estudio se le predice un sueldo de S/ 1820.",
],
rel=["minimos-cuadrados-ordinarios", "coeficiente-de-determinacion", "correlacion", "endogeneidad"],
))

T.append(dict(
slug="minimos-cuadrados-ordinarios", t="Mínimos cuadrados ordinarios (MCO)", cat="bienestar", ic="◻️",
alias="MCO OLS mínimos cuadrados estimación residuos",
corto="Es el método más usado para estimar una regresión: elige la recta que hace más pequeña la suma de los errores al cuadrado.",
simple=[
r"Cada dato se aleja un poco de la recta: esa distancia es el <strong>residuo</strong>. MCO elige la pendiente y el intercepto que minimizan la suma de los residuos al cuadrado.",
r"Bajo ciertos supuestos (errores sin relación con las variables explicativas, varianza constante, sin autocorrelación) los estimadores de MCO son los mejores posibles entre los lineales e insesgados. Cuando esos supuestos fallan aparecen problemas como la <a href='heterocedasticidad.html'>heterocedasticidad</a> o la <a href='endogeneidad.html'>endogeneidad</a>.",
],
formula=dict(
tex=r"\hat{\beta}_1=\frac{\sum (x_i-\bar{x})(y_i-\bar{y})}{\sum (x_i-\bar{x})^{2}},\qquad \hat{\beta}_0=\bar{y}-\hat{\beta}_1\bar{x}",
calculo=[r"\hat{\beta}_1=\frac{240}{2}=120"],
),
ejemplo=[
r"Si la suma de productos cruzados de desvíos es 240 y la suma de desvíos de x al cuadrado es 2, la pendiente estimada es 120.",
],
rel=["regresion-lineal", "heterocedasticidad", "autocorrelacion", "multicolinealidad"],
))

T.append(dict(
slug="coeficiente-de-determinacion", t="Coeficiente de determinación (R²)", cat="bienestar", ic="🎯",
alias="R cuadrado R2 bondad de ajuste R2 ajustado",
corto="Indica qué porcentaje de la variación de la variable que estudias es explicado por el modelo de regresión; va de 0 a 1.",
simple=[
r"Un <strong>R²</strong> de 0.7 significa que el modelo explica el 70 % de las diferencias observadas en la variable dependiente; el 30 % restante queda en el error.",
r"Un R² alto no prueba que el modelo sea correcto ni que haya causalidad, y agregar variables siempre lo sube. Por eso se usa también el <strong>R² ajustado</strong>, que penaliza agregar variables inútiles.",
],
formula=dict(
tex=r"R^{2}=1-\frac{\sum \hat{u}_i^{2}}{\sum (y_i-\bar{y})^{2}}",
calculo=[r"1-\frac{30}{100}=0.70"],
),
ejemplo=[
r"Si la suma de errores al cuadrado es 30 y la variación total es 100, el R² es 0.70.",
],
rel=["regresion-lineal", "minimos-cuadrados-ordinarios", "correlacion", "multicolinealidad"],
))

T.append(dict(
slug="intervalo-de-confianza", t="Intervalo de confianza", cat="bienestar", ic="🎚️",
alias="intervalo de confianza margen de error nivel de confianza 95",
corto="Es un rango de valores dentro del cual se espera que esté el valor verdadero que se quiere estimar, con cierto nivel de confianza.",
simple=[
r"Una encuesta nunca da el valor exacto de toda la población. Por eso se informa un <strong>intervalo</strong>: por ejemplo, «la pobreza está entre 24 % y 27 % con 95 % de confianza».",
r"Cuanto más grande es la muestra, más estrecho es el intervalo. El «margen de error» de las encuestas electorales es la mitad del ancho de este intervalo.",
],
formula=dict(
tex=r"IC_{95\%}=\bar{x}\pm1.96\,\frac{s}{\sqrt{n}}",
calculo=[r"1500\pm1.96\times\frac{400}{\sqrt{400}}=1500\pm39.2"],
),
ejemplo=[
r"Con 400 personas encuestadas, un ingreso promedio de S/ 1500 y desviación estándar de S/ 400, el intervalo de 95 % va de S/ 1460.8 a S/ 1539.2.",
],
rel=["muestra-y-poblacion", "distribucion-normal", "prueba-de-hipotesis", "valor-p"],
))

T.append(dict(
slug="prueba-de-hipotesis", t="Prueba de hipótesis", cat="bienestar", ic="⚖️",
alias="prueba de hipótesis hipótesis nula hipótesis alternativa estadístico t significancia",
corto="Es un procedimiento para decidir, con datos, si se puede rechazar una afirmación inicial (la hipótesis nula).",
simple=[
r"Se parte de una <strong>hipótesis nula</strong>, por ejemplo «estudiar un año más no cambia el sueldo» (\(\beta_1=0\)). Luego se calcula qué tan raro sería observar los datos si esa hipótesis fuera cierta.",
r"Si sería muy raro, se rechaza la nula. En regresiones se usa el <strong>estadístico t</strong>: valores mayores que 1.96 en valor absoluto indican significancia al 5 % en muestras grandes.",
],
formula=dict(
tex=r"t=\frac{\hat{\beta}_1-0}{\operatorname{ee}(\hat{\beta}_1)}",
calculo=[r"\frac{120}{40}=3>1.96"],
),
ejemplo=[
r"Si la pendiente estimada es 120 y su error estándar es 40, el estadístico t es 3: se rechaza que el efecto sea cero, al 5 % de significancia.",
],
rel=["valor-p", "errores-tipo-i-y-ii", "intervalo-de-confianza", "regresion-lineal"],
))

T.append(dict(
slug="valor-p", t="Valor p", cat="bienestar", ic="🅿️",
alias="valor p p-value significancia estadística nivel de significancia",
corto="Es la probabilidad de obtener resultados tan extremos como los observados si la hipótesis nula fuera cierta; si es muy pequeño, se rechaza la nula.",
simple=[
r"Lo habitual es comparar el <strong>valor p</strong> con 0.05. Si es menor, se dice que el resultado es «estadísticamente significativo» al 5 %.",
r"Un valor p pequeño no dice que el efecto sea grande ni importante, solo que es poco probable que sea puro azar. Y un valor p grande no prueba que el efecto sea cero.",
],
ejemplo=[
r"Si un estudio encuentra que un programa social aumenta la asistencia escolar con un valor p de 0.01, es muy poco probable que ese resultado se deba solo a la suerte.",
],
rel=["prueba-de-hipotesis", "errores-tipo-i-y-ii", "intervalo-de-confianza", "regresion-lineal"],
))

T.append(dict(
slug="errores-tipo-i-y-ii", t="Errores tipo I y tipo II", cat="bienestar", ic="❌",
alias="error tipo I error tipo II falso positivo falso negativo potencia",
corto="El error tipo I es rechazar una hipótesis nula que era cierta (falso positivo); el tipo II es no rechazar una que era falsa (falso negativo).",
simple=[
r"El <strong>error tipo I</strong> es como condenar a un inocente: concluir que hay un efecto cuando no lo hay. Su probabilidad es el nivel de significancia, por ejemplo 5 %.",
r"El <strong>error tipo II</strong> es como absolver a un culpable: no detectar un efecto que sí existe. Reducir uno suele aumentar el otro; una muestra más grande ayuda a reducir ambos.",
],
ejemplo=[
r"Una prueba médica que dice que una persona sana está enferma comete un error tipo I; si dice que una persona enferma está sana, comete un error tipo II.",
],
rel=["prueba-de-hipotesis", "valor-p", "muestra-y-poblacion", "intervalo-de-confianza"],
))

T.append(dict(
slug="multicolinealidad", t="Multicolinealidad", cat="bienestar", ic="🪢",
alias="multicolinealidad variables correlacionadas VIF regresión múltiple",
corto="Es cuando dos o más variables explicativas de una regresión están muy relacionadas entre sí, lo que hace difícil separar el efecto de cada una.",
simple=[
r"Si en una regresión pones como variables explicativas los años de estudio y el nivel educativo alcanzado, ambas dicen casi lo mismo. El modelo no sabe a cuál atribuir el efecto y los coeficientes se vuelven imprecisos.",
r"Una señal es un <a href='coeficiente-de-determinacion.html'>R²</a> alto con coeficientes individualmente no significativos. Se detecta, por ejemplo, con el factor de inflación de la varianza (VIF).",
],
ejemplo=[
r"Al explicar el consumo con el ingreso y la riqueza de las familias, que suelen moverse juntas, puede costar distinguir cuánto influye cada una.",
],
rel=["regresion-lineal", "minimos-cuadrados-ordinarios", "coeficiente-de-determinacion", "correlacion"],
))

T.append(dict(
slug="heterocedasticidad", t="Heterocedasticidad", cat="bienestar", ic="🎺",
alias="heterocedasticidad varianza no constante errores robustos White",
corto="Es cuando la dispersión de los errores de una regresión no es la misma para todas las observaciones.",
simple=[
r"Por ejemplo, el gasto de las familias de altos ingresos varía mucho más que el de las de bajos ingresos. Si se estima una regresión del gasto contra el ingreso, los errores serán más grandes para los ingresos altos.",
r"Los coeficientes de <a href='minimos-cuadrados-ordinarios.html'>MCO</a> siguen siendo insesgados, pero sus errores estándar están mal calculados y las pruebas de hipótesis pueden engañar. La solución habitual es usar errores estándar <strong>robustos</strong>.",
],
ejemplo=[
r"Al estimar las ventas de empresas según su tamaño, las grandes muestran variaciones mucho mayores que las pequeñas: es un caso típico de heterocedasticidad.",
],
rel=["minimos-cuadrados-ordinarios", "regresion-lineal", "autocorrelacion", "prueba-de-hipotesis"],
))

T.append(dict(
slug="autocorrelacion", t="Autocorrelación", cat="bienestar", ic="🔂",
alias="autocorrelación correlación serial Durbin-Watson series de tiempo",
corto="Es cuando los errores de una regresión están relacionados con los de periodos anteriores; es común en datos que se miden en el tiempo.",
simple=[
r"Si la inflación de un mes fue más alta de lo que predecía el modelo, es probable que la del mes siguiente también lo sea. Esa relación entre errores es la <strong>autocorrelación</strong>.",
r"Igual que la <a href='heterocedasticidad.html'>heterocedasticidad</a>, no sesga los coeficientes de MCO, pero hace que los errores estándar sean incorrectos. Se detecta con pruebas como la de Durbin-Watson.",
],
ejemplo=[
r"En una regresión de las ventas mensuales de una tienda, un mes de ventas inesperadamente altas suele venir seguido de otro similar: los errores están autocorrelacionados.",
],
rel=["series-de-tiempo", "heterocedasticidad", "minimos-cuadrados-ordinarios", "estacionariedad"],
))

T.append(dict(
slug="variable-dicotomica", t="Variable dicotómica (dummy)", cat="bienestar", ic="🔘",
alias="variable dummy variable ficticia variable binaria 0 y 1",
corto="Es una variable que solo toma los valores 0 o 1 para indicar si algo ocurre o no, como ser mujer, vivir en zona urbana o haber recibido un programa.",
simple=[
r"Las regresiones trabajan con números, así que las características cualitativas se convierten en <strong>dummies</strong>: 1 si la persona vive en Lima, 0 si no.",
r"Su coeficiente se interpreta como la diferencia promedio entre los dos grupos, manteniendo constante lo demás.",
],
ejemplo=[
r"En la regresión sueldo = 900 + 300 × Lima, quien vive en Lima gana en promedio S/ 300 más que quien vive fuera, con las demás variables iguales.",
],
rel=["regresion-lineal", "diferencias-en-diferencias", "datos-de-panel", "endogeneidad"],
))

T.append(dict(
slug="endogeneidad", t="Endogeneidad", cat="bienestar", ic="🌀",
alias="endogeneidad variable omitida causalidad inversa sesgo error de medición",
corto="Es cuando una variable explicativa está relacionada con el error de la regresión; eso hace que el efecto estimado esté sesgado.",
simple=[
r"Tiene tres causas típicas. <strong>Variables omitidas</strong>: la habilidad influye en el estudio y en el sueldo, pero no se observa. <strong>Causalidad inversa</strong>: más policías pueden reducir el crimen, pero más crimen también atrae más policías. <strong>Errores de medición</strong> en la variable explicativa.",
r"Con endogeneidad, la regresión mide una <a href='correlacion.html'>correlación</a>, no el efecto causal. Se corrige con <a href='variables-instrumentales.html'>variables instrumentales</a>, datos de panel, experimentos o métodos como <a href='diferencias-en-diferencias.html'>diferencias en diferencias</a>.",
],
ejemplo=[
r"Si se estima que las personas con más estudios ganan más, parte de ese efecto puede deberse a que son más hábiles o tienen mejores contactos, no solo al estudio.",
],
rel=["variables-instrumentales", "correlacion", "sesgo-de-seleccion", "diferencias-en-diferencias"],
))

T.append(dict(
slug="variables-instrumentales", t="Variables instrumentales", cat="bienestar", ic="🎻",
alias="variables instrumentales VI MC2E mínimos cuadrados en dos etapas instrumento",
corto="Es un método para estimar efectos causales cuando hay endogeneidad, usando una variable (el instrumento) que influye en la causa pero no directamente en el resultado.",
simple=[
r"Un buen <strong>instrumento</strong> cumple dos condiciones: está relacionado con la variable explicativa (relevancia) y solo afecta al resultado a través de ella (exogeneidad).",
r"Se suele estimar con <strong>mínimos cuadrados en dos etapas</strong>: primero se predice la variable explicativa con el instrumento y luego se usa esa predicción en la regresión principal.",
],
ejemplo=[
r"Un ejemplo clásico usa la cercanía de una universidad al hogar como instrumento de los años de estudio: vivir cerca facilita estudiar, pero no debería cambiar el sueldo por sí mismo.",
],
rel=["endogeneidad", "regresion-lineal", "minimos-cuadrados-ordinarios", "diferencias-en-diferencias"],
))

T.append(dict(
slug="datos-de-panel", t="Datos de panel", cat="bienestar", ic="🗃️",
alias="datos de panel datos longitudinales efectos fijos efectos aleatorios",
corto="Son datos que siguen a las mismas personas, empresas o países a lo largo de varios periodos.",
simple=[
r"Combinan la dimensión de corte transversal (muchos individuos) con la temporal (varios años). Por ejemplo, las mismas 1000 empresas observadas cada año entre 2015 y 2025.",
r"Su gran ventaja es que permiten controlar características que no cambian en el tiempo y que no se observan, usando <strong>efectos fijos</strong>. Eso reduce la <a href='endogeneidad.html'>endogeneidad</a> por variables omitidas.",
],
ejemplo=[
r"Seguir a los mismos hogares durante varios años permite ver cómo cambia su ingreso cuando uno de sus miembros consigue un empleo formal, comparando al hogar consigo mismo.",
],
rel=["endogeneidad", "series-de-tiempo", "diferencias-en-diferencias", "regresion-lineal"],
))

T.append(dict(
slug="series-de-tiempo", t="Series de tiempo", cat="bienestar", ic="🕰️",
alias="series de tiempo series temporales tendencia estacionalidad pronóstico ARIMA",
corto="Son datos de una misma variable medidos en momentos sucesivos, como la inflación mensual o el PBI trimestral.",
simple=[
r"Una serie de tiempo suele tener <strong>tendencia</strong> (dirección de largo plazo), <strong>estacionalidad</strong> (patrones que se repiten, como las ventas de diciembre) y movimientos irregulares.",
r"Para analizarlas se usan técnicas como la <a href='desestacionalizacion.html'>desestacionalización</a>, los <a href='promedio-movil.html'>promedios móviles</a> o modelos ARIMA, y hay que revisar si son <a href='estacionariedad.html'>estacionarias</a>.",
],
ejemplo=[
r"La serie mensual del tipo de cambio desde el año 2000 permite estudiar cómo reaccionó el sol frente a las crisis internacionales.",
],
rel=["estacionariedad", "autocorrelacion", "desestacionalizacion", "promedio-movil"],
))

T.append(dict(
slug="estacionariedad", t="Estacionariedad", cat="bienestar", ic="🧘",
alias="estacionariedad raíz unitaria Dickey-Fuller regresión espuria",
corto="Una serie es estacionaria si su promedio y su variabilidad se mantienen estables en el tiempo, sin una tendencia que la arrastre.",
simple=[
r"Muchas series económicas, como el PBI, crecen con el tiempo: no son estacionarias. Su tasa de crecimiento, en cambio, suele serlo.",
r"Si se hace una regresión entre dos series no estacionarias, se pueden encontrar relaciones falsas (<strong>regresión espuria</strong>). Por eso se aplican pruebas de raíz unitaria, como la de Dickey-Fuller, y se trabaja con diferencias o tasas de variación.",
],
ejemplo=[
r"El número de celulares en el Perú y el PBI crecieron juntos durante años, pero una regresión entre ambos en niveles podría mostrar una relación engañosamente fuerte.",
],
rel=["series-de-tiempo", "tasa-de-variacion", "autocorrelacion", "regresion-lineal"],
))

T.append(dict(
slug="diferencias-en-diferencias", t="Diferencias en diferencias", cat="bienestar", ic="➖",
alias="diferencias en diferencias DiD evaluación de impacto grupo de control grupo de tratamiento",
corto="Es un método para medir el efecto de una política comparando cómo cambió un grupo que la recibió frente a otro que no, antes y después.",
simple=[
r"Se calcula el cambio del grupo tratado (después menos antes) y se le resta el cambio del grupo de control. Así se descuentan los factores que afectaron a ambos por igual, como la situación económica general.",
r"El supuesto clave es el de <strong>tendencias paralelas</strong>: sin la política, ambos grupos habrían evolucionado de forma parecida.",
],
formula=dict(
tex=r"\widehat{DiD}=(\bar{y}_{T,\text{después}}-\bar{y}_{T,\text{antes}})-(\bar{y}_{C,\text{después}}-\bar{y}_{C,\text{antes}})",
calculo=[r"(80-60)-(70-62)=20-8=12"],
),
ejemplo=[
r"Si la asistencia escolar en distritos con un programa pasó de 60 % a 80 % y en distritos sin el programa de 62 % a 70 %, el efecto estimado del programa es de 12 puntos.",
],
rel=["endogeneidad", "datos-de-panel", "variable-dicotomica", "sesgo-de-seleccion"],
))

T.append(dict(
slug="sesgo-de-seleccion", t="Sesgo de selección", cat="bienestar", ic="🍒",
alias="sesgo de selección sesgo de supervivencia muestra no aleatoria autoselección",
corto="Es el error que aparece cuando el grupo estudiado no representa a la población, porque se eligió (o se eligió solo) de forma no aleatoria.",
simple=[
r"Si comparas los sueldos de quienes hicieron un curso con los de quienes no, puede que los que se inscribieron ya fueran más motivados. La diferencia no se debería solo al curso: hay <strong>autoselección</strong>.",
r"Un caso famoso es el <strong>sesgo de supervivencia</strong>: mirar solo a las empresas que siguen abiertas hace pensar que emprender es más fácil de lo que es, porque las que quebraron ya no aparecen.",
],
ejemplo=[
r"Una encuesta hecha solo por internet sobre el uso de la banca digital exagerará su uso, porque deja fuera a quienes no tienen internet.",
],
rel=["muestra-y-poblacion", "endogeneidad", "diferencias-en-diferencias", "correlacion"],
))

T.append(dict(
slug="numeros-indice", t="Números índice", cat="precios", ic="💯",
alias="número índice año base índice 100 Laspeyres Paasche",
corto="Son valores que comparan una variable con un periodo base al que se le asigna el valor 100, para ver fácilmente cuánto cambió.",
simple=[
r"Si el índice de un año es 125, la variable es 25 % mayor que en el año base. Así se construyen el <a href='ipc.html'>IPC</a>, los índices de producción o los <a href='terminos-de-intercambio.html'>términos de intercambio</a>.",
r"Los índices de precios combinan muchos productos con distintos pesos. El de <strong>Laspeyres</strong> usa las cantidades del año base; el de <strong>Paasche</strong>, las del año actual.",
],
formula=dict(
tex=r"\text{Índice}_t=\frac{x_t}{x_{\text{base}}}\times100",
calculo=[r"\frac{5}{4}\times100=125"],
),
ejemplo=[
r"Si el pasaje costaba S/ 4 en el año base y hoy cuesta S/ 5, su índice es 125: subió 25 %.",
],
herramienta=("Calcular la inflación entre dos fechas", "../inflacion/"),
rel=["ipc", "tasa-de-variacion", "deflactor-del-pbi", "valor-nominal-y-real"],
))

T.append(dict(
slug="tasa-de-variacion", t="Tasa de variación porcentual", cat="precios", ic="📶",
alias="variación porcentual tasa de crecimiento cambio porcentual puntos porcentuales",
corto="Es cuánto cambió una variable en porcentaje respecto a su valor inicial.",
simple=[
r"Es la operación más usada en economía: para la inflación, el crecimiento del PBI o la subida de un precio. Se resta el valor inicial del final y se divide entre el inicial.",
r"No hay que confundirla con la diferencia en <a href='puntos-porcentuales.html'>puntos porcentuales</a>: si el desempleo pasa de 5 % a 6 %, sube 1 punto porcentual, pero 20 % en términos relativos.",
],
formula=dict(
tex=r"\%\Delta=\frac{x_{\text{final}}-x_{\text{inicial}}}{x_{\text{inicial}}}\times100",
calculo=[r"\frac{4.40-4.00}{4.00}\times100=10\,\%"],
),
ejemplo=[
r"Si el kilo de arroz pasó de S/ 4.00 a S/ 4.40, su precio subió 10 %.",
],
herramienta=("Calcular la inflación entre dos fechas", "../inflacion/"),
rel=["puntos-porcentuales", "numeros-indice", "tasa-de-crecimiento-anual-compuesta", "inflacion"],
))

T.append(dict(
slug="tasa-de-crecimiento-anual-compuesta", t="Tasa de crecimiento anual compuesta", cat="produccion", ic="📈",
alias="TCAC CAGR crecimiento promedio anual media geométrica",
corto="Es el crecimiento promedio por año que, repetido cada año, lleva de un valor inicial a uno final; se calcula con la media geométrica.",
simple=[
r"Si algo creció 50 % en total en 5 años, no creció 10 % por año, porque el crecimiento se acumula. La tasa compuesta da el ritmo anual constante equivalente.",
r"Se usa para comparar el crecimiento del PBI entre décadas, la rentabilidad de inversiones o la evolución de las ventas de una empresa.",
],
formula=dict(
tex=r"TCAC=\left(\frac{x_{\text{final}}}{x_{\text{inicial}}}\right)^{1/n}-1",
calculo=[r"\left(\frac{150}{100}\right)^{1/5}-1\approx0.0845=8.45\,\%"],
),
ejemplo=[
r"Si las ventas de una empresa pasaron de S/ 100 mil a S/ 150 mil en 5 años, crecieron a una tasa compuesta de aproximadamente 8.45 % anual.",
],
rel=["tasa-de-variacion", "interes-compuesto", "crecimiento-economico", "regla-del-72"],
))

T.append(dict(
slug="deflactor-del-pbi", t="Deflactor del PBI", cat="precios", ic="🎈",
alias="deflactor implícito del PBI índice de precios de la economía",
corto="Es un índice de precios de todo lo que produce la economía; se obtiene dividiendo el PBI nominal entre el PBI real.",
simple=[
r"El <a href='ipc.html'>IPC</a> mide los precios de lo que consumen las familias. El <strong>deflactor del PBI</strong> abarca todos los bienes y servicios producidos en el país, incluidos los de inversión y exportación.",
r"Por eso puede moverse distinto del IPC: si sube mucho el precio del cobre, el deflactor sube aunque los precios al consumidor casi no cambien.",
],
formula=dict(
tex=r"\text{Deflactor}=\frac{\text{PBI nominal}}{\text{PBI real}}\times100",
calculo=[r"\frac{1100}{1000}\times100=110"],
),
ejemplo=[
r"Si el PBI nominal es S/ 1.1 billones y el real, a precios del año base, es S/ 1 billón, el deflactor es 110: los precios de la producción subieron 10 % desde el año base.",
],
rel=["pbi-nominal-y-real", "ipc", "numeros-indice", "inflacion"],
))

T.append(dict(
slug="inflacion-mensual-acumulada-y-anual", t="Inflación mensual, acumulada y anual", cat="precios", ic="🗓️",
alias="inflación mensual inflación acumulada inflación interanual últimos 12 meses",
corto="Son tres formas de medir la inflación: la del último mes, la acumulada desde enero y la de los últimos 12 meses.",
simple=[
r"La <strong>mensual</strong> compara el IPC de este mes con el del mes anterior. La <strong>acumulada</strong> compara con diciembre del año pasado. La <strong>anual</strong> o interanual compara con el mismo mes del año anterior; es la que usa el BCRP para su <a href='meta-de-inflacion.html'>meta</a>.",
r"Las tasas mensuales no se suman, se acumulan multiplicando, aunque con tasas pequeñas la suma da una aproximación cercana.",
],
formula=dict(
tex=r"\pi_{\text{acum}}=\prod_{m=1}^{k}(1+\pi_m)-1",
calculo=[r"(1.002)(1.003)(1.001)-1\approx0.0060=0.60\,\%"],
),
ejemplo=[
r"Si la inflación fue 0.2 % en enero, 0.3 % en febrero y 0.1 % en marzo, la acumulada al primer trimestre es de aproximadamente 0.60 %.",
],
herramienta=("Calcular la inflación entre dos fechas", "../inflacion/"),
rel=["inflacion", "ipc", "meta-de-inflacion", "tasa-de-variacion"],
))

# --- Otros conceptos -------------------------------------------------------

T.append(dict(
slug="equivalencia-ricardiana", t="Equivalencia ricardiana", cat="estado", ic="🪞",
alias="equivalencia ricardiana Barro deuda e impuestos futuros",
corto="Es la idea de que, si el Estado baja impuestos hoy y se endeuda, la gente ahorra más porque espera pagar más impuestos mañana, y el consumo no cambia.",
simple=[
r"La idea fue planteada por David Ricardo y formalizada por Robert Barro en los años setenta. Si las personas son muy previsoras, un recorte de impuestos financiado con deuda no las hace sentir más ricas: saben que la deuda se pagará con impuestos futuros.",
r"En la práctica se cumple solo en parte, porque muchas personas no pueden pedir prestado, no planifican tan a largo plazo o esperan que la deuda la paguen generaciones futuras.",
],
ejemplo=[
r"Si el Estado devuelve S/ 500 a cada familia financiándose con deuda, una familia «ricardiana» ahorraría esos S/ 500 para los impuestos futuros en lugar de gastarlos.",
],
rel=["deuda-publica", "politica-fiscal", "multiplicador-keynesiano", "expectativas-racionales"],
))

T.append(dict(
slug="bono-demografico", t="Bono demográfico", cat="trabajo", ic="👨‍👩‍👧‍👦",
alias="bono demográfico ventana demográfica población en edad de trabajar envejecimiento",
corto="Es el periodo en que la población en edad de trabajar es mucho mayor que la de niños y adultos mayores dependientes, lo que favorece el crecimiento.",
simple=[
r"Cuando baja la natalidad, durante varias décadas hay proporcionalmente más personas en edad de trabajar y menos dependientes. Eso reduce la <a href='tasa-de-dependencia.html'>tasa de dependencia</a> y puede elevar el ahorro y la producción.",
r"El bono no es automático: se aprovecha solo si hay empleo productivo y educación de calidad. Además es temporal, porque luego la población envejece.",
],
ejemplo=[
r"Varios países de Asia oriental crecieron muy rápido durante su bono demográfico porque lograron emplear a una gran población joven en industrias productivas.",
],
rel=["tasa-de-dependencia", "pea", "fuentes-de-crecimiento", "afp-y-onp"],
))
