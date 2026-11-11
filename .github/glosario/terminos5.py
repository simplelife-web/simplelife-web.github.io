# -*- coding: utf-8 -*-
# Términos del glosario (parte 5): tercera tanda tomada de la lista del
# Glosario de Términos Económicos del BCRP. Las definiciones están
# redactadas con palabras propias; el campo "bcrp" guarda el nombre exacto
# del término en ese glosario para citarlo como fuente.

T = []

T.append(dict(
slug="economia", t="Economía", cat="mercados", ic="🌍",
bcrp="Economía", alias="ciencia económica escasez microeconomía macroeconomía",
corto="Es la ciencia que estudia cómo las personas, las empresas y los países deciden usar recursos escasos para satisfacer necesidades que no tienen fin.",
simple=[
r"Nadie tiene todo el dinero, el tiempo o los recursos que quisiera. Por eso hay que elegir, y cada elección tiene un <a href='costo-de-oportunidad.html'>costo de oportunidad</a>. La economía estudia cómo se toman esas decisiones y qué resultados producen.",
r"Se divide en dos grandes ramas. La <strong>microeconomía</strong> mira las decisiones de una familia, una empresa o un mercado, como el precio del pollo. La <strong>macroeconomía</strong> mira el país entero: <a href='pbi.html'>PBI</a>, <a href='inflacion.html'>inflación</a>, desempleo y <a href='tipo-de-cambio.html'>tipo de cambio</a>.",
],
ejemplo=[
r"Cuando decides si gastas tu gratificación en un viaje o la ahorras, haces microeconomía. Cuando el BCRP decide si sube su tasa de referencia para controlar la inflación, hace macroeconomía.",
],
rel=["costo-de-oportunidad", "oferta-y-demanda", "pbi", "inflacion"],
))

T.append(dict(
slug="banco-mundial", t="Banco Mundial", cat="comercio", ic="🌐",
bcrp="Banco Mundial", alias="BM BIRF organismo multilateral préstamos desarrollo",
corto="Es un organismo internacional que presta dinero y da asesoría a los países para proyectos de desarrollo y para reducir la pobreza.",
simple=[
r"Se creó en 1944, al final de la Segunda Guerra Mundial, junto con el Fondo Monetario Internacional (FMI). Al inicio ayudó a reconstruir Europa; hoy se enfoca en los países en desarrollo.",
r"Presta a largo plazo y con tasas más bajas que los bancos privados para obras como carreteras, agua, salud o educación. También publica muchas estadísticas que se usan en todo el mundo, como datos de pobreza o de inflación por país.",
r"No hay que confundirlo con el FMI: el FMI se ocupa sobre todo de la estabilidad financiera y de ayudar en crisis de balanza de pagos.",
],
ejemplo=[
r"Las cifras históricas de inflación del Perú que citamos en este glosario provienen de la base de datos del Banco Mundial.",
],
rel=["deuda-externa", "club-de-paris", "economias-emergentes", "pobreza-monetaria"],
))

T.append(dict(
slug="bono-cupon-cero", t="Bono cupón cero", cat="mercados", ic="0️⃣",
bcrp="Bono cupón cero", alias="bono descontado sin intereses periódicos",
corto="Es un bono que no paga intereses durante su vida. Se compra más barato que su valor y, al vencer, se cobra el valor completo.",
simple=[
r"Un <a href='bono.html'>bono</a> común paga intereses (cupones) cada cierto tiempo. El bono cupón cero no: se vende con <strong>descuento</strong> y la ganancia es la diferencia entre lo que pagaste y lo que recibes al final.",
r"Su precio depende mucho de la tasa de interés: si las tasas suben, el bono vale menos hoy. Por eso sirve para entender el <a href='valor-presente-y-valor-futuro.html'>valor presente</a>.",
],
ejemplo=[
r"Compras un bono cupón cero que pagará S/ 1000 dentro de 2 años. Si la tasa es 5 % anual, hoy pagarías unos S/ 907.",
],
formula=dict(
tex=r"P=\frac{VN}{(1+r)^n}",
donde=[(r"P", "precio hoy"), (r"VN", "valor que pagará al vencer"), (r"r", "tasa de interés anual"), (r"n", "años hasta el vencimiento")],
calculo=[r"P=\frac{1000}{(1.05)^2}\approx 907\ \text{soles}"],
),
rel=["bono", "valor-presente-y-valor-futuro", "rendimiento-al-vencimiento", "curva-de-rendimiento"],
))

T.append(dict(
slug="bono-corporativo", t="Bono corporativo", cat="mercados", ic="🏢",
bcrp="Bono corporativo", alias="bonos de empresas deuda privada",
corto="Es un bono que emite una empresa privada para conseguir dinero de muchos inversionistas, en lugar de pedir un préstamo al banco.",
simple=[
r"Una empresa grande que necesita financiar una planta o un proyecto puede emitir <strong>bonos corporativos</strong>: pide prestado a muchas personas e instituciones a la vez y se compromete a pagar intereses y devolver el dinero en una fecha.",
r"Pagan más que un <a href='bono-soberano.html'>bono soberano</a> porque es más probable que una empresa deje de pagar que el Estado. Esa diferencia es la <a href='prima-de-riesgo.html'>prima de riesgo</a>, y depende de su <a href='calificacion-de-riesgo.html'>calificación de riesgo</a>.",
],
ejemplo=[
r"En la Bolsa de Valores de Lima se negocian bonos de empresas peruanas de energía, bancos o retail. Las AFP compran muchos de ellos con el dinero de los fondos de pensiones.",
],
rel=["bono", "bono-soberano", "calificacion-de-riesgo", "mercado-de-capitales"],
))

T.append(dict(
slug="bonos-vac", t="Bonos VAC", cat="mercados", ic="🛡️",
bcrp="Bonos VAC", alias="bonos indexados a la inflación valor adquisitivo constante",
corto="Son bonos del Estado peruano cuyo valor se ajusta con la inflación, para que el inversionista no pierda poder adquisitivo.",
simple=[
r"VAC significa <strong>Valor Adquisitivo Constante</strong>. Es un índice que sigue la evolución de los precios. Los bonos VAC ajustan su capital según ese índice y, además, pagan una tasa de interés real.",
r"Así, si la inflación sube, el inversionista recibe más soles y su ganancia real queda protegida. Son útiles para quien necesita ingresos estables a largo plazo, como los fondos de pensiones.",
],
ejemplo=[
r"Inviertes S/ 10 000 en un bono VAC. Si la inflación del año es 3 %, tu capital pasa a valer S/ 10 300 en soles, y además cobras el interés real pactado sobre ese monto.",
],
formula=dict(
tex=r"\text{Capital ajustado}=\text{Capital}\times\frac{VAC_t}{VAC_0}",
donde=[(r"VAC_t", "índice VAC de hoy"), (r"VAC_0", "índice VAC al comprar el bono")],
calculo=[r"10\,000\times 1.03=10\,300\ \text{soles}"],
),
rel=["indexacion", "tasa-de-interes-real", "bono-soberano", "inflacion"],
))

T.append(dict(
slug="capitalizacion-bursatil", t="Capitalización bursátil", cat="mercados", ic="🏷️",
bcrp="Capitalización bursátil", alias="valor de mercado de una empresa market cap",
corto="Es cuánto vale una empresa en la bolsa: el precio de su acción multiplicado por el número de acciones.",
simple=[
r"La capitalización bursátil dice cuánto pagarías, en teoría, por comprar toda la empresa al precio de hoy en la <a href='bolsa-de-valores.html'>bolsa</a>. Cambia todos los días, porque el precio de la acción cambia.",
r"Si sumas la capitalización de todas las empresas listadas en una bolsa, obtienes el tamaño de ese mercado. Comparado con el PBI, sirve para medir qué tan desarrollado es el <a href='mercado-de-capitales.html'>mercado de capitales</a> de un país.",
],
ejemplo=[
r"Una empresa tiene 500 millones de acciones y cada una vale S/ 8. Su capitalización bursátil es S/ 4000 millones.",
],
formula=dict(
tex=r"\text{Capitalización}=P\times N",
donde=[(r"P", "precio de una acción"), (r"N", "número de acciones")],
calculo=[r"8\times 500\ \text{millones}=4000\ \text{millones de soles}"],
),
rel=["accion", "bolsa-de-valores", "indices-bursatiles", "mercado-de-capitales"],
))

T.append(dict(
slug="club-de-paris", t="Club de París", cat="estado", ic="🗼",
bcrp="Club de París", alias="acreedores oficiales renegociación de deuda",
corto="Es un grupo de países acreedores que se reúne para renegociar las deudas que otros Estados no pueden pagar.",
simple=[
r"Cuando un país tiene problemas para pagar préstamos a otros gobiernos, el <strong>Club de París</strong> ofrece un espacio para negociar: más plazo, menos intereses o, a veces, perdón de una parte de la deuda.",
r"No es un organismo con leyes propias, sino un foro informal de países ricos acreedores. Suele exigir que el país deudor tenga un programa económico serio, muchas veces acordado con el FMI.",
],
ejemplo=[
r"Tras la crisis de los años ochenta, cuando el Perú dejó de pagar gran parte de su deuda externa, el país renegoció en los noventa sus deudas con los acreedores oficiales del Club de París como parte de su regreso al sistema financiero internacional.",
],
rel=["deuda-externa", "deuda-publica", "banco-mundial", "riesgo-pais"],
))

T.append(dict(
slug="comunidad-andina", t="Comunidad Andina (CAN)", cat="comercio", ic="⛰️",
bcrp="Comunidad Andina - CAN", alias="CAN Pacto Andino integración Bolivia Colombia Ecuador",
corto="Es un bloque de integración formado por Bolivia, Colombia, Ecuador y el Perú, con libre comercio de bienes entre sus miembros.",
simple=[
r"Nació en 1969 como Pacto Andino. Hoy sus miembros comercian casi todos sus productos sin aranceles entre ellos y comparten algunas normas, por ejemplo sobre aduanas, transporte o propiedad intelectual.",
r"Gracias a la CAN, los ciudadanos de los países miembros pueden viajar entre ellos solo con su documento de identidad.",
],
ejemplo=[
r"Una empresa peruana que vende alimentos procesados a Ecuador o Colombia no paga aranceles en esos países por ser parte de la CAN, lo que le da ventaja frente a competidores de otras regiones.",
],
rel=["zona-de-libre-comercio", "arancel", "apertura-comercial", "salvaguardia-y-antidumping"],
))

T.append(dict(
slug="contrato-de-futuro", t="Contrato de futuro", cat="mercados", ic="⏳",
bcrp="Contrato de futuro", alias="futuros derivados bolsa de futuros",
corto="Es un acuerdo estandarizado, negociado en bolsa, para comprar o vender algo en una fecha futura a un precio que se fija hoy.",
simple=[
r"Con un futuro, comprador y vendedor fijan hoy el precio de una operación que se hará después. Se negocian en bolsas especializadas, con cantidades y fechas estándar, y la bolsa garantiza el cumplimiento pidiendo depósitos de garantía.",
r"Sirven para <strong>cubrirse</strong> del riesgo de precios o para especular. Son un tipo de <strong>derivado</strong>: su valor depende del precio de otro activo, como el cobre, el petróleo o una moneda.",
],
ejemplo=[
r"Una minera teme que el precio del cobre baje. Vende contratos de futuro de cobre a 6 meses a un precio fijo. Si el precio cae, pierde en la venta del metal, pero gana en los futuros, y su ingreso queda protegido.",
],
rel=["contrato-forward", "opcion", "swaps", "volatilidad"],
))

T.append(dict(
slug="contrato-forward", t="Contrato forward", cat="mercados", ic="📆",
bcrp="Contrato a término, contrato a plazo", alias="forward a plazo cobertura cambiaria",
corto="Es un acuerdo privado entre dos partes para comprar o vender algo en una fecha futura a un precio pactado hoy.",
simple=[
r"Se parece a un <a href='contrato-de-futuro.html'>futuro</a>, pero se negocia directamente entre las partes (por ejemplo, una empresa y su banco), con montos y fechas a la medida.",
r"En el Perú son muy usados los <strong>forwards de moneda</strong>: una empresa fija hoy el tipo de cambio al que comprará o venderá dólares en unos meses y así elimina el <a href='riesgo-cambiario.html'>riesgo cambiario</a>.",
],
ejemplo=[
r"Un importador debe pagar US$ 50 000 en 90 días. Firma un forward con su banco a S/ 3.75 por dólar. Pase lo que pase con el dólar, pagará S/ 187 500.",
],
formula=dict(
tex=r"\text{Pago en soles}=\text{Monto en US\$}\times TC_{\text{forward}}",
calculo=[r"50\,000\times 3.75=187\,500\ \text{soles}"],
),
rel=["riesgo-cambiario", "contrato-de-futuro", "tipo-de-cambio", "swaps"],
))

T.append(dict(
slug="opcion", t="Opción financiera", cat="mercados", ic="🔀",
bcrp="Opción", alias="opción call put derecho de compra",
corto="Es un contrato que da el derecho, pero no la obligación, de comprar o vender algo a un precio fijado, hasta una fecha.",
simple=[
r"Una <strong>opción call</strong> da el derecho a comprar; una <strong>opción put</strong>, el derecho a vender. Quien compra la opción paga un precio llamado <strong>prima</strong>.",
r"Si al final no te conviene usarla, simplemente no la ejerces y solo pierdes la prima. Por eso funcionan como un seguro: limitan la pérdida máxima.",
],
ejemplo=[
r"Compras una opción call para comprar una acción a S/ 10 dentro de 3 meses y pagas S/ 1 de prima. Si la acción sube a S/ 14, ejerces la opción y ganas S/ 3 (14 − 10 − 1). Si baja a S/ 8, no la usas y pierdes solo S/ 1.",
],
formula=dict(
tex=r"\text{Ganancia de un call}=\max(S-K,\,0)-\text{Prima}",
donde=[(r"S", "precio del activo al vencer"), (r"K", "precio pactado (de ejercicio)")],
calculo=[r"\max(14-10,\,0)-1=3\ \text{soles}"],
),
rel=["contrato-de-futuro", "contrato-forward", "accion", "volatilidad"],
))

T.append(dict(
slug="swaps", t="Swap", cat="mercados", ic="🔁",
bcrp="Swap de divisas", alias="permuta financiera swap cambiario swap de tasas",
corto="Es un acuerdo entre dos partes para intercambiar pagos durante un tiempo, por ejemplo una tasa fija por una variable, o soles por dólares.",
simple=[
r"En un <strong>swap de tasas</strong>, una parte paga una tasa fija y recibe una variable (o al revés). En un <strong>swap de divisas</strong>, se intercambian pagos en monedas distintas.",
r"Las empresas los usan para cambiar el tipo de deuda que tienen sin pedir un préstamo nuevo. El BCRP también usa <strong>swaps cambiarios</strong> para dar cobertura contra la subida del dólar sin vender sus reservas.",
],
ejemplo=[
r"Una empresa tiene un préstamo a tasa variable y teme que las tasas suban. Firma un swap con un banco: el banco le paga la tasa variable y ella paga una tasa fija. En la práctica, su deuda pasa a ser a tasa fija.",
],
rel=["tasa-fija-y-variable", "contrato-forward", "intervencion-cambiaria", "riesgo-cambiario"],
))

T.append(dict(
slug="control-cambiario", t="Control cambiario", cat="dinero", ic="🚧",
bcrp="Control cambiario", alias="cepo cambiario restricción de divisas dólar oficial",
corto="Es cuando el gobierno limita la compra y venta libre de moneda extranjera, por ejemplo fijando cupos o precios oficiales del dólar.",
simple=[
r"Con control cambiario, no puedes comprar todos los dólares que quieras al precio del mercado: el Estado decide cuánto, para qué y a qué precio. Suele aplicarse cuando faltan divisas o para frenar la salida de capitales.",
r"El problema es que casi siempre aparece un <strong>mercado paralelo</strong>, donde el dólar se vende más caro, y se generan escasez, corrupción y desconfianza.",
],
ejemplo=[
r"El Perú tuvo controles cambiarios y varios tipos de cambio oficiales en los años ochenta. Hoy, en cambio, cualquier persona puede comprar y vender dólares libremente.",
],
rel=["regimen-cambiario", "tipo-de-cambio", "divisa", "hiperinflacion"],
))

T.append(dict(
slug="cooperativa-de-ahorro-y-credito", t="Cooperativa de ahorro y crédito", cat="dinero", ic="🫱",
bcrp="Cooperativa de ahorro y crédito", alias="coopac cooperativas socios",
corto="Es una entidad cuyos dueños son sus propios socios, que ahorran y se prestan dinero entre ellos.",
simple=[
r"En una cooperativa, cada socio aporta capital y tiene voz y voto. La cooperativa recibe los ahorros de los socios y les presta, muchas veces en lugares o a personas que los bancos no atienden.",
r"En el Perú se llaman <strong>Coopac</strong>. Durante años tuvieron poca supervisión; hoy la SBS las supervisa. Aun así, antes de ahorrar en una conviene revisar que esté inscrita en el registro de la SBS y entender qué protección tienen tus depósitos.",
],
ejemplo=[
r"Los profesores de una región forman una cooperativa: cada uno ahorra un monto mensual y, cuando alguien necesita un préstamo para su casa, la cooperativa le presta a una tasa acordada por los socios.",
],
rel=["sbs", "sistema-financiero", "cajas-municipales", "intermediacion-financiera"],
))

T.append(dict(
slug="cofide", t="COFIDE", cat="dinero", ic="🏗️",
bcrp="Corporación Financiera de Desarrollo S.A -COFIDE-", alias="banco de desarrollo segundo piso",
corto="Es el banco de desarrollo del Estado peruano. Presta dinero a otras entidades financieras para que estas financien a empresas y proyectos.",
simple=[
r"COFIDE es un banco de <strong>segundo piso</strong>: normalmente no atiende al público, sino que canaliza recursos a bancos, cajas y otras entidades, que luego prestan a empresas y personas.",
r"El Estado lo usa para impulsar sectores que considera clave, como las micro y pequeñas empresas o la infraestructura, y en crisis puede administrar programas de apoyo.",
],
ejemplo=[
r"Una caja municipal recibe una línea de crédito de COFIDE para prestar a mypes agrícolas. El agricultor nunca habla con COFIDE, pero el dinero de su préstamo vino de ahí.",
],
rel=["banco-de-la-nacion", "sistema-financiero", "linea-de-credito", "cajas-municipales"],
))

T.append(dict(
slug="credit-crunch", t="Credit crunch (contracción del crédito)", cat="dinero", ic="🗜️",
bcrp="Credit crunch", alias="contracción del crédito sequía de crédito",
corto="Es cuando los bancos, de golpe, prestan mucho menos, aunque haya personas y empresas que quieran y puedan pagar.",
simple=[
r"En un <strong>credit crunch</strong>, los bancos se vuelven muy cautelosos: suben requisitos, cortan líneas de crédito o simplemente dejan de prestar. Suele pasar después de una crisis financiera, cuando temen más impagos o necesitan proteger su capital.",
r"Es peligroso porque las empresas no consiguen dinero para operar o invertir, lo que provoca despidos y una caída de la economía. Por eso los bancos centrales y los gobiernos suelen intervenir con programas de liquidez o garantías.",
],
ejemplo=[
r"Tras la crisis de las <a href='hipotecas-subprime.html'>hipotecas subprime</a> de 2008, muchos bancos de Estados Unidos y Europa redujeron fuertemente sus préstamos, lo que profundizó la recesión.",
],
rel=["hipotecas-subprime", "riesgo-de-liquidez", "recesion", "politica-anticiclica"],
))

T.append(dict(
slug="desestacionalizacion", t="Desestacionalización", cat="produccion", ic="🗓️",
bcrp="Desestacionalización", alias="serie desestacionalizada efecto estacional",
corto="Es quitar de una serie de datos los cambios que se repiten cada año en la misma época, para ver la tendencia real.",
simple=[
r"Muchas cifras suben o bajan siempre en los mismos meses: las ventas en diciembre, la pesca en temporada de anchoveta, el empleo en campañas agrícolas. Ese patrón es la <strong>estacionalidad</strong>.",
r"Si comparas diciembre con noviembre sin corregir, parecerá que la economía «explotó», cuando solo fue Navidad. La <strong>desestacionalización</strong> usa métodos estadísticos para quitar ese efecto y permitir comparar mes a mes.",
],
ejemplo=[
r"Las ventas de una tienda suben 40 % en diciembre todos los años. Si este diciembre subieron 45 %, el dato desestacionalizado mostrará solo un pequeño aumento real, no uno de 45 %.",
],
rel=["pbi", "ciclo-economico", "indicador-adelantado", "pbi-primario-y-no-primario"],
))

T.append(dict(
slug="economias-emergentes", t="Economías emergentes", cat="comercio", ic="🌅",
bcrp="Economías emergentes", alias="mercados emergentes países en desarrollo",
corto="Son países de ingreso medio que crecen y se integran a los mercados financieros mundiales, como el Perú, México o la India.",
simple=[
r"Las economías emergentes están entre los países ricos y los más pobres. Suelen crecer más rápido que los desarrollados, pero también son más sensibles a los cambios en las tasas de interés de Estados Unidos, al precio de las materias primas o a la confianza de los inversionistas.",
r"Los inversionistas comparan su riesgo con indicadores como el <a href='riesgo-pais.html'>riesgo país</a> (EMBI).",
],
ejemplo=[
r"Cuando la Reserva Federal de Estados Unidos sube sus tasas, el dinero suele salir de las economías emergentes y sus monedas, como el sol, tienden a depreciarse.",
],
rel=["riesgo-pais", "grado-de-inversion", "inversion-extranjera-en-cartera", "banco-mundial"],
))

T.append(dict(
slug="etf", t="ETF (fondo cotizado)", cat="mercados", ic="🧺",
bcrp="ETF", alias="exchange traded fund fondo indexado",
corto="Es un fondo de inversión que se compra y vende en la bolsa como si fuera una acción, y que suele copiar a un índice.",
simple=[
r"Un ETF junta el dinero de muchos inversionistas y lo invierte en una canasta de activos, por ejemplo todas las acciones de un <a href='indices-bursatiles.html'>índice</a>. Al comprar una sola cuota del ETF, ya estás <a href='portafolio.html'>diversificado</a>.",
r"A diferencia de un <a href='fondo-mutuo.html'>fondo mutuo</a> común, su precio cambia durante todo el día en la bolsa. Suelen cobrar comisiones bajas, porque solo replican el índice en lugar de elegir acciones.",
],
ejemplo=[
r"Con una sola compra de un ETF que replica el índice S&amp;P 500, inviertes a la vez en las 500 empresas grandes de Estados Unidos que forman ese índice.",
],
rel=["fondo-mutuo", "indices-bursatiles", "portafolio", "bolsa-de-valores"],
))

T.append(dict(
slug="euro", t="Euro", cat="comercio", ic="💶",
bcrp="Euro", alias="eurozona zona euro BCE",
corto="Es la moneda común que usan muchos países de la Unión Europea, administrada por el Banco Central Europeo.",
simple=[
r"El euro nació en 1999 para operaciones financieras y sus billetes y monedas empezaron a circular en 2002. Hoy lo usan una veintena de países de la Unión Europea, que forman la <strong>zona euro</strong>.",
r"Al compartir moneda, esos países no pueden tener su propia política monetaria: la decide el Banco Central Europeo para todos. Es el ejemplo más grande de <a href='union-monetaria.html'>unión monetaria</a>.",
],
ejemplo=[
r"Un turista peruano que viaja a España, Francia e Italia solo necesita cambiar sus soles a euros una vez, porque los tres países usan la misma moneda.",
],
rel=["divisa", "tipo-de-cambio", "regimen-cambiario", "zona-de-libre-comercio"],
))

T.append(dict(
slug="hipotecas-subprime", t="Hipotecas subprime", cat="finanzas", ic="🏚️",
bcrp="Hipotecas subprime", alias="crisis financiera 2008 hipotecas de alto riesgo",
corto="Eran créditos hipotecarios dados en Estados Unidos a personas con alto riesgo de no pagar. Su caída desató la crisis financiera de 2008.",
simple=[
r"Durante los años 2000, muchos bancos de EE. UU. prestaron para comprar casas a personas con ingresos inestables o mal historial, confiando en que el precio de las viviendas seguiría subiendo. Esos préstamos se empaquetaron en títulos y se vendieron a inversionistas de todo el mundo.",
r"Cuando las tasas subieron y los precios de las casas cayeron, muchos dejaron de pagar. Los títulos perdieron valor, varios bancos quebraron (como Lehman Brothers en 2008) y la crisis se extendió al mundo.",
],
ejemplo=[
r"La crisis llegó al Perú por la caída de los precios de los metales y de la demanda externa: en 2009 la economía peruana creció muy poco, aunque evitó una recesión profunda.",
],
ojo=["La lección: prestar sin evaluar bien la capacidad de pago es riesgoso, aunque haya una garantía, porque esa garantía también puede perder valor."],
rel=["credito-hipotecario", "credit-crunch", "riesgo-de-credito", "recesion"],
))

T.append(dict(
slug="indexacion", t="Indexación", cat="precios", ic="🔗",
bcrp="Indexación", alias="reajuste por inflación indexar",
corto="Es ajustar automáticamente un precio, sueldo o deuda según un índice, normalmente la inflación.",
simple=[
r"Si un contrato está <strong>indexado</strong>, su monto sube cuando sube el índice elegido. Así se protege el <a href='poder-adquisitivo.html'>poder adquisitivo</a> de quien recibe el pago.",
r"Ayuda a protegerse de la inflación, pero tiene un riesgo: si todo se indexa, la inflación de hoy se traslada automáticamente a los precios de mañana y es más difícil bajarla.",
],
ejemplo=[
r"Un contrato de alquiler de S/ 1500 se reajusta cada año según el IPC. Si la inflación fue 3 %, el nuevo alquiler será S/ 1545.",
],
formula=dict(
tex=r"\text{Monto nuevo}=\text{Monto anterior}\times(1+\pi)",
donde=[(r"\pi", "variación del índice (por ejemplo, la inflación)")],
calculo=[r"1500\times 1.03=1545\ \text{soles}"],
),
rel=["ipc", "bonos-vac", "inflacion", "poder-adquisitivo"],
herramienta=("Usa el IPC para actualizar montos de otros años", "../inflacion/"),
))

T.append(dict(
slug="indicador-adelantado", t="Indicador adelantado", cat="produccion", ic="🔭",
bcrp="Indicador adelantado", alias="indicadores líderes anticipan",
corto="Es un dato que suele moverse antes que la economía y por eso ayuda a anticipar hacia dónde va.",
simple=[
r"El <a href='pbi.html'>PBI</a> se conoce con retraso. Por eso los analistas miran datos que llegan antes y que suelen anticipar el ciclo: las expectativas de los empresarios, la venta de cemento, la importación de maquinaria o el consumo de electricidad.",
r"Ningún indicador es perfecto. Por eso se miran varios a la vez y se busca que apunten en la misma dirección.",
],
ejemplo=[
r"Si durante varios meses suben los despachos de cemento y la importación de bienes de capital, es probable que la construcción y la inversión estén creciendo, antes de que lo confirme el dato del PBI.",
],
rel=["expectativas", "ciclo-economico", "desestacionalizacion", "indice-de-confianza-empresarial"],
))

T.append(dict(
slug="indices-bursatiles", t="Índices bursátiles", cat="mercados", ic="📊",
bcrp="Indices bursátiles", alias="índice de bolsa S&P/BVL Dow Jones",
corto="Son números que resumen cómo se mueven los precios de un grupo de acciones de una bolsa.",
simple=[
r"En lugar de seguir cientos de acciones, se mira un <strong>índice</strong>, que promedia el comportamiento de las más representativas. Si el índice sube, en general las acciones subieron.",
r"Cada bolsa tiene los suyos. En el Perú, el principal es el S&amp;P/BVL Peru General; en EE. UU., el S&amp;P 500 y el Dow Jones. También sirven como referencia para fondos y ETF.",
],
ejemplo=[
r"Si un índice pasa de 20 000 a 21 000 puntos en un año, subió 5 %: en promedio, las acciones que lo forman se valorizaron 5 %.",
],
formula=dict(
tex=r"\text{Variación}=\frac{I_1-I_0}{I_0}\times 100",
calculo=[r"\frac{21\,000-20\,000}{20\,000}\times 100=5\ \%"],
),
rel=["bolsa-de-valores", "accion", "etf", "capitalizacion-bursatil"],
))

T.append(dict(
slug="indice-de-confianza-empresarial", t="Expectativas empresariales", cat="produccion", ic="🧭",
bcrp="Índice de confianza empresarial", alias="confianza empresarial expectativas de la economía encuesta",
corto="Es un indicador, basado en encuestas, que muestra si los empresarios son optimistas o pesimistas sobre la economía y sus negocios.",
simple=[
r"Cada mes se pregunta a empresas cómo ven la economía en los próximos meses, si piensan contratar más gente o invertir. Con las respuestas se arma un índice: por encima de 50 puntos, predominan los optimistas; por debajo, los pesimistas.",
r"Importa porque las <a href='expectativas.html'>expectativas</a> influyen en las decisiones: una empresa pesimista posterga inversiones, y eso frena la economía.",
],
ejemplo=[
r"El BCRP publica cada mes una encuesta de expectativas macroeconómicas a empresas. Si el indicador de expectativas a 3 meses baja de 50, es una señal de alerta sobre la inversión privada.",
],
rel=["expectativas", "indicador-adelantado", "inversion", "ciclo-economico"],
))

T.append(dict(
slug="meta-de-inflacion", t="Meta de inflación", cat="precios", ic="🎯",
bcrp="Meta de inflación", alias="metas explícitas de inflación rango meta inflation targeting",
corto="Es el nivel de inflación que el banco central se compromete públicamente a lograr. En el Perú, el rango meta va de 1 % a 3 % anual.",
simple=[
r"En un esquema de <strong>metas de inflación</strong>, el banco central anuncia su objetivo y usa su <a href='tasa-de-referencia.html'>tasa de referencia</a> para alcanzarlo. Si prevé que la inflación se saldrá del rango, ajusta la tasa.",
r"El BCRP usa este esquema desde 2002. Desde 2007, su meta es 2 %, con un margen de un punto hacia arriba o hacia abajo. Anunciar la meta ayuda a anclar las <a href='expectativas.html'>expectativas</a>: si la gente cree que la inflación será baja, fija precios y sueldos con eso en mente.",
],
ejemplo=[
r"Si la inflación sube a 4 % por un choque de alimentos, el BCRP evalúa si es temporal. Si cree que puede contagiar a otros precios, sube su tasa para devolverla al rango de 1 % a 3 %.",
],
formula=dict(
tex=r"\pi^{*}=2\ \%\pm 1\ \text{punto}\ \Rightarrow\ 1\ \%\le\pi\le 3\ \%",
donde=[(r"\pi^{*}", "meta de inflación del BCRP"), (r"\pi", "inflación anual")],
),
rel=["inflacion", "bcrp", "tasa-de-referencia", "reporte-de-inflacion", "regla-de-taylor"],
))

T.append(dict(
slug="insolvencia", t="Insolvencia", cat="finanzas", ic="🆘",
bcrp="Insolvencia", alias="quiebra no poder pagar deudas concurso",
corto="Es cuando una persona o empresa no puede pagar sus deudas porque lo que debe supera lo que tiene o lo que puede generar.",
simple=[
r"No es lo mismo que la falta de liquidez. Una empresa <strong>ilíquida</strong> tiene bienes, pero no tiene efectivo hoy para pagar. Una empresa <strong>insolvente</strong> no podría pagar aunque vendiera todo.",
r"En el Perú, una empresa insolvente puede entrar a un procedimiento concursal ante el Indecopi, donde los acreedores deciden si se reestructura o se liquida.",
],
ejemplo=[
r"Una empresa debe S/ 2 millones y todos sus bienes valen S/ 1.2 millones. Aunque venda todo, no alcanza: está insolvente.",
],
rel=["riesgo-de-liquidez", "riesgo-de-credito", "balance-general", "liquidez"],
))

T.append(dict(
slug="interes-moratorio", t="Interés moratorio", cat="finanzas", ic="⏰",
bcrp="Interés moratorio", alias="mora intereses por atraso penalidad",
corto="Es el interés adicional que se cobra cuando pagas una deuda después de la fecha acordada.",
simple=[
r"Una deuda normal genera un interés compensatorio, que es el precio de usar el dinero. Si te atrasas, además se puede cobrar un <strong>interés moratorio</strong>, que funciona como castigo por la demora.",
r"Por eso conviene pagar a tiempo: el atraso no solo suma intereses, también queda registrado en la <a href='central-de-riesgos.html'>central de riesgos</a> y puede dificultar créditos futuros.",
],
ejemplo=[
r"Debías pagar tu cuota el día 5 y la pagas el 20. Además de la cuota, el banco puede cobrarte intereses moratorios por esos 15 días de atraso, según lo que diga tu contrato.",
],
rel=["tasa-de-interes", "cartera-morosa", "central-de-riesgos", "tcea"],
))

T.append(dict(
slug="inversion-extranjera-en-cartera", t="Inversión extranjera de cartera", cat="comercio", ic="💼",
bcrp="Inversión extranjera en cartera", alias="inversión de portafolio capitales golondrinos",
corto="Es cuando extranjeros compran acciones o bonos de un país sin buscar controlar las empresas. Es dinero que puede entrar y salir rápido.",
simple=[
r"La <a href='inversion-extranjera-directa.html'>inversión extranjera directa</a> busca manejar una empresa a largo plazo. La <strong>inversión de cartera</strong>, en cambio, solo busca rentabilidad financiera: comprar bonos del Estado o acciones en bolsa.",
r"Ayuda a financiar al país, pero es más volátil: si cambia el humor de los mercados, esos capitales pueden salir en días y presionar al alza el tipo de cambio.",
],
ejemplo=[
r"Un fondo extranjero compra bonos soberanos peruanos en soles porque pagan buenas tasas. Si sube la tensión política, puede venderlos rápidamente, y al llevarse los dólares el sol tiende a depreciarse.",
],
rel=["inversion-extranjera-directa", "bono-soberano", "balanza-de-pagos", "economias-emergentes"],
))

T.append(dict(
slug="letra-de-cambio", t="Letra de cambio", cat="finanzas", ic="✉️",
bcrp="Letra de cambio", alias="título valor protesto girador aceptante",
corto="Es un documento en el que una persona ordena a otra pagar una suma de dinero en una fecha determinada.",
simple=[
r"En la letra participan tres personas: el <strong>girador</strong> (quien la emite), el <strong>aceptante</strong> (quien se compromete a pagar) y el <strong>beneficiario</strong> (quien cobra). Es un <strong>título valor</strong>: si no se paga, se puede cobrar por vía judicial de forma más rápida.",
r"Se usa mucho en ventas al crédito entre empresas. Si el aceptante no paga, la letra puede ser <strong>protestada</strong> y esa deuda puede aparecer en los registros de morosidad.",
],
ejemplo=[
r"Una ferretería compra mercadería por S/ 10 000 y acepta una letra a 60 días. El proveedor puede esperar el pago o llevar la letra a su banco para cobrarla antes, a cambio de un descuento.",
],
rel=["pagare", "linea-de-credito", "central-de-riesgos", "interes-moratorio"],
))

T.append(dict(
slug="linea-de-credito", t="Línea de crédito", cat="finanzas", ic="📏",
bcrp="Línea de crédito", alias="crédito revolvente monto aprobado",
corto="Es un monto máximo de dinero que un banco te aprueba para que lo uses cuando lo necesites, total o parcialmente.",
simple=[
r"A diferencia de un préstamo, en el que recibes todo el dinero de una vez, en una línea de crédito usas solo lo que necesitas y pagas intereses solo sobre lo usado. Cuando devuelves, puedes volver a usar ese monto.",
r"La <a href='tarjetas-de-credito-y-debito.html'>tarjeta de crédito</a> es el ejemplo más común. Las empresas también tienen líneas para capital de trabajo.",
],
ejemplo=[
r"Tu tarjeta tiene una línea de S/ 5000. Gastas S/ 1200, así que te quedan S/ 3800 disponibles. Si pagas los S/ 1200, vuelves a tener S/ 5000.",
],
formula=dict(
tex=r"\text{Disponible}=\text{Línea}-\text{Saldo usado}",
calculo=[r"5000-1200=3800\ \text{soles}"],
),
rel=["tarjetas-de-credito-y-debito", "creditos-de-consumo", "tcea", "central-de-riesgos"],
))

T.append(dict(
slug="mercado-primario-y-secundario", t="Mercado primario y secundario", cat="mercados", ic="🛍️",
bcrp="Mercado primario", alias="emisión colocación reventa bolsa",
corto="En el mercado primario se venden valores por primera vez. En el secundario, los inversionistas se los revenden entre ellos.",
simple=[
r"Cuando una empresa o el Estado emite acciones o bonos nuevos, los vende en el <strong>mercado primario</strong>: ahí recibe el dinero que necesita.",
r"Después, quien los compró puede venderlos a otro inversionista en el <strong>mercado secundario</strong>, como la <a href='bolsa-de-valores.html'>bolsa</a>. La empresa ya no recibe dinero, pero ese mercado es clave: da liquidez y hace que la gente se anime a comprar en el primario.",
],
ejemplo=[
r"El MEF subasta bonos soberanos nuevos: eso es mercado primario. Un mes después, una AFP vende parte de esos bonos a un banco: eso es mercado secundario.",
],
rel=["bolsa-de-valores", "mercado-de-capitales", "bono-soberano", "accion"],
))

T.append(dict(
slug="mercado-de-dinero", t="Mercado de dinero", cat="mercados", ic="⌛",
bcrp="Mercado de dinero", alias="money market corto plazo papeles comerciales",
corto="Es el mercado donde se presta y se pide dinero a corto plazo, normalmente a menos de un año.",
simple=[
r"Mientras el <a href='mercado-de-capitales.html'>mercado de capitales</a> financia proyectos de largo plazo, el <strong>mercado de dinero</strong> cubre necesidades de días o meses. Ahí se negocian préstamos interbancarios, certificados del BCRP, letras del Tesoro y papeles comerciales de empresas.",
r"Es muy líquido y de bajo riesgo, y sus tasas se mueven muy cerca de la <a href='tasa-de-referencia.html'>tasa de referencia</a>.",
],
ejemplo=[
r"Un banco al que le sobran soles por una noche se los presta a otro banco en el mercado interbancario, que es parte del mercado de dinero.",
],
rel=["tasa-de-interes-interbancaria", "operacion-de-mercado-abierto", "mercado-de-capitales", "liquidez"],
))

T.append(dict(
slug="miedo-a-flotar", t="Miedo a flotar", cat="dinero", ic="😟",
bcrp="Miedo a flotar", alias="fear of floating flotación administrada",
corto="Es cuando un país dice tener tipo de cambio flotante, pero su banco central interviene a menudo porque le preocupan los saltos del dólar.",
simple=[
r"El término lo popularizaron los economistas Guillermo Calvo y Carmen Reinhart. Observaron que muchos países emergentes declaran flotación, pero en la práctica evitan grandes movimientos del tipo de cambio.",
r"Ese «miedo» tiene razones: si muchas deudas están en dólares, una depreciación fuerte puede dañar a familias, empresas y bancos (el <a href='descalce-de-monedas.html'>descalce de monedas</a>). También porque el dólar influye en la inflación (el <a href='efecto-traspaso.html'>efecto traspaso</a>).",
],
ejemplo=[
r"La flotación administrada del Perú, con un BCRP que interviene para reducir la volatilidad, suele citarse en los estudios sobre este tema.",
],
rel=["regimen-cambiario", "intervencion-cambiaria", "descalce-de-monedas", "dolarizacion"],
))

T.append(dict(
slug="pagare", t="Pagaré", cat="finanzas", ic="📝",
bcrp="Pagaré", alias="título valor promesa de pago",
corto="Es un documento en el que una persona promete pagar una suma de dinero a otra en una fecha determinada.",
simple=[
r"A diferencia de la <a href='letra-de-cambio.html'>letra de cambio</a>, que es una orden de pago, el pagaré es una <strong>promesa</strong>: el mismo deudor firma que pagará. Es un título valor, así que se puede cobrar judicialmente de forma rápida.",
r"Los bancos suelen pedir que firmes un pagaré al darte un préstamo. Firmar un pagaré en blanco es riesgoso: lee bien y guarda una copia.",
],
ejemplo=[
r"Al recibir un préstamo de S/ 8000, firmas un pagaré por ese monto a 12 meses. Si dejas de pagar, el banco puede usarlo para iniciar el cobro judicial.",
],
rel=["letra-de-cambio", "creditos-de-consumo", "interes-moratorio", "amortizacion"],
))

T.append(dict(
slug="portafolio", t="Portafolio y diversificación", cat="finanzas", ic="🧺",
bcrp="Portafolio", alias="cartera de inversiones diversificar no poner todos los huevos",
corto="Un portafolio es el conjunto de inversiones de una persona o fondo. Diversificarlo es repartir el dinero para no depender de una sola inversión.",
simple=[
r"Si pones todo tu dinero en una sola acción y le va mal, pierdes mucho. Si lo repartes entre acciones, bonos, depósitos y distintas empresas o países, las pérdidas de unas se compensan con las ganancias de otras.",
r"Diversificar no elimina todo el riesgo (una crisis global afecta a casi todo), pero reduce el riesgo que depende de una sola empresa o sector.",
],
ejemplo=[
r"Un portafolio de S/ 10 000 con 40 % en un depósito a plazo, 40 % en un fondo de bonos y 20 % en un fondo de acciones es menos riesgoso que poner los S/ 10 000 en las acciones de una sola minera.",
],
formula=dict(
tex=r"r_p=w_1 r_1+w_2 r_2+\dots+w_n r_n",
donde=[(r"r_p", "rendimiento del portafolio"), (r"w_i", "peso de cada inversión (suman 1)"), (r"r_i", "rendimiento de cada inversión")],
calculo=[r"0.4(5\ \%)+0.4(6\ \%)+0.2(10\ \%)=6.4\ \%"],
),
rel=["rentabilidad", "fondo-mutuo", "etf", "volatilidad"],
))

T.append(dict(
slug="pbi-primario-y-no-primario", t="PBI primario y no primario", cat="produccion", ic="⛏️",
bcrp="PBI sectores primarios", alias="sectores primarios no primarios recursos naturales",
corto="El PBI primario viene de actividades ligadas a los recursos naturales. El no primario, del resto: industria, construcción, comercio y servicios.",
simple=[
r"En el Perú, el PBI <strong>primario</strong> incluye agro, pesca, minería e hidrocarburos y la manufactura que procesa esos recursos (como la harina de pescado o la refinación de metales). Depende mucho del clima y de la producción de las grandes minas.",
r"El PBI <strong>no primario</strong> incluye la manufactura no primaria, la electricidad, la construcción, el comercio y los servicios. Se relaciona más con la demanda interna y con el empleo urbano.",
],
ejemplo=[
r"Si un año entra en producción una mina grande, el PBI primario puede saltar aunque el comercio y la construcción crezcan poco. Por eso los analistas miran ambos por separado.",
],
rel=["pbi", "sectores-economicos", "exportaciones-tradicionales-y-no-tradicionales", "crecimiento-economico"],
))

T.append(dict(
slug="provisiones", t="Provisiones bancarias", cat="dinero", ic="🧯",
bcrp="Provisiones", alias="provisiones genéricas específicas cartera morosa",
corto="Son reservas que un banco separa de sus ganancias para cubrir los préstamos que probablemente no se cobrarán.",
simple=[
r"Un banco sabe que algunos clientes no pagarán. Por eso, en lugar de esperar la pérdida, va «guardando» una parte de sus ganancias como <strong>provisión</strong>. Así, cuando un préstamo no se cobra, la pérdida ya está cubierta.",
r"Hay <strong>provisiones genéricas</strong>, para toda la cartera sana, y <strong>específicas</strong>, para los créditos que ya muestran problemas. La SBS fija cuánto debe provisionarse según el riesgo de cada crédito.",
],
ejemplo=[
r"Si sube la <a href='cartera-morosa.html'>morosidad</a> en créditos de consumo, el banco debe aumentar sus provisiones. Eso reduce sus utilidades, aunque todavía no haya perdido el dinero.",
],
rel=["cartera-morosa", "riesgo-de-credito", "sbs", "central-de-riesgos"],
))

T.append(dict(
slug="rendimiento-al-vencimiento", t="Rendimiento al vencimiento", cat="mercados", ic="🏁",
bcrp="Rendimiento al vencimiento", alias="YTM yield tasa de rendimiento de un bono",
corto="Es la ganancia anual que obtendrías si compras un bono al precio de hoy y lo mantienes hasta que venza.",
simple=[
r"Un <a href='bono.html'>bono</a> paga cupones fijos, pero su precio cambia en el mercado. El <strong>rendimiento al vencimiento</strong> es la tasa que iguala lo que pagas hoy con todos los pagos que recibirás. Es como la <a href='tir.html'>TIR</a> del bono.",
r"Hay una regla clave: cuando el precio del bono baja, su rendimiento sube, y al revés. Por eso, cuando los inversionistas desconfían de un país, sus bonos caen de precio y sus rendimientos suben.",
],
ejemplo=[
r"Un bono que paga S/ 1100 en un año (S/ 1000 de capital más S/ 100 de cupón) cuesta hoy S/ 1050. Su rendimiento al vencimiento es de alrededor de 4.8 %.",
],
formula=dict(
tex=r"P=\sum_{t=1}^{n}\frac{C}{(1+y)^t}+\frac{VN}{(1+y)^n}",
donde=[(r"P", "precio hoy"), (r"C", "cupón de cada periodo"), (r"VN", "valor nominal"), (r"y", "rendimiento al vencimiento")],
calculo=[r"1050=\frac{1100}{1+y}\ \Rightarrow\ y\approx 4.8\ \%"],
),
rel=["bono", "tir", "curva-de-rendimiento", "bono-cupon-cero"],
))

T.append(dict(
slug="reporte-de-inflacion", t="Reporte de Inflación", cat="precios", ic="📘",
bcrp="Reporte de inflación", alias="informe de inflación BCRP proyecciones",
corto="Es el informe en el que el BCRP explica cómo ve la economía y presenta sus proyecciones de inflación y de crecimiento.",
simple=[
r"El BCRP publica su Reporte de Inflación cuatro veces al año. Ahí explica qué pasó con la inflación, el PBI, el sector externo y las finanzas públicas, y qué espera para los próximos años.",
r"Es una herramienta de <strong>transparencia</strong>: al explicar sus razones, el BCRP ayuda a que empresas y familias formen sus <a href='expectativas.html'>expectativas</a>, lo que hace más eficaz su política monetaria.",
],
ejemplo=[
r"Si en su reporte el BCRP proyecta que la inflación volverá al rango meta el próximo año, las empresas pueden fijar precios y sueldos con esa referencia.",
],
rel=["meta-de-inflacion", "bcrp", "politica-monetaria", "expectativas"],
))

T.append(dict(
slug="riesgo-de-credito", t="Riesgo de crédito", cat="finanzas", ic="🎯",
bcrp="Riesgo de crédito", alias="riesgo de impago default incumplimiento",
corto="Es la posibilidad de perder dinero porque quien te debe no te paga, total o parcialmente.",
simple=[
r"Todo el que presta asume riesgo de crédito: un banco, una AFP que compra bonos o una persona que le presta a un amigo. Para medirlo se mira la capacidad de pago, el historial (por ejemplo, en la <a href='central-de-riesgos.html'>central de riesgos</a>) y las garantías.",
r"Mientras mayor el riesgo, mayor la tasa que se cobra (la <a href='prima-de-riesgo.html'>prima de riesgo</a>). Los bancos se protegen con <a href='provisiones.html'>provisiones</a> y diversificando a quién prestan.",
],
ejemplo=[
r"Si un banco presta S/ 100 000 a 100 mypes y estima que 5 no pagarán, debe cobrar una tasa que cubra esas pérdidas esperadas, además de sus costos.",
],
formula=dict(
tex=r"\text{Pérdida esperada}=PD\times LGD\times EAD",
donde=[(r"PD", "probabilidad de incumplimiento"), (r"LGD", "parte que se pierde si no paga"), (r"EAD", "monto expuesto")],
calculo=[r"0.05\times 0.6\times 100\,000=3000\ \text{soles}"],
),
rel=["cartera-morosa", "provisiones", "calificacion-de-riesgo", "prima-de-riesgo"],
))

T.append(dict(
slug="riesgo-de-liquidez", t="Riesgo de liquidez", cat="finanzas", ic="💧",
bcrp="Riesgo de liquidez", alias="falta de efectivo corrida bancaria",
corto="Es el peligro de no tener efectivo a tiempo para pagar, aunque se tengan bienes de valor.",
simple=[
r"Un banco recibe depósitos que la gente puede retirar en cualquier momento, pero presta a plazos largos. Si muchos clientes retiran a la vez, puede no tener efectivo suficiente, aunque sus préstamos sean buenos. Ese es el <strong>riesgo de liquidez</strong>.",
r"Por eso los bancos deben mantener activos líquidos y <a href='encaje-bancario.html'>encaje</a>, y el BCRP puede prestarles en emergencias. Las personas también lo enfrentan: tener una casa no ayuda si mañana necesitas pagar una emergencia en efectivo.",
],
ejemplo=[
r"Tienes un departamento de S/ 300 000 pero solo S/ 500 en la cuenta. Si mañana necesitas S/ 5000 para una emergencia médica, tienes un problema de liquidez: vender el departamento toma meses.",
],
rel=["liquidez", "insolvencia", "encaje-bancario", "credit-crunch"],
))

T.append(dict(
slug="salvaguardia-y-antidumping", t="Salvaguardia y antidumping", cat="comercio", ic="🛑",
bcrp="Salvaguardia", alias="medidas de defensa comercial dumping derechos compensatorios",
corto="Son medidas temporales que un país puede aplicar para proteger a su industria de un aumento brusco de importaciones o de precios desleales.",
simple=[
r"Una <strong>salvaguardia</strong> limita las importaciones de un producto (con aranceles extra o cuotas) cuando entran tantas que dañan seriamente a los productores locales, aunque no haya competencia desleal.",
r"El <strong>antidumping</strong> se aplica cuando un exportador vende en otro país por debajo de lo que cobra en su propio mercado (el «dumping»). En el Perú, el Indecopi investiga estos casos y puede imponer derechos antidumping.",
],
ejemplo=[
r"Si una empresa extranjera vende tejidos en el Perú a un precio menor que en su país de origen, y eso daña a los fabricantes peruanos, el Indecopi puede fijar un derecho antidumping que encarezca esos tejidos.",
],
rel=["arancel", "apertura-comercial", "zona-de-libre-comercio", "monopolio"],
))

T.append(dict(
slug="secreto-bancario", t="Secreto bancario", cat="dinero", ic="🔒",
bcrp="Secreto bancario", alias="reserva bancaria confidencialidad",
corto="Es la obligación de los bancos de no revelar información sobre los depósitos y operaciones de sus clientes.",
simple=[
r"Tus depósitos y movimientos bancarios son privados: el banco no puede contárselos a cualquiera. En el Perú, la Constitución protege el secreto bancario como parte de la intimidad de las personas.",
r"No es absoluto. Puede levantarse por pedido de un juez, del fiscal de la Nación o de una comisión investigadora del Congreso, siempre que se relacione con el caso investigado. También hay reglas para que la SUNAT y la Unidad de Inteligencia Financiera reciban cierta información.",
],
ejemplo=[
r"Un vecino no puede ir al banco y pedir cuánto dinero tienes. En cambio, en una investigación por lavado de activos, un juez sí puede ordenar que el banco entregue tus movimientos.",
],
rel=["sbs", "sistema-financiero", "evasion-y-elusion-tributaria", "bancarizacion"],
))

T.append(dict(
slug="sectores-economicos", t="Sectores económicos", cat="produccion", ic="🧱",
bcrp="Sectores Económicos", alias="sector primario secundario terciario",
corto="Es la forma de agrupar las actividades de un país: el primario extrae recursos, el secundario los transforma y el terciario ofrece servicios.",
simple=[
r"El <strong>sector primario</strong> obtiene recursos de la naturaleza: agricultura, ganadería, pesca, minería e hidrocarburos. El <strong>secundario</strong> los transforma: manufactura, construcción y generación de electricidad. El <strong>terciario</strong> son los servicios: comercio, transporte, bancos, educación, salud y turismo.",
r"Al desarrollarse, los países suelen pasar de depender del sector primario a tener más peso en industria y servicios. En el Perú, la minería pesa mucho en las exportaciones, pero los servicios y el comercio dan la mayor parte del empleo.",
],
ejemplo=[
r"El café que se cosecha en Junín es sector primario; la planta que lo tuesta y envasa es sector secundario; la cafetería de Miraflores que lo vende en taza es sector terciario.",
],
rel=["pbi-primario-y-no-primario", "pbi", "valor-agregado", "productividad"],
))

T.append(dict(
slug="servicio-de-deuda", t="Servicio de la deuda", cat="estado", ic="🧾",
bcrp="Servicio de deuda", alias="pago de deuda intereses amortizaciones",
corto="Es lo que un país, empresa o persona paga en un periodo por sus deudas: intereses más amortización del capital.",
simple=[
r"Tener deuda no es malo en sí, pero hay que poder pagarla. El <strong>servicio de la deuda</strong> mide cuánto dinero se va cada año en cuotas, sumando intereses y la parte del capital que se devuelve.",
r"En el Estado, se compara con los ingresos o con las exportaciones: si el servicio de la deuda se come una parte muy grande, queda menos para salud, educación o inversión. La Constitución prohíbe aprobar un presupuesto sin incluir la partida para pagar la deuda pública.",
],
ejemplo=[
r"Si una familia gana S/ 4000 al mes y paga S/ 1600 en cuotas de préstamos, su servicio de deuda es 40 % de su ingreso: muy alto para cubrir imprevistos.",
],
formula=dict(
tex=r"\text{Servicio de deuda}=\text{Intereses}+\text{Amortización}",
calculo=[r"\frac{1600}{4000}\times 100=40\ \%\ \text{del ingreso}"],
),
rel=["deuda-publica", "amortizacion", "presupuesto-publico", "deuda-externa"],
))

T.append(dict(
slug="tasa-de-actividad", t="Tasa de actividad", cat="trabajo", ic="🧑‍🔧",
bcrp="Tasa de actividad", alias="tasa de participación PET PEA",
corto="Es el porcentaje de personas en edad de trabajar que trabajan o están buscando trabajo.",
simple=[
r"En el Perú, el INEI considera <strong>en edad de trabajar</strong> (PET) a las personas de 14 años a más. De ellas, las que trabajan o buscan activamente trabajo forman la <a href='pea.html'>PEA</a>. La tasa de actividad compara ambas.",
r"Si baja, puede ser porque más jóvenes estudian, porque más personas se jubilan o porque algunos se desaniman y dejan de buscar empleo. Por eso se mira junto con la <a href='tasa-de-desempleo.html'>tasa de desempleo</a>.",
],
ejemplo=[
r"Si en una ciudad hay 1 000 000 de personas de 14 años a más y 700 000 trabajan o buscan trabajo, la tasa de actividad es 70 %.",
],
formula=dict(
tex=r"\text{Tasa de actividad}=\frac{PEA}{PET}\times 100",
donde=[(r"PEA", "población económicamente activa"), (r"PET", "población en edad de trabajar")],
calculo=[r"\frac{700\,000}{1\,000\,000}\times 100=70\ \%"],
),
rel=["pea", "tasa-de-desempleo", "subempleo", "informalidad"],
))

T.append(dict(
slug="tasa-impositiva-marginal", t="Tasa impositiva marginal", cat="impuestos", ic="🪜",
bcrp="Tasa impositiva marginal", alias="tasa marginal tramos escala progresiva tasa media",
corto="Es el porcentaje de impuesto que pagas por el siguiente sol que ganas, según el tramo en el que estés.",
simple=[
r"En un impuesto progresivo, como el <a href='impuesto-a-la-renta.html'>impuesto a la renta</a> de trabajo en el Perú, la renta se divide en tramos y cada tramo paga su propia tasa (8 %, 14 %, 17 %, 20 % y 30 %). La tasa del último tramo que alcanzas es tu <strong>tasa marginal</strong>.",
r"Un error común es creer que si pasas a un tramo más alto, toda tu renta paga la tasa más alta. No es así: solo la parte que está dentro de ese tramo paga más. Por eso tu <strong>tasa media</strong> (impuesto total entre renta) siempre es menor que tu tasa marginal.",
],
ejemplo=[
r"Con la UIT de 2026 (S/ 5500), si tu renta neta es de 10 UIT, los primeros 5 UIT pagan 8 % y los otros 5 UIT pagan 14 %. Tu tasa marginal es 14 %, pero tu tasa media es 11 %.",
],
formula=dict(
tex=r"\text{Tasa media}=\frac{\text{Impuesto total}}{\text{Renta neta}}\times 100",
calculo=[r"\frac{0.08(5)+0.14(5)}{10}\times 100=11\ \%"],
),
rel=["impuesto-a-la-renta", "uit", "base-imponible", "impuesto-directo-e-indirecto"],
))

T.append(dict(
slug="tasa-fija-y-variable", t="Tasa fija y tasa variable", cat="finanzas", ic="📌",
bcrp="Tasa fija", alias="tasa de interés fija variable flotante",
corto="Con tasa fija, el interés no cambia durante el crédito. Con tasa variable, se ajusta según una tasa de referencia del mercado.",
simple=[
r"Con <strong>tasa fija</strong> sabes desde el inicio cuánto pagarás: la cuota no cambia aunque suban las tasas del mercado. A cambio, suele ser un poco más alta al comienzo.",
r"Con <strong>tasa variable</strong>, tu tasa se ajusta cada cierto tiempo según una referencia más un margen. Si las tasas bajan, pagas menos; si suben, pagas más. En el Perú, la mayoría de créditos a personas son a tasa fija.",
],
ejemplo=[
r"Tomas un crédito hipotecario a 20 años. Si eliges tasa fija, tu cuota de S/ 1800 se mantiene. Si eliges tasa variable y las tasas suben 2 puntos, tu cuota podría subir a más de S/ 2000.",
],
rel=["tasa-de-interes", "credito-hipotecario", "swaps", "tcea"],
))

T.append(dict(
slug="renta-fija-y-variable", t="Renta fija y renta variable", cat="mercados", ic="⚖️",
bcrp="Valor de renta fija", alias="instrumentos de renta fija variable bonos acciones",
corto="Las inversiones de renta fija pagan montos conocidos de antemano, como los bonos. Las de renta variable no garantizan un monto, como las acciones.",
simple=[
r"En la <strong>renta fija</strong>, el emisor se compromete a pagarte intereses y devolverte el capital en fechas establecidas: <a href='bono.html'>bonos</a>, depósitos a plazo o papeles comerciales. El riesgo principal es que el emisor no pague o que suban las tasas.",
r"En la <strong>renta variable</strong> no hay pagos asegurados: tu ganancia depende de cómo le vaya a la empresa y del precio en bolsa, como en las <a href='accion.html'>acciones</a>. Puede rendir más a largo plazo, pero con más altibajos.",
],
ejemplo=[
r"Un depósito a plazo al 4 % anual es renta fija: sabes que recibirás S/ 400 por cada S/ 10 000. Una acción puede subir 20 % o bajar 15 % en el mismo año: es renta variable.",
],
rel=["bono", "accion", "portafolio", "volatilidad"],
))

T.append(dict(
slug="volatilidad", t="Volatilidad", cat="mercados", ic="🌊",
bcrp="Volatilidad", alias="variabilidad desviación estándar riesgo de mercado",
corto="Mide cuánto suben y bajan los precios de un activo. Mientras más se mueve, más volátil y riesgoso es.",
simple=[
r"Si el precio de algo cambia poco día a día, es poco volátil. Si da saltos grandes, es muy volátil. La volatilidad se suele medir con la <strong>desviación estándar</strong> de los rendimientos.",
r"Más volatilidad significa más incertidumbre: puedes ganar mucho o perder mucho en poco tiempo. Por eso el BCRP busca reducir la volatilidad del <a href='tipo-de-cambio.html'>tipo de cambio</a>, y por eso los inversionistas piden más rendimiento por activos volátiles.",
],
ejemplo=[
r"Una acción minera que en un año sube y baja entre S/ 4 y S/ 8 es más volátil que un bono soberano cuyo precio se mueve apenas unos céntimos.",
],
formula=dict(
tex=r"\sigma=\sqrt{\frac{1}{n-1}\sum_{t=1}^{n}(r_t-\bar r)^2}",
donde=[(r"\sigma", "volatilidad (desviación estándar)"), (r"r_t", "rendimiento de cada periodo"), (r"\bar r", "rendimiento promedio")],
),
rel=["prima-de-riesgo", "portafolio", "intervencion-cambiaria", "renta-fija-y-variable"],
))

T.append(dict(
slug="union-monetaria", t="Unión monetaria", cat="comercio", ic="🤝",
bcrp="Unión monetaria", alias="moneda común unión económica",
corto="Es cuando varios países deciden usar la misma moneda y tener un solo banco central.",
simple=[
r"En una unión monetaria desaparece el tipo de cambio entre los miembros, lo que facilita el comercio, el turismo y las inversiones. A cambio, cada país renuncia a su propia política monetaria.",
r"Eso es un problema si un país entra en crisis y los demás no: no puede bajar su tasa de interés ni dejar que su moneda se deprecie para recuperarse. Por eso las uniones monetarias funcionan mejor entre economías parecidas y bien coordinadas.",
],
ejemplo=[
r"La zona del <a href='euro.html'>euro</a> es la unión monetaria más conocida. En la crisis de deuda de 2010-2012, Grecia no pudo devaluar su moneda para salir adelante porque usaba el euro.",
],
rel=["euro", "regimen-cambiario", "zona-de-libre-comercio", "politica-monetaria"],
))
