# -*- coding: utf-8 -*-
# Términos del glosario (parte 2): finanzas personales, trabajo, impuestos,
# Estado, comercio exterior, mercados y bienestar. Mismo formato que terminos1.py.



T = []

T.append(dict(
slug="valor-presente-y-valor-futuro", t="Valor presente y valor futuro", cat="finanzas", ic="⏳",
alias="valor actual valor del dinero en el tiempo descontar actualizar",
corto="Un sol hoy vale más que un sol mañana. El valor futuro dice cuánto será tu dinero más adelante; el valor presente, cuánto vale hoy un monto futuro.",
simple=[
r"Esta es una de las ideas más importantes de las finanzas: el <strong>valor del dinero en el tiempo</strong>. Un sol hoy vale más que un sol dentro de un año, porque hoy puedes ahorrarlo y ganar intereses (y porque la inflación puede comérselo).",
r"El <strong>valor futuro</strong> (VF) lleva un monto de hoy hacia adelante con la tasa de interés. El <strong>valor presente</strong> (VP) hace lo contrario: trae un monto futuro a soles de hoy. A eso se le llama <strong>descontar</strong>.",
],
ejemplo=[
r"Te ofrecen S/ 1000 hoy o S/ 1100 dentro de dos años. Si puedes ahorrar al 6 % anual, los S/ 1100 futuros valen hoy unos S/ 979. Te conviene más recibir los S/ 1000 hoy.",
],
formula=dict(
tex=r"VF=VP\,(1+i)^{n}\qquad\Longleftrightarrow\qquad VP=\frac{VF}{(1+i)^{n}}",
donde=[(r"VP", "valor presente (hoy)"), (r"VF", "valor futuro"), (r"i", "tasa de interés por periodo"), (r"n", "número de periodos")],
calculo=[r"VP=\frac{1100}{(1.06)^{2}}=\frac{1100}{1.1236}\approx 979\ \text{soles}"],
),
rel=["interes-compuesto", "van", "tir", "costo-de-oportunidad"],
))

T.append(dict(
slug="van", t="Valor actual neto (VAN)", cat="finanzas", ic="📊",
alias="van vpn valor presente neto evaluacion de proyectos",
corto="Es la ganancia de un proyecto medida en soles de hoy: el valor presente de todo lo que recibirás menos lo que inviertes. Si es positivo, el proyecto conviene.",
simple=[
r"El VAN sirve para decidir si vale la pena invertir en algo: abrir un negocio, comprar una máquina o estudiar una carrera. Trae a <a href=\"valor-presente-y-valor-futuro.html\">valor presente</a> todos los ingresos futuros y les resta la inversión inicial.",
r"La regla es simple: si el <strong>VAN es mayor que cero</strong>, el proyecto gana más que la tasa que usaste para descontar (tu mejor alternativa), así que conviene. Si es negativo, te iría mejor con la alternativa.",
],
ejemplo=[
r"Quieres poner una máquina de jugos que cuesta S/ 5000 y te dejaría S/ 2000 al año durante 3 años. Si tu dinero podría rendir 10 % en otro lado, el VAN es de unos S/ −26: casi cero, pero negativo. Por poco, no conviene.",
],
formula=dict(
tex=r"VAN=-I_0+\sum_{t=1}^{n}\frac{F_t}{(1+i)^{t}}",
donde=[(r"I_0", "inversión inicial"), (r"F_t", "flujo de dinero neto del año t"), (r"i", "tasa de descuento (costo de oportunidad)"), (r"n", "años del proyecto")],
calculo=[r"VAN=-5000+\frac{2000}{1.1}+\frac{2000}{1.1^{2}}+\frac{2000}{1.1^{3}}", r"VAN=-5000+1818.18+1652.89+1502.63,\quad VAN\approx -26.30"],
),
rel=["tir", "valor-presente-y-valor-futuro", "costo-de-oportunidad", "inversion"],
))

T.append(dict(
slug="tir", t="Tasa interna de retorno (TIR)", cat="finanzas", ic="🔁",
alias="tir rentabilidad de un proyecto",
corto="Es la rentabilidad propia de un proyecto: la tasa de descuento con la que el VAN se vuelve cero.",
simple=[
r"La TIR responde a la pregunta: «¿cuánto rinde, en porcentaje, este proyecto?». Es la tasa que hace que el <a href=\"van.html\">VAN</a> sea exactamente cero.",
r"Se compara con tu <a href=\"costo-de-oportunidad.html\">costo de oportunidad</a>: si la TIR es mayor que lo que ganarías en otra alternativa, el proyecto conviene. No suele tener una fórmula directa: se calcula probando tasas o con Excel (función TIR).",
],
ejemplo=[
r"En el ejemplo de la máquina de jugos (invertir S/ 5000 para recibir S/ 2000 por 3 años), la TIR es de alrededor de 9.7 %. Como tu alternativa rinde 10 %, el proyecto rinde un poco menos y no conviene, lo mismo que dijo el VAN.",
],
formula=dict(
tex=r"0=-I_0+\sum_{t=1}^{n}\frac{F_t}{(1+TIR)^{t}}",
donde=[(r"I_0", "inversión inicial"), (r"F_t", "flujo neto del año t")],
calculo=[r"-5000+\frac{2000}{1.097}+\frac{2000}{1.097^{2}}+\frac{2000}{1.097^{3}}\approx 0,\quad TIR\approx 9.7\ \%"],
),
rel=["van", "valor-presente-y-valor-futuro", "costo-de-oportunidad", "tcea"],
))

T.append(dict(
slug="costo-de-oportunidad", t="Costo de oportunidad", cat="mercados", ic="🔀",
alias="lo que dejas de ganar renuncia eleccion",
corto="Es lo que dejas de ganar al elegir una opción en lugar de la mejor alternativa que tenías.",
simple=[
r"Toda decisión tiene un costo escondido: lo que <strong>renuncias</strong> por elegir. Si usas una tarde para trabajar, dejas de estudiar; si gastas tus ahorros en un viaje, dejas de ganar sus intereses.",
r"El costo de oportunidad es el valor de la <strong>mejor</strong> alternativa que dejaste, no de todas. Es la base de la economía: como los recursos (tiempo, dinero) son escasos, siempre hay que elegir.",
],
ejemplo=[
r"Un taxista que trabaja por aplicativo decide tomarse el sábado libre. Si ese día suele ganar S/ 150, el costo de oportunidad de su descanso son esos S/ 150, aunque no «pague» nada.",
r"En finanzas, la tasa que usas para calcular el <a href=\"van.html\">VAN</a> es justamente tu costo de oportunidad: lo que rendiría tu dinero en la mejor alternativa.",
],
rel=["van", "tir", "oferta-y-demanda", "ahorro"],
))

T.append(dict(
slug="ahorro", t="Ahorro", cat="finanzas", ic="🫙",
alias="ahorrar guardar dinero propension a ahorrar",
corto="Es la parte del ingreso que no se gasta en consumo. Sirve para emergencias, metas futuras e inversión.",
simple=[
r"Ahorrar es no gastar hoy todo lo que ganas. A nivel de una familia, sirve para tener un <strong>fondo de emergencia</strong> y para cumplir metas, como estudiar o comprar una casa. A nivel de un país, el ahorro financia la <a href=\"inversion.html\">inversión</a>, que hace crecer la economía.",
r"Guardar el dinero «bajo el colchón» tiene un costo: la <a href=\"inflacion.html\">inflación</a> le quita valor. Por eso conviene ahorrar en una entidad supervisada por la SBS y comparar su <a href=\"trea.html\">TREA</a>.",
],
ejemplo=[
r"Si ganas S/ 2500 al mes y gastas S/ 2200, ahorras S/ 300, es decir, el 12 % de tu ingreso. Una recomendación común es juntar, poco a poco, un fondo que cubra de 3 a 6 meses de gastos.",
],
formula=dict(
tex=r"S=Y-C,\qquad \text{Tasa de ahorro}=\frac{S}{Y}\times 100",
donde=[(r"S", "ahorro"), (r"Y", "ingreso disponible (después de impuestos)"), (r"C", "consumo")],
calculo=[r"S=2500-2200=300,\qquad \frac{300}{2500}\times 100=12\ \%"],
),
rel=["inversion", "trea", "interes-compuesto", "afp-y-onp", "costo-de-oportunidad"],
))

T.append(dict(
slug="inversion", t="Inversión", cat="produccion", ic="🏗️",
alias="inversion privada inversion publica formacion bruta de capital",
corto="En economía, invertir es gastar hoy en cosas que sirven para producir más mañana: maquinaria, edificios, carreteras o tecnología.",
simple=[
r"En el lenguaje diario, «invertir» es poner tu dinero en algo para que crezca. En macroeconomía, inversión significa algo más concreto: comprar <strong>bienes de capital</strong>, como maquinaria, fábricas, viviendas nuevas, carreteras o equipos.",
r"Hay <strong>inversión privada</strong> (empresas y familias) e <strong>inversión pública</strong> (Estado: colegios, hospitales, pistas). Es clave para el <a href=\"crecimiento-economico.html\">crecimiento</a>, porque aumenta lo que el país puede producir.",
],
ejemplo=[
r"Cuando una minera construye un nuevo proyecto en el sur del país, o cuando un gobierno regional construye un hospital, eso suma a la inversión del PBI. Comprar acciones de una empresa ya existente, en cambio, es una inversión financiera, no una inversión en el sentido del PBI.",
],
formula=dict(
tex=r"PBI=C+\boxed{I}+G+(X-M)",
donde=[(r"I", "inversión, uno de los componentes del gasto del PBI")],
),
rel=["pbi", "ahorro", "crecimiento-economico", "van", "politica-fiscal"],
))

T.append(dict(
slug="remuneracion-minima-vital", t="Remuneración mínima vital (sueldo mínimo)", cat="trabajo", ic="💼",
alias="rmv sueldo minimo salario minimo",
corto="Es el sueldo mensual más bajo que se puede pagar por una jornada completa en el sector privado. Desde el 1 de octubre de 2026 es S/ 1230.",
simple=[
r"La remuneración mínima vital (RMV) es el <strong>piso legal</strong> del sueldo de un trabajador del régimen privado con jornada completa (8 horas diarias o 48 semanales). La fija el Gobierno por decreto supremo.",
r"Desde el <strong>1 de octubre de 2026</strong>, la RMV es de <strong>S/ 1230</strong>; antes era de S/ 1130. Lo fijó el Decreto Supremo 015-2026-TR, que también anuncia un segundo aumento de S/ 70, hasta S/ 1300, mediante otro decreto durante el primer semestre de 2027.",
r"La RMV también sirve de referencia para otros pagos, como la asignación familiar, que es el 10 % de la RMV para quien tiene hijos menores de edad o que estudian.",
],
ejemplo=[
r"Con la RMV de S/ 1230, la asignación familiar es S/ 123 al mes. Si un trabajador de jornada completa gana menos de S/ 1230, su empleador está incumpliendo la ley.",
],
formula=dict(
tex=r"\text{Asignación familiar}=10\ \%\times RMV",
donde=[(r"RMV", "remuneración mínima vital vigente")],
calculo=[r"0.10\times 1230=123\ \text{soles}"],
),
ojo=["Mucha gente trabaja en la informalidad y no recibe la RMV: la ley solo se cumple si el empleo es formal."],
rel=["informalidad", "poder-adquisitivo", "cts", "gratificacion", "afp-y-onp"],
))

T.append(dict(
slug="cts", t="Compensación por tiempo de servicios (CTS)", cat="trabajo", ic="🛟",
alias="cts deposito de cts seguro de desempleo",
corto="Es un ahorro obligatorio que tu empleador deposita en mayo y noviembre en una cuenta a tu nombre, para protegerte si te quedas sin trabajo.",
simple=[
r"La CTS funciona como un <strong>seguro de desempleo</strong>: es un dinero que el empleador deposita dos veces al año en una cuenta CTS que tú eliges (banco, caja o financiera). La idea es que la uses cuando dejes de trabajar.",
r"Se deposita en los <strong>primeros 15 días de mayo y de noviembre</strong>. Cada depósito equivale, más o menos, a medio sueldo si trabajaste todo el semestre. Para calcularla se usa la «remuneración computable», que suma tu sueldo y un sexto de tu última gratificación.",
r"Le corresponde a los trabajadores del régimen privado que trabajan, en promedio, al menos 4 horas diarias y tienen por lo menos un mes de servicios. No la reciben, por ejemplo, quienes cobran una remuneración integral anual que ya incluye la CTS ni los trabajadores de microempresas inscritas en el Remype contratados después de su inscripción.",
],
ejemplo=[
r"Lucía gana S/ 2400 al mes y recibió S/ 2400 de gratificación en julio. Su remuneración computable es S/ 2400 + S/ 400 = S/ 2800. Si trabajó los 6 meses completos (mayo a octubre), en noviembre le depositan S/ 1400.",
],
formula=dict(
tex=r"CTS=\frac{R+\frac{1}{6}G}{12}\times m",
donde=[(r"R", "sueldo mensual"), (r"G", "última gratificación recibida"), (r"m", "meses completos trabajados en el semestre")],
calculo=[r"CTS=\frac{2400+\frac{2400}{6}}{12}\times 6", r"CTS=\frac{2800}{12}\times 6=1400\ \text{soles}"],
),
ojo=["Si el 15 cae domingo o feriado, el plazo pasa al siguiente día hábil (en noviembre de 2026 vence el lunes 16).",
     "La Ley 32322 permite retirar libremente el 100 % de la CTS hasta el 31 de diciembre de 2026. Después de esa fecha, revisa qué regla está vigente."],
rel=["gratificacion", "remuneracion-minima-vital", "afp-y-onp", "ahorro"],
))

T.append(dict(
slug="gratificacion", t="Gratificación", cat="trabajo", ic="🎁",
alias="gratificacion de julio gratificacion de diciembre bonificacion extraordinaria",
corto="Es un sueldo extra que recibes en julio (Fiestas Patrias) y otro en diciembre (Navidad), más una bonificación del 9 %.",
simple=[
r"Los trabajadores del régimen privado reciben dos gratificaciones al año: una en <strong>julio</strong> y otra en <strong>diciembre</strong>, pagadas en la primera quincena. Si trabajaste todo el semestre, cada una equivale a un sueldo completo.",
r"Si trabajaste menos meses, recibes la parte proporcional: un sexto del sueldo por cada mes completo. Además, como la gratificación no paga aporte a EsSalud, ese 9 % se te entrega como <strong>bonificación extraordinaria</strong>.",
r"Según la Ley 27735, la gratificación no tiene aportaciones ni descuentos (ni AFP, ni ONP, ni EsSalud), salvo los que ordene la ley o un juez, como una pensión de alimentos. Lo que sí hace es sumar a tu ingreso anual para el impuesto a la renta de quinta categoría.",
],
ejemplo=[
r"Jorge gana S/ 2000 y trabajó de enero a junio. En julio recibe S/ 2000 de gratificación más S/ 180 de bonificación (9 %): en total, S/ 2180. Si hubiera entrado en marzo (4 meses completos), recibiría S/ 1333.33 más S/ 120.",
],
formula=dict(
tex=r"G=\frac{R}{6}\times m,\qquad \text{Total}=G\times 1.09",
donde=[(r"R", "sueldo mensual"), (r"m", "meses completos trabajados en el semestre (de 1 a 6)")],
calculo=[r"G=\frac{2000}{6}\times 6=2000,\qquad 2000\times 1.09=2180\ \text{soles}"],
),
ojo=["Si tu seguro de salud es una EPS, la bonificación es 6.75 % en lugar de 9 %."],
rel=["cts", "remuneracion-minima-vital", "impuesto-a-la-renta", "afp-y-onp"],
))

T.append(dict(
slug="afp-y-onp", t="AFP y ONP (sistema de pensiones)", cat="trabajo", ic="👵",
alias="afp onp jubilacion pension aporte spp snp",
corto="Son los dos sistemas para jubilarte en el Perú: el privado (AFP), con una cuenta personal, y el público (ONP), con un fondo común.",
simple=[
r"Si trabajas en planilla, parte de tu sueldo se descuenta cada mes para tu <strong>jubilación</strong>. Puedes estar en uno de dos sistemas:",
r"<strong>Sistema Privado de Pensiones (AFP)</strong>: aportas el <strong>10 %</strong> de tu sueldo a una <strong>cuenta individual</strong> a tu nombre, que la AFP invierte. Además pagas una comisión y una prima de seguro. Tu pensión dependerá de cuánto juntes en tu cuenta.",
r"<strong>Sistema Nacional de Pensiones (ONP)</strong>: aportas el <strong>13 %</strong> de tu sueldo a un <strong>fondo común</strong> que paga las pensiones de los jubilados de hoy. Para recibir pensión necesitas un número mínimo de años de aportes, que fija la ley.",
],
ejemplo=[
r"Con un sueldo de S/ 3000, en la ONP te descuentan S/ 390 al mes. En una AFP te descuentan S/ 300 para tu cuenta, más la comisión y la prima de seguro, que varían según la AFP.",
],
formula=dict(
tex=r"\text{Aporte ONP}=0.13\times R,\qquad \text{Aporte AFP}=0.10\times R+\text{comisión}+\text{prima}",
donde=[(r"R", "remuneración mensual")],
calculo=[r"0.13\times 3000=390,\qquad 0.10\times 3000=300\ \text{soles}"],
),
ojo=["La Ley 32123 (2024), de modernización del sistema de pensiones, mantiene estos porcentajes y crea, entre otras cosas, un aporte por consumo (1 % de tus boletas electrónicas con DNI, pagado por el Estado) y una pensión mínima. Varias de sus reglas entran en vigor poco a poco.",
     "Antes de decidir entre AFP y ONP, revisa la información de la SBS y de la ONP."],
rel=["ahorro", "interes-compuesto", "remuneracion-minima-vital", "cts", "informalidad"],
))

T.append(dict(
slug="pea", t="Población económicamente activa (PEA)", cat="trabajo", ic="👷",
alias="pea fuerza laboral poblacion en edad de trabajar pet",
corto="Son las personas en edad de trabajar que tienen trabajo o lo están buscando activamente.",
simple=[
r"En el Perú, el INEI considera <strong>población en edad de trabajar</strong> (PET) a las personas de <strong>14 años a más</strong>. De ellas, la <strong>PEA</strong> es la que participa en el mercado laboral: los que trabajan (<strong>ocupados</strong>) y los que no trabajan pero buscan empleo (<strong>desocupados</strong>).",
r"Para el INEI basta con haber trabajado <strong>al menos una hora</strong> en la semana de la encuesta para contar como ocupado. Quienes no trabajan ni buscan trabajo, como muchos estudiantes, jubilados o personas dedicadas solo a su hogar, forman la <strong>población económicamente inactiva</strong>.",
],
ejemplo=[
r"Una estudiante universitaria que solo estudia es PEA inactiva. Si consigue unas prácticas pagadas, pasa a ser PEA ocupada. Si termina las prácticas y empieza a buscar trabajo, es PEA desocupada.",
],
formula=dict(
tex=r"PEA=\text{Ocupados}+\text{Desocupados},\qquad \text{Tasa de actividad}=\frac{PEA}{PET}\times 100",
donde=[(r"PET", "población en edad de trabajar (14 años a más)")],
),
rel=["tasa-de-desempleo", "informalidad", "remuneracion-minima-vital"],
))

T.append(dict(
slug="tasa-de-desempleo", t="Tasa de desempleo", cat="trabajo", ic="🔎",
alias="desempleo desocupacion paro subempleo",
corto="Es el porcentaje de la población económicamente activa que no tiene trabajo y lo está buscando.",
simple=[
r"La tasa de desempleo no se calcula sobre toda la población, sino sobre la <a href=\"pea.html\">PEA</a>: solo cuenta a quienes <strong>quieren trabajar y buscan empleo</strong>. Un jubilado que no busca trabajo no es un desempleado.",
r"En el Perú el desempleo suele ser bajo comparado con otros países, porque muchas personas no pueden darse el lujo de no trabajar y se emplean en lo que encuentran, aunque sea informal o con pocas horas. Por eso también se mira el <strong>subempleo</strong> y la <a href=\"informalidad.html\">informalidad</a>.",
],
ejemplo=[
r"Si en un distrito hay 50 000 personas en la PEA y 3000 buscan trabajo sin encontrarlo, la tasa de desempleo es 6 %.",
],
formula=dict(
tex=r"u=\frac{\text{Desocupados}}{PEA}\times 100",
donde=[(r"u", "tasa de desempleo, en %")],
calculo=[r"u=\frac{3000}{50\,000}\times 100=6\ \%"],
),
rel=["pea", "informalidad", "recesion", "ciclo-economico"],
))

T.append(dict(
slug="informalidad", t="Informalidad", cat="trabajo", ic="🧺",
alias="empleo informal economia informal",
corto="Es el trabajo o la actividad económica que no está registrada ante el Estado: sin contrato, sin seguro de salud y sin aportes para la jubilación.",
simple=[
r"Un empleo es <strong>informal</strong> cuando el trabajador no tiene los beneficios de ley: no está en planilla, no tiene seguro de salud pagado por el empleador ni aporta a una AFP o a la ONP. Un negocio es informal cuando no tiene RUC ni está registrado.",
r"El Perú tiene una de las tasas de informalidad más altas de la región: con datos de la Encuesta Nacional de Hogares (ENAHO) del INEI, se estima que el <strong>72 %</strong> de la PEA trabaja en la informalidad, es decir, más de 7 de cada 10 personas. Las causas incluyen la baja productividad de muchos negocios pequeños, los costos y trámites de formalizarse y la poca fiscalización.",
r"La informalidad deja a las personas sin protección ante una enfermedad o la vejez, y reduce lo que el Estado recauda en impuestos.",
],
ejemplo=[
r"Una persona que vende comida en la calle sin RUC, o un trabajador de construcción contratado «de palabra» por días, sin seguro ni boleta de pago, están en la informalidad.",
],
rel=["pea", "remuneracion-minima-vital", "afp-y-onp", "impuesto-a-la-renta", "pobreza-monetaria"],
))

T.append(dict(
slug="uit", t="Unidad impositiva tributaria (UIT)", cat="impuestos", ic="📏",
alias="uit 2026 valor de la uit",
corto="Es un monto de referencia que fija el Estado cada año para calcular impuestos, multas y límites legales. En 2026 vale S/ 5500.",
simple=[
r"La UIT no es un impuesto: es una <strong>unidad de medida</strong> en soles. Muchas normas no dicen «S/ 27 500», sino «5 UIT». Así, cuando la UIT se actualiza cada año, los límites se actualizan solos.",
r"Para el año <strong>2026</strong>, la UIT es de <strong>S/ 5500</strong>, según el Decreto Supremo 301-2025-EF del Ministerio de Economía y Finanzas.",
r"Se usa, por ejemplo, para calcular el <a href=\"impuesto-a-la-renta.html\">impuesto a la renta</a> (se restan 7 UIT a los ingresos anuales del trabajo antes de calcular el impuesto), las multas y los topes de algunos trámites.",
],
ejemplo=[
r"Si un trabajador gana menos de 7 UIT al año (S/ 38 500 en 2026), no paga impuesto a la renta de quinta categoría.",
],
formula=dict(
tex=r"7\ UIT=7\times 5500=38\,500\ \text{soles (2026)}",
donde=[(r"UIT", "valor de la UIT del año")],
),
rel=["impuesto-a-la-renta", "igv", "politica-fiscal"],
))

T.append(dict(
slug="igv", t="Impuesto general a las ventas (IGV)", cat="impuestos", ic="🧾",
alias="igv iva impuesto al consumo 18",
corto="Es el impuesto que se paga al comprar la mayoría de bienes y servicios. En el Perú es 18 % del precio sin impuesto.",
simple=[
r"El IGV es un impuesto al <strong>consumo</strong>: lo pagas tú al comprar, aunque quien lo entrega a la SUNAT es el vendedor. La tasa total es <strong>18 %</strong>: 16 % de IGV propiamente dicho más 2 % de Impuesto de Promoción Municipal (IPM).",
r"Es un impuesto al <strong>valor agregado</strong>: en cada etapa de la cadena (productor, mayorista, tienda) se paga el impuesto solo sobre lo que esa etapa añade, porque cada empresa descuenta el IGV que ya pagó en sus compras (el «crédito fiscal»).",
r"La ley exonera algunos bienes y servicios. Además, hay tasas especiales: en 2026, los restaurantes, hoteles y alojamientos turísticos que son mype y cumplen ciertos requisitos pagan 10.5 % (8 % de IGV más 2.5 % de IPM).",
],
ejemplo=[
r"Una mochila cuesta S/ 100 sin impuesto. Con IGV, pagas S/ 118. Y al revés: si una boleta dice S/ 59 en total, el IGV incluido es S/ 9 y el valor de venta, S/ 50.",
],
formula=dict(
tex=r"P=V\times 1.18,\qquad IGV=P\times\frac{18}{118}",
donde=[(r"V", "valor de venta (sin IGV)"), (r"P", "precio final con IGV")],
calculo=[r"100\times 1.18=118,\qquad 59\times\frac{18}{118}=9\ \text{soles}"],
),
rel=["impuesto-a-la-renta", "uit", "politica-fiscal", "deficit-fiscal"],
))

T.append(dict(
slug="impuesto-a-la-renta", t="Impuesto a la renta", cat="impuestos", ic="🧮",
alias="renta de quinta categoria impuesto al sueldo renta de cuarta",
corto="Es el impuesto que se paga sobre los ingresos: sueldos, honorarios, alquileres o ganancias de empresas. El de sueldos se llama de quinta categoría.",
simple=[
r"En el Perú los ingresos se ordenan en <strong>categorías</strong>: alquileres (primera), ganancias de capital (segunda), empresas (tercera), trabajo independiente con recibos por honorarios (cuarta) y trabajo en planilla (<strong>quinta</strong>).",
r"Para la quinta categoría, a tu ingreso anual (12 sueldos más gratificaciones) se le restan <strong>7 UIT</strong>. Sobre lo que queda se aplica una escala <strong>progresiva</strong>: quien gana más paga una tasa mayor, pero solo sobre la parte que pasa cada tramo.",
r"La escala de la SUNAT es: hasta 5 UIT, 8 %; más de 5 hasta 20 UIT, 14 %; más de 20 hasta 35 UIT, 17 %; más de 35 hasta 45 UIT, 20 %; más de 45 UIT, 30 %. Además, puedes deducir hasta 3 UIT más por gastos pagados con comprobante electrónico: el 30 % del alquiler de tu vivienda, el 30 % de los honorarios de profesionales independientes (como médicos o psicólogos), el 15 % de lo que gastas en restaurantes, bares y hoteles, y los aportes a EsSalud por trabajadores del hogar.",
],
ejemplo=[
r"Rosa gana S/ 4000 al mes en planilla. Al año: 12 sueldos más 2 gratificaciones = S/ 56 000. Le restan 7 UIT (S/ 38 500) y queda S/ 17 500. Como no pasa de 5 UIT (S/ 27 500), paga 8 %: S/ 1400 al año, que su empleador le retiene poco a poco cada mes.",
],
formula=dict(
tex=r"\text{Renta neta}=\text{Ingreso anual}-7\,UIT,\qquad \text{Impuesto}=\sum_{k}\tau_k\times RN_k",
donde=[(r"\tau_k", "tasa de cada tramo: 8 %, 14 %, 17 %, 20 % o 30 %"), (r"RN_k", "parte de la renta neta que cae en el tramo k"), (r"UIT", "S/ 5500 en 2026")],
calculo=[r"56\,000-38\,500=17\,500", r"0.08\times 17\,500=1400\ \text{soles al año}"],
),
ojo=["El ejemplo no incluye las deducciones adicionales de hasta 3 UIT ni la bonificación extraordinaria, que también está gravada."],
rel=["uit", "igv", "gratificacion", "politica-fiscal", "informalidad"],
))

T.append(dict(
slug="politica-fiscal", t="Política fiscal", cat="estado", ic="🏦",
alias="gasto publico impuestos presupuesto mef",
corto="Son las decisiones del Estado sobre cuánto gastar y cuánto cobrar en impuestos. En el Perú la conduce el Ministerio de Economía y Finanzas (MEF).",
simple=[
r"Con la política fiscal, el Estado decide su <strong>presupuesto</strong>: cuánto recauda (impuestos como el <a href=\"igv.html\">IGV</a> y el <a href=\"impuesto-a-la-renta.html\">impuesto a la renta</a>) y en qué gasta (sueldos públicos, colegios, hospitales, carreteras, programas sociales).",
r"Es <strong>expansiva</strong> cuando el Estado gasta más o cobra menos impuestos, para animar la economía, y <strong>contractiva</strong> cuando gasta menos o cobra más, por ejemplo para reducir el déficit.",
r"El Perú tiene <strong>reglas fiscales</strong>: límites legales al déficit y a la deuda pública, para que las cuentas del Estado se mantengan sanas. Por ejemplo, la regla de mediano plazo pide un déficit de 1 % del PBI, y el Decreto Legislativo 1621 (2024) fija cómo volver a ella poco a poco después de la pandemia.",
],
ejemplo=[
r"En 2020, durante la pandemia, el Estado peruano entregó bonos a millones de familias y aumentó el gasto en salud. Fue una política fiscal expansiva, que aumentó el déficit y la deuda.",
],
rel=["deficit-fiscal", "deuda-publica", "politica-monetaria", "igv", "impuesto-a-la-renta"],
))

T.append(dict(
slug="deficit-fiscal", t="Déficit fiscal", cat="estado", ic="➖",
alias="resultado fiscal superavit fiscal",
corto="Es cuando el Estado gasta más de lo que recauda en un año. Si recauda más de lo que gasta, hay superávit.",
simple=[
r"El resultado fiscal compara los <strong>ingresos</strong> del Estado (sobre todo impuestos) con sus <strong>gastos</strong>. Si los gastos son mayores, hay <strong>déficit</strong>, que se cubre pidiendo prestado. Si los ingresos son mayores, hay <strong>superávit</strong>.",
r"Se suele expresar como <strong>porcentaje del PBI</strong>, para comparar entre años y países. Un déficit pequeño de vez en cuando es normal; uno grande y permanente hace crecer la <a href=\"deuda-publica.html\">deuda pública</a>.",
],
ejemplo=[
r"Si en un año el Estado recauda 200 mil millones de soles y gasta 220 mil millones, el déficit es de 20 mil millones. Si el PBI es de 1000 mil millones, el déficit es 2 % del PBI.",
r"Con datos reales: en su Marco Macroeconómico Multianual 2026-2029, el MEF proyectó un déficit de 2.2 % del PBI para 2025 y de 1.8 % para 2026, bajando hacia la regla de 1 %.",
],
formula=dict(
tex=r"\text{Resultado fiscal}=\text{Ingresos}-\text{Gastos},\qquad \frac{\text{Déficit}}{PBI}\times 100",
calculo=[r"200-220=-20,\qquad \frac{20}{1000}\times 100=2\ \%\ \text{del PBI}"],
),
rel=["politica-fiscal", "deuda-publica", "pbi", "riesgo-pais"],
))

T.append(dict(
slug="deuda-publica", t="Deuda pública", cat="estado", ic="📒",
alias="deuda del estado bonos soberanos endeudamiento",
corto="Es todo lo que el Estado debe, dentro y fuera del país. Se mide como porcentaje del PBI.",
simple=[
r"Cuando el Estado tiene <a href=\"deficit-fiscal.html\">déficit</a>, pide prestado: emite <strong>bonos</strong> (papeles que prometen devolver el dinero con intereses) o toma préstamos de organismos como el Banco Mundial. La suma de todo eso es la deuda pública.",
r"Lo importante no es el monto en soles, sino su tamaño frente a la economía (<strong>deuda / PBI</strong>) y si se puede pagar sin problemas. El Ministerio de Economía y Finanzas (MEF) destaca el bajo nivel de deuda del Perú como una de sus fortalezas, y eso ayuda a que el país pague tasas de interés más bajas cuando se endeuda.",
],
ejemplo=[
r"Si el Estado debe 330 mil millones de soles y el PBI es de 1000 mil millones, la deuda es 33 % del PBI. En la realidad, el MEF proyectó la deuda pública peruana en 32.1 % del PBI para 2025 y 2026, una de las más bajas de América Latina.",
],
formula=dict(
tex=r"\text{Ratio de deuda}=\frac{\text{Deuda pública}}{PBI}\times 100",
calculo=[r"\frac{330}{1000}\times 100=33\ \%"],
),
rel=["deficit-fiscal", "politica-fiscal", "riesgo-pais", "pbi"],
))

T.append(dict(
slug="riesgo-pais", t="Riesgo país", cat="estado", ic="🌡️",
alias="embig spread soberano puntos basicos",
corto="Mide cuánto más interés piden los inversionistas para prestarle a un país, frente a prestarle a Estados Unidos. Se mide en puntos básicos.",
simple=[
r"Prestarle al Gobierno de Estados Unidos se considera casi sin riesgo. Prestarle a otro país tiene más riesgo, así que los inversionistas piden una tasa más alta. Esa diferencia es el <strong>riesgo país</strong>.",
r"Se expresa en <strong>puntos básicos</strong>: 100 puntos básicos son 1 punto porcentual. El indicador más usado es el EMBIG de J. P. Morgan. Si el riesgo país sube, al Estado y a las empresas les cuesta más endeudarse.",
r"Según el BCRP, en junio de 2026 el riesgo país del Perú bajó a 108 puntos básicos, su nivel más bajo en 19 años, frente a un promedio de 294 en América Latina. En la región, solo Chile tuvo uno menor.",
],
ejemplo=[
r"Si los bonos de Estados Unidos rinden 4.0 % y los bonos del Perú en dólares rinden 5.5 %, el riesgo país es 1.5 puntos porcentuales, es decir, 150 puntos básicos.",
],
formula=dict(
tex=r"\text{Riesgo país}=(i_{\text{país}}-i_{\text{EE. UU.}})\times 100\ \text{puntos básicos}",
donde=[(r"i", "rendimiento de los bonos del gobierno, en %")],
calculo=[r"(5.5-4.0)\times 100=150\ \text{pb}"],
),
rel=["deuda-publica", "deficit-fiscal", "tasa-de-interes", "bcrp"],
))

T.append(dict(
slug="balanza-comercial", t="Balanza comercial", cat="comercio", ic="🚢",
alias="exportaciones importaciones superavit comercial",
corto="Es la diferencia entre lo que un país vende al exterior (exportaciones) y lo que compra (importaciones).",
simple=[
r"Si un país exporta más de lo que importa, tiene <strong>superávit comercial</strong>; si importa más, tiene <strong>déficit comercial</strong>.",
r"El Perú exporta sobre todo <strong>minerales</strong>: el cobre es cerca del 30 % de las exportaciones, y China compra alrededor de tres cuartas partes de ese cobre. Le siguen el oro, el zinc, la plata, los productos agrícolas (como arándanos, uvas y paltas) y los pesqueros. Importa bienes de capital (maquinaria), insumos, combustibles y bienes de consumo.",
r"Cuando los precios de los metales están altos, la balanza comercial peruana tiene un superávit grande: según el BCRP, entre junio de 2025 y mayo de 2026 llegó a un récord de unos US$ 44 000 millones.",
],
ejemplo=[
r"Si en un año el Perú exporta 70 mil millones de dólares e importa 50 mil millones, su balanza comercial tiene un superávit de 20 mil millones de dólares.",
],
formula=dict(
tex=r"BC=X-M",
donde=[(r"X", "exportaciones"), (r"M", "importaciones")],
calculo=[r"BC=70-50=20\ \text{mil millones de US\$}"],
),
rel=["terminos-de-intercambio", "pbi", "tipo-de-cambio", "depreciacion-y-apreciacion"],
))

T.append(dict(
slug="terminos-de-intercambio", t="Términos de intercambio", cat="comercio", ic="🔄",
alias="precio de exportaciones precio de importaciones precio de los metales",
corto="Comparan los precios de lo que un país exporta con los precios de lo que importa. Si suben, el país puede comprar más con lo que vende.",
simple=[
r"Los términos de intercambio son un <strong>cociente de precios</strong>: precios de exportación entre precios de importación. Si los metales que vende el Perú suben más que el petróleo y las máquinas que compra, los términos de intercambio <strong>mejoran</strong>.",
r"Para el Perú son muy importantes, porque sus exportaciones dependen mucho del precio del cobre y del oro. Mejores términos de intercambio traen más dólares, más inversión y más recaudación.",
],
ejemplo=[
r"Si en un año los precios de exportación suben 10 % y los de importación 2 %, los términos de intercambio mejoran alrededor de 8 %: con el mismo cobre, el Perú puede comprar más bienes importados.",
],
formula=dict(
tex=r"TI=\frac{IPX}{IPM}\times 100",
donde=[(r"IPX", "índice de precios de exportación"), (r"IPM", "índice de precios de importación")],
calculo=[r"TI=\frac{110}{102}\times 100\approx 107.8"],
),
rel=["balanza-comercial", "ciclo-economico", "tipo-de-cambio", "crecimiento-economico"],
))

T.append(dict(
slug="oferta-y-demanda", t="Oferta y demanda", cat="mercados", ic="🤝",
alias="precio de equilibrio mercado ley de la oferta ley de la demanda",
corto="La demanda es cuánto quieren comprar las personas a cada precio; la oferta, cuánto quieren vender los productores. Donde se cruzan se forma el precio.",
simple=[
r"<strong>Ley de la demanda</strong>: cuando un producto sube de precio, la gente compra menos. <strong>Ley de la oferta</strong>: cuando sube el precio, los productores quieren vender más.",
r"El precio de <strong>equilibrio</strong> es el punto donde la cantidad que la gente quiere comprar es igual a la que los productores quieren vender. Si el precio está por encima, sobra producto y el precio baja; si está por debajo, falta producto y el precio sube.",
],
ejemplo=[
r"Cuando un friaje o un huaico corta las carreteras, llegan menos limones a los mercados de Lima: la oferta cae y el precio sube. Cuando hay una gran cosecha, ocurre lo contrario.",
r"Con números: si la demanda de un producto es \(Q_d=100-2P\) y la oferta es \(Q_s=20+2P\), el equilibrio está en un precio de S/ 20 y una cantidad de 60 unidades.",
],
formula=dict(
tex=r"Q_d(P)=Q_s(P)",
donde=[(r"Q_d", "cantidad demandada"), (r"Q_s", "cantidad ofrecida"), (r"P", "precio")],
calculo=[r"100-2P=20+2P\ \Rightarrow\ 4P=80\ \Rightarrow\ P^{*}=20", r"Q^{*}=100-2(20)=60"],
),
rel=["elasticidad-precio", "monopolio", "costo-de-oportunidad", "inflacion"],
))

T.append(dict(
slug="elasticidad-precio", t="Elasticidad precio de la demanda", cat="mercados", ic="🪢",
alias="elasticidad bien elastico bien inelastico",
corto="Mide cuánto cambia la cantidad que se compra cuando cambia el precio. Si cambia mucho, la demanda es elástica; si cambia poco, es inelástica.",
simple=[
r"No todos los productos reaccionan igual a una subida de precio. Si sube la sal, compras casi lo mismo: su demanda es <strong>inelástica</strong>. Si sube una marca de gaseosa, muchos se pasan a otra: su demanda es <strong>elástica</strong>.",
r"Suelen ser inelásticos los bienes necesarios y sin buenos sustitutos (medicinas, sal, combustible a corto plazo). Suelen ser elásticos los que tienen muchos sustitutos o no son urgentes.",
],
ejemplo=[
r"Una cevichería sube el precio de su ceviche de S/ 20 a S/ 22 (10 % más) y sus ventas bajan de 100 a 85 platos (15 % menos). La elasticidad es 1.5: la demanda es elástica, y la subida le hizo perder ingresos (de S/ 2000 a S/ 1870).",
],
formula=dict(
tex=r"E_p=\left|\frac{\%\Delta Q}{\%\Delta P}\right|",
donde=[(r"E_p", "elasticidad precio (en valor absoluto)"), (r"\%\Delta Q", "cambio porcentual de la cantidad"), (r"\%\Delta P", "cambio porcentual del precio")],
calculo=[r"E_p=\left|\frac{-15\ \%}{10\ \%}\right|=1.5>1\ \Rightarrow\ \text{elástica}"],
),
rel=["oferta-y-demanda", "monopolio", "igv"],
))

T.append(dict(
slug="monopolio", t="Monopolio", cat="mercados", ic="👑",
alias="competencia oligopolio libre competencia indecopi",
corto="Es un mercado con un solo vendedor, que puede poner precios más altos porque no tiene competencia.",
simple=[
r"En <strong>competencia</strong>, muchas empresas compiten por los clientes y eso empuja los precios hacia abajo y la calidad hacia arriba. En un <strong>monopolio</strong> hay un solo vendedor, así que puede cobrar más y vender menos de lo que se vendería con competencia.",
r"Cuando hay pocas empresas grandes se habla de <strong>oligopolio</strong>. Si se ponen de acuerdo para subir precios, forman un <strong>cártel</strong>, lo cual está prohibido.",
r"En el Perú, el <strong>Indecopi</strong> defiende la libre competencia: investiga y sanciona los acuerdos de precios y los abusos de posición de dominio. Algunos servicios que son monopolios naturales, como la distribución de agua o luz, tienen tarifas reguladas por organismos como la Sunass y Osinergmin.",
],
ejemplo=[
r"Si en un pueblo hay una sola empresa de transporte hacia la ciudad, puede cobrar pasajes altos. Cuando entra una segunda empresa, el pasaje suele bajar.",
r"Un caso real de cártel: en 2022 el Indecopi multó con más de S/ 17 millones a cuatro cadenas de supermercados y a un proveedor por acordar un precio mínimo del pavo entero en las campañas navideñas de 2009 a 2016 (sanción en primera instancia).",
],
rel=["oferta-y-demanda", "elasticidad-precio", "punto-de-equilibrio"],
))

T.append(dict(
slug="punto-de-equilibrio", t="Punto de equilibrio", cat="mercados", ic="🎯",
alias="costos fijos costos variables margen de contribucion break even",
corto="Es la cantidad que un negocio debe vender para no ganar ni perder: los ingresos cubren justo todos sus costos.",
simple=[
r"Todo negocio tiene <strong>costos fijos</strong>, que se pagan aunque no vendas nada (alquiler, sueldos fijos, internet), y <strong>costos variables</strong>, que suben con cada unidad que vendes (insumos, empaques).",
r"Cada venta deja un <strong>margen de contribución</strong>: el precio menos su costo variable. El punto de equilibrio es la cantidad de ventas cuyo margen alcanza justo para pagar los costos fijos. Desde ahí en adelante, el negocio gana.",
],
ejemplo=[
r"Una juguería paga S/ 3000 al mes de costos fijos. Cada jugo se vende a S/ 8 y cuesta S/ 3 en fruta, azúcar y vaso. Cada jugo deja S/ 5, así que necesita vender 600 jugos al mes (unos 20 al día) para no perder.",
],
formula=dict(
tex=r"Q^{*}=\frac{CF}{P-CVu}",
donde=[(r"Q^{*}", "cantidad de equilibrio"), (r"CF", "costos fijos del periodo"), (r"P", "precio de venta por unidad"), (r"CVu", "costo variable por unidad")],
calculo=[r"Q^{*}=\frac{3000}{8-3}=600\ \text{jugos al mes}"],
),
rel=["van", "costo-de-oportunidad", "oferta-y-demanda", "monopolio"],
))

T.append(dict(
slug="pobreza-monetaria", t="Pobreza monetaria", cat="bienestar", ic="🏠",
alias="linea de pobreza canasta basica pobreza extrema",
corto="Una persona es pobre, en términos monetarios, cuando su gasto no alcanza para comprar una canasta básica de alimentos y otros bienes y servicios.",
simple=[
r"El INEI mide la pobreza comparando el <strong>gasto por persona</strong> de cada hogar con una <strong>línea de pobreza</strong>: el costo de una canasta básica de consumo (alimentos, vivienda, ropa, transporte, salud, educación). Si el gasto queda por debajo, la persona es pobre.",
r"La <strong>pobreza extrema</strong> usa una línea más baja: solo el costo de una canasta de <strong>alimentos</strong>. Quien está debajo no puede ni siquiera alimentarse bien.",
r"La pobreza monetaria es una de varias formas de medir la pobreza. Otras miran carencias como no tener agua potable, desagüe o acceso a la escuela.",
],
ejemplo=[
r"Según el INEI, en 2025 la línea de pobreza fue de S/ 462 por persona al mes (S/ 1848 para un hogar de 4) y la de pobreza extrema, S/ 260. Con esas líneas, el 25.7 % de los peruanos era pobre y el 4.7 %, pobre extremo. Un hogar de 4 personas que gasta S/ 1800 al mes (S/ 450 por persona) está por debajo de la línea: es pobre.",
],
formula=dict(
tex=r"\text{Pobre si}\quad \frac{G}{n}<L",
donde=[(r"G", "gasto mensual del hogar"), (r"n", "número de miembros del hogar"), (r"L", "línea de pobreza por persona")],
calculo=[r"\frac{1800}{4}=450<462\ \Rightarrow\ \text{pobre}"],
),
rel=["coeficiente-de-gini", "pbi-per-capita", "informalidad", "inflacion"],
))

T.append(dict(
slug="coeficiente-de-gini", t="Coeficiente de Gini", cat="bienestar", ic="🍰",
alias="gini desigualdad distribucion del ingreso curva de lorenz",
corto="Mide qué tan desigual es la distribución del ingreso: va de 0 (todos ganan igual) a 1 (una sola persona se queda con todo).",
simple=[
r"El coeficiente de Gini resume en un número cómo se reparte el «pastel» del ingreso. Si es <strong>0</strong>, todos tienen lo mismo (igualdad perfecta). Si es <strong>1</strong>, una sola persona tiene todo (desigualdad total).",
r"Se calcula a partir de la <strong>curva de Lorenz</strong>, que muestra qué porcentaje del ingreso total recibe el 10 %, 20 %, 30 %… más pobre de la población. Mientras más se aleja esa curva de la línea de igualdad, mayor es el Gini.",
r"Se puede expresar de 0 a 1 o de 0 a 100 (multiplicado por 100). América Latina es una de las regiones más desiguales del mundo.",
],
ejemplo=[
r"Si el área entre la línea de igualdad y la curva de Lorenz (A) es 0.2 y el área bajo la curva de Lorenz (B) es 0.3, el Gini es 0.2 ÷ 0.5 = 0.40.",
],
formula=dict(
tex=r"G=\frac{A}{A+B}",
donde=[(r"A", "área entre la línea de igualdad y la curva de Lorenz"), (r"B", "área bajo la curva de Lorenz")],
calculo=[r"G=\frac{0.2}{0.2+0.3}=0.40"],
),
rel=["pobreza-monetaria", "pbi-per-capita", "impuesto-a-la-renta"],
))
