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
 * Qué crea:
 *   - Formulario "publicar mi oferta" y formulario "quiero contactar".
 *   - Hoja PRIVADA con las respuestas (ahí están correos y teléfonos; no la compartas).
 *   - Hoja PÚBLICA solo con las ofertas que apruebes (sin correos ni teléfonos).
 *   - Avisos a tu correo cuando llega una oferta nueva o alguien quiere contactar.
 *
 * Para aprobar una oferta: en la hoja privada, pestaña de ofertas, elige "Sí" en la
 * columna "Aprobado". Para quitarla, elige "No" o borra la fila.
 */

const PRIVACIDAD_URL = 'https://simplelife-web.github.io/intercambio/privacidad.html';
const CATEGORIAS = ['Tecnología y celular', 'Cocina', 'Costura y tejido', 'Jardinería y plantas',
  'Oficios y reparaciones', 'Idiomas', 'Música y arte', 'Estudios y finanzas', 'Otros'];
const COLUMNAS_PUBLICAS = 9;   // marca temporal + 8 preguntas públicas
const COL_CORREO = 10;         // columna J
const COL_TELEFONO = 11;       // columna K
const COL_APROBADO = 13;       // columna M

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
  ScriptApp.newTrigger('sincronizar').forSpreadsheet(privada).onEdit().create();
  ScriptApp.newTrigger('sincronizar').timeBased().everyHours(1).create();
  ScriptApp.newTrigger('alPublicar').forForm(f1).onFormSubmit().create();
  ScriptApp.newTrigger('alContactar').forForm(f2).onFormSubmit().create();

  sincronizar();
  enviarmeLosEnlaces();
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

// Aviso por correo cuando llega una oferta nueva para revisar
function alPublicar(e) {
  const p = PropertiesService.getScriptProperties();
  const r = {};
  e.response.getItemResponses().forEach(function (x) { r[x.getItem().getTitle()] = x.getResponse(); });
  MailApp.sendEmail(Session.getEffectiveUser().getEmail(),
    'Nueva oferta para revisar: ' + r['¿Qué puedes enseñar?'],
    'Llegó una oferta de ' + r['Tu nombre o apodo'] + ' (' + r['Distrito y ciudad'] + ').\n\n' +
    'Enseña: ' + r['¿Qué puedes enseñar?'] + '\nQuiere aprender: ' + r['¿Qué te gustaría aprender?'] + '\n' +
    'Sobre ti: ' + (r['Cuéntanos un poco de ti (opcional)'] || '-') + '\n\n' +
    'Si está bien, elige "Sí" en la columna Aprobado:\n' +
    SpreadsheetApp.openById(p.getProperty('privadaId')).getUrl());
}

// Aviso por correo cuando alguien quiere contactar, con todo listo para presentarlos
function alContactar(e) {
  const p = PropertiesService.getScriptProperties();
  const r = {};
  e.response.getItemResponses().forEach(function (x) { r[x.getItem().getTitle()] = x.getResponse(); });
  const oferta = String(r['Oferta que te interesa'] || '');
  let datosOferta = 'No encontré el código de la oferta. Búscala a mano en la hoja privada.';
  const m = oferta.match(/^O(\d+)/);
  if (m) {
    const fila = SpreadsheetApp.openById(p.getProperty('privadaId')).getSheetByName('Ofertas')
      .getRange(+m[1], 1, 1, COL_APROBADO).getValues()[0];
    datosOferta = 'Persona de la oferta: ' + fila[1] + '\nSu correo: ' + fila[COL_CORREO - 1] +
      (fila[COL_TELEFONO - 1] ? '\nSu teléfono: ' + fila[COL_TELEFONO - 1] : '');
  }
  MailApp.sendEmail(Session.getEffectiveUser().getEmail(),
    'Alguien quiere aprender: ' + oferta.slice(0, 80),
    'Oferta: ' + oferta + '\n' + datosOferta + '\n\n' +
    'Quien escribe: ' + r['Tu nombre'] + '\nSu correo: ' + r['Tu correo electrónico'] + '\n' +
    'Mensaje: ' + r['Tu mensaje: preséntate y cuenta qué puedes enseñar a cambio'] + '\n\n' +
    'Si el mensaje está bien, escribe UN correo a la persona de la oferta, con copia a quien escribe, ' +
    'pegando su mensaje y recordándoles los consejos de seguridad.');
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
