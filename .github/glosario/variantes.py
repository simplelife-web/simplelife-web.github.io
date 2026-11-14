# -*- coding: utf-8 -*-
# Términos del Glosario del BCRP que son variantes o detalles de un término
# que ya tiene página. Se muestran dentro de esa página, en la sección
# «Otros términos del glosario del BCRP», con su cita y en el buscador.
# Formato: "slug-de-la-pagina": [("Título exacto en el BCRP", r"explicación propia"), ...]
# Todo redactado con palabras propias; nunca copiar el texto del BCRP.

VARIANTES = {}


def _v(slug, *pares):
    VARIANTES.setdefault(slug, []).extend(pares)


# --- Bloque 1 (A a E) -----------------------------------------------------
_v("titulizacion",
   ("ABS", r"Siglas en inglés de «valores respaldados por activos»: bonos que se pagan con el flujo de un paquete de préstamos u otros activos agrupados en un fondo. Es el producto típico de la titulización."))
_v("reservas-internacionales",
   ("Activos de reserva del BCRP", r"Son los activos en el exterior que el BCRP controla y puede usar de inmediato, como divisas, depósitos en bancos extranjeros de primer nivel, valores de corto plazo y oro. También se les llama reservas internacionales brutas."),
   ("Cuenta de valuación", r"Es la cuenta del BCRP donde se anotan las ganancias o pérdidas contables que aparecen solo porque cambia el valor en soles de sus activos en oro o en moneda extranjera."))
_v("balanza-de-pagos",
   ("Activos externos", r"Todo lo que los residentes de un país tienen frente al exterior: divisas, depósitos, bonos, préstamos y otros activos emitidos por no residentes."),
   ("Activos externos a corto plazo", r"Activos frente al exterior que pueden convertirse en efectivo en menos de un año, como depósitos en bancos extranjeros o valores de corto plazo."),
   ("Activos externos a largo plazo", r"Activos frente al exterior con plazo mayor a un año, como bonos, acciones o préstamos de largo plazo, que son menos líquidos."),
   ("Balanza de capital a largo plazo", r"Parte de la balanza de pagos que registra las operaciones financieras con el exterior a más de un año, como préstamos de largo plazo e inversión; muestra cómo se endeuda o invierte el país a largo plazo."),
   ("Capitales de corto plazo", r"Rubro de la balanza de pagos que recoge los movimientos de activos y pasivos a menos de un año de bancos, empresas y familias con el exterior (sin contar al BCRP)."),
   ("Cuenta de capital", r"Pequeña parte de la balanza de pagos que registra transferencias de capital, como condonaciones de deuda, y la compra o venta de activos no producidos, como marcas o derechos."),
   ("Déficit de la balanza de pagos", r"Ocurre cuando salen del país más divisas de las que entran en un periodo; se refleja en una caída de las reservas internacionales."))
_v("cuenta-financiera",
   ("Balanza en cuenta financiera", r"Otro nombre de la cuenta financiera: registra los cambios en los activos y pasivos financieros del país con el exterior, tanto de corto como de largo plazo."))
_v("activos-ponderados-por-riesgo",
   ("Activos y contingentes ponderados por riesgo", r"Es la suma de los activos y créditos indirectos ponderados por su riesgo de crédito, más el capital que se exige por riesgo de mercado y por riesgo operacional. Es la base para calcular el capital mínimo de un banco."))
_v("sistema-de-pagos",
   ("Acuerdo de liquidación de valores", r"Reglas y procedimientos que siguen al menos tres entidades para confirmar, compensar y liquidar compras y ventas de valores."),
   ("Compensación o neteo", r"Es restar lo que cada participante debe de lo que le deben, para que solo se pague la diferencia neta y no cada operación por separado."),
   ("Débitos Directos", r"Cargos a tu cuenta que tú autorizaste antes y que inicia quien te cobra, como el pago automático de un servicio."))
_v("cavali",
   ("Custodia", r"Servicio de guardar títulos y valores de los clientes para protegerlos de pérdidas o robos, a cambio de una comisión."),
   ("Custodio", r"Entidad, normalmente un banco, que guarda y administra valores para sus clientes, y que puede ofrecer servicios como la liquidación de operaciones o el cobro de intereses."))
_v("circulante",
   ("Bóveda de custodia", r"Espacio protegido dentro de la bóveda de un banco o de una empresa de transporte de valores donde se guardan billetes y monedas bajo reglas del BCRP."),
   ("Circulante", r"Tiene dos usos: en contabilidad, los activos o pasivos de corto plazo (menos de un año); en economía monetaria, los billetes y monedas que están en manos del público."))
_v("repo",
   ("Acuerdo reverso de recompra", r"Es la operación inversa al repo: se vende un título con el compromiso de recomprarlo después. Para un banco central, sirve para retirar liquidez en lugar de inyectarla."),
   ("Compra temporal de títulos valores", r"Operación en la que se compra un título hoy con el compromiso de venderlo de vuelta en una fecha fija, ganando un rendimiento por ese plazo; en la práctica es un préstamo con garantía."),
   ("Compras repo", r"Compras de títulos que hace el BCRP con pacto de recompra: entrega soles a los bancos por un plazo y luego les devuelve los títulos. Así inyecta liquidez de forma temporal."))
_v("filial-y-sucursal",
   ("Agencia", r"Oficina de representación de un banco en otro país, que depende legalmente de su casa matriz. También se usa para entidades públicas con funciones especializadas."),
   ("Casa matriz", r"Empresa que encabeza un grupo y lo controla porque tiene la mayoría de su propiedad."),
   ("Empresa matriz", r"En la balanza de pagos, es la empresa extranjera que tiene inversiones en empresas del país."))
_v("calificacion-de-riesgo",
   ("Agencias Calificadoras de Riesgo", r"Empresas como Standard & Poor's, Moody's o Fitch que evalúan la capacidad y la voluntad de pago de quien emite deuda, y la clasifican en grado de inversión o especulativo."),
   ("Clasificación de largo plazo", r"Escala de letras que usan las calificadoras para la deuda de largo plazo: desde AAA, la más segura, hasta las categorías de impago."))
_v("ahorro",
   ("Ahorro interno", r"Parte del ingreso de los residentes del país (familias, empresas y Estado) que no se consume."))
_v("brecha-ahorro-inversion",
   ("Ahorro externo", r"Es el ahorro de otros países que financia la inversión local cuando el ahorro interno no alcanza. Equivale al déficit en cuenta corriente."))
_v("gasto-corriente-y-de-capital",
   ("Ahorro en cuenta corriente", r"En las cuentas del Estado, es lo que sobra de los ingresos corrientes después de pagar los gastos corrientes; muestra si el Estado cubre su funcionamiento diario sin endeudarse."))
_v("contrato-forward",
   ("Al contado", r"Pago en efectivo en el momento de la operación; en mercados financieros, una operación «spot» que se liquida casi de inmediato."),
   ("Compras forward", r"Contratos para comprar algo, por ejemplo dólares, en una fecha futura a un precio fijado hoy."),
   ("Compras spot", r"Compras que se pagan y entregan casi de inmediato, en uno o dos días hábiles, al precio de ese momento."))
_v("salvaguardia-y-antidumping",
   ("Antidumping", r"Medidas, normalmente aranceles extra, que un país aplica a importaciones vendidas por debajo de su precio normal (dumping) para proteger a su industria."))
_v("cono-monetario",
   ("Anverso", r"Cara principal de un billete o moneda. En los billetes peruanos es el lado del personaje principal; en las monedas, el lado del Escudo Nacional. El otro lado es el reverso."),
   ("Billete", r"Documento de papel o polímero con elementos de seguridad, emitido por el BCRP, que representa una cantidad de soles y sirve para pagar."),
   ("Cospel", r"Disco de metal liso que todavía no ha sido acuñado; al recibir el grabado se convierte en moneda."),
   ("Cospel Bimetálico o Bicolor", r"Cospel hecho con dos metales de distinto color, un aro exterior y un centro, como el de las monedas de S/ 2 y S/ 5."))
_v("apalancamiento",
   ("Apalancamiento global", r"Uso de dinero prestado para financiar inversiones o negocios; puede aumentar la ganancia, pero también el riesgo."),
   ("Coeficiente de apalancamiento financiero", r"Indicador que compara las deudas o los activos de una entidad con su patrimonio. La SBS lo usa para limitar cuánto pueden endeudarse los bancos frente a su capital."))
_v("depreciacion-y-apreciacion",
   ("Apreciación", r"Aumento del valor de un bien o de un título; en el caso de una moneda, que compre más unidades de otra moneda."))
_v("reporte-de-inflacion",
   ("Balance de riesgos", r"Parte de las proyecciones del BCRP que evalúa qué escenarios podrían hacer que la inflación o el crecimiento se desvíen hacia arriba o hacia abajo del escenario base."))
_v("banca-electronica",
   ("Banca virtual", r"Canales para hacer operaciones bancarias sin ir a una ventanilla ni a un cajero: internet, aplicación del celular o banca telefónica."))
_v("sistema-financiero",
   ("Banco", r"Empresa que recibe dinero del público en depósitos y lo usa, junto con su capital, para dar préstamos y prestar otros servicios financieros."),
   ("Empresa bancaria", r"Nombre legal de los bancos en el Perú: su negocio principal es captar depósitos y prestar ese dinero."))
_v("arrendamiento-financiero",
   ("Empresa de arrendamiento financiero", r"Entidad especializada en comprar bienes, como máquinas o inmuebles, para dárselos en uso a una empresa a cambio de cuotas, con opción de compra al final."),
   ("Bonos de arrendamiento financiero", r"Bonos que emiten las entidades financieras para conseguir dinero con el que financiar operaciones de leasing."))
_v("banco-de-inversion",
   ("Empresa de inversión", r"Empresa que consigue financiamiento de largo plazo para sus clientes, por ejemplo organizando y colocando emisiones de bonos o acciones."))
_v("compania-de-seguros",
   ("Empresa de seguros", r"Empresa que, a cambio de una prima, se compromete a pagar una indemnización, un capital o una renta si ocurre el evento asegurado."),
   ("Empresa de reaseguros", r"Aseguradora de las aseguradoras: asume parte de los riesgos de una compañía de seguros cuando los montos son muy grandes."))
_v("barreras-al-comercio",
   ("Barreras fiscales", r"Obstáculos al comercio que vienen de los impuestos, como aranceles o impuestos internos que encarecen los productos importados."))
_v("base-monetaria",
   ("Base monetaria", r"Es lo mismo que la emisión primaria: el dinero creado directamente por el BCRP, es decir, billetes y monedas en circulación más los fondos que los bancos tienen en el BCRP."))
_v("cheque",
   ("Cuenta corriente", r"Cuenta bancaria de la que puedes disponer en cualquier momento, normalmente girando cheques o con transferencias; suele pagar poco o ningún interés."),
   ("Depósito a la vista", r"Depósito que puedes retirar en cualquier momento, sin plazo ni aviso, por ejemplo girando un cheque."),
   ("Depósito en cuenta corriente", r"Dinero depositado en una cuenta corriente, del que se puede disponer con cheques u otras órdenes de pago."))
_v("deficit-fiscal",
   ("Déficit", r"Situación en la que los gastos superan a los ingresos en un periodo. Si es del Estado, se cubre con deuda o usando ahorros."),
   ("Brecha fiscal", r"Diferencia entre lo que gasta y lo que recauda el Estado; si los gastos son mayores, hay que financiarla."))
_v("balanza-comercial",
   ("Déficit comercial", r"Ocurre cuando un país importa más bienes de los que exporta en un periodo."))
_v("demanda-agregada",
   ("Demanda global", r"Otro nombre de la demanda agregada: el gasto total en bienes y servicios de la economía."),
   ("Demanda externa", r"La parte de la demanda que viene del exterior, es decir, lo que el resto del mundo compra a un país: sus exportaciones."))
_v("intermediacion-financiera",
   ("Depósitos", r"Dinero que familias y empresas entregan a las entidades financieras autorizadas, que se comprometen a devolverlo según lo pactado."))
_v("mercado-de-dinero",
   ("Dinero a la vista", r"Préstamo, normalmente entre bancos, que debe devolverse en cuanto el prestamista lo pide."))
_v("empleo-formal-e-informal",
   ("Empleo informal", r"Trabajo sin contrato, sin seguro de salud y sin aportes a un sistema de pensiones; incluye también a muchos independientes y trabajadores familiares no remunerados."))
_v("pea",
   ("Empleo", r"Situación de las personas en edad de trabajar que tienen alguna ocupación, sea asalariada o independiente; muestra cuánto se usa la fuerza laboral."))
_v("costo-de-transaccion",
   ("Empresa", r"Organización que combina capital y trabajo para producir bienes o servicios y venderlos, buscando una ganancia."))
_v("bienes-de-capital-y-de-consumo",
   ("Bienes de consumo", r"Bienes y servicios que se compran para usarlos directamente, no para producir otros bienes."),
   ("Bienes de consumo duradero", r"Bienes de consumo que se usan durante mucho tiempo, como un refrigerador o un auto."),
   ("Bienes de consumo no duradero", r"Bienes de consumo que se gastan rápido, como los alimentos o los artículos de limpieza."))
_v("bienes-transables-y-no-transables",
   ("Bienes no transables", r"Bienes y servicios que no se pueden comerciar con otros países, como un corte de pelo o un alquiler; su precio depende sobre todo de la oferta y la demanda locales."))
_v("presupuesto-publico",
   ("Bienes y servicios", r"En las cuentas del Estado, es el gasto en compras que no aumentan su patrimonio, como útiles, combustible o servicios contratados sin relación laboral."),
   ("Ejecución del gasto", r"Las etapas por las que pasa el gasto público: compromiso (se reserva el dinero), devengado (se reconoce la obligación) y pago."),
   ("Ejecución presupuestaria", r"Registro de cuánto se recaudó y cuánto se gastó realmente del presupuesto aprobado en un periodo."),
   ("Caja del Tesoro Público", r"Indicador de la posición de efectivo del Tesoro: sus entradas y salidas de dinero en soles y en dólares."),
   ("Dirección Nacional del Tesoro Público", r"Órgano del Ministerio de Economía y Finanzas que centraliza los fondos públicos y programa y autoriza los pagos del Estado. Hoy sus funciones las cumple la Dirección General del Tesoro Público."),
   ("Donación", r"Ingreso que el Estado recibe sin tener que devolverlo ni dar nada a cambio, por ejemplo de otros gobiernos o de organismos internacionales."),
   ("Donación de capital", r"Donación destinada a comprar o reponer activos de capital, como infraestructura dañada por un desastre."))
_v("deuda-publica",
   ("Crédito público", r"Financiamiento que obtienen las entidades del Estado, como ministerios, gobiernos regionales o municipios."),
   ("Bonos por canje de deuda pública", r"Bonos que el Estado entrega a cambio de otros bonos o deudas suyas, para cambiar plazos o condiciones."))
_v("liquidez",
   ("Caja", r"En sentido amplio, el dinero disponible; en contabilidad, la cuenta donde se registra el efectivo que se puede usar de inmediato."))
_v("camara-de-compensacion",
   ("Canje", r"Cheques de otros bancos que una entidad recibió y todavía no ha presentado a la cámara de compensación."),
   ("Canje de cheques", r"Proceso por el que los bancos se intercambian los cheques que recibieron para cobrarlos entre ellos."))
_v("capital",
   ("Capital fijo", r"Parte del capital de una empresa invertida en bienes que se quedan por largo tiempo, como máquinas, edificios o patentes."))
_v("presion-tributaria",
   ("Carga fiscal", r"Cuánto pesan todos los impuestos sobre el ingreso de una persona, de una operación o de un sector."))
_v("cartera-pesada",
   ("Cartera normal", r"Créditos de deudores que pagan puntualmente y tienen una situación financiera sana."),
   ("Cartera deficiente", r"Créditos de deudores con problemas: su flujo de caja no les alcanza para pagar todo el capital y los intereses a tiempo."),
   ("Cartera dudosa", r"Créditos de deudores con un flujo de caja claramente insuficiente y una situación crítica, con alta probabilidad de no pagar."))
_v("cartera-morosa",
   ("Cartera Morosa Neta", r"Créditos vencidos, en cobranza judicial, refinanciados y reestructurados, después de restar las provisiones que ya hizo la entidad."),
   ("Cartera vencida", r"Créditos que no se pagaron en la fecha de vencimiento."))
_v("colocaciones",
   ("Colocaciones Brutas", r"Todos los créditos de una entidad, sumando los que están al día y los que están en mora."),
   ("Crédito", r"Operación en la que alguien entrega dinero o bienes ahora a cambio de la promesa de recibir el pago después, normalmente con intereses."),
   ("Crédito al sector privado", r"Préstamos e inversiones del sistema financiero en empresas privadas, familias e instituciones sin fines de lucro."),
   ("Crédito interno neto", r"Total del crédito que el sistema financiero da a residentes del país, sumando el crédito al sector privado y al sector público (en términos netos)."))
_v("credito-refinanciado",
   ("Cartera Refinanciada", r"Créditos a los que se les cambió el plazo o el monto porque el deudor tenía problemas para pagar."),
   ("Crédito reestructurado", r"Créditos cuyos pagos se reprogramaron dentro de un proceso formal de reestructuración del deudor."))
_v("portafolio",
   ("Cartera de valores", r"Conjunto de inversiones en acciones, bonos y otros activos financieros que tiene una persona o una empresa."))
_v("riesgo-de-mercado",
   ("Cartera negociable", r"Inversiones de un banco expuestas a cambios en los precios de mercado, como bonos, acciones, posiciones en moneda extranjera o materias primas."))
_v("choques-de-oferta-y-demanda",
   ("Choques de demanda", r"Cambios inesperados en la demanda agregada; si son positivos, aumentan la actividad y la inflación al mismo tiempo."),
   ("Choques de política monetaria", r"Cambios inesperados en la tasa de interés del banco central; funcionan como un choque de demanda."),
   ("Choques de tipo de cambio", r"Movimientos inesperados del tipo de cambio que no se deben a la política monetaria."))
_v("dolarizacion",
   ("Coeficiente de dolarización", r"Porcentaje de los depósitos o de los créditos que está en moneda extranjera."),
   ("Dolarización financiera", r"Cuando la gente prefiere ahorrar o endeudarse en dólares, por riesgo o por rentabilidad, aunque use soles para sus compras diarias."))
_v("preferencia-por-circulante",
   ("Coeficiente de preferencia por circulante", r"Otro nombre de la tasa de preferencia por circulante: el efectivo en manos del público dividido entre sus depósitos."))
_v("encaje-bancario",
   ("Coeficiente de reservas", r"Proporción de los depósitos que los bancos mantienen como reservas, en caja o en el BCRP."),
   ("Encaje adicional", r"Parte del encaje exigido que supera el mínimo legal."),
   ("Déficit de encaje", r"Ocurre cuando un banco tiene menos encaje del que se le exige; el BCRP le cobra una multa."),
   ("Depósitos en el BCRP", r"Fondos que las entidades financieras dejan en el BCRP, sobre todo para cumplir con el encaje; el BCRP también ofrece depósitos a plazo como herramienta monetaria."))
_v("deposito-overnight",
   ("Depósitos call", r"Depósitos de muy corto plazo que los bancos dejan en el banco central a una tasa fijada por este; ayudan a controlar la cantidad de dinero."))
_v("ratio-de-capital-global",
   ("Coeficiente de solvencia o margen de solvencia", r"Indicador que compara el patrimonio de una empresa con sus deudas o riesgos, para ver si puede responder ante sus acreedores."))
_v("banco-mundial",
   ("Comité de Desarrollo", r"Grupo de ministros que asesora a las juntas de gobernadores del Banco Mundial y del FMI en temas de financiamiento del desarrollo."))
_v("organismos-multilaterales",
   ("Compra-recompra", r"Términos del FMI: «compra» es cuando un país recibe un desembolso de un acuerdo con el FMI y «recompra» cuando lo devuelve."))
_v("intervencion-cambiaria",
   ("Compras netas en mesa de negociación", r"Dólares que el BCRP compra menos los que vende directamente en el mercado cambiario; si el resultado es negativo, vendió más de lo que compró."))
_v("mercado-de-capitales",
   ("Conasev - Comisión Nacional Supervisora de Empresas y Valores", r"Era la entidad que supervisaba el mercado de valores peruano. Desde 2011 se llama Superintendencia del Mercado de Valores (SMV)."),
   ("Empresas proveedoras de precios", r"Empresas autorizadas que calculan precios y tasas de valorización para bonos y otros instrumentos, que usan fondos e inversionistas para valorizar sus carteras."))
_v("consumo-privado-y-publico",
   ("Consumo final", r"Todo el gasto en consumo de la economía: el de las familias, las instituciones sin fines de lucro y el Estado."),
   ("Consumo público", r"El gasto del Estado en bienes y servicios para su funcionamiento."))
_v("backwardation-y-contango",
   ("Contango", r"Situación en la que los contratos de entrega más lejana cotizan más caro que los de entrega más cercana; es lo contrario del backwardation."))
_v("linea-de-credito",
   ("Contingente", r"Créditos «fuera de balance»: garantías, líneas aprobadas no usadas o préstamos aprobados todavía no desembolsados, que podrían convertirse en préstamos."))
_v("credito-documentario",
   ("Crédito contingente", r"Compromiso de un banco de pagar a un beneficiario si su cliente no cumple; es una garantía, como una carta fianza."))
_v("tributo",
   ("Contribución", r"Tributo que se paga porque una obra o actividad del Estado te beneficia directamente, como las aportaciones a EsSalud."),
   ("Devolución de impuestos", r"Cuando la administración tributaria devuelve impuestos pagados de más, por error, o por regímenes especiales como el de exportadores."))
_v("swaps",
   ("Crédito swap", r"Operación en la que una parte deja un depósito en un banco extranjero mientras ese banco presta otra moneda a un tercero; el depósito funciona como garantía."))
_v("agregados-monetarios",
   ("Cuentas monetarias", r"Registros de los activos y pasivos de las entidades financieras, presentados para mostrar cómo crean dinero y crédito."),
   ("Cuentas monetarias del BCRP", r"Resumen de las operaciones del BCRP: reservas internacionales netas, emisión de dinero, depósitos y otras cuentas."))
_v("divisa",
   ("Depósitos de eurodivisas", r"Depósitos en una moneda que se mantienen fuera del país que la emite, por ejemplo dólares depositados en un banco de Londres."))
_v("oferta-y-demanda",
   ("Desequilibrio", r"Situación en la que la oferta y la demanda no coinciden y el precio todavía no se ha ajustado."))
_v("indicador-adelantado",
   ("Despachos locales de cemento", r"Ventas de cemento en el país; como casi todo se usa en construcción, sirven para seguir de cerca la actividad de ese sector."))
_v("creacion-y-desviacion-de-comercio",
   ("Desviación del comercio", r"Cuando un acuerdo comercial hace que se importe de un socio menos eficiente en lugar de un proveedor más barato de fuera del bloque, solo por la diferencia de aranceles."))
_v("duracion",
   ("Duración vectorial", r"Mide cómo cambia el valor de una cartera de bonos si sube 1 punto porcentual la tasa de un plazo específico, en lugar de toda la curva."))
_v("evasion-y-elusion-tributaria",
   ("Elusión tributaria", r"Reducir los impuestos aprovechando vacíos o ambigüedades de la ley, sin violarla directamente; a diferencia de la evasión, no es delito, aunque las normas antielusivas buscan limitarla."))
_v("bono",
   ("Bono del Tesoro", r"Título de deuda de mediano o largo plazo que emite el gobierno para financiarse."),
   ("Bono de interés flotante", r"Bono cuyo interés cambia con una tasa de referencia del mercado más un margen fijo."),
   ("Bonos de apoyo al sistema financiero", r"Bonos de bancos en los que el Estado era el accionista mayoritario, adquiridos por el Banco de la Nación para apoyarlos."))
_v("credito-hipotecario",
   ("Bonos hipotecarios", r"Bonos respaldados por hipotecas sobre inmuebles."),
   ("Bonos hipotecarios cubiertos", r"Bonos que emiten los bancos respaldados por una cartera de créditos hipotecarios, que queda separada como garantía para los bonistas."))
_v("bonos-vac",
   ("Bonos indexados", r"Bonos cuyos pagos se ajustan según un índice, normalmente la inflación, para proteger el poder adquisitivo del inversionista."))
_v("bono-soberano",
   ("Bonos Soberanos de Tesoro Público", r"Nombre oficial de los bonos que emite la República del Perú en el mercado local; se registran en CAVALI y se pueden negociar libremente."))
_v("bono-cupon-cero",
   ("Cupón cero, títulos", r"Títulos que no pagan intereses periódicos: se compran por debajo de su valor nominal y la ganancia es la diferencia al vencimiento."))
_v("valor-a-la-par",
   ("Emisión bajo la par", r"Venta de títulos a un precio menor que su valor nominal."),
   ("Emisión sobre la par", r"Venta de títulos a un precio mayor que su valor nominal; en acciones, esa diferencia se llama prima de emisión."))


# --- Bloque 2 (E a M) -----------------------------------------------------
_v("encaje-bancario",
   ("Encaje legal", r"Es el encaje mínimo obligatorio: un porcentaje fijo de los depósitos que todos los bancos deben guardar."),
   ("Encaje marginal", r"Encaje adicional que el BCRP puede exigir sobre los depósitos que crecen por encima de un nivel base, normalmente para frenar un crecimiento muy rápido del crédito."),
   ("Encaje exigible", r"El total de encaje que un banco está obligado a tener en un periodo, sumando el encaje legal y el marginal."),
   ("Encaje efectivo", r"El encaje que el banco realmente tiene: el efectivo en sus bóvedas más sus depósitos en el BCRP."),
   ("Excedente de encaje", r"Lo que el encaje efectivo supera al exigido; también se le llama sobreencaje."),
   ("Fondos de encaje", r"Recursos con los que un banco cumple su encaje: efectivo en caja y depósitos en el BCRP."))
_v("liquidez",
   ("Fondos disponibles en bancos", r"Los recursos más líquidos de un banco o una empresa: efectivo en caja y depósitos que se pueden usar de inmediato."))
_v("deuda-externa",
   ("Endeudamiento externo neto", r"Lo que realmente aumenta la deuda con el exterior en un periodo: los nuevos préstamos recibidos menos lo que se pagó del capital."),
   ("Financiamiento externo", r"Préstamos que el sector público obtiene de acreedores del exterior, menos lo que amortiza a esos acreedores."),
   ("Financiamiento externo neto", r"Flujo neto de endeudamiento con el exterior en un periodo, sin contar los cambios por tipo de cambio o precios."))
_v("balanza-de-pagos",
   ("Financiamiento excepcional", r"Mecanismos distintos a usar reservas o créditos del FMI para cubrir problemas de balanza de pagos, como reprogramar deudas o acumular atrasos."),
   ("Equilibrio de la balanza de pagos", r"No se refiere a que la balanza sume cero (eso siempre ocurre en la contabilidad), sino a que las operaciones normales con el exterior se financien sin tener que usar reservas ni recursos excepcionales."),
   ("Flujos financieros externos", r"Todos los movimientos de activos y pasivos financieros con el exterior en un periodo, registrados en términos netos."))
_v("oferta-y-demanda",
   ("Equilibrio económico", r"Situación de estabilidad en la que las fuerzas de un mercado o de la economía se compensan; en un mercado, cuando la oferta iguala a la demanda."))
_v("tasa-impositiva-marginal",
   ("Escala imponible", r"Los tramos de la base de un impuesto, cada uno con una tasa distinta. Puede ser progresiva (la tasa sube con el monto), proporcional o regresiva."))
_v("meta-de-inflacion",
   ("Esquema de política monetaria", r"El marco que define qué busca el banco central, qué meta usa, qué instrumento mueve y cómo comunica sus decisiones. El del BCRP es el de metas explícitas de inflación."),
   ("Inflación objetivo", r"Otro nombre del esquema de metas explícitas de inflación."))
_v("politica-anticiclica",
   ("Estabilización", r"Políticas que buscan reducir los altibajos de la economía, como la inflación alta o las caídas de la producción, con medidas fiscales, monetarias o de crédito."))
_v("impulso-fiscal",
   ("Medidas fiscales", r"Acciones del gobierno sobre el gasto o los impuestos para reactivar la economía en una recesión o enfriarla si se recalienta."))
_v("servicio-de-deuda",
   ("Estructura del servicio de la deuda", r"Cómo se reparten en el tiempo los pagos de intereses y capital de una deuda, por plazo o por tipo de acreedor; muestra si hay años con pagos muy concentrados."))
_v("exoneracion-tributaria",
   ("Exención", r"Liberación de la obligación de pagar un tributo; en la práctica se usa casi como sinónimo de exoneración."),
   ("Incentivo tributario", r"Exoneraciones, rebajas o facilidades tributarias que el Estado da para promover una actividad o una región."))
_v("exportaciones-tradicionales-y-no-tradicionales",
   ("Exportaciones no tradicionales", r"Exportaciones con más transformación o valor agregado, como agroexportaciones, textiles o químicos, que históricamente se vendían poco al exterior."))
_v("sistema-de-pagos",
   ("Fecha valor", r"El día desde el cual un movimiento en una cuenta empieza a contar para calcular intereses, que puede ser distinto del día de la operación."),
   ("Liquidación", r"Momento en que una deuda entre participantes de un sistema de pagos se cumple de forma definitiva, al moverse el dinero o los valores."),
   ("Instrumento de pago", r"Medio que sirve para pagar o para pedir un pago, como una transferencia, un cheque, una tarjeta o un débito directo."))
_v("sistema-lbtr",
   ("Fondos propios", r"En el sistema LBTR, el dinero libre que cada participante tiene en su cuenta del BCRP y que puede usar para sus transferencias."))
_v("camara-de-compensacion",
   ("Instrumento compensable", r"Cheques, órdenes de pago y otros documentos que, según las reglas del BCRP, pasan por el proceso de canje y compensación entre bancos."))
_v("deficit-fiscal",
   ("Financiamiento interno", r"Cómo se financia el Estado con residentes del país: préstamos y bonos locales, o usando sus propios depósitos."),
   ("Financiamiento neto", r"Préstamos recibidos menos lo amortizado en un periodo; en las cuentas fiscales incluye también los ingresos por privatizaciones."),
   ("Financiamiento interno neto", r"Préstamos recibidos de residentes menos lo amortizado a ellos en un periodo."))
_v("balanza-de-servicios",
   ("Flete", r"En la balanza de pagos, lo que se cobra o se paga por el transporte internacional de carga."))
_v("regimen-cambiario",
   ("Flotación cambiaria", r"Régimen en el que el tipo de cambio lo fijan la oferta y la demanda. Es «limpia» si el banco central no interviene y «sucia» o administrada si interviene para suavizarlo."),
   ("Límites de la banda cambiaria", r"En un sistema de bandas, el tipo de cambio mínimo y máximo dentro de los cuales se permite que se mueva la moneda; si llega a un límite, el banco central interviene."))
_v("cheque",
   ("Flotante – Perú", r"Diferencia entre el saldo que figura en el banco y el que registra la empresa en sus libros, por cheques o depósitos que todavía no se han procesado."))
_v("volatilidad",
   ("Fluctuación", r"Subidas y bajadas de un precio o de una variable a lo largo del tiempo."))
_v("cuentas-nacionales",
   ("Flujos macroeconómicos", r"Las grandes relaciones entre los agregados de la economía, como ahorro e inversión, el saldo fiscal y el saldo con el exterior."))
_v("ingreso-nacional",
   ("Ingreso nacional bruto - INB", r"El PBI más las rentas que los residentes reciben del exterior y menos las que pagan al exterior. Es parecido al antiguo producto nacional bruto (PNB)."),
   ("Ingreso nacional neto", r"El ingreso nacional bruto menos el desgaste del capital (consumo de capital fijo)."))
_v("renta-de-factores",
   ("Ingresos primarios", r"Ingresos que se obtienen por participar en la producción (sueldos) o por ser dueño de activos (intereses, dividendos, alquileres)."))
_v("fondo-mutuo",
   ("Fondo común de inversión", r"Fondo que junta el dinero de muchos inversionistas y emite o recompra cuotas de forma continua; es otro nombre para los fondos mutuos abiertos."))
_v("organismos-multilaterales",
   ("Fondo fiduciario", r"Fondo del FMI, formado con ganancias de la venta de oro, que se usó para financiar créditos en condiciones blandas a países pobres."),
   ("Línea de Crédito Contingente del FMI", r"Línea preventiva que el FMI creó en 1999 para apoyar a países con buenas políticas ante el contagio de crisis ajenas; luego fue reemplazada por otros instrumentos."))
_v("presupuesto-publico",
   ("Fondo revolvente", r"Fondo que se repone con lo que generan las actividades que financia, de modo que puede volver a usarse una y otra vez."),
   ("Fondos", r"Recursos reunidos para un fin; en contabilidad, también las partidas que se separan para gastos especiales."),
   ("Marco presupuestal", r"El presupuesto aprobado por ley más todas sus modificaciones durante el año."),
   ("Hacienda pública", r"Conjunto de bienes, derechos e ingresos del Estado, y la actividad de administrarlos para cumplir sus funciones."))
_v("devengado",
   ("Gasto devengado", r"En el presupuesto público, el gasto que ya es una obligación de pago porque el bien o servicio se recibió, aunque todavía no se haya pagado."),
   ("Ingresos devengados", r"Ingresos que corresponden a un periodo porque se generaron en él, se hayan cobrado o no."))
_v("fideicomiso",
   ("Fondos en fideicomiso", r"Dinero que recibe una entidad financiera para administrarlo con un fin específico; no le pertenece ni forma parte de sus activos."))
_v("tasa-de-interes-interbancaria",
   ("Fondos interbancarios", r"Préstamos entre entidades del sistema financiero a plazos muy cortos, de hasta 90 días."))
_v("formacion-bruta-de-capital",
   ("Formación bruta de capital fijo", r"Compras de activos fijos, como maquinaria, equipos y construcciones, que se usarán por más de un año en la producción."),
   ("Inversión bruta", r"Toda la inversión del periodo, incluida la que solo repone el capital gastado y la variación de inventarios."),
   ("Inversión bruta fija", r"Inversión en capital físico, incluida la de reposición, sin contar inventarios."),
   ("Inversión bruta interna", r"Formación bruta de capital fijo más la variación de existencias."))
_v("inversion",
   ("Inversión bruta fija privada", r"La inversión en capital físico de las empresas y familias. En el Perú se obtiene restando la inversión pública de la inversión total."),
   ("Inversión del sector privado", r"Gasto de las empresas y familias en bienes duraderos para producir, como máquinas, plantas o viviendas."),
   ("Inversión neta", r"La inversión que aumenta el capital después de descontar el desgaste del capital existente."),
   ("Inversión financiera", r"Compra de activos financieros, como acciones o bonos, a diferencia de la inversión en capital físico."))
_v("inversion-publica",
   ("Inversión bruta fija pública", r"La inversión en capital físico del gobierno y de las empresas del Estado."),
   ("Inversión del sector público", r"Gasto del Estado para crear, ampliar o mejorar infraestructura y otros activos públicos, como carreteras, escuelas o hospitales."))
_v("contrato-forward",
   ("Forwards en moneda extranjera", r"Acuerdos para comprar o vender una cantidad de divisas en una fecha futura a un tipo de cambio fijado hoy; sirven para protegerse de variaciones del dólar."))
_v("utilidades-retenidas",
   ("Ganancias no distribuidas", r"Utilidades que la empresa guarda en lugar de repartir. En la balanza de pagos, las de empresas con inversión extranjera se registran como reinversión."))
_v("gasto-corriente-y-de-capital",
   ("Gasto", r"Salida de dinero a cambio de un bien o un servicio."),
   ("Gastos de capital", r"Gastos en bienes que duran más de un año, como obras o equipos; en las cuentas del Estado, incluyen la inversión pública."))
_v("gobierno-general",
   ("Gobierno central", r"Los ministerios, oficinas y organismos que dependen del Poder Ejecutivo nacional."),
   ("Gobierno central consolidado", r"El gobierno central junto con otras entidades nacionales que tienen presupuesto propio, como EsSalud o la ONP, sin duplicar las transferencias entre ellas."),
   ("Gastos de Gobierno Central", r"Todo el gasto de los ministerios y organismos que dependen del Poder Ejecutivo."))
_v("gobiernos-regionales-y-locales",
   ("Gobierno local", r"Las municipalidades provinciales y distritales, con autonomía política, económica y administrativa en su territorio."))
_v("margen-de-utilidad",
   ("Gastos operativos", r"Gastos para que la empresa funcione que no son el costo directo de lo que vende, como sueldos administrativos, alquileres o publicidad."))
_v("reservas-internacionales",
   ("Good delivery", r"Estándar de calidad de las barras de oro y plata que aceptan los mercados de Londres y Nueva York; las reservas en oro suelen guardarse en barras con este estándar."),
   ("Liquidez internacional", r"Capacidad de un país para pagar sus obligaciones en moneda extranjera; se mide sobre todo con las reservas internacionales."))
_v("negociacion-colectiva",
   ("Huelga", r"Suspensión colectiva y pacífica del trabajo que deciden los trabajadores para presionar en un conflicto laboral; la ley fija los requisitos para que sea legal."))
_v("riesgo-de-liquidez",
   ("Iliquidez", r"Situación en la que alguien no tiene suficientes activos líquidos para pagar sus deudas de corto plazo, aunque pueda tener otros bienes."))
_v("exportaciones-e-importaciones",
   ("Importación", r"Compra de bienes o servicios a otro país."),
   ("Importación de bienes de capital", r"Compras al exterior de maquinaria, equipos y otros bienes que se usan para producir."),
   ("Importación de bienes de consumo", r"Compras al exterior de bienes para uso final de las familias, como ropa, electrodomésticos o alimentos."),
   ("Importación de insumos", r"Compras al exterior de materias primas y productos intermedios que las empresas transforman, como combustibles o químicos."))
_v("consumo-intermedio",
   ("Insumo", r"Bien que se usa y transforma en la producción de otro producto."))
_v("tributo",
   ("Impuesto", r"Tributo que se paga sin recibir a cambio un servicio directo del Estado, como el IGV o el impuesto a la renta."))
_v("impuesto-directo-e-indirecto",
   ("Impuesto indirecto", r"Impuesto sobre el consumo, la producción o las ventas, como el IGV o el ISC; lo paga quien compra, sin importar su ingreso."),
   ("Impuestos a los ingresos", r"Impuestos sobre lo que ganan las personas y empresas; en el Perú, principalmente el impuesto a la renta."),
   ("Impuestos al patrimonio", r"Impuestos sobre lo que se posee o se transfiere, como el predial, el vehicular o la alcabala."),
   ("Impuestos a los combustibles", r"Impuestos al consumo de gasolina y otros derivados del petróleo, principalmente el impuesto selectivo al consumo."))
_v("arancel",
   ("Impuestos a la importación", r"Impuestos sobre el valor CIF de los productos importados; es otro nombre de los aranceles."),
   ("Impuestos a la exportación", r"Impuestos sobre el valor FOB de lo que se exporta; hoy el Perú no cobra derechos a la exportación de bienes."))
_v("demanda-interna",
   ("Indicador de demanda interna", r"Indicador que sigue cuánto gastan en total los residentes del país, en consumo e inversión."))
_v("indicador-adelantado",
   ("Indicador económico", r"Dato cuya evolución informa sobre la marcha de la economía, como el PBI, el empleo o la inflación.") )
_v("indice-de-confianza-empresarial",
   ("Índice de acceso al crédito", r"Indicador de la encuesta del BCRP que pregunta a las empresas si hoy les es más fácil o más difícil conseguir crédito que antes."))
_v("roe-y-roa",
   ("Indicadores de empresas bancarias", r"Ratios para evaluar a un banco: solvencia, calidad de su cartera, eficiencia, rentabilidad (como ROE y ROA) y liquidez."))
_v("riesgo-de-mercado",
   ("Indicadores de riesgo", r"Medidas de cuánto puede ganar o perder una entidad si se mueven las tasas, el tipo de cambio o los precios de mercado."))
_v("numeros-indice",
   ("Índice", r"Serie de números que muestra cómo cambia una variable en el tiempo respecto a un periodo base."))
_v("indice-de-precios-de-exportacion",
   ("Índice de Precios de Importación", r"Mide cómo cambian, en promedio, los precios de lo que el país compra al exterior, como alimentos, combustibles e insumos."),
   ("Índice de volumen de exportación", r"Mide cómo cambian las cantidades exportadas, sin el efecto de los precios, respecto a un año base."),
   ("Índice de volumen de importación", r"Mide cómo cambian las cantidades importadas, sin el efecto de los precios, respecto a un año base."))
_v("bienes-transables-y-no-transables",
   ("Índice de precios de productos no transables", r"Sigue los precios de bienes y servicios que no se comercian con el exterior, como servicios personales o alquileres."),
   ("Índice de precios de productos transables", r"Sigue los precios de bienes y servicios que sí se comercian con el exterior, cuyo precio depende más del tipo de cambio y de los precios internacionales."),
   ("Inflación no transables", r"La inflación de los productos no transables; refleja sobre todo las presiones de la demanda interna."))
_v("terminos-de-intercambio",
   ("Índice de Términos de Intercambio", r"Índice de precios de exportación dividido entre índice de precios de importación; muestra cuánto puede comprar el país con lo que vende."))
_v("tipo-de-cambio-real",
   ("Índice de Tipo de Cambio Real", r"Muestra cómo evoluciona el tipo de cambio real respecto a un periodo base; si sube, el sol se depreció en términos reales."))
_v("pea",
   ("Índices de empleo urbano", r"Índices que siguen el empleo en empresas de ciudades respecto a un periodo base, a partir de una encuesta mensual del Ministerio de Trabajo."))
_v("inflacion-importada",
   ("Inflación externa", r"Promedio de la inflación de los principales socios comerciales del país, medida en dólares."))
_v("inflacion-sin-alimentos-y-energia",
   ("Inflación sin alimentos", r"La inflación calculada excluyendo los precios de alimentos y bebidas, que suelen moverse mucho por el clima."))
_v("remuneracion-minima-vital",
   ("Ingreso mínimo legal", r"Otro nombre de la remuneración mínima vital."))
_v("pbi-per-capita",
   ("Ingreso per cápita", r"Ingreso promedio por habitante en un año; sirve para comparar niveles de vida entre países."))
_v("ingresos-tributarios",
   ("Ingresos", r"Recursos que una entidad recibe de forma regular por su actividad."),
   ("Ingresos corrientes", r"En las cuentas del Estado, los ingresos regulares: tributarios y no tributarios."),
   ("Ingresos corrientes tributarios", r"Los impuestos que los contribuyentes pagan al gobierno central."),
   ("Ingresos corrientes no tributarios", r"Ingresos regulares del Estado que no son impuestos, como tasas por servicios, intereses, canon o regalías."),
   ("Ingresos no tributarios", r"Ingresos del Estado por servicios (tasas), por el uso de recursos naturales (canon, regalías) y otros conceptos distintos de los impuestos."),
   ("Ingresos de capital", r"Ingresos del Estado que no son regulares y suelen destinarse a inversión, como la venta de activos o transferencias de capital."))
_v("privatizacion",
   ("Ingresos de privatización", r"Lo que recibe el Estado por vender empresas o activos públicos o por dar concesiones."))
_v("margen-financiero",
   ("Ingresos financieros", r"Ingresos por los intereses que generan depósitos, préstamos y bonos."),
   ("Margen", r"Diferencia entre dos precios o tasas: en un banco, entre la tasa que cobra y la que paga; en bonos, entre su rendimiento y el de un bono de referencia."))
_v("bcrp",
   ("Instituto emisor", r"Otro nombre del banco central, porque es quien emite los billetes y monedas."))
_v("censo",
   ("Instituto Nacional de Estadística e Informática - INEI", r"Entidad que produce las estadísticas oficiales del Perú, como el IPC, la pobreza, el empleo y los censos nacionales."))
_v("operacion-de-mercado-abierto",
   ("Instrumento de política monetaria", r"Herramientas del banco central para manejar la liquidez y las tasas: operaciones de mercado abierto, encaje, depósitos y créditos de regulación."),
   ("Mercado abierto", r"Mercado de títulos donde el banco central compra y vende valores para regular la liquidez; las operaciones se basan en el valor de los títulos y no en quién es el deudor."))
_v("tasa-de-interes",
   ("Interés", r"El precio que paga quien recibe un préstamo por usar dinero ajeno durante un tiempo."),
   ("Interés adeudado", r"Interés que genera un préstamo y que el cliente debe."),
   ("Intereses por cobrar", r"Cuenta del activo con los intereses que ya se ganaron pero todavía no se cobraron."),
   ("Intereses por pagar", r"Cuenta del pasivo con los intereses que ya se deben pero todavía no se pagaron."))
_v("interes-moratorio",
   ("Interés atrasado", r"Todos los intereses vencidos y no pagados, incluidos los moratorios, los de refinanciación y otros cargos."))
_v("tasa-de-interes-real",
   ("Interés real", r"Otro nombre de la tasa de interés real: el interés descontando la inflación."))
_v("intermediacion-financiera",
   ("Intermediario financiero", r"Entidad que recibe dinero del público y lo presta a otros, cambiando plazos y montos, como un banco o una caja."))
_v("esterilizacion",
   ("Intervención esterilizada", r"Compra o venta de dólares por parte del banco central acompañada de una operación que neutraliza su efecto sobre la cantidad de soles."))
_v("variacion-de-existencias",
   ("Inventario", r"Bienes que una empresa guarda, como materias primas o productos terminados, para producir o vender después."))
_v("inversion-extranjera-directa",
   ("Inversión extranjera neta", r"La inversión que entra del exterior menos lo que sale por recuperación de capital o remesas de utilidades."),
   ("Inversionistas no residentes", r"Personas o empresas cuyo centro de intereses económicos está fuera del país."))
_v("inversion-extranjera-en-cartera",
   ("Inversiones en el exterior", r"Activos de residentes fuera del país, como bonos, depósitos, fondos o acciones extranjeras."),
   ("Inversionistas residentes", r"Personas o empresas cuyo centro de intereses económicos está dentro del país."))
_v("ciclo-economico",
   ("Largo plazo", r"En finanzas, un plazo mayor a un año; en teoría económica, el horizonte en que pueden ajustarse todos los factores, incluida la capacidad de las fábricas."))
_v("credito-hipotecario",
   ("Letras hipotecarias", r"Títulos que emite una entidad financiera respaldados por un crédito hipotecario y que pueden negociarse en el mercado."))
_v("apertura-comercial",
   ("Liberalización del comercio exterior", r"Proceso de reducir o eliminar aranceles y otras barreras al comercio."))
_v("dolarizacion",
   ("Liquidez en moneda extranjera", r"Depósitos y otras obligaciones en dólares de las entidades financieras con el público."))
_v("agregados-monetarios",
   ("Liquidez en moneda nacional", r"Depósitos y otras obligaciones en soles de las entidades financieras con el público, incluido el dinero y el cuasidinero."),
   ("Masa monetaria", r"Los activos líquidos en manos del público; es otro nombre de la liquidez o dinero en sentido amplio."))
_v("salvaguardia-y-antidumping",
   ("Medidas compensatorias", r"Aranceles adicionales que un país aplica para contrarrestar el daño de importaciones que recibieron subsidios en su país de origen."))


# --- Bloque 3 (M a S) -----------------------------------------------------
_v("contrato-forward",
   ("Mercado al contado", r"Mercado donde la entrega y el pago son inmediatos o casi inmediatos, a diferencia de los mercados a plazo o de futuros."),
   ("Operaciones forward", r"Compras o ventas pactadas hoy para hacerse en una fecha futura, con precio, cantidad y fecha fijados en el contrato."))
_v("contrato-de-futuro",
   ("Mercado de futuros", r"Mercado organizado donde se negocian contratos estandarizados para comprar o vender en el futuro materias primas, divisas o tasas de interés."),
   ("Precio de liquidación", r"Precio de referencia que se usa para calcular las ganancias y pérdidas de un contrato de futuro u opción en una fecha."))
_v("opcion",
   ("Mercado de opciones", r"Mercado organizado donde se compran y venden opciones estandarizadas sobre acciones, materias primas o activos financieros."),
   ("Opción call", r"Opción de compra: da el derecho, pero no la obligación, de comprar un activo a un precio fijado."),
   ("Prima", r"En opciones, el precio que paga el comprador por el derecho; en seguros, lo que se paga por la cobertura; en bonos, lo que el precio supera al valor nominal."))
_v("mercado-de-capitales",
   ("Mercado de valores", r"Mercado donde se compran y venden acciones, bonos y otros títulos; incluye el mercado primario y el secundario."),
   ("Mercados financieros", r"Espacios donde quienes tienen fondos y quienes los necesitan negocian directamente: mercados de dinero, de capitales, de divisas y de derivados."),
   ("Oferta pública de valores", r"Invitación al público en general o a un grupo amplio para comprar valores, como acciones o bonos; necesita autorización del supervisor."))
_v("mercado-primario-y-secundario",
   ("Mercado secundario", r"Mercado donde se negocian títulos que ya fueron emitidos antes, entre inversionistas."))
_v("economias-emergentes",
   ("Mercados emergentes", r"Mercados financieros de países en desarrollo que se abrieron al capital extranjero y están creciendo y profundizándose."),
   ("Países desarrollados", r"Países con ingreso por habitante alto, como la mayoría de Europa occidental, Estados Unidos, Canadá o Japón."),
   ("Países en vías de desarrollo", r"Países con ingreso por habitante bajo o medio que están en proceso de crecimiento."))
_v("materias-primas",
   ("Metales preciosos", r"Metales de alto valor por unidad, como el oro, la plata y el platino."),
   ("Minerales no metálicos", r"Minerales que no son metales, como la arcilla, la caliza, el mármol o el yeso, muy usados en construcción."),
   ("Petróleo crudo", r"Mezcla de hidrocarburos líquidos extraída del subsuelo; es la materia prima de la gasolina, el diésel y otros derivados."),
   ("Productos básicos", r"Otro nombre de las materias primas o commodities: bienes poco diferenciados, como metales, petróleo o granos, que se venden en mercados internacionales."))
_v("cono-monetario",
   ("Moneda", r"Pieza de metal acuñada por encargo del BCRP, de curso legal, que se usa sobre todo en pagos pequeños."),
   ("Reverso", r"Cara secundaria de un billete o moneda, opuesta al anverso; en las monedas peruanas es donde aparece el valor."),
   ("Patrón de calidad", r"Billetes y monedas de referencia que fija el BCRP para decidir hasta qué nivel de desgaste pueden seguir circulando."),
   ("Retiro de circulación", r"Cuando el BCRP deja de poner en circulación billetes o monedas deteriorados, de poco valor o reemplazados por otros."))
_v("circulante",
   ("Numerario", r"Los billetes y monedas que emite el BCRP y que están en manos del público y de los bancos."),
   ("Programación de numerario", r"Cálculo de cuántos billetes y monedas de cada denominación necesitará la economía en un periodo."))
_v("reservas-internacionales",
   ("Monetización del oro", r"Cuando el banco central pasa a contar como reserva oro que ya tenía o compra en el país."),
   ("Oro en bóveda", r"Oro en barras o monedas que el BCRP guarda en sus propias bóvedas."),
   ("Oro monetario", r"Oro refinado de alta pureza que tiene la autoridad monetaria como parte de sus reservas."),
   ("Reservas de divisas", r"Monedas extranjeras y derechos especiales de giro que tiene un país en su banco central o en organismos internacionales."),
   ("Pasivos internacionales", r"Deudas de corto plazo del banco central con el exterior, incluidas las del FMI; se restan de las reservas brutas para obtener las reservas netas."))
_v("programa-monetario",
   ("Nota informativa", r"Comunicado del BCRP que explica la decisión sobre la tasa de referencia y resume la situación económica reciente."))
_v("pagare",
   ("Notas comerciales", r"Promesas de pago de corto plazo, sin garantía, que emiten empresas reconocidas para financiarse."))
_v("bono",
   ("Obligación", r"Deber legal de dar, hacer o no hacer algo; en finanzas, también un título de deuda parecido a un bono."))
_v("cheque",
   ("Obligaciones a la vista", r"Deudas de las entidades financieras que el público puede retirar de inmediato, como los depósitos en cuenta corriente."))
_v("deposito-de-ahorro",
   ("Obligaciones de ahorro", r"Lo que las entidades financieras deben a sus clientes por depósitos de ahorro."))
_v("deuda-externa",
   ("Obligaciones a largo plazo con el exterior", r"Deudas con no residentes con plazo mayor a un año."),
   ("Pasivos con el exterior", r"Deudas de corto y largo plazo con acreedores extranjeros, como préstamos de bancos del exterior."),
   ("Renegociación de la deuda", r"Proceso para cambiar las condiciones de pago de una deuda, con nuevos plazos, refinanciación o descuentos."))
_v("linea-de-credito",
   ("Obligaciones contingentes", r"Deudas que solo aparecen si ocurre un hecho, como el incumplimiento de un cliente garantizado; no figuran en el balance mientras tanto."))
_v("deuda-publica",
   ("Obligaciones del sector público", r"Deuda de mediano y largo plazo que emite el Estado para financiarse."))
_v("deuda-interna",
   ("Obligaciones domésticas", r"Títulos de deuda que el Estado coloca en el mercado local para conseguir recursos."))
_v("oferta-agregada",
   ("Oferta global", r"Otro nombre de la oferta agregada: toda la oferta de bienes y servicios de la economía, producción local más importaciones."))
_v("agregados-monetarios",
   ("Oferta monetaria", r"La cantidad de dinero disponible en la economía, medida con agregados monetarios como la liquidez."))
_v("inversion-extranjera-directa",
   ("Operación conjunta", r"Acuerdo entre dos o más empresas para hacer juntas un proyecto (joint venture); es una forma frecuente de inversión extranjera."),
   ("Reinversión extranjera", r"Parte de las utilidades de empresas con capital extranjero que se queda en el país en lugar de enviarse a sus dueños; cuenta como inversión directa."))
_v("letra-de-cambio",
   ("Operación de descuento", r"Cuando un banco adelanta el dinero de un título por cobrar, como una letra, descontando los intereses por el tiempo que falta para su vencimiento."))
_v("redescuento",
   ("Operación de redescuento", r"Cuando el banco central vuelve a descontar a un banco títulos que este ya había descontado a sus clientes; así le da liquidez."))
_v("repo",
   ("Operación de recompra", r"Otro nombre del repo: venta de un título con el compromiso de recomprarlo después a un precio pactado."))
_v("intervencion-cambiaria",
   ("Operaciones cambiarias", r"Compras y ventas de moneda extranjera que hace el BCRP en el mercado y con el sector público."))
_v("gobierno-general",
   ("Operaciones de gobierno central", r"Presentación ordenada de los ingresos y gastos de las entidades del gobierno central."),
   ("Operaciones de gobierno general", r"Presentación ordenada de los ingresos y gastos de todo el gobierno general: central, regional y local."))
_v("gobiernos-regionales-y-locales",
   ("Operaciones de gobiernos locales", r"Ingresos y gastos de las municipalidades provinciales y distritales."))
_v("tasa-de-interes-interbancaria",
   ("Operaciones interbancarias", r"Préstamos de muy corto plazo entre entidades financieras para cubrir faltantes temporales de dinero."))
_v("sistema-de-pagos",
   ("Orden de transferencia aceptada", r"Orden de pago que cumple las reglas del sistema y, por eso, ya no puede revocarse."),
   ("Orden de transferencia de fondos", r"Instrucción de un participante para mover dinero a favor de un beneficiario a través de un sistema de pagos."),
   ("Orden de transferencia de valores", r"Instrucción para transferir la propiedad de valores a otro participante en un sistema de liquidación."),
   ("Participante", r"Entidad aceptada en un sistema de pagos o de liquidación de valores, que puede enviar órdenes de transferencia."),
   ("Participante receptor", r"Entidad que recibe los pagos o cobros enviados por otra entidad, para aplicarlos en las cuentas de sus clientes."),
   ("Proveedor de servicios de pagos", r"Empresa que ofrece servicios para transferir dinero, como transferencias, tarjetas o billeteras digitales."),
   ("Recursos", r"En un sistema de pagos, el dinero y los valores que cada participante tiene disponibles para cumplir sus pagos."))
_v("balanza-de-pagos",
   ("Otros capitales", r"Rubro que registra los atrasos de deuda, es decir, los pagos de intereses y capital que vencieron y no se pagaron."),
   ("Residente", r"Persona o empresa cuyo centro de intereses económicos está en el país, aunque tenga otra nacionalidad; la balanza de pagos registra operaciones entre residentes y no residentes."),
   ("Repatriación de capitales", r"Cuando los residentes traen de vuelta al país el dinero que tenían en el exterior, normalmente porque esperan que la economía local mejore."))
_v("balance-general",
   ("Pasivos", r"Todas las deudas y obligaciones de una persona o empresa con terceros."),
   ("Otros activos", r"Activos que no entran en las cuentas principales, como pagos adelantados o cuentas por cobrar diversas."),
   ("Otros pasivos", r"Obligaciones que no entran en las cuentas principales, como dividendos por pagar o provisiones."),
   ("Reservas", r"En contabilidad, parte de las utilidades que se separa y se guarda en el patrimonio para un fin, como la reserva legal."),
   ("Saldo", r"Diferencia entre lo que entra y lo que sale en una cuenta en un momento dado."))
_v("gasto-corriente-y-de-capital",
   ("Otros gastos de capital", r"Gastos de capital del Estado que no son inversión directa, como transferencias para promover actividades o aportes a organismos."))
_v("exportaciones-tradicionales-y-no-tradicionales",
   ("Otros productos tradicionales", r"Exportaciones tradicionales que no son minería, pesca, petróleo ni café o azúcar, como la lana de alpaca o algunas pieles."))
_v("balanza-de-servicios",
   ("Otros servicios", r"Exportaciones e importaciones de servicios distintos del transporte y los viajes, como seguros, servicios financieros, de informática o de gobierno."))
_v("presupuesto-publico",
   ("Pago", r"Última etapa del gasto público: cuando se cancela la obligación."),
   ("Rendición de cuentas", r"Presentar públicamente, por escrito, qué resultados logró una institución o un programa con los recursos que recibió."))
_v("ingresos-tributarios",
   ("Recursos directamente recaudados", r"Ingresos que las entidades públicas generan y administran ellas mismas, como tasas por trámites o alquileres de sus bienes."),
   ("Recaudación", r"Lo que el Estado cobra por tributos; la recaudación neta resta las devoluciones."))
_v("remesas",
   ("Pagos de transferencia", r"Transferencias sin contraprestación entre países que se registran en la cuenta corriente, como donaciones entre gobiernos o remesas familiares."))
_v("apalancamiento",
   ("Palanca Global", r"Relación entre los activos ponderados por riesgo de un banco (de crédito, de mercado y operacional) y su patrimonio efectivo; la ley le pone un límite."))
_v("patron-oro",
   ("Paridad oro", r"En el patrón oro, cuánto oro valía cada unidad de moneda; de esas paridades salían los tipos de cambio entre países."))
_v("accion",
   ("Participación de capital", r"Parte del capital de una empresa que da derechos a su dueño; puede estar representada por acciones físicas o anotaciones electrónicas."))
_v("ratio-de-capital-global",
   ("Patrimonio efectivo", r"El capital que la regulación reconoce para respaldar los riesgos de un banco: capital pagado, reservas y otras partidas permitidas."))
_v("desestacionalizacion",
   ("PBI desestacionalizado", r"El PBI al que se le quitó el efecto de la estacionalidad, para comparar un periodo con el anterior sin la distorsión de fiestas o campañas."))
_v("pbi-primario-y-no-primario",
   ("PBI sectores no primarios", r"La producción de manufactura no primaria, construcción, comercio y servicios, que depende más de la demanda interna."))
_v("tasa-de-desempleo",
   ("PEA desocupada", r"Personas de 14 años o más que no tenían trabajo pero buscaron activamente uno en el periodo de referencia."),
   ("Población desempleada", r"Personas en edad y disposición de trabajar que no tenían empleo y lo buscaron en el periodo de referencia."))
_v("pea",
   ("PEA ocupada", r"Parte de la PEA que trabajó en el periodo de referencia, con o sin pago."),
   ("Población ocupada o empleada", r"Todas las personas en edad de trabajar que tenían un empleo en el periodo de referencia."))
_v("subempleo",
   ("Población adecuadamente empleada", r"Trabajadores que no están subempleados: trabajan las horas que desean y ganan al menos un ingreso considerado adecuado."))
_v("afp-y-onp",
   ("Pensiones", r"Pagos periódicos que reciben las personas de la seguridad social o de una entidad privada autorizada, por jubilación, invalidez o sobrevivencia."),
   ("Prestaciones", r"Servicios o pagos que reciben los trabajadores o sus familias ante riesgos como enfermedad, vejez, invalidez o muerte."))
_v("censo",
   ("Población total", r"Todas las personas registradas en un censo de población."),
   ("Población urbana", r"Personas que viven en centros poblados urbanos, según la definición del INEI en los censos."))
_v("apertura-comercial",
   ("Política de apertura", r"Políticas que definen cuánto se expone la economía al comercio y a los capitales del exterior."))
_v("politica-anticiclica",
   ("Política de estabilización", r"Medidas de corto plazo para que la demanda crezca al ritmo de lo que la economía puede producir, evitando presiones sobre precios."),
   ("Programa económico", r"Conjunto de medidas que las autoridades ponen en marcha para lograr objetivos económicos o salir de una crisis."))
_v("remuneracion-minima-vital",
   ("Política de ingresos", r"Intervención del gobierno en cómo se forman los sueldos y otros ingresos, por ejemplo con salarios mínimos o acuerdos salariales."),
   ("Remuneración", r"Todo lo que el empleador paga a un trabajador por su trabajo, en dinero o en especie."),
   ("Salario", r"Pago que recibe un trabajador por su trabajo, pactado con su empleador."))
_v("presion-tributaria",
   ("Política tributaria", r"Decisiones sobre qué tributos cobrar, a qué tasas, a quiénes y cómo administrarlos."))
_v("evasion-y-elusion-tributaria",
   ("Regularización de impuestos", r"Pago de impuestos atrasados, ya sea de forma voluntaria o tras una fiscalización."))
_v("valor-a-la-par",
   ("Por debajo de la par / bajo la par", r"Cuando un título se negocia a un precio menor que su valor nominal."),
   ("Precio de emisión", r"Precio al que se vende por primera vez un título; puede ser igual, mayor o menor que su valor nominal."),
   ("Premio", r"Diferencia entre el precio de un título y su valor a la par, expresada en porcentaje; en divisas, la diferencia entre el tipo de cambio a plazo y al contado."))
_v("portafolio",
   ("Portafolio de referencia", r"Cartera que sirve como punto de comparación (benchmark) para medir el rendimiento y el riesgo de otra."),
   ("Ratio de información", r"Mide cuánto rinde un portafolio por encima de su referencia por cada unidad de riesgo adicional asumida."))
_v("posicion-larga-y-corta",
   ("Posición", r"Saldo de una cuenta en un momento dado, o la exposición que tiene un inversionista en un activo, sea comprador o vendedor."),
   ("Posición corta", r"Cuando se ha vendido más de una moneda o activo del que se ha comprado; se gana si su precio baja."),
   ("Posición descubierta o al descubierto", r"Vender un valor que todavía no se tiene, con la obligación de entregarlo después."))
_v("posicion-de-cambio",
   ("Posición de cambio del BCRP", r"Los activos en moneda extranjera del BCRP menos sus obligaciones en esa moneda; muestra los dólares de libre disponibilidad del banco central."))
_v("oferta-y-demanda",
   ("Precio", r"El valor de un bien o servicio expresado en dinero; puede fijarlo el mercado o una autoridad."))
_v("precios-al-por-mayor",
   ("Precio al por menor", r"Precio que paga el consumidor final en una tienda; suele ser mayor que el precio al por mayor."))
_v("colocaciones",
   ("Préstamo", r"Entrega de dinero a un deudor que se compromete a devolverlo, normalmente con intereses, según un documento firmado."))
_v("credito-hipotecario",
   ("Préstamo hipotecario", r"Crédito para comprar, construir o mejorar una vivienda, con la vivienda como garantía."))
_v("indicador-adelantado",
   ("Producción industrial", r"Índice de la Reserva Federal que mide la producción de la industria, la minería y los servicios públicos en Estados Unidos; se sigue de cerca como termómetro de su economía."))
_v("sectores-economicos",
   ("Producción manufacturera", r"El PBI del sector manufactura, calculado con índices de volumen de producción de la industria."),
   ("Producción pesquera", r"El PBI del sector pesca, con datos de captura y desembarque de especies."),
   ("Producción de electricidad", r"La generación de energía eléctrica, que se usa como indicador de la actividad del sector electricidad y agua."))
_v("bienes-transables-y-no-transables",
   ("Productos no transables", r"Bienes y servicios que no se comercian con el exterior y cuyo precio depende del mercado local."),
   ("Productos transables", r"Bienes que se pueden comerciar internacionalmente y cuyo precio sigue a los precios del exterior."))
_v("pbi",
   ("Producto", r"Bien o servicio que resulta de un proceso de producción."))
_v("transferencias-condicionadas",
   ("Programas de alivio a la pobreza", r"Acciones del Estado o de organizaciones privadas para reducir la pobreza, como transferencias, comedores o programas de empleo temporal."))
_v("provisiones",
   ("Provisiones Específicas", r"Provisiones sobre créditos de deudores que ya muestran problemas de pago; crecen según el riesgo de cada deudor."),
   ("Provisiones Genéricas", r"Provisiones preventivas sobre créditos que hoy están al día, para cubrir pérdidas que podrían aparecer."),
   ("Saneamiento de los activos", r"Limpiar el balance eliminando bienes que no rinden y créditos difíciles de cobrar."))
_v("valor-nominal-y-real",
   ("Real", r"Se dice de una cifra a la que se le quitó el efecto de la inflación, para medir cantidades y no solo precios."))
_v("regimen-cambiario",
   ("Régimen de tipo de cambio fijo", r"El país fija el valor de su moneda frente a otra moneda o a una canasta, y el banco central se compromete a defenderlo."),
   ("Régimen de tipo de cambio flotante", r"El tipo de cambio lo determina el mercado por la oferta y la demanda de divisas, sin un valor fijo."))
_v("regla-de-taylor",
   ("Regla de política monetaria", r"Fórmula que describe cómo debería mover el banco central su tasa de interés ante cambios en la inflación y la actividad; la regla de Taylor es la más conocida."))
_v("encaje-bancario",
   ("Remuneración al encaje", r"Intereses que el BCRP paga por parte del encaje que los bancos dejan depositado en él."),
   ("Reserva legal", r"Otro nombre del encaje exigible."),
   ("Reservas bancarias", r"Otro nombre del encaje: el dinero que los bancos guardan en caja o en el BCRP."))
_v("rentabilidad",
   ("Rendimiento", r"Ganancia que produce una inversión, expresada como porcentaje de lo invertido; se usa casi como sinónimo de rentabilidad."),
   ("Rendimiento de la inversión", r"Ganancia que se espera obtener de un proyecto, estimada con criterios como el VAN o la TIR."))
_v("renta-de-factores",
   ("Renta de inversiones", r"Ingresos por intereses, dividendos y utilidades de activos en el exterior, y pagos por esos mismos conceptos a no residentes."))
_v("amortizacion",
   ("Repago, redención", r"Devolución de una deuda o de un bono, al vencimiento o antes, en efectivo o con nuevos títulos."),
   ("Principal de la deuda", r"El monto prestado, sin intereses, que debe devolverse en una o varias cuotas."))
_v("renta-vitalicia",
   ("Renta", r"Cantidad que alguien recibe periódicamente, por un tiempo o de por vida; también, el ingreso que produce un bien o una actividad."))
_v("resultado-primario",
   ("Resultado económico", r"Diferencia entre todos los ingresos y todos los gastos del sector público, incluidos los intereses; si es negativo, hay déficit."),
   ("Resultado económico estructural", r"El resultado fiscal sin los efectos de factores fuera de control del gobierno, como el ciclo económico o los precios de los minerales."))
_v("prima-de-riesgo",
   ("Riesgo", r"Probabilidad de que ocurra algo adverso o grado de incertidumbre de una operación; mayor riesgo suele exigir mayor rentabilidad."))
_v("riesgo-pais",
   ("Riesgo soberano", r"Riesgo de que el Estado de un país no pague su deuda; se usa casi como sinónimo de riesgo país."))

# --- Bloque 4 (S a Z) ---
_v("sectores-economicos",
   ("Sector agropecuario", r"Agricultura y ganadería: cultivos, crianza de animales y sus productos, como papa, arroz, leche o pollo."),
   ("Sector comercio", r"Compra y venta de productos sin transformarlos. En las cuentas nacionales se mide con el margen que ganan los comerciantes."),
   ("Sector construcción", r"Obras de vivienda, edificios, carreteras y otras. En el Perú se sigue sobre todo con el consumo de cemento y el avance de la obra pública."),
   ("Sector electricidad", r"Producción y reparto de energía eléctrica, junto con agua y gas en muchas estadísticas."),
   ("Sector manufactura", r"Fábricas que transforman insumos en productos, como alimentos envasados, textiles, cemento o refinación de metales."),
   ("Sector minería e hidrocarburos", r"Extracción de minerales (cobre, oro, zinc) y de petróleo y gas natural."),
   ("Sector pesca", r"Captura de peces y otras especies del mar o de ríos, para consumo humano o para harina y aceite de pescado."),
   ("Sector primario", r"Actividades que sacan recursos de la naturaleza casi sin transformarlos: agro, pesca, minería e hidrocarburos."),
   ("Sector secundario", r"Actividades que transforman materias primas en otros bienes: manufactura y construcción."),
   ("Sector terciario", r"Actividades que producen servicios: comercio, transporte, finanzas, educación, salud, turismo y otros."),
   ("Sector Servicios", r"Otra forma de llamar al sector terciario: todo lo que no es un bien físico, sino una atención o una actividad que se presta."),
   ("Sector no primario", r"Todo lo que no es sector primario, es decir, los sectores secundario y terciario juntos."))
_v("balanza-de-pagos",
   ("Sector externo", r"Todas las operaciones de un país con el resto del mundo: comercio, rentas, transferencias y movimientos de capital. Se resume en la balanza de pagos."),
   ("Superávit de la balanza de pagos", r"Cuando en un periodo entran más dólares de los que salen por todas las operaciones con el exterior; suele reflejarse en un aumento de las reservas internacionales."),
   ("Transferencias de capital", r"Traspasos sin pago a cambio ligados a inversión o activos, como el perdón de una deuda o donaciones para construir obras."))
_v("mercado-de-dinero",
   ("Sector monetario", r"Parte de la economía que estudia el dinero, el crédito y los mercados financieros, y cómo los afecta la política del banco central."))
_v("consumo-privado-y-publico",
   ("Sector privado", r"Hogares, empresas privadas y entidades sin fines de lucro; todo lo que no depende del Estado."),
   ("Sector público", r"Todas las entidades del Estado: gobierno central, regional y local, y empresas públicas."))
_v("compania-de-seguros",
   ("Seguros", r"Contrato en el que pagas una prima y, a cambio, la aseguradora te paga una suma si ocurre el daño cubierto (accidente, robo, enfermedad, muerte)."))
_v("balanza-de-servicios",
   ("Servicios", r"En la balanza de pagos, el comercio de cosas que no se ven ni se tocan con el exterior: transporte, viajes, seguros, regalías y otros."),
   ("Servicios de gobierno", r"Gastos de embajadas, consulados y otras oficinas del Estado en el extranjero, y los de oficinas extranjeras en el país."),
   ("Servicios diversos", r"Servicios con el exterior que no entran en los rubros grandes: consultoría, informática, comunicaciones, publicidad y otros."),
   ("Transportes", r"Fletes y pasajes que se pagan o cobran al resto del mundo por llevar carga o personas."))
_v("pobreza-multidimensional",
   ("Servicios de la vivienda", r"Agua, desagüe y luz con que cuenta un hogar. Su falta se usa para medir pobreza más allá del ingreso."))
_v("bienes-publicos",
   ("Servicios públicos", r"Servicios que suele dar el Estado o que regula, como agua, luz, salud, educación o limpieza; pueden ser gratuitos o con tarifa."),
   ("Tarifa", r"Precio que paga el usuario por un servicio público, como la luz o el agua; en el Perú lo fijan o supervisan reguladores como Osinergmin o Sunass."))
_v("sistema-financiero",
   ("Sistema bancario", r"El conjunto de bancos de un país, que reciben depósitos y dan préstamos."),
   ("Sistema financiero bancario", r"Igual que el sistema bancario: todos los bancos que operan en el país, incluido el banco central en algunas estadísticas."),
   ("Sistema financiero no bancario", r"Entidades financieras que no son bancos: cajas, financieras, AFP, aseguradoras, fondos mutuos y otras."),
   ("Sociedades de depósitos", r"Entidades que reciben depósitos que funcionan casi como dinero: el banco central, los bancos, cajas y financieras."))
_v("circulante",
   ("Sistema de Custodia", r"Acuerdo por el que el BCRP guarda parte de sus billetes y monedas en bóvedas de bancos, para tenerlos cerca de donde se usan."))
_v("arancel",
   ("Sistema de franja de precios", r"Mecanismo que sube el arancel cuando el precio internacional de un producto cae bajo un piso y lo baja cuando supera un techo, para que el precio local se mueva menos."))
_v("cavali",
   ("Sistema de Liquidación de Valores", r"Reglas y procesos para que, al negociar acciones o bonos, el comprador reciba los títulos y el vendedor el dinero. En el Perú lo opera CAVALI."))
_v("indexacion",
   ("Sistema de reajuste de deudas", r"Crédito cuyo saldo se actualiza con un índice, como la inflación, para que el prestamista no pierda poder de compra."))
_v("posicion-larga-y-corta",
   ("Stop order", r"Orden al intermediario para comprar o vender en cuanto el precio llegue a cierto nivel; se usa para cortar pérdidas."))
_v("subastas",
   ("Subasta", r"Venta en la que varios compradores ofrecen precios y el bien se queda con quien cumple la regla, casi siempre la mejor oferta."),
   ("Subasta de Primer Precio", r"Cada comprador entrega una sola oferta en sobre cerrado; gana la más alta y paga lo que ofreció."),
   ("Subasta inglesa", r"Las ofertas son públicas y van subiendo hasta que nadie da más; gana el último que ofreció."),
   ("Subasta Vickrey o de Segundo Precio", r"Sobre cerrado, gana la oferta más alta, pero paga el precio de la segunda mejor oferta. Así conviene ofrecer lo que de verdad vale para ti."),
   ("Subasta Yankee", r"Se venden varias unidades iguales; cada ganador paga lo que ofreció y debe llevarse la cantidad que pidió."))
_v("subempleo",
   ("Subempleo", r"Empleo de mala calidad: se gana menos de lo mínimo aceptable o se trabajan menos horas de las que uno quiere."))
_v("filial-y-sucursal",
   ("Subsidiaria", r"Otro nombre de la filial: empresa con personería propia controlada por otra."),
   ("Sucursal", r"Oficina de una misma empresa en otro lugar, que hace las mismas actividades que la sede y no tiene personería propia."))
_v("deficit-fiscal",
   ("Superávit", r"Cuando los ingresos superan a los gastos; es lo contrario del déficit."))
_v("balanza-comercial",
   ("Superávit comercial", r"Cuando un país exporta más de lo que importa en bienes."))
_v("balanza-en-cuenta-corriente",
   ("Superávit en cuenta corriente", r"Cuando el país recibe del exterior más de lo que paga por bienes, servicios, rentas y transferencias juntos."))
_v("sbs",
   ("Supervisión bancaria", r"Vigilancia de los bancos para que no tomen riesgos excesivos y puedan devolver los depósitos. En el Perú la hace la SBS."))
_v("organismos-multilaterales",
   ("Suscripción FMI y FLAR", r"Aporte que un país hace al FMI o al Fondo Latinoamericano de Reservas para ser miembro; le da derecho a participar y a pedir apoyo."))
_v("accion",
   ("Suscripción temporal de acciones", r"Aporte de capital a una empresa por un tiempo fijo, con el compromiso de recuperarlo luego."))
_v("swaps",
   ("Swap de tasas de interés", r"Dos partes intercambian los intereses de una deuda: una paga tasa fija y la otra tasa variable, sobre un mismo monto de referencia."),
   ("Tasa swap", r"Diferencia entre el tipo de cambio a futuro y el de hoy, expresada como tasa; muestra el costo de cubrirse con un forward."))
_v("tarjetas-de-credito-y-debito",
   ("Tarjetas de débito", r"Tarjeta que paga con tu propio dinero de la cuenta, al instante; no es un préstamo."))
_v("sistema-de-pagos",
   ("Transferencia de clientes", r"Envío de dinero de una persona o empresa a otra a través de un sistema de pagos, por ejemplo entre dos bancos."),
   ("Transferencia de Fondos", r"Movimiento de dinero entre cuentas, dentro de un mismo banco o entre bancos distintos."),
   ("Transferencias de crédito", r"Pago que inicia quien paga: ordena a su banco que mande el dinero a la cuenta del que cobra."))
_v("tributo",
   ("Tasa", r"Tributo que pagas por un servicio concreto del Estado, como un trámite, una licencia o un derecho de uso."))
_v("encaje-bancario",
   ("Tasa de encaje", r"Porcentaje de los depósitos que los bancos deben guardar y no pueden prestar."),
   ("Tasa de encaje efectivo", r"Lo que el banco realmente tiene guardado como encaje dividido entre sus depósitos sujetos a encaje."),
   ("Tasa de encaje exigible", r"Lo que el banco está obligado a guardar dividido entre sus depósitos sujetos a encaje."),
   ("Tasa de encaje legal", r"El porcentaje mínimo de encaje que fija la autoridad monetaria."),
   ("Tasa de encaje marginal", r"Porcentaje que se exige solo sobre los depósitos nuevos, por encima de un nivel base."),
   ("TOSE moneda extranjera", r"Total de obligaciones sujetas a encaje en dólares u otras monedas: la base sobre la que se calcula el encaje en moneda extranjera."),
   ("TOSE moneda nacional", r"Total de obligaciones sujetas a encaje en soles: la base sobre la que se calcula el encaje en moneda nacional."))
_v("inflacion",
   ("Tasa de inflación", r"Cuánto subieron los precios en un periodo, en porcentaje; en el Perú se mide con el IPC de Lima Metropolitana."))
_v("tasa-de-interes-activa-y-pasiva",
   ("Tasa de interés comercial", r"La que cobran los bancos a empresas por créditos para su negocio."),
   ("Tasa de interés de consumo", r"La que cobran a personas por créditos para comprar bienes o servicios, incluidas las tarjetas."),
   ("Tasa de interés hipotecario", r"La que cobran a personas por créditos para comprar o construir vivienda."),
   ("Tasa de interés pasiva", r"La que pagan los bancos a quienes depositan su dinero."),
   ("Tasa de interés preferencial", r"La tasa más baja que cobran los bancos, reservada para sus mejores clientes corporativos."),
   ("Tasa preferencial corporativa a 90 días", r"Tasa promedio a 90 días que cobran los bancos a las empresas grandes de menor riesgo; el BCRP la publica a diario."),
   ("Tasa préstamos y descuentos hasta 360 días", r"Tasa promedio de los créditos a un año o menos."),
   ("Tasa préstamos y descuentos a más de 360 días", r"Tasa promedio de los créditos a más de un año."))
_v("tasa-de-interes-legal",
   ("Tasa de interés compensatoria", r"Interés que se paga por usar el dinero de otro durante el plazo pactado; distinto del moratorio, que castiga el atraso."))
_v("tamn-y-tamex",
   ("Tasa de interés pasiva en moneda extranjera-TIPMEX", r"Tasa promedio que pagan los bancos por depósitos en dólares; la publica la SBS, igual que la TIPMN en soles."))
_v("pobreza-monetaria",
   ("Tasa de pobreza", r"Porcentaje de la población cuyo gasto está por debajo de la línea de pobreza; en el Perú la mide el INEI."),
   ("Tasa de pobreza extrema", r"Porcentaje de personas cuyo gasto no alcanza ni para la canasta básica de alimentos."))
_v("tasa-de-referencia",
   ("Tasa de política monetaria", r"Otro nombre de la tasa de referencia: la tasa interbancaria que el banco central busca lograr."))
_v("preferencia-por-circulante",
   ("Tasa de preferencia por circulante", r"Circulante dividido entre los depósitos: cuánto efectivo guarda la gente por cada sol que tiene en el banco."))
_v("tasa-impositiva-marginal",
   ("Tasa impositiva", r"Porcentaje que se aplica a la base imponible para calcular un impuesto, por ejemplo 18 % en el IGV."))
_v("presupuesto-publico",
   ("Tesoro público", r"Todo el dinero, valores y créditos que maneja el Estado; en el Perú lo administra el MEF."))
_v("contrato-forward",
   ("Tipo de cambio a futuro", r"Tipo de cambio que se acuerda hoy para comprar o vender divisas en una fecha futura."),
   ("Ventas a futuro pactadas", r"Venta cuyo precio y condiciones se fijan hoy, pero que se ejecuta en una fecha futura."),
   ("Ventas al contado", r"Venta en la que el pago y la entrega se hacen al mismo tiempo, sin plazo."))
_v("tipo-de-cambio",
   ("Tipo de cambio contable", r"Tipo de cambio del día que usan las empresas para registrar en soles sus cuentas en moneda extranjera; lo publica la SBS."),
   ("Tipo de cambio oficial", r"Tipo de cambio que fija o controla la autoridad, distinto del que sale libremente del mercado."))
_v("regimen-cambiario",
   ("Tipo de cambio fijo", r"El banco central mantiene el precio del dólar en un nivel y compra o vende divisas para sostenerlo."),
   ("Tipo de cambio flotante", r"El precio del dólar lo fijan la oferta y la demanda; el banco central puede intervenir solo para evitar saltos bruscos."))
_v("control-cambiario",
   ("Tipo de cambio múltiple", r"Cuando conviven dos o más tipos de cambio oficiales, según el tipo de operación (importar, exportar, viajar…)."))
_v("tipo-de-cambio-real",
   ("Tipo de cambio real bilateral", r"Tipo de cambio real frente a un solo país, por ejemplo Perú frente a Estados Unidos."),
   ("Tipo de cambio real de equilibrio", r"El nivel del tipo de cambio real que permite a la vez pleno uso de recursos internos y una cuenta corriente sostenible."),
   ("Tipo de cambio real multilateral", r"Promedio del tipo de cambio real frente a los principales socios comerciales, ponderado por cuánto comerciamos con cada uno."))
_v("deuda-publica",
   ("Título de deuda pública", r"Bono o letra que emite el Estado para financiarse; quien lo compra le presta dinero."),
   ("Valores gubernamentales", r"Todos los títulos que emite el gobierno para captar fondos, como bonos soberanos y letras del Tesoro."))
_v("inversion-extranjera-en-cartera",
   ("Títulos de deuda extranjeros", r"Bonos u otros papeles de deuda emitidos por entidades de otros países."))
_v("remesas",
   ("Transferencia", r"Entrega de dinero, bienes o servicios sin recibir nada a cambio, como una remesa o una donación."),
   ("Transferencias corrientes", r"En la balanza de pagos, envíos sin contrapartida que no son de capital, como las remesas familiares o donaciones para gasto."))
_v("dinero",
   ("Unidad monetaria", r"La moneda oficial con que se cuentan los precios en un país; en el Perú, el sol."))
_v("integracion-economica",
   ("Unión económica", r"Etapa de integración en la que, además de libre comercio y libre movimiento de capitales y personas, los países coordinan sus políticas económicas."))
_v("union-monetaria",
   ("Unión Europea", r"Comunidad de países europeos con mercado único y normas comunes; parte de ellos comparte el euro."),
   ("Zona del Euro", r"Los países de la Unión Europea que usan el euro y cuya política monetaria dirige el Banco Central Europeo."),
   ("Zona monetaria", r"Grupo de países que comparten una moneda o fijan sus tipos de cambio entre sí, con libre movimiento de capitales."))
_v("utilidades-retenidas",
   ("Utilidad acumulada", r"Las ganancias de años anteriores que la empresa no repartió y se van sumando."),
   ("Utilidades capitalizadas", r"Ganancias que la empresa pasa formalmente a su capital social en lugar de repartirlas."))
_v("estado-de-resultados",
   ("Utilidad neta", r"Lo que gana la empresa al final, después de restar todos los costos, gastos e impuestos."),
   ("Venta", r"Entrega de un bien o servicio a cambio de dinero; en contabilidad, es el ingreso principal de la empresa."))
_v("renta-de-factores",
   ("Utilidades remitidas", r"Ganancias que empresas extranjeras en el país envían a sus dueños en el exterior."),
   ("Utilidades y dividendos", r"En la balanza de pagos, ganancias que pagan las empresas a sus inversionistas de otro país."))
_v("capitalizacion-bursatil",
   ("Valor de mercado", r"El precio que se obtendría hoy por un bien o título si se vendiera en condiciones normales."))
_v("renta-fija-y-variable",
   ("Valor de renta variable", r"Título, como una acción, cuyo rendimiento no está fijado y depende de cómo le vaya a la empresa."))
_v("fondo-mutuo",
   ("Valor del fondo", r"Lo que vale todo el patrimonio de un fondo mutuo; dividido entre las cuotas da el valor cuota."))
_v("reservas-internacionales",
   ("Valuación", r"Calcular de nuevo el valor de un activo con los precios o tipos de cambio actuales."),
   ("Valuación contable del oro", r"Ganancia o pérdida contable de las reservas por cambios en el precio del oro."))
_v("repo",
   ("Venta temporal de títulos valores", r"Se vende un título con el compromiso de recomprarlo luego a un precio pactado; en la práctica es un préstamo con garantía."))
_v("redescuento",
   ("Ventanilla de descuento", r"Facilidad por la que el banco central presta a los bancos a corto plazo cuando les falta liquidez."))
_v("indice-de-precios-de-exportacion",
   ("Volumen de exportaciones", r"Cuánto se exporta en cantidades físicas, sin el efecto de los precios."),
   ("Volumen de importaciones", r"Cuánto se importa en cantidades físicas, sin el efecto de los precios."))
_v("riesgo-pais",
   ("Vulnerabilidad", r"Qué tan expuesta está una economía a sufrir daño ante un choque externo o interno; cuanto menos vulnerable, menor es la probabilidad de una crisis."))
_v("cuentas-nacionales",
   ("Sociedades no financieras públicas", r"En cuentas nacionales, empresas del Estado que venden bienes o servicios no financieros, como Petroperú o Sedapal."),
   ("Otras sociedades no financieras", r"En cuentas nacionales, empresas privadas que producen bienes o servicios no financieros."),
   ("Gobiernos estatales", r"En países federales, el nivel de gobierno entre el nacional y el local (por ejemplo, los estados de México o Brasil); en el Perú lo más parecido son los gobiernos regionales."))
