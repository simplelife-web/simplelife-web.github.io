# -*- coding: utf-8 -*-
# Términos del glosario (parte 8): sexta tanda tomada de la lista del
# Glosario de Términos Económicos del BCRP. Las definiciones están
# redactadas con palabras propias; el campo "bcrp" guarda el nombre exacto
# del término en ese glosario para citarlo como fuente.

T = []

T.append(dict(
slug="activos-ponderados-por-riesgo", t="Activos ponderados por riesgo", cat="finanzas", ic="🏋️",
bcrp="Activos ponderados por riesgo", alias="APR activos ponderados requerimiento de capital Basilea",
corto="Es el total de préstamos e inversiones de un banco, pero «pesado» según lo riesgoso que es cada uno.",
simple=[
r"No todos los activos de un banco son igual de peligrosos. Un bono del Estado casi no tiene riesgo; un préstamo a una empresa nueva, mucho más. Por eso a cada activo se le asigna un <strong>peso</strong>: los más seguros cuentan poco y los más riesgosos cuentan más.",
r"La suma de esos valores ya ponderados sirve para saber cuánto capital propio debe tener el banco. Es el denominador del <a href='ratio-de-capital-global.html'>ratio de capital global</a>.",
],
formula=dict(
tex=r"\text{APR}=\sum_i \text{Activo}_i\times\text{Ponderador}_i",
donde=[(r"\text{Ponderador}_i", "porcentaje de riesgo asignado a cada activo (por ejemplo, 0 %, 50 % o 100 %)")],
calculo=[r"1000\times0\,\%+500\times100\,\%=500\ \text{millones}"],
),
ejemplo=[
r"Un banco tiene S/ 1000 millones en bonos del Estado con ponderador 0 % y S/ 500 millones en préstamos a empresas con ponderador 100 %. Aunque sus activos suman S/ 1500 millones, sus activos ponderados por riesgo son solo S/ 500 millones.",
],
rel=["ratio-de-capital-global", "riesgo-de-credito", "sbs", "patrimonio"],
))

T.append(dict(
slug="backwardation-y-contango", t="Backwardation y contango", cat="mercados", ic="〰️",
bcrp="Backwardation", alias="contango backwardation curva de futuros precio futuro precio spot",
corto="Son los nombres de dos situaciones del mercado de futuros: cuando el precio a futuro es menor que el de hoy (backwardation) o mayor (contango).",
simple=[
r"En un <a href='contrato-de-futuro.html'>contrato de futuro</a> se pacta hoy el precio de algo que se entregará después. Ese precio futuro no tiene por qué ser igual al precio al contado de hoy.",
r"Hay <strong>contango</strong> cuando el precio futuro es <strong>mayor</strong> que el de hoy, algo normal cuando guardar el producto cuesta (almacén, seguros, intereses). Hay <strong>backwardation</strong> cuando el precio futuro es <strong>menor</strong>, lo que suele indicar que el producto escasea ahora y se paga más por tenerlo de inmediato.",
],
ejemplo=[
r"Si hoy el cobre cuesta 9000 dólares la tonelada y el contrato a seis meses se pacta en 9200, el mercado está en contango. Si se pactara en 8800, estaría en backwardation.",
],
rel=["contrato-de-futuro", "materias-primas", "contrato-forward", "volatilidad"],
))

T.append(dict(
slug="banca-offshore", t="Banca offshore", cat="finanzas", ic="🏝️",
bcrp="Banca offshore", alias="banco offshore paraíso fiscal banca extraterritorial sucursal en el exterior",
corto="Son bancos que operan fuera del país de sus clientes, a menudo en centros financieros con impuestos bajos y reglas más flexibles.",
simple=[
r"Un banco <strong>offshore</strong> capta depósitos y da préstamos desde otro país, normalmente uno con impuestos bajos o con menos exigencias que el país de origen de sus clientes.",
r"No es ilegal en sí mismo, pero los depósitos allí no siempre tienen las mismas protecciones ni la misma supervisión local. Por eso los supervisores vigilan estas operaciones y los países intercambian información para evitar la evasión de impuestos y el lavado de dinero.",
],
ejemplo=[
r"Un grupo financiero peruano puede tener una sucursal en un centro financiero del Caribe para atender a clientes que quieren ahorrar en dólares fuera del país.",
],
ojo=["Si te ofrecen invertir en una entidad del extranjero, verifica quién la supervisa y qué protección tiene tu dinero."],
rel=["sistema-financiero", "evasion-y-elusion-tributaria", "secreto-bancario", "sbs"],
))

T.append(dict(
slug="banco-corresponsal", t="Banco corresponsal", cat="finanzas", ic="🌐",
bcrp="Banco corresponsal", alias="corresponsalía bancaria transferencias internacionales SWIFT",
corto="Es un banco extranjero que presta servicios a otro banco, por ejemplo para hacer pagos y transferencias en su país y en su moneda.",
simple=[
r"Un banco peruano no tiene oficinas en todos los países. Para mandar dólares a Estados Unidos o euros a España, usa un <strong>banco corresponsal</strong> de allá, donde mantiene una cuenta.",
r"El corresponsal recibe, paga y cobra por cuenta del banco peruano. Por eso, en una transferencia internacional a veces aparecen comisiones de bancos intermediarios.",
],
ejemplo=[
r"Si envías dinero a un familiar en Estados Unidos desde tu banco en Lima, el pago puede pasar por un banco de Nueva York que actúa como corresponsal y lo deposita en la cuenta de destino.",
],
rel=["remesas", "sistema-de-pagos", "divisa", "credito-documentario"],
))

T.append(dict(
slug="cajero-automatico", t="Cajero automático", cat="finanzas", ic="🏧",
bcrp="Cajero automático", alias="ATM cajero retiro de efectivo",
corto="Es la máquina con la que puedes retirar efectivo, consultar tu saldo y hacer algunas operaciones sin ir a una ventanilla.",
simple=[
r"El <strong>cajero automático</strong> (ATM, por sus siglas en inglés) funciona con tu tarjeta de débito o crédito y tu clave. Se conecta con el banco al instante para verificar tu saldo.",
r"Retirar en un cajero de otra red puede costar una comisión. Y si sacas efectivo con una <a href='tarjetas-de-credito-y-debito.html'>tarjeta de crédito</a>, eso es una disposición de efectivo, que suele tener una tasa de interés alta.",
],
ejemplo=[
r"Antes de retirar, revisa en la pantalla si el cajero cobra comisión. Algunos bancos no cobran en sus propios cajeros pero sí en los de otras redes.",
],
ojo=["Tapa el teclado al escribir tu clave y revisa que no haya piezas extrañas en la ranura de la tarjeta."],
rel=["tarjetas-de-credito-y-debito", "banca-electronica", "bancarizacion", "sistema-de-pagos"],
))

T.append(dict(
slug="canasta-de-monedas", t="Canasta de monedas", cat="mercados", ic="🧺",
bcrp="Canasta de monedas", alias="canasta de divisas DEG tipo de cambio multilateral",
corto="Es un grupo de monedas combinadas con ciertos pesos que se usa como referencia para medir el valor de otra moneda.",
simple=[
r"En vez de comparar el sol solo con el dólar, se puede comparar con una <strong>canasta</strong>: por ejemplo, el dólar, el euro, el yuan y las monedas de otros socios comerciales, cada una con un peso según cuánto comerciamos con ese país.",
r"Así se calcula el <a href='tipo-de-cambio-real.html'>tipo de cambio real multilateral</a>. Algunos países incluso fijan su moneda a una canasta, y los derechos especiales de giro del FMI también son una canasta de monedas.",
],
ejemplo=[
r"Si el sol se aprecia frente al dólar pero se deprecia frente al euro y al yuan, mirar la canasta completa dice si, en promedio, nuestros productos se volvieron más caros o más baratos para el mundo.",
],
rel=["tipo-de-cambio-real", "tipo-de-cambio", "divisa", "regimen-cambiario"],
))

T.append(dict(
slug="carta-de-intencion", t="Carta de intención (FMI)", cat="estado", ic="✉️",
bcrp="Carta de intención", alias="carta de intención FMI acuerdo con el FMI programa económico",
corto="Es el documento en el que un gobierno le presenta al FMI las políticas económicas que se compromete a aplicar para recibir su apoyo.",
simple=[
r"Cuando un país pide un acuerdo al Fondo Monetario Internacional, el ministerio de Economía y el banco central firman una <strong>carta de intención</strong>. Allí explican la situación del país y las metas que piensan cumplir: déficit, inflación, reservas, reformas.",
r"El FMI usa esas metas para hacer seguimiento y, según cómo se cumplan, entrega o no los desembolsos acordados.",
],
ejemplo=[
r"En los años noventa, el Perú firmó varias cartas de intención con el FMI como parte de su programa de estabilización tras la hiperinflación.",
],
rel=["organismos-multilaterales", "politica-fiscal", "deficit-fiscal", "hiperinflacion"],
))

T.append(dict(
slug="cartera-pesada", t="Cartera pesada", cat="finanzas", ic="🪨",
bcrp="Cartera pesada", alias="cartera deficiente cartera dudosa cartera de alto riesgo créditos en pérdida",
corto="Son los préstamos de un banco que tienen alto riesgo de no ser pagados: los clasificados como deficientes, dudosos o pérdida.",
simple=[
r"Los bancos clasifican a sus deudores según cómo pagan: normal, con problemas potenciales, deficiente, dudoso y pérdida. La <strong>cartera pesada</strong> agrupa las tres últimas categorías.",
r"Es una medida más amplia que la <a href='cartera-morosa.html'>morosidad</a>, porque incluye créditos que quizá todavía no están vencidos pero cuyo deudor ya muestra serias dificultades. Por esos créditos, el banco debe hacer <a href='provisiones.html'>provisiones</a> más grandes.",
],
formula=dict(
tex=r"\begin{aligned}&\text{Ratio de cartera pesada}=\\&\frac{\text{Deficientes}+\text{Dudosos}+\text{Pérdida}}{\text{Créditos totales}}\times100\end{aligned}",
calculo=[r"\frac{6}{100}\times100=6\,\%"],
),
ejemplo=[
r"Si una caja tiene S/ 100 millones en créditos y S/ 6 millones están clasificados como deficientes, dudosos o pérdida, su ratio de cartera pesada es 6 %.",
],
rel=["cartera-morosa", "provisiones", "riesgo-de-credito", "central-de-riesgos"],
))

T.append(dict(
slug="cdo", t="CDO (obligación de deuda garantizada)", cat="mercados", ic="🧩",
bcrp="CDO", alias="collateralized debt obligation CDO tramos crisis financiera 2008",
corto="Es un título que agrupa muchas deudas (préstamos, bonos) y las reparte en tramos con distinto riesgo y rentabilidad.",
simple=[
r"Un CDO junta un paquete de deudas y vende títulos respaldados por ellas. Los pagos se reparten por <strong>tramos</strong>: el tramo «senior» cobra primero y es el más seguro; el último tramo cobra al final, asume las primeras pérdidas y por eso paga más.",
r"Es una forma de <a href='titulizacion.html'>titulización</a>. En la crisis de 2008, muchos CDO estaban llenos de <a href='hipotecas-subprime.html'>hipotecas subprime</a>: cuando esas hipotecas dejaron de pagarse, incluso tramos que parecían seguros perdieron valor.",
],
ejemplo=[
r"Si un CDO agrupa 1000 préstamos y 50 no se pagan, las pérdidas las absorbe primero el tramo más riesgoso; el tramo senior solo pierde si los impagos son muy grandes.",
],
rel=["titulizacion", "hipotecas-subprime", "calificacion-de-riesgo", "credit-default-swap"],
))

T.append(dict(
slug="censo", t="Censo", cat="bienestar", ic="🧑‍🤝‍🧑",
bcrp="Censo", alias="censo nacional INEI población vivienda censo agropecuario",
corto="Es el conteo completo de toda la población (o de todas las viviendas, empresas o chacras) de un país en una fecha determinada.",
simple=[
r"A diferencia de una encuesta, que pregunta solo a una muestra, un <strong>censo</strong> intenta llegar a <strong>todos</strong>. Por eso es caro y se hace cada varios años.",
r"Sus resultados sirven de base para casi todo: repartir recursos entre regiones, diseñar muestras de encuestas, calcular tasas de pobreza o planificar escuelas y hospitales. En el Perú, los censos nacionales los hace el INEI.",
],
ejemplo=[
r"Los Censos Nacionales de 2017 permitieron actualizar cuántas personas viven en cada distrito y cómo son sus viviendas, información que luego usan los ministerios y los gobiernos locales.",
],
rel=["pea", "pobreza-monetaria", "mapa-de-pobreza", "tasa-de-dependencia"],
))

T.append(dict(
slug="coeficiente-de-monetizacion", t="Coeficiente de monetización", cat="dinero", ic="💧",
bcrp="Coeficiente de monetización", alias="monetización liquidez sobre PBI profundidad financiera",
corto="Mide cuánto dinero o liquidez hay en la economía en relación con el tamaño de la economía (el PBI).",
simple=[
r"Se calcula dividiendo un agregado monetario (por ejemplo, la liquidez del sistema financiero) entre el <a href='pbi.html'>PBI</a>. Un coeficiente alto indica que la gente usa mucho el sistema financiero para guardar su dinero.",
r"Tras la hiperinflación de los ochenta, la monetización del Perú cayó mucho porque la gente huía de los soles. Con la estabilidad, el coeficiente ha ido subiendo, señal de mayor confianza en la moneda.",
],
formula=dict(
tex=r"\text{Monetización}=\frac{\text{Liquidez}}{\text{PBI}}\times100",
calculo=[r"\frac{450}{1000}\times100=45\,\%"],
),
ejemplo=[
r"Si la liquidez total es S/ 450 mil millones y el PBI es S/ 1 billón, el coeficiente de monetización es 45 %.",
],
rel=["agregados-monetarios", "liquidez", "bancarizacion", "dolarizacion"],
))

T.append(dict(
slug="coeficiente-deuda-pbi", t="Coeficiente deuda/PBI", cat="estado", ic="⚖️",
bcrp="Coeficiente deuda-PBI", alias="deuda sobre PBI ratio de endeudamiento sostenibilidad fiscal",
corto="Es la deuda pública dividida entre el PBI: dice qué tan grande es la deuda del Estado comparada con todo lo que produce el país.",
simple=[
r"Una deuda de S/ 300 mil millones no dice mucho por sí sola. Al compararla con el <a href='pbi.html'>PBI</a> se ve si el país puede cargarla: una deuda del 30 % del PBI es mucho más manejable que una del 100 %.",
r"El coeficiente sube si el Estado tiene <a href='deficit-fiscal.html'>déficit</a> o si la economía crece poco, y baja si crece rápido o hay superávit. Las agencias de <a href='calificacion-de-riesgo.html'>calificación</a> lo miran con atención.",
],
formula=dict(
tex=r"\text{Deuda/PBI}=\frac{\text{Deuda pública}}{\text{PBI nominal}}\times100",
calculo=[r"\frac{330}{1100}\times100=30\,\%"],
),
ejemplo=[
r"Si la deuda pública es S/ 330 mil millones y el PBI nominal es S/ 1.1 billones, la deuda equivale al 30 % del PBI.",
],
rel=["deuda-publica", "deficit-fiscal", "pbi-nominal-y-real", "grado-de-inversion"],
))

T.append(dict(
slug="covenant", t="Covenant (cláusula de resguardo)", cat="finanzas", ic="📜",
bcrp="Covenant", alias="covenant resguardo financiero cláusula restrictiva condiciones del préstamo",
corto="Es una condición que el deudor acepta cumplir mientras tenga el préstamo, como no endeudarse de más o mantener ciertos indicadores.",
simple=[
r"Al prestar a una empresa o comprar sus bonos, los acreedores piden <strong>covenants</strong>: compromisos como no pasar de cierto nivel de deuda, mantener una liquidez mínima o no vender activos importantes sin permiso.",
r"Si la empresa incumple un covenant, el acreedor puede exigir el pago anticipado o renegociar condiciones. Así se protege del riesgo de que la empresa cambie de comportamiento después de recibir el dinero.",
],
ejemplo=[
r"Un banco presta a una empresa con la condición de que su deuda no supere tres veces su utilidad operativa anual. Si la empresa se endeuda más allá de ese límite, el banco puede pedir el pago del préstamo.",
],
rel=["bono-corporativo", "apalancamiento", "riesgo-de-credito", "garantia"],
))

T.append(dict(
slug="creadores-de-mercado", t="Creadores de mercado", cat="mercados", ic="🛠️",
bcrp="Creadores de mercados", alias="market makers creadores de mercado bonos soberanos liquidez",
corto="Son entidades que se comprometen a comprar y vender ciertos títulos de forma continua, para que siempre haya con quién negociar.",
simple=[
r"Un mercado funciona mejor si siempre hay alguien dispuesto a comprar y vender. Los <strong>creadores de mercado</strong> publican precios de compra y de venta y cumplen esas órdenes, lo que da <a href='liquidez.html'>liquidez</a> al mercado.",
r"En el Perú, el Ministerio de Economía tiene un programa de creadores de mercado: un grupo de bancos que participa en las subastas de <a href='bono-soberano.html'>bonos soberanos</a> y los negocia en el mercado secundario.",
],
ejemplo=[
r"Si un fondo de pensiones quiere vender bonos soberanos, puede venderlos a un creador de mercado aunque en ese momento no aparezca otro comprador.",
],
rel=["bono-soberano", "mercado-primario-y-secundario", "liquidez", "subastas"],
))

T.append(dict(
slug="credit-default-swap", t="Credit default swap (CDS)", cat="mercados", ic="🛡️",
bcrp="Credit default Swap", alias="CDS seguro contra impago swap de incumplimiento crediticio riesgo soberano",
corto="Es un contrato que funciona como un seguro contra el impago de una deuda: quien lo compra paga una prima y recibe una compensación si el deudor no paga.",
simple=[
r"El comprador de un CDS paga cada año un porcentaje (la prima). Si la empresa o el país de referencia incumple sus pagos, el vendedor del CDS cubre la pérdida.",
r"Por eso la prima del CDS sirve como termómetro del <a href='riesgo-pais.html'>riesgo país</a>: si sube, el mercado cree que es más probable un impago. Se mide en <a href='puntos-basicos.html'>puntos básicos</a>.",
],
ejemplo=[
r"Si el CDS a cinco años de un país cuesta 80 puntos básicos, asegurar 10 millones de dólares de su deuda cuesta 80 mil dólares al año.",
],
rel=["riesgo-pais", "swaps", "riesgo-de-credito", "puntos-basicos"],
))

T.append(dict(
slug="credito-suplementario", t="Crédito suplementario", cat="estado", ic="➕",
bcrp="Crédito suplementario", alias="ampliación presupuestal crédito suplementario Congreso presupuesto",
corto="Es un aumento del presupuesto público aprobado durante el año, cuando aparecen gastos que no estaban previstos.",
simple=[
r"El <a href='presupuesto-publico.html'>presupuesto</a> se aprueba antes de que empiece el año. Si luego surgen necesidades nuevas, como un desastre natural, el Ejecutivo puede pedir al Congreso un <strong>crédito suplementario</strong>.",
r"Para aprobarlo debe indicar de dónde saldrá el dinero: mayores ingresos, saldos de años anteriores o nueva deuda.",
],
ejemplo=[
r"Después de unas lluvias intensas, el Congreso aprueba un crédito suplementario para financiar la reconstrucción de puentes y carreteras.",
],
rel=["presupuesto-publico", "politica-fiscal", "gasto-corriente-y-de-capital", "deficit-fiscal"],
))

T.append(dict(
slug="cuasidinero", t="Cuasidinero", cat="dinero", ic="💦",
bcrp="Cuasidinero", alias="cuasidinero depósitos de ahorro depósitos a plazo dinero en sentido amplio",
corto="Son activos financieros que casi funcionan como dinero porque se pueden convertir en efectivo rápido, como los depósitos de ahorro y a plazo.",
simple=[
r"No puedes pagar en la tienda con un depósito a plazo, pero puedes convertirlo en efectivo con relativa facilidad. Por eso a estos depósitos se les llama <strong>cuasidinero</strong>: «casi dinero».",
r"El dinero en sentido estricto incluye el efectivo y los depósitos a la vista. Si a eso se le suma el cuasidinero, se obtiene la <a href='liquidez.html'>liquidez</a> en sentido amplio, uno de los <a href='agregados-monetarios.html'>agregados monetarios</a>.",
],
ejemplo=[
r"Tu cuenta de ahorros y tu depósito a plazo fijo forman parte del cuasidinero; los billetes de tu billetera, no.",
],
rel=["agregados-monetarios", "deposito-de-ahorro", "deposito-a-plazo", "dinero"],
))

T.append(dict(
slug="cuenta-financiera", t="Cuenta financiera", cat="comercio", ic="🔃",
bcrp="Cuenta financiera", alias="cuenta financiera balanza de pagos flujos de capital inversión extranjera",
corto="Es la parte de la balanza de pagos que registra las inversiones y los préstamos que entran y salen del país.",
simple=[
r"La <a href='balanza-de-pagos.html'>balanza de pagos</a> tiene dos grandes partes. La <a href='balanza-en-cuenta-corriente.html'>cuenta corriente</a> registra comercio, rentas y transferencias; la <strong>cuenta financiera</strong> registra cómo se financia: inversión extranjera directa, compra de acciones y bonos, y préstamos.",
r"Si un país tiene déficit en cuenta corriente, necesita que entren capitales por la cuenta financiera para cubrirlo.",
],
ejemplo=[
r"Cuando una minera extranjera trae dólares para construir una mina en el Perú, ese ingreso se registra en la cuenta financiera como inversión extranjera directa.",
],
rel=["balanza-de-pagos", "balanza-en-cuenta-corriente", "inversion-extranjera-directa", "errores-y-omisiones"],
))

T.append(dict(
slug="efecto-hoja-de-balance", t="Efecto hoja de balance", cat="finanzas", ic="📒",
bcrp="Efecto hoja de balance", alias="efecto balance descalce cambiario deuda en dólares depreciación",
corto="Es el daño que sufren familias y empresas endeudadas en dólares cuando el sol se deprecia, porque su deuda en soles se vuelve más grande.",
simple=[
r"Si ganas en soles pero debes en dólares, una subida del dólar hace que tu deuda, medida en soles, crezca de golpe, aunque tus ingresos sigan iguales. Eso empeora tu <a href='balance-general.html'>balance</a>.",
r"Por este efecto, en economías con mucha <a href='dolarizacion.html'>dolarización</a> una depreciación fuerte puede provocar impagos y frenar el crédito. Es una de las razones por las que el BCRP evita saltos bruscos del tipo de cambio.",
],
ejemplo=[
r"Una empresa debe 100 mil dólares. Con el dólar a S/ 3.50, la deuda equivale a S/ 350 mil; si el dólar sube a S/ 4.00, pasa a S/ 400 mil, sin haber pedido un sol más.",
],
rel=["descalce-de-monedas", "dolarizacion", "miedo-a-flotar", "riesgo-cambiario"],
))

T.append(dict(
slug="embi", t="EMBI (índice de bonos de mercados emergentes)", cat="mercados", ic="🌎",
bcrp="EMBI+ Paises emergentes", alias="EMBI EMBIG spread soberano JP Morgan riesgo país",
corto="Es un índice elaborado por JP Morgan que mide el rendimiento de los bonos en dólares de países emergentes; su diferencial es la medida más usada del riesgo país.",
simple=[
r"El EMBI compara lo que pagan los bonos en dólares de un país emergente con lo que pagan los bonos del Tesoro de Estados Unidos. Esa diferencia, en <a href='puntos-basicos.html'>puntos básicos</a>, es el <strong>spread</strong>.",
r"Cuanto más alto el spread, más interés exigen los inversionistas para prestarle al país, porque lo ven más riesgoso. Por eso las noticias sobre el <a href='riesgo-pais.html'>riesgo país</a> del Perú suelen citar el EMBIG.",
],
formula=dict(
tex=r"\begin{aligned}\text{Spread}={}&(\text{Rend. bono emergente}\\&-\text{Rend. bono de EE. UU.})\times100\end{aligned}",
calculo=[r"(5.6-4.2)\times100=140\ \text{puntos básicos}"],
),
ejemplo=[
r"Si los bonos del Perú en dólares rinden 5.6 % y los del Tesoro de Estados Unidos del mismo plazo rinden 4.2 %, el spread es de 140 puntos básicos.",
],
rel=["riesgo-pais", "puntos-basicos", "bono-soberano", "economias-emergentes"],
))

T.append(dict(
slug="empleo-formal-e-informal", t="Empleo formal e informal", cat="trabajo", ic="🪪",
bcrp="Empleo formal", alias="empleo formal empleo informal planilla seguridad social trabajador informal",
corto="El empleo formal es el que está registrado y da derechos laborales (seguro, pensión, beneficios); el informal no cumple esos registros.",
simple=[
r"Un trabajo es <strong>formal</strong> cuando el trabajador está en planilla o registrado, aporta a un sistema de pensiones y tiene seguro de salud. Es <strong>informal</strong> cuando falta esa protección, aunque la empresa pague impuestos.",
r"En el Perú, la mayor parte de los trabajadores tiene empleo informal. Eso significa menos acceso a <a href='cts.html'>CTS</a>, <a href='gratificacion.html'>gratificaciones</a> y pensión, y más vulnerabilidad ante enfermedades o crisis.",
],
ejemplo=[
r"Una cajera en planilla de un supermercado tiene empleo formal. Un ayudante de taller que trabaja sin contrato ni seguro tiene empleo informal.",
],
rel=["informalidad", "pea", "subempleo", "afp-y-onp"],
))

T.append(dict(
slug="errores-y-omisiones", t="Errores y omisiones netos", cat="comercio", ic="❔",
bcrp="Errores y omisiones", alias="errores y omisiones balanza de pagos partida de ajuste capitales no registrados",
corto="Es una partida de la balanza de pagos que recoge la diferencia entre lo que se registró y lo que debería cuadrar, por datos incompletos o errores.",
simple=[
r"En teoría, la <a href='balanza-de-pagos.html'>balanza de pagos</a> siempre debe sumar cero, porque cada operación tiene dos lados. En la práctica, los datos vienen de muchas fuentes y no todo se registra a tiempo.",
r"La diferencia que queda se anota como <strong>errores y omisiones</strong>. Si es grande y persistente, puede indicar capitales que entran o salen sin registrarse.",
],
ejemplo=[
r"Si las exportaciones registradas en aduanas no coinciden con los dólares que entran por el sistema financiero, parte de esa diferencia aparece en errores y omisiones.",
],
rel=["balanza-de-pagos", "cuenta-financiera", "balanza-en-cuenta-corriente", "reservas-internacionales"],
))

T.append(dict(
slug="expectativas-adaptativas", t="Expectativas adaptativas", cat="precios", ic="🔭",
bcrp="Expectativas adaptativas", alias="expectativas adaptativas inflación pasada aprendizaje",
corto="Es la idea de que la gente predice el futuro mirando lo que pasó antes, y corrige poco a poco cuando se equivoca.",
simple=[
r"Con <strong>expectativas adaptativas</strong>, si la inflación fue 5 % el año pasado, la gente espera algo parecido este año. Si se equivoca, ajusta su predicción solo en parte.",
r"Esta visión explica por qué la inflación puede ser «pegajosa»: si todos esperan que siga alta, piden aumentos y suben precios. Se contrasta con las <a href='expectativas-racionales.html'>expectativas racionales</a>, que usan toda la información disponible.",
],
formula=dict(
tex=r"\pi^{e}_{t}=\pi^{e}_{t-1}+\lambda\,(\pi_{t-1}-\pi^{e}_{t-1})",
donde=[(r"\pi^{e}", "inflación esperada"), (r"\pi", "inflación observada"), (r"\lambda", "rapidez del ajuste, entre 0 y 1")],
calculo=[r"3+0.5\times(5-3)=4\,\%"],
),
ejemplo=[
r"Una persona esperaba 3 % de inflación, pero fue 5 %. Si corrige la mitad de su error (\(\lambda=0.5\)), para el próximo año esperará 4 %.",
],
rel=["expectativas-racionales", "expectativas", "inflacion", "meta-de-inflacion"],
))

T.append(dict(
slug="fianza", t="Fianza", cat="finanzas", ic="✍️",
bcrp="Fianza", alias="fiador carta fianza aval garantía personal",
corto="Es el compromiso de una persona o un banco de pagar la deuda u obligación de otro si este no cumple.",
simple=[
r"En una <strong>fianza</strong>, el fiador respalda a otra persona. Si el deudor no paga, el acreedor puede cobrarle al fiador.",
r"Las empresas usan mucho la <strong>carta fianza</strong> bancaria: el banco garantiza, por ejemplo, que la empresa cumplirá una obra pública. Si no cumple, el banco paga y luego le cobra a la empresa.",
],
ejemplo=[
r"Para alquilar un local, el dueño pide un fiador. Si el inquilino deja de pagar, el fiador tendrá que cubrir las rentas pendientes.",
],
ojo=["Ser fiador es asumir una deuda ajena: firma solo si podrías pagarla tú."],
rel=["garantia", "riesgo-de-credito", "linea-de-credito", "credito-documentario"],
))

T.append(dict(
slug="filial-y-sucursal", t="Filial y sucursal", cat="finanzas", ic="🏢",
bcrp="Filial", alias="filial sucursal subsidiaria casa matriz",
corto="Una filial es una empresa con personería propia controlada por otra; una sucursal es una oficina de la misma empresa en otro lugar, sin personería propia.",
simple=[
r"Una <strong>filial</strong> (o subsidiaria) es una empresa distinta, con su propia contabilidad y responsabilidad legal, pero cuya mayoría de acciones pertenece a otra empresa, la matriz.",
r"Una <strong>sucursal</strong> es solo una extensión de la misma empresa: no es una persona jurídica aparte, así que la matriz responde directamente por sus deudas.",
],
ejemplo=[
r"Un banco extranjero puede operar en el Perú creando una filial peruana (una empresa local con su propio capital) o abriendo una sucursal que depende directamente de la casa matriz.",
],
rel=["empresa-holding", "inversion-extranjera-directa", "fusion-y-adquisicion", "banca-offshore"],
))

T.append(dict(
slug="fondo-de-pensiones", t="Fondo de pensiones", cat="finanzas", ic="👵",
bcrp="Fondo de pensiones", alias="fondo de pensiones AFP tipos de fondo 0 1 2 3 jubilación",
corto="Es el dinero que se acumula con los aportes de los trabajadores y que se invierte para pagar sus pensiones cuando se jubilen.",
simple=[
r"Cada mes, una parte del sueldo de los afiliados a una <a href='afp-y-onp.html'>AFP</a> va a su cuenta individual. Las AFP juntan esos aportes en <strong>fondos de pensiones</strong> y los invierten en bonos, acciones y otros activos.",
r"En el Perú hay varios tipos de fondo según el riesgo: desde el fondo 0, muy conservador, hasta el fondo 3, que invierte más en acciones y puede subir o bajar más.",
],
ejemplo=[
r"Una persona joven puede elegir un fondo más arriesgado porque tiene muchos años para recuperarse de las caídas; alguien cercano a jubilarse suele preferir uno más estable.",
],
rel=["afp-y-onp", "rentabilidad", "renta-fija-y-variable", "bono-de-reconocimiento"],
))

T.append(dict(
slug="hora-hombre", t="Hora hombre", cat="trabajo", ic="⏱️",
bcrp="Hora hombre", alias="horas hombre horas trabajadas productividad por hora",
corto="Es la unidad que mide el trabajo de una persona durante una hora; sirve para calcular cuánto trabajo requiere una tarea o cuánto se produce por hora.",
simple=[
r"Si una obra necesita 400 <strong>horas hombre</strong>, puede hacerla una persona en 400 horas o diez personas en 40 horas.",
r"Dividir la producción entre las horas hombre da la <a href='productividad.html'>productividad</a> por hora, una medida clave para comparar empresas y países.",
],
formula=dict(
tex=r"\text{Productividad por hora}=\frac{\text{Producción}}{\text{Horas hombre}}",
calculo=[r"\frac{2000}{400}=5\ \text{unidades por hora}"],
),
ejemplo=[
r"Un taller fabrica 2000 sillas en un mes con 400 horas hombre: produce 5 sillas por hora hombre.",
],
rel=["productividad", "pea", "remuneracion-minima-vital", "subempleo"],
))

T.append(dict(
slug="inflacion-no-subyacente", t="Inflación no subyacente", cat="precios", ic="🌪️",
bcrp="Inflación no subyacente", alias="inflación no subyacente componentes volátiles alimentos combustibles",
corto="Es la parte de la inflación que viene de precios muy volátiles, como algunos alimentos, combustibles y tarifas, que suben y bajan por choques pasajeros.",
simple=[
r"El IPC se divide en dos partes. La <a href='inflacion-subyacente.html'>inflación subyacente</a> mide la tendencia de los precios más estables. La <strong>no subyacente</strong> recoge los precios que saltan por factores puntuales: una helada que encarece la papa, una subida del petróleo o un ajuste de tarifas.",
r"El BCRP mira ambas, pero reacciona sobre todo a la tendencia. Si el salto viene solo de la parte no subyacente y es temporal, suele esperar a que se corrija sola.",
],
ejemplo=[
r"Si por el fenómeno El Niño sube fuerte el precio del limón, la inflación no subyacente aumenta; cuando se normaliza la cosecha, el efecto se revierte.",
],
herramienta=("Ver cómo cambian los precios por rubro", "../precios/"),
rel=["inflacion-subyacente", "inflacion-sin-alimentos-y-energia", "ipc", "choques-de-oferta-y-demanda"],
))

T.append(dict(
slug="ingreso-nacional-disponible", t="Ingreso nacional disponible", cat="produccion", ic="👛",
bcrp="Ingreso nacional disponible", alias="ingreso nacional disponible bruto INB transferencias remesas",
corto="Es el ingreso que realmente queda para consumir o ahorrar en el país, después de sumar o restar las rentas y transferencias con el exterior.",
simple=[
r"Se parte del PBI, se resta lo que se paga al exterior (por ejemplo, utilidades de empresas extranjeras) y se suma lo que se recibe (por ejemplo, <a href='remesas.html'>remesas</a> de peruanos que viven afuera).",
r"El resultado muestra mejor cuánto pueden gastar o ahorrar los residentes que el PBI solo, porque descuenta lo que sale del país y agrega lo que llega.",
],
formula=dict(
tex=r"\begin{aligned}\text{IND}={}&\text{PBI}+\text{Renta neta del exterior}\\&+\text{Transferencias netas del exterior}\end{aligned}",
calculo=[r"1000-40+20=980\ \text{mil millones}"],
),
ejemplo=[
r"Si el PBI es S/ 1000 mil millones, se pagan al exterior S/ 40 mil millones netos en utilidades e intereses y llegan S/ 20 mil millones netos en remesas, el ingreso nacional disponible es S/ 980 mil millones.",
],
rel=["ingreso-nacional", "pbi", "remesas", "cuentas-nacionales"],
))

T.append(dict(
slug="margen-financiero", t="Margen financiero", cat="finanzas", ic="↔️",
bcrp="Margen financiero", alias="margen financiero spread bancario ingresos financieros gastos financieros",
corto="Es la diferencia entre lo que un banco gana por los intereses de sus préstamos e inversiones y lo que paga por los intereses de los depósitos.",
simple=[
r"Un banco presta a una tasa (la <a href='tasa-de-interes-activa-y-pasiva.html'>tasa activa</a>) y paga a los ahorristas otra más baja (la tasa pasiva). La diferencia en soles es su <strong>margen financiero</strong>.",
r"Con ese margen el banco debe cubrir sus gastos, sus provisiones por créditos impagos y sus impuestos; lo que queda es su utilidad.",
],
formula=dict(
tex=r"\text{Margen financiero}=\text{Ingresos financieros}-\text{Gastos financieros}",
calculo=[r"120-45=75\ \text{millones}"],
),
ejemplo=[
r"Si una caja cobra S/ 120 millones al año en intereses de préstamos y paga S/ 45 millones en intereses de depósitos, su margen financiero bruto es S/ 75 millones.",
],
rel=["tasa-de-interes-activa-y-pasiva", "intermediacion-financiera", "provisiones", "rentabilidad"],
))

T.append(dict(
slug="margin-call", t="Margin call (llamada de margen)", cat="mercados", ic="📞",
bcrp="Margin call", alias="llamada de margen garantía adicional apalancamiento derivados",
corto="Es el aviso que recibe un inversionista para que deposite más garantía porque su inversión apalancada perdió valor.",
simple=[
r"Al invertir con dinero prestado o en <a href='contrato-de-futuro.html'>futuros</a>, se deja una garantía llamada margen. Si los precios se mueven en contra y el margen cae por debajo de un mínimo, el intermediario hace una <strong>margin call</strong>.",
r"Si el inversionista no repone el dinero a tiempo, el intermediario puede vender su posición, aunque sea con pérdida. En las crisis, muchas margin calls a la vez obligan a vender en masa y agravan las caídas.",
],
ejemplo=[
r"Compras acciones por 10 mil dólares, 5 mil con dinero propio y 5 mil prestados. Si las acciones caen a 7 mil, tu parte se reduce a 2 mil y el intermediario te pide depositar más garantía.",
],
rel=["apalancamiento", "contrato-de-futuro", "volatilidad", "garantia"],
))

T.append(dict(
slug="mercado-comun", t="Mercado común", cat="comercio", ic="🤲",
bcrp="Mercado común", alias="mercado común integración libre movilidad de factores",
corto="Es una etapa de integración en la que varios países eliminan aranceles entre ellos, tienen un arancel común frente a terceros y permiten que el trabajo y el capital circulen libremente.",
simple=[
r"La <a href='integracion-economica.html'>integración económica</a> avanza por etapas. Primero viene la <a href='zona-de-libre-comercio.html'>zona de libre comercio</a>; luego la <a href='union-aduanera.html'>unión aduanera</a>, con arancel externo común; y después el <strong>mercado común</strong>, que agrega la libre circulación de trabajadores y capitales.",
r"La siguiente etapa sería la unión económica, en la que se coordinan también las políticas económicas, y en algunos casos se adopta una moneda común.",
],
ejemplo=[
r"El Mercosur nació con el objetivo de formar un mercado común entre Argentina, Brasil, Paraguay y Uruguay, aunque todavía mantiene excepciones.",
],
rel=["integracion-economica", "union-aduanera", "zona-de-libre-comercio", "union-monetaria"],
))

T.append(dict(
slug="moratoria", t="Moratoria", cat="estado", ic="⏸️",
bcrp="Moratoria", alias="moratoria de deuda suspensión de pagos default cesación de pagos",
corto="Es la suspensión de los pagos de una deuda, ya sea por decisión del deudor o por acuerdo con los acreedores.",
simple=[
r"Un país o una empresa declara <strong>moratoria</strong> cuando deja de pagar, total o parcialmente, sus deudas. A veces es unilateral (impago) y otras veces se pacta con los acreedores para ganar tiempo.",
r"Una moratoria suele cerrar el acceso al crédito internacional y encarecer los préstamos futuros, porque los inversionistas exigen más interés para volver a prestar.",
],
ejemplo=[
r"En los años ochenta varios países de América Latina, incluido el Perú, limitaron o suspendieron el pago de su deuda externa; la normalización llegó más tarde, en el Perú a través del <a href='plan-brady.html'>Plan Brady</a>.",
],
rel=["deuda-externa", "plan-brady", "club-de-paris", "riesgo-pais"],
))

T.append(dict(
slug="posicion-larga-y-corta", t="Posición larga y corta", cat="mercados", ic="↕️",
bcrp="Posición larga", alias="posición larga posición corta long short venta en corto",
corto="Estar en posición larga es ganar si el precio sube; estar en posición corta es ganar si el precio baja.",
simple=[
r"Tienes una <strong>posición larga</strong> cuando compras algo (una acción, dólares) esperando que suba de precio.",
r"Tienes una <strong>posición corta</strong> cuando te comprometes a vender algo que no tienes, o vendes algo prestado, esperando que baje para recomprarlo más barato. Las pérdidas de una posición corta pueden ser muy grandes si el precio sube mucho.",
],
ejemplo=[
r"Si compras dólares a S/ 3.70 pensando que subirán, estás largo en dólares. Un banco que se comprometió a entregar dólares en un forward sin tenerlos está corto en dólares: gana si el dólar baja y pierde si sube.",
],
rel=["posicion-de-cambio", "contrato-forward", "volatilidad", "toma-de-ganancias"],
))

T.append(dict(
slug="posicion-de-cambio", t="Posición de cambio", cat="mercados", ic="💹",
bcrp="Posición de cambio", alias="posición global de cambio posición de cambio del BCRP sobrecompra sobreventa",
corto="Es la diferencia entre los activos y los pasivos en moneda extranjera de un banco: muestra cuánto gana o pierde si el dólar sube.",
simple=[
r"Si un banco tiene más activos que pasivos en dólares, está <strong>sobrecomprado</strong>: gana si el dólar sube. Si tiene más pasivos, está <strong>sobrevendido</strong>: pierde si el dólar sube.",
r"Los supervisores ponen límites a esta posición para que los bancos no apuesten demasiado al tipo de cambio. El BCRP también publica su propia posición de cambio, que muestra cuántos dólares son de su libre disponibilidad.",
],
formula=dict(
tex=r"\text{Posición de cambio}=\text{Activos en ME}-\text{Pasivos en ME}",
calculo=[r"800-750=50\ \text{millones de dólares (sobrecomprado)}"],
),
ejemplo=[
r"Un banco tiene 800 millones de dólares en activos y 750 millones en pasivos en dólares: su posición es de 50 millones de dólares sobrecomprada.",
],
rel=["posicion-larga-y-corta", "riesgo-cambiario", "descalce-de-monedas", "reservas-internacionales"],
))

T.append(dict(
slug="precio-al-productor", t="Precio al productor", cat="precios", ic="🚜",
bcrp="Precio al productor", alias="precio en chacra precio en fábrica precios al productor",
corto="Es el precio que recibe quien produce un bien, antes de sumar transporte, márgenes del comercio e impuestos.",
simple=[
r"Entre la chacra o la fábrica y tu mesa hay transporte, mayoristas, minoristas e impuestos. El <strong>precio al productor</strong> es el que se paga en el primer eslabón de esa cadena.",
r"Seguirlo ayuda a anticipar la inflación: si suben los precios al productor, es probable que luego suban los <a href='precios-al-por-mayor.html'>precios al por mayor</a> y los de consumo.",
],
ejemplo=[
r"Un agricultor puede vender el kilo de papa a S/ 0.80 en su chacra, mientras que en un mercado de Lima se vende a S/ 2.50. La diferencia cubre transporte, mermas y márgenes de los comerciantes.",
],
herramienta=("Ver precios de alimentos y materias primas", "../precios/"),
rel=["precios-al-por-mayor", "ipc", "inflacion", "materias-primas"],
))

T.append(dict(
slug="promedio-movil", t="Promedio móvil", cat="precios", ic="📈",
bcrp="Promedio móvil", alias="media móvil promedio de 12 meses suavizar series",
corto="Es un promedio que se recalcula cada periodo con los últimos datos, para suavizar los altibajos de una serie y ver mejor su tendencia.",
simple=[
r"Por ejemplo, el promedio móvil de 3 meses de marzo usa enero, febrero y marzo; el de abril usa febrero, marzo y abril. Cada mes entra un dato nuevo y sale el más antiguo.",
r"Así se reducen los saltos puntuales y se aprecia mejor si una variable, como la inflación o la producción, tiende a subir o a bajar.",
],
formula=dict(
tex=r"PM_t=\frac{x_t+x_{t-1}+\cdots+x_{t-n+1}}{n}",
donde=[(r"x_t", "dato del periodo t"), (r"n", "número de periodos que se promedian")],
calculo=[r"\frac{4+6+5}{3}=5"],
),
ejemplo=[
r"Si las ventas de una tienda fueron 4, 6 y 5 mil soles en los últimos tres meses, su promedio móvil de tres meses es 5 mil soles.",
],
rel=["desestacionalizacion", "indicador-adelantado", "volatilidad", "inflacion-subyacente"],
))

T.append(dict(
slug="quiebra-bancaria", t="Quiebra bancaria", cat="finanzas", ic="🏚️",
bcrp="Quiebra bancaria", alias="quiebra de banco liquidación bancaria corrida bancaria fondo de seguro de depósitos",
corto="Es cuando un banco no puede devolver el dinero a sus depositantes ni pagar sus deudas, y el supervisor lo interviene y liquida.",
simple=[
r"Un banco puede quebrar por perder demasiado en créditos impagos o por una <strong>corrida</strong>: muchos depositantes retiran su dinero a la vez y el banco no tiene suficiente efectivo.",
r"En el Perú, la <a href='sbs.html'>SBS</a> interviene a la entidad con problemas, y el Fondo de Seguro de Depósitos devuelve a las personas sus depósitos hasta un monto máximo.",
],
ejemplo=[
r"Si una entidad supervisada quiebra, un ahorrista con un depósito cubierto por el Fondo de Seguro de Depósitos recupera su dinero hasta el tope vigente, aunque la entidad desaparezca.",
],
ojo=["Ahorra solo en entidades supervisadas por la SBS y que formen parte del Fondo de Seguro de Depósitos."],
rel=["sbs", "riesgo-de-liquidez", "insolvencia", "ratio-de-capital-global"],
))

T.append(dict(
slug="renta-de-factores", t="Renta de factores", cat="comercio", ic="↩️",
bcrp="Renta de factores", alias="renta de factores ingreso primario utilidades intereses balanza de pagos",
corto="Son los ingresos que un país paga o recibe del exterior por el uso de capital o trabajo: utilidades, dividendos e intereses.",
simple=[
r"Cuando una empresa extranjera gana dinero en el Perú y envía utilidades a su casa matriz, o cuando el Estado paga intereses de su deuda externa, eso es <strong>renta de factores</strong> pagada al exterior.",
r"Forma parte de la <a href='balanza-en-cuenta-corriente.html'>cuenta corriente</a>. En el Perú suele ser negativa, porque hay mucha inversión extranjera en minería que genera utilidades para sus dueños de afuera.",
],
ejemplo=[
r"Si una minera extranjera gana 500 millones de dólares en el Perú y transfiere 300 millones como dividendos a su matriz, esos 300 millones se registran como renta de factores pagada.",
],
rel=["balanza-en-cuenta-corriente", "ingreso-nacional", "inversion-extranjera-directa", "dividendo"],
))

T.append(dict(
slug="renta-vitalicia", t="Renta vitalicia", cat="finanzas", ic="♾️",
bcrp="Renta Familiar Vitalicia", alias="renta vitalicia renta familiar vitalicia seguro de pensión jubilación AFP",
corto="Es una pensión que una compañía de seguros paga de por vida al jubilado y, al fallecer, a sus beneficiarios, a cambio de su fondo de pensiones.",
simple=[
r"Al jubilarse, un afiliado a una AFP puede entregar su fondo a una aseguradora, que se compromete a pagarle una pensión mensual <strong>mientras viva</strong>. En la modalidad <strong>familiar</strong>, al morir la pensión pasa a su cónyuge o a sus hijos, según las reglas.",
r"La ventaja es la seguridad: la pensión no se acaba aunque el jubilado viva muchos años. A cambio, el dinero entregado ya no forma parte de la herencia.",
],
ejemplo=[
r"Una jubilada contrata una renta vitalicia familiar y recibe una pensión cada mes; si fallece, su esposo sigue recibiendo una pensión de sobrevivencia.",
],
rel=["afp-y-onp", "fondo-de-pensiones", "compania-de-seguros", "valor-presente-y-valor-futuro"],
))

T.append(dict(
slug="retroarrendamiento-financiero", t="Retroarrendamiento financiero (leaseback)", cat="finanzas", ic="🔁",
bcrp="Retroarrendamiento financiero", alias="leaseback lease back venta con arrendamiento posterior",
corto="Es cuando una empresa vende un bien suyo a un banco y luego lo alquila con opción de recomprarlo, para conseguir liquidez sin dejar de usarlo.",
simple=[
r"La empresa necesita efectivo pero no quiere dejar de usar, por ejemplo, su fábrica. Entonces la vende a una entidad financiera y se la vuelve a <a href='arrendamiento-financiero.html'>arrendar</a> pagando cuotas.",
r"Al final del contrato puede recomprarla por un precio pactado. En la práctica funciona como un préstamo con el bien como garantía.",
],
ejemplo=[
r"Una empresa vende su planta a un banco por S/ 5 millones, la sigue usando y paga cuotas mensuales durante cinco años; al final, la recompra por un monto simbólico.",
],
rel=["arrendamiento-financiero", "capital-de-trabajo", "garantia", "liquidez"],
))

T.append(dict(
slug="riesgo-operacional", t="Riesgo operacional", cat="finanzas", ic="⚙️",
bcrp="Riesgo operacional", alias="riesgo operativo fallas de sistemas fraude errores humanos",
corto="Es el riesgo de perder dinero por fallas internas: errores de personas, procesos o sistemas, fraudes o eventos externos como desastres.",
simple=[
r"Un banco no solo puede perder porque un cliente no le pague (<a href='riesgo-de-credito.html'>riesgo de crédito</a>) o porque cambien los precios (<a href='riesgo-de-mercado.html'>riesgo de mercado</a>). También puede perder por una caída de sus sistemas, un fraude interno o un error al registrar una operación.",
r"Ese es el <strong>riesgo operacional</strong>. Los supervisores exigen que las entidades lo midan, lo controlen y tengan capital para cubrirlo.",
],
ejemplo=[
r"Si una falla informática deja a un banco sin poder procesar pagos durante un día, las compensaciones y multas que debe asumir son pérdidas por riesgo operacional.",
],
rel=["riesgo-de-credito", "riesgo-de-mercado", "ratio-de-capital-global", "sbs"],
))

T.append(dict(
slug="rueda-de-bolsa", t="Rueda de bolsa", cat="mercados", ic="🎡",
bcrp="Rueda de bolsa", alias="rueda de bolsa sesión bursátil negociación en bolsa",
corto="Es la sesión de negociación de la bolsa de valores, el horario en el que se compran y venden acciones y bonos.",
simple=[
r"Durante la <strong>rueda de bolsa</strong>, las sociedades agentes de bolsa ingresan las órdenes de compra y venta de sus clientes, y el sistema las empareja cuando coinciden en precio.",
r"El nombre viene de cuando los operadores se reunían físicamente en el recinto de la bolsa. Hoy la negociación es electrónica, pero se sigue usando la expresión.",
],
ejemplo=[
r"Si das una orden de compra de acciones por la noche, se ejecutará durante la siguiente rueda de bolsa, si alguien vende al precio que pediste.",
],
rel=["bolsa-de-valores", "accion", "indices-bursatiles", "cavali"],
))

T.append(dict(
slug="sistema-lbtr", t="Sistema LBTR", cat="dinero", ic="⚡",
bcrp="Sistema de Liquidación Bruta en Tiempo Real - Sistema LBTR", alias="LBTR liquidación bruta en tiempo real transferencias interbancarias BCRP",
corto="Es el sistema del BCRP por el que los bancos se transfieren grandes montos entre sí, uno por uno y al instante.",
simple=[
r"Cada banco tiene una cuenta en el BCRP. En el <strong>LBTR</strong>, cada transferencia se liquida de inmediato y por su monto completo («bruto»), sin esperar a compensarla con otras.",
r"Por eso es un sistema muy seguro para pagos grandes o urgentes: si el banco tiene fondos, el dinero llega en el momento. Es una pieza central del <a href='sistema-de-pagos.html'>sistema de pagos</a> del país.",
],
ejemplo=[
r"Cuando una empresa paga una compra millonaria a otra con cuenta en otro banco, la transferencia entre ambos bancos puede liquidarse por el LBTR en segundos.",
],
rel=["sistema-de-pagos", "camara-de-compensacion", "bcrp", "encaje-bancario"],
))

T.append(dict(
slug="sobrecanon", t="Sobrecanon", cat="estado", ic="🛢️",
bcrp="Sobrecanon", alias="sobrecanon petrolero regiones petroleras",
corto="Es un ingreso adicional al canon que reciben algunas regiones productoras de petróleo, como un porcentaje del valor de lo extraído.",
simple=[
r"El <a href='canon.html'>canon</a> reparte parte de los impuestos que pagan las empresas que explotan recursos naturales. El <strong>sobrecanon</strong> petrolero es un monto extra, fijado por leyes específicas, para regiones como Loreto, Ucayali, Piura o Tumbes.",
r"Como depende del precio y de la producción de petróleo, estos ingresos pueden variar mucho de un año a otro.",
],
ejemplo=[
r"Si cae la producción de petróleo de una región, también baja lo que recibe por canon y sobrecanon, y sus gobiernos locales tienen menos dinero para obras.",
],
rel=["canon", "regalias", "materias-primas", "foncomun"],
))

T.append(dict(
slug="sobregiro", t="Sobregiro", cat="finanzas", ic="🔻",
bcrp="Sobregiro", alias="sobregiro bancario descubierto cuenta corriente",
corto="Es cuando el banco te permite gastar más dinero del que tienes en tu cuenta corriente, como un préstamo automático y de muy corto plazo.",
simple=[
r"Si tu cuenta corriente tiene S/ 1000 y giras un cheque por S/ 1500, el banco puede cubrir la diferencia: es un <strong>sobregiro</strong>.",
r"Es cómodo para una emergencia, pero suele tener una tasa de interés alta y debe pagarse pronto.",
],
ejemplo=[
r"Una empresa tiene un sobregiro aprobado de S/ 20 mil para pagar a sus proveedores mientras le pagan sus clientes. Lo usa unos días y lo devuelve con intereses.",
],
ojo=["Pregunta la tasa efectiva anual del sobregiro antes de usarlo: suele ser de las más altas."],
rel=["linea-de-credito", "cheque", "tea", "capital-de-trabajo"],
))

T.append(dict(
slug="toma-de-ganancias", t="Toma de ganancias", cat="mercados", ic="💰",
bcrp="Toma de ganancias", alias="toma de utilidades realización de ganancias corrección bursátil",
corto="Es cuando los inversionistas venden activos que subieron de precio para asegurar lo que ganaron, lo que suele hacer bajar el precio por un tiempo.",
simple=[
r"Después de una subida fuerte de una acción o del oro, muchos inversionistas venden para «llevarse» la ganancia. Esa ola de ventas presiona el precio a la baja.",
r"Por eso, en las noticias es común leer que «la bolsa cayó por toma de ganancias»: no necesariamente hay malas noticias, sino gente cobrando lo que ya ganó.",
],
ejemplo=[
r"Si una acción subió 20 % en un mes y luego baja 3 % en un día sin noticias nuevas, los analistas suelen atribuirlo a toma de ganancias.",
],
rel=["bolsa-de-valores", "posicion-larga-y-corta", "volatilidad", "indices-bursatiles"],
))

T.append(dict(
slug="union-aduanera", t="Unión aduanera", cat="comercio", ic="🛃",
bcrp="Unión Aduanera", alias="unión aduanera arancel externo común integración",
corto="Es un acuerdo en el que varios países eliminan los aranceles entre ellos y además cobran un mismo arancel a los productos que vienen de fuera.",
simple=[
r"En una <a href='zona-de-libre-comercio.html'>zona de libre comercio</a>, cada país mantiene sus propios aranceles con el resto del mundo. En una <strong>unión aduanera</strong>, en cambio, todos aplican un <strong>arancel externo común</strong>.",
r"Así se evita que los productos de fuera entren por el país con el arancel más bajo para luego pasar al resto. Es un paso previo al <a href='mercado-comun.html'>mercado común</a>.",
],
ejemplo=[
r"La Unión Europea funciona como una unión aduanera: un producto chino paga el mismo arancel al entrar por Francia o por Alemania.",
],
rel=["zona-de-libre-comercio", "mercado-comun", "arancel", "integracion-economica"],
))

T.append(dict(
slug="utilidades-retenidas", t="Utilidades retenidas", cat="finanzas", ic="🐷",
bcrp="Utilidades no distribuidas", alias="utilidades no distribuidas utilidades acumuladas reinversión de utilidades resultados acumulados",
corto="Son las ganancias que una empresa decide no repartir como dividendos y guarda para reinvertir o reforzar su patrimonio.",
simple=[
r"Al cerrar el año, la empresa elige qué hacer con su utilidad neta: repartirla a los accionistas como <a href='dividendo.html'>dividendos</a> o <strong>retenerla</strong>.",
r"Las utilidades retenidas se suman al <a href='patrimonio.html'>patrimonio</a> y financian nuevas inversiones sin pedir préstamos. En la balanza de pagos, las que retienen las empresas extranjeras se registran como reinversión.",
],
formula=dict(
tex=r"\text{Utilidades retenidas}=\text{Utilidad neta}-\text{Dividendos}",
calculo=[r"10-4=6\ \text{millones}"],
),
ejemplo=[
r"Una empresa ganó S/ 10 millones, reparte S/ 4 millones en dividendos y retiene S/ 6 millones para comprar maquinaria.",
],
rel=["dividendo", "patrimonio", "estado-de-resultados", "inversion-extranjera-directa"],
))

T.append(dict(
slug="valor-intrinseco", t="Valor intrínseco", cat="mercados", ic="💎",
bcrp="Valor intrínseco", alias="valor intrínseco valor fundamental opción dentro del dinero",
corto="Es el valor «real» que se estima que tiene un activo según sus fundamentos; en una opción, es lo que se ganaría si se ejerciera hoy.",
simple=[
r"En acciones, el <strong>valor intrínseco</strong> es lo que vale la empresa según las ganancias futuras que se espera que genere, traídas a <a href='valor-presente-y-valor-futuro.html'>valor presente</a>. Si el precio en bolsa está por debajo, algunos inversionistas la consideran barata.",
r"En una <a href='opcion.html'>opción</a> de compra, es la diferencia entre el precio actual del activo y el precio de ejercicio, si es positiva; si no, es cero.",
],
formula=dict(
tex=r"\text{Valor intrínseco (call)}=\max(P-K,\ 0)",
donde=[(r"P", "precio actual del activo"), (r"K", "precio de ejercicio de la opción")],
calculo=[r"\max(120-100,\ 0)=20"],
),
ejemplo=[
r"Una opción de compra permite comprar una acción a 100 dólares y hoy la acción cotiza a 120: su valor intrínseco es 20 dólares.",
],
rel=["opcion", "valor-presente-y-valor-futuro", "accion", "van"],
))

T.append(dict(
slug="variacion-de-existencias", t="Variación de existencias", cat="produccion", ic="📦",
bcrp="Variación de existencias", alias="variación de inventarios existencias inventarios inversión bruta",
corto="Es el cambio en los inventarios de las empresas durante un periodo; en las cuentas nacionales forma parte de la inversión.",
simple=[
r"Si una empresa produce más de lo que vende, guarda la diferencia en su almacén: sus <strong>existencias</strong> aumentan. Si vende más de lo que produce, las existencias bajan.",
r"En el cálculo del PBI por el lado del gasto, esa variación se suma a la <a href='formacion-bruta-de-capital.html'>formación bruta de capital</a>, porque lo producido y no vendido también es parte de lo que el país produjo.",
],
formula=dict(
tex=r"\text{Variación de existencias}=\text{Inventario final}-\text{Inventario inicial}",
calculo=[r"130-100=30"],
),
ejemplo=[
r"Una fábrica empezó el año con 100 mil unidades en almacén y terminó con 130 mil. La variación de existencias, de 30 mil unidades, cuenta como inversión.",
],
rel=["formacion-bruta-de-capital", "pbi", "cuentas-nacionales", "inversion"],
))

T.append(dict(
slug="vix", t="VIX (índice del miedo)", cat="mercados", ic="😨",
bcrp="VIX", alias="VIX índice del miedo volatilidad implícita S&P 500 aversión al riesgo",
corto="Es un índice que mide cuánta volatilidad esperan los inversionistas en la bolsa de Estados Unidos en los próximos 30 días; sube cuando hay miedo.",
simple=[
r"El VIX se calcula con los precios de las <a href='opcion.html'>opciones</a> sobre el índice S&amp;P 500. Si los inversionistas pagan caro por protegerse de caídas, el VIX sube.",
r"Por eso se le llama el «índice del miedo». Cuando sube mucho, los capitales suelen salir de <a href='economias-emergentes.html'>economías emergentes</a> como el Perú, y las monedas y bolsas de esos países tienden a caer.",
],
ejemplo=[
r"En marzo de 2020, al inicio de la pandemia, el VIX se disparó a niveles récord mientras las bolsas del mundo se desplomaban.",
],
rel=["volatilidad", "opcion", "indices-bursatiles", "economias-emergentes"],
))
