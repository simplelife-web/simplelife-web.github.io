#!/usr/bin/env python3
"""Genera las páginas de Trámite fácil Perú en /tramites/."""
import html, json, os, sys

# Uso: python3 .github/tramites/generar.py tramites
OUT = sys.argv[1] if len(sys.argv) > 1 else "tramites"
REV = "10 de noviembre de 2026"
SITE = "https://simplelife-web.github.io/tramites/"
PAGALO = ("Págalo.pe (Banco de la Nación)", "https://pagalo.pe")

T = [
 dict(slug="duplicado-dni", ent="RENIEC", icon="🪪",
  t="Sacar el duplicado de tu DNI electrónico",
  r="Si perdiste tu DNI, te lo robaron o se malogró, pides uno nuevo por internet y lo recoges en la oficina que elijas.",
  quien="Peruanos mayores de 18 años. Si es para un menor de edad, el trámite se hace en una oficina del RENIEC.",
  nec=["Tu número de DNI.", "Un celular con cámara (para la foto de validación).", "Un número de celular y un correo que revises seguido.", "Dinero para pagar el trámite."],
  costo="S/ 33.00", pago="Págalo.pe o Banco de la Nación con el código 00522. También con tarjeta o Yape durante el trámite.",
  pasos=["Entra a la página oficial del duplicado (botón verde de abajo) y acepta los términos.",
         "Valida tu identidad: completa tus datos o usa la app DNI BioFacial, que te toma una foto de la cara.",
         "En los datos de tus padres escribe solo un nombre de cada uno, sin apellidos.",
         "Escribe tu celular y tu correo.",
         "Paga, si no pagaste antes, y elige la oficina del RENIEC donde lo vas a recoger.",
         "Revisa cómo va tu trámite en la página de seguimiento. Cuando diga «al 100 %» y «En agencia», ve a recogerlo."],
  links=[("Pedir el duplicado (RENIEC)", "https://portaladminusuarios.reniec.gob.pe/duplicado/#!/index"),
         ("Ver cómo va tu trámite", "https://serviciosportal.reniec.gob.pe/cetdnipi/inicio.htm"), PAGALO],
  ojo=["Solo tú puedes recogerlo: en la oficina te toman las huellas.", "El DNI nuevo mantiene la misma foto y la misma fecha de caducidad del anterior."],
  src=[("RENIEC, nota del 4 de octubre de 2025", "https://identidad.reniec.gob.pe/b/ahorra-tiempo-renueva-tramita-el-duplicado-o-actualiza-tu-domicilio-de-dnie-de-mayor-de-edad-sin-acudir-a-una-agencia-del-reniec"),
       ("TV Perú, enero de 2026", "https://www.tvperu.gob.pe/noticias/tecnologia/tramite-de-duplicado-del-dni-electronico-online-pasos-para-obtener-el-documento-sin-ir-a-oficinas-reniec")]),

 dict(slug="renovar-dni", ent="RENIEC", icon="🔄",
  t="Renovar tu DNI electrónico desde el celular",
  r="Cuando tu DNI electrónico está por vencer, lo renuevas con una foto desde la app del RENIEC, sin hacer cola.",
  quien="Mayores de 18 años que ya tienen DNI electrónico. Puedes hacerlo desde 60 días antes de que venza.",
  nec=["Tu DNI electrónico.", "Un celular Android con la app DNI BioFacial.", "Una pared blanca y buena luz para la foto.", "Dinero para pagar el trámite."],
  costo="S/ 41.00", pago="En la misma app o en Págalo.pe (Banco de la Nación) con el código 00525.",
  pasos=["Descarga la app DNI BioFacial del RENIEC en tu celular.",
         "Valida tu identidad con una foto de tu cara.",
         "Tómate la foto nueva para el DNI siguiendo las indicaciones de la app.",
         "Paga y elige la oficina donde lo vas a recoger.",
         "Revisa cómo va tu trámite. Cuando diga «al 100 %» y «En agencia», ve a recogerlo. No necesitas cita."],
  links=[("Trámites en línea del RENIEC", "https://www.reniec.gob.pe"),
         ("Ver cómo va tu trámite", "https://serviciosportal.reniec.gob.pe/cetdnipi/inicio.htm"), PAGALO],
  ojo=["Para la foto: fondo blanco, luz natural sin sombras, ropa oscura de un solo color.", "Pide a otra persona que te tome la foto; no uses la cámara para selfis.", "En la web del RENIEC busca la opción «Ahorre tiempo con su trámite en línea»."],
  src=[("RENIEC, nota del 4 de octubre de 2025", "https://identidad.reniec.gob.pe/b/ahorra-tiempo-renueva-tramita-el-duplicado-o-actualiza-tu-domicilio-de-dnie-de-mayor-de-edad-sin-acudir-a-una-agencia-del-reniec")]),

 dict(slug="cambiar-domicilio-dni", ent="RENIEC", icon="🏠",
  t="Cambiar la dirección de tu DNI electrónico",
  r="Si te mudaste, actualizas tu dirección por internet y te dan un DNI nuevo con la dirección correcta.",
  quien="Mayores de 18 años con DNI electrónico.",
  nec=["Tu DNI electrónico.", "La app DNI BioFacial en tu celular.", "Tu nueva dirección completa.", "Los nombres de algunos familiares y su parentesco contigo."],
  costo="S/ 34.00", pago="Págalo.pe con el código 00730, o con tarjeta o Yape durante el trámite.",
  pasos=["Valida tu identidad con la app DNI BioFacial.",
         "Entra a la página oficial de cambio de domicilio (botón verde de abajo).",
         "Llena la declaración jurada con los datos de tus familiares.",
         "Escribe tu nueva dirección y revisa que esté bien.",
         "Elige la oficina donde lo vas a recoger y paga, si no pagaste antes.",
         "Cuando el seguimiento diga «al 100 %» y «En agencia», ve a recogerlo."],
  links=[("Cambiar domicilio (RENIEC)", "https://apps.reniec.gob.pe/domicilio/#!/index"),
         ("Ver cómo va tu trámite", "https://serviciosportal.reniec.gob.pe/cetdnipi/inicio.htm"), PAGALO],
  ojo=["El recojo siempre es en persona."],
  src=[("RENIEC, nota del 4 de octubre de 2025", "https://identidad.reniec.gob.pe/b/ahorra-tiempo-renueva-tramita-el-duplicado-o-actualiza-tu-domicilio-de-dnie-de-mayor-de-edad-sin-acudir-a-una-agencia-del-reniec")]),

 dict(slug="partida-nacimiento", ent="RENIEC", icon="📄",
  t="Sacar una copia de tu partida de nacimiento",
  r="Descargas en PDF la copia certificada de tu acta de nacimiento, matrimonio o defunción, sin ir a una oficina.",
  quien="Mayores de edad. El acta de un menor solo la puede pedir su papá o su mamá, con su DNI.",
  nec=["Tu DNI.", "Una computadora o laptop (mejor si tiene impresora).", "Los datos de la persona del acta."],
  costo="S/ 10.30", pago="Págalo.pe (Banco de la Nación), concepto «Copias certificadas de actas vía Internet», código 02141. Se paga con el DNI de quien lo pide.",
  pasos=["Entra a la web del RENIEC y busca «Solicitar copia certificada o partida Reniec».",
         "Elige «Verifica acta/partida» y escribe los datos de la persona.",
         "Si aparece «Acta ubicada en Reniec», paga el trámite.",
         "Descarga el PDF o imprímelo."],
  links=[("Trámites de actas (RENIEC)", "https://identidad.reniec.gob.pe/tramites"), PAGALO],
  ojo=["Primero verifica que el acta esté en el RENIEC y recién después paga.", "Si el acta no está, pídela en la municipalidad donde se registró (o en Cancillería si fue en un consulado).", "Esta copia sirve solo para trámites dentro del Perú. Para Cancillería, pídela en una oficina del RENIEC.", "Si es un acta de defunción, se paga con el DNI de quien la pide, no con el de la persona fallecida."],
  src=[("RENIEC, nota del 22 de septiembre de 2025", "https://identidad.reniec.gob.pe/b/obten-copias-de-actas-sin-ir-a-una-agencia-del-reniec")]),

 dict(slug="sacar-ruc", ent="SUNAT", icon="🧾",
  t="Sacar tu RUC como persona natural",
  r="El RUC es tu número de contribuyente. Lo necesitas para dar recibos por honorarios, alquilar algo, vender un inmueble o empezar un negocio.",
  quien="Cualquier persona con DNI que todavía no tenga RUC.",
  nec=["Tu DNI.", "La app Personas SUNAT en tu celular.", "Si vas a tener un negocio, saber qué régimen tributario te conviene."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Revisa que todavía no tengas RUC (en «Consulta RUC»).",
         "Abre la app Personas SUNAT o la página de inscripción virtual.",
         "Escribe tu DNI y elige el motivo (por ejemplo, prestar servicios).",
         "Valida tu identidad con tu huella dactilar, como te indique la app.",
         "En el mismo trámite crea tu Clave SOL. Guárdala bien."],
  links=[("Inscripción en el RUC (gob.pe)", "https://www.gob.pe/284-inscripcion-en-el-ruc"),
         ("Inscripción virtual (SUNAT)", "https://www.sunat.gob.pe/a/html/contribuyente2/registro/adminforuc/registroruc/informativo.html"),
         ("Consulta RUC", "https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias")],
  ojo=["La SUNAT tiene una guía para que la huella se lea bien: «Instructivo de lectura de huella dactilar».", "Si no sabes qué régimen elegir, revisa el folleto de regímenes tributarios de la SUNAT."],
  src=[("SUNAT, Orientación: Inscríbete en el RUC", "https://orientacion.sunat.gob.pe/1097-0-inscribete-en-el-ruc")]),

 dict(slug="clave-sol", ent="SUNAT", icon="🔑",
  t="Obtener o recuperar tu Clave SOL",
  r="La Clave SOL es tu usuario y contraseña de la SUNAT. Con ella emites recibos por honorarios, declaras y haces trámites en línea.",
  quien="Personas que ya tienen RUC.",
  nec=["Tu DNI vigente.", "Para hacerlo por internet: tu correo y tu celular actualizados en tu ficha RUC."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a la página de la SUNAT o abre la app Personas SUNAT.",
         "Elige «Obtener clave SOL».",
         "Escribe tu DNI y sigue las indicaciones.",
         "Si no puedes por internet, ve a un Centro de Servicios al Contribuyente de la SUNAT con tu DNI original."],
  links=[("Obtener Clave SOL (SUNAT)", "https://ww1.sunat.gob.pe/ol-ti-itadminforuc-inscripcion/inscripcion"),
         ("Guía de la SUNAT", "https://orientacion.sunat.gob.pe/6614-02-requisitos-para-obtener-la-clave-sol")],
  ojo=["Si otra persona hace el trámite por ti en la oficina, necesita una solicitud con tu firma legalizada por notario.", "Nunca le des tu Clave SOL a nadie que te la pida por teléfono o mensaje."],
  src=[("SUNAT, Orientación: Requisitos para obtener la Clave SOL", "https://orientacion.sunat.gob.pe/6614-02-requisitos-para-obtener-la-clave-sol")]),

 dict(slug="antecedentes-policiales", ent="PNP", icon="👮",
  t="Sacar tu certificado de antecedentes policiales",
  r="Documento que dice si tienes o no antecedentes en la Policía. Te lo suelen pedir para trabajar.",
  quien="La persona interesada. También su cónyuge, conviviente o un familiar directo, con su autorización.",
  nec=["Tu DNI.", "El comprobante de pago.", "Un correo electrónico."],
  costo="S/ 5.40", pago="Banco de la Nación con el código 08116, o Págalo.pe.",
  pasos=["Paga la tasa.",
         "Entra a la página oficial del trámite (botón verde de abajo).",
         "Acepta los términos y escribe los datos de tu comprobante de pago.",
         "Escribe tus datos y elige para qué lo necesitas.",
         "Valida tu identidad.",
         "Descarga tu certificado en PDF."],
  links=[("Antecedentes policiales (gob.pe)", "https://www.gob.pe/309-certificado-de-antecedentes-policiales-para-uso-nacional"), PAGALO],
  ojo=["El certificado vale 90 días desde que se emite."],
  verif="Costo y código según la ficha oficial citada por Infobae en septiembre de 2026. Confírmalo en la página oficial antes de pagar.",
  src=[("Infobae, 21 de septiembre de 2026", "https://www.infobae.com/peru/2026/09/21/antecedentes-penales-policiales-y-judiciales-como-sacar-cada-certificado-por-internet-en-peru-requisitos-y-precios/")]),

 dict(slug="antecedentes-penales", ent="Poder Judicial", icon="⚖️",
  t="Sacar tu certificado de antecedentes penales",
  r="Documento del Poder Judicial que dice si tienes o no condenas. Lo piden para trabajar, estudiar o viajar.",
  quien="La persona interesada, con su DNI.",
  nec=["Tu DNI.", "El pago del trámite."],
  costo="S/ 52.80 (referencial)", pago="Págalo.pe, tarjeta u otros medios que indique el Poder Judicial.",
  pasos=["Paga la tasa.",
         "Entra a la página oficial del trámite (botón verde de abajo).",
         "Escribe los datos que te pide.",
         "Valida tu identidad.",
         "Espera la respuesta y descarga tu certificado."],
  links=[("Antecedentes penales (gob.pe)", "https://www.gob.pe/326-antecedentes-penales"), PAGALO],
  ojo=["Si tu trámite sale «observado», tienes que ir a la sede que te indiquen con tu DNI.", "El Poder Judicial advirtió que hay personas que venden este certificado de forma irregular. Sácalo solo en la página oficial."],
  verif="Costo según el Poder Judicial, citado por Infobae en septiembre de 2026. Confírmalo en la página oficial antes de pagar.",
  src=[("Infobae, 21 de septiembre de 2026", "https://www.infobae.com/peru/2026/09/21/antecedentes-penales-policiales-y-judiciales-como-sacar-cada-certificado-por-internet-en-peru-requisitos-y-precios/"),
       ("Poder Judicial, alerta de febrero de 2025", "https://pj.gob.pe/wps/wcm/connect/cortesuprema/s_cortes_suprema_home/as_inicio/as_enlaces_destacados/as_imagen_prensa/as_notas_noticias/2025/cs_n-personas-ofrecen-certificado-de-antecedentes-penales-18022025")]),

 dict(slug="certificado-unico-laboral", ent="Ministerio de Trabajo", icon="💼",
  t="Sacar tu Certificado Único Laboral (CUL)",
  r="Un solo documento gratis que junta tus datos de identidad, antecedentes, estudios y experiencia laboral. Sirve para postular a un trabajo.",
  quien="Personas con DNI que buscan trabajo.",
  nec=["Tu DNI.", "Un correo electrónico.", "Una cuenta en Empleos Perú (se crea gratis)."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a la página de Empleos Perú (botón verde de abajo).",
         "Inicia sesión o crea tu cuenta con tu DNI y tu correo.",
         "Elige la opción para generar el Certificado Único Laboral.",
         "Espera a que el sistema revise tus datos.",
         "Descarga tu certificado en PDF."],
  links=[("Obtener el CUL (gob.pe)", "https://www.gob.pe/47089-obtener-tu-certificado-unico-laboral-cul"),
         ("Empleos Perú", "https://www.empleosperu.gob.pe/CertificadoUnicoLaboral/")],
  ojo=["Reemplaza al antiguo CertiJoven y CertiAdulto.", "Si te cobran por sacarlo, desconfía: es gratis."],
  verif="Datos del Ministerio de Trabajo (gob.pe). Algunas páginas oficiales no se pudieron abrir para esta revisión; confirma los pasos en el enlace oficial.",
  src=[("Ministerio de Trabajo, ficha en gob.pe", "https://www.gob.pe/47089-obtener-tu-certificado-unico-laboral-cul")]),

 dict(slug="pasaporte", ent="Migraciones", icon="🛂",
  t="Sacar tu pasaporte electrónico",
  r="Documento para viajar fuera del país. Desde 2026 ya no es obligatorio sacar cita por internet.",
  quien="Peruanos con DNI vigente.",
  nec=["Tu DNI vigente y en buen estado.", "El comprobante de pago."],
  costo="S/ 120.90", pago="Yape, Banco de la Nación o Págalo.pe con el código 01810.",
  pasos=["Paga la tasa del pasaporte.",
         "Ve a cualquier sede de Migraciones con tu DNI y tu comprobante.",
         "Te atienden por orden de llegada y te dan una cita en el momento.",
         "Puedes recibir tu pasaporte el mismo día."],
  links=[("Migraciones (gob.pe)", "https://www.gob.pe/institucion/migraciones"), PAGALO],
  ojo=["Ve temprano: la atención es por orden de llegada."],
  verif="Según el anuncio de Migraciones publicado por TV Perú el 19 de mayo de 2026. Confirma en Migraciones antes de ir.",
  src=[("TV Perú, 19 de mayo de 2026", "https://tvperu.gob.pe/noticias/nacionales/migraciones-eliminara-citas-virtuales-y-facilitara-tramite-de-pasaporte-electronico")]),

 dict(slug="licencia-funcionamiento", ent="Municipalidad", icon="🏪",
  t="Sacar la licencia de funcionamiento de tu negocio",
  r="Permiso de tu municipalidad para abrir una tienda, un taller u otro local. Cada municipalidad pone su costo, pero la ley fija lo máximo que te pueden pedir.",
  quien="Personas o empresas que van a abrir un local. Necesitas RUC.",
  nec=["Una solicitud con carácter de declaración jurada, con tu RUC y tu DNI.",
       "Si es una empresa: la vigencia de poder del representante legal.",
       "La declaración jurada de condiciones de seguridad o la inspección técnica que corresponda.",
       "Solo en algunos casos: título profesional, autorización del sector o del Ministerio de Cultura."],
  costo="Depende de tu municipalidad", pago="Lo indica tu municipalidad en su TUPA (la lista oficial de trámites y costos).",
  pasos=["Saca tu RUC si todavía no lo tienes.",
         "Busca tu municipalidad en gob.pe y revisa el trámite «licencia de funcionamiento».",
         "Prepara los documentos de la lista.",
         "Presenta tu solicitud en la municipalidad o por su mesa de partes virtual.",
         "La municipalidad tiene como máximo 15 días hábiles para responder. Si no responde, se entiende aprobada (silencio positivo)."],
  links=[("Buscar el trámite en gob.pe", "https://www.gob.pe/busquedas?term=licencia+de+funcionamiento"),
         ("Ley 28976 (texto)", "https://www.miraflores.gob.pe/Gestorw3b/files/pdf/5055-466-leylicenciafuncionamiento.pdf")],
  ojo=["La licencia no vence: tiene vigencia indeterminada.", "La municipalidad no puede pedirte más requisitos que los de la ley."],
  verif="Requisitos generales de la Ley Marco de Licencia de Funcionamiento (Ley 28976). Tu municipalidad puede tener detalles propios; revisa su TUPA.",
  src=[("Ley 28976, Ley Marco de Licencia de Funcionamiento", "https://www.miraflores.gob.pe/Gestorw3b/files/pdf/5055-466-leylicenciafuncionamiento.pdf")]),
]

# ---------- Tanda 2 (11/11/2026) ----------
N = dict(rev="11 de noviembre de 2026", mod="2026-11-11")
T += [
 dict(N, slug="licencia-conducir", ent="MTC", icon="🚗",
  t="Sacar tu brevete (licencia A-I) por primera vez",
  r="La licencia A-I es el brevete para manejar autos particulares. Para sacarla apruebas un examen médico, uno de reglas de tránsito y uno de manejo.",
  quien="Personas mayores de 18 años.",
  nec=["Tu DNI.", "Aprobar el examen médico en un centro autorizado por el MTC.", "Aprobar el examen de reglas de tránsito (40 preguntas; necesitas 35 buenas).", "Aprobar el examen práctico de manejo (con cita)."],
  costo="S/ 14.70 la licencia física (S/ 6.70 la electrónica)", pago="Págalo.pe, Banco de la Nación o el portal del MTC. En Lima, el examen de reglas cuesta aparte S/ 74.80, con dos intentos. El examen médico también se paga aparte.",
  pasos=["Haz el examen médico en un centro autorizado. El resultado llega solo al sistema del MTC.",
         "Estudia y da el examen de reglas de tránsito.",
         "Saca cita para el examen de manejo. En Lima se pide en la web o por teléfono al Touring; en regiones, con la dirección de transporte de tu región.",
         "Cuando apruebes, paga la licencia y pide que te la emitan (física o electrónica)."],
  links=[("Trámites de licencias (MTC)", "https://licencias-tramite.mtc.gob.pe/frmAcuerdo.aspx"),
         ("Centros médicos autorizados", "https://rec.mtc.gob.pe/LicenciaConducir/ArCentroMedicoConfiguracion"), PAGALO],
  ojo=["La primera licencia dura 10 años.", "Paga siempre a nombre de la entidad. El MTC advierte que no se paga a cuentas personales ni por Yape o Plin.", "Consultas al MTC: (01) 615 7900, de lunes a viernes."],
  verif="Costos de Lima según el MTC, citados por Infobae en marzo de 2026. En regiones pueden variar.",
  src=[("Infobae, 11 de marzo de 2026", "https://www.infobae.com/peru/2026/03/11/mtc-y-tu-primera-licencia-de-conducir-todo-lo-que-debes-saber-para-empezar-a-manejar-en-peru/")]),

 dict(N, slug="revalidar-licencia", ent="MTC", icon="🔁",
  t="Revalidar (renovar) tu brevete A-I",
  r="Cuando tu brevete está por vencer o ya venció, lo revalidas para seguir manejando. Para la A-I no necesitas volver a dar el examen de reglas.",
  quien="Personas con brevete vencido o por vencer, sin multas pendientes ni licencia suspendida o retenida.",
  nec=["Tu DNI.", "Tu brevete vencido o por vencer.", "Aprobar un nuevo examen médico en un centro autorizado."],
  costo="S/ 6.70 electrónica o S/ 14.70 física", pago="Banco de la Nación o Págalo.pe (código 1601 para la electrónica y 1602 para la física).",
  pasos=["Haz el examen médico en un centro autorizado.",
         "Paga la tasa.",
         "En Lima puedes hacerlo por internet: entra al portal de licencias del MTC, elige «Revalidación», escribe tu DNI y elige dónde recogerla.",
         "Si no, ve a un Centro de Emisión de Licencias con tu DNI y tu brevete anterior.",
         "Recoge tu licencia."],
  links=[("Trámites de licencias (MTC)", "https://licencias-tramite.mtc.gob.pe/frmAcuerdo.aspx"),
         ("Centros médicos autorizados", "https://rec.mtc.gob.pe/LicenciaConducir/ArCentroMedicoConfiguracion"), PAGALO],
  ojo=["Sin el examen médico aprobado, el sistema no te deja revalidar por internet.", "Manejar con el brevete vencido tiene multa.", "Entre los 75 y 81 años, la A-I se revalida cada 3 años."],
  verif="Pasos y códigos de pago según la Agencia Andina (mayo de 2023). Los costos coinciden con los informados por el MTC en 2026. Confírmalos antes de pagar.",
  src=[("Andina, 22 de mayo de 2023", "https://andina.pe/agencia/noticia-vencio-tu-licencia-conducir-conoce-paso-a-paso-como-revalidarla-908603.aspx"),
       ("Infobae, 11 de marzo de 2026", "https://www.infobae.com/peru/2026/03/11/mtc-y-tu-primera-licencia-de-conducir-todo-lo-que-debes-saber-para-empezar-a-manejar-en-peru/")]),

 dict(N, slug="consulta-vehicular", ent="SUNARP", icon="🔎",
  t="Ver los datos de un auto con su placa",
  r="Antes de comprar un auto usado, escribe su placa y mira quién es el dueño, el color, la marca, el motor y si tiene reporte de robo.",
  quien="Cualquier persona.",
  nec=["El número de placa del vehículo."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a la Consulta Vehicular de la SUNARP (botón verde de abajo) o abre la app SUNARP.",
         "Escribe la placa.",
         "Revisa los datos: dueño, serie, motor, color, marca, modelo y si tiene anotación de robo.",
         "Compara con la tarjeta de propiedad que te muestran. Si algo no coincide, no compres y avisa a la Policía."],
  links=[("Consulta Vehicular (SUNARP)", "https://www.sunarp.gob.pe/ConsultaVehicular/ConsultaPlaca")],
  ojo=["Funciona las 24 horas, todos los días."],
  src=[("El Peruano, 25 de junio de 2021", "https://www.elperuano.pe/noticia/123382-servicio-gratuito-de-consulta-vehicular-de-la-sunarp-contribuye-con-la-prevencion-de-robos-y-estafas")]),

 dict(N, slug="vehiculos-a-mi-nombre", ent="SUNARP", icon="🚙",
  t="Ver qué vehículos están a tu nombre",
  r="Revisa si aparece algún carro o moto a tu nombre que ya vendiste, que te robaron o que no conoces.",
  quien="Personas con DNI o carné de extranjería.",
  nec=["Tu DNI o carné de extranjería."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a «Vehículos a mi nombre» (botón verde de abajo).",
         "Valida tu identidad con tu documento.",
         "Revisa la lista. Tienes 30 minutos por sesión.",
         "Si aparece un vehículo que ya vendiste, formaliza la transferencia. Si no lo reconoces, busca asesoría legal."],
  links=[("Vehículos a mi nombre (SUNARP)", "https://vehiculosaminombre.sunarp.gob.pe")],
  ojo=["No necesitas instalar nada.", "Si vendiste un auto y sigue a tu nombre, podrías recibir sus multas."],
  src=[("Andina, 29 de abril de 2026", "https://andina.pe/agencia/noticia-minjusdh-lanza-servicio-digital-gratuito-permite-consultar-vehiculos-registrados-1073206.aspx")]),

 dict(N, slug="alerta-registral", ent="SUNARP", icon="🔔",
  t="Proteger tu casa o tu auto con la Alerta Registral",
  r="La SUNARP te avisa por correo si alguien presenta un trámite sobre tu propiedad. Así puedes reaccionar a tiempo ante un fraude.",
  quien="Cualquier persona con propiedades inscritas en la SUNARP.",
  nec=["Tu DNI.", "Un correo electrónico.", "El número de partida de tu inmueble o la placa de tu vehículo."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a Alerta Registral (botón verde de abajo) y regístrate.",
         "Confirma tu cuenta desde tu correo.",
         "Agrega las partidas o placas que quieres vigilar.",
         "Si te llega una alerta de un trámite que no hiciste, acude a la SUNARP de inmediato."],
  links=[("Alerta Registral (SUNARP)", "https://alertaregistral.sunarp.gob.pe")],
  ojo=["Es ideal para personas mayores o para propiedades que no se usan seguido."],
  verif="Los pasos de registro son un resumen; sigue las indicaciones de la página oficial.",
  src=[("El Peruano, 12 de octubre de 2026", "https://elperuano.pe/noticia/306649-temes-perder-tu-patrimonio-sunarp-ofrece-alertas-gratuitas-para-vigilar-tus-partidas-registrales")]),

 dict(N, slug="constancia-grados", ent="SUNEDU", icon="🎓",
  t="Sacar la constancia de tu grado o título universitario",
  r="Documento oficial que prueba que tu bachiller o título está inscrito en la SUNEDU. Te lo piden en trabajos y concursos.",
  quien="Personas con grado o título inscrito en el Registro Nacional de Grados y Títulos.",
  nec=["Tu DNI.", "Un correo electrónico.", "El número de operación de tu pago."],
  costo="S/ 10.00", pago="Págalo.pe. Guarda el número de secuencia y la fecha del pago.",
  pasos=["Primero revisa gratis en SUNEDU en Línea que tu grado aparezca inscrito.",
         "Paga en Págalo.pe.",
         "Entra a SUNEDU en Línea y elige «Solicita tu constancia de inscripción».",
         "Escribe tu documento, elige el grado o título (uno por trámite) y los datos del pago.",
         "La constancia llega a tu correo."],
  links=[("SUNEDU en Línea", "https://enlinea.sunedu.gob.pe/"), PAGALO],
  ojo=["Si tu grado no aparece, tu universidad tiene que enviar sus datos a la SUNEDU."],
  src=[("SUNEDU, guía de la constancia de inscripción 2026", "https://enlinea.sunedu.gob.pe/Documents/guia-constancia-de-inscripcion-2026-v01.pdf")]),

 dict(N, slug="certificado-estudios", ent="MINEDU", icon="🏫",
  t="Descargar tu certificado de estudios del colegio",
  r="Descarga gratis tu certificado oficial de primaria o secundaria desde la web del Ministerio de Educación.",
  quien="El exalumno, o su papá, mamá o apoderado.",
  nec=["El DNI del estudiante o de quien lo pide."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a la página de certificados del MINEDU (botón verde de abajo).",
         "Revisa que tu colegio aparezca habilitado para el trámite por internet.",
         "Escribe los datos que te piden.",
         "Descarga e imprime tu certificado."],
  links=[("Certificado de estudios (MINEDU)", "https://certificado.minedu.gob.pe"),
         ("Trámite en gob.pe", "https://www.gob.pe/11745-obtener-primera-emision-o-duplicado-del-certificado-oficial-de-estudios-desde-el-ano-1986")],
  ojo=["Si terminaste antes de 1985, o tu colegio cerró o no aparece, haz el trámite en tu UGEL o en el colegio."],
  src=[("Andina, 1 de diciembre de 2022", "https://andina.pe/agencia/noticia-atencion-sepa-como-obtener-gratis-certificado-estudios-escolares-919936.aspx")]),

 dict(N, slug="afiliarse-sis", ent="SIS", icon="🏥",
  t="Afiliarte al SIS (seguro de salud gratuito)",
  r="Si no tienes ningún seguro de salud, puedes afiliarte al SIS sin pagar y atenderte en los centros de salud del Estado.",
  quien="Peruanos con DNI y extranjeros con carné de extranjería que vivan en el Perú y no tengan otro seguro. No hay límite de edad.",
  nec=["Tu DNI o carné de extranjería.", "Un correo electrónico (para la afiliación por internet)."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Primero revisa si ya estás afiliado (botón «Consultar si tienes SIS»).",
         "Si no tienes seguro, entra a gob.pe/sis y busca la afiliación virtual, o usa la app del SIS.",
         "Llena tus datos y confirma el código que llega a tu correo.",
         "Espera la respuesta en tu correo.",
         "También puedes afiliarte en el centro de salud más cercano."],
  links=[("SIS (gob.pe)", "https://www.gob.pe/sis"),
         ("Consultar si tienes SIS", "http://www.sis.gob.pe/sisERP/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx"),
         ("Consultar si tienes EsSalud", "http://ww4.essalud.gob.pe:7779/acredita/")],
  ojo=["Central del SIS: (01) 514 5555.", "Si tienes EsSalud u otro seguro, no puedes tener SIS a la vez."],
  verif="Las fuentes son de 2021 y 2022; los canales pueden haber cambiado. Confírmalos en gob.pe/sis.",
  src=[("TV Perú, 21 de noviembre de 2022", "https://tvperu.gob.pe/noticias/nacionales/sis-no-hay-limite-de-edad-y-en-cualquier-momento-se-puede-afiliar-para-gozar-de-cobertura-de-salud"),
       ("Andina, 15 de marzo de 2021", "https://andina.pe/agencia/noticia-sis-crea-aplicativo-para-te-asegures-manera-rapida-y-sencilla-837022.aspx"),
       ("SIS, preguntas frecuentes", "http://www.sis.gob.pe/Portal/paginas/preguntas.html")]),

 dict(N, slug="pension-65", ent="MIDIS", icon="👵",
  t="Pedir Pensión 65 para un adulto mayor",
  r="Pensión 65 da S/ 350 cada dos meses a adultos mayores en pobreza extrema que no reciben otra pensión.",
  quien="Personas de más de 65 años, con DNI, sin pensión de la ONP, AFP ni EsSalud, y cuyo hogar esté clasificado como pobre extremo en el SISFOH.",
  nec=["DNI del adulto mayor.", "La clasificación socioeconómica del hogar (la da la municipalidad).", "La declaración jurada (Formulario 1000), firmada o con huella."],
  costo="Gratis", pago="El trámite no cuesta nada.",
  pasos=["Ve a la Unidad Local de Empadronamiento (ULE) de tu municipalidad distrital y pide la clasificación socioeconómica.",
         "Personal de la municipalidad visita la casa del adulto mayor.",
         "Con la clasificación lista, presenta en la municipalidad el Formulario 1000.",
         "Si es aceptado, cobra con la tarjeta del programa en el Banco de la Nación o en cajeros Multired."],
  links=[("Pensión 65 (gob.pe)", "https://www.gob.pe/pension65"),
         ("Formulario 1000", "https://www.pension65.gob.pe/wp-content/uploads/Formulario-1000.pdf")],
  ojo=["Nadie puede cobrarte por inscribirte.", "Consultas: WhatsApp o teléfono 942 962 116."],
  src=[("Andina, 11 de febrero de 2025", "https://andina.pe/agencia/noticia-pension-65-requisitos-se-necesitan-para-ser-parte-del-programa-social-del-midis-1018323.aspx"),
       ("El Peruano, octubre de 2026 (monto)", "https://elperuano.pe/noticia/305994-pension-65-mas-de-824000-usuarios-cobraran-s-350-desde-el-5-de-octubre")]),

 dict(N, slug="aportes-onp", ent="ONP", icon="📊",
  t="Ver tus aportes a la ONP",
  r="Revisa si tu empleador pagó todos tus aportes al Sistema Nacional de Pensiones. Te sirve para tu futura jubilación.",
  quien="Trabajadores y extrabajadores que aportan o aportaron a la ONP.",
  nec=["Tu DNI.", "Tu clave virtual de la ONP (la pides gratis en la misma web)."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a ONP Virtual y elige «Tu zona segura».",
         "Si no tienes clave, elige «Quiero mi clave virtual».",
         "Entra con tu DNI y tu clave y elige «Estado de cuenta en línea».",
         "Descarga tu reporte y compáralo con tus boletas de pago.",
         "Sin internet: llama al (01) 634 2222, opción 1, y te envían el reporte al correo."],
  links=[("ONP Virtual", "https://onpvirtual.pe")],
  ojo=["Si faltan meses, pide a tu empleador que lo regularice.", "Si tus aportes fueron por error a una AFP, también se puede corregir."],
  src=[("El Peruano, 20 de octubre de 2026", "https://elperuano.pe/noticia/307207-tu-empleador-registro-todos-tus-aportes-la-onp-explica-como-comprobarlo-en-minutos")]),

 dict(N, slug="recibo-honorarios", ent="SUNAT", icon="🧑‍💻",
  t="Emitir un recibo por honorarios electrónico",
  r="Si trabajas por tu cuenta, el recibo por honorarios es el comprobante que entregas a quien te paga. Se hace gratis en la web de la SUNAT.",
  quien="Personas con RUC y Clave SOL que dan servicios como independientes.",
  nec=["Tu RUC y tu Clave SOL.", "El RUC o DNI de quien te paga.", "La descripción del servicio y el monto."],
  costo="Gratis", pago="No se paga nada por emitirlo.",
  pasos=["Entra a sunat.gob.pe, ve a «Mis Trámites y Consultas» e ingresa con tu Clave SOL.",
         "Elige «Emisión de Recibos por Honorarios Electrónicos».",
         "Indica si corresponde retención del impuesto (SÍ o NO).",
         "Escribe el RUC o DNI de quien te paga y valida.",
         "Describe el servicio, el monto, la moneda y la fecha.",
         "Revisa todo y pulsa «Emitir Recibo»."],
  links=[("SUNAT Operaciones en Línea", "https://www.sunat.gob.pe"),
         ("Guía de la SUNAT (PDF)", "https://orientacion.sunat.gob.pe/sites/default/files/inline-files/Recibo_honorarios%20web_2.pdf")],
  ojo=["También puedes emitirlo desde la app Personas SUNAT.", "Si aún no tienes RUC, mira la guía «Sacar tu RUC como persona natural»."],
  src=[("SUNAT, guía para emitir el recibo por honorarios", "https://orientacion.sunat.gob.pe/sites/default/files/inline-files/Recibo_honorarios%20web_2.pdf")]),

 dict(N, slug="suspension-cuarta", ent="SUNAT", icon="✂️",
  t="Pedir que no te descuenten el 8 % de tus recibos por honorarios",
  r="Es la «suspensión de retenciones de cuarta categoría». Si tus ingresos del año no pasan el límite, evitas que te retengan el 8 %.",
  quien="En 2026: independientes que proyectan ganar hasta S/ 48 125 en el año. Directores, síndicos o albaceas: hasta S/ 38 500.",
  nec=["Tu RUC y tu Clave SOL.", "La fecha de tu primer ingreso del año.", "Cuánto calculas ganar en el año."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a SUNAT Operaciones en Línea con tu Clave SOL, en «Mis trámites y consultas».",
         "Ve a «Otras declaraciones y solicitudes» y elige «Solicito Suspensión de Retenciones 4ta Categoría» (Formulario 1609).",
         "Escribe la fecha de tu primer ingreso y el monto que proyectas para el año.",
         "Si procede, la SUNAT te da una constancia. Envíala a quien te paga."],
  links=[("SUNAT Operaciones en Línea", "https://www.sunat.gob.pe"),
         ("Información de la SUNAT", "https://personas.sunat.gob.pe/trabajador-independiente/suspension-retenciones")],
  ojo=["Vale desde el día siguiente y hasta el 31 de diciembre. Se pide cada año.", "Si en un mes pasas el límite, desde ese mes declaras y pagas a cuenta."],
  src=[("El Peruano, enero de 2026", "https://www.elperuano.pe/noticia/286631-ganas-hasta-s-4-010-al-mes-revisa-si-puedes-suspender-el-impuesto-a-la-renta-en-2026")]),

 dict(N, slug="movimiento-migratorio", ent="Migraciones", icon="✈️",
  t="Sacar tu certificado de movimiento migratorio",
  r="Muestra tus entradas y salidas del Perú. Lo piden para visas, trámites de residencia o juicios.",
  quien="La persona interesada, o un tercero con el pago a nombre de quien hace el trámite.",
  nec=["Tu DNI, carné de extranjería o pasaporte.", "Un correo electrónico.", "El comprobante de pago."],
  costo="S/ 15.10", pago="Banco de la Nación o Págalo.pe con el código 07561.",
  pasos=["Paga la tasa.",
         "Entra a la Agencia Digital de Migraciones y escribe tus datos.",
         "Elige «Certificados», luego «Movimiento migratorio» y si es personal o para otra persona.",
         "Escribe los códigos de tu comprobante de pago.",
         "Descarga el certificado. También llega a tu correo."],
  links=[("Agencia Digital Migraciones", "https://agenciavirtual.migraciones.gob.pe/agencia-virtual/identidad"), PAGALO],
  ojo=["El pago debe estar a nombre de quien entra a la plataforma.", "Migraciones recomienda no contratar tramitadores."],
  src=[("Andina, 1 de agosto de 2025", "https://andina.pe/agencia/noticia-como-tramitar-certificado-movimiento-migratorio-virtualmente-aqui-te-contamos-1039434.aspx")]),

 dict(N, slug="antecedentes-judiciales", ent="INPE", icon="🏛️",
  t="Sacar tu certificado de antecedentes judiciales",
  r="Documento del INPE que dice si estuviste o no en un penal. A veces lo piden junto con los antecedentes penales y policiales.",
  quien="Peruanos con DNI. Si naciste en el extranjero o eres extranjero, el trámite es presencial.",
  nec=["Tu DNI.", "El comprobante de pago.", "Un correo electrónico."],
  costo="S/ 37.70 (referencial)", pago="Banco de la Nación, agentes Multired o Págalo.pe.",
  pasos=["Paga el derecho de trámite.",
         "Entra a la plataforma de antecedentes judiciales y valida tu pago.",
         "Regístrate.",
         "Espera tu usuario y contraseña en tu correo (unos 30 minutos).",
         "Entra y descarga tu certificado."],
  links=[("Antecedentes judiciales (gob.pe)", "https://www.gob.pe/305-solicitar-antecedentes-judiciales"), PAGALO],
  ojo=["Revisa si de verdad te lo piden: muchas veces basta con el Certificado Único Laboral, que es gratis."],
  verif="Costo según el INPE, citado por Infobae en septiembre de 2026. Confírmalo antes de pagar.",
  src=[("Infobae, 21 de septiembre de 2026", "https://www.infobae.com/peru/2026/09/21/antecedentes-penales-policiales-y-judiciales-como-sacar-cada-certificado-por-internet-en-peru-requisitos-y-precios/")]),
]

ORDEN = ["RENIEC", "SUNAT", "MTC", "SUNARP", "Migraciones", "PNP", "Poder Judicial", "INPE",
         "Ministerio de Trabajo", "SIS", "ONP", "MIDIS", "MINEDU", "SUNEDU", "Municipalidad"]
ETIQ = {"RENIEC": "DNI y actas", "SUNAT": "Impuestos", "MTC": "Brevete", "SUNARP": "Propiedades y autos",
        "Migraciones": "Viajes", "PNP": "Antecedentes", "Poder Judicial": "Antecedentes", "INPE": "Antecedentes",
        "Ministerio de Trabajo": "Trabajo", "SIS": "Salud", "ONP": "Pensiones", "MIDIS": "Pensiones",
        "MINEDU": "Estudios", "SUNEDU": "Estudios", "Municipalidad": "Negocios"}
GRUPOS = ["DNI y actas", "Impuestos", "Brevete", "Propiedades y autos", "Viajes", "Antecedentes",
          "Trabajo", "Salud", "Pensiones", "Estudios", "Negocios"]
T.sort(key=lambda d: (GRUPOS.index(ETIQ[d["ent"]]), ORDEN.index(d["ent"])))

e = html.escape
BASE = "https://simplelife-web.github.io/"
ORG = {"@type": "Organization", "name": "Simplelife", "url": BASE, "logo": BASE + "logo.svg", "email": "simplelifecontacto899@gmail.com"}

def jl(o):
    return json.dumps(o, ensure_ascii=False, separators=(",", ":"))

def head(title, desc, canon, ld):
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<link rel="icon" href="../logo.svg" type="image/svg+xml">
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:image" content="https://simplelife-web.github.io/og-imagen.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="es_PE">
<script type="application/ld+json">
{jl(ld)}
</script>
<meta property="og:title" content="{e(title)}">
<meta property="og:site_name" content="Simplelife">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9798339025422593"
     crossorigin="anonymous"></script>
<link rel="stylesheet" href="estilo.css">
<script src="letra.js"></script>
</head>
<body>
<a class="saltar" href="#contenido">Ir al contenido</a>
<script src="../nav.js"></script>
<header class="top">
  <span class="brand"><a class="hoja" href="../" title="Ir al inicio de Simplelife"><img src="../logo.svg" alt="Inicio Simplelife" width="48" height="48"></a><a class="brand-txt" href="../" title="Ir al inicio de Simplelife"><span>Trámite <b>fácil</b><small>Perú · de Simplelife</small></span></a></span>
  <div class="letra" role="group" aria-label="Tamaño de letra">
    <button type="button" data-letra="-1" aria-label="Letra más pequeña">A−</button>
    <button type="button" data-letra="1" aria-label="Letra más grande">A+</button>
  </div>
</header>
<main id="contenido">
'''

FOOT = '''</main>
<footer>
  <p><strong>Trámite fácil Perú</strong> no es una página del Estado. Explicamos los trámites con palabras sencillas y te llevamos a las páginas oficiales. Los costos y requisitos pueden cambiar: confírmalos siempre en el enlace oficial antes de pagar.</p>
  <p>Nunca te pediremos dinero ni datos personales. Paga solo en las páginas oficiales o en el Banco de la Nación.</p>
  <p><a href="./">Todos los trámites</a> · <a href="../">Inicio Simplelife</a> · <a href="../transcriptor/">Transcriptor de audio</a> · <a href="../acerca.html">Acerca de</a> · <a href="../contacto.html">Contacto</a> · <a href="../privacidad.html">Privacidad</a></p>
</footer>
</body>
</html>
'''

def crumbs(extra=None):
    l = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE},
         {"@type": "ListItem", "position": 2, "name": "Trámite fácil Perú", "item": SITE}]
    if extra: l.append({"@type": "ListItem", "position": 3, "name": extra[0], "item": extra[1]})
    return {"@type": "BreadcrumbList", "itemListElement": l}

def page(d):
    url = SITE + d["slug"] + ".html"
    nec = "".join(f"<li>{e(x)}</li>" for x in d["nec"])
    pasos = "".join(f"<li>{e(x)}</li>" for x in d["pasos"])
    main, *rest = d["links"]
    links = f'<a class="btn" href="{e(main[1])}" target="_blank" rel="noopener">{e(main[0])} ↗</a>'
    links += "".join(f'<a class="btn sec" href="{e(u)}" target="_blank" rel="noopener">{e(n)} ↗</a>' for n, u in rest)
    ojo = "".join(f"<li>{e(x)}</li>" for x in d["ojo"])
    src = " · ".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a>' for n, u in d["src"])
    verif = d.get("verif", "")
    desc = f'{d["t"]} paso a paso, explicado con palabras sencillas: requisitos, costo y enlace oficial ({d["ent"]}).'
    ld = {"@context": "https://schema.org", "@graph": [crumbs((d["t"], url)),
          {"@type": "Article", "headline": d["t"], "description": desc, "inLanguage": "es-PE",
           "dateModified": d.get("mod", "2026-11-10"), "mainEntityOfPage": url, "image": BASE + "og-imagen.png",
           "author": ORG, "publisher": ORG}]}
    body = f'''<p class="miga"><a href="./">← Todos los trámites</a></p>
<article>
<p class="ent">{e(d["ent"])}</p>
<h1><span aria-hidden="true">{d["icon"]}</span> {e(d["t"])}</h1>
<p class="lead">{e(d["r"])}</p>

<div class="datos">
  <div class="dato"><span>Cuánto cuesta</span><strong>{e(d["costo"])}</strong></div>
  <div class="dato"><span>Quién puede hacerlo</span><p>{e(d["quien"])}</p></div>
</div>

<section class="card">
<h2>Lo que necesitas</h2>
<ul class="check">{nec}</ul>
<p class="pago"><strong>Cómo pagar:</strong> {e(d["pago"])}</p>
</section>

<section class="card">
<h2>Paso a paso</h2>
<ol class="pasos">{pasos}</ol>
<div class="botones">{links}</div>
</section>

<section class="card ojo">
<h2>Ten en cuenta</h2>
<ul>{ojo}</ul>
</section>

<p class="rev">Revisado el {d.get("rev", REV)}. {e(verif)} Fuente: {src}</p>
<p class="acciones"><button type="button" class="btn sec" onclick="window.print()">Imprimir esta guía</button></p>
</article>
'''
    return head(f'{d["t"]} | Trámite fácil Perú', desc, url, ld) + body + FOOT

def index():
    usados = [g for g in GRUPOS if any(ETIQ[d["ent"]] == g for d in T)]
    chips = '<button type="button" class="chip" data-g="" aria-pressed="true">Todos</button>' + "".join(
        f'<button type="button" class="chip" data-g="{e(g)}" aria-pressed="false">{e(g)}</button>' for g in usados)
    cards = "".join(f'''<a class="tram" href="{d["slug"]}.html" data-g="{e(ETIQ[d["ent"]])}" data-b="{e((d["t"]+" "+d["ent"]+" "+ETIQ[d["ent"]]+" "+d["r"]).lower())}">
  <span class="ic" aria-hidden="true">{d["icon"]}</span>
  <span><small>{e(d["ent"])}</small><strong>{e(d["t"])}</strong><em>{e(d["costo"])}</em></span>
</a>''' for d in T)
    ld = {"@context": "https://schema.org", "@graph": [crumbs(),
          {"@type": "ItemList", "name": "Trámites del Perú paso a paso", "numberOfItems": len(T),
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": d["t"], "url": SITE + d["slug"] + ".html"} for i, d in enumerate(T)]}]}
    body = f'''<h1>Trámites del Perú, paso a paso y en palabras sencillas</h1>
<p class="lead">Elige tu trámite. Te decimos qué necesitas, cuánto cuesta y te llevamos a la página oficial para hacerlo. Gratis y sin registrarte. Ya hay {len(T)} guías y seguimos agregando más.</p>
<label class="buscar"><span>¿Qué trámite buscas?</span>
<input type="search" id="q" placeholder="Ej.: DNI, brevete, SIS" autocomplete="off"></label>
<div class="chips" role="group" aria-label="Filtrar por tema">{chips}</div>
<p id="cuenta" class="cuenta" aria-live="polite"></p>
<p id="nada" class="hidden">No encontramos ese trámite. Prueba con otra palabra o elige «Todos».</p>
<div class="lista" id="lista">{cards}</div>

<section class="card ojo">
<h2>Consejos para no caer en estafas</h2>
<ul>
<li>Las páginas oficiales del Estado terminan en <strong>.gob.pe</strong>.</li>
<li>Paga solo en la página oficial, en Págalo.pe o en el Banco de la Nación.</li>
<li>Nadie del Estado te pedirá tu clave por teléfono, WhatsApp o mensaje.</li>
<li>Si alguien te ofrece «sacar tu trámite más rápido» a cambio de dinero, desconfía.</li>
</ul>
</section>
<script>
(function(){{
  var q=document.getElementById('q'), it=document.querySelectorAll('.tram'), nada=document.getElementById('nada'),
      cuenta=document.getElementById('cuenta'), chips=document.querySelectorAll('.chip'), g='';
  function n(s){{return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}}
  function filtrar(){{
    var v=n(q.value.trim()), c=0;
    it.forEach(function(a){{var ok=(!g||a.dataset.g===g)&&(!v||n(a.dataset.b).indexOf(v)>-1); a.hidden=!ok; if(ok)c++;}});
    nada.classList.toggle('hidden',c>0);
    cuenta.textContent=c+(c===1?' trámite':' trámites');
  }}
  chips.forEach(function(b){{b.addEventListener('click',function(){{
    g=b.dataset.g; chips.forEach(function(x){{x.setAttribute('aria-pressed',String(x===b));}}); filtrar();
  }});}});
  q.addEventListener('input',filtrar);
  filtrar();
}})();
</script>
'''
    return head("Trámite fácil Perú | Trámites paso a paso y en palabras sencillas",
                "Guías sencillas para hacer trámites del RENIEC, SUNAT, MTC, SUNARP, SIS, Migraciones y más: requisitos, costo y enlace oficial. Gratis, con letra grande.",
                SITE, ld) + body + FOOT

os.makedirs(OUT, exist_ok=True)
for d in T:
    open(os.path.join(OUT, d["slug"] + ".html"), "w").write(page(d))
open(os.path.join(OUT, "index.html"), "w").write(index())
print(len(T), "páginas")
