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

# ---------- Tanda 3 (11/11/2026, tarde) ----------
T += [
 dict(N, slug="dni-menores", ent="RENIEC", icon="👶",
  t="Sacar el DNI de tu hijo o hija por primera vez",
  r="El primer DNI de un menor se tramita en persona en el RENIEC. En 2026 es gratis en las oficinas del RENIEC dentro de los hospitales.",
  quien="Menores de hasta 16 años que nunca tuvieron DNI, con su papá o su mamá.",
  nec=["El CUI del certificado de nacido vivo, el acta de nacimiento o el DNI de uno de los padres.",
       "El pago, si no te toca gratis.",
       "Una foto tamaño pasaporte a color y fondo blanco, solo si la oficina no toma la foto ahí mismo (cuando la toman en la oficina, es gratis)."],
  costo="S/ 16.00 (gratis en 2026 en algunos casos)", pago="Yape, Banco de la Nación o Págalo.pe con el código 00647.",
  pasos=["Revisa si te toca gratis: en 2026 lo es para menores de 0 a 16 años que se inscriben en las oficinas del RENIEC de los hospitales, y para bebés de 0 a 1 año en los centros del RENIEC.",
         "Si no es gratis, paga S/ 16 con el código 00647.",
         "Ve con el menor a una oficina del RENIEC con los documentos.",
         "Le toman la foto y las huellas.",
         "Recoge el DNI en la oficina. Si no puedes ir, un familiar directo puede recogerlo con el ticket y una carta poder."],
  links=[("Trámites de DNI de menores (RENIEC)", "https://identidad.reniec.gob.pe/tramites-y-servicios1"), PAGALO],
  ojo=["Este trámite no se puede hacer por internet.", "Las personas con discapacidad también tienen DNI gratis en 2026, si acreditan su condición."],
  src=[("RENIEC, preguntas frecuentes de trámites", "https://identidad.reniec.gob.pe/tramites-y-servicios1"),
       ("Andina, 28 de diciembre de 2025 (DNI gratis 2026)", "https://andina.pe/agencia/noticia-reniec-autoriza-dni-electronico-gratuito-para-menores-y-poblaciones-prioritarias-2026-1057151.aspx")]),

 dict(N, slug="dni-electronico-primera-vez", ent="RENIEC", icon="💳",
  t="Cambiar tu DNI azul por el DNI electrónico",
  r="Si todavía tienes el DNI azul, puedes pasar al DNI electrónico desde el celular. Hasta el 31 de diciembre de 2026 cuesta S/ 30.",
  quien="Mayores de edad con DNI azul. No es obligatorio cambiarlo si tu DNI azul sigue vigente.",
  nec=["Un celular Android o iPhone de gama media o alta, con cámara.", "Buena luz y una pared lisa de color claro.", "Alguien que te ayude a tomar la foto."],
  costo="S/ 30.00 (hasta el 31/12/2026)", pago="Dentro de la plataforma con tarjeta o Yape, o antes en Págalo.pe, Banco de la Nación o agentes BCP con el código 02121.",
  pasos=["Descarga la app DNI BioFacial 3.0 del RENIEC.",
         "Elige «emisión por primera vez del DNIe».",
         "Valida tu rostro: mira a la cámara, sin sonreír y sin gorra.",
         "La app te lleva a la web del RENIEC para terminar el trámite y pagar.",
         "Cuando el seguimiento diga «al 100 %» y «En agencia», recógelo en la oficina que elegiste."],
  links=[("Emisión del DNIe (RENIEC)", "https://apps.reniec.gob.pe/EmisionDnie/"),
         ("Ver cómo va tu trámite", "https://serviciosportal.reniec.gob.pe/cetdnipi/inicio.htm"), PAGALO],
  ojo=["El DNI electrónico dura 10 años para adultos.", "Si tu DNI azul ya venció, mira la guía de renovación."],
  src=[("RENIEC, nota del 18 de octubre de 2026", "https://identidad.reniec.gob.pe/b/-necesitas-obtener-tu-dni-electronico-asi-puedes-hacerlo-con-la-app-dni-biofacial"),
       ("RENIEC, nota del 26 de marzo de 2026", "https://identidad.reniec.gob.pe/b/reniec-amplia-beneficio-de-primer-dni-electronico-a-s-30-hasta-diciembre-2026")]),

 dict(N, slug="copia-literal", ent="SUNARP", icon="📑",
  t="Sacar la copia literal de tu casa o terreno",
  r="La copia literal muestra todo lo inscrito sobre un inmueble: dueños, hipotecas y cargas. Se pide para vender, comprar o hacer trámites en bancos.",
  quien="Cualquier persona. No tienes que ser el dueño.",
  nec=["El número de partida del inmueble (o los datos para buscarlo).", "Tu DNI y tu fecha de nacimiento para crear tu cuenta.", "Una tarjeta de débito o crédito, o pago en Págalo.pe."],
  costo="Depende del número de páginas", pago="Tarjeta en la plataforma de la SUNARP o Págalo.pe. El monto exacto aparece antes de pagar.",
  pasos=["Crea tu cuenta en el Servicio de Publicidad Registral en Línea (SPRL) de la SUNARP.",
         "Acepta el contrato de acceso a la información.",
         "Busca la partida y pide el certificado literal.",
         "Paga.",
         "Si la partida tiene hasta 80 páginas, se emite al momento. Descárgala en la web de la SUNARP o en Síguelo."],
  links=[("Servicios en línea SUNARP", "https://www.sunarp.gob.pe/serviciosenlinea/portal/index.html"),
         ("Trámite en gob.pe", "https://www.gob.pe/360")],
  ojo=["El certificado trae un código para verificarlo por internet durante 90 días.", "Algunas partidas antiguas no salen al instante; las revisa un registrador.", "Desde julio de 2026 también lo dan al instante en las oficinas de la SUNARP."],
  verif="Los pasos en línea vienen de una nota de 2021. Confirma el costo en la plataforma antes de pagar.",
  src=[("Andina, 12 de noviembre de 2021", "https://andina.pe/agencia/noticia-sunarp-emitira-automaticamente-certificados-literales-partidas-solicitadas-internet-869297.aspx"),
       ("El Peruano, 17 de julio de 2026", "https://elperuano.pe/noticia/300481-solicitaras-un-certificado-literal-sunarp-lo-entregara-al-instante-con-firma-digital")]),

 dict(N, slug="papeletas-sat", ent="SAT Lima", icon="🚦",
  t="Consultar y pagar tus papeletas en Lima (SAT)",
  r="Revisa con tu placa si tienes papeletas en Lima y págalas por internet. En septiembre de 2026 el SAT activó un descuento de 90 %.",
  quien="Dueños o conductores de vehículos con papeletas del SAT de Lima.",
  nec=["La placa del vehículo.", "Yape, Plin, tarjeta o banca por internet para pagar."],
  costo="Depende de la papeleta", pago="Yape, Plin, Bim, Google Pay, Apple Pay, banca por internet o agentes KasNet.",
  pasos=["Entra a Pagos en línea del SAT (botón verde de abajo).",
         "Escribe la placa.",
         "Elige la papeleta que quieres pagar o paga todo.",
         "Completa tus datos y elige cómo pagar."],
  links=[("Pagos en línea SAT Lima", "https://www.sat.gob.pe/pagosenlinea/")],
  ojo=["El descuento de 90 % no aplica a las infracciones más graves (por ejemplo, manejar ebrio).", "Al pagar con el descuento, esas multas no suman puntos en tu licencia.", "Solo sirve para papeletas del SAT de Lima. En otras ciudades, consulta en el SAT o la municipalidad provincial."],
  verif="Descuento vigente según El Peruano del 11 de septiembre de 2026; la nota no indica hasta cuándo dura.",
  src=[("El Peruano, 11 de septiembre de 2026", "https://elperuano.pe/noticia/304533-papeletas-conoce-como-acceder-al-90-de-descuento-y-pagar-desde-cualquier-lugar")]),

 dict(N, slug="consultar-essalud", ent="EsSalud", icon="🩺",
  t="Saber si tu seguro de EsSalud está activo",
  r="Antes de sacar una cita, revisa si estás asegurado en EsSalud y en qué centro te toca atenderte.",
  quien="Trabajadores en planilla y sus familiares inscritos (cónyuge o conviviente e hijos menores).",
  nec=["Tu DNI."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a «¿Dónde me atiendo?» de EsSalud (botón verde de abajo).",
         "Escribe tu tipo y número de documento.",
         "Mira si tu seguro está vigente y cuál es tu centro asignado.",
         "Si está activo, saca tu cita por EsSalud en Línea o llamando al 411 8000."],
  links=[("¿Dónde me atiendo? (EsSalud)", "https://dondemeatiendo.essalud.gob.pe/"),
         ("Consultas en línea EsSalud", "http://www.essalud.gob.pe/consultas-en-linea/")],
  ojo=["Si no aparece activo, puede que tu empleador no te haya declarado o lo haya hecho tarde. Pregúntale.", "Si te mudaste, actualiza tu domicilio en una oficina de seguros de EsSalud."],
  verif="Los pasos vienen de una nota de EsSalud de 2014; el enlace «¿Dónde me atiendo?» sigue activo.",
  src=[("EsSalud, ¿Cómo saber si su seguro está activo?", "http://www.essalud.gob.pe/%C2%BFcomo-saber-si-su-seguro-de-essalud-esta-activo/")]),

 dict(N, slug="consultar-afp", ent="SBS", icon="🏦",
  t="Saber en qué AFP estás y cuánto tienes",
  r="Con la SBS ves a qué AFP perteneces. Luego, en la web de tu AFP, ves cuánto dinero tienes acumulado.",
  quien="Personas afiliadas al Sistema Privado de Pensiones.",
  nec=["Tu DNI.", "Un correo electrónico."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a Servicios SBS en línea y regístrate con tu DNI y tu correo.",
         "Elige el «Reporte de situación previsional» para ver tu AFP.",
         "Entra a la web de tu AFP (Integra, Prima, Habitat o Profuturo) con tu DNI y contraseña.",
         "Revisa tu fondo y tus aportes."],
  links=[("Servicios SBS en línea", "https://servicios.sbs.gob.pe/serviciosenlinea"),
         ("AFP Integra", "https://www.afpintegra.pe/iniciar-sesion"),
         ("AFP Habitat", "https://www.afphabitat.com.pe/"),
         ("Profuturo AFP", "https://enlinea.profuturo.com.pe/zonaprivada/aviso")],
  ojo=["Si estás en la ONP, mira la guía «Ver tus aportes a la ONP».", "No des tu clave de la AFP a nadie que te prometa «sacar tu fondo»."],
  verif="Pasos según El Peruano (2023). Prima AFP también tiene su zona «Mi cuenta» en su web.",
  src=[("El Peruano, 6 de noviembre de 2023", "https://www.elperuano.pe/noticia/227156-consulta-tu-afp-conoce-aqui-cuanto-tienes-acumulado-en-tu-fondo-de-pensiones-en-2023-links")]),
]

# ---------- Tanda 4 (11/11/2026, tarde) ----------
T += [
 dict(N, slug="cts", ent="Ministerio de Trabajo", icon="💰",
  t="Revisar y retirar tu CTS",
  r="La CTS es un ahorro que tu empleador deposita en mayo y noviembre. En 2026 puedes retirar el 100 %.",
  quien="Trabajadores del régimen privado que trabajan en promedio 4 horas diarias o más y tienen al menos un mes en la empresa.",
  nec=["Tu DNI.", "Saber en qué banco o caja te depositan la CTS."],
  costo="Gratis", pago="No se paga nada por retirarla.",
  pasos=["Calcula cuánto te toca: tu sueldo de octubre más 1/6 de la gratificación de julio, dividido entre 12 y multiplicado por los meses trabajados del semestre (hasta 6).",
         "Revisa el depósito en tu banco. El plazo de noviembre de 2026 vence el lunes 16.",
         "Si quieres, retira tu dinero en tu banco o caja: hasta el 31 de diciembre de 2026 puedes sacar el 100 %."],
  links=[("Ministerio de Trabajo (gob.pe)", "https://www.gob.pe/mtpe")],
  ojo=["Ejemplo: con S/ 2 000 de sueldo y el semestre completo, la CTS es unos S/ 1 000 (sin contar la gratificación).", "No reciben CTS quienes trabajan menos de 4 horas diarias ni quienes cobran remuneración integral anual.", "Puedes elegir el banco donde te depositan.", "Si tu empleador no deposita, pide orientación al Ministerio de Trabajo o a la SUNAFIL."],
  src=[("El Peruano, 25 de octubre de 2026", "https://elperuano.pe/noticia/307575-cts-de-noviembre-quienes-la-reciben-como-se-calcula-hasta-cuando-se-puede-retirar"),
       ("Andina, noviembre de 2026", "https://andina.pe/agencia/noticia-cts-noviembre-2026-mira-quienes-reciben-cuanto-y-hasta-cuando-se-puede-retirar-1097292.aspx")]),

 dict(N, slug="carne-conadis", ent="CONADIS", icon="♿",
  t="Sacar el carné de discapacidad (CONADIS)",
  r="El carné del CONADIS te inscribe en el Registro Nacional de la Persona con Discapacidad y te da acceso a beneficios de ley.",
  quien="Personas con discapacidad que ya tienen su Certificado de Discapacidad. Puede tramitarlo otra persona con carta poder simple.",
  nec=["El Certificado de Discapacidad (lo da un establecimiento de salud certificador).", "Tu DNI.", "Para hacerlo por internet: el certificado y el DNI escaneados (JPG o PNG) y un celular o correo."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Saca primero tu Certificado de Discapacidad en un establecimiento de salud certificador.",
         "Entra a la plataforma «Mi Registro en todo el Perú» del CONADIS y elige inscripción.",
         "Llena el formulario y sube el certificado y el DNI escaneados.",
         "Recibe tu carné digital en tu celular o correo. El físico se coordina contigo.",
         "Si prefieres ir en persona: sede del CONADIS (Av. Arequipa 375, Lima), su oficina regional o la OMAPED de tu municipalidad."],
  links=[("Mi Registro en todo el Perú (CONADIS)", "https://sirnpdpide.conadisperu.gob.pe/")],
  ojo=["Carné celeste: discapacidad leve o moderada. Carné amarillo: discapacidad severa.", "Algunos beneficios: pase libre en transporte público (discapacidad severa), tarifas preferenciales, distintivo vehicular, becas y la pensión Contigo (discapacidad severa).", "En 2026 el DNI también es gratis para personas con discapacidad que lo acrediten."],
  verif="Pasos según Andina (septiembre de 2023); en diciembre de 2025 el CONADIS seguía atendiendo en su sede de Av. Arequipa.",
  src=[("Andina, 3 de septiembre de 2023", "https://andina.pe/agencia/noticia-sin-costo-estos-son-los-pasos-para-tramitar-carne-conadis-y-acceder-a-beneficios-953844.aspx"),
       ("Andina, 12 de diciembre de 2025", "https://andina.pe/agencia/noticia-conadis-obten-carne-discapacidad-tan-solo-30-minutos-donde-1055133.aspx")]),

 dict(N, slug="reporte-soat", ent="SBS", g="Autos y propiedades", icon="🛡️",
  t="Ver el SOAT y los choques de un auto",
  r="Con la placa ves el SOAT y los seguros que tuvo un vehículo en los últimos 5 años, y si tuvo accidentes. Útil antes de comprar un auto usado.",
  quien="Cualquier persona.",
  nec=["El número de placa."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra al Reporte SOAT/CAT y Seguro Vehicular de la SBS (botón verde de abajo).",
         "Escribe la placa.",
         "Revisa la aseguradora o AFOCAT, el número de póliza, la vigencia y los siniestros."],
  links=[("Reporte SOAT/CAT (SBS)", "https://www.sbs.gob.pe/usuarios/nuestros-servicios/reporte-vehicular")],
  ojo=["Revisa también los datos del auto en la guía «Ver los datos de un auto con su placa» (SUNARP)."],
  src=[("Andina, 2 de julio de 2025", "https://andina.pe/agencia/noticia-sabias-puedes-solicitar-gratis-reporte-seguro-vehicular-portal-sbs-1035758.aspx")]),

 dict(N, slug="reporte-deudas", ent="SBS", icon="📋",
  t="Ver tu reporte de deudas (central de riesgos)",
  r="La SBS te muestra gratis tus deudas con bancos, cajas y financieras, y las tarjetas o líneas de crédito que tienes sin usar.",
  quien="Cualquier persona con DNI o carné de extranjería.",
  nec=["Tu DNI.", "Un correo electrónico."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a Servicios SBS en línea y regístrate con tu DNI y tu correo.",
         "Elige el reporte de deudas.",
         "Revisa tus deudas y su calificación (normal, con problemas potenciales, etc.).",
         "Si ves una deuda que no reconoces, reclama primero a esa entidad."],
  links=[("Servicios SBS en línea", "https://servicios.sbs.gob.pe/serviciosenlinea")],
  ojo=["Si te suscribes, la SBS te avisa por correo cuando cambia tu reporte.", "Nadie puede «limpiarte» de la central de riesgos a cambio de dinero."],
  verif="La nota oficial es de 2018; los pasos son un resumen. Sigue las indicaciones de la plataforma de la SBS.",
  src=[("TV Perú, 23 de agosto de 2018", "https://www.tvperu.gob.pe/noticias/economia/sbs-brinda-detalles-para-conocer-tu-reporte-de-deudas")]),

 dict(N, slug="licencia-edificacion", ent="Municipalidad", icon="🏗️",
  t="Sacar la licencia para construir o ampliar tu casa",
  r="Antes de construir, ampliar o demoler, necesitas la licencia de edificación de tu municipalidad. Para una casa pequeña el trámite es más simple (modalidad A).",
  quien="Dueños del terreno o sus representantes.",
  nec=["El Formulario Único de Edificación (FUE) firmado.",
       "La copia literal de tu propiedad (ver la guía de SUNARP).",
       "Los planos firmados por un arquitecto o ingeniero colegiado, o un proyecto del banco de proyectos de tu municipalidad.",
       "El pago de la licencia."],
  costo="Depende de tu municipalidad", pago="Lo indica tu municipalidad en su TUPA.",
  pasos=["Revisa la modalidad. La modalidad A sirve, por ejemplo, para una vivienda unifamiliar de hasta 120 m² que sea la única en el lote, o ampliaciones que no pasen de 200 m² en total.",
         "Busca en el TUPA de tu municipalidad los requisitos y el costo actuales.",
         "Prepara el formulario, la copia literal y los planos.",
         "Presenta todo en la municipalidad y paga.",
         "Guarda tu licencia en la obra."],
  links=[("Buscar el trámite en gob.pe", "https://www.gob.pe/busquedas?term=licencia+de+edificacion"),
         ("Ley 29090 (texto)", "https://www.miraflores.gob.pe/Gestorw3b/files/pdf/5145-902-ley-29090.pdf")],
  ojo=["Si la obra lleva sótano o excavaciones de más de 1,50 m junto a otras casas, ya no es modalidad A.", "La licencia dura 36 meses y se puede ampliar 12 meses más una sola vez.", "Construir sin licencia puede traer multas o la demolición."],
  verif="Requisitos generales de la Ley 29090 y sus cambios; la ley se ha modificado varias veces. Tu municipalidad tiene los requisitos vigentes en su TUPA.",
  src=[("Ley 29090, Ley de Regulación de Habilitaciones Urbanas y de Edificaciones", "https://www.miraflores.gob.pe/Gestorw3b/files/pdf/5145-902-ley-29090.pdf")]),
]

# Tanda 4 (11-11-2026)
T += [
 dict(N, slug="pension-contigo", ent="MIDIS", icon="♿",
  t="Pedir la pensión Contigo por discapacidad severa",
  r="El programa Contigo da S/ 300 cada dos meses a personas con discapacidad severa que viven en pobreza.",
  quien="Personas con discapacidad severa, que no tienen ingresos ni pensión, y cuyo hogar está en pobreza o pobreza extrema según el SISFOH.",
  nec=["DNI de la persona con discapacidad.",
       "El certificado de discapacidad que diga «severa», dado por un establecimiento de salud autorizado.",
       "La clasificación socioeconómica del hogar (SISFOH), que da la municipalidad."],
  costo="Gratis", pago="Inscribirse no cuesta nada.",
  pasos=["Pide el certificado de discapacidad en un hospital o centro de salud autorizado. Debe decir que la discapacidad es severa.",
         "Pide la clasificación socioeconómica en la Unidad Local de Empadronamiento (ULE) de tu municipalidad.",
         "Con los dos documentos, acércate a la OMAPED de tu municipalidad o llama al programa Contigo para que te inscriban.",
         "Revisa si ya eres usuario en la consulta rápida de Contigo, solo con el DNI.",
         "Si eres usuario, cobra en cajeros del Banco de la Nación, agentes Multired o ventanilla."],
  links=[("Consultar si soy usuario de Contigo", "https://sicontigo.contigo.gob.pe/"),
         ("Pensión 65 (para adultos mayores)", "pension-65.html")],
  ojo=["Nadie puede cobrarte por inscribirte. El MIDIS avisa que el programa no pide pagos.",
       "Consultas: teléfono (01) 644 9006.",
       "Si la persona tiene más de 65 años, revisa también Pensión 65."],
  verif="No pudimos abrir la página oficial de Contigo desde nuestro sistema; los pasos salen de notas de TV Perú y El Peruano. Confírmalos por teléfono antes de ir.",
  src=[("TV Perú: cómo saber si soy beneficiario", "https://www.tvperu.gob.pe/noticias/locales/pension-del-programa-contigo-como-saber-si-soy-beneficiario-y-cuando-pagan"),
       ("TV Perú: el MIDIS no exige pagos", "https://www.tvperu.gob.pe/noticias/economia/midis-advierte-que-el-programa-contigo-no-exige-pagos-para-tramites-o-convocatorias"),
       ("El Peruano (monto de S/ 300)", "https://www.elperuano.pe/noticia/221550-programa-contigo-deposito-pension-de-s300-para-106-mil-personas-con-discapacidad-severa")]),

 dict(N, slug="beca-18", ent="Pronabec", icon="🎓",
  t="Postular a Beca 18",
  r="Beca del Estado que cubre los estudios de una carrera universitaria o técnica a jóvenes con buenas notas y pocos recursos.",
  quien="En la modalidad ordinaria: jóvenes de menos de 22 años, con alto rendimiento en la secundaria (por ejemplo, tercio superior) y hogar en pobreza o pobreza extrema según el SISFOH. Hay otras modalidades con reglas propias (por ejemplo, para comunidades nativas, Fuerzas Armadas, VRAEM o Huallaga).",
  nec=["Tu DNI.", "Haber terminado la secundaria con alto rendimiento.",
       "La clasificación socioeconómica de tu hogar (SISFOH), si postulas a la modalidad ordinaria.",
       "Un correo y un celular para inscribirte por internet."],
  costo="Gratis", pago="Inscribirte y dar el examen no cuesta nada.",
  pasos=["Revisa en la página del Pronabec la convocatoria del año y tu modalidad.",
         "Inscríbete por internet en las fechas de la convocatoria.",
         "Da el Examen Nacional de Preselección.",
         "Si pasas, ingresa a una carrera y a una universidad o instituto que estén en la lista de la beca.",
         "Postula a la beca en la etapa de selección con tus documentos y espera los resultados."],
  links=[("Beca 18 en la web del Pronabec", "https://www.pronabec.gob.pe/beca-18/")],
  ojo=["Convocatoria Beca 18-2027: 6000 becas; la inscripción cerró el 18 de octubre de 2026 y el examen es el domingo 22 de noviembre de 2026.",
       "Cada año hay una convocatoria nueva, más o menos entre setiembre y octubre. Si te la perdiste, prepárate para la siguiente.",
       "Ayuda: WhatsApp 914 121 106 o línea gratuita 0800 000 18. En los centros MAC Express también te ayudan a inscribirte."],
  verif="Fechas de la convocatoria Beca 18-2027; cambian cada año.",
  src=[("El Peruano: requisitos de Beca 18-2027", "https://elperuano.pe/noticia/306716-beca-18-2027-estos-son-los-requisitos-para-postular-a-una-de-las-6000-vacantes-hasta-el-16-de-octubre"),
       ("El Peruano: inscripción ampliada al 18 de octubre", "https://elperuano.pe/noticia/306985--lo-ultimo-pronabec-amplia-hasta-este-domingo-18-de-octubre-la-inscripcion-para-postular-a-beca-18"),
       ("Andina: MAC Express ayuda a inscribirse", "https://andina.pe/agencia/noticia-quieres-postular-a-beca-182027-mac-express-te-ayuda-con-inscripcion-1096050.aspx")]),

 dict(N, slug="inscribir-defuncion", ent="RENIEC", icon="🕊️",
  t="Inscribir la defunción de un familiar",
  r="Cuando alguien fallece, hay que registrarlo en el RENIEC. Así se obtiene el acta de defunción y su DNI queda como «fallecido».",
  quien="Un familiar u otra persona que presenta el caso (el declarante), con su propio documento de identidad.",
  nec=["El certificado de defunción firmado y sellado por un profesional de la salud. Donde no hay uno, sirve una declaración jurada de una autoridad política, judicial o religiosa.",
       "El DNI de la persona fallecida, o una declaración jurada de pérdida firmada por el declarante.",
       "El DNI del declarante (si es extranjero, su carné de extranjería, pasaporte o cédula)."],
  costo="Pregunta en la oficina", pago="Si hay algún pago, te lo indican en la oficina del RENIEC.",
  pasos=["Junta el certificado de defunción y los documentos de identidad.",
         "Ve a una oficina del RENIEC y entrega los documentos.",
         "El personal registra la defunción en el sistema.",
         "En 5 a 7 días hábiles el DNI de la persona aparece como fallecido.",
         "Si necesitas una copia del acta de defunción, pídela por internet (mira la guía de copias de actas)."],
  links=[("Trámites de actas del RENIEC", "https://identidad.reniec.gob.pe/tramites"),
         ("Pedir copia de un acta", "partida-nacimiento.html")],
  ojo=["Si la persona falleció en el extranjero, el acta sellada por el consulado peruano se presenta por la mesa de partes virtual del RENIEC.",
       "Registrar la defunción evita que la persona siga apareciendo en el padrón electoral.",
       "Consultas del RENIEC: 315 2700 o 315 4000, anexo 1900."],
  verif="Requisitos y pasos según TV Perú (marzo de 2025). La nota no dice si hay costo ni un plazo límite.",
  src=[("TV Perú: cómo registrar una defunción", "https://www.tvperu.gob.pe/noticias/nacionales/como-registrar-una-defuncion-para-evitar-que-una-persona-aparezca-en-el-padron-de-elecciones-2026"),
       ("RENIEC: preguntas frecuentes de actas", "https://identidad.reniec.gob.pe/preguntas-frecuentes-actas-de-nacimiento-matrimonio-y-defunci%C3%B3n")]),

 dict(N, slug="inscribir-recien-nacido", ent="RENIEC", icon="🍼",
  t="Inscribir a un recién nacido y sacar su primer DNI",
  r="Registra el nacimiento de tu bebé para que tenga su acta de nacimiento y su DNI. Es gratis.",
  quien="La madre, el padre o ambos, con su DNI.",
  nec=["El certificado de nacido vivo que te da el hospital o la clínica (tiene un código llamado CUI).",
       "El DNI de la madre y, si lo reconoce, el del padre."],
  costo="Gratis", pago="La inscripción del nacimiento y la primera copia del acta son gratis por ley.",
  pasos=["Pide en el hospital o clínica el certificado de nacido vivo.",
         "Si el hospital tiene una oficina del RENIEC, inscribe ahí a tu bebé antes de salir. Si no, ve a una oficina del RENIEC o al registro civil de tu municipalidad.",
         "Firma el acta de nacimiento y recibe tu copia.",
         "Pide ahí mismo el DNI de tu bebé: toman su foto y las huellas de la mamá.",
         "Recoge el DNI cuando te avisen."],
  links=[("Trámites de actas del RENIEC", "https://identidad.reniec.gob.pe/tramites"),
         ("DNI para menores de edad", "dni-menores.html")],
  ojo=["Tienes 60 días desde el nacimiento. Después, la inscripción es «extemporánea» y lleva más pasos.",
       "Con el programa «Nacer con identidad», el RENIEC registra a bebés en salas de maternidad durante sus primeros 5 días.",
       "En 2026 el DNI electrónico es gratis para niños de 0 a 1 año (campaña del RENIEC).",
       "El DNI del bebé sirve para el SIS, las vacunas, el control del niño sano y los programas sociales."],
  verif="La gratuidad del DNI de 0 a 1 año es por campaña de 2026; puede cambiar.",
  src=[("RENIEC: programa para registrar a bebés en sus 5 primeros días", "https://identidad.reniec.gob.pe/b/reniec-lanza-programa-para-registrar-a-bebes-durante-los-cinco-dias-de-nacidos"),
       ("Andina: DNI electrónico gratuito para menores en 2026", "https://andina.pe/agencia/noticia-reniec-autoriza-dni-electronico-gratuito-para-menores-y-poblaciones-prioritarias-2026-1057151.aspx"),
       ("Ley de gratuidad de la inscripción del nacimiento (RENIEC)", "https://identidad.reniec.gob.pe/documents/d/guest/modificatorias_a_la_ley_organica")]),

 dict(N, slug="denuncia-perdida-documentos", ent="PNP", icon="📝",
  t="Denunciar por internet la pérdida o robo de documentos",
  r="Si perdiste o te robaron tu DNI, brevete, pasaporte u otros documentos, haz la denuncia policial por internet, gratis y a cualquier hora.",
  quien="Cualquier persona que perdió o a quien le robaron sus documentos.",
  nec=["Tu DNI (el número) o tu documento de identidad.", "Un correo electrónico.", "Los datos de los documentos que perdiste."],
  costo="Gratis", pago="La denuncia digital no cuesta nada.",
  pasos=["Entra a la web de Denuncias Digitales de la Policía.",
         "Elige si fue pérdida o robo y escribe tus datos.",
         "Marca los documentos que perdiste (DNI, brevete, pasaporte, SOAT, carné universitario, fotocheck, facturas o boletas).",
         "Cuenta brevemente qué pasó y envía.",
         "Descarga o guarda la denuncia que te llega. Úsala para sacar el duplicado de tus documentos."],
  links=[("Denuncias Digitales de la PNP", "https://sistemas.policia.gob.pe/denuncias_digitales/"),
         ("Sacar el duplicado de tu DNI", "duplicado-dni.html")],
  ojo=["Este servicio es solo para documentos. Si te robaron otras cosas o hubo violencia, ve a una comisaría.",
       "Decir datos falsos en una denuncia es delito.",
       "Para el duplicado del DNI no siempre te piden denuncia; revisa la guía del duplicado."],
  verif="Servicio activo desde setiembre de 2020 según TV Perú y Andina.",
  src=[("TV Perú: PNP presenta servicio de denuncia digital", "https://www.tvperu.gob.pe/novedades/tvperu/policia-nacional-del-peru-presenta-servicio-de-denuncia-digital"),
       ("TV Perú: casi 220 mil denuncias digitales", "https://www.tvperu.gob.pe/noticias/nacionales/casi-220-mil-denuncias-digitales-por-perdida-de-documentos-registro-la-pnp-este-ano"),
       ("Andina: más de 600 mil denuncias digitales", "https://andina.pe/agencia/noticia-mas-600-mil-personas-han-denunciado-digitalmente-perdida-sus-documentos-936239.aspx")]),
]

# Tanda 5 (11-11-2026)
T += [
 dict(N, slug="record-conductor", ent="MTC", icon="🚦",
  t="Ver tu récord de conductor y tus puntos",
  r="Revisa gratis tus papeletas y los puntos que tienes acumulados en tu licencia de conducir.",
  quien="Cualquier persona. Solo necesitas el DNI o el número de licencia.",
  nec=["Tu DNI o tu número de licencia de conducir (también puedes buscar por apellidos y nombres)."],
  costo="Gratis", pago="La consulta no cuesta nada.",
  pasos=["Entra a la página del récord de conductor del MTC.",
         "Elige cómo buscar: por DNI, por número de licencia o por nombres.",
         "Escribe el dato y el código de la imagen (captcha), y pulsa «Buscar».",
         "Revisa tus últimas papeletas, con fecha y falta, y los puntos de cada licencia."],
  links=[("Récord de conductor (MTC)", "https://slcp.mtc.gob.pe/"),
         ("Ver tus papeletas del SAT Lima", "papeletas-sat.html")],
  ojo=["Si llegas a 100 puntos te suspenden la licencia: 6 meses la primera vez, 1 año la segunda y para siempre la tercera.",
       "Las papeletas de Lima también se ven en el SAT; mira esa guía para pagarlas."],
  verif="Pasos según El Comercio (abril de 2023); la página del MTC puede verse distinta hoy.",
  src=[("El Comercio: cómo consultar tu récord de conductor", "https://elcomercio.pe/respuestas/mtc-como-consultar-online-tu-record-de-conductor-tramites-revtli-noticia/"),
       ("gob.pe: Consulta tu récord de conductor", "https://www.gob.pe/341-consulta-tu-record-de-conductor")]),

 dict(N, slug="multas-electorales", ent="JNE", icon="🗳️",
  t="Consultar y pagar multas electorales",
  r="Revisa si tienes multa por no votar o por no ir como miembro de mesa, y págala o pide la dispensa.",
  quien="Cualquier persona con DNI.",
  nec=["Tu número de DNI.", "Para pagar: tarjeta, Págalo.pe o ir al Banco de la Nación."],
  costo="Consultar es gratis", pago="En Págalo.pe, en el Banco de la Nación, en los pagos en línea del JNE o en su sede central.",
  pasos=["Entra a la consulta de multas del JNE.",
         "Escribe tu DNI y el código de la imagen, acepta las condiciones y pulsa «Consultar».",
         "Si tienes multa, mira el monto y desde cuándo la debes.",
         "Págala en línea (JNE o Págalo.pe) o en el Banco de la Nación.",
         "Si tuviste un motivo válido para no votar, pide una dispensa o justificación en vez de pagar."],
  links=[("Consultar multas electorales (JNE)", "https://multas.jne.gob.pe/login"),
         ("Pagos en línea del JNE", "https://pagosenlinea.jne.gob.pe/"), PAGALO],
  ojo=["Por no votar se paga hasta el 2 % de la UIT del año de la elección (con la UIT de 2026, S/ 110). Puede ser menos según tu distrito.",
       "Por no ir como miembro de mesa se paga el 5 % de la UIT.",
       "Tener multas sin pagar trae restricciones civiles y notariales. Regularízala pronto.",
       "Si crees que la multa no corresponde, puedes reclamar (reconsideración o apelación)."],
  verif="Montos y lugares de pago según Andina (marzo de 2026). La multa usa la UIT del año en que no votaste.",
  src=[("Andina: ¿Tienes multas electorales? Consulta aquí", "https://andina.pe/agencia/noticia-elecciones-2026-tienes-multas-electorales-consulta-aqui-1064098.aspx")]),

 dict(N, slug="reclamo-indecopi", ent="Indecopi", icon="📣",
  t="Reclamar a una empresa ante Indecopi",
  r="Si una tienda o empresa no te cumplió, primero reclama en su Libro de Reclamaciones. Si no te hace caso, reclama gratis en Indecopi.",
  quien="Cualquier consumidor que compró un producto o pagó un servicio.",
  nec=["Tu DNI.", "La boleta, factura, contrato o estado de cuenta.",
       "Pruebas: correos, capturas de pantalla o fotos.", "La respuesta del Libro de Reclamaciones, si la tienes."],
  costo="Gratis", pago="Reclamar en Indecopi no cuesta nada.",
  pasos=["Escribe tu reclamo en el Libro de Reclamaciones de la empresa (físico o virtual) y guarda la constancia.",
         "La empresa debe responderte en un máximo de 15 días hábiles.",
         "Si no responde o su respuesta no te sirve, entra a Reclama Virtual de Indecopi.",
         "Elige el tipo de reclamo, responde las preguntas y sube tus pruebas.",
         "Indecopi contacta a la empresa para buscar un acuerdo. Revisa el estado de tu reclamo en la misma página."],
  links=[("Reclama Virtual (Indecopi)", "https://enlinea.indecopi.gob.pe/reclamavirtual/#/"),
         ("gob.pe: Presentar reclamos en Indecopi", "https://www.gob.pe/532-presentar-reclamos-en-indecopi")],
  ojo=["Reclama Virtual atiende las 24 horas, todos los días.",
       "Según Indecopi, iniciar el trámite toma unos 6 días hábiles y resolverlo unos 17 días hábiles en promedio.",
       "Consultas: Lima 224-7777; regiones 0-800-44040 (gratis).",
       "El reclamo busca un acuerdo. Si quieres que multen a la empresa, eso es una denuncia, que es otro trámite."],
  verif="Plazo de 15 días hábiles según la Ley 31435 (2022).",
  src=[("Infobae: cómo reclamar ante Indecopi (junio de 2026)", "https://www.infobae.com/peru/2026/06/29/indecopi-como-reclamar-si-una-empresa-no-te-entrega-un-producto-o-servicio/"),
       ("Andina: Reclama Virtual, sin costo", "https://andina.pe/ingles/noticia-indecopi-lanza-reclama-virtual-para-facilitar-procesos-iniciados-los-consumidores-770398.aspx"),
       ("Ley 31435 (texto consolidado)", "https://leyes.congreso.gob.pe/Documentos/2021_2026/ADLP/Texto_Consolidado/31435-TXM.pdf")]),

 dict(N, slug="devolucion-impuestos", ent="SUNAT", icon="💸",
  t="Recibir tu devolución de impuestos",
  r="Si te retuvieron más impuesto del que te tocaba por tu sueldo o tus recibos por honorarios, la SUNAT te devuelve la diferencia.",
  quien="Trabajadores con renta de cuarta categoría (recibos por honorarios) o de quinta categoría (planilla) que tienen saldo a favor al cerrar el año.",
  nec=["Tu DNI o RUC y tu Clave SOL.", "El código de cuenta interbancario (CCI) de tu cuenta bancaria."],
  costo="Gratis", pago="No se paga nada.",
  pasos=["Entra a SUNAT con tu Clave SOL y registra el CCI de tu cuenta.",
         "Espera la devolución automática («de oficio»): la SUNAT te avisa en tu Buzón SOL y deposita en tu cuenta.",
         "Para saber si tienes saldo a favor, revisa la opción «Renta Anual» en SUNAT.",
         "Si no estás de acuerdo con el monto o no te llegó, presenta tu declaración anual y pide la devolución."],
  links=[("gob.pe: Devolución de oficio de cuarta y quinta", "https://www.gob.pe/1203-devolucion-de-oficio-del-impuesto-a-la-renta-de-quinta-categoria"),
         ("Sacar tu Clave SOL", "clave-sol.html")],
  ojo=["Los gastos en restaurantes, hoteles, alquiler, servicios profesionales y aportes a EsSalud de trabajadores del hogar pueden darte más saldo a favor (hasta 3 UIT).",
       "Para que cuenten, esos gastos deben tener boleta o recibo electrónico con tu DNI.",
       "Las devoluciones se pagan a mitad de año, después de la declaración anual."],
  verif="Según Bloomberg Línea (febrero de 2025) y El Peruano (abril de 2026). Las fechas cambian cada año.",
  src=[("Bloomberg Línea: devolución de quinta categoría", "https://www.bloomberglinea.com/latinoamerica/peru/devolucion-de-renta-de-quinta-categoria-en-peru-para-quienes-aplica/"),
       ("El Peruano: devolución de impuestos 2026", "https://elperuano.pe/noticia/292856-devolucion-de-impuestos-2026-como-saber-si-tienes-saldo-a-favor-y-que-hacer-para-recuperarlo")]),

 dict(N, slug="registrar-marca", ent="Indecopi", icon="™️",
  t="Registrar la marca de tu negocio",
  r="Registrar tu marca en Indecopi impide que otros usen tu nombre o tu logo para lo mismo que vendes.",
  quien="Personas o empresas con un nombre o logo para sus productos o servicios.",
  nec=["Tu DNI o RUC.", "El nombre y, si tienes, el logo de tu marca.",
       "Saber en qué «clase» va tu producto o servicio (Indecopi te orienta).", "El pago de la tasa."],
  costo="S/ 534.90 por una clase (referencial)", pago="Págalo.pe o el Banco de la Nación, con el código de la tasa que indica Indecopi.",
  pasos=["Busca si ya hay marcas parecidas en «Busca tu marca» de Indecopi.",
         "Si tienes dudas, pide la asesoría gratuita de marcas de Indecopi.",
         "Paga la tasa.",
         "Envía tu solicitud por el Servicio en Línea de Indecopi o en sus oficinas.",
         "Sigue tu trámite en la consulta de expedientes de marcas."],
  links=[("Busca tu marca (Indecopi)", "https://enlinea.indecopi.gob.pe/buscatumarca/"),
         ("Enviar la solicitud en línea", "https://servicio.indecopi.gob.pe/sel/login.jsf"),
         ("gob.pe: Registrar una marca", "https://www.gob.pe/335")],
  ojo=["El registro dura 10 años y se puede renovar.",
       "Cada clase adicional cuesta aparte (alrededor de S/ 533).",
       "Si otra persona se opone a tu marca, el trámite toma más tiempo."],
  verif="Costos de 2026 según LaLey.pe (junio de 2026), un sitio privado; confírmalos en Indecopi antes de pagar.",
  src=[("LaLey.pe: cuánto cuesta registrar una marca", "https://laley.pe/cuanto-cuesta-registrar-una-marca-en-indecopi/"),
       ("El Peruano: guía para registrar una marca", "https://elperuano.pe/noticia/177417-registro-de-marca-guia-para-efectuar-el-tramite-ante-indecopi")]),
]

ORDEN = ["RENIEC", "SUNAT", "MTC", "SUNARP", "Migraciones", "PNP", "Poder Judicial", "INPE", "SAT Lima", "EsSalud", "SBS", "CONADIS",
         "Ministerio de Trabajo", "SIS", "ONP", "MIDIS", "MINEDU", "SUNEDU", "Pronabec", "Indecopi", "JNE", "Municipalidad"]
ETIQ = {"RENIEC": "DNI y actas", "SUNAT": "Impuestos", "MTC": "Brevete y papeletas", "SUNARP": "Autos y propiedades",
        "Migraciones": "Viajes", "PNP": "Policía y justicia", "Poder Judicial": "Policía y justicia", "INPE": "Policía y justicia",
        "Ministerio de Trabajo": "Trabajo", "SAT Lima": "Brevete y papeletas", "EsSalud": "Salud", "SBS": "Pensiones y finanzas", "CONADIS": "Salud", "SIS": "Salud", "ONP": "Pensiones y finanzas", "MIDIS": "Ayudas del Estado",
        "MINEDU": "Estudios", "SUNEDU": "Estudios", "Pronabec": "Estudios", "Indecopi": "Consumidor y negocios", "JNE": "Elecciones", "Municipalidad": "Municipalidad"}
# Secciones: nombre, archivo, ícono y una frase que explica qué hay dentro
SECC = [("DNI y actas", "dni-y-actas", "🪪", "DNI, partidas de nacimiento, recién nacidos y defunciones (RENIEC)."),
        ("Impuestos", "impuestos", "🧾", "RUC, Clave SOL, recibos por honorarios y devolución de impuestos (SUNAT)."),
        ("Brevete y papeletas", "brevete-y-papeletas", "🚗", "Licencia de conducir, récord de conductor y papeletas."),
        ("Autos y propiedades", "autos-y-propiedades", "🏠", "Vehículos, SOAT y propiedades inscritas en SUNARP."),
        ("Viajes", "viajes", "✈️", "Pasaporte y movimiento migratorio."),
        ("Policía y justicia", "policia-y-justicia", "👮", "Antecedentes policiales, penales y judiciales, y denuncias."),
        ("Trabajo", "trabajo", "💼", "Certificado Único Laboral y CTS."),
        ("Salud", "salud", "🏥", "SIS, EsSalud y carné de discapacidad."),
        ("Ayudas del Estado", "ayudas-del-estado", "🤝", "Pensión 65 y pensión Contigo (MIDIS)."),
        ("Pensiones y finanzas", "pensiones-y-finanzas", "💰", "ONP, AFP y reporte de deudas."),
        ("Estudios", "estudios", "🎓", "Certificados, grados y Beca 18."),
        ("Consumidor y negocios", "consumidor-y-negocios", "🛍️", "Reclamos a empresas y registro de marcas (Indecopi)."),
        ("Elecciones", "elecciones", "🗳️", "Multas electorales y dispensas (JNE)."),
        ("Municipalidad", "municipalidad", "🏛️", "Licencias de funcionamiento y de edificación.")]
GRUPOS = [x[0] for x in SECC]
SEC = {x[0]: {"slug": "seccion-" + x[1], "icon": x[2], "desc": x[3]} for x in SECC}
def grp(d):
    return d.get("g") or ETIQ[d["ent"]]
T.sort(key=lambda d: (GRUPOS.index(grp(d)), ORDEN.index(d["ent"])))

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

def crumbs(*extra):
    l = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE},
         {"@type": "ListItem", "position": 2, "name": "Trámite fácil Perú", "item": SITE}]
    for i, (n, u) in enumerate(extra):
        l.append({"@type": "ListItem", "position": 3 + i, "name": n, "item": u})
    return {"@type": "BreadcrumbList", "itemListElement": l}

def usados():
    return [g for g in GRUPOS if any(grp(d) == g for d in T)]

def barra(actual=""):
    """Barra de temas: en el celular se desliza de lado; en la computadora ocupa varias filas."""
    it = [f'<a href="./"{" aria-current=\"page\"" if actual == "*" else ""}>Todos</a>']
    for g in usados():
        s = SEC[g]
        cur = ' aria-current="page"' if g == actual else ""
        it.append(f'<a href="{s["slug"]}.html"{cur}><span aria-hidden="true">{s["icon"]}</span> {e(g)}</a>')
    return f'<nav class="temas" aria-label="Temas de trámites">{"".join(it)}</nav>\n'

def tarjeta(d):
    return f'''<a class="tram" href="{d["slug"]}.html" data-g="{e(grp(d))}" data-b="{e((d["t"]+" "+d["ent"]+" "+grp(d)+" "+d["r"]).lower())}">
  <span class="ic" aria-hidden="true">{d["icon"]}</span>
  <span><small>{e(d["ent"])}</small><strong>{e(d["t"])}</strong><em>{e(d["costo"])}</em></span>
</a>'''

def boton(n, u, sec=False):
    c = "btn sec" if sec else "btn"
    if u.startswith("http"):
        return f'<a class="{c}" href="{e(u)}" target="_blank" rel="noopener">{e(n)} ↗</a>'
    return f'<a class="{c}" href="{e(u)}">{e(n)} →</a>'

def page(d):
    url = SITE + d["slug"] + ".html"
    g = grp(d); s = SEC[g]; surl = SITE + s["slug"] + ".html"
    nec = "".join(f"<li>{e(x)}</li>" for x in d["nec"])
    pasos = "".join(f"<li>{e(x)}</li>" for x in d["pasos"])
    main, *rest = d["links"]
    links = boton(*main) + "".join(boton(n, u, True) for n, u in rest)
    ojo = "".join(f"<li>{e(x)}</li>" for x in d["ojo"])
    src = " · ".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a>' for n, u in d["src"])
    verif = d.get("verif", "")
    otros = [x for x in T if grp(x) == g and x is not d]
    mas = "".join(f'<li><a href="{x["slug"]}.html"><span aria-hidden="true">{x["icon"]}</span> {e(x["t"])}</a></li>' for x in otros)
    mas = (f'<section class="card mas"><h2>Más trámites de {e(g)}</h2><ul>{mas}</ul>'
           f'<p><a href="{s["slug"]}.html">Ver la sección {e(g)} →</a> · <a href="./">Ver todos los trámites →</a></p></section>\n') if otros else \
          f'<section class="card mas"><h2>¿Buscas otro trámite?</h2><p><a href="./">Ver todos los trámites →</a></p></section>\n'
    desc = f'{d["t"]} paso a paso, explicado con palabras sencillas: requisitos, costo y enlace oficial ({d["ent"]}).'
    ld = {"@context": "https://schema.org", "@graph": [crumbs((g, surl), (d["t"], url)),
          {"@type": "Article", "headline": d["t"], "description": desc, "inLanguage": "es-PE",
           "dateModified": d.get("mod", "2026-11-10"), "mainEntityOfPage": url, "image": BASE + "og-imagen.png",
           "author": ORG, "publisher": ORG}]}
    body = barra(g) + f'''<nav class="miga" aria-label="Estás aquí"><a href="./">Trámites</a> <span aria-hidden="true">›</span> <a href="{s["slug"]}.html">{e(g)}</a></nav>
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
''' + mas
    return head(f'{d["t"]} | Trámite fácil Perú', desc, url, ld) + body + FOOT

def seccion(g):
    s = SEC[g]; url = SITE + s["slug"] + ".html"
    L = [d for d in T if grp(d) == g]
    ld = {"@context": "https://schema.org", "@graph": [crumbs((g, url)),
          {"@type": "ItemList", "name": f"Trámites de {g}", "numberOfItems": len(L),
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": d["t"], "url": SITE + d["slug"] + ".html"} for i, d in enumerate(L)]}]}
    body = barra(g) + f'''<nav class="miga" aria-label="Estás aquí"><a href="./">Trámites</a> <span aria-hidden="true">›</span> {e(g)}</nav>
<h1><span aria-hidden="true">{s["icon"]}</span> {e(g)}</h1>
<p class="lead">{e(s["desc"])} {len(L)} {"guía" if len(L) == 1 else "guías"} con requisitos, costo y enlace oficial.</p>
<div class="lista" id="lista">{"".join(tarjeta(d) for d in L)}</div>
<p><a class="btn sec volver" href="./">← Ver todos los temas</a></p>
'''
    return head(f'Trámites de {g} | Trámite fácil Perú', f'Guías sencillas de trámites de {g} en el Perú: {s["desc"]}', url, ld) + body + FOOT

def index():
    U = usados()
    tiles = "".join(f'''<a class="tema" href="{SEC[g]["slug"]}.html"><span class="ic" aria-hidden="true">{SEC[g]["icon"]}</span><span><strong>{e(g)}</strong><small>{sum(grp(d) == g for d in T)} guías</small></span></a>''' for g in U)
    grupos = "".join(f'''<section class="grupo" data-grupo="{e(g)}"><h2><a href="{SEC[g]["slug"]}.html"><span aria-hidden="true">{SEC[g]["icon"]}</span> {e(g)}</a></h2>
<div class="lista">{"".join(tarjeta(d) for d in T if grp(d) == g)}</div></section>''' for g in U)
    ld = {"@context": "https://schema.org", "@graph": [crumbs(),
          {"@type": "ItemList", "name": "Trámites del Perú paso a paso", "numberOfItems": len(T),
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": d["t"], "url": SITE + d["slug"] + ".html"} for i, d in enumerate(T)]}]}
    body = f'''<h1>Trámites del Perú, paso a paso y en palabras sencillas</h1>
<p class="lead">Elige tu trámite. Te decimos qué necesitas, cuánto cuesta y te llevamos a la página oficial para hacerlo. Gratis y sin registrarte. Ya hay {len(T)} guías y seguimos agregando más.</p>
<label class="buscar"><span>¿Qué trámite buscas?</span>
<input type="search" id="q" placeholder="Ej.: DNI, brevete, SIS" autocomplete="off"></label>
<p id="cuenta" class="cuenta" aria-live="polite"></p>
<p id="nada" class="hidden">No encontramos ese trámite. Prueba con otra palabra o mira los temas.</p>
<section id="temas-caja"><h2>O elige un tema</h2>
<div class="temas-grid">{tiles}</div></section>
<div id="lista">{grupos}</div>

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
      cuenta=document.getElementById('cuenta'), gr=document.querySelectorAll('.grupo'), caja=document.getElementById('temas-caja');
  function n(s){{return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}}
  function filtrar(){{
    var v=n(q.value.trim()), c=0;
    it.forEach(function(a){{var ok=!v||n(a.dataset.b).indexOf(v)>-1; a.hidden=!ok; if(ok)c++;}});
    gr.forEach(function(s){{s.hidden=!s.querySelector('.tram:not([hidden])');}});
    caja.hidden=!!v;
    nada.classList.toggle('hidden',c>0);
    cuenta.textContent=v?(c+(c===1?' trámite encontrado':' trámites encontrados')):'';
  }}
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
for g in usados():
    open(os.path.join(OUT, SEC[g]["slug"] + ".html"), "w").write(seccion(g))
open(os.path.join(OUT, "index.html"), "w").write(index())
print(len(T), "guías y", len(usados()), "secciones")
