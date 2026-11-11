# -*- coding: utf-8 -*-
# Términos del glosario (parte 3): primera tanda tomada de la lista del
# Glosario de Términos Económicos del BCRP (2011). Las definiciones están
# redactadas con palabras propias; el campo "bcrp" guarda el nombre exacto
# del término en ese glosario para citarlo como fuente.

T = []

T.append(dict(
slug="accion", t="Acción", cat="finanzas", ic="📜", bcrp="Acción",
alias="acciones accionista bolsa dividendos",
corto="Es una parte pequeña del capital de una empresa. Quien la compra se vuelve socio y puede recibir parte de las ganancias.",
simple=[
r"Cuando una empresa se forma como sociedad anónima, su capital se divide en muchas partes iguales llamadas <strong>acciones</strong>. Si compras una, eres <strong>accionista</strong>: dueño de una pequeña parte de la empresa.",
r"Ser accionista suele dar tres derechos: recibir una parte de las ganancias cuando la empresa las reparte (los <strong>dividendos</strong>), votar en la junta de accionistas y tener preferencia para comprar acciones nuevas. Si la empresa cierra, recibes una parte de lo que quede después de pagar las deudas.",
r"El precio de una acción sube o baja según cómo le va a la empresa y lo que esperan los inversionistas. Por eso las acciones son <strong>renta variable</strong>: no sabes de antemano cuánto ganarás.",
],
ejemplo=[
r"Muchas empresas grandes del Perú tienen acciones que se compran y venden en la Bolsa de Valores de Lima. Si compras 100 acciones a S/ 5 cada una y luego suben a S/ 6, tu inversión pasa de S/ 500 a S/ 600; si bajan a S/ 4, pierdes S/ 100.",
],
formula=dict(
tex=r"\text{Rentabilidad}=\frac{P_1-P_0+D}{P_0}\times 100",
donde=[(r"P_0", "precio al que compraste"), (r"P_1", "precio al que vendes"), (r"D", "dividendos recibidos")],
calculo=[r"\frac{6-5+0.20}{5}\times 100=24\ \%"],
),
rel=["bolsa-de-valores", "bono", "mercado-de-capitales", "fondo-mutuo"],
))

T.append(dict(
slug="amortizacion", t="Amortización", cat="finanzas", ic="🧩",
bcrp="Amortización", alias="pagar capital cuota principal",
corto="Es la parte de una cuota que sirve para devolver el dinero prestado (el capital), sin contar los intereses.",
simple=[
r"Cuando pagas un préstamo en cuotas, cada cuota tiene dos partes: los <strong>intereses</strong> (el costo del préstamo) y la <strong>amortización</strong> (lo que reduce tu deuda). Amortizar es, entonces, devolver poco a poco el capital.",
r"En el sistema de cuota fija, que usan casi todos los bancos, al inicio la mayor parte de la cuota son intereses y poco a poco la amortización crece. Por eso, si haces un <strong>prepago</strong> al principio, ahorras más intereses.",
],
ejemplo=[
r"Debes S/ 10 000 a una tasa de 2 % mensual y tu cuota es S/ 500. El primer mes pagas S/ 200 de intereses (2 % de 10 000) y amortizas S/ 300. Tu deuda baja a S/ 9700, así que el mes siguiente pagarás un poco menos de intereses y amortizarás un poco más.",
],
formula=dict(
tex=r"\text{Amortización}_k=\text{Cuota}-i\times\text{Saldo}_{k-1}",
donde=[(r"i", "tasa de interés del periodo"), (r"\text{Saldo}_{k-1}", "lo que debías antes de pagar la cuota k")],
calculo=[r"500-0.02\times 10\,000=300\ \text{soles}"],
),
rel=["tea", "tcea", "credito-hipotecario", "interes-compuesto"],
))

T.append(dict(
slug="apalancamiento", t="Apalancamiento", cat="finanzas", ic="🏋️",
bcrp="Apalancamiento", alias="leverage endeudamiento palanca financiera",
corto="Es usar dinero prestado para invertir más de lo que tienes. Puede aumentar tus ganancias, pero también tus pérdidas.",
simple=[
r"Apalancarse es como usar una palanca: con poco dinero propio mueves una inversión más grande, porque el resto es prestado. Si la inversión sale bien, ganas mucho en relación con lo que pusiste.",
r"El problema es que la deuda hay que pagarla igual. Si la inversión sale mal, las pérdidas también se multiplican y puedes quedarte sin poder pagar. Por eso la SBS limita cuánto pueden apalancarse los bancos.",
],
ejemplo=[
r"Compras un departamento de S/ 300 000 con S/ 60 000 tuyos y S/ 240 000 de un crédito hipotecario. Si el departamento sube 10 % (S/ 30 000), ganaste la mitad de lo que pusiste (sin contar intereses). Si baja 10 %, perdiste la mitad.",
],
formula=dict(
tex=r"\text{Apalancamiento}=\frac{\text{Activos}}{\text{Capital propio}}",
calculo=[r"\frac{300\,000}{60\,000}=5\ \text{veces}"],
),
rel=["credito-hipotecario", "accion", "tasa-de-interes", "costo-de-oportunidad"],
))

T.append(dict(
slug="arancel", t="Arancel", cat="comercio", ic="🛃",
bcrp="Arancel", alias="impuesto a la importacion derechos de aduana ad valorem",
corto="Es un impuesto que se cobra a los productos que entran de otro país (importaciones).",
simple=[
r"El arancel encarece los productos importados. Puede servir para que el Estado recaude dinero o para proteger a los productores nacionales de la competencia de fuera.",
r"Puede ser <strong>ad valorem</strong> (un porcentaje del valor del producto) o <strong>específico</strong> (un monto fijo por unidad, por ejemplo por kilo). En el Perú lo cobra la SUNAT en la aduana.",
r"Bajar aranceles abarata lo importado y favorece a los consumidores, pero puede golpear a los productores locales que compiten con esos productos. Los tratados de libre comercio suelen eliminar aranceles entre los países que los firman.",
],
ejemplo=[
r"Si una máquina importada vale US$ 1000 y tiene un arancel ad valorem de 6 %, en la aduana se pagan US$ 60 de arancel (además de otros impuestos, como el IGV).",
],
formula=dict(
tex=r"\text{Arancel ad valorem}=t\times\text{Valor en aduana}",
calculo=[r"0.06\times 1000=60\ \text{US\$}"],
),
rel=["balanza-comercial", "igv", "ventaja-comparativa", "bienes-transables-y-no-transables"],
))

T.append(dict(
slug="balanza-de-pagos", t="Balanza de pagos", cat="comercio", ic="🌐",
bcrp="Balanza de pagos", alias="cuenta corriente cuenta financiera reservas",
corto="Es el registro de todo el dinero que entra y sale de un país por comercio, inversiones, préstamos y transferencias con el resto del mundo.",
simple=[
r"La balanza de pagos es como el «estado de cuenta» de un país con el exterior en un periodo. Anota las exportaciones e importaciones, los pagos de intereses y utilidades, las remesas, las inversiones y los préstamos entre residentes y no residentes.",
r"Tiene dos grandes partes: la <a href=\"balanza-en-cuenta-corriente.html\">cuenta corriente</a> (comercio de bienes y servicios, renta y transferencias) y la <strong>cuenta financiera</strong> (inversiones y préstamos). Al final, la suma muestra cuánto cambiaron las <a href=\"reservas-internacionales.html\">reservas internacionales</a> del BCRP.",
r"En el Perú, por ley, el BCRP es el responsable de elaborar la balanza de pagos.",
],
ejemplo=[
r"Si un año entran muchos dólares por exportaciones de cobre e inversión extranjera, y salen menos por importaciones y pagos al exterior, la balanza de pagos tiene superávit y las reservas del BCRP suben.",
],
formula=dict(
tex=r"\Delta RIN=CC+CF+\text{Errores y omisiones}",
donde=[(r"\Delta RIN", "variación de las reservas internacionales netas"), (r"CC", "saldo de la cuenta corriente"), (r"CF", "saldo de la cuenta financiera (entradas netas de capitales)")],
),
ojo=["La forma exacta de presentar las cuentas cambia con los manuales del FMI; la idea general es la misma."],
rel=["balanza-en-cuenta-corriente", "balanza-comercial", "reservas-internacionales", "inversion-extranjera-directa", "remesas"],
))

T.append(dict(
slug="balanza-en-cuenta-corriente", t="Balanza en cuenta corriente", cat="comercio", ic="🧾",
bcrp="Balanza en cuenta corriente", alias="cuenta corriente deficit en cuenta corriente",
corto="Es la parte de la balanza de pagos que suma el comercio de bienes y servicios, la renta (intereses y utilidades) y las transferencias, como las remesas.",
simple=[
r"La cuenta corriente responde a la pregunta: ¿el país gana del exterior más de lo que gasta en el exterior? Junta cuatro cosas: la <a href=\"balanza-comercial.html\">balanza comercial</a> de bienes, los servicios (turismo, fletes, seguros), la <strong>renta de factores</strong> (intereses y utilidades que se pagan o se reciben) y las <strong>transferencias</strong> (como las <a href=\"remesas.html\">remesas</a>).",
r"Un <strong>déficit</strong> en cuenta corriente significa que el país gasta en el exterior más de lo que recibe, y lo financia con capitales que vienen de fuera (inversión o préstamos). No es malo si se financia con inversión de largo plazo, pero sí puede ser riesgoso si es muy grande.",
],
ejemplo=[
r"En el Perú, la balanza comercial suele tener superávit por las exportaciones mineras, pero la renta de factores suele ser negativa, porque las empresas extranjeras envían a sus países parte de sus utilidades.",
],
formula=dict(
tex=r"\begin{aligned}CC={}&(X-M)_{\text{bienes}}+(X-M)_{\text{servicios}}\\&+\text{Renta neta}+\text{Transferencias netas}\end{aligned}",
),
rel=["balanza-de-pagos", "balanza-comercial", "remesas", "inversion-extranjera-directa"],
))

T.append(dict(
slug="bancarizacion", t="Bancarización", cat="dinero", ic="🏦",
bcrp="Bancarización", alias="inclusion financiera uso de bancos",
corto="Mide cuánto usa la gente los servicios de los bancos: cuentas, tarjetas, créditos y pagos digitales.",
simple=[
r"Un país está más bancarizado cuando más personas y empresas tienen cuentas, ahorran, se prestan y pagan a través del sistema financiero, en lugar de usar solo efectivo.",
r"Una forma de medirla es comparar el crédito o los depósitos con el tamaño de la economía (como porcentaje del PBI). Más bancarización suele traer créditos más baratos, pagos más seguros y menos informalidad.",
r"En el lenguaje tributario, «bancarizar» también es pagar ciertos montos mediante bancos (transferencias, depósitos o tarjetas) para que la SUNAT los reconozca.",
],
ejemplo=[
r"Los pagos con billeteras digitales y las cuentas que se abren desde el celular han ayudado a que más peruanos usen el sistema financiero, incluso en zonas donde no hay una agencia bancaria cerca.",
],
formula=dict(
tex=r"\text{Bancarización}=\frac{\text{Crédito al sector privado}}{PBI}\times 100",
),
rel=["informalidad", "credito-hipotecario", "cajas-municipales", "liquidez"],
))

T.append(dict(
slug="base-monetaria", t="Base monetaria (emisión primaria)", cat="dinero", ic="🪙",
bcrp="Emisión primaria", alias="emision primaria dinero de alto poder",
corto="Es el dinero que crea directamente el banco central: los billetes y monedas que emite y los depósitos de los bancos en el BCRP.",
simple=[
r"La base monetaria, que el BCRP llama <strong>emisión primaria</strong>, tiene dos partes: los billetes y monedas que emitió (en manos del público o en las bóvedas de los bancos) y los depósitos en soles que los bancos guardan en el BCRP.",
r"Es la «semilla» del dinero: a partir de ella, los bancos prestan y crean más dinero en forma de depósitos (el efecto multiplicador que se explica en <a href=\"encaje-bancario.html\">encaje bancario</a>).",
r"El BCRP la aumenta o reduce con sus operaciones: comprando o vendiendo dólares, colocando sus certificados de depósito o prestando a los bancos por pocos días.",
],
ejemplo=[
r"Cuando el BCRP compra dólares a los bancos, les paga con soles nuevos, y la base monetaria crece. Cuando vende dólares, recibe soles y la base monetaria se reduce.",
],
formula=dict(
tex=r"B=C+R",
donde=[(r"B", "base monetaria"), (r"C", "billetes y monedas emitidos"), (r"R", "depósitos de los bancos en el BCRP")],
),
rel=["dinero", "encaje-bancario", "liquidez", "bcrp", "senoreaje"],
))

T.append(dict(
slug="bienes-transables-y-no-transables", t="Bienes transables y no transables", cat="comercio", ic="📦",
bcrp="Bienes transables", alias="transables no transables comercio internacional servicios locales",
corto="Los transables se pueden comprar o vender a otros países; los no transables solo se comercian dentro del país, como un corte de pelo o un alquiler.",
simple=[
r"Un bien es <strong>transable</strong> si puede exportarse o importarse: cobre, celulares, arroz, ropa. Su precio local se parece al precio internacional más los aranceles y el transporte.",
r"Un bien o servicio es <strong>no transable</strong> si, por su naturaleza, no se puede vender fuera: una peluquería, un alquiler, un taxi o un menú. Su precio depende solo de la oferta y la demanda dentro del país.",
r"La relación entre ambos precios es una de las formas de medir el <a href=\"tipo-de-cambio-real.html\">tipo de cambio real</a>.",
],
ejemplo=[
r"Si sube el precio internacional del trigo, sube el precio del pan en Lima, porque el trigo es transable. Pero si sube la demanda de cortes de pelo en un barrio, eso no depende de lo que pase en otros países.",
],
rel=["tipo-de-cambio-real", "arancel", "balanza-comercial", "inflacion"],
))

T.append(dict(
slug="bolsa-de-valores", t="Bolsa de valores", cat="finanzas", ic="📈",
bcrp="Bolsa de valores", alias="bvl bolsa de valores de lima mercado bursatil",
corto="Es el mercado organizado donde se compran y venden acciones, bonos y otros valores de forma pública y regulada.",
simple=[
r"La bolsa reúne a quienes quieren invertir y a empresas o gobiernos que necesitan financiarse. Las operaciones se hacen a través de intermediarios autorizados (las sociedades agentes de bolsa) y los precios se publican, así todos ven a cuánto se negocia cada valor.",
r"Sirve para dos cosas: que las empresas consigan dinero vendiendo acciones o bonos, y que los inversionistas puedan vender sus valores cuando quieran. Además, sus índices muestran cómo ven los inversionistas a las empresas y a la economía.",
r"En el Perú funciona la <strong>Bolsa de Valores de Lima</strong>, supervisada por la Superintendencia del Mercado de Valores (SMV).",
],
ejemplo=[
r"Una persona que quiere invertir en acciones de una minera o de un banco peruano abre una cuenta con una sociedad agente de bolsa y le da la orden de compra. La operación se realiza en la Bolsa de Valores de Lima.",
],
rel=["accion", "bono", "mercado-de-capitales", "fondo-mutuo"],
))

T.append(dict(
slug="bono", t="Bono", cat="finanzas", ic="📃",
bcrp="Bono", alias="bonos renta fija cupon deuda corporativa",
corto="Es un título de deuda: quien lo compra le presta dinero a una empresa o a un gobierno, que promete devolverlo con intereses en fechas fijas.",
simple=[
r"Comprar un bono es prestar dinero. A cambio, el emisor (una empresa, una municipalidad o el gobierno) se compromete a pagarte intereses periódicos, llamados <strong>cupones</strong>, y a devolverte el capital al vencimiento.",
r"Por eso los bonos son <strong>renta fija</strong>: sabes de antemano cuánto te pagarán, salvo que el emisor no cumpla. Mientras más riesgoso es el emisor, más interés tiene que ofrecer.",
r"El precio de un bono en el mercado se mueve al revés que las tasas de interés: si las tasas suben, los bonos antiguos (que pagan menos) bajan de precio.",
],
ejemplo=[
r"Compras un bono de S/ 1000 a 3 años que paga 6 % al año. Recibirás S/ 60 cada año y, al final del tercer año, tus S/ 1000 de vuelta.",
],
formula=dict(
tex=r"P=\sum_{t=1}^{n}\frac{C}{(1+r)^{t}}+\frac{VN}{(1+r)^{n}}",
donde=[(r"P", "precio del bono"), (r"C", "cupón de cada periodo"), (r"VN", "valor nominal que se devuelve al final"), (r"r", "rendimiento exigido por el mercado")],
calculo=[r"\frac{60}{1.06}+\frac{60}{1.06^{2}}+\frac{60+1000}{1.06^{3}}=1000"],
),
rel=["bono-soberano", "accion", "curva-de-rendimiento", "calificacion-de-riesgo", "valor-presente-y-valor-futuro"],
))

T.append(dict(
slug="bono-soberano", t="Bono soberano", cat="estado", ic="🏛️",
bcrp="Bono soberano", alias="bonos del tesoro deuda del gobierno",
corto="Es un bono que emite el gobierno de un país para financiarse. Su tasa refleja cuánto riesgo ve el mercado en ese país.",
simple=[
r"Cuando el Estado necesita dinero, además de cobrar impuestos puede emitir <a href=\"bono.html\">bonos</a>. Los que emite el gobierno central se llaman bonos soberanos. En el Perú los emite el Ministerio de Economía y Finanzas, en soles o en dólares.",
r"El interés que exige el mercado para comprarlos es una medida del <a href=\"riesgo-pais.html\">riesgo país</a>: mientras más confianza hay en que el país pagará, menor es la tasa.",
],
ejemplo=[
r"Si los bonos soberanos peruanos en dólares rinden 5.5 % y los del Tesoro de Estados Unidos 4 %, la diferencia (1.5 puntos o 150 <a href=\"puntos-basicos.html\">puntos básicos</a>) es lo que el mercado pide de más por prestarle al Perú.",
],
rel=["bono", "riesgo-pais", "deuda-publica", "curva-de-rendimiento", "grado-de-inversion"],
))

T.append(dict(
slug="brecha-del-producto", t="Brecha del producto", cat="produccion", ic="📐",
bcrp="Brecha del producto", alias="pbi potencial output gap producto potencial",
corto="Es la diferencia entre lo que la economía produce realmente y lo que podría producir usando sus recursos con normalidad (el PBI potencial).",
simple=[
r"El <strong>PBI potencial</strong> es lo que un país puede producir sin forzar sus máquinas ni a sus trabajadores, y sin generar inflación. La brecha del producto compara el PBI real con ese potencial.",
r"Si la brecha es <strong>negativa</strong>, la economía produce menos de lo que podría: hay capacidad ociosa y desempleo, y la inflación tiende a bajar. Si es <strong>positiva</strong>, la economía está «recalentada» y la inflación tiende a subir.",
r"El PBI potencial no se observa directamente: se estima con modelos. Por eso la brecha siempre es una estimación, que el BCRP usa para decidir su <a href=\"tasa-de-referencia.html\">tasa de referencia</a>.",
],
ejemplo=[
r"Si se estima que el Perú podría producir 1000 (en miles de millones de soles) y produce 980, la brecha es −2 %: la economía está por debajo de su potencial.",
],
formula=dict(
tex=r"\text{Brecha}=\frac{Y-Y^{*}}{Y^{*}}\times 100",
donde=[(r"Y", "PBI observado"), (r"Y^{*}", "PBI potencial")],
calculo=[r"\frac{980-1000}{1000}\times 100=-2\ \%"],
),
rel=["pbi", "ciclo-economico", "regla-de-taylor", "politica-monetaria"],
))

T.append(dict(
slug="canon", t="Canon", cat="estado", ic="⛏️",
bcrp="Canon", alias="canon minero gasifero petrolero regiones municipios",
corto="Es la parte de lo que el Estado recauda por la explotación de recursos naturales que se entrega a las regiones y municipios donde están esos recursos.",
simple=[
r"Cuando una empresa explota minerales, gas, petróleo, pesca, bosques o ríos para generar electricidad, paga impuestos al Estado. Una parte de esos ingresos se transfiere a los gobiernos regionales y locales de la zona: eso es el canon.",
r"Hay varios tipos: <strong>minero</strong>, <strong>gasífero</strong>, <strong>hidroenergético</strong>, <strong>pesquero</strong>, <strong>forestal</strong> y el <strong>canon y sobrecanon petrolero</strong>. El canon minero, por ejemplo, es el 50 % del impuesto a la renta que pagan las mineras.",
r"El MEF reparte el canon con índices que consideran la población y las necesidades básicas insatisfechas de cada zona. Ese dinero debe usarse sobre todo en obras de inversión.",
],
ejemplo=[
r"Si una minera paga S/ 100 millones de impuesto a la renta, S/ 50 millones se reparten como canon minero entre la región, las provincias y los distritos donde opera.",
],
formula=dict(
tex=r"\text{Canon minero}=0.50\times\text{Impuesto a la renta minero}",
calculo=[r"0.50\times 100=50\ \text{millones de soles}"],
),
rel=["impuesto-a-la-renta", "politica-fiscal", "inversion", "terminos-de-intercambio"],
))

T.append(dict(
slug="cajas-municipales", t="Caja municipal de ahorro y crédito", cat="dinero", ic="🏘️",
bcrp="Caja municipal de ahorro y crédito", alias="cmac caja municipal microfinanzas mype",
corto="Es una entidad financiera de propiedad municipal que recibe ahorros y presta dinero, sobre todo a pequeñas y microempresas.",
simple=[
r"Las cajas municipales nacieron para llevar crédito a quienes los bancos grandes atendían poco: micro y pequeños empresarios de provincias. Reciben depósitos del público y prestan, principalmente, para capital de trabajo y negocios.",
r"Su dueño es una municipalidad provincial, pero la ley les prohíbe prestarle a cualquier municipalidad. Están supervisadas por la SBS, y sus depósitos están cubiertos por el Fondo de Seguro de Depósitos, igual que los de los bancos.",
],
ejemplo=[
r"Una señora que tiene una bodega en Huancayo puede pedir a una caja municipal un préstamo para comprar mercadería al por mayor antes de la campaña escolar.",
],
rel=["bancarizacion", "credito-hipotecario", "creditos-de-consumo", "tcea", "trea"],
))

T.append(dict(
slug="calificacion-de-riesgo", t="Calificación de riesgo crediticio", cat="finanzas", ic="🏅",
bcrp="Calificación de riesgo crediticio", alias="clasificadora de riesgo rating aaa bbb s&p moodys fitch",
corto="Es una nota (como AAA o BBB) que ponen las agencias especializadas para indicar qué tan probable es que un emisor pague sus deudas.",
simple=[
r"Las agencias calificadoras (como S&P, Moody's o Fitch, y otras locales) estudian las finanzas de una empresa o de un país y resumen su capacidad de pago en una <strong>nota</strong>.",
r"En la escala más usada, <strong>AAA</strong> es la más segura y luego vienen AA, A, BBB, BB, B, CCC, CC, C y D (incumplimiento). Desde BBB− hacia arriba se habla de <a href=\"grado-de-inversion.html\">grado de inversión</a>; por debajo, de grado especulativo.",
r"Una mejor nota permite endeudarse a tasas más bajas, porque los inversionistas piden menos premio por el riesgo.",
],
ejemplo=[
r"Moody's califica la deuda del Perú con Baa1 (equivale a BBB+), tres escalones dentro del grado de inversión, según informó El Peruano en diciembre de 2025.",
],
rel=["grado-de-inversion", "bono", "riesgo-pais", "bono-soberano"],
))

T.append(dict(
slug="cartera-morosa", t="Cartera morosa", cat="dinero", ic="⏰",
bcrp="Cartera morosa", alias="morosidad cartera vencida creditos atrasados",
corto="Son los créditos que los clientes no están pagando a tiempo o que tuvieron que refinanciarse por problemas de pago.",
simple=[
r"La «cartera» de un banco es el conjunto de créditos que ha dado. La parte <strong>morosa</strong> son los créditos con problemas: los que están atrasados (cartera vencida o en cobranza judicial) y los que se refinanciaron o reestructuraron porque el cliente no podía pagar.",
r"El <strong>índice de morosidad</strong> compara esos créditos con el total. Si sube, el banco tiene que guardar más dinero en provisiones por si no recupera esos préstamos, y suele volverse más estricto al prestar.",
],
ejemplo=[
r"Si una caja tiene S/ 500 millones prestados y S/ 25 millones están atrasados o refinanciados, su morosidad es 5 %.",
],
formula=dict(
tex=r"\text{Morosidad}=\frac{\text{Créditos atrasados y refinanciados}}{\text{Créditos totales}}\times 100",
calculo=[r"\frac{25}{500}\times 100=5\ \%"],
),
rel=["central-de-riesgos", "creditos-de-consumo", "tasa-de-interes", "cajas-municipales"],
))

T.append(dict(
slug="central-de-riesgos", t="Central de riesgos", cat="dinero", ic="🗂️",
bcrp="Central de Riesgos", alias="infocorp reporte de deudas calificacion del deudor sbs",
corto="Es un registro con las deudas de cada persona y empresa en el sistema financiero y si las paga a tiempo. Los bancos lo revisan antes de prestar.",
simple=[
r"La SBS reúne la información que le envían bancos, cajas y financieras sobre quién les debe, cuánto y cómo paga. Así cualquier entidad puede saber si un cliente ya tiene muchas deudas o se atrasa.",
r"A cada deudor se le asigna una <strong>calificación</strong>: Normal, Con Problemas Potenciales (CPP), Deficiente, Dudoso o Pérdida. Mientras mejor es tu calificación, más fácil y barato te será conseguir un crédito.",
r"Puedes consultar gratis tu propio reporte en la página de la SBS. Además, existen centrales privadas de riesgo que juntan otras fuentes.",
],
ejemplo=[
r"Si te atrasas varios meses con tu tarjeta, tu calificación puede pasar de Normal a Deficiente. Aunque luego pagues, otros bancos verán ese historial por un tiempo.",
],
rel=["cartera-morosa", "creditos-de-consumo", "tcea", "bancarizacion"],
))

T.append(dict(
slug="consumo", t="Consumo", cat="produccion", ic="🛍️",
bcrp="Consumo", alias="consumo privado consumo publico gasto de los hogares",
corto="Es el gasto en bienes y servicios para satisfacer necesidades: comida, ropa, transporte, educación, ocio. Es la parte más grande del PBI por el lado del gasto.",
simple=[
r"En las cuentas nacionales, el consumo se divide en <strong>consumo privado</strong> (lo que gastan las familias y las instituciones sin fines de lucro que las sirven) y <strong>consumo público</strong> (lo que gasta el Estado en bienes, servicios y sueldos para funcionar).",
r"Lo que una familia no consume, lo ahorra. Por eso, a nivel de un país, la parte del ingreso que no se consume financia la <a href=\"inversion.html\">inversión</a>.",
],
ejemplo=[
r"En la fórmula del PBI por el lado del gasto, el consumo privado es la letra C. En el Perú, como en la mayoría de países, es el componente más grande.",
],
formula=dict(
tex=r"PBI=\boxed{C}+I+G+(X-M)",
donde=[(r"C", "consumo privado"), (r"G", "gasto del gobierno, que incluye el consumo público")],
),
rel=["pbi", "ahorro", "demanda-agregada", "inversion"],
))

T.append(dict(
slug="credito-hipotecario", t="Crédito hipotecario", cat="finanzas", ic="🏠",
bcrp="Crédito hipotecario", alias="hipoteca prestamo de vivienda mivivienda",
corto="Es un préstamo para comprar o construir una vivienda, en el que la propia casa queda como garantía (hipoteca).",
simple=[
r"En un crédito hipotecario, el banco te presta para tu casa y, a cambio, la casa queda <strong>hipotecada</strong>: la hipoteca se inscribe en Registros Públicos. Si dejas de pagar, el banco puede ejecutar la garantía y vender el inmueble para cobrarse.",
r"Como hay una garantía, la tasa suele ser más baja que la de un préstamo personal, y el plazo es largo (10, 20 o más años). Normalmente debes pagar una <strong>cuota inicial</strong> y contratar seguros de desgravamen y del inmueble.",
r"Para comparar ofertas, mira la <a href=\"tcea.html\">TCEA</a> y si el crédito es en soles o en dólares: si ganas en soles, endeudarte en dólares es riesgoso.",
],
ejemplo=[
r"Una pareja compra un departamento de S/ 300 000: pone S/ 30 000 de cuota inicial (10 %) y el banco le presta S/ 270 000 a 20 años.",
],
rel=["amortizacion", "tcea", "apalancamiento", "dolarizacion", "tasa-de-interes"],
))

T.append(dict(
slug="creditos-de-consumo", t="Crédito de consumo", cat="finanzas", ic="💳",
bcrp="Créditos de consumo", alias="prestamo personal tarjeta de credito credito de consumo",
corto="Es un préstamo a una persona para comprar bienes o servicios o pagar gastos que no tienen que ver con un negocio. Incluye las tarjetas de crédito.",
simple=[
r"Los créditos de consumo financian cosas como electrodomésticos, viajes, estudios o gastos del día a día. Se incluyen los préstamos personales, las tarjetas de crédito y los créditos de tiendas.",
r"Suelen tener tasas más altas que los créditos hipotecarios, porque no tienen una garantía como una casa. Por eso es clave comparar la <a href=\"tcea.html\">TCEA</a> y no endeudarse por encima de lo que se puede pagar.",
],
ejemplo=[
r"Comprar un televisor en 12 cuotas con tarjeta es un crédito de consumo. Si la tarjeta tiene una TEA de 60 %, el televisor puede terminar costando bastante más que su precio al contado.",
],
rel=["tcea", "tea", "cartera-morosa", "central-de-riesgos", "credito-hipotecario"],
))

T.append(dict(
slug="curva-de-rendimiento", t="Curva de rendimiento", cat="finanzas", ic="〰️",
bcrp="Curva de rendimiento", alias="yield curve estructura de tasas por plazo",
corto="Es un gráfico que muestra las tasas de interés de bonos parecidos según su plazo: 1 año, 5 años, 10 años, 30 años.",
simple=[
r"Normalmente, mientras más largo es el plazo, más alta es la tasa: prestar por 30 años es más riesgoso que prestar por 1, y el inversionista pide más. Por eso la curva suele ir <strong>hacia arriba</strong>.",
r"La forma de la curva también refleja lo que el mercado espera de la inflación y de las tasas del banco central. Una curva <strong>invertida</strong> (tasas largas más bajas que las cortas) suele interpretarse como señal de que se esperan tasas más bajas, a veces por una desaceleración.",
],
ejemplo=[
r"Si los bonos soberanos peruanos en soles rinden 4.5 % a 2 años y 6.5 % a 20 años, la curva tiene pendiente positiva.",
],
rel=["bono", "bono-soberano", "tasa-de-referencia", "puntos-basicos"],
))

T.append(dict(
slug="demanda-agregada", t="Demanda agregada", cat="produccion", ic="🛒",
bcrp="Demanda agregada", alias="demanda interna demanda externa gasto total",
corto="Es todo lo que se quiere comprar en una economía: lo que gastan familias, empresas y Estado (demanda interna) más lo que compran otros países (exportaciones).",
simple=[
r"La demanda agregada suma el <a href=\"consumo.html\">consumo</a>, la <a href=\"inversion.html\">inversión</a> y el gasto del gobierno, que juntos forman la <strong>demanda interna</strong>, más la <strong>demanda externa</strong> (las exportaciones).",
r"Si la demanda agregada crece más rápido que lo que la economía puede producir, los precios tienden a subir. Por eso la política monetaria y la fiscal buscan que no crezca ni demasiado ni demasiado poco.",
],
ejemplo=[
r"Una baja de la tasa de referencia abarata los créditos, la gente y las empresas compran e invierten más, y la demanda agregada sube.",
],
formula=dict(
tex=r"DA=\underbrace{C+I+G}_{\text{demanda interna}}+\underbrace{X}_{\text{demanda externa}}",
),
ojo=["Con las importaciones (M) se cumple el equilibrio: lo que se demanda (DA) es igual a lo que se ofrece, que es el PBI más las importaciones."],
rel=["oferta-agregada", "consumo", "inversion", "pbi", "brecha-del-producto"],
))

T.append(dict(
slug="oferta-agregada", t="Oferta agregada", cat="produccion", ic="🏗️",
bcrp="Oferta agregada", alias="oferta global produccion mas importaciones",
corto="Es el total de bienes y servicios disponibles en una economía: lo que produce el país (PBI) más lo que importa.",
simple=[
r"Para el BCRP, la oferta agregada (u oferta global) suma la producción nacional (el <a href=\"pbi.html\">PBI</a>) y las importaciones. Es todo lo que hay disponible para vender en un periodo.",
r"En equilibrio, la oferta agregada es igual a la <a href=\"demanda-agregada.html\">demanda agregada</a>. Si ocurre un «choque de oferta», como un fenómeno El Niño que destruye cosechas, la oferta cae y los precios tienden a subir aunque la demanda no cambie.",
],
ejemplo=[
r"Si el Perú produce 1000 y importa 250 (en miles de millones), la oferta global es 1250. Esa cantidad se reparte entre consumo, inversión, gasto público y exportaciones.",
],
formula=dict(
tex=r"OA=PBI+M=C+I+G+X",
calculo=[r"1000+250=1250"],
),
rel=["demanda-agregada", "pbi", "inflacion", "productividad"],
))

T.append(dict(
slug="deposito-a-plazo", t="Depósito a plazo fijo", cat="finanzas", ic="🔐",
bcrp="Depósito a plazo", alias="plazo fijo ahorro a plazo cdt",
corto="Es dejar dinero en un banco o caja durante un tiempo fijo a cambio de una tasa de interés más alta que la de una cuenta de ahorros.",
simple=[
r"En un depósito a plazo, te comprometes a no retirar tu dinero hasta una fecha (por ejemplo, 6 meses o 1 año). A cambio, la entidad te paga más intereses que en una cuenta de ahorros común.",
r"Si lo retiras antes, normalmente pierdes parte o todos los intereses. Para comparar ofertas, mira la <a href=\"trea.html\">TREA</a> y confirma que la entidad esté supervisada por la SBS.",
],
ejemplo=[
r"Depositas S/ 5000 a 1 año con una TREA de 5 %. Al final recibes S/ 5250. Si lo retiras a los 6 meses, podrías recibir solo los S/ 5000.",
],
formula=dict(
tex=r"M=C\,(1+TREA)^{\frac{d}{360}}",
donde=[(r"C", "monto depositado"), (r"d", "días del depósito"), (r"M", "monto al vencimiento")],
calculo=[r"5000\,(1.05)^{\frac{360}{360}}=5250\ \text{soles}"],
),
ojo=["Muchas entidades usan años de 360 días para estos cálculos; revisa la cartilla de información de tu depósito."],
rel=["trea", "ahorro", "interes-compuesto", "cajas-municipales"],
))

T.append(dict(
slug="dinero", t="Dinero", cat="dinero", ic="💵",
bcrp="Dinero", alias="funciones del dinero medio de pago unidad de cuenta reserva de valor cuasidinero",
corto="Es lo que la gente acepta para pagar. Cumple tres funciones: medio de pago, unidad de cuenta y reserva de valor.",
simple=[
r"El dinero cumple tres funciones: <strong>medio de pago</strong> (sirve para comprar), <strong>unidad de cuenta</strong> (los precios se expresan en soles) y <strong>reserva de valor</strong> (puedes guardarlo para gastarlo después, aunque la inflación le quita valor).",
r"En sentido estricto, el BCRP llama dinero a los billetes y monedas en manos del público (el <strong>circulante</strong>) más los depósitos a la vista, que se pueden usar de inmediato. Los depósitos de ahorro y a plazo son <strong>cuasidinero</strong>: se convierten en dinero rápido, pero no se usan directamente para pagar.",
],
ejemplo=[
r"Los S/ 50 de tu billetera y el saldo de tu cuenta corriente son dinero. Un depósito a plazo fijo es cuasidinero: tendrías que retirarlo antes de poder gastarlo.",
],
formula=dict(
tex=r"\text{Dinero}=\text{Circulante}+\text{Depósitos a la vista}",
),
rel=["base-monetaria", "liquidez", "inflacion", "bcrp", "senoreaje"],
))

T.append(dict(
slug="efecto-traspaso", t="Efecto traspaso (pass-through)", cat="precios", ic="➡️",
bcrp="Efecto traspaso", alias="pass through tipo de cambio inflacion",
corto="Mide cuánto se trasladan a los precios internos las subidas o bajadas del tipo de cambio.",
simple=[
r"Cuando sube el dólar, los productos importados se encarecen en soles, y algunas empresas suben sus precios. El efecto traspaso mide qué parte de esa subida del dólar termina en la <a href=\"inflacion.html\">inflación</a>.",
r"Mientras más dolarizada está una economía, más fuerte suele ser el traspaso, porque más precios se fijan pensando en dólares. Por eso la <a href=\"dolarizacion.html\">desdolarización</a> y la credibilidad del BCRP ayudan a que un salto del dólar no dispare la inflación.",
],
ejemplo=[
r"Si el dólar sube 10 % y, por eso, la inflación aumenta 1 punto, el coeficiente de traspaso es 0.1 (10 %).",
],
formula=dict(
tex=r"\text{Traspaso}=\frac{\Delta\pi}{\%\Delta TC}",
calculo=[r"\frac{1}{10}=0.1"],
),
rel=["tipo-de-cambio", "depreciacion-y-apreciacion", "inflacion", "dolarizacion"],
))

T.append(dict(
slug="estanflacion", t="Estanflación", cat="precios", ic="🥶",
bcrp="Estanflación", alias="estancamiento con inflacion stagflation",
corto="Es cuando, al mismo tiempo, la economía no crece (o cae), hay desempleo alto y la inflación es alta.",
simple=[
r"La palabra junta «estancamiento» e «inflación». Es una situación difícil, porque las herramientas habituales chocan: si el banco central sube tasas para frenar la inflación, enfría aún más la economía; si las baja para reactivarla, la inflación puede subir más.",
r"Suele aparecer tras un <strong>choque de oferta</strong>, como una fuerte subida del petróleo, que encarece todo y a la vez reduce la producción.",
],
ejemplo=[
r"El caso más citado es el de muchas economías en los años setenta, cuando el precio del petróleo se disparó: los precios subían rápido mientras la producción se estancaba y crecía el desempleo.",
],
rel=["inflacion", "recesion", "oferta-agregada", "politica-monetaria"],
))

T.append(dict(
slug="evasion-y-elusion-tributaria", t="Evasión y elusión tributaria", cat="impuestos", ic="🕵️",
bcrp="Evasión tributaria", alias="evasion elusion pagar menos impuestos delito tributario",
corto="Evadir es dejar de pagar impuestos con engaños (es delito). Eludir es pagar menos aprovechando vacíos de la ley, sin cometer delito.",
simple=[
r"La <strong>evasión tributaria</strong> es dejar de pagar, a propósito, impuestos que la ley exige, usando engaños: no dar comprobantes, ocultar ventas o inventar gastos. Es ilegal y puede ser delito.",
r"La <strong>elusión tributaria</strong> es organizar las operaciones para pagar menos impuestos aprovechando ambigüedades o vacíos de la ley. No es un delito, pero la SUNAT puede cuestionar operaciones artificiales hechas solo para no pagar.",
r"Ambas reducen lo que el Estado recauda para salud, educación y obras, y hacen que quienes sí cumplen carguen con más.",
],
ejemplo=[
r"Un negocio que vende sin entregar boleta para no declarar esas ventas está evadiendo. Una empresa que divide artificialmente sus operaciones para quedarse en un régimen con menos impuestos podría estar eludiendo.",
],
rel=["igv", "impuesto-a-la-renta", "informalidad", "politica-fiscal"],
))

T.append(dict(
slug="expectativas", t="Expectativas", cat="precios", ic="🔮",
bcrp="Expectativas", alias="expectativas de inflacion expectativas racionales adaptativas autocumplidas",
corto="Son lo que las personas y empresas creen que pasará con la economía. Influyen en sus decisiones de hoy, como subir precios o invertir.",
simple=[
r"En economía, lo que la gente espera importa mucho. Si todos esperan que los precios suban, los trabajadores piden más sueldo y las empresas suben precios antes: la inflación esperada termina causando inflación. A eso se le llama expectativa <strong>autocumplida</strong>.",
r"Hay dos ideas clásicas: las expectativas <strong>adaptativas</strong> (la gente espera que el futuro se parezca al pasado reciente) y las <strong>racionales</strong> (la gente usa toda la información disponible, incluidos los anuncios del banco central).",
r"Por eso el BCRP publica su meta, explica sus decisiones y hace encuestas de expectativas: si la gente confía en que la inflación volverá a la meta, es más fácil que vuelva.",
],
ejemplo=[
r"Si una encuesta muestra que las empresas esperan una inflación de 2.5 % para el próximo año, dentro del rango de 1 % a 3 %, se dice que las expectativas están «ancladas».",
],
rel=["inflacion", "politica-monetaria", "tasa-de-referencia", "bcrp"],
))

T.append(dict(
slug="exportaciones-tradicionales-y-no-tradicionales", t="Exportaciones tradicionales y no tradicionales", cat="comercio", ic="🚛",
bcrp="Exportaciones tradicionales", alias="exportaciones mineras agroexportacion valor agregado",
corto="Las tradicionales son las que el Perú siempre ha vendido, con poca transformación (minerales, harina de pescado). Las no tradicionales tienen más valor agregado (agroexportación, textiles, químicos).",
simple=[
r"La diferencia es legal: las <strong>tradicionales</strong> están en una lista del Decreto Supremo 076-92-EF (minerales, petróleo y derivados, harina y aceite de pescado, algunos productos agrícolas como el café). El gas natural también se cuenta como tradicional.",
r"Todo lo demás es <strong>no tradicional</strong>: productos con más transformación o que el país no exportaba antes en cantidades importantes, como arándanos, paltas, uvas, espárragos, textiles, confecciones y químicos.",
r"Las no tradicionales suelen generar más empleo por cada dólar exportado, porque requieren más mano de obra y procesamiento.",
],
ejemplo=[
r"El cobre concentrado que sale de una mina es una exportación tradicional. Los arándanos frescos que se envían en contenedores refrigerados son una exportación no tradicional.",
],
rel=["balanza-comercial", "terminos-de-intercambio", "ventaja-comparativa", "bienes-transables-y-no-transables"],
))

T.append(dict(
slug="fideicomiso", t="Fideicomiso", cat="finanzas", ic="🤝",
bcrp="Fideicomiso", alias="fiduciario fideicomitente fideicomisario patrimonio fideicometido",
corto="Es un acuerdo en el que alguien entrega bienes o dinero a una entidad de confianza para que los administre con un fin específico, a favor de otra persona.",
simple=[
r"En un fideicomiso hay tres partes: el <strong>fideicomitente</strong> (quien entrega los bienes), el <strong>fiduciario</strong> (quien los administra, normalmente un banco o una empresa autorizada) y el <strong>fideicomisario</strong> (quien se beneficia).",
r"Los bienes forman un <strong>patrimonio aparte</strong>, separado del de cada una de las partes, y solo pueden usarse para el fin acordado. Eso da seguridad: por ejemplo, los acreedores del fideicomitente no pueden tocarlos.",
],
ejemplo=[
r"Una inmobiliaria pone en un fideicomiso el dinero que pagan los compradores de un edificio en construcción. El banco fiduciario solo libera ese dinero a medida que avanza la obra, para proteger a los compradores.",
],
rel=["fondo-mutuo", "credito-hipotecario", "bono"],
))

T.append(dict(
slug="fondo-mutuo", t="Fondo mutuo", cat="finanzas", ic="🧺",
bcrp="Fondo mutuo de inversión en valores", alias="fondos mutuos inversion colectiva cuotas de participacion",
corto="Es un fondo que junta el dinero de muchas personas para invertirlo en bonos, acciones u otros instrumentos, administrado por una empresa especializada.",
simple=[
r"En vez de invertir solo, compras <strong>cuotas</strong> de un fondo. Una sociedad administradora decide en qué invertir el dinero de todos, siguiendo la política del fondo (por ejemplo, solo bonos de corto plazo o una mezcla con acciones).",
r"La ganancia o pérdida depende de cómo les va a esas inversiones: <strong>no tienen una tasa garantizada</strong>. Hay fondos más conservadores y otros más arriesgados. La administradora cobra una comisión y está supervisada por la SMV.",
],
ejemplo=[
r"Si inviertes S/ 2000 en un fondo cuya cuota vale S/ 100, recibes 20 cuotas. Si al año la cuota vale S/ 106, tu inversión vale S/ 2120 (antes de impuestos y comisiones de rescate, si las hay).",
],
formula=dict(
tex=r"\text{Valor de tu inversión}=\text{N.° de cuotas}\times\text{Valor cuota}",
calculo=[r"20\times 106=2120\ \text{soles}"],
),
rel=["accion", "bono", "bolsa-de-valores", "mercado-de-capitales", "ahorro"],
))

T.append(dict(
slug="grado-de-inversion", t="Grado de inversión", cat="finanzas", ic="✅",
bcrp="Grado de inversión", alias="investment grade bbb- calificacion pais",
corto="Es la calificación que dan las agencias a emisores considerados seguros (de BBB− para arriba). Abre la puerta a más inversionistas y a tasas más bajas.",
simple=[
r"Las agencias de <a href=\"calificacion-de-riesgo.html\">calificación de riesgo</a> dividen sus notas en dos grupos: <strong>grado especulativo</strong> (más riesgoso, por debajo de BBB−) y <strong>grado de inversión</strong> (más seguro, desde BBB− hasta AAA).",
r"Tener grado de inversión importa porque muchos fondos de pensiones y aseguradoras del mundo solo pueden comprar bonos con esa calificación. Así, el país o la empresa consigue más compradores y paga menos intereses.",
],
ejemplo=[
r"El Perú tiene grado de inversión. A fines de 2025, Moody's mantenía su nota en Baa1 (equivalente a BBB+), tres escalones dentro del grado de inversión.",
],
rel=["calificacion-de-riesgo", "riesgo-pais", "bono-soberano", "deuda-publica"],
))

T.append(dict(
slug="hiperinflacion", t="Hiperinflación", cat="precios", ic="🔥",
bcrp="Hiperinflación", alias="hiperinflacion peru 1990 inflacion descontrolada",
corto="Es una inflación altísima y fuera de control: los precios suben tan rápido que el dinero pierde su valor en días.",
simple=[
r"En una hiperinflación, el poder de compra del dinero se derrumba. Se crea un círculo vicioso: como todos esperan más inflación, gastan su dinero de inmediato y suben sus precios, y eso alimenta aún más la inflación.",
r"Su causa más común es que el Estado financie su gasto <strong>imprimiendo dinero sin control</strong>. También influyen guerras, crisis políticas o depresiones económicas.",
r"Para salir de ella se necesitan medidas fuertes: dejar de financiar al Estado con emisión, ordenar las cuentas públicas y recuperar la confianza en la moneda.",
],
ejemplo=[
r"El Perú vivió una hiperinflación a fines de los ochenta: según el Banco Mundial, la inflación de 1990 superó el 7000 % anual. Por eso, la Constitución de 1993 prohíbe al BCRP financiar al Tesoro Público.",
],
rel=["inflacion", "bcrp", "dolarizacion", "senoreaje", "expectativas"],
))

T.append(dict(
slug="inflacion-subyacente", t="Inflación subyacente", cat="precios", ic="🧭",
bcrp="Inflación subyacente", alias="core inflation inflacion sin alimentos y energia inflacion no subyacente",
corto="Es la inflación sin los precios más volátiles, como algunos alimentos y los combustibles. Muestra mejor la tendencia de fondo de los precios.",
simple=[
r"Algunos precios saltan mucho por causas pasajeras: una mala cosecha encarece el limón, o el petróleo internacional sube la gasolina. Esos saltos no dicen mucho sobre la tendencia de la inflación. La inflación <strong>subyacente</strong> los saca del cálculo para ver mejor qué pasa con el resto.",
r"El BCRP publica varios indicadores de este tipo. Uno muy usado es la <strong>inflación sin alimentos y energía</strong>, que excluye alimentos y bebidas, combustibles y electricidad.",
r"La parte que se excluye se llama <strong>inflación no subyacente</strong>: depende de factores que el banco central no controla, como el clima (El Niño) o los precios internacionales.",
],
ejemplo=[
r"Si un mes la inflación total sube por un fenómeno El Niño que encarece los alimentos, pero la inflación sin alimentos y energía sigue estable, el BCRP puede entender que el salto es temporal y no necesariamente subir su tasa.",
],
rel=["inflacion", "ipc", "politica-monetaria", "expectativas"],
))

T.append(dict(
slug="inversion-extranjera-directa", t="Inversión extranjera directa", cat="comercio", ic="🏗️",
bcrp="Inversión directa extranjera", alias="ied inversion extranjera inversionista no residente",
corto="Es la inversión que hace una empresa o persona de otro país en una empresa local con interés de largo plazo y con influencia en su gestión (10 % o más).",
simple=[
r"No toda inversión extranjera es igual. La <strong>directa</strong> busca quedarse y participar en la empresa: construir una mina, comprar una fábrica o abrir una cadena de tiendas. Por norma general, se considera directa cuando el inversionista extranjero tiene 10 % o más del capital.",
r"La <strong>inversión de cartera</strong>, en cambio, compra acciones o bonos en pequeñas proporciones y puede salir rápido. Por eso la inversión directa se considera más estable para financiar el <a href=\"balanza-en-cuenta-corriente.html\">déficit en cuenta corriente</a>.",
],
ejemplo=[
r"Cuando una empresa minera extranjera construye un nuevo proyecto en el Perú, o una cadena chilena compra supermercados peruanos, eso es inversión extranjera directa.",
],
rel=["balanza-de-pagos", "balanza-en-cuenta-corriente", "inversion", "riesgo-pais"],
))

T.append(dict(
slug="liquidez", t="Liquidez", cat="dinero", ic="💧",
bcrp="Liquidez", alias="activo liquido liquidez del sistema financiero cuasidinero",
corto="Tiene dos sentidos: qué tan fácil es convertir algo en dinero sin perder valor, y el total de dinero y depósitos que el sistema financiero debe al público.",
simple=[
r"En el sentido común, un bien es más <strong>líquido</strong> mientras más rápido y fácil puedes convertirlo en dinero sin perder valor. El efectivo es lo más líquido; una casa es poco líquida, porque venderla toma tiempo.",
r"En las estadísticas del BCRP, la <strong>liquidez</strong> es el total de obligaciones del sistema financiero con el público: el <a href=\"dinero.html\">dinero</a> (circulante y depósitos a la vista) más el cuasidinero (depósitos de ahorro, a plazo y otros valores), en soles y en dólares.",
r"Para un banco, tener liquidez es tener dinero disponible para pagar a sus depositantes cuando lo pidan.",
],
ejemplo=[
r"Un depósito a plazo es menos líquido que una cuenta de ahorros: si lo retiras antes de tiempo, pierdes intereses. Una acción de una empresa pequeña que casi nadie compra es todavía menos líquida.",
],
rel=["dinero", "base-monetaria", "encaje-bancario", "bancarizacion"],
))

T.append(dict(
slug="mercado-de-capitales", t="Mercado de capitales", cat="finanzas", ic="🏛️",
bcrp="Mercado de capitales", alias="mercado de valores financiamiento de largo plazo emision de valores",
corto="Es el mercado donde empresas y gobiernos consiguen financiamiento de mediano y largo plazo emitiendo acciones y bonos que compran los inversionistas.",
simple=[
r"En vez de pedir un préstamo a un banco, una empresa puede financiarse directamente con los inversionistas: vendiendo <a href=\"accion.html\">acciones</a> (nuevos socios) o <a href=\"bono.html\">bonos</a> (deuda). Ese es el mercado de capitales.",
r"Tiene un <strong>mercado primario</strong>, donde se venden los valores por primera vez, y un <strong>mercado secundario</strong>, donde los inversionistas los compran y venden entre ellos, por ejemplo en la <a href=\"bolsa-de-valores.html\">bolsa</a>.",
r"Los fondos de pensiones (AFP), las aseguradoras y los <a href=\"fondo-mutuo.html\">fondos mutuos</a> son grandes inversionistas en este mercado.",
],
ejemplo=[
r"Una empresa eléctrica que necesita construir una central puede emitir bonos a 10 años. Las AFP los compran, y así el ahorro de los trabajadores financia una obra de largo plazo.",
],
rel=["accion", "bono", "bolsa-de-valores", "fondo-mutuo", "afp-y-onp"],
))

T.append(dict(
slug="paridad-del-poder-adquisitivo", t="Paridad del poder adquisitivo", cat="comercio", ic="🍔",
bcrp="Paridad del poder adquisitivo", alias="ppa ppp indice big mac tipo de cambio de equilibrio",
corto="Es la teoría de que un mismo producto debería costar lo mismo en todos los países si se mide en la misma moneda. Sirve para ver si una moneda está cara o barata.",
simple=[
r"Si una canasta cuesta S/ 350 en el Perú y US$ 100 en Estados Unidos, el tipo de cambio que «iguala» los precios sería S/ 3.50 por dólar. Esa es la idea de la paridad del poder adquisitivo (PPA).",
r"En su versión de cambios, dice que si un país tiene más inflación que otro, su moneda tiende a depreciarse en esa diferencia. En la práctica no se cumple al pie de la letra (por transporte, aranceles y bienes no transables), pero ayuda a comparar.",
r"Un ejemplo famoso es el <strong>índice Big Mac</strong> de la revista <em>The Economist</em>, que compara el precio de esa hamburguesa en muchos países para ver si las monedas están sobrevaluadas o subvaluadas.",
],
ejemplo=[
r"Si una hamburguesa cuesta US$ 5 en Estados Unidos y S/ 14 en Lima, el tipo de cambio PPA sería S/ 2.80 por dólar. Si el dólar real está a S/ 3.50, según esta idea el sol estaría «barato» (subvaluado).",
],
formula=dict(
tex=r"TC_{PPA}=\frac{P_{\text{Perú}}}{P_{\text{EE. UU.}}}",
calculo=[r"\frac{14}{5}=2.80\ \text{soles por dólar}"],
),
rel=["tipo-de-cambio", "tipo-de-cambio-real", "poder-adquisitivo", "inflacion"],
))

T.append(dict(
slug="productividad", t="Productividad", cat="produccion", ic="⚙️",
bcrp="Productividad", alias="productividad laboral ptf productividad total de factores",
corto="Es cuánto se produce con cada unidad de recursos, por ejemplo por cada trabajador o por cada hora trabajada.",
simple=[
r"Si un taller hace 100 polos al día con 5 personas, cada una produce 20. Si con mejores máquinas o mejor organización hacen 120 con las mismas 5, la productividad subió a 24 por persona.",
r"La <strong>productividad total de factores</strong> (PTF) mide lo que crece la producción más allá de lo que explican el aumento de trabajadores y de máquinas: refleja la tecnología, la educación, la buena organización y las instituciones.",
r"A largo plazo, la productividad es lo que más explica que suban los sueldos y el nivel de vida de un país.",
],
ejemplo=[
r"Un agricultor que instala riego tecnificado y obtiene más kilos de palta por hectárea, con la misma tierra y el mismo personal, ha aumentado su productividad.",
],
formula=dict(
tex=r"\text{Productividad laboral}=\frac{\text{Producción}}{\text{Trabajadores (u horas)}}",
calculo=[r"\frac{120}{5}=24\ \text{polos por persona}"],
),
rel=["crecimiento-economico", "pbi", "informalidad", "oferta-agregada"],
))

T.append(dict(
slug="puntos-basicos", t="Puntos básicos y puntos porcentuales", cat="finanzas", ic="📏",
bcrp="Puntos básicos", alias="pb pbs bps puntos porcentuales",
corto="Un punto básico es la centésima parte de un punto porcentual (0.01 %). Se usan para hablar de cambios en tasas de interés sin confusiones.",
simple=[
r"Si una tasa pasa de 4 % a 5 %, subió <strong>1 punto porcentual</strong>. No es lo mismo que decir que subió «1 %»: en realidad subió 25 % (porque 1 es la cuarta parte de 4). Para evitar esa confusión se usan los puntos porcentuales.",
r"Para cambios pequeños se usan los <strong>puntos básicos</strong>: 100 puntos básicos son 1 punto porcentual. Se usan mucho en el <a href=\"riesgo-pais.html\">riesgo país</a> y en las decisiones de tasas del BCRP.",
],
ejemplo=[
r"Si el BCRP baja su tasa de referencia de 4.50 % a 4.25 %, la redujo en 25 puntos básicos (0.25 puntos porcentuales).",
],
formula=dict(
tex=r"1\ \text{punto porcentual}=100\ \text{pb},\qquad 1\ \text{pb}=0.01\ \%",
calculo=[r"4.50\ \%-4.25\ \%=0.25\ \text{puntos}=25\ \text{pb}"],
),
rel=["riesgo-pais", "tasa-de-referencia", "tasa-de-interes", "curva-de-rendimiento"],
))

T.append(dict(
slug="regla-de-taylor", t="Regla de Taylor", cat="dinero", ic="📏",
bcrp="Regla de Taylor", alias="john taylor regla de politica monetaria tasa neutral",
corto="Es una regla sencilla que sugiere cuánto debería fijar un banco central su tasa de interés según la inflación y la actividad económica.",
simple=[
r"El economista John Taylor propuso que los bancos centrales suben su tasa cuando la inflación está por encima de la meta o la economía está «recalentada», y la bajan cuando la inflación está baja o la economía está débil. La regla pone números a esa idea.",
r"No es una ley que el BCRP aplique de forma automática: es una guía para analizar si la tasa está muy alta o muy baja.",
],
ejemplo=[
r"Si la tasa real neutral es 1.5 %, la inflación está en 4 %, la meta es 2 % y la <a href=\"brecha-del-producto.html\">brecha del producto</a> es 0, la regla sugiere una tasa de 6.5 %.",
],
formula=dict(
tex=r"i=r^{*}+\pi+0.5\,(\pi-\pi^{*})+0.5\,(y-y^{*})",
donde=[(r"i", "tasa de interés sugerida"), (r"r^{*}", "tasa real neutral"), (r"\pi", "inflación actual"), (r"\pi^{*}", "meta de inflación"), (r"y-y^{*}", "brecha del producto, en %")],
calculo=[r"i=1.5+4+0.5\,(4-2)+0.5\,(0)=6.5\ \%"],
),
rel=["tasa-de-referencia", "politica-monetaria", "brecha-del-producto", "inflacion"],
))

T.append(dict(
slug="remesas", t="Remesas", cat="comercio", ic="✉️",
bcrp="Remesa", alias="remesas del exterior dinero de familiares en el extranjero",
corto="Es el dinero que envían a sus familias los peruanos que viven y trabajan en otro país.",
simple=[
r"Muchos peruanos que trabajan en Estados Unidos, España, Chile, Argentina u otros países mandan parte de su sueldo a su familia en el Perú. Esos envíos son remesas.",
r"En la <a href=\"balanza-de-pagos.html\">balanza de pagos</a>, las remesas se registran como <strong>transferencias corrientes</strong> dentro de la cuenta corriente. Se considera emigrante a quien vive en otra economía por un año o más.",
r"Para muchas familias, las remesas son una fuente importante de ingresos para gastos de alimentación, educación o salud.",
],
ejemplo=[
r"Una peruana que trabaja en Madrid envía 300 euros al mes a su madre en Trujillo. Ese envío suma a las remesas que recibe el Perú.",
],
rel=["balanza-de-pagos", "balanza-en-cuenta-corriente", "tipo-de-cambio"],
))

T.append(dict(
slug="reservas-internacionales", t="Reservas internacionales netas (RIN)", cat="dinero", ic="🏦",
bcrp="Reservas internacionales brutas", alias="rin reservas del bcrp activos de reserva colchon de dolares",
corto="Son los dólares, oro y otros activos externos que el BCRP tiene disponibles, menos lo que debe al exterior. Son el «colchón» del país ante crisis.",
simple=[
r"Las reservas <strong>brutas</strong> son los activos externos que el BCRP puede usar de inmediato: divisas en sus bóvedas, depósitos en bancos del exterior de primer nivel, valores de entidades internacionales, oro y derechos especiales de giro del FMI. Las <strong>netas</strong> (RIN) restan sus obligaciones con el exterior.",
r"Sirven para enfrentar salidas bruscas de dólares, intervenir en el mercado cambiario para evitar saltos del dólar y dar confianza a los inversionistas. Unas reservas altas son una señal de solidez.",
],
ejemplo=[
r"Según el MEF, a inicios de julio de 2026 las reservas internacionales netas del Perú llegaban a unos US$ 99 700 millones, alrededor de 28 % del PBI, más que Colombia, Chile y México en proporción a su economía.",
],
formula=dict(
tex=r"\begin{aligned}RIN={}&\text{Activos de reserva}\\&-\text{Pasivos externos de corto plazo del BCRP}\end{aligned}",
),
rel=["balanza-de-pagos", "bcrp", "tipo-de-cambio", "riesgo-pais"],
))

T.append(dict(
slug="senoreaje", t="Señoreaje", cat="dinero", ic="👑",
bcrp="Señoreaje", alias="ganancia por emitir dinero impuesto inflacionario",
corto="Es la ganancia que obtiene quien emite dinero: la diferencia entre el valor de un billete o moneda y lo que cuesta fabricarlo.",
simple=[
r"Fabricar un billete de S/ 100 cuesta mucho menos de S/ 100. Esa diferencia es el señoreaje. El nombre viene de los antiguos señores feudales, que ganaban al acuñar monedas.",
r"En un sentido más amplio, el señoreaje es lo que el Estado puede financiar emitiendo dinero. Si se abusa de él, la cantidad de dinero crece más que la producción y genera inflación, que funciona como un «impuesto» sobre quienes tienen efectivo. Ese abuso fue una de las causas de la <a href=\"hiperinflacion.html\">hiperinflación</a> peruana.",
],
ejemplo=[
r"Si producir una moneda de S/ 5 cuesta S/ 0.80, el señoreaje por cada moneda es S/ 4.20.",
],
formula=dict(
tex=r"\text{Señoreaje}=\text{Valor nominal}-\text{Costo de fabricación}",
calculo=[r"5-0.80=4.20\ \text{soles}"],
),
rel=["base-monetaria", "dinero", "hiperinflacion", "bcrp"],
))

T.append(dict(
slug="subempleo", t="Subempleo", cat="trabajo", ic="🕰️",
bcrp="Población subempleada", alias="subempleo por horas subempleo por ingresos empleo adecuado",
corto="Es tener trabajo, pero de baja calidad: con menos horas de las que quieres trabajar o con un ingreso por debajo de un mínimo de referencia.",
simple=[
r"Una persona puede estar ocupada y, aun así, no tener un buen empleo. El INEI distingue dos tipos de subempleo:",
r"<strong>Por horas</strong>: trabaja menos de 35 horas a la semana y quiere trabajar más. <strong>Por ingresos</strong>: trabaja 35 horas o más, pero gana menos que un ingreso mínimo de referencia, calculado con el costo de una canasta mínima de consumo.",
r"Quien no está subempleado ni desempleado tiene un <strong>empleo adecuado</strong>. Como en el Perú el desempleo es bajo, el subempleo y la <a href=\"informalidad.html\">informalidad</a> dicen más sobre la calidad del trabajo.",
],
ejemplo=[
r"Un joven que hace delivery 20 horas a la semana y busca más horas está subempleado por horas. Una persona que trabaja 50 horas en un puesto de mercado pero gana muy poco está subempleada por ingresos.",
],
rel=["pea", "tasa-de-desempleo", "informalidad", "remuneracion-minima-vital"],
))

T.append(dict(
slug="subsidio", t="Subsidio", cat="estado", ic="🎗️",
bcrp="Subsidio", alias="subsidios ayuda del estado transferencias bono",
corto="Es una ayuda económica del Estado, sin devolución, para abaratar un bien o apoyar a un grupo de personas o empresas.",
simple=[
r"Un subsidio puede ser <strong>directo</strong>, cuando el Estado entrega dinero a un grupo específico (por ejemplo, un bono a familias pobres), o <strong>indirecto</strong>, cuando baja el precio de algo para todos (por ejemplo, cubriendo parte del costo de un servicio o de un combustible).",
r"Los subsidios bien diseñados ayudan a quienes más lo necesitan. Los mal focalizados pueden beneficiar a quien no lo necesita, cuestan mucho al Estado y pueden distorsionar los precios.",
],
ejemplo=[
r"Un programa que entrega dinero mensual a adultos mayores en pobreza es un subsidio directo. Un fondo que reduce el precio de un combustible en el grifo es un subsidio indirecto.",
],
rel=["politica-fiscal", "deficit-fiscal", "pobreza-monetaria"],
))

T.append(dict(
slug="tipo-de-cambio-real", t="Tipo de cambio real", cat="comercio", ic="⚖️",
bcrp="Tipo de cambio real", alias="tcr competitividad tipo de cambio real multilateral",
corto="Compara los precios de dos países en una misma moneda. Indica si los productos peruanos están caros o baratos frente a los del exterior.",
simple=[
r"El <a href=\"tipo-de-cambio.html\">tipo de cambio</a> nominal dice cuántos soles cuesta un dólar. El <strong>real</strong> ajusta ese número por la inflación de cada país, para saber cuántas canastas peruanas cuesta una canasta extranjera.",
r"Si el tipo de cambio real <strong>sube</strong>, los productos peruanos se abaratan frente a los extranjeros: mejora la competitividad de los exportadores. Si <strong>baja</strong>, lo importado se vuelve relativamente más barato.",
r"El BCRP publica un índice de tipo de cambio real <strong>multilateral</strong>, que compara al Perú con sus principales socios comerciales a la vez.",
],
ejemplo=[
r"Si el dólar sigue en S/ 3.50 pero en el Perú los precios subieron 5 % y en Estados Unidos 2 %, el tipo de cambio real bajó: los productos peruanos se encarecieron un poco frente a los estadounidenses.",
],
formula=dict(
tex=r"TCR=TC\times\frac{P^{*}}{P}",
donde=[(r"TC", "tipo de cambio nominal (soles por dólar)"), (r"P^{*}", "índice de precios externo"), (r"P", "índice de precios del Perú")],
calculo=[r"3.50\times\frac{1.02}{1.05}\approx 3.40"],
),
rel=["tipo-de-cambio", "paridad-del-poder-adquisitivo", "bienes-transables-y-no-transables", "depreciacion-y-apreciacion"],
))

T.append(dict(
slug="ventaja-comparativa", t="Ventaja comparativa y ventaja absoluta", cat="comercio", ic="🍇",
bcrp="Ventaja comparativa", alias="david ricardo adam smith especializacion comercio internacional",
corto="Un país tiene ventaja comparativa en lo que produce con menor costo de oportunidad. Especializarse en eso y comerciar beneficia a ambos países.",
simple=[
r"La <strong>ventaja absoluta</strong> (idea de Adam Smith) es producir algo con menos recursos que otro país. La <strong>ventaja comparativa</strong> (idea de David Ricardo) es producir algo con menor <a href=\"costo-de-oportunidad.html\">costo de oportunidad</a>, es decir, sacrificando menos de otros bienes.",
r"La lección de Ricardo es sorprendente: aunque un país sea mejor en todo (ventaja absoluta en todo), igual le conviene especializarse en aquello en que es <em>relativamente</em> mejor y comprar lo demás. Así, ambos países ganan con el comercio.",
],
ejemplo=[
r"Con su clima y sus valles costeros, el Perú puede producir arándanos y uvas en temporadas en que otros países no pueden. Le conviene exportarlos e importar, por ejemplo, maquinaria, que otros países fabrican con menor costo de oportunidad.",
],
rel=["costo-de-oportunidad", "arancel", "balanza-comercial", "exportaciones-tradicionales-y-no-tradicionales"],
))

T.append(dict(
slug="tasa-de-interes-activa-y-pasiva", t="Tasa de interés activa y pasiva", cat="dinero", ic="↔️",
bcrp="Tasa de interés activa", alias="tamn tamex tasa activa tasa pasiva spread margen financiero",
corto="La tasa activa es la que cobran los bancos por prestar; la pasiva, la que pagan por los depósitos. La diferencia es el margen (spread) del banco.",
simple=[
r"Para un banco, los préstamos son <strong>activos</strong> (dinero que le deben), por eso la tasa que cobra se llama <strong>activa</strong>. Los depósitos son <strong>pasivos</strong> (dinero que debe a sus clientes), por eso la tasa que paga se llama <strong>pasiva</strong>.",
r"La tasa activa siempre es mayor que la pasiva. La diferencia, llamada <strong>spread</strong> o margen financiero, cubre los costos del banco, el riesgo de que no le paguen y su ganancia.",
r"El BCRP y la SBS publican promedios del mercado, como la <strong>TAMN</strong> (tasa activa promedio en moneda nacional) y la <strong>TAMEX</strong> (en moneda extranjera).",
],
ejemplo=[
r"Si un banco paga 3 % a los depósitos a plazo y presta a 15 %, su spread es 12 puntos porcentuales.",
],
formula=dict(
tex=r"\text{Spread}=i_{\text{activa}}-i_{\text{pasiva}}",
calculo=[r"15\ \%-3\ \%=12\ \text{puntos porcentuales}"],
),
rel=["tasa-de-interes", "tcea", "trea", "tasa-de-referencia"],
))
