# -*- coding: utf-8 -*-
# Términos del glosario (parte 4): segunda tanda tomada de la lista del
# Glosario de Términos Económicos del BCRP. Las definiciones están
# redactadas con palabras propias; el campo "bcrp" guarda el nombre exacto
# del término en ese glosario para citarlo como fuente.

T = []

T.append(dict(
slug="agregados-monetarios", t="Agregados monetarios", cat="dinero", ic="🪙",
bcrp="Agregados monetarios", alias="M1 M2 circulante cuasidinero liquidez oferta monetaria",
corto="Son las distintas formas de medir cuánto dinero hay en la economía, desde los billetes en el bolsillo hasta los ahorros en el banco.",
simple=[
r"No todo el dinero es igual de fácil de gastar. Por eso los bancos centrales lo miden en «capas», de lo más líquido a lo menos líquido. Cada capa es un <strong>agregado monetario</strong>.",
r"La primera capa es el <strong>circulante</strong>: billetes y monedas en manos del público. Si le sumas los depósitos que puedes usar al instante (cuentas corrientes), tienes el <strong>dinero</strong> en sentido estricto. Si además sumas los depósitos de ahorro y a plazo (el <strong>cuasidinero</strong>), obtienes la <strong>liquidez</strong> del sistema.",
r"El BCRP sigue estos agregados porque, si crecen mucho más rápido que la producción, pueden anticipar más <a href='inflacion.html'>inflación</a>.",
],
ejemplo=[
r"Si tienes S/ 100 en la billetera, S/ 500 en tu cuenta de sueldo y S/ 2000 en un depósito a plazo, los S/ 100 son circulante, los S/ 600 son «dinero» y los S/ 2600 forman parte de la liquidez.",
],
formula=dict(
tex=r"\text{Liquidez}=\underbrace{\text{Circulante}+\text{Depósitos a la vista}}_{\text{Dinero}}+\text{Cuasidinero}",
donde=[(r"\text{Cuasidinero}", "depósitos de ahorro y a plazo")],
),
rel=["base-monetaria", "dinero", "liquidez", "multiplicador-bancario", "bcrp"],
))

T.append(dict(
slug="brecha-ahorro-inversion", t="Brecha ahorro-inversión", cat="comercio", ic="⚖️",
bcrp="Brecha ahorro-inversión", alias="ahorro externo ahorro interno cuenta corriente",
corto="Es la diferencia entre lo que un país ahorra y lo que invierte. Si invierte más de lo que ahorra, cubre la diferencia con dinero del exterior.",
simple=[
r"Para construir carreteras, fábricas o casas, un país necesita ahorro. Si el ahorro interno (de familias, empresas y Estado) no alcanza para toda la inversión, la diferencia se financia con <strong>ahorro externo</strong>: préstamos o inversiones que llegan de afuera.",
r"Esa brecha aparece en la <a href='balanza-en-cuenta-corriente.html'>cuenta corriente</a>: cuando el país invierte más de lo que ahorra, la cuenta corriente tiene déficit. Cuando ahorra más de lo que invierte, tiene superávit y le presta al resto del mundo.",
],
ejemplo=[
r"Imagina un país que ahorra el 20 % de su PBI e invierte el 22 %. Le faltan 2 puntos del PBI, que llegan como inversión extranjera o deuda. Su cuenta corriente tendrá un déficit de alrededor de 2 % del PBI.",
],
formula=dict(
tex=r"S-I=CC",
donde=[(r"S", "ahorro interno"), (r"I", "inversión"), (r"CC", "saldo de la cuenta corriente")],
calculo=[r"20\ \%-22\ \%=-2\ \%\ \text{del PBI (déficit)}"],
),
rel=["ahorro", "inversion", "balanza-en-cuenta-corriente", "inversion-extranjera-directa"],
))

T.append(dict(
slug="apertura-comercial", t="Apertura comercial", cat="comercio", ic="🚢",
bcrp="Apertura comercial", alias="grado de apertura libre comercio globalización",
corto="Mide cuánto comercia un país con el mundo. Se calcula sumando exportaciones e importaciones y comparándolas con el PBI.",
simple=[
r"Un país es más «abierto» cuando compra y vende mucho al exterior y pone pocas trabas al comercio, como <a href='arancel.html'>aranceles</a> altos o prohibiciones.",
r"La apertura trae ventajas: más variedad de productos, precios más bajos y mercados más grandes para vender. También trae riesgos: el país depende más de lo que pasa afuera, como una caída en el precio de los minerales.",
],
ejemplo=[
r"Desde los años noventa, el Perú bajó sus aranceles y firmó muchos tratados de libre comercio. Por eso sus exportaciones e importaciones pesan mucho más en su PBI que hace treinta años.",
],
formula=dict(
tex=r"\text{Apertura}=\frac{X+M}{PBI}\times 100",
donde=[(r"X", "exportaciones"), (r"M", "importaciones"), (r"PBI", "producto bruto interno")],
calculo=[r"\frac{70+60}{280}\times 100\approx 46\ \%"],
),
rel=["balanza-comercial", "arancel", "zona-de-libre-comercio", "ventaja-comparativa"],
))

T.append(dict(
slug="arrendamiento-financiero", t="Arrendamiento financiero (leasing)", cat="finanzas", ic="🚚",
bcrp="Arrendamiento financiero", alias="leasing alquiler con opción de compra",
corto="Es un contrato en el que un banco compra un bien y te lo alquila por cuotas. Al final, puedes quedarte con él pagando un precio pequeño.",
simple=[
r"Si una empresa necesita un camión o una máquina y no tiene todo el dinero, puede pedir un <strong>leasing</strong>. El banco compra el bien y la empresa lo usa a cambio de cuotas mensuales.",
r"Al terminar el contrato, la empresa tiene una <strong>opción de compra</strong>: paga un monto final y el bien pasa a ser suyo. Mientras tanto, el bien es del banco, lo que le da más seguridad y suele bajar el costo del financiamiento.",
],
ejemplo=[
r"Una empresa de transporte de Arequipa quiere un camión de S/ 300 000. En lugar de pedir un préstamo, firma un leasing a cinco años: paga cuotas mensuales y, al final, ejerce la opción de compra con un pago pequeño para quedarse con el camión.",
],
ojo=["Antes de firmar, compara la TCEA del leasing con la de un préstamo normal: es la mejor forma de saber cuál cuesta menos."],
rel=["tcea", "amortizacion", "inversion", "bienes-de-capital-y-de-consumo"],
))

T.append(dict(
slug="asociaciones-publico-privadas", t="Asociaciones público-privadas (APP)", cat="estado", ic="🤝",
bcrp="Asociaciones Público Privadas", alias="APP concesiones ProInversión infraestructura",
corto="Son acuerdos en los que el Estado y una empresa privada se juntan para construir u operar obras o servicios públicos, compartiendo riesgos.",
simple=[
r"En una APP, una empresa privada pone dinero y experiencia para construir, mantener u operar una obra pública, como una carretera o un aeropuerto. A cambio, recibe pagos del Estado, cobra tarifas a los usuarios o ambas cosas, durante muchos años.",
r"La idea es aprovechar la eficiencia privada sin que el Estado tenga que pagar todo de golpe. El riesgo es que, si el contrato está mal hecho, el Estado termine pagando de más o la obra se retrase. En el Perú, ProInversión promueve estos proyectos.",
],
ejemplo=[
r"El aeropuerto Jorge Chávez de Lima es operado por una empresa privada bajo un contrato de concesión con el Estado: la empresa invierte en el aeropuerto y, a cambio, cobra tarifas durante el plazo del contrato.",
],
rel=["inversion", "politica-fiscal", "deuda-publica", "presupuesto-publico"],
))

T.append(dict(
slug="balance-general", t="Balance general", cat="mercados", ic="📊",
bcrp="Balance general", alias="estado de situación financiera activo pasivo patrimonio",
corto="Es una «foto» de lo que una empresa tiene, lo que debe y lo que les pertenece a sus dueños en una fecha determinada.",
simple=[
r"El balance general tiene tres partes. Los <strong>activos</strong> son lo que la empresa tiene: dinero, mercadería, máquinas, cuentas por cobrar. Los <strong>pasivos</strong> son lo que debe: préstamos, proveedores, impuestos por pagar. El <strong>patrimonio</strong> es lo que queda para los dueños.",
r"Siempre se cumple que los activos son iguales a los pasivos más el patrimonio. Por eso se llama «balance»: los dos lados pesan lo mismo.",
],
ejemplo=[
r"Una bodega tiene S/ 40 000 entre mercadería, refrigeradora y caja. Le debe S/ 15 000 a una caja municipal. Su patrimonio es S/ 25 000: lo que de verdad es del dueño.",
],
formula=dict(
tex=r"\text{Activo}=\text{Pasivo}+\text{Patrimonio}",
calculo=[r"40\,000=15\,000+25\,000"],
),
rel=["apalancamiento", "accion", "dividendo", "rentabilidad"],
))

T.append(dict(
slug="banco-de-la-nacion", t="Banco de la Nación", cat="dinero", ic="🏛️",
bcrp="Banco de la Nación – BN", alias="BN banco del Estado Multired agente",
corto="Es el banco del Estado peruano. Maneja las cuentas del gobierno y lleva servicios bancarios a lugares donde no llegan otros bancos.",
simple=[
r"El Banco de la Nación no compite como un banco común: su tarea principal es atender al Estado. Por él pasan pagos y cobros del gobierno, y muchos trabajadores y pensionistas públicos reciben ahí su dinero.",
r"También tiene un papel de <a href='bancarizacion.html'>inclusión financiera</a>: abre agencias y agentes en distritos alejados, donde a veces es el único banco. A través de él se pagan programas sociales como Pensión 65 y Juntos.",
r"No hay que confundirlo con el <a href='bcrp.html'>BCRP</a>: el Banco Central no atiende al público, y el Banco de la Nación sí.",
],
ejemplo=[
r"Según una nota de Andina de enero de 2026, el Banco de la Nación está presente en más del 94 % de los distritos y es la única oferta bancaria en más de 350 de ellos. Un tercio de sus clientes activos recibe fondos de programas sociales.",
],
rel=["bcrp", "bancarizacion", "sistema-financiero", "sbs"],
))

T.append(dict(
slug="base-imponible", t="Base imponible", cat="impuestos", ic="🧾",
bcrp="Base imponible", alias="monto gravado base del impuesto",
corto="Es el monto sobre el que se calcula un impuesto. Al multiplicarlo por la tasa, sale cuánto hay que pagar.",
simple=[
r"Todo impuesto tiene dos piezas: la <strong>base imponible</strong> (sobre qué monto se cobra) y la <strong>tasa</strong> (qué porcentaje se cobra). En el <a href='igv.html'>IGV</a>, la base es el valor de venta sin impuesto; en el <a href='impuesto-a-la-renta.html'>impuesto a la renta</a>, es la renta neta después de las deducciones permitidas.",
r"Por eso dos personas con el mismo sueldo pueden pagar distinto: si una tiene más deducciones, su base imponible es menor.",
],
ejemplo=[
r"Una zapatería vende un par a S/ 100 sin IGV. La base imponible es S/ 100 y la tasa total del IGV es 18 %, así que el impuesto es S/ 18 y el cliente paga S/ 118.",
],
formula=dict(
tex=r"\text{Impuesto}=\text{Base imponible}\times\text{Tasa}",
calculo=[r"100\times 0.18=18\ \text{soles}"],
),
rel=["igv", "impuesto-a-la-renta", "tributo", "credito-fiscal"],
))

T.append(dict(
slug="bienes-de-capital-y-de-consumo", t="Bienes de capital y bienes de consumo", cat="produccion", ic="🏭",
bcrp="Bienes de capital", alias="maquinaria equipos bienes duraderos insumos",
corto="Los bienes de consumo los usan las familias para satisfacer sus necesidades. Los bienes de capital sirven para producir otros bienes.",
simple=[
r"Un pan, una camisa o un celular para uso personal son <strong>bienes de consumo</strong>. Algunos se acaban rápido (no duraderos, como los alimentos) y otros duran años (duraderos, como una refrigeradora).",
r"Una máquina, un tractor o un camión de reparto son <strong>bienes de capital</strong>: no se compran para disfrutarlos, sino para producir. Cuando las empresas compran más bienes de capital, aumenta la <a href='inversion.html'>inversión</a> y el país puede producir más en el futuro.",
],
ejemplo=[
r"Las estadísticas de importaciones del Perú se separan en bienes de consumo, insumos y bienes de capital. Si suben mucho las importaciones de bienes de capital, es una señal de que las empresas están invirtiendo.",
],
rel=["inversion", "consumo", "formacion-bruta-de-capital", "productividad"],
))

T.append(dict(
slug="choques-de-oferta-y-demanda", t="Choques de oferta y de demanda", cat="produccion", ic="⚡",
bcrp="Choques de oferta", alias="shock de oferta shock de demanda perturbaciones",
corto="Son sucesos inesperados que cambian de golpe cuánto se produce (oferta) o cuánto se quiere comprar (demanda) en la economía.",
simple=[
r"Un <strong>choque de oferta</strong> afecta la capacidad de producir: una sequía, un terremoto o una subida fuerte del petróleo. Los choques de oferta negativos suelen subir los precios y bajar la producción a la vez.",
r"Un <strong>choque de demanda</strong> cambia las ganas o la capacidad de gastar: una crisis de confianza, un bono del gobierno o una caída de las exportaciones. Si la demanda cae, bajan la producción y la presión sobre los precios.",
r"Distinguirlos importa: el <a href='bcrp.html'>BCRP</a> suele reaccionar distinto ante cada uno.",
],
ejemplo=[
r"Un Fenómeno El Niño fuerte puede destruir cultivos y carreteras. Es un choque de oferta: hay menos alimentos y sus precios suben, aunque la gente no quiera comprar más que antes.",
],
rel=["oferta-agregada", "demanda-agregada", "inflacion", "estanflacion", "politica-monetaria"],
))

T.append(dict(
slug="crecimiento-potencial", t="Crecimiento potencial", cat="produccion", ic="🚀",
bcrp="Crecimiento potencial", alias="PBI potencial producto potencial",
corto="Es cuánto puede crecer una economía cada año sin generar inflación, usando normalmente sus trabajadores, máquinas y tecnología.",
simple=[
r"Una economía puede crecer muy rápido por un tiempo si hay mucho gasto, pero si produce por encima de su capacidad, los precios empiezan a subir. El <strong>crecimiento potencial</strong> es el ritmo «sostenible» que permiten sus recursos.",
r"Depende de tres cosas: cuántas personas trabajan, cuánto capital (máquinas, carreteras) hay y qué tan productivo es todo eso. Para subirlo hacen falta más inversión, mejor educación y menos trabas: no basta con gastar más.",
],
ejemplo=[
r"Si un país tiene un crecimiento potencial de 3 % y un año crece 6 % por un auge de consumo, probablemente aparezcan presiones inflacionarias. Si crece solo 1 %, tiene recursos sin usar: una <a href='brecha-del-producto.html'>brecha del producto</a> negativa.",
],
rel=["brecha-del-producto", "crecimiento-economico", "productividad", "pbi"],
))

T.append(dict(
slug="credito-fiscal", t="Crédito fiscal", cat="impuestos", ic="🧮",
bcrp="Crédito fiscal", alias="IGV de compras descuento del IGV factura",
corto="Es el IGV que una empresa pagó en sus compras y que puede restar del IGV que cobra en sus ventas.",
simple=[
r"El <a href='igv.html'>IGV</a> se cobra en cada etapa de la cadena, pero cada empresa solo debe pagar al fisco el impuesto sobre lo que ella añadió. Para lograrlo, resta el IGV que ya pagó a sus proveedores: ese monto es su <strong>crédito fiscal</strong>.",
r"Para usarlo, la compra debe estar sustentada con una <strong>factura</strong> válida y relacionada con el negocio. Por eso a las empresas les conviene comprar con factura y no con boleta.",
],
ejemplo=[
r"Una panadería compra harina y cobra IGV por sus panes. En un mes, cobra S/ 1800 de IGV en ventas y pagó S/ 1000 de IGV en compras con factura. A la SUNAT solo le paga la diferencia: S/ 800.",
],
formula=dict(
tex=r"\text{IGV por pagar}=\text{IGV de ventas}-\text{Crédito fiscal}",
calculo=[r"1800-1000=800\ \text{soles}"],
),
rel=["igv", "base-imponible", "valor-agregado", "tributo"],
))

T.append(dict(
slug="cuentas-nacionales", t="Cuentas nacionales", cat="produccion", ic="📒",
bcrp="Cuentas nacionales", alias="contabilidad nacional PBI INEI",
corto="Es el sistema de estadísticas que mide toda la actividad económica de un país: cuánto produce, cuánto gasta y cuánto gana.",
simple=[
r"Así como una empresa lleva su contabilidad, un país lleva sus <strong>cuentas nacionales</strong>. De ahí salen cifras como el <a href='pbi.html'>PBI</a>, el consumo, la inversión o el ingreso nacional.",
r"El PBI se puede medir de tres formas que deben dar el mismo resultado: sumando lo que produce cada sector (producción), sumando lo que se gasta (consumo, inversión, gasto público y exportaciones netas) o sumando lo que se gana (sueldos, utilidades e impuestos).",
],
ejemplo=[
r"En el Perú, el INEI elabora las cuentas nacionales y publica cada mes cuánto creció la producción; el BCRP las usa para sus proyecciones.",
],
formula=dict(
tex=r"PBI=C+I+G+(X-M)",
donde=[(r"C", "consumo privado"), (r"I", "inversión"), (r"G", "gasto público"), (r"X-M", "exportaciones netas")],
),
rel=["pbi", "valor-agregado", "ingreso-nacional", "demanda-interna"],
))

T.append(dict(
slug="demanda-interna", t="Demanda interna", cat="produccion", ic="🛒",
bcrp="Demanda interna", alias="gasto interno consumo inversión gasto público",
corto="Es todo lo que gastan dentro del país las familias, las empresas y el Estado, sin contar las exportaciones.",
simple=[
r"La demanda interna suma el <a href='consumo.html'>consumo</a> (privado y público) y la <a href='inversion.html'>inversión</a> (privada y pública). Mide la fuerza del gasto «de casa».",
r"Si la demanda interna crece rápido, suele ser buena señal para el empleo y los negocios locales. Pero si crece mucho más que la producción, el país tiene que importar más y pueden subir los precios.",
],
ejemplo=[
r"Cuando un gobierno aumenta la inversión pública en carreteras y las familias gastan más por la gratificación de julio, la demanda interna sube aunque las exportaciones no cambien.",
],
formula=dict(
tex=r"DI=C+I+G",
donde=[(r"C", "consumo privado"), (r"I", "inversión"), (r"G", "gasto del gobierno")],
),
rel=["demanda-agregada", "consumo", "inversion", "cuentas-nacionales"],
))

T.append(dict(
slug="demanda-de-dinero", t="Demanda de dinero", cat="dinero", ic="👛",
bcrp="Demanda por dinero", alias="preferencia por liquidez motivo transacción",
corto="Es cuánto dinero en efectivo o en cuentas a la vista quiere tener la gente, en lugar de guardarlo en inversiones que rinden más.",
simple=[
r"Tener dinero «a la mano» es cómodo, pero no paga intereses. Por eso la gente decide cuánto mantener líquido y cuánto invertir. Esa decisión, sumada en toda la economía, es la <strong>demanda de dinero</strong>.",
r"Se pide dinero por tres motivos: para hacer compras del día a día (transacción), para emergencias (precaución) y para esperar mejores oportunidades (especulación). Cuando suben los ingresos, se demanda más dinero; cuando suben las tasas de interés, se demanda menos, porque guardar dinero sin rendimiento sale más caro.",
],
ejemplo=[
r"En diciembre la gente quiere más efectivo para las compras navideñas. El BCRP lo sabe y se asegura de que haya suficientes billetes y liquidez en los bancos.",
],
rel=["dinero", "tasa-de-interes", "agregados-monetarios", "velocidad-del-dinero"],
))

T.append(dict(
slug="deuda-externa", t="Deuda externa", cat="estado", ic="🌎",
bcrp="Deuda externa", alias="deuda con el exterior acreedores extranjeros",
corto="Es lo que el Estado, las empresas o los bancos de un país les deben a acreedores de otros países.",
simple=[
r"Cuando un país pide prestado a bancos extranjeros, organismos como el Banco Mundial o compradores extranjeros de sus bonos, se endeuda con el exterior. Esa es la <strong>deuda externa</strong>, y puede ser pública (del Estado) o privada (de empresas).",
r"Suele estar en dólares u otras monedas extranjeras, así que si el sol se deprecia, pagarla cuesta más soles. Por eso los países prudentes cuidan cuánta deuda tienen en moneda extranjera.",
],
ejemplo=[
r"En los años ochenta, el Perú dejó de pagar parte de su deuda externa y perdió acceso al crédito internacional. Hoy, gracias a su bajo endeudamiento, puede emitir bonos en el exterior a tasas mucho menores.",
],
rel=["deuda-publica", "bono-soberano", "riesgo-pais", "descalce-de-monedas"],
))

T.append(dict(
slug="devaluacion", t="Devaluación", cat="dinero", ic="📉",
bcrp="Devaluación monetaria", alias="devaluar moneda tipo de cambio fijo",
corto="Es cuando el gobierno o el banco central decide subir el precio oficial de la moneda extranjera, es decir, bajar el valor de su propia moneda.",
simple=[
r"La palabra se usa sobre todo cuando hay <strong>tipo de cambio fijo</strong>: el banco central fija el precio del dólar y, un día, lo sube por decisión propia. Eso es una devaluación.",
r"Cuando el tipo de cambio es flotante, como en el Perú, el precio del dólar lo fija el mercado. Si el sol pierde valor por la oferta y la demanda, lo correcto es decir que se <a href='depreciacion-y-apreciacion.html'>deprecia</a>, aunque en la calle muchos digan «devaluación».",
],
ejemplo=[
r"En los años ochenta, con tipos de cambio controlados, el Perú vivió devaluaciones frecuentes de su moneda, que encarecían de golpe los productos importados.",
],
formula=dict(
tex=r"\%\,\text{devaluación}=\frac{TC_{\text{nuevo}}-TC_{\text{anterior}}}{TC_{\text{anterior}}}\times 100",
donde=[(r"TC", "tipo de cambio oficial (soles por dólar)")],
calculo=[r"\frac{4-3.2}{3.2}\times 100=25\ \%"],
),
rel=["tipo-de-cambio", "depreciacion-y-apreciacion", "regimen-cambiario", "hiperinflacion"],
))

T.append(dict(
slug="dividendo", t="Dividendo", cat="mercados", ic="💵",
bcrp="Dividendo", alias="reparto de utilidades accionistas",
corto="Es la parte de las ganancias de una empresa que se reparte entre sus accionistas.",
simple=[
r"Cuando una empresa gana dinero, la junta de accionistas decide qué hacer con esas utilidades: reinvertirlas en el negocio o repartir una parte. Lo que se reparte son los <strong>dividendos</strong>, y cada accionista recibe según cuántas <a href='accion.html'>acciones</a> tiene.",
r"No todas las empresas pagan dividendos. Las que están creciendo rápido suelen reinvertirlo todo; las más maduras suelen repartir más.",
],
ejemplo=[
r"Tienes 1000 acciones de una empresa que reparte S/ 0.30 por acción. Recibes S/ 300. Si cada acción vale S/ 6, el rendimiento por dividendo es 5 %.",
],
formula=dict(
tex=r"\text{Rendimiento por dividendo}=\frac{D}{P}\times 100",
donde=[(r"D", "dividendo por acción"), (r"P", "precio de la acción")],
calculo=[r"\frac{0.30}{6}\times 100=5\ \%"],
),
rel=["accion", "bolsa-de-valores", "rentabilidad", "balance-general"],
))

T.append(dict(
slug="divisa", t="Divisa", cat="dinero", ic="💱",
bcrp="Divisa", alias="moneda extranjera dólares euros",
corto="Es una moneda extranjera que se acepta en los pagos internacionales, como el dólar o el euro.",
simple=[
r"Para comprar productos de otros países, viajar o pagar deudas externas, se necesitan <strong>divisas</strong>. Las más usadas en el mundo son el dólar estadounidense, el euro, el yen y la libra.",
r"Un país consigue divisas exportando, recibiendo inversión extranjera o <a href='remesas.html'>remesas</a>. El BCRP guarda una parte como <a href='reservas-internacionales.html'>reservas internacionales</a> para usarlas en momentos difíciles.",
],
ejemplo=[
r"Cuando una minera peruana exporta cobre, recibe dólares. Al cambiarlos a soles para pagar sueldos e impuestos, aumenta la oferta de divisas en el mercado y eso ayuda a que el dólar no suba.",
],
rel=["tipo-de-cambio", "reservas-internacionales", "dolarizacion", "balanza-de-pagos"],
))

T.append(dict(
slug="descalce-de-monedas", t="Descalce de monedas", cat="finanzas", ic="⚠️",
bcrp="Descalce de monedas", alias="riesgo cambiario crediticio deuda en dólares ingresos en soles efecto hoja de balance",
corto="Es cuando alguien gana en una moneda pero tiene deudas en otra. Si la moneda de la deuda sube, la deuda se vuelve más pesada.",
simple=[
r"Si cobras tu sueldo en soles pero tu préstamo está en dólares, estás <strong>descalzado</strong>. Mientras el dólar esté estable, no pasa nada; pero si sube mucho, necesitas más soles para pagar la misma cuota.",
r"Cuando muchas familias y empresas están descalzadas, una subida fuerte del dólar puede causar impagos masivos. A ese daño en las cuentas de deudores y bancos se le llama <strong>efecto hoja de balance</strong>. Por eso el BCRP impulsó la <a href='dolarizacion.html'>desdolarización</a> del crédito.",
],
ejemplo=[
r"Pagas una cuota de US$ 200 al mes. Con el dólar a S/ 3.40 son S/ 680; si el dólar sube a S/ 3.90, la misma cuota cuesta S/ 780, aunque tu sueldo en soles no haya cambiado.",
],
formula=dict(
tex=r"\text{Cuota en soles}=\text{Cuota en dólares}\times TC",
calculo=[r"200\times 3.90=780\ \text{soles}"],
),
ojo=["La regla práctica es endeudarte en la misma moneda en la que recibes tus ingresos."],
rel=["dolarizacion", "riesgo-cambiario", "tipo-de-cambio", "encaje-bancario"],
))

T.append(dict(
slug="esterilizacion", t="Esterilización monetaria", cat="dinero", ic="🧽",
bcrp="Esterilización", alias="operaciones de esterilización CD BCRP intervención esterilizada",
corto="Es cuando el banco central retira del mercado los soles que puso al comprar dólares, para que no sobre dinero y no suba la inflación.",
simple=[
r"Cuando el BCRP compra dólares para evitar que el tipo de cambio baje demasiado, paga con soles nuevos. Esos soles aumentan la liquidez y podrían empujar la inflación.",
r"Para evitarlo, el BCRP los «recoge» vendiendo instrumentos como sus certificados de depósito (CD BCRP): los bancos le entregan soles y reciben un título que paga intereses. Así, el efecto sobre la cantidad de dinero se neutraliza. Eso es <strong>esterilizar</strong>.",
],
ejemplo=[
r"Si el BCRP compra US$ 100 millones a S/ 3.70, inyecta S/ 370 millones. Si luego coloca S/ 370 millones en CD BCRP, la cantidad de soles en el mercado queda casi igual que antes.",
],
rel=["intervencion-cambiaria", "operacion-de-mercado-abierto", "base-monetaria", "reservas-internacionales"],
))

T.append(dict(
slug="exoneracion-tributaria", t="Exoneración tributaria", cat="impuestos", ic="🎟️",
bcrp="Exoneración tributaria", alias="exonerado beneficio tributario inafecto",
corto="Es cuando una ley libera de pagar un impuesto a ciertas personas, productos o zonas, normalmente por un tiempo.",
simple=[
r"Una actividad puede estar dentro del alcance de un impuesto y, aun así, no pagarlo porque una ley la <strong>exonera</strong>. Las exoneraciones suelen tener fecha de vencimiento y buscan promover algo: una región, un sector o un producto.",
r"No es lo mismo que estar <strong>inafecto</strong>: lo inafecto está fuera del impuesto desde el inicio, mientras que lo exonerado sí estaría gravado, pero se le perdona por ley. La Constitución dice que los tributos solo se exoneran por ley o decreto legislativo.",
r"Las exoneraciones tienen un costo: el Estado deja de recaudar y otros contribuyentes terminan cargando más.",
],
ejemplo=[
r"Ciertas ventas en zonas de la Amazonía peruana tienen exoneraciones del IGV para promover la inversión en esa región.",
],
rel=["tributo", "igv", "presion-tributaria", "subsidio"],
))

T.append(dict(
slug="regimen-cambiario", t="Régimen cambiario", cat="dinero", ic="🎚️",
bcrp="Régimen cambiario", alias="tipo de cambio fijo flotante flotación administrada",
corto="Es la regla que sigue un país para decidir el precio de su moneda frente a las demás: fijo, flotante o algo intermedio.",
simple=[
r"Con <strong>tipo de cambio fijo</strong>, el banco central se compromete a mantener un precio (por ejemplo, 1 a 1 con el dólar). Da estabilidad, pero obliga a tener muchas reservas y quita libertad para manejar las tasas de interés.",
r"Con <strong>tipo de cambio flotante</strong>, el precio lo deciden la oferta y la demanda. En la <strong>flotación administrada</strong>, el mercado decide, pero el banco central interviene para evitar saltos bruscos.",
],
ejemplo=[
r"El Perú tiene flotación administrada: el dólar sube o baja según el mercado, pero el BCRP compra o vende dólares cuando hay mucha volatilidad. En 2021, por ejemplo, vendió miles de millones de dólares para calmar al mercado.",
],
rel=["tipo-de-cambio", "intervencion-cambiaria", "devaluacion", "reservas-internacionales"],
))

T.append(dict(
slug="formacion-bruta-de-capital", t="Formación bruta de capital", cat="produccion", ic="🏗️",
bcrp="Formación bruta de capital", alias="inversión bruta FBKF existencias",
corto="Es el nombre técnico de la inversión en las cuentas nacionales: lo que se gasta en construcciones, maquinaria y en aumentar inventarios.",
simple=[
r"Tiene dos partes. La <strong>formación bruta de capital fijo</strong> es lo que se invierte en cosas que duran: edificios, carreteras, máquinas, vehículos. La <strong>variación de existencias</strong> es cuánto aumentan o disminuyen los inventarios de las empresas.",
r"Se llama «bruta» porque no descuenta el desgaste del capital que ya existía (la depreciación). Si se descuenta, se obtiene la inversión neta.",
],
ejemplo=[
r"Si en un año se construyen viviendas, una minera compra camiones y las tiendas llenan sus almacenes para Navidad, todo eso suma a la formación bruta de capital del Perú.",
],
formula=dict(
tex=r"FBK=FBKF+\Delta\text{Existencias}",
donde=[(r"FBKF", "formación bruta de capital fijo"), (r"\Delta\text{Existencias}", "variación de inventarios")],
),
rel=["inversion", "bienes-de-capital-y-de-consumo", "cuentas-nacionales", "crecimiento-potencial"],
))

T.append(dict(
slug="ilusion-monetaria", t="Ilusión monetaria", cat="precios", ic="🎭",
bcrp="Ilusión monetaria", alias="confundir nominal con real",
corto="Es el error de fijarse en la cantidad de soles y no en lo que realmente se puede comprar con ellos.",
simple=[
r"Si tu sueldo sube 5 % pero los precios suben 8 %, tienes más soles pero puedes comprar menos. Quien se siente más rico en ese caso sufre <strong>ilusión monetaria</strong>: mira el valor nominal y no el <a href='valor-nominal-y-real.html'>valor real</a>.",
r"Este error es común en negociaciones de sueldos, alquileres o ahorros: un aumento «grande» puede ser, en realidad, una pérdida de <a href='poder-adquisitivo.html'>poder adquisitivo</a>.",
],
ejemplo=[
r"Tu sueldo pasa de S/ 2000 a S/ 2100 (sube 5 %), pero la inflación del año fue 8 %. En términos reales tu sueldo bajó cerca de 3 %.",
],
formula=dict(
tex=r"\text{Variación real}\approx\text{Variación nominal}-\pi",
donde=[(r"\pi", "inflación del periodo")],
calculo=[r"5\ \%-8\ \%=-3\ \%"],
),
rel=["valor-nominal-y-real", "poder-adquisitivo", "inflacion", "tasa-de-interes-real"],
herramienta=("Calcula cuánto valen hoy tus soles de otro año", "../inflacion/"),
))

T.append(dict(
slug="impuesto-directo-e-indirecto", t="Impuesto directo e indirecto", cat="impuestos", ic="🏷️",
bcrp="Impuesto directo", alias="impuestos directos indirectos renta IGV ISC",
corto="El impuesto directo grava lo que ganas o tienes. El indirecto grava lo que compras o consumes.",
simple=[
r"Los <strong>impuestos directos</strong> recaen sobre la persona según su ingreso o su patrimonio, como el <a href='impuesto-a-la-renta.html'>impuesto a la renta</a> o el impuesto predial. Se pueden ajustar para que quien gana más pague más.",
r"Los <strong>impuestos indirectos</strong> se cobran en el precio de los productos, como el <a href='igv.html'>IGV</a> o el impuesto selectivo al consumo (ISC) de cigarrillos o bebidas alcohólicas. Los paga igual el rico y el pobre en cada compra, por eso pesan más, en proporción, a quien gana menos.",
],
ejemplo=[
r"Una trabajadora paga impuesto a la renta por su sueldo (directo) y, cada vez que compra en el supermercado, paga IGV incluido en el precio (indirecto).",
],
rel=["tributo", "impuesto-a-la-renta", "igv", "presion-tributaria"],
))

T.append(dict(
slug="indice-big-mac", t="Índice Big Mac", cat="comercio", ic="🍔",
bcrp="Índice Big Mac", alias="paridad de poder adquisitivo hamburguesa The Economist",
corto="Es una forma sencilla de ver si una moneda está cara o barata, comparando el precio de la misma hamburguesa en distintos países.",
simple=[
r"Lo inventó la revista <em>The Economist</em> como aplicación divertida de la <a href='paridad-del-poder-adquisitivo.html'>paridad del poder adquisitivo</a>. La idea: si una hamburguesa es igual en todo el mundo, debería costar lo mismo una vez convertida a dólares.",
r"Si en un país sale más barata en dólares que en Estados Unidos, su moneda estaría «subvaluada»; si sale más cara, estaría «sobrevaluada». Es una guía aproximada, no una predicción: los sueldos, alquileres e impuestos cambian mucho entre países.",
],
ejemplo=[
r"Con números de ejemplo: si la hamburguesa cuesta S/ 15 en Lima y US$ 5.50 en Estados Unidos, el tipo de cambio que la iguala sería S/ 2.73 por dólar. Si el dólar real está en S/ 3.70, el sol estaría subvaluado según este índice.",
],
formula=dict(
tex=r"TC_{\text{implícito}}=\frac{P_{\text{Perú}}}{P_{\text{EE. UU.}}}",
donde=[(r"P_{\text{Perú}}", "precio en soles"), (r"P_{\text{EE. UU.}}", "precio en dólares")],
calculo=[r"\frac{15}{5.50}\approx 2.73\ \text{soles por dólar}"],
),
rel=["paridad-del-poder-adquisitivo", "tipo-de-cambio", "tipo-de-cambio-real", "poder-adquisitivo"],
))

T.append(dict(
slug="indice-de-desarrollo-humano", t="Índice de desarrollo humano (IDH)", cat="bienestar", ic="🌱",
bcrp="Índice de Desarrollo Humano", alias="IDH PNUD bienestar salud educación",
corto="Es un indicador del PNUD que mide el bienestar de un país combinando salud, educación e ingresos, en una escala de 0 a 1.",
simple=[
r"El PBI per cápita dice cuánto se produce por persona, pero no si la gente vive muchos años o estudia. El <strong>IDH</strong> junta tres dimensiones: una vida larga y saludable (esperanza de vida), conocimientos (años de estudio) y un nivel de vida digno (ingreso por persona).",
r"Cada dimensión se convierte en un índice entre 0 y 1, y el IDH es su promedio geométrico. Así, un país no puede compensar del todo una salud muy mala con ingresos altos.",
],
ejemplo=[
r"El PNUD también calcula un IDH por regiones dentro del Perú. Ahí se ve que, en un mismo país, hay regiones con niveles de salud, educación e ingresos muy distintos.",
],
formula=dict(
tex=r"IDH=\left(I_{\text{salud}}\times I_{\text{educación}}\times I_{\text{ingreso}}\right)^{1/3}",
donde=[(r"I", "índice de cada dimensión, entre 0 y 1")],
calculo=[r"(0.85\times 0.70\times 0.72)^{1/3}\approx 0.75"],
),
rel=["pbi-per-capita", "pobreza-monetaria", "coeficiente-de-gini", "crecimiento-economico"],
))

T.append(dict(
slug="intermediacion-financiera", t="Intermediación financiera", cat="dinero", ic="🔁",
bcrp="Intermediación financiera", alias="spread bancario captar prestar",
corto="Es el trabajo de los bancos y otras entidades de recibir el dinero de quienes ahorran y prestárselo a quienes lo necesitan.",
simple=[
r"Una persona que ahorra y una empresa que necesita un préstamo casi nunca se conocen. Los bancos, cajas y financieras hacen de puente: <strong>captan</strong> depósitos y <strong>colocan</strong> préstamos.",
r"Ganan con la diferencia entre la tasa que cobran por prestar y la que pagan por los depósitos (el <strong>margen</strong> o <em>spread</em>). A cambio, asumen el riesgo de que alguien no pague y reúnen información para decidir a quién prestar.",
],
ejemplo=[
r"Un banco paga 3 % al año por un depósito a plazo y presta ese dinero a una mype al 20 %. El margen de 17 puntos cubre costos, morosidad y la ganancia del banco.",
],
formula=dict(
tex=r"\text{Margen}=i_{\text{activa}}-i_{\text{pasiva}}",
calculo=[r"20\ \%-3\ \%=17\ \text{puntos}"],
),
rel=["tasa-de-interes-activa-y-pasiva", "sistema-financiero", "bancarizacion", "cartera-morosa"],
))

T.append(dict(
slug="multiplicador-bancario", t="Multiplicador bancario", cat="dinero", ic="✖️",
bcrp="Multiplicador bancario", alias="multiplicador monetario creación de dinero encaje",
corto="Explica cómo los bancos, al prestar una parte de los depósitos, terminan creando más dinero del que puso el banco central.",
simple=[
r"Cuando depositas S/ 100, el banco guarda una parte como <a href='encaje-bancario.html'>encaje</a> y presta el resto. Ese préstamo se gasta y vuelve a depositarse en otro banco, que también presta una parte, y así sucesivamente.",
r"Al final, los S/ 100 iniciales se convierten en varias veces esa cantidad en depósitos. Cuanto más bajo es el encaje, mayor es el <strong>multiplicador</strong>. En la práctica es menor que la fórmula simple, porque la gente también guarda efectivo.",
],
ejemplo=[
r"Con un encaje de 10 %, un depósito nuevo de S/ 1000 puede convertirse, en teoría, en hasta S/ 10 000 de depósitos en todo el sistema.",
],
formula=dict(
tex=r"m=\frac{1}{r}\qquad \Delta D=m\times\Delta\text{Depósito inicial}",
donde=[(r"m", "multiplicador"), (r"r", "tasa de encaje (en decimales)"), (r"\Delta D", "aumento total de depósitos")],
calculo=[r"m=\frac{1}{0.10}=10\qquad 10\times 1000=10\,000"],
),
rel=["encaje-bancario", "base-monetaria", "agregados-monetarios", "dinero"],
))

T.append(dict(
slug="operacion-de-mercado-abierto", t="Operaciones de mercado abierto", cat="dinero", ic="🔄",
bcrp="Operación de mercado abierto", alias="repos CD BCRP inyección esterilización liquidez",
corto="Son compras y ventas de títulos que hace el banco central con los bancos para darles o quitarles soles y guiar la tasa de interés.",
simple=[
r"Si a los bancos les falta liquidez, el BCRP les <strong>inyecta</strong> soles, por ejemplo con operaciones de reporte (repos): les presta soles a cambio de títulos como garantía. Si les sobra, los <strong>retira</strong> vendiéndoles sus certificados de depósito.",
r"Con estas operaciones, el BCRP logra que la tasa a la que se prestan los bancos entre sí (la <a href='tasa-de-interes-interbancaria.html'>tasa interbancaria</a>) se mantenga cerca de su <a href='tasa-de-referencia.html'>tasa de referencia</a>.",
],
ejemplo=[
r"Antes de las fiestas de fin de año, la gente retira más efectivo y los bancos quedan con menos soles. El BCRP hace repos para inyectar liquidez y evitar que la tasa interbancaria se dispare.",
],
rel=["tasa-de-referencia", "tasa-de-interes-interbancaria", "esterilizacion", "politica-monetaria"],
))

T.append(dict(
slug="prima-de-riesgo", t="Prima de riesgo", cat="finanzas", ic="🎲",
bcrp="Prima de riesgo", alias="premio por riesgo spread rendimiento extra",
corto="Es el rendimiento adicional que exige un inversionista por aceptar una inversión más riesgosa que una segura.",
simple=[
r"Nadie arriesga su dinero gratis. Si una inversión puede salir mal, el inversionista pide ganar más que en una inversión «segura», como un bono del Tesoro de EE. UU. Esa diferencia es la <strong>prima de riesgo</strong>.",
r"Cuanto más riesgoso es el deudor, mayor es la prima. Por eso una empresa pequeña paga tasas más altas que una grande, y un país con problemas paga más que uno estable. El <a href='riesgo-pais.html'>riesgo país</a> es la prima de riesgo de un país.",
],
ejemplo=[
r"Si un bono seguro rinde 4 % y un bono de una empresa nueva rinde 9 %, la prima de riesgo de esa empresa es de 5 puntos porcentuales.",
],
formula=dict(
tex=r"r=r_f+\text{Prima de riesgo}",
donde=[(r"r", "rendimiento exigido"), (r"r_f", "rendimiento de una inversión sin riesgo")],
calculo=[r"9\ \%=4\ \%+5\ \%"],
),
rel=["riesgo-pais", "puntos-basicos", "bono", "calificacion-de-riesgo"],
))

T.append(dict(
slug="presion-tributaria", t="Presión tributaria", cat="impuestos", ic="🗜️",
bcrp="Presión tributaria", alias="carga tributaria recaudación PBI",
corto="Mide qué parte de todo lo que produce un país se recauda en impuestos. Se calcula dividiendo los ingresos tributarios entre el PBI.",
simple=[
r"La <strong>presión tributaria</strong> no dice cuánto paga cada persona, sino cuánto recauda el Estado en relación con el tamaño de la economía.",
r"Si es baja, el Estado tiene menos recursos para salud, educación o infraestructura. En el Perú suele ser baja frente a otros países de la región, en parte por la alta <a href='informalidad.html'>informalidad</a>, la evasión y las <a href='exoneracion-tributaria.html'>exoneraciones</a>.",
],
ejemplo=[
r"Con números de ejemplo: si un país recauda S/ 160 000 millones en impuestos y su PBI es S/ 1 100 000 millones, su presión tributaria es de aproximadamente 14.5 %.",
],
formula=dict(
tex=r"\text{Presión tributaria}=\frac{\text{Ingresos tributarios}}{PBI}\times 100",
calculo=[r"\frac{160\,000}{1\,100\,000}\times 100\approx 14.5\ \%"],
),
rel=["tributo", "evasion-y-elusion-tributaria", "politica-fiscal", "informalidad"],
))

T.append(dict(
slug="presupuesto-publico", t="Presupuesto público", cat="estado", ic="📑",
bcrp="Presupuesto", alias="ley de presupuesto gasto público MEF Congreso",
corto="Es el plan anual que dice cuánto dinero espera recibir el Estado y en qué lo va a gastar.",
simple=[
r"Cada año, el Poder Ejecutivo prepara el proyecto de presupuesto (con el MEF) y lo envía al Congreso, que lo debate y lo aprueba como ley. Ahí se fija cuánto recibe cada ministerio, región y municipio.",
r"La Constitución pone plazos: el proyecto debe llegar al Congreso hasta el 30 de agosto y, si la ley no se envía al Ejecutivo hasta el 30 de noviembre, entra en vigencia el proyecto. Además, el presupuesto debe estar equilibrado y no puede usar préstamos para pagar gastos permanentes.",
],
ejemplo=[
r"Cuando escuchas que «se asignó más presupuesto a educación», significa que en la ley de presupuesto de ese año el sector educación recibió más soles para sueldos, colegios o materiales.",
],
rel=["politica-fiscal", "deficit-fiscal", "resultado-primario", "deuda-publica"],
))

T.append(dict(
slug="nuevo-rus", t="Nuevo RUS", cat="impuestos", ic="🏪",
bcrp="Régimen Único Simplificado-RUS", alias="RUS NRUS régimen único simplificado bodegas pequeños negocios",
corto="Es el régimen tributario más simple del Perú, pensado para pequeños negocios: se paga una cuota fija al mes y no se llevan libros contables.",
simple=[
r"El Nuevo RUS es para bodegas, puestos de mercado, peluquerías y negocios parecidos que solo venden con <strong>boleta</strong>. En lugar de calcular varios impuestos, pagan una sola cuota mensual según su categoría.",
r"A cambio de esa simplicidad, tienen límites: no pueden emitir facturas, sus ventas o compras no deben pasar de cierto monto y deben operar en un solo local. Si el negocio crece, puede cambiarse a otro régimen.",
],
ejemplo=[
r"Según El Peruano (2023), la categoría 1 es para ingresos o compras de hasta S/ 5000 al mes y paga S/ 20; la categoría 2, hasta S/ 8000 al mes, paga S/ 50. El tope anual es S/ 96 000.",
],
ojo=["Los montos pueden cambiar. Antes de inscribirte, confirma las categorías vigentes en la SUNAT."],
rel=["tributo", "informalidad", "igv", "impuesto-a-la-renta"],
))

T.append(dict(
slug="rentabilidad", t="Rentabilidad", cat="finanzas", ic="📈",
bcrp="Rentabilidad", alias="retorno ROE ROA ganancia porcentaje",
corto="Es cuánto ganas en relación con lo que invertiste, expresado en porcentaje.",
simple=[
r"Ganar S/ 1000 puede ser mucho o poco: depende de cuánto pusiste. La <strong>rentabilidad</strong> compara la ganancia con la inversión para poder comparar opciones distintas.",
r"En las empresas se usan dos medidas comunes: la rentabilidad sobre el patrimonio (ROE), que mira lo que ganan los dueños sobre su dinero, y la rentabilidad sobre los activos (ROA), que mira lo que rinde todo lo que la empresa tiene.",
],
ejemplo=[
r"Pones S/ 5000 en un negocio de venta de ropa y, en un año, te deja S/ 900 de ganancia. Tu rentabilidad es 18 % anual, más que un depósito a plazo, pero con más riesgo.",
],
formula=dict(
tex=r"\text{Rentabilidad}=\frac{\text{Ganancia}}{\text{Inversión}}\times 100",
calculo=[r"\frac{900}{5000}\times 100=18\ \%"],
),
rel=["tir", "trea", "dividendo", "prima-de-riesgo"],
))

T.append(dict(
slug="sistema-financiero", t="Sistema financiero", cat="dinero", ic="🏦",
bcrp="Sistema financiero", alias="bancos cajas financieras cooperativas AFP seguros",
corto="Es el conjunto de instituciones y mercados que mueven el dinero de quienes ahorran hacia quienes necesitan financiamiento.",
simple=[
r"Incluye a los bancos, las financieras, las <a href='cajas-municipales.html'>cajas municipales y rurales</a>, las cooperativas, las aseguradoras, las AFP y el <a href='mercado-de-capitales.html'>mercado de valores</a>. Todos cumplen la tarea de <a href='intermediacion-financiera.html'>intermediación</a>, de distintas formas.",
r"Un sistema financiero sano permite que las familias ahorren con seguridad y que las empresas consigan crédito para crecer. Por eso está supervisado: en el Perú, la <a href='sbs.html'>SBS</a> vigila a bancos, seguros y AFP, y la SMV al mercado de valores.",
],
ejemplo=[
r"Cuando una familia de Huancayo ahorra en una caja municipal y esa caja presta a una pequeña empresa de la misma ciudad, el sistema financiero está haciendo su trabajo.",
],
rel=["intermediacion-financiera", "sbs", "cajas-municipales", "bcrp"],
))

T.append(dict(
slug="tarjetas-de-credito-y-debito", t="Tarjeta de crédito y tarjeta de débito", cat="finanzas", ic="💳",
bcrp="Tarjetas de crédito", alias="tarjeta crédito débito revolvente línea",
corto="Con la tarjeta de débito pagas con tu propio dinero. Con la de crédito pagas con dinero que te presta el banco y que luego debes devolver.",
simple=[
r"La <strong>tarjeta de débito</strong> está unida a tu cuenta: cada compra se descuenta al instante de tu saldo. No genera deuda.",
r"La <strong>tarjeta de crédito</strong> te da una línea de crédito. Si pagas el total del mes antes de la fecha límite, normalmente no pagas intereses. Si pagas solo el mínimo o compras en cuotas, el saldo genera intereses, y las tasas de las tarjetas suelen estar entre las más altas del mercado.",
],
ejemplo=[
r"Compras un televisor de S/ 2000 con tarjeta de crédito. Si pagas los S/ 2000 en la fecha de pago, no pagas intereses. Si pagas solo el mínimo, lo que queda empieza a crecer con la TEA de la tarjeta, que puede superar el 60 % anual.",
],
ojo=["Compara siempre la TCEA, que incluye intereses, comisiones y seguros, antes de elegir una tarjeta o comprar en cuotas."],
rel=["tcea", "tea", "creditos-de-consumo", "central-de-riesgos"],
))

T.append(dict(
slug="tasa-de-interes-interbancaria", t="Tasa de interés interbancaria", cat="dinero", ic="🔗",
bcrp="Tasa de interés interbancaria", alias="tasa interbancaria overnight préstamos entre bancos",
corto="Es la tasa a la que los bancos se prestan dinero entre ellos, normalmente de un día para otro.",
simple=[
r"Al final del día, algunos bancos tienen soles de sobra y otros necesitan más para cumplir su encaje. Se prestan entre ellos por plazos muy cortos, y el precio de esos préstamos es la <strong>tasa interbancaria</strong>.",
r"Es la tasa que el BCRP busca guiar con su política monetaria: usa <a href='operacion-de-mercado-abierto.html'>operaciones de mercado abierto</a> para que se mantenga cerca de la <a href='tasa-de-referencia.html'>tasa de referencia</a>. Desde ahí, los cambios pasan a las tasas de los préstamos y depósitos de las personas.",
],
ejemplo=[
r"Según Andina, en mayo de 2026 el BCRP mantuvo su tasa de referencia en 4.25 %. Con eso, la tasa interbancaria en soles se ubica alrededor de ese nivel.",
],
rel=["tasa-de-referencia", "operacion-de-mercado-abierto", "politica-monetaria", "encaje-bancario"],
))

T.append(dict(
slug="velocidad-del-dinero", t="Velocidad del dinero", cat="dinero", ic="💨",
bcrp="Velocidad de circulación del dinero", alias="velocidad de circulación teoría cuantitativa MV=PY",
corto="Indica cuántas veces, en promedio, cambia de manos un sol en un año para pagar bienes y servicios.",
simple=[
r"Un mismo billete puede usarse muchas veces: pagas en la bodega, el bodeguero paga al proveedor, el proveedor paga a su trabajador. La <strong>velocidad del dinero</strong> mide qué tan rápido circula.",
r"La <strong>ecuación cuantitativa</strong> relaciona el dinero con los precios: la cantidad de dinero por su velocidad es igual al valor de lo que se produce. Si la velocidad y la producción no cambian, imprimir más dinero termina subiendo los precios.",
],
ejemplo=[
r"Si en una economía hay S/ 200 000 millones de dinero y el PBI nominal es S/ 1 000 000 millones, cada sol se usó en promedio 5 veces en el año.",
],
formula=dict(
tex=r"M\times V=P\times Y\qquad V=\frac{P\times Y}{M}",
donde=[(r"M", "cantidad de dinero"), (r"V", "velocidad"), (r"P\times Y", "PBI nominal (precios por producción)")],
calculo=[r"V=\frac{1\,000\,000}{200\,000}=5"],
),
rel=["dinero", "inflacion", "demanda-de-dinero", "agregados-monetarios"],
))

T.append(dict(
slug="ventaja-absoluta", t="Ventaja absoluta", cat="comercio", ic="🥇",
bcrp="Ventaja absoluta", alias="Adam Smith producir con menos recursos",
corto="Un país tiene ventaja absoluta en un producto cuando puede producirlo usando menos recursos que otro país.",
simple=[
r"La idea es de Adam Smith: si un país produce algo de forma más eficiente que otro, a ambos les conviene especializarse en lo que cada uno hace mejor y comerciar.",
r"Pero no hace falta ser el mejor en algo para ganar con el comercio. David Ricardo mostró que lo importante es la <a href='ventaja-comparativa.html'>ventaja comparativa</a>: producir lo que te cuesta menos dejar de producir otra cosa.",
],
ejemplo=[
r"Con números de ejemplo: si un trabajador peruano cosecha 100 kilos de espárragos al día y uno de otro país, 60, el Perú tiene ventaja absoluta en espárragos.",
],
rel=["ventaja-comparativa", "apertura-comercial", "costo-de-oportunidad", "productividad"],
))

T.append(dict(
slug="zona-de-libre-comercio", t="Zona de libre comercio y TLC", cat="comercio", ic="🌐",
bcrp="Zona de libre comercio", alias="TLC tratado de libre comercio acuerdo comercial",
corto="Es un acuerdo entre países para eliminar o reducir los aranceles entre ellos, aunque cada uno mantiene sus propios aranceles frente al resto.",
simple=[
r"Cuando dos o más países firman un <strong>tratado de libre comercio (TLC)</strong>, crean una zona de libre comercio: sus productos pasan la frontera sin aranceles o con aranceles bajos, según un calendario.",
r"Es distinto de una unión aduanera, donde los países además ponen un mismo arancel al resto del mundo. Los TLC suelen incluir también reglas sobre servicios, inversiones y propiedad intelectual.",
],
ejemplo=[
r"El TLC entre el Perú y Estados Unidos entró en vigencia el 1 de febrero de 2009. Según Andina, en su primera década el comercio entre ambos países creció cerca de 50 %.",
],
rel=["arancel", "apertura-comercial", "ventaja-comparativa", "exportaciones-tradicionales-y-no-tradicionales"],
))

T.append(dict(
slug="sbs", t="SBS (Superintendencia de Banca, Seguros y AFP)", cat="dinero", ic="🛡️",
bcrp="Superintendencia de Banca, Seguros y AFP - SBS", alias="superintendencia supervisor bancos AFP seguros",
corto="Es la entidad que supervisa a los bancos, aseguradoras y AFP del Perú para proteger el dinero de ahorristas y afiliados.",
simple=[
r"La SBS revisa que las entidades financieras tengan suficiente capital, no asuman riesgos excesivos y traten bien a sus clientes. Si una entidad está en problemas, puede intervenirla.",
r"La Constitución le da ese papel. También administra la <a href='central-de-riesgos.html'>central de riesgos</a>, donde figura cómo paga cada persona sus deudas. No hay que confundirla con el <a href='bcrp.html'>BCRP</a>, que maneja la política monetaria, ni con la SMV, que supervisa el mercado de valores.",
],
ejemplo=[
r"Antes de ahorrar en una cooperativa o una financiera, conviene verificar en la web de la SBS si está registrada y supervisada.",
],
rel=["sistema-financiero", "central-de-riesgos", "bcrp", "afp-y-onp"],
))

T.append(dict(
slug="resultado-primario", t="Resultado primario", cat="estado", ic="➖",
bcrp="Resultado primario", alias="superávit primario déficit primario",
corto="Es el resultado de las cuentas del Estado sin contar el pago de intereses de la deuda.",
simple=[
r"El <a href='deficit-fiscal.html'>resultado fiscal</a> total compara todos los ingresos con todos los gastos. El <strong>resultado primario</strong> deja fuera los intereses de la deuda, para ver si el Estado gasta más de lo que recauda en sus operaciones de cada año.",
r"Si un país tiene superávit primario, está generando recursos para pagar intereses y reducir su deuda. Si tiene déficit primario, la deuda tiende a crecer aunque las tasas sean bajas.",
],
ejemplo=[
r"Con números de ejemplo: un Estado recauda S/ 200 000 millones, gasta S/ 205 000 millones sin contar intereses y paga S/ 10 000 millones de intereses. Su déficit primario es S/ 5000 millones y su déficit total, S/ 15 000 millones.",
],
formula=dict(
tex=r"\text{Resultado primario}=\text{Resultado total}+\text{Intereses}",
calculo=[r"-15\,000+10\,000=-5000\ \text{millones}"],
),
rel=["deficit-fiscal", "deuda-publica", "politica-fiscal", "presupuesto-publico"],
))

T.append(dict(
slug="politica-anticiclica", t="Política anticíclica", cat="estado", ic="🔃",
bcrp="Política anticíclica", alias="contracíclica estabilización estímulo",
corto="Es actuar en contra del ciclo económico: gastar o bajar tasas cuando la economía cae, y ahorrar o subir tasas cuando crece demasiado.",
simple=[
r"La economía pasa por épocas buenas y malas (el <a href='ciclo-economico.html'>ciclo económico</a>). Una política <strong>anticíclica</strong> busca suavizar esos altibajos.",
r"En la recesión, el Estado aumenta la inversión pública o el BCRP baja la <a href='tasa-de-referencia.html'>tasa de referencia</a>. En el auge, el Estado ahorra y el BCRP sube la tasa. Para poder gastar en las malas, hay que haber ahorrado en las buenas.",
],
ejemplo=[
r"En 2020, durante la pandemia, el BCRP bajó su tasa de referencia a 0.25 %, la más baja de su historia, y el gobierno lanzó bonos y préstamos garantizados para sostener la economía.",
],
rel=["ciclo-economico", "politica-fiscal", "politica-monetaria", "recesion"],
))

T.append(dict(
slug="ingreso-nacional", t="Ingreso nacional", cat="produccion", ic="🧺",
bcrp="Ingreso nacional", alias="ingreso nacional bruto INB PNB",
corto="Es lo que ganan en total los residentes de un país, estén donde estén produciendo, incluidas las rentas que reciben del exterior.",
simple=[
r"El <a href='pbi.html'>PBI</a> mide lo que se produce dentro del país, sin importar quién es el dueño. El <strong>ingreso nacional</strong> mide lo que les queda a los residentes: al PBI se le suman las rentas que llegan del exterior y se le restan las que se van.",
r"En el Perú, el ingreso nacional suele ser menor que el PBI, porque muchas empresas extranjeras (por ejemplo, mineras) envían a sus países parte de sus utilidades.",
],
ejemplo=[
r"Si el PBI es S/ 1 000 000 millones y se pagan al exterior S/ 60 000 millones netos de utilidades e intereses, el ingreso nacional bruto es S/ 940 000 millones.",
],
formula=dict(
tex=r"INB=PBI+\text{Renta neta de factores del exterior}",
calculo=[r"1\,000\,000-60\,000=940\,000"],
),
rel=["pbi", "pbi-per-capita", "cuentas-nacionales", "balanza-en-cuenta-corriente"],
))

T.append(dict(
slug="tributo", t="Tributo: impuesto, contribución y tasa", cat="impuestos", ic="🏛️",
bcrp="Tributo", alias="tributos impuesto contribución tasa arbitrio",
corto="Es un pago obligatorio al Estado. En el Perú hay tres tipos: impuestos, contribuciones y tasas.",
simple=[
r"El <strong>impuesto</strong> se paga sin recibir algo directo a cambio, como el <a href='igv.html'>IGV</a> o el <a href='impuesto-a-la-renta.html'>impuesto a la renta</a>. La <strong>contribución</strong> se paga porque te beneficias de una obra o servicio estatal, como los aportes a EsSalud. La <strong>tasa</strong> se paga por un servicio público concreto que recibes, como los arbitrios municipales o el pago por un trámite.",
r"La Constitución dice que los tributos solo pueden crearse, cambiarse o exonerarse por ley o decreto legislativo, salvo los aranceles y las tasas, que se regulan por decreto supremo. Además, ningún tributo puede ser confiscatorio.",
],
ejemplo=[
r"Una vecina de Surco paga IGV al comprar (impuesto), su empleador aporta a EsSalud por ella (contribución) y ella paga arbitrios de limpieza a su municipalidad (tasa).",
],
rel=["igv", "impuesto-a-la-renta", "impuesto-directo-e-indirecto", "uit"],
))

T.append(dict(
slug="riesgo-cambiario", t="Riesgo cambiario", cat="finanzas", ic="🎢",
bcrp="Riesgo cambiario", alias="riesgo de tipo de cambio volatilidad del dólar",
corto="Es la posibilidad de perder dinero porque cambia el tipo de cambio entre la moneda de tus ingresos y la de tus deudas o ahorros.",
simple=[
r"Si tus ingresos, deudas o ahorros están en monedas distintas, el tipo de cambio puede jugar a favor o en contra. Ese peligro es el <strong>riesgo cambiario</strong>.",
r"Lo enfrentan exportadores, importadores, viajeros y cualquier persona con deudas en dólares. Se reduce endeudándose en la misma moneda en la que se gana o usando contratos de cobertura (como los <em>forwards</em>), que fijan hoy el tipo de cambio futuro.",
],
ejemplo=[
r"Un importador peruano debe pagar US$ 10 000 en tres meses. Si el dólar sube de S/ 3.70 a S/ 3.80, pagará S/ 1000 más de lo que había calculado.",
],
formula=dict(
tex=r"\text{Pérdida}=\text{Monto en US\$}\times(TC_{\text{final}}-TC_{\text{inicial}})",
calculo=[r"10\,000\times(3.80-3.70)=1000\ \text{soles}"],
),
rel=["descalce-de-monedas", "tipo-de-cambio", "dolarizacion", "depreciacion-y-apreciacion"],
))

T.append(dict(
slug="intervencion-cambiaria", t="Intervención cambiaria", cat="dinero", ic="✋",
bcrp="Intervención cambiaria", alias="BCRP compra venta de dólares volatilidad swaps cambiarios",
corto="Es cuando el banco central compra o vende dólares, u otros instrumentos, para evitar que el tipo de cambio suba o baje de forma brusca.",
simple=[
r"Si el dólar sube muy rápido, el BCRP puede <strong>vender</strong> dólares de sus reservas o colocar instrumentos que protegen contra la subida (como los swaps cambiarios). Si baja muy rápido, puede <strong>comprar</strong> dólares.",
r"El objetivo no es fijar un precio, sino reducir la volatilidad, para que familias y empresas con deudas en dólares no sufran golpes repentinos. Cuando compra dólares, suele <a href='esterilizacion.html'>esterilizar</a> los soles que inyecta.",
],
ejemplo=[
r"Según Andina, en 2021, un año de mucha incertidumbre, el BCRP ofertó US$ 10 700 millones en el mercado para atenuar la volatilidad del dólar.",
],
rel=["regimen-cambiario", "reservas-internacionales", "esterilizacion", "tipo-de-cambio"],
))

T.append(dict(
slug="valor-agregado", t="Valor agregado", cat="produccion", ic="➕",
bcrp="Valor agregado bruto", alias="valor añadido VAB producción insumos",
corto="Es lo que una empresa o sector añade al valor de los insumos que compra. Sumando el valor agregado de todos, se obtiene el PBI.",
simple=[
r"Una panadería compra harina, azúcar y gas por S/ 600 y vende panes por S/ 1000. No creó S/ 1000 de valor: creó S/ 400, que es su <strong>valor agregado</strong>. Lo demás ya lo habían producido otros.",
r"Medir así evita contar dos veces lo mismo. Por eso el <a href='pbi.html'>PBI</a> se calcula sumando el valor agregado de todos los sectores (más los impuestos a los productos), y no sumando todas las ventas.",
],
ejemplo=[
r"El cobre que sale de una mina y luego se convierte en cables en una fábrica peruana genera valor agregado dos veces: en la minería y en la manufactura.",
],
formula=dict(
tex=r"VA=\text{Valor de producción}-\text{Consumo intermedio}",
calculo=[r"1000-600=400\ \text{soles}"],
),
rel=["pbi", "cuentas-nacionales", "credito-fiscal", "productividad"],
))
