// Robot de "¿Qué hago hoy?"
// Cada mañana revisa las páginas OFICIALES de quehagohoy/fuentes.json,
// lee su agenda si la publican en formato abierto (calendario de WordPress o RSS)
// y guarda los eventos en quehagohoy/eventos.json. Cada evento lleva el enlace
// a su publicación oficial. Respeta el robots.txt de cada página.
// Uso: node .github/robot/buscar-eventos.mjs   (Node 20 o más, sin instalar nada)

import { readFileSync, writeFileSync, existsSync, appendFileSync } from "node:fs";

const RAIZ = new URL("../../", import.meta.url);
const ARCHIVO = new URL("quehagohoy/eventos.json", RAIZ);
const { fuentes } = JSON.parse(readFileSync(new URL("quehagohoy/fuentes.json", RAIZ), "utf8"));
const UA = "SimplelifeBot/1.0 (+https://simplelife-web.github.io/quehagohoy/)";
const DIAS_NOVEDAD = 15;    // si no encontramos fecha, mostramos la publicación 15 días
const DIAS_ADELANTE = 120;  // no guardamos eventos a más de 4 meses

// ---------- fechas (hora de Lima) ----------
const hoyLima = () => new Date(new Date().toLocaleString("en-US", { timeZone: "America/Lima" }));
const iso = (d) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
const HOY = hoyLima(); HOY.setHours(0, 0, 0, 0);
const HOY_ISO = iso(HOY);
const MESES = { enero: 0, febrero: 1, marzo: 2, abril: 3, mayo: 4, junio: 5, julio: 6, agosto: 7, septiembre: 8, setiembre: 8, octubre: 9, noviembre: 10, diciembre: 11 };

// ---------- red ----------
async function traer(url, tipo = "text") {
  try {
    const r = await fetch(url, { headers: { "User-Agent": UA, "Accept": tipo === "json" ? "application/json" : "application/rss+xml, application/xml, text/xml, */*" }, redirect: "follow", signal: AbortSignal.timeout(20000) });
    if (!r.ok) return { ok: false, status: r.status };
    const texto = await r.text();
    return { ok: true, status: r.status, texto, ctype: r.headers.get("content-type") || "" };
  } catch (e) { return { ok: false, status: String(e.cause?.code || e.name || e) }; }
}

const robotsCache = new Map();
async function permitido(url) {
  const u = new URL(url);
  if (!robotsCache.has(u.origin)) {
    const r = await traer(u.origin + "/robots.txt");
    robotsCache.set(u.origin, r.ok ? leerRobots(r.texto) : []);
  }
  const reglas = robotsCache.get(u.origin);
  const ruta = u.pathname + u.search;
  let mejor = null;
  for (const [permite, prefijo] of reglas) {
    if (prefijo && ruta.startsWith(prefijo) && (!mejor || prefijo.length > mejor[1].length)) mejor = [permite, prefijo];
  }
  return !mejor || mejor[0];
}
function leerRobots(txt) {
  // Reglas del grupo "*" (o de nuestro robot). Devuelve [[permite, prefijo], ...]
  const reglas = []; let aplica = false, enAgentes = false;
  for (let linea of txt.split(/\r?\n/)) {
    linea = linea.replace(/#.*/, "").trim(); if (!linea) continue;
    const [k, ...v] = linea.split(":"); const clave = k.trim().toLowerCase(); const valor = v.join(":").trim();
    if (clave === "user-agent") {
      const coincide = valor === "*" || /simplelife/i.test(valor);
      aplica = enAgentes ? (aplica || coincide) : coincide; enAgentes = true;
    } else {
      enAgentes = false;
      if (!aplica) continue;
      if (clave === "disallow" && valor) reglas.push([false, valor.replace(/\*.*$/, "")]);
      if (clave === "allow" && valor) reglas.push([true, valor.replace(/\*.*$/, "")]);
    }
  }
  return reglas;
}

// ---------- texto ----------
const ENT = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'", nbsp: " ", aacute: "á", eacute: "é", iacute: "í", oacute: "ó", uacute: "ú", ntilde: "ñ", Aacute: "Á", Eacute: "É", Iacute: "Í", Oacute: "Ó", Uacute: "Ú", Ntilde: "Ñ", uuml: "ü", iexcl: "¡", iquest: "¿", laquo: "«", raquo: "»", ndash: "–", mdash: "—", hellip: "…", rsquo: "’", lsquo: "‘", ldquo: "“", rdquo: "”" };
function limpiar(s = "") {
  return String(s)
    .replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, "$1")
    .replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(+n))
    .replace(/&#x([0-9a-f]+);/gi, (_, n) => String.fromCodePoint(parseInt(n, 16)))
    .replace(/&([a-z]+);/gi, (m, n) => ENT[n] ?? m)
    .replace(/\s+/g, " ").trim();
}
const corto = (s, n = 220) => (s.length > n ? s.slice(0, n).replace(/\s+\S*$/, "") + "…" : s);

// Palabras de actividad: deben estar en el TÍTULO
const RE_EVENTO = /\b(exposici[oó]n|muestra|taller(es)?|concierto|recital|feria|festival|funci[oó]n|obra|teatro|cine|cineclub|pel[ií]cula|proyecci[oó]n|charla|conversatorio|conferencia|presentaci[oó]n de(l)? libro|cuentacuentos|visita guiada|recorrido|danza|baile|m[uú]sica|curso|ciclo de|seminario|festival|noche de|tarde de|serenata|verbena|carnaval|maratón|corso)/i;
// Señales de que es una invitación a algo que viene (no un resumen de algo pasado)
const RE_INVITA = /\b(invita|inv[ií]tanos|participa|inscr[ií]bete|inscripci[oó]n|inscripciones|no te pierdas|ven a|asiste|te esperamos|programaci[oó]n|agenda|se realizar[aá]|se llevar[aá] a cabo|presentar[aá]|ofrecer[aá]|tendr[aá] lugar|hasta el|del \d{1,2} al \d{1,2}|este (lunes|martes|mi[eé]rcoles|jueves|viernes|s[aá]bado|domingo|fin de semana)|pr[oó]xim[oa]|ingreso libre|entrada libre|gratis|gratuit[oa])\b/i;
// Resúmenes de algo que ya pasó o noticias que no son planes
const RE_PASADO = /\b(se llen[oó]|celebr[oó]|realiz[oó]|inaugur[oó]|entreg[oó]|particip[oó]|reuni[oó]|clausur[oó]|culmin[oó]|congreg[oó]|recibi[oó]|disfrutaron|asistieron|fue un [eé]xito|balance)\b/i;
const RE_NO_PLAN = /\b(subasta|licitaci[oó]n|convocatoria|cas n|proceso de selecci[oó]n|alcalde|regidor|gerente|fiscaliza|operativo|prevenir|violencia|denuncia|obras? de (pistas|veredas|agua)|comunicado|transparencia|presupuesto)\b/i;
// Si el título nombra otra región, el evento no es en Lima
const RE_OTRA_REGION = /\b(amazonas|[aá]ncash|apur[ií]mac|arequipa|ayacucho|cajamarca|cusco|cuzco|huancavelica|hu[aá]nuco|ica|jun[ií]n|la libertad|lambayeque|loreto|madre de dios|moquegua|pasco|piura|puno|san mart[ií]n|tacna|tumbes|ucayali|trujillo|chiclayo|iquitos|huancayo|raquina)\b/i;
const RE_GRATIS = /\b(gratis|gratuit[oa]s?|ingreso libre|entrada libre|libre acceso|acceso libre|sin costo)\b/i;

function tipoDe(t, base) {
  if (/concierto|recital|m[uú]sica|orquesta|coro/i.test(t)) return "concierto";
  if (/taller|curso|clase/i.test(t)) return "taller";
  if (/feria/i.test(t)) return "feria";
  if (/cine|pel[ií]cula|proyecci[oó]n/i.test(t)) return "cine";
  if (/teatro|obra|danza|baile|funci[oó]n/i.test(t)) return "teatro";
  if (/exposici[oó]n|muestra/i.test(t)) return "exposicion";
  return base || "cultura";
}
function publicoDe(t) {
  const p = [];
  if (/j[oó]venes|universitari|adolescente/i.test(t)) p.push("j");
  if (/niñ[oa]s|familia|infantil|cuentacuentos|escolares/i.test(t)) p.push("f");
  if (/adult[oa]s? mayor|tercera edad/i.test(t)) p.push("m");
  return p;
}
function precioDe(t, cost) {
  if (cost) return RE_GRATIS.test(cost) || /^0+(\.0+)?$/.test(cost) ? "Gratis" : limpiar(cost);
  if (RE_GRATIS.test(t)) return "Gratis";
  const m = t.match(/S\/\.?\s?\d+(?:[.,]\d{1,2})?/);
  return m ? "Desde " + m[0].replace(/\s+/, " ") : "";
}

// Fechas en español dentro del texto: "12 de noviembre", "del 5 al 20 de diciembre de 2026"
function fechasEn(texto, publicado) {
  const out = [];
  const re = /(\d{1,2})(?:\s*(?:,|y|al|a|-|–)\s*(\d{1,2}))?\s+de\s+(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)(?:\s+(?:de|del)\s+(\d{4}))?/gi;
  let m;
  while ((m = re.exec(texto))) {
    const mes = MESES[m[3].toLowerCase()];
    for (const d of [m[1], m[2]].filter(Boolean)) {
      const dia = +d; if (dia < 1 || dia > 31) continue;
      let anio = m[4] ? +m[4] : (publicado || HOY).getFullYear();
      let f = new Date(anio, mes, dia);
      if (!m[4] && publicado && f < new Date(publicado.getTime() - 60 * 864e5)) f = new Date(anio + 1, mes, dia);
      out.push(f);
    }
  }
  return out.sort((a, b) => a - b);
}

// ---------- lectores ----------
async function leerCalendarioWP(f) {
  const url = `${f.web}/wp-json/tribe/events/v1/events?per_page=50&start_date=${HOY_ISO}`;
  if (!(await permitido(url))) return { metodo: "calendario", bloqueado: true, eventos: [] };
  const r = await traer(url, "json");
  if (!r.ok) return null;
  let j; try { j = JSON.parse(r.texto); } catch { return null; }
  if (!Array.isArray(j.events)) return null;
  const eventos = j.events.map((e) => {
    const titulo = limpiar(e.title), texto = titulo + " " + limpiar(e.excerpt || e.description || "");
    const v = e.venue && !Array.isArray(e.venue) ? e.venue : {};
    return {
      titulo, url: e.url, fecha: (e.start_date || "").slice(0, 10), fechaFin: (e.end_date || "").slice(0, 10),
      hora: e.all_day ? "" : (e.start_date || "").slice(11, 16),
      lugar: limpiar(v.venue || ""), direccion: limpiar([v.address, v.city].filter(Boolean).join(", ")),
      lat: v.geo_lat ? +v.geo_lat : null, lon: v.geo_lng ? +v.geo_lng : null,
      precio: precioDe(texto, e.cost), tipo: tipoDe(texto, f.tipo), publico: publicoDe(texto),
      resumen: corto(limpiar(e.excerpt || e.description || "")),
    };
  });
  return { metodo: "calendario", eventos };
}

function itemsRSS(xml) {
  const bloques = xml.match(/<item\b[\s\S]*?<\/item>/gi) || xml.match(/<entry\b[\s\S]*?<\/entry>/gi) || [];
  const campo = (b, ...tags) => { for (const t of tags) { const m = b.match(new RegExp(`<${t}\\b[^>]*>([\\s\\S]*?)<\\/${t}>`, "i")); if (m) return m[1]; } return ""; };
  return bloques.map((b) => {
    let link = limpiar(campo(b, "link"));
    if (!link) { const m = b.match(/<link\b[^>]*href="([^"]+)"/i); link = m ? m[1] : ""; }
    return {
      titulo: limpiar(campo(b, "title")), link: link.replace(/&amp;/g, "&"),
      fecha: limpiar(campo(b, "pubDate", "published", "updated", "dc:date")),
      texto: limpiar(campo(b, "description", "summary")) , cuerpo: limpiar(campo(b, "content:encoded", "content")),
    };
  });
}

async function leerRSS(f) {
  for (const ruta of ["/feed/", "/rss.xml", "/feed", "/index.php/feed/"]) {
    const url = f.web + ruta;
    if (!(await permitido(url))) continue;
    const r = await traer(url);
    if (!r.ok || !/<(rss|feed|rdf:RDF)\b/i.test(r.texto.slice(0, 2000))) continue;
    const eventos = [];
    for (const it of itemsRSS(r.texto)) {
      if (!it.titulo || !/^https?:\/\//.test(it.link)) continue;
      const pub = it.fecha ? new Date(it.fecha) : null;
      const publicado = pub && !isNaN(pub) ? pub : null;
      const texto = `${it.titulo}. ${it.texto} ${it.cuerpo}`;
      // Solo actividades a las que se puede ir en Lima, no noticias institucionales
      if (!RE_EVENTO.test(it.titulo)) continue;
      if (RE_PASADO.test(it.titulo) || RE_NO_PLAN.test(it.titulo) || RE_OTRA_REGION.test(it.titulo)) continue;
      const corta = `${it.titulo}. ${it.texto}`;
      if (!RE_INVITA.test(corta + " " + it.cuerpo.slice(0, 1500))) continue;
      const fechas = fechasEn(corta + " " + it.cuerpo.slice(0, 800), publicado);
      let fecha = "", fechaFin = "";
      if (fechas.length) {
        const primera = fechas[0], ultima = fechas[fechas.length - 1];
        if (ultima < HOY) continue; // ya pasó
        if (primera - HOY > DIAS_ADELANTE * 864e5) continue; // demasiado lejos (suele ser un error de lectura)
        fecha = iso(primera);
        // Un rango solo si es corto (hasta 3 meses); si no, suele ser una fecha suelta del texto
        if (iso(ultima) !== fecha && ultima - primera <= 92 * 864e5) fechaFin = iso(ultima);
        if (!fechaFin && primera < HOY) continue;
      } else {
        if (!publicado || HOY - publicado > DIAS_NOVEDAD * 864e5) continue;
      }
      eventos.push({
        titulo: it.titulo, url: it.link, fecha, fechaFin, hora: "",
        publicado: publicado ? iso(publicado) : "",
        lugar: "", direccion: "", lat: null, lon: null,
        precio: precioDe(texto), tipo: tipoDe(texto, f.tipo), publico: publicoDe(texto),
        resumen: corto(it.texto || it.cuerpo),
      });
    }
    return { metodo: "rss", eventos };
  }
  return null;
}

// ---------- principal ----------
const todos = [], informe = [];
for (const f of fuentes) {
  let res = null;
  try { res = (await leerCalendarioWP(f)) || (await leerRSS(f)); }
  catch (e) { console.log(`! ${f.nombre}: error ${e.message}`); }
  if (!res) { informe.push({ fuente: f.nombre, estado: "sin agenda abierta", n: 0 }); console.log(`- ${f.nombre}: no publica agenda en formato abierto (se salta)`); continue; }
  if (res.bloqueado) { informe.push({ fuente: f.nombre, estado: "su robots.txt no lo permite", n: 0 }); console.log(`- ${f.nombre}: robots.txt no lo permite (se respeta)`); continue; }
  for (const e of res.eventos) {
    todos.push({ ...e, fuente: f.nombre, fuenteWeb: f.web, distrito: f.distrito, lat: e.lat ?? f.lat, lon: e.lon ?? f.lon });
  }
  informe.push({ fuente: f.nombre, estado: res.metodo, n: res.eventos.length });
  console.log(`✓ ${f.nombre}: ${res.metodo}, ${res.eventos.length} actividades`);
}

// quitar repetidos y vencidos, ordenar por fecha
const vistos = new Set();
const eventos = todos
  .filter((e) => { const k = e.url; if (vistos.has(k)) return false; vistos.add(k); return true; })
  .filter((e) => (e.fechaFin || e.fecha || HOY_ISO) >= HOY_ISO)
  .sort((a, b) => (a.fecha || a.publicado || "9").localeCompare(b.fecha || b.publicado || "9"))
  .slice(0, 300);

const anterior = existsSync(ARCHIVO) ? JSON.parse(readFileSync(ARCHIVO, "utf8")) : {};
const igual = JSON.stringify(anterior.eventos || []) === JSON.stringify(eventos) && JSON.stringify(anterior.fuentes || []) === JSON.stringify(informe);
if (igual) console.log("\nSin cambios en los eventos.");
else {
  writeFileSync(ARCHIVO, JSON.stringify({ actualizado: new Date().toISOString(), eventos, fuentes: informe }, null, 1) + "\n");
  console.log(`\nGuardados ${eventos.length} eventos en quehagohoy/eventos.json`);
}
if (process.env.GITHUB_STEP_SUMMARY) {
  appendFileSync(process.env.GITHUB_STEP_SUMMARY, `## Robot ¿Qué hago hoy?\n\n| Fuente | Cómo se leyó | Actividades |\n|---|---|---|\n${informe.map((i) => `| ${i.fuente} | ${i.estado} | ${i.n} |`).join("\n")}\n\nTotal guardado: ${eventos.length}\n`);
}
