/**
 * YO TE ENSEÑO, TÚ ME ENSEÑAS: crea todo en tu Google con un clic (gratis).
 *
 * Cómo usarlo:
 *   1. Entra a https://script.google.com y pulsa "Nuevo proyecto".
 *   2. Borra lo que aparece, pega TODO este archivo y guarda (ícono del disquete).
 *   3. Arriba elige la función "crearTodo" y pulsa "Ejecutar".
 *   4. Google pedirá permiso: "Revisar permisos" → tu cuenta → "Configuración avanzada"
 *      → "Ir a ... (no seguro)" → "Permitir". Sale ese aviso porque el script es tuyo
 *      y no lo revisó Google; solo trabaja dentro de tu cuenta.
 *   5. Te llegará un correo "Tus 3 enlaces". Pásaselos a Claude.
 *
 * ¿Ya lo habías ejecutado antes y solo estás actualizando el script?
 *   Pega esta versión nueva, guarda, elige la función "actualizar" y pulsa "Ejecutar".
 *
 * Qué crea:
 *   - Formulario "publicar mi oferta" y formulario "quiero contactar".
 *   - Hoja PRIVADA con las respuestas (ahí están correos y teléfonos; no la compartas).
 *   - Hoja PÚBLICA solo con las ofertas que apruebes (sin correos ni teléfonos).
 *   - Avisos a tu correo cuando llega una oferta nueva o alguien quiere contactar.
 *
 * Cómo funciona:
 *   - Verificación: cada oferta nueva te llega por correo con un enlace directo a su
 *     fila. Si está bien, eliges "Sí" en "Aprobado" y se publica. Si tiene algo
 *     sospechoso (enlaces, correos o teléfonos en el texto, precios o cobros), el
 *     correo te lo advierte.
 *   - Al aprobarla, el script avisa solo a la persona que su oferta ya está publicada.
 *   - Cuando alguien quiere aprender, el script envía solo un correo de presentación a
 *     las dos personas, con los consejos de seguridad. Tú recibes una copia oculta.
 *     Si el mensaje parece sospechoso, no lo envía y te lo manda a ti para que decidas.
 *
 * Para quitar una oferta: elige "No" en la columna "Aprobado" o borra la fila.
 */

const PRIVACIDAD_URL = 'https://simplelife-web.github.io/intercambio/privacidad.html';
const CATEGORIAS = ['Tecnología y celular', 'Cocina', 'Costura y tejido', 'Jardinería y plantas',
  'Oficios y reparaciones', 'Idiomas', 'Música y arte', 'Estudios y finanzas', 'Otros'];
const COLUMNAS_PUBLICAS = 9;   // marca temporal + 8 preguntas públicas
const COL_CORREO = 10;         // columna J
const COL_TELEFONO = 11;       // columna K
const COL_APROBADO = 13;       // columna M
const APROBAR_A_MANO = true;   // true: tú verificas cada oferta antes de publicarla
const PRESENTAR_SOLO = true;   // true: el script presenta a las personas por correo
const COL_AVISADO = 14;        // columna N: marca que ya se avisó a la persona
const WEB = 'https://simplelife-web.github.io/intercambio/';

function crearTodo() {
  const props = PropertiesService.getScriptProperties();
  if (props.getProperty('privadaId')) {
    throw new Error('Ya se creó todo antes. Revisa tu correo "Tus 3 enlaces" o ejecuta "enviarmeLosEnlaces".');
  }

  // 1) Formulario para publicar ofertas
  const f1 = FormApp.create('Yo te enseño, tú me enseñas: publicar mi oferta');
  f1.setDescription('Cuéntanos qué puedes enseñar y qué te gustaría aprender. Revisamos cada oferta antes de publicarla. Tu correo y tu teléfono nunca se publican.');
  f1.addTextItem().setTitle('Tu nombre o apodo').setRequired(true);
  f1.addMultipleChoiceItem().setTitle('Tu generación').setChoiceValues(['Menos de 30 años', '30 a 59 años', '60 años o más']).setRequired(true);
  f1.addTextItem().setTitle('Distrito y ciudad').setHelpText('Ejemplo: San Miguel, Lima').setRequired(true);
  f1.addTextItem().setTitle('¿Qué puedes enseñar?').setHelpText('Ejemplo: usar WhatsApp, cocina criolla, tejido a crochet').setRequired(true);
  f1.addListItem().setTitle('Categoría de lo que enseñas').setChoiceValues(CATEGORIAS).setRequired(true);
  f1.addTextItem().setTitle('¿Qué te gustaría aprender?').setRequired(true);
  f1.addMultipleChoiceItem().setTitle('Modalidad').setChoiceValues(['Presencial', 'Virtual', 'Ambas']).setRequired(true);
  f1.addParagraphTextItem().setTitle('Cuéntanos un poco de ti (opcional)').setHelpText('Se publica. No escribas aquí tu teléfono, correo ni dirección.');
  f1.addTextItem().setTitle('Correo electrónico (privado, no se publica)').setRequired(true)
    .setValidation(FormApp.createTextValidation().requireTextIsEmail().build());
  f1.addTextItem().setTitle('WhatsApp o teléfono (opcional, privado)');
  f1.addCheckboxItem().setTitle('Privacidad').setHelpText('Lee cómo cuidamos tus datos: ' + PRIVACIDAD_URL)
    .setChoiceValues(['Acepto la política de privacidad y soy mayor de 18 años (o participo con un adulto responsable)']).setRequired(true);
  f1.setConfirmationMessage('¡Gracias! Revisaremos tu oferta y la publicaremos pronto.');

  // 2) Formulario para contactar
  const f2 = FormApp.create('Yo te enseño, tú me enseñas: quiero contactar');
  f2.setDescription('Te pondremos en contacto por correo con la persona de la oferta.');
  const itemOferta = f2.addTextItem().setTitle('Oferta que te interesa').setRequired(true);
  f2.addTextItem().setTitle('Tu nombre').setRequired(true);
  f2.addTextItem().setTitle('Tu correo electrónico').setRequired(true)
    .setValidation(FormApp.createTextValidation().requireTextIsEmail().build());
  f2.addParagraphTextItem().setTitle('Tu mensaje: preséntate y cuenta qué puedes enseñar a cambio').setRequired(true);
  f2.addCheckboxItem().setTitle('Privacidad').setHelpText(PRIVACIDAD_URL)
    .setChoiceValues(['Acepto que Simplelife envíe mi mensaje y mi correo a la persona de la oferta']).setRequired(true);
  f2.setConfirmationMessage('¡Listo! Te escribiremos por correo para ponerte en contacto.');

  // 3) Hoja privada con las respuestas de los dos formularios
  const privada = SpreadsheetApp.create('Yo te enseño - respuestas (PRIVADO, no compartir)');
  f1.setDestination(FormApp.DestinationType.SPREADSHEET, privada.getId());
  f2.setDestination(FormApp.DestinationType.SPREADSHEET, privada.getId());
  SpreadsheetApp.flush();
  Utilities.sleep(3000);
  const hojaOfertas = hojaDeFormulario_(privada, f1);
  const hojaContactos = hojaDeFormulario_(privada, f2);
  hojaOfertas.setName('Ofertas');
  hojaContactos.setName('Contactos');
  privada.getSheets().forEach(function (h) {
    if (h.getSheetId() !== hojaOfertas.getSheetId() && h.getSheetId() !== hojaContactos.getSheetId()) privada.deleteSheet(h);
  });
  hojaOfertas.getRange(1, COL_APROBADO).setValue('Aprobado').setFontWeight('bold');
  hojaOfertas.getRange(1, COL_AVISADO).setValue('Avisado').setFontWeight('bold');
  hojaOfertas.getRange(2, COL_APROBADO, 999, 1).setDataValidation(
    SpreadsheetApp.newDataValidation().requireValueInList(['Sí', 'No'], true).build());

  // 4) Hoja pública (solo datos públicos de las ofertas aprobadas)
  const publica = SpreadsheetApp.create('Yo te enseño - ofertas publicadas (PÚBLICO)');
  publica.getSheets()[0].setName('Publicadas');
  DriveApp.getFileById(publica.getId()).setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);

  props.setProperties({
    privadaId: privada.getId(), publicaId: publica.getId(),
    f1Id: f1.getId(), f2Id: f2.getId(),
    prefijado: f2.createResponse().withItemResponse(itemOferta.createResponse('OFERTA')).toPrefilledUrl()
  });

  // 5) Automatismos
  crearAutomatismos_();
  sincronizar();
  enviarmeLosEnlaces();
}

// Ejecuta esta función una vez después de pegar una versión nueva del script
function actualizar() {
  const p = PropertiesService.getScriptProperties();
  SpreadsheetApp.openById(p.getProperty('privadaId')).getSheetByName('Ofertas')
    .getRange(1, COL_AVISADO).setValue('Avisado').setFontWeight('bold');
  crearAutomatismos_();
  sincronizar();
  Logger.log('Listo: automatismos actualizados.');
}

function crearAutomatismos_() {
  const p = PropertiesService.getScriptProperties();
  ScriptApp.getProjectTriggers().forEach(function (t) { ScriptApp.deleteTrigger(t); });
  const privada = SpreadsheetApp.openById(p.getProperty('privadaId'));
  ScriptApp.newTrigger('alEditar').forSpreadsheet(privada).onEdit().create();
  ScriptApp.newTrigger('sincronizar').timeBased().everyHours(1).create();
  ScriptApp.newTrigger('alResponder').forSpreadsheet(privada).onFormSubmit().create();
}

function hojaDeFormulario_(ss, form) {
  const id = form.getId();
  const h = ss.getSheets().filter(function (s) { return (s.getFormUrl() || '').indexOf(id) >= 0; })[0];
  if (!h) throw new Error('No encontré la pestaña del formulario. Vuelve a intentarlo en un minuto.');
  return h;
}

// Copia a la hoja pública solo las ofertas con "Sí" en Aprobado, sin correos ni teléfonos
function sincronizar() {
  const p = PropertiesService.getScriptProperties();
  const ofertas = SpreadsheetApp.openById(p.getProperty('privadaId')).getSheetByName('Ofertas');
  const datos = ofertas.getDataRange().getValues();
  const titulos = ['Código'].concat(datos[0].slice(0, COLUMNAS_PUBLICAS));
  const filas = [titulos];
  for (let i = 1; i < datos.length; i++) {
    if (String(datos[i][COL_APROBADO - 1]).trim() !== 'Sí') continue;
    const fila = datos[i].slice(0, COLUMNAS_PUBLICAS);
    if (fila[0] instanceof Date) fila[0] = Utilities.formatDate(fila[0], 'America/Lima', 'dd/MM/yyyy');
    filas.push(['O' + (i + 1)].concat(fila));
  }
  const pub = SpreadsheetApp.openById(p.getProperty('publicaId')).getSheetByName('Publicadas');
  pub.clearContents();
  pub.getRange(1, 1, filas.length, titulos.length).setValues(filas);
}

// Busca señales de riesgo: enlaces, correos o teléfonos en el texto, precios o cobros
function motivoSospecha_(texto) {
  const t = String(texto || '');
  if (/https?:|www\.|\.com\b/i.test(t)) return 'tiene un enlace';
  if (/@/.test(t)) return 'tiene un correo en el texto';
  if (/\d[\d\s.-]{6,}\d/.test(t)) return 'parece tener un número de teléfono o de cuenta';
  if (/\bS\/|soles|d[oó]lares|precio|cobro|cobrar|tarifa|dep[oó]sito|transferencia|cuenta bancaria|tarjeta/i.test(t)) return 'habla de dinero o cobros';
  return '';
}

// Se ejecuta cada vez que alguien llena cualquiera de los dos formularios
function alResponder(e) {
  const hoja = e.range.getSheet().getName();
  if (hoja === 'Ofertas') alPublicar_(e);
  else if (hoja === 'Contactos') alContactar_(e);
}

function alPublicar_(e) {
  const p = PropertiesService.getScriptProperties();
  const yo = Session.getEffectiveUser().getEmail();
  const v = e.range.getValues()[0];
  const hojaOfertas = e.range.getSheet();
  const fila = e.range.getRow();
  const nombre = v[1], ensena = v[4], aprende = v[6], sobre = v[8];
  const sospecha = motivoSospecha_([nombre, v[3], ensena, aprende, sobre].join(' '));

  if (!APROBAR_A_MANO && !sospecha) {
    hojaOfertas.getRange(fila, COL_APROBADO).setValue('Sí');
    avisarPublicada_(hojaOfertas, fila);
    sincronizar();
    return;
  }
  const enlace = SpreadsheetApp.openById(p.getProperty('privadaId')).getUrl() +
    '#gid=' + hojaOfertas.getSheetId() + '&range=M' + fila;
  MailApp.sendEmail(yo, (sospecha ? '⚠️ Revisa con cuidado: ' : 'Nueva oferta para verificar: ') + ensena,
    (sospecha ? 'Atención: esta oferta ' + sospecha + '.\n\n' : '') +
    nombre + ' (' + v[2] + ', ' + v[3] + ')\nEnseña: ' + ensena + ' (' + v[5] + ')\nQuiere aprender: ' + aprende +
    '\nModalidad: ' + v[7] + '\nSobre ti: ' + (sobre || '-') +
    '\n\nSi está bien, abre este enlace y elige "Sí" en Aprobado. Se publica y la persona recibe un aviso:\n' + enlace);
}

// Se ejecuta cuando editas la hoja privada: publica lo aprobado y avisa a la persona
function alEditar(e) {
  if (e && e.range && e.range.getSheet().getName() === 'Ofertas' && e.range.getColumn() <= COL_APROBADO &&
      e.range.getLastColumn() >= COL_APROBADO) {
    const hoja = e.range.getSheet();
    for (let f = e.range.getRow(); f <= e.range.getLastRow(); f++) {
      if (f > 1 && String(hoja.getRange(f, COL_APROBADO).getValue()).trim() === 'Sí') avisarPublicada_(hoja, f);
    }
  }
  sincronizar();
}

function avisarPublicada_(hoja, fila) {
  if (!PRESENTAR_SOLO || hoja.getRange(fila, COL_AVISADO).getValue()) return;
  const v = hoja.getRange(fila, 1, 1, COL_APROBADO).getValues()[0];
  if (!v[COL_CORREO - 1]) return;
  MailApp.sendEmail(v[COL_CORREO - 1], 'Tu oferta ya está publicada en Yo te enseño, tú me enseñas',
    'Hola, ' + v[1] + ':\n\nTu oferta "' + v[4] + '" ya aparece en ' + WEB + '\n\n' +
    'Cuando alguien quiera aprender contigo, te enviaremos un correo para presentarte. ' +
    'Tu correo y tu teléfono no se publican.\n\nSi quieres borrar tu oferta, responde a este correo.\n\nEquipo Simplelife',
    { name: 'Simplelife', replyTo: Session.getEffectiveUser().getEmail() });
  hoja.getRange(fila, COL_AVISADO).setValue(new Date());
}

function alContactar_(e) {
  const p = PropertiesService.getScriptProperties();
  const yo = Session.getEffectiveUser().getEmail();
  const v = e.range.getValues()[0];
  const oferta = String(v[1] || ''), quien = v[2], suCorreo = v[3], mensaje = v[4];
  const m = oferta.match(/^O(\d+)/);
  let datos = null;
  if (m) datos = SpreadsheetApp.openById(p.getProperty('privadaId')).getSheetByName('Ofertas')
    .getRange(+m[1], 1, 1, COL_APROBADO).getValues()[0];
  const valida = datos && datos[1] && String(datos[COL_APROBADO - 1]).trim() === 'Sí';
  const sospecha = motivoSospecha_(mensaje);

  if (PRESENTAR_SOLO && valida && !sospecha) {
    const nombreOferta = datos[1], correoOferta = datos[COL_CORREO - 1], ensena = datos[4];
    MailApp.sendEmail(correoOferta, quien + ' quiere aprender contigo: ' + ensena,
      'Hola, ' + nombreOferta + ' y ' + quien + ':\n\n' +
      quien + ' vio la oferta de ' + nombreOferta + ' ("' + ensena + '") en Yo te enseño, tú me enseñas y quiere aprender. Su mensaje:\n\n' +
      '"' + mensaje + '"\n\n' +
      'Para ponerse de acuerdo, respondan a este correo ("Responder a todos").\n\n' +
      'Consejos para un intercambio seguro:\n' +
      '- La primera vez, conversen por videollamada o reúnanse en un lugar público.\n' +
      '- Avisen a un familiar o amigo con quién y dónde se van a reunir.\n' +
      '- Aquí nadie cobra. Si alguien pide dinero, desconfíen y avísennos.\n' +
      '- Nunca compartan contraseñas, claves del banco ni códigos que lleguen por mensaje.\n\n' +
      '¡Que disfruten el intercambio!\nEquipo Simplelife\n' + WEB,
      { name: 'Simplelife', cc: suCorreo, bcc: yo, replyTo: suCorreo + ',' + correoOferta });
  } else {
    let motivo = !valida ? 'no encontré la oferta o ya no está aprobada' : (sospecha ? 'el mensaje ' + sospecha : 'la presentación automática está apagada');
    let datosOferta = datos && datos[1] ? '\nPersona de la oferta: ' + datos[1] + '\nSu correo: ' + datos[COL_CORREO - 1] +
      (datos[COL_TELEFONO - 1] ? '\nSu teléfono: ' + datos[COL_TELEFONO - 1] : '') : '';
    MailApp.sendEmail(yo, 'Contacto en espera de tu revisión: ' + oferta.slice(0, 60),
      'No lo presenté solo porque ' + motivo + '.\n\nOferta: ' + oferta + datosOferta + '\n\n' +
      'Quien escribe: ' + quien + '\nSu correo: ' + suCorreo + '\nMensaje: ' + mensaje + '\n\n' +
      'Si está bien, escribe tú un correo a la persona de la oferta con copia a quien escribe.');
  }
}

// Te envía por correo los 3 enlaces para la página web
function enviarmeLosEnlaces() {
  const p = PropertiesService.getScriptProperties();
  const texto =
    'formPublicar: ' + FormApp.openById(p.getProperty('f1Id')).getPublishedUrl() + '\n\n' +
    'formContacto: ' + p.getProperty('prefijado') + '\n\n' +
    'hojaCSV: https://docs.google.com/spreadsheets/d/' + p.getProperty('publicaId') + '/gviz/tq?tqx=out:csv&headers=1&sheet=Publicadas\n\n' +
    'Hoja PRIVADA (solo para ti, aquí apruebas ofertas): ' + SpreadsheetApp.openById(p.getProperty('privadaId')).getUrl();
  Logger.log(texto);
  MailApp.sendEmail(Session.getEffectiveUser().getEmail(), 'Tus 3 enlaces de Yo te enseño, tú me enseñas', texto);
}
