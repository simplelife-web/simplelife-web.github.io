# -*- coding: utf-8 -*-
# Términos del glosario (parte 7): quinta tanda tomada de la lista del
# Glosario de Términos Económicos del BCRP. Las definiciones están
# redactadas con palabras propias; el campo "bcrp" guarda el nombre exacto
# del término en ese glosario para citarlo como fuente.

T = []

T.append(dict(
slug="repo", t="Operación de reporte (repo)", cat="dinero", ic="🔄",
bcrp="Acuerdo de recompra, repo", alias="repo reporte compra con pacto de recompra inyección de liquidez",
corto="Es un préstamo de corto plazo disfrazado de compraventa: una parte vende un título y se compromete a recomprarlo después a un precio un poco mayor.",
simple=[
r"En un <strong>repo</strong>, quien necesita dinero entrega un título (por ejemplo, un bono) y recibe efectivo. Al vencer, devuelve el efectivo más un interés y recupera su título. El título funciona como garantía.",
r"El BCRP usa repos para <strong>inyectar liquidez</strong> a los bancos: les presta soles por días o meses a cambio de títulos, monedas o carteras de créditos como garantía. Es una de sus principales <a href='operacion-de-mercado-abierto.html'>operaciones de mercado abierto</a>.",
],
ejemplo=[
r"Un banco necesita S/ 100 millones por una semana. Entrega al BCRP bonos soberanos como garantía, recibe los soles y, a la semana, los devuelve con intereses y recupera sus bonos.",
],
rel=["operacion-de-mercado-abierto", "tasa-de-referencia", "liquidez", "deposito-overnight"],
))

T.append(dict(
slug="deposito-overnight", t="Depósito overnight en el BCRP", cat="dinero", ic="🌙",
bcrp="Depósito overnight en el BCRP", alias="depósito a un día facilidad de depósito corredor de tasas",
corto="Es la opción que tienen los bancos de dejar en el BCRP, de un día para otro, los soles que les sobran, ganando una tasa menor que la de referencia.",
simple=[
r"Al final del día, si un banco tiene soles de sobra y nadie se los pide prestados, puede depositarlos en el BCRP hasta el día siguiente. A cambio recibe una tasa de interés baja.",
r"Esa tasa funciona como un «piso» para la <a href='tasa-de-interes-interbancaria.html'>tasa interbancaria</a>: ningún banco prestará a otro más barato de lo que le pagaría el BCRP. Junto con la tasa de los préstamos de emergencia del BCRP, que funciona como «techo», forma un corredor alrededor de la <a href='tasa-de-referencia.html'>tasa de referencia</a>.",
],
ejemplo=[
r"Según Andina, en mayo de 2026 el BCRP mantuvo su tasa de referencia en 4.25 % y fijó en 2.25 % la tasa de los depósitos overnight, y en 4.75 % la de sus operaciones de reporte y créditos de regulación monetaria.",
],
rel=["tasa-de-referencia", "tasa-de-interes-interbancaria", "repo", "operacion-de-mercado-abierto"],
))

T.append(dict(
slug="certificados-de-deposito-del-bcrp", t="Certificados de depósito del BCRP (CD BCRP)", cat="dinero", ic="📄",
bcrp="Certificado de Depósito Negociable", alias="CD BCRP CDR certificados del BCRP esterilización",
corto="Son títulos que emite el BCRP para retirar soles del mercado: los bancos se los compran, le entregan soles y reciben intereses.",
simple=[
r"Cuando el BCRP quiere reducir la liquidez en soles, subasta <strong>certificados de depósito</strong>. Los bancos los compran con sus soles excedentes, que quedan «guardados» en el BCRP hasta el vencimiento.",
r"Son una herramienta clave para la <a href='esterilizacion.html'>esterilización</a>: si el BCRP compró dólares y puso soles en el mercado, puede retirarlos colocando CD BCRP. Además, como se negocian entre bancos, ayudan a formar una curva de tasas de corto plazo en soles.",
],
ejemplo=[
r"El BCRP subasta S/ 500 millones en CD BCRP a 3 meses. Los bancos que ganan la subasta le entregan esos soles y, al vencer, reciben su dinero más los intereses.",
],
rel=["esterilizacion", "operacion-de-mercado-abierto", "subastas", "curva-de-rendimiento"],
))

T.append(dict(
slug="redescuento", t="Redescuento", cat="dinero", ic="🆘",
bcrp="Redescuento", alias="ventanilla de descuento prestamista de última instancia créditos de regulación monetaria",
corto="Es el préstamo de emergencia que el banco central da a un banco que necesita liquidez urgente, a cambio de garantías.",
simple=[
r"Si un banco sano tiene un problema temporal de liquidez, puede acudir al banco central, que le presta por un plazo corto. Por eso se dice que el banco central es el <strong>prestamista de última instancia</strong>.",
r"Suele cobrar una tasa más alta que la de referencia, para que los bancos lo usen solo cuando de verdad lo necesitan y no como fuente normal de dinero.",
],
ejemplo=[
r"Si un banco sufre retiros inesperados un viernes, puede pedir un crédito de regulación monetaria al BCRP para atender a sus clientes, entregando bonos u otros activos como garantía.",
],
rel=["riesgo-de-liquidez", "repo", "deposito-overnight", "bcrp"],
))

T.append(dict(
slug="programa-monetario", t="Programa monetario", cat="dinero", ic="📅",
bcrp="Programa monetario", alias="decisión de política monetaria directorio del BCRP nota informativa",
corto="Es la reunión mensual en la que el Directorio del BCRP decide su tasa de referencia y explica sus razones en un comunicado.",
simple=[
r"Cada mes, en fechas anunciadas con anticipación, el Directorio del BCRP evalúa la inflación, la actividad económica y el contexto internacional. Luego decide si sube, baja o mantiene la <a href='tasa-de-referencia.html'>tasa de referencia</a>.",
r"La decisión se publica en una <strong>nota informativa</strong> que explica los motivos y da pistas de lo que podría venir. Anunciar las fechas y explicar las decisiones hace más predecible la política monetaria.",
],
ejemplo=[
r"Las noticias como «el BCRP mantuvo su tasa de referencia en 4.25 %» se publican el día del programa monetario, cuando sale la nota informativa del BCRP.",
],
rel=["tasa-de-referencia", "politica-monetaria", "reporte-de-inflacion", "bcrp"],
))

T.append(dict(
slug="mecanismos-de-transmision", t="Mecanismos de transmisión de la política monetaria", cat="dinero", ic="📡",
bcrp="Canal de expectativas", alias="canal de tasas de interés canal de crédito canal cambiario canal de expectativas",
corto="Son los caminos por los que un cambio en la tasa de referencia del banco central termina afectando el gasto, la producción y la inflación.",
simple=[
r"Cuando el BCRP sube su tasa, el efecto viaja por varios canales. Por el <strong>canal de tasas</strong>, suben los intereses de préstamos y depósitos. Por el <strong>canal de crédito</strong>, los bancos prestan con más cuidado. Por el <strong>canal cambiario</strong>, el sol puede apreciarse y abaratar importaciones. Por el <strong>canal de expectativas</strong>, la gente cree que la inflación bajará y fija precios con esa idea.",
r"Estos efectos no son inmediatos: suelen tardar varios trimestres en sentirse en la inflación. Por eso el BCRP decide mirando hacia adelante.",
],
ejemplo=[
r"Si el BCRP baja su tasa, con el tiempo los créditos se abaratan, las familias compran más a plazos y las empresas invierten más, lo que impulsa la economía.",
],
rel=["politica-monetaria", "tasa-de-referencia", "expectativas", "efecto-traspaso"],
))

T.append(dict(
slug="politica-monetaria-expansiva-y-contractiva", t="Política monetaria expansiva y contractiva", cat="dinero", ic="🎛️",
bcrp="Política monetaria acomodaticia", alias="acomodaticia restrictiva laxa dura",
corto="Es expansiva (o acomodaticia) cuando el banco central baja tasas para impulsar la economía, y contractiva (o restrictiva) cuando las sube para frenar la inflación.",
simple=[
r"Con una política <strong>expansiva</strong>, el banco central abarata el crédito para que la gente gaste e invierta más. Se usa cuando la economía está débil y la inflación está controlada.",
r"Con una política <strong>contractiva</strong>, encarece el crédito para enfriar la demanda y bajar la inflación. Saber si una tasa es expansiva o contractiva depende de compararla con una tasa «neutral», que ni impulsa ni frena.",
],
ejemplo=[
r"En 2020 el BCRP bajó su tasa a 0.25 % (muy expansiva) por la pandemia. En 2021 y 2022, cuando la inflación subió, la elevó varias veces (contractiva).",
],
rel=["politica-monetaria", "tasa-de-referencia", "politica-anticiclica", "regla-de-taylor"],
))

T.append(dict(
slug="ano-fiscal", t="Año fiscal", cat="estado", ic="📆",
bcrp="Año fiscal", alias="ejercicio fiscal periodo presupuestal",
corto="Es el periodo de doce meses que usa el Estado para su presupuesto y sus cuentas. En el Perú coincide con el año calendario.",
simple=[
r"El presupuesto público, la ejecución del gasto y el cálculo de varios impuestos se hacen por año fiscal. En el Perú va del 1 de enero al 31 de diciembre.",
r"Otros países usan fechas distintas: por ejemplo, el gobierno de Estados Unidos empieza su año fiscal el 1 de octubre.",
],
ejemplo=[
r"La declaración anual del impuesto a la renta que presentas entre marzo y abril corresponde a lo que ganaste en el año fiscal anterior, de enero a diciembre.",
],
rel=["presupuesto-publico", "impuesto-a-la-renta", "devengado", "politica-fiscal"],
))

T.append(dict(
slug="banco-de-pagos-internacionales", t="Banco de Pagos Internacionales (BPI)", cat="dinero", ic="🏦",
bcrp="Banco de Pagos Internacionales", alias="BIS Basilea banco de los bancos centrales",
corto="Es la institución internacional, con sede en Basilea (Suiza), que funciona como el «banco de los bancos centrales» y promueve la estabilidad financiera.",
simple=[
r"El BPI da servicios financieros a los bancos centrales, organiza su cooperación y publica estudios. Desde ahí se impulsan los <strong>acuerdos de Basilea</strong>, que fijan estándares de capital y liquidez para los bancos de todo el mundo.",
r"Esos estándares inspiran reglas como el <a href='ratio-de-capital-global.html'>ratio de capital global</a> que la SBS exige a los bancos peruanos.",
],
ejemplo=[
r"Las reglas que obligan a los bancos a tener suficiente capital para cubrir sus riesgos, que la SBS aplica en el Perú, se basan en recomendaciones del comité de Basilea del BPI.",
],
rel=["ratio-de-capital-global", "sbs", "bcrp", "organismos-multilaterales"],
))

T.append(dict(
slug="banca-electronica", t="Banca electrónica", cat="finanzas", ic="📱",
bcrp="Banca electrónica", alias="banca por internet banca móvil apps bancarias",
corto="Son los servicios bancarios que se usan por internet o por el celular, sin ir a una agencia: transferencias, pagos, consultas o préstamos.",
simple=[
r"Hoy muchas operaciones se hacen desde una app: pagar servicios, transferir a otros bancos, abrir depósitos o pedir créditos. Eso ahorra tiempo y costos.",
r"El riesgo principal es el fraude: mensajes falsos que piden tus claves, enlaces engañosos o llamadas de supuestos bancos. Los bancos nunca te piden tu clave completa ni tus códigos de seguridad.",
],
ejemplo=[
r"Pagar la luz desde la app del banco a medianoche, sin hacer cola, es banca electrónica.",
],
ojo=["Nunca compartas claves ni códigos que te llegan por SMS, aunque quien llama diga que es del banco."],
rel=["sistema-de-pagos", "bancarizacion", "tarjetas-de-credito-y-debito", "camara-de-compensacion"],
))

T.append(dict(
slug="banco-de-inversion", t="Banco de inversión", cat="mercados", ic="🏙️",
bcrp="Banco de inversiones", alias="banca de inversión estructuración emisiones asesoría",
corto="Es una entidad que ayuda a empresas y gobiernos a conseguir financiamiento en los mercados, emitiendo acciones o bonos, y asesora en compras y fusiones de empresas.",
simple=[
r"A diferencia de un banco comercial, que recibe depósitos y presta, un banco de inversión <strong>estructura y coloca</strong> emisiones de valores, asesora en <a href='fusion-y-adquisicion.html'>fusiones y adquisiciones</a> y opera en mercados financieros.",
r"Gana comisiones por esos servicios. Grandes nombres internacionales son ejemplos típicos; en el Perú, estas funciones suelen estar en áreas de los bancos grandes o en sociedades agentes de bolsa.",
],
ejemplo=[
r"Si una empresa peruana quiere emitir bonos por US$ 300 millones en el exterior, contrata bancos de inversión que preparan la emisión y buscan inversionistas que los compren.",
],
rel=["mercado-de-capitales", "bono-corporativo", "fusion-y-adquisicion", "mercado-primario-y-secundario"],
))

T.append(dict(
slug="base-tributaria", t="Base tributaria", cat="impuestos", ic="👥",
bcrp="Base tributaria", alias="universo de contribuyentes ampliar la base tributaria",
corto="Es el conjunto de personas, empresas y actividades que pagan impuestos. «Ampliar la base» significa que más gente y más actividades tributen.",
simple=[
r"No hay que confundirla con la <a href='base-imponible.html'>base imponible</a>, que es el monto sobre el que se calcula un impuesto. La <strong>base tributaria</strong> mira cuántos contribuyen.",
r"En el Perú, la base tributaria es estrecha por la alta <a href='informalidad.html'>informalidad</a>: pocos contribuyentes pagan la mayor parte. Ampliarla permite recaudar más sin subir las tasas.",
],
ejemplo=[
r"Cuando la SUNAT logra que miles de pequeños negocios se formalicen y emitan comprobantes, amplía la base tributaria aunque las tasas de los impuestos no cambien.",
],
rel=["base-imponible", "presion-tributaria", "informalidad", "evasion-y-elusion-tributaria"],
))

T.append(dict(
slug="bono-subordinado", t="Bono subordinado", cat="mercados", ic="🪜",
bcrp="Bono subordinado", alias="deuda subordinada capital de segundo nivel",
corto="Es un bono que, si la empresa quiebra, se paga después de las demás deudas. Por eso es más riesgoso y paga una tasa más alta.",
simple=[
r"Si una empresa no puede pagar a todos, primero cobran los acreedores principales y recién después los dueños de <strong>deuda subordinada</strong>. Ese mayor riesgo se compensa con un interés mayor.",
r"Los bancos emiten bonos subordinados porque, bajo ciertas condiciones, cuentan como parte de su capital regulatorio (patrimonio efectivo), lo que les permite prestar más.",
],
ejemplo=[
r"Un banco emite bonos subordinados a 10 años que pagan 1.5 puntos más que sus bonos normales. Si el banco quebrara, esos bonistas cobrarían después de los depositantes y otros acreedores.",
],
rel=["bono", "bono-corporativo", "ratio-de-capital-global", "prima-de-riesgo"],
))

T.append(dict(
slug="bono-de-reconocimiento", t="Bono de reconocimiento", cat="trabajo", ic="📜",
bcrp="Bono de reconocimiento", alias="ONP AFP traslado aportes SNP SPP",
corto="Es un documento que emite la ONP para reconocer los aportes que una persona hizo al sistema público antes de pasarse a una AFP.",
simple=[
r"Si un trabajador aportó a la ONP (Sistema Nacional de Pensiones) y luego se cambió a una AFP (Sistema Privado de Pensiones), no pierde esos aportes. El Estado le entrega un <strong>bono de reconocimiento</strong> que representa ese dinero.",
r"El bono se redime, es decir, se convierte en dinero en su cuenta de la AFP, cuando la persona se jubila o en otros casos que fija la ley, como invalidez o fallecimiento, siempre que cumpla los requisitos.",
],
ejemplo=[
r"Ana aportó 6 años a la ONP y luego pasó a una AFP. Al jubilarse, su bono de reconocimiento se suma al fondo de su cuenta individual y aumenta su pensión.",
],
rel=["afp-y-onp", "tasa-de-dependencia", "bono", "valor-presente-y-valor-futuro"],
))

T.append(dict(
slug="titulizacion", t="Titulización", cat="mercados", ic="📦",
bcrp="Bonos de titulización", alias="bonos de titulización securitización flujos futuros",
corto="Es convertir activos que generan pagos futuros, como préstamos o alquileres, en títulos que se venden a inversionistas.",
simple=[
r"Una empresa o banco junta activos que producen flujos de dinero (cuotas de créditos, cobros de peajes, alquileres) y los pasa a un patrimonio separado. Con ese respaldo se emiten <strong>bonos de titulización</strong>.",
r"Así, la empresa obtiene dinero hoy, y los inversionistas cobran con los flujos de esos activos. Bien usada, da financiamiento; mal usada, como en la crisis de las <a href='hipotecas-subprime.html'>hipotecas subprime</a>, puede esconder riesgos.",
],
ejemplo=[
r"Un centro comercial titulizado emite bonos que se pagan con los alquileres de las tiendas. Los inversionistas reciben su dinero de esos alquileres, no del resto del negocio del dueño.",
],
rel=["bono", "fideicomiso", "hipotecas-subprime", "mercado-de-capitales"],
))

T.append(dict(
slug="bonos-globales", t="Bonos globales", cat="estado", ic="🌎",
bcrp="Bonos Globales de Tesoro Público", alias="bonos globales emisión internacional deuda en dólares",
corto="Son bonos que emite el Estado peruano en los mercados internacionales, normalmente en dólares o euros, para financiarse con inversionistas extranjeros.",
simple=[
r"Además de vender <a href='bono-soberano.html'>bonos soberanos</a> en soles en el mercado local, el Perú emite <strong>bonos globales</strong> que se negocian en mercados como Nueva York.",
r"Permiten acceder a muchos inversionistas y plazos largos. La tasa que pagan refleja el <a href='riesgo-pais.html'>riesgo país</a>: mientras mejor es la calificación del Perú, más baratos son.",
],
ejemplo=[
r"Si el Perú coloca US$ 2000 millones en bonos globales a 30 años, obtiene financiamiento de largo plazo para su presupuesto, pero tendrá que pagar intereses en dólares.",
],
rel=["bono-soberano", "deuda-externa", "riesgo-pais", "grado-de-inversion"],
))

T.append(dict(
slug="letras-del-tesoro", t="Letras del Tesoro", cat="estado", ic="🗒️",
bcrp="Letras de Tesorería", alias="letras del tesoro deuda de corto plazo",
corto="Son títulos de deuda de corto plazo, menos de un año, que emite el Tesoro Público para cubrir necesidades temporales de caja.",
simple=[
r"El Estado no recibe sus ingresos al mismo ritmo que paga sus gastos. Para cubrir esos desfases, el Tesoro emite <strong>letras</strong> a plazos cortos, que se venden con descuento y se pagan completas al vencer, como un <a href='bono-cupon-cero.html'>bono cupón cero</a>.",
r"Son de muy bajo riesgo y sus tasas sirven como referencia para el mercado de corto plazo.",
],
ejemplo=[
r"Un banco compra una letra del Tesoro a 6 meses por S/ 980 que pagará S/ 1000 al vencer. Gana S/ 20 en ese plazo.",
],
rel=["bono-cupon-cero", "mercado-de-dinero", "deuda-interna", "bono-soberano"],
))

T.append(dict(
slug="caja-rural", t="Caja rural de ahorro y crédito", cat="dinero", ic="🌾",
bcrp="Caja rural de ahorro y crédito", alias="cajas rurales microfinanzas agro",
corto="Es una entidad financiera regulada por la SBS que capta ahorros y presta, sobre todo, a pequeñas empresas y al sector rural y agropecuario.",
simple=[
r"Las cajas rurales nacieron para llevar crédito al campo, donde los bancos casi no llegaban. Hoy prestan también a micro y pequeñas empresas urbanas.",
r"Como las <a href='cajas-municipales.html'>cajas municipales</a>, son parte de las <strong>microfinanzas</strong>. Están supervisadas por la <a href='sbs.html'>SBS</a> y sus depósitos están protegidos por el Fondo de Seguro de Depósitos, con los límites de ley.",
],
ejemplo=[
r"Un productor de papa de Huancavelica pide un crédito a una caja rural para comprar semillas y fertilizantes, y lo devuelve después de la cosecha.",
],
rel=["cajas-municipales", "sistema-financiero", "sbs", "bancarizacion"],
))

T.append(dict(
slug="camara-de-compensacion", t="Cámara de Compensación Electrónica (CCE)", cat="dinero", ic="🔀",
bcrp="Cámara de Compensación Electrónica", alias="CCE transferencias interbancarias cheques transferencias inmediatas",
corto="Es la entidad que procesa los cheques y las transferencias entre bancos distintos, para que el dinero llegue de una cuenta a otra.",
simple=[
r"Cuando transfieres dinero de tu banco a una cuenta de otro banco, la operación pasa por la <strong>CCE</strong>. Esta junta todas las órdenes del día, calcula cuánto debe cada banco a los demás y luego se liquidan los saldos en las cuentas que los bancos tienen en el BCRP.",
r"Ese cálculo neto se llama <strong>compensación</strong>: en lugar de mover millones de pagos uno por uno, cada banco solo paga o recibe la diferencia. Hoy existen también transferencias inmediatas, que llegan en segundos.",
],
ejemplo=[
r"Si pagas el alquiler con una transferencia interbancaria usando el CCI (código de cuenta interbancario) del dueño, la CCE se encarga de que el dinero pase de tu banco al suyo.",
],
rel=["sistema-de-pagos", "banca-electronica", "cheque", "bcrp"],
))

T.append(dict(
slug="cheque", t="Cheque", cat="finanzas", ic="🧾",
bcrp="Cheque", alias="cheque de gerencia cheque sin fondos girar endosar",
corto="Es una orden escrita para que un banco pague una suma de dinero, de la cuenta de quien lo firma, a otra persona.",
simple=[
r"Quien firma el cheque (el <strong>girador</strong>) ordena a su banco pagar al <strong>beneficiario</strong>. El beneficiario puede cobrarlo en ventanilla o depositarlo en su cuenta. Si es de otro banco, pasa por la <a href='camara-de-compensacion.html'>Cámara de Compensación</a>.",
r"Si la cuenta no tiene fondos, el cheque es rechazado. Por eso para pagos grandes se usa a veces el <strong>cheque de gerencia</strong>, que emite el propio banco y tiene el pago asegurado. Hoy los cheques se usan cada vez menos, reemplazados por las transferencias.",
],
ejemplo=[
r"Al comprar un auto usado, el vendedor puede pedir un cheque de gerencia para estar seguro de que el dinero existe.",
],
rel=["camara-de-compensacion", "letra-de-cambio", "sistema-de-pagos", "banca-electronica"],
))

T.append(dict(
slug="capacidad-de-endeudamiento", t="Capacidad de endeudamiento", cat="finanzas", ic="📏",
bcrp="Capacidad de endeudamiento", alias="capacidad de pago cuánto me pueden prestar ratio deuda ingreso",
corto="Es cuánto puede deber una persona, empresa o país sin poner en riesgo su capacidad de pagar.",
simple=[
r"Para decidir cuánto prestar, los bancos miran cuánto ganas, cuánto ya debes y cuánto gastas. Una regla práctica es que la suma de tus cuotas no supere una parte razonable de tu ingreso, por ejemplo alrededor de un tercio.",
r"Para un país, se mira la deuda frente al PBI, el <a href='servicio-de-deuda.html'>servicio de la deuda</a> frente a los ingresos y en qué moneda está la deuda.",
],
ejemplo=[
r"Si ganas S/ 3600 al mes y ya pagas S/ 400 de cuotas, con un límite de un tercio de tu ingreso (S/ 1200), podrías asumir una cuota adicional de hasta S/ 800.",
],
formula=dict(
tex=r"\text{Cuota máxima adicional}=\frac{\text{Ingreso}}{3}-\text{Cuotas actuales}",
calculo=[r"\frac{3600}{3}-400=800\ \text{soles}"],
),
rel=["servicio-de-deuda", "central-de-riesgos", "creditos-de-consumo", "deuda-publica"],
))

T.append(dict(
slug="capital", t="Capital", cat="produccion", ic="⚒️",
bcrp="Capital", alias="factor de producción capital físico capital financiero capital humano",
corto="Es el conjunto de bienes y recursos que se usan para producir otros bienes, como máquinas, edificios o dinero invertido.",
simple=[
r"En economía, el <strong>capital físico</strong> son las máquinas, herramientas, edificios e infraestructura. Es uno de los factores de producción, junto con el trabajo y los recursos naturales.",
r"La palabra también se usa para el <strong>capital financiero</strong> (el dinero que se invierte o se presta) y para el <strong>capital humano</strong> (los conocimientos y habilidades de las personas, que se aumentan con educación y experiencia).",
],
ejemplo=[
r"Un taxista que compra un segundo auto para trabajar con otro chofer aumenta su capital físico. Si estudia un curso de mecánica, aumenta su capital humano.",
],
rel=["inversion", "bienes-de-capital-y-de-consumo", "fuentes-de-crecimiento", "consumo-de-capital-fijo"],
))

T.append(dict(
slug="consumo-de-capital-fijo", t="Consumo de capital fijo (depreciación)", cat="produccion", ic="⏳",
bcrp="Consumo de capital fijo", alias="depreciación desgaste del capital inversión neta",
corto="Es el desgaste que sufren las máquinas, edificios e infraestructura con el uso y el paso del tiempo.",
simple=[
r"Todo capital se gasta: una máquina se avería, un edificio envejece, una computadora queda obsoleta. Ese desgaste es el <strong>consumo de capital fijo</strong>, también llamado depreciación.",
r"Por eso la inversión bruta no es igual al aumento real del capital: hay que restar lo que se desgastó. Si un país invierte menos de lo que se deprecia, su capital disminuye.",
],
ejemplo=[
r"Si un año se invierten S/ 200 000 millones en capital fijo y el desgaste se estima en S/ 120 000 millones, la inversión neta es S/ 80 000 millones.",
],
formula=dict(
tex=r"\text{Inversión neta}=\text{Inversión bruta}-\text{Depreciación}",
calculo=[r"200\,000-120\,000=80\,000\ \text{millones}"],
),
rel=["formacion-bruta-de-capital", "capital", "inversion", "ingreso-nacional"],
))

T.append(dict(
slug="cavali", t="Cavali", cat="mercados", ic="🗄️",
bcrp="Cavali I.L.C.V. S.A.", alias="institución de compensación y liquidación de valores registro de valores",
corto="Es la entidad que registra quién es dueño de las acciones y bonos en el Perú y se encarga de que las operaciones de bolsa se paguen y se entreguen.",
simple=[
r"Hoy las acciones y bonos casi no existen en papel: son registros electrónicos. <strong>Cavali</strong> lleva ese registro central y, cuando alguien compra o vende en bolsa, asegura que el comprador reciba los valores y el vendedor reciba el dinero.",
r"Esta función de <strong>compensación y liquidación</strong> da seguridad al mercado. Cada inversionista puede consultar sus valores registrados a su nombre.",
],
ejemplo=[
r"Si compras acciones a través de una sociedad agente de bolsa, esas acciones quedan anotadas a tu nombre en Cavali, aunque nunca recibas un papel.",
],
rel=["bolsa-de-valores", "mercado-de-capitales", "accion", "mercado-primario-y-secundario"],
))

T.append(dict(
slug="cono-monetario", t="Cono monetario", cat="dinero", ic="🪙",
bcrp="Cono monetario", alias="denominaciones de billetes y monedas sol céntimos",
corto="Es el conjunto de billetes y monedas de distintos valores que circulan en un país.",
simple=[
r"En el Perú, los billetes son de S/ 10, 20, 50, 100 y 200, y las monedas de 10, 20 y 50 céntimos y de S/ 1, 2 y 5. El BCRP decide qué denominaciones existen y las adapta a las necesidades de pago.",
r"Con el tiempo, las monedas muy pequeñas se dejan de usar: el BCRP retiró de circulación las de 1 y 5 céntimos porque costaba más fabricarlas que lo que valían y casi no se usaban.",
],
ejemplo=[
r"Por eso, cuando pagas en efectivo, los montos se redondean a los 10 céntimos más cercanos según las reglas del BCRP.",
],
rel=["circulante", "curso-legal", "elemento-de-seguridad", "valor-numismatico"],
))

T.append(dict(
slug="elemento-de-seguridad", t="Elementos de seguridad de los billetes", cat="dinero", ic="🔍",
bcrp="Elemento de seguridad", alias="billete falso marca de agua hilo de seguridad toca mira gira",
corto="Son las características especiales de los billetes, como la marca de agua o el hilo de seguridad, que permiten reconocer si son auténticos.",
simple=[
r"Los billetes tienen elementos difíciles de copiar. Al <strong>tocar</strong>, se siente el relieve de algunas partes. Al <strong>mirar</strong> a contraluz, aparecen la marca de agua y el hilo de seguridad. Al <strong>girar</strong> el billete, algunos elementos cambian de color o de imagen.",
r"El BCRP difunde estos elementos para que cualquier persona pueda revisar un billete en segundos. Un billete falso no tiene valor: si lo recibes, pierdes ese dinero.",
],
ejemplo=[
r"Si te dan un billete de S/ 100 que se siente liso y, al mirarlo a contraluz, no muestra marca de agua, lo más probable es que sea falso.",
],
ojo=["Revisa los billetes de alta denominación en el momento en que los recibes, sobre todo de noche o en lugares con poca luz."],
rel=["circulante", "cono-monetario", "bcrp", "curso-legal"],
))

T.append(dict(
slug="inti", t="Inti", cat="precios", ic="☀️",
bcrp="Inti", alias="moneda peruana 1985 1991 sol de oro nuevo sol",
corto="Fue la moneda del Perú entre 1985 y 1991. Perdió casi todo su valor durante la hiperinflación y fue reemplazada por el nuevo sol.",
simple=[
r"El inti reemplazó al sol de oro en 1985: un inti equivalía a mil soles de oro. A fines de los ochenta, la <a href='hiperinflacion.html'>hiperinflación</a> hizo que los precios subieran a una velocidad enorme y aparecieron billetes de millones de intis.",
r"En 1991 se creó el <strong>nuevo sol</strong>: un nuevo sol equivalía a un millón de intis. Desde fines de 2015, la moneda se llama simplemente <strong>sol</strong>.",
],
ejemplo=[
r"Algo que en 1985 costaba 1 inti, a inicios de los noventa podía costar cientos de miles de intis. Hoy, los billetes de intis solo tienen <a href='valor-numismatico.html'>valor de colección</a>.",
],
formula=dict(
tex=r"1\ \text{sol}=10^{6}\ \text{intis}=10^{9}\ \text{soles de oro}",
),
rel=["hiperinflacion", "estabilidad-monetaria", "curso-legal", "inflacion"],
))

T.append(dict(
slug="valor-numismatico", t="Valor numismático", cat="dinero", ic="🏅",
bcrp="Valor numismático", alias="monedas de colección numismática",
corto="Es el valor que tiene una moneda o billete como objeto de colección, que puede ser mayor que su valor para pagar.",
simple=[
r"Una moneda tiene un <strong>valor facial</strong> (lo que dice que vale) y, a veces, un <strong>valor numismático</strong>, que depende de su rareza, antigüedad, estado y demanda de coleccionistas.",
r"El BCRP ha emitido series de monedas conmemorativas, por ejemplo sobre riqueza cultural y natural del Perú. Siguen siendo de curso legal, pero muchos las guardan como colección.",
],
ejemplo=[
r"Una moneda de S/ 1 conmemorativa sirve para pagar S/ 1, pero un coleccionista podría pagar más por ella si está en perfecto estado y le falta en su colección.",
],
rel=["cono-monetario", "inti", "curso-legal", "circulante"],
))

T.append(dict(
slug="creacion-y-desviacion-de-comercio", t="Creación y desviación de comercio", cat="comercio", ic="↪️",
bcrp="Creación de comercio", alias="efectos de los acuerdos comerciales Viner",
corto="Cuando dos países firman un acuerdo comercial, puede crearse comercio nuevo y eficiente, o desviarse comercio desde un proveedor más eficiente que quedó fuera.",
simple=[
r"Hay <strong>creación de comercio</strong> cuando, al bajar aranceles entre socios, se empieza a importar de un socio más eficiente algo que antes se producía caro en casa. Eso beneficia al país.",
r"Hay <strong>desviación de comercio</strong> cuando se deja de comprar al proveedor más barato del mundo, que paga arancel, para comprarle a un socio un poco más caro que ya no lo paga. Eso puede salir mal, porque el país pierde la recaudación del arancel y paga un precio más alto.",
],
ejemplo=[
r"Con números de ejemplo: si el país A compraba a B a US$ 100 más 20 % de arancel (US$ 120 en total) y firma un TLC con C, que vende a US$ 110 sin arancel, empezará a comprar a C aunque B produzca más barato. Eso es desviación de comercio.",
],
rel=["zona-de-libre-comercio", "integracion-economica", "arancel", "ventaja-comparativa"],
))

T.append(dict(
slug="credito-documentario", t="Carta de crédito (crédito documentario)", cat="comercio", ic="📨",
bcrp="Crédito documentario", alias="carta de crédito comercio exterior pago internacional",
corto="Es un compromiso de un banco de pagar a un exportador cuando este presente los documentos que prueban que envió la mercadería.",
simple=[
r"En el comercio internacional, el exportador teme no cobrar y el importador teme pagar y no recibir. Con un <strong>crédito documentario</strong>, el banco del importador garantiza el pago siempre que el exportador entregue documentos como la factura y el conocimiento de embarque.",
r"Es más seguro que un pago directo, pero tiene costos y trámites, por lo que se usa más en operaciones grandes o con socios nuevos.",
],
ejemplo=[
r"Un exportador peruano de mangos vende por primera vez a un comprador en Europa. Pide una carta de crédito: cuando embarca la fruta y entrega los documentos al banco, cobra aunque el comprador no le pague directamente.",
],
rel=["balanza-comercial", "riesgo-de-credito", "garantia", "divisa"],
))

T.append(dict(
slug="diferencial-cambiario", t="Diferencial cambiario (precio de compra y venta)", cat="dinero", ic="↔️",
bcrp="Diferencial cambiario", alias="spread cambiario compra venta del dólar casa de cambio",
corto="Es la diferencia entre el precio al que una casa de cambio o banco te compra dólares y el precio al que te los vende.",
simple=[
r"Siempre hay dos precios: la <strong>compra</strong> (lo que te pagan por tus dólares) y la <strong>venta</strong> (lo que te cobran por darte dólares). La venta es más alta. Esa diferencia es la ganancia de quien hace el cambio.",
r"El diferencial suele ser menor en casas de cambio digitales y mayor en ventanillas de bancos o aeropuertos. Comparar puede ahorrarte dinero cuando cambias montos grandes.",
],
ejemplo=[
r"Si un banco compra a S/ 3.70 y vende a S/ 3.80, el diferencial es de 10 céntimos. Si cambias US$ 1000 y al rato los vuelves a comprar, pierdes S/ 100.",
],
formula=dict(
tex=r"\text{Diferencial}=TC_{\text{venta}}-TC_{\text{compra}}",
calculo=[r"3.80-3.70=0.10\ \text{soles por dólar}"],
),
rel=["tipo-de-cambio", "tipo-de-cambio-bancario", "divisa", "dolarizacion"],
))

T.append(dict(
slug="tipo-de-cambio-bancario", t="Tipo de cambio interbancario, bancario y paralelo", cat="dinero", ic="💱",
bcrp="Tipo de cambio bancario", alias="dólar interbancario dólar paralelo cambistas tipo de cambio SBS",
corto="El dólar tiene varios precios: el interbancario (entre bancos), el bancario (en ventanilla) y el paralelo (de cambistas y casas de cambio).",
simple=[
r"El <strong>tipo de cambio interbancario</strong> es el que se forma en las operaciones grandes entre bancos; es el que suele aparecer en las noticias. El <strong>bancario</strong> es el que te cobran o pagan en un banco, con un margen. El <strong>paralelo</strong> es el de casas de cambio y cambistas en la calle.",
r"La SBS publica cada día un tipo de cambio promedio que se usa como referencia en contratos, y la SUNAT usa ese dato para fines tributarios.",
],
ejemplo=[
r"Un día el interbancario puede estar en S/ 3.75, mientras un banco vende a S/ 3.82 en ventanilla y una casa de cambio digital a S/ 3.77.",
],
rel=["tipo-de-cambio", "diferencial-cambiario", "regimen-cambiario", "intervencion-cambiaria"],
))

T.append(dict(
slug="duracion", t="Duración de un bono", cat="mercados", ic="⏱️",
bcrp="Duración modificada", alias="duración modificada sensibilidad del precio de un bono a la tasa",
corto="Mide cuánto cambia el precio de un bono cuando cambian las tasas de interés. Mientras mayor la duración, más se mueve el precio.",
simple=[
r"Los bonos de largo plazo son más sensibles a las tasas que los de corto plazo. La <strong>duración modificada</strong> resume esa sensibilidad en un solo número: indica cuánto cae aproximadamente el precio, en porcentaje, si la tasa sube un punto.",
r"Los fondos de pensiones y los bancos la usan para medir el <a href='riesgo-de-tasa-de-interes.html'>riesgo de tasa de interés</a> de sus carteras.",
],
ejemplo=[
r"Si un bono tiene una duración modificada de 7 y las tasas suben 1 punto, su precio cae aproximadamente 7 %.",
],
formula=dict(
tex=r"\frac{\Delta P}{P}\approx -D_{\text{mod}}\times\Delta y",
donde=[(r"D_{\text{mod}}", "duración modificada"), (r"\Delta y", "cambio en la tasa (en decimales)")],
calculo=[r"-7\times 0.01=-0.07=-7\ \%"],
),
rel=["bono", "rendimiento-al-vencimiento", "riesgo-de-tasa-de-interes", "curva-de-rendimiento"],
))

T.append(dict(
slug="valor-a-la-par", t="Valor a la par, bajo la par y sobre la par", cat="mercados", ic="⚖️",
bcrp="Valor a la par", alias="emisión bajo la par sobre la par precio de un bono 100",
corto="Un bono está «a la par» cuando su precio es igual a su valor nominal; «bajo la par» si cuesta menos y «sobre la par» si cuesta más.",
simple=[
r"Los precios de los bonos se expresan como porcentaje de su valor nominal. Un precio de 100 es <strong>a la par</strong>; 95 es <strong>bajo la par</strong>; 105 es <strong>sobre la par</strong>.",
r"Un bono cotiza sobre la par cuando su cupón paga más que las tasas actuales del mercado, y bajo la par cuando paga menos. Por eso, si las tasas suben, los bonos ya emitidos bajan de precio.",
],
ejemplo=[
r"Un bono de S/ 1000 de valor nominal que se compra a 97 cuesta S/ 970. Al vencer, se cobrarán los S/ 1000 completos.",
],
rel=["bono", "rendimiento-al-vencimiento", "bono-cupon-cero", "duracion"],
))

T.append(dict(
slug="empresa-financiera", t="Empresa financiera", cat="dinero", ic="🏢",
bcrp="Empresa financiera", alias="financieras consumo microempresa",
corto="Es una entidad regulada por la SBS que capta depósitos y presta dinero, especializada a menudo en créditos de consumo o a pequeñas empresas.",
simple=[
r"Las financieras hacen muchas operaciones parecidas a un banco, pero con un alcance más limitado según la ley. Suelen enfocarse en segmentos como préstamos a microempresas, créditos de consumo o tarjetas de tiendas.",
r"Están supervisadas por la <a href='sbs.html'>SBS</a> y sus depósitos están protegidos por el Fondo de Seguro de Depósitos, con los límites de ley.",
],
ejemplo=[
r"Algunas grandes tiendas por departamento tienen una financiera asociada que emite su tarjeta de crédito para que los clientes compren en cuotas.",
],
rel=["sistema-financiero", "sbs", "creditos-de-consumo", "cajas-municipales"],
))

T.append(dict(
slug="empresa-holding", t="Holding, filial y subsidiaria", cat="mercados", ic="🏗️",
bcrp="Empresa holding", alias="grupo empresarial matriz subsidiaria filial sucursal",
corto="Un holding es una empresa cuyo negocio principal es ser dueña de otras empresas, llamadas subsidiarias o filiales.",
simple=[
r"Un grupo empresarial suele organizarse con una empresa <strong>matriz</strong> o <strong>holding</strong> en la cima, dueña de la mayoría de acciones de varias <strong>subsidiarias</strong>, cada una con su propia personalidad jurídica.",
r"Una <strong>sucursal</strong>, en cambio, no es una empresa separada: es una oficina o extensión de la misma empresa en otro lugar.",
],
ejemplo=[
r"Un grupo financiero puede tener un holding que es dueño de un banco, una aseguradora y una AFP. Cada una es una subsidiaria con su propia contabilidad y supervisión.",
],
rel=["accion", "fusion-y-adquisicion", "estados-financieros", "capitalizacion-bursatil"],
))

T.append(dict(
slug="empresa-publica", t="Empresa pública", cat="estado", ic="🏭",
bcrp="Empresa pública", alias="empresa estatal Petroperú Sedapal Fonafe",
corto="Es una empresa cuyo dueño, total o mayoritario, es el Estado, y que vende bienes o servicios en el mercado.",
simple=[
r"A diferencia de un ministerio, una empresa pública cobra por lo que vende y debería cubrir sus costos con sus ingresos. En el Perú, muchas están agrupadas bajo el Fonafe, y otras, como Petroperú, tienen régimen propio.",
r"Pueden cumplir objetivos sociales, como dar agua o electricidad a zonas alejadas. Pero si pierden dinero de forma constante, el Estado tiene que rescatarlas con recursos de todos los contribuyentes.",
],
ejemplo=[
r"Sedapal, que da agua potable y alcantarillado en Lima, es una empresa del Estado; el <a href='banco-de-la-nacion.html'>Banco de la Nación</a> también es una empresa pública.",
],
rel=["gobierno-general", "deficit-fiscal", "subsidio", "banco-de-la-nacion"],
))

T.append(dict(
slug="fondo-de-inversion", t="Fondo de inversión", cat="mercados", ic="🗂️",
bcrp="Fondo de inversión", alias="fondo cerrado fondos de inversión SMV",
corto="Es un patrimonio formado con aportes de varios inversionistas para invertir en proyectos o activos específicos, normalmente por un plazo fijo.",
simple=[
r"Se parece a un <a href='fondo-mutuo.html'>fondo mutuo</a>, pero suele ser <strong>cerrado</strong>: tiene un número fijo de cuotas y no puedes retirar tu dinero cuando quieras, sino al final del plazo o vendiendo tus cuotas a otro inversionista.",
r"Por eso puede invertir en activos menos líquidos, como inmuebles, facturas de empresas o proyectos de infraestructura. Están supervisados por la SMV.",
],
ejemplo=[
r"Un fondo de inversión inmobiliario junta S/ 50 millones de varios inversionistas para comprar oficinas, alquilarlas durante 8 años y repartir los alquileres y la ganancia de la venta final.",
],
rel=["fondo-mutuo", "etf", "portafolio", "mercado-de-capitales"],
))

T.append(dict(
slug="estado-de-resultados", t="Estado de resultados (ganancias y pérdidas)", cat="mercados", ic="🧮",
bcrp="Ganancias y pérdidas", alias="estado de ganancias y pérdidas utilidad neta utilidad operativa",
corto="Es el informe que muestra cuánto vendió una empresa en un periodo, cuánto gastó y cuánto ganó o perdió al final.",
simple=[
r"Empieza con las <strong>ventas</strong>, resta el costo de lo vendido y obtiene la <strong>utilidad bruta</strong>. Luego resta los gastos de administración y ventas para llegar a la <strong>utilidad operativa</strong>. Después de intereses e impuestos queda la <strong>utilidad neta</strong>.",
r"Es uno de los <a href='estados-financieros.html'>estados financieros</a> principales. La utilidad neta es la que puede repartirse como <a href='dividendo.html'>dividendos</a> o reinvertirse.",
],
ejemplo=[
r"Una empresa vende S/ 1 000 000, el costo de lo vendido es S/ 600 000, sus gastos operativos S/ 250 000, paga S/ 30 000 de intereses y S/ 35 000 de impuestos. Su utilidad neta es S/ 85 000.",
],
formula=dict(
tex=r"\begin{aligned}\text{Utilidad neta}={}&\text{Ventas}-\text{Costos}-\text{Gastos}\\&-\text{Intereses}-\text{Impuestos}\end{aligned}",
calculo=[r"1\,000\,000-600\,000-250\,000-30\,000-35\,000=85\,000"],
),
rel=["estados-financieros", "balance-general", "rentabilidad", "dividendo"],
))

T.append(dict(
slug="impuestos-municipales", t="Impuestos municipales", cat="impuestos", ic="🏘️",
bcrp="Impuestos municipales", alias="impuesto predial alcabala impuesto vehicular arbitrios",
corto="Son impuestos que cobran y administran las municipalidades, como el predial, la alcabala y el impuesto vehicular.",
simple=[
r"El <strong>impuesto predial</strong> se paga cada año por ser dueño de un inmueble, según su valor. La <strong>alcabala</strong> se paga cuando compras un inmueble. El <strong>impuesto al patrimonio vehicular</strong> se paga durante los primeros años después de comprar un auto.",
r"No hay que confundirlos con los <strong>arbitrios</strong>, que son tasas por servicios como limpieza, parques y serenazgo. Todo esto financia a tu municipalidad.",
],
ejemplo=[
r"Si compras un departamento, pagas la alcabala a la municipalidad de ese distrito y, desde el año siguiente, el impuesto predial y los arbitrios cada año.",
],
rel=["tributo", "impuesto-directo-e-indirecto", "foncomun", "gobierno-general"],
))

T.append(dict(
slug="plan-brady", t="Plan Brady", cat="estado", ic="🤝",
bcrp="Plan Brady", alias="bonos Brady reestructuración de deuda bancaria años 90",
corto="Fue un plan de los años noventa para que los países en crisis canjearan su deuda con bancos privados por bonos nuevos, con descuento y garantías.",
simple=[
r"En los años ochenta, muchos países de América Latina dejaron de pagar sus deudas con bancos internacionales. A fines de esa década, el secretario del Tesoro de EE. UU., Nicholas Brady, propuso un plan: los bancos aceptaban una rebaja de la deuda o de los intereses y, a cambio, recibían bonos nuevos más seguros, los <strong>bonos Brady</strong>.",
r"El Perú se acogió al plan Brady en la segunda mitad de los noventa, lo que le permitió normalizar su relación con los bancos acreedores y volver a los mercados internacionales.",
],
ejemplo=[
r"Gracias a acuerdos como el plan Brady y la renegociación con el <a href='club-de-paris.html'>Club de París</a>, el Perú pasó de ser un país en cesación de pagos a obtener, años después, el <a href='grado-de-inversion.html'>grado de inversión</a>.",
],
rel=["deuda-externa", "club-de-paris", "condonacion-de-deuda", "grado-de-inversion"],
))

T.append(dict(
slug="precio-de-transferencia", t="Precios de transferencia", cat="impuestos", ic="🔁",
bcrp="Precio de transferencia", alias="partes vinculadas valor de mercado elusión",
corto="Son los precios que se cobran entre empresas de un mismo grupo. La ley exige que sean iguales a los que se pactarían entre empresas independientes.",
simple=[
r"Un grupo con empresas en varios países podría vender barato a su filial en un país de impuestos bajos y caro a la de un país de impuestos altos, para pagar menos. Para evitarlo, las reglas de <strong>precios de transferencia</strong> exigen usar valores de mercado.",
r"La SUNAT puede ajustar esos precios si no se respetan, y exige declaraciones y estudios a las empresas que superan ciertos montos de operaciones con partes vinculadas.",
],
ejemplo=[
r"Si una minera peruana vende concentrado a una empresa de su mismo grupo en el exterior por debajo del precio internacional, la SUNAT puede recalcular el impuesto como si se hubiera vendido al precio de mercado.",
],
rel=["evasion-y-elusion-tributaria", "impuesto-a-la-renta", "empresa-holding", "base-imponible"],
))

T.append(dict(
slug="ratio-de-capital-global", t="Ratio de capital global", cat="dinero", ic="🧱",
bcrp="Ratio de Capital Global", alias="solvencia bancaria patrimonio efectivo activos ponderados por riesgo Basilea",
corto="Mide cuánto capital propio tiene un banco frente a los riesgos que asume. Mientras más alto, más preparado está para absorber pérdidas.",
simple=[
r"Un banco presta sobre todo dinero de los depositantes. Si sus préstamos fallan, el primero en absorber las pérdidas debe ser su propio capital. Por eso la ley exige un mínimo de <strong>patrimonio efectivo</strong> frente a sus <strong>activos ponderados por riesgo</strong>.",
r"En el Perú, la ley de bancos fija un mínimo legal de 10 %, y la SBS puede exigir colchones adicionales. Los créditos más riesgosos «pesan» más en el cálculo.",
],
ejemplo=[
r"Si un banco tiene S/ 15 000 millones de patrimonio efectivo y S/ 100 000 millones de activos ponderados por riesgo, su ratio es 15 %, por encima del mínimo de 10 %.",
],
formula=dict(
tex=r"RCG=\frac{PE}{APR}\times 100",
donde=[(r"PE", "patrimonio efectivo"), (r"APR", "activos ponderados por riesgo")],
calculo=[r"\frac{15\,000}{100\,000}\times 100=15\ \%"],
),
rel=["banco-de-pagos-internacionales", "sbs", "apalancamiento", "riesgo-de-credito"],
))

T.append(dict(
slug="tipo-de-cambio-reptante", t="Tipo de cambio reptante (crawling peg)", cat="dinero", ic="🐌",
bcrp="Régimen de tipo de cambio reptante", alias="crawling peg minidevaluaciones banda cambiaria",
corto="Es un régimen en el que el tipo de cambio se ajusta poco a poco, en pequeños pasos anunciados, en lugar de quedarse fijo o flotar libremente.",
simple=[
r"Con un tipo de cambio <strong>reptante</strong>, el banco central mueve el precio de la divisa de forma gradual, por ejemplo un poco cada semana, a menudo para compensar la diferencia de inflación con otros países.",
r"Una variante es la <strong>banda cambiaria</strong>: el tipo de cambio flota, pero solo dentro de límites que el banco central defiende. Son regímenes intermedios entre el <a href='regimen-cambiario.html'>fijo y el flotante</a>.",
],
ejemplo=[
r"Si un país con 10 % de inflación anual mantuviera fijo su tipo de cambio frente a un socio con 2 %, sus productos se encarecerían. Con un régimen reptante, su moneda se deprecia poco a poco para compensar.",
],
rel=["regimen-cambiario", "devaluacion", "tipo-de-cambio-real", "control-cambiario"],
))

T.append(dict(
slug="revaluacion", t="Revaluación", cat="dinero", ic="📈",
bcrp="Revaluación", alias="revaluar apreciación decidida por el banco central",
corto="Es lo contrario de la devaluación: el gobierno o banco central decide bajar el precio oficial de la moneda extranjera, es decir, subir el valor de su moneda.",
simple=[
r"Igual que la <a href='devaluacion.html'>devaluación</a>, la palabra se usa sobre todo con tipo de cambio fijo. Si el tipo de cambio es flotante y la moneda gana valor por el mercado, se dice que se <a href='depreciacion-y-apreciacion.html'>aprecia</a>.",
r"Una revaluación abarata las importaciones y los viajes al exterior, pero hace menos competitivas las exportaciones.",
],
ejemplo=[
r"Si un país con tipo de cambio fijo pasa de 4 a 3.6 unidades de su moneda por dólar, ha revaluado su moneda 10 %.",
],
formula=dict(
tex=r"\%\,\text{revaluación}=\frac{TC_{\text{anterior}}-TC_{\text{nuevo}}}{TC_{\text{anterior}}}\times 100",
calculo=[r"\frac{4-3.6}{4}\times 100=10\ \%"],
),
rel=["devaluacion", "depreciacion-y-apreciacion", "regimen-cambiario", "tipo-de-cambio"],
))

T.append(dict(
slug="riesgo-de-mercado", t="Riesgo de mercado", cat="finanzas", ic="🌪️",
bcrp="Riesgo de mercado", alias="riesgo de precios pérdidas por cambios de precios",
corto="Es la posibilidad de perder dinero porque cambian los precios en los mercados: acciones, bonos, tasas de interés, monedas o materias primas.",
simple=[
r"Aunque elijas bien una inversión, su precio puede caer por factores generales: una crisis internacional, una subida de tasas o un salto del dólar. Ese es el <strong>riesgo de mercado</strong>.",
r"Incluye el riesgo de precio de acciones, el <a href='riesgo-de-tasa-de-interes.html'>riesgo de tasa de interés</a> y el <a href='riesgo-cambiario.html'>riesgo cambiario</a>. Se mide con la <a href='volatilidad.html'>volatilidad</a> y se reduce diversificando o con <a href='cobertura.html'>coberturas</a>.",
],
ejemplo=[
r"Si tienes un fondo de acciones y la bolsa cae 15 % por una crisis mundial, tu fondo probablemente baje, aunque las empresas en las que invierte sigan funcionando bien.",
],
rel=["volatilidad", "riesgo-de-tasa-de-interes", "riesgo-cambiario", "portafolio"],
))

T.append(dict(
slug="riesgo-de-tasa-de-interes", t="Riesgo de tasa de interés", cat="finanzas", ic="📉",
bcrp="Riesgo de tasa de interés", alias="riesgo de tasas sensibilidad a las tasas",
corto="Es la posibilidad de perder dinero porque cambian las tasas de interés, por ejemplo cuando suben y bajan los precios de los bonos.",
simple=[
r"Si tienes un bono que paga 5 % y las tasas del mercado suben a 7 %, nadie querrá pagar el precio completo por tu bono: su precio baja. Ese es el <strong>riesgo de tasa de interés</strong>, y es mayor en bonos de largo plazo (más <a href='duracion.html'>duración</a>).",
r"Los bancos también lo enfrentan: si prestan a tasa fija por muchos años y se financian con depósitos de corto plazo, una subida de tasas les reduce el margen.",
],
ejemplo=[
r"Un fondo de pensiones con muchos bonos a 20 años puede ver caer el valor de su cartera cuando el BCRP y los mercados suben las tasas.",
],
rel=["duracion", "bono", "tasa-fija-y-variable", "riesgo-de-mercado"],
))

T.append(dict(
slug="subastas", t="Subastas del BCRP y del Tesoro", cat="dinero", ic="🔨",
bcrp="Subasta holandesa", alias="subasta holandesa inglesa Vickrey primer precio",
corto="El BCRP y el Tesoro colocan sus títulos, como CD BCRP, repos o bonos, mediante subastas en las que los bancos y otros inversionistas ofrecen tasas o precios.",
simple=[
r"En una subasta, cada participante dice cuánto quiere y a qué tasa o precio. Se asigna primero a las mejores ofertas hasta completar el monto. Si cada ganador paga lo que ofreció, es una subasta de <strong>primer precio</strong> (o discriminatoria). Si todos pagan un mismo precio de corte, se parece a la subasta <strong>holandesa</strong>.",
r"En la subasta <strong>inglesa</strong> el precio sube hasta que queda un solo comprador, y en la <strong>Vickrey</strong> gana la mejor oferta pero paga el precio de la segunda. Cada tipo da incentivos distintos a los participantes.",
],
ejemplo=[
r"Si el BCRP subasta S/ 300 millones en CD y recibe ofertas por S/ 500 millones a distintas tasas, asigna primero a las tasas más bajas hasta completar los S/ 300 millones.",
],
rel=["certificados-de-deposito-del-bcrp", "repo", "operacion-de-mercado-abierto", "bono-soberano"],
))

T.append(dict(
slug="tasa-de-interes-legal", t="Tasa de interés legal", cat="finanzas", ic="⚖️",
bcrp="Tasa de interés legal", alias="interés legal deudas sin tasa pactada",
corto="Es la tasa que se aplica por ley a una deuda cuando las partes no acordaron una tasa de interés. En el Perú la fija el BCRP.",
simple=[
r"A veces una deuda no dice qué interés cobrar, por ejemplo una indemnización ordenada por un juez o un préstamo entre conocidos sin contrato claro. En esos casos se usa la <strong>tasa de interés legal</strong>.",
r"El BCRP la publica en soles y en dólares. También se usa en cálculos laborales y judiciales.",
],
ejemplo=[
r"Si un juez ordena pagar una deuda de S/ 20 000 con intereses legales desde hace dos años, el monto final se calcula con la tasa legal que publica el BCRP para ese periodo.",
],
rel=["tasa-de-interes", "interes-moratorio", "usura", "interes-compuesto"],
))

T.append(dict(
slug="tamn-y-tamex", t="TAMN y TAMEX", cat="dinero", ic="📊",
bcrp="Tasa de interés activa en Moneda extranjera TAMEX", alias="TAMN TAMEX TIPMN TIPMEX tasas promedio SBS",
corto="Son las tasas promedio que cobran los bancos por sus préstamos en soles (TAMN) y en dólares (TAMEX). Sus pares para depósitos son la TIPMN y la TIPMEX.",
simple=[
r"La SBS calcula y publica cada día estos promedios del sistema bancario. La <strong>TAMN</strong> es la tasa activa promedio en moneda nacional y la <strong>TAMEX</strong>, en moneda extranjera. Las tasas <strong>pasivas</strong> promedio (para depósitos) son la <strong>TIPMN</strong> y la <strong>TIPMEX</strong>.",
r"Sirven como referencia en contratos y procesos judiciales, y para ver cómo evolucionan las tasas en el mercado.",
],
ejemplo=[
r"Si la TAMN sube varios meses seguidos, significa que, en promedio, los créditos en soles se están encareciendo, por ejemplo tras subidas de la tasa de referencia.",
],
rel=["tasa-de-interes-activa-y-pasiva", "tasa-de-interes", "intermediacion-financiera", "tasa-de-referencia"],
))

T.append(dict(
slug="usura", t="Usura y tasas máximas", cat="finanzas", ic="🚫",
bcrp="Usura", alias="tasas de interés máximas préstamos abusivos gota a gota",
corto="Es cobrar intereses abusivos por un préstamo, por encima de lo que permite la ley. En el Perú, el BCRP fija tasas máximas para ciertos créditos.",
simple=[
r"Desde 2021, por ley, el BCRP establece tasas de interés máximas para créditos de consumo y para préstamos a micro y pequeñas empresas otorgados por entidades supervisadas. Las revisa cada cierto tiempo.",
r"Fuera del sistema, los prestamistas informales como el llamado «gota a gota» cobran tasas altísimas y usan cobranzas violentas. Prestar a tasas usurarias puede ser delito.",
],
ejemplo=[
r"Un prestamista informal da S/ 1000 y pide S/ 1200 al mes siguiente: ¡20 % mensual, más de 790 % al año! Ningún crédito formal supervisado puede cobrar algo así.",
],
formula=dict(
tex=r"TEA=(1+i_m)^{12}-1",
donde=[(r"i_m", "tasa mensual en decimales")],
calculo=[r"(1.20)^{12}-1\approx 7.92=792\ \%"],
),
ojo=["Antes de pedir un préstamo, verifica que la entidad esté supervisada por la SBS."],
rel=["tea", "tasa-de-interes-legal", "creditos-de-consumo", "sbs"],
))

T.append(dict(
slug="mapa-de-pobreza", t="Mapa de pobreza", cat="bienestar", ic="🗺️",
bcrp="Mapa de pobreza", alias="pobreza por distritos focalización INEI",
corto="Es una herramienta que muestra qué tan pobre es cada región, provincia o distrito, para dirigir mejor la ayuda y la inversión pública.",
simple=[
r"La pobreza nacional es un promedio que esconde grandes diferencias. El INEI combina el censo con encuestas para estimar la pobreza en zonas pequeñas, como los distritos.",
r"Con el mapa, el Estado puede <strong>focalizar</strong>: llevar programas sociales e inversiones a los lugares que más los necesitan.",
],
ejemplo=[
r"Un programa de agua potable puede priorizar los distritos que el mapa de pobreza muestra con mayor porcentaje de población pobre.",
],
rel=["pobreza-monetaria", "distribucion-del-ingreso", "indice-de-desarrollo-humano", "foncomun"],
))
