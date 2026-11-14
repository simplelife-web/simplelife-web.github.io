// Simplelife · lector de subtítulos de YouTube
// Corre gratis en Cloudflare Workers (100 000 consultas al día en el plan gratuito).
// Recibe ?v=ID_DEL_VIDEO&lang=es y devuelve el texto del video en JSON.
// Prueba tres caminos, uno tras otro, por si YouTube bloquea alguno.
// Cómo instalarlo: crea un Worker en dash.cloudflare.com, pega este código y pulsa «Implementar».
// Luego pon su dirección (https://…workers.dev) en la constante SERVIDOR de youtube/index.html.

const PERMITIDOS = ['https://simplelife-web.github.io', 'http://localhost', 'http://127.0.0.1'];
const NAVEGADOR = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const ANDROID_VER = '20.10.38';

export default {
  async fetch(req, env, ctx) {
    const origen = req.headers.get('Origin') || '';
    const cors = {
      'Access-Control-Allow-Origin': PERMITIDOS.some((p) => origen.startsWith(p)) ? origen : PERMITIDOS[0],
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      Vary: 'Origin',
    };
    if (req.method === 'OPTIONS') return new Response(null, { headers: cors });

    const url = new URL(req.url);
    const v = url.searchParams.get('v') || '';
    if (!/^[\w-]{11}$/.test(v)) return json({ error: 'enlace', mensaje: 'Simplelife: falta ?v=ID del video' }, 400, cors);
    const lang = (url.searchParams.get('lang') || 'es').replace(/[^a-zA-Z-]/g, '').slice(0, 8) || 'es';

    // Si el mismo video ya se pidió hoy, se responde al instante desde la memoria de Cloudflare.
    const cache = caches.default;
    const llave = new Request(`https://memoria.simplelife/${v}/${lang}`);
    const guardado = await cache.match(llave);
    if (guardado) return json(await guardado.json(), 200, cors);

    const errores = [];
    let res = null;
    for (const [nombre, metodo] of [['apps', porApps], ['web', porWeb], ['transcripcion', porTranscripcion], ['tactiq', porTactiq]]) {
      try {
        res = await metodo(v, lang);
        if (res && res.segs.length) break;
        errores.push(nombre + ': vacío');
      } catch (e) {
        errores.push(nombre + ': ' + (e && e.message ? e.message : e));
      }
      res = null;
    }
    if (!res) return json({ error: 'sin-texto', detalle: errores }, 404, cors);

    res.metodo = res.metodo || '';
    ctx.waitUntil(cache.put(llave, new Response(JSON.stringify(res), { headers: { 'Cache-Control': 'public, max-age=86400' } })));
    return json(res, 200, cors);
  },
};

function json(obj, status, extra) {
  return new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json; charset=utf-8', ...extra } });
}

// ---------- camino 1: las apps de YouTube (varias, por si YouTube frena alguna) ----------
const CLIENTES = [
  { nombre: 'android_vr', id: '28', ua: 'com.google.android.apps.youtube.vr.oculus/1.62.27 (Linux; U; Android 12L; eureka-user Build/SQ3A.220605.009.A1) gzip',
    client: { clientName: 'ANDROID_VR', clientVersion: '1.62.27', deviceMake: 'Oculus', deviceModel: 'Quest 3', androidSdkVersion: 32, osName: 'Android', osVersion: '12L' } },
  { nombre: 'ios', id: '5', ua: 'com.google.ios.youtube/20.10.4 (iPhone16,2; U; CPU iOS 18_3_2 like Mac OS X;)',
    client: { clientName: 'IOS', clientVersion: '20.10.4', deviceMake: 'Apple', deviceModel: 'iPhone16,2', osName: 'iPhone', osVersion: '18.3.2.22D82' } },
  { nombre: 'tv', id: '85', ua: 'Mozilla/5.0 (PlayStation; PlayStation 4/12.00) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
    client: { clientName: 'TVHTML5_SIMPLY_EMBEDDED_PLAYER', clientVersion: '2.0' }, embed: true },
  { nombre: 'web_embed', id: '56', ua: NAVEGADOR,
    client: { clientName: 'WEB_EMBEDDED_PLAYER', clientVersion: '1.20250310.01.00' }, embed: true },
  { nombre: 'android', id: '3', ua: `com.google.android.youtube/${ANDROID_VER} (Linux; U; Android 14) gzip`,
    client: { clientName: 'ANDROID', clientVersion: ANDROID_VER, androidSdkVersion: 34 } },
];
async function porApps(v, lang) {
  const fallas = [];
  for (const c of CLIENTES) {
    try {
      const ctx = { client: { ...c.client, hl: lang, gl: 'PE' } };
      if (c.embed) ctx.thirdParty = { embedUrl: 'https://www.youtube.com/watch?v=' + v };
      const r = await fetch('https://www.youtube.com/youtubei/v1/player?prettyPrint=false', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'User-Agent': c.ua, 'X-Youtube-Client-Name': c.id, 'X-Youtube-Client-Version': c.client.clientVersion, Origin: 'https://www.youtube.com' },
        body: JSON.stringify({ context: ctx, videoId: v, contentCheckOk: true, racyCheckOk: true }),
      });
      if (!r.ok) { fallas.push(c.nombre + ' HTTP ' + r.status); continue; }
      const j = await r.json();
      const pistas = j && j.captions && j.captions.playerCaptionsTracklistRenderer && j.captions.playerCaptionsTracklistRenderer.captionTracks;
      if (!pistas || !pistas.length) { fallas.push(c.nombre + ' ' + ((j && j.playabilityStatus && j.playabilityStatus.status) || 'sin pistas')); continue; }
      const res = await leerPista(elegir(pistas, lang));
      if (!res.segs.length) { fallas.push(c.nombre + ' pista vacía'); continue; }
      res.titulo = (j.videoDetails && j.videoDetails.title) || '';
      res.metodo = c.nombre;
      return res;
    } catch (e) { fallas.push(c.nombre + ' ' + (e && e.message)); }
  }
  throw new Error(fallas.join(' | '));
}

// ---------- camino 2: la página web del video ----------
let paginas = new Map();
async function pagina(v, lang) {
  const k = v + lang;
  if (!paginas.has(k)) {
    const r = await fetch(`https://www.youtube.com/watch?v=${v}&hl=${lang}&bpctr=9999999999&has_verified=1`, {
      headers: { 'User-Agent': NAVEGADOR, 'Accept-Language': lang + ',es;q=0.9,en;q=0.8', Cookie: 'CONSENT=YES+cb; SOCS=CAI' },
    });
    if (!r.ok) throw new Error('HTTP ' + r.status);
    paginas.set(k, await r.text());
    if (paginas.size > 20) paginas = new Map([...paginas].slice(-10));
  }
  return paginas.get(k);
}
function tituloDe(html) {
  const m = html.match(/<meta name="title" content="([^"]*)"/) || html.match(/<title>([^<]*)<\/title>/);
  return m ? entidades(m[1]).replace(/\s*-\s*YouTube$/, '') : '';
}
async function porWeb(v, lang) {
  const html = await pagina(v, lang);
  if (/g-recaptcha|confirm you.re not a bot/i.test(html)) throw new Error('YouTube pidió verificación');
  const pistas = sacarLista(html, 'captionTracks');
  if (!pistas || !pistas.length) {
    const est = (html.match(/"playabilityStatus":\{"status":"([A-Z_]+)"/) || [])[1] || '?';
    throw new Error('sin subtítulos (estado ' + est + ', ' + html.length + ' bytes)');
  }
  const res = await leerPista(elegir(pistas, lang));
  res.titulo = tituloDe(html);
  res.metodo = 'web';
  return res;
}

// ---------- camino 3: el panel «Mostrar transcripción» ----------
async function porTranscripcion(v, lang) {
  const html = await pagina(v, lang);
  const p = html.match(/"getTranscriptEndpoint":\{"params":"([^"]+)"/);
  if (!p) throw new Error('sin transcripción');
  const ver = (html.match(/"INNERTUBE_CLIENT_VERSION":"([^"]+)"/) || [])[1] || '2.20250101.00.00';
  const visitor = (html.match(/"VISITOR_DATA":"([^"]+)"/) || html.match(/"visitorData":"([^"]+)"/) || [])[1];
  const r = await fetch('https://www.youtube.com/youtubei/v1/get_transcript?prettyPrint=false', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'User-Agent': NAVEGADOR, 'X-Youtube-Client-Name': '1', 'X-Youtube-Client-Version': ver, Origin: 'https://www.youtube.com', Referer: 'https://www.youtube.com/watch?v=' + v, ...(visitor ? { 'X-Goog-Visitor-Id': visitor } : {}) },
    body: JSON.stringify({ context: { client: { clientName: 'WEB', clientVersion: ver, hl: lang, gl: 'PE', visitorData: visitor } }, params: p[1] }),
  });
  if (!r.ok) throw new Error('HTTP ' + r.status);
  const segs = buscar(await r.json(), 'transcriptSegmentRenderer', [])
    .map((s) => ({ t: Number(s.startMs) || 0, s: texto(s.snippet) }))
    .filter((s) => s.s.trim());
  return { titulo: tituloDe(html), idioma: '', automatico: false, segs, metodo: 'transcripcion' };
}

// ---------- camino 4: servicio gratuito de Tactiq (respaldo externo) ----------
async function porTactiq(v, lang) {
  const r = await fetch('https://tactiq-apps-prod.tactiq.io/transcript', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Origin: 'https://tactiq.io', Referer: 'https://tactiq.io/', 'User-Agent': NAVEGADOR },
    body: JSON.stringify({ videoUrl: 'https://www.youtube.com/watch?v=' + v, langCode: lang }),
  });
  if (!r.ok) throw new Error('HTTP ' + r.status);
  const j = await r.json();
  const segs = (j.captions || []).map((c) => ({ t: Math.round(Number(c.start || 0) * 1000), s: entidades(String(c.text || '')).replace(/\s+/g, ' ').trim() }))
    .filter((x) => x.s && !/^\[(música|music|aplausos|applause)\]$/i.test(x.s));
  return { titulo: j.title || '', idioma: lang, automatico: true, segs, metodo: 'tactiq' };
}

// ---------- utilidades ----------
function elegir(pistas, lang) {
  const base = lang.split('-')[0];
  const es = (p) => (p.languageCode || '').split('-')[0] === base;
  return pistas.find((p) => es(p) && p.kind !== 'asr') || pistas.find(es) ||
    pistas.find((p) => p.kind !== 'asr') || pistas[0];
}
async function leerPista(p) {
  const u = new URL(p.baseUrl.replace(/\\u0026/g, '&'), 'https://www.youtube.com');
  u.searchParams.set('fmt', 'json3');
  let segs = [];
  const r = await fetch(u, { headers: { 'User-Agent': NAVEGADOR } });
  const tx = r.ok ? await r.text() : '';
  if (tx && tx.trim().startsWith('{')) {
    const j = JSON.parse(tx);
    segs = (j.events || []).filter((e) => e.segs).map((e) => ({
      t: e.tStartMs || 0,
      s: e.segs.map((s) => s.utf8 || '').join('').replace(/\s+/g, ' ').trim(),
    }));
  } else {
    // Formato XML clásico
    u.searchParams.delete('fmt');
    const x = tx && tx.includes('<') ? tx : await (await fetch(u, { headers: { 'User-Agent': NAVEGADOR } })).text();
    const re = /<(text|p)\b([^>]*)>([\s\S]*?)<\/\1>/g;
    let m;
    while ((m = re.exec(x))) {
      const a = m[2];
      const mt = a.match(/\bt="(\d+)"/), ms = a.match(/\bstart="([\d.]+)"/);
      const t = mt ? Number(mt[1]) : ms ? Math.round(Number(ms[1]) * 1000) : 0;
      segs.push({ t, s: entidades(m[3].replace(/<[^>]+>/g, '')).replace(/\s+/g, ' ').trim() });
    }
  }
  return { idioma: p.languageCode || '', automatico: p.kind === 'asr', segs: segs.filter((s) => s.s) };
}
function entidades(s) {
  return s.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"')
    .replace(/&#39;|&#x27;/g, "'").replace(/&#(\d+);/g, (m, n) => String.fromCodePoint(Number(n)));
}
function sacarLista(html, clave) {
  let i = html.indexOf('"' + clave + '":');
  if (i < 0) return null;
  i = html.indexOf('[', i);
  let n = 0, enTexto = false, esc = false;
  for (let j = i; j < html.length; j++) {
    const c = html[j];
    if (enTexto) { if (esc) esc = false; else if (c === '\\') esc = true; else if (c === '"') enTexto = false; continue; }
    if (c === '"') enTexto = true;
    else if (c === '[') n++;
    else if (c === ']' && --n === 0) { try { return JSON.parse(html.slice(i, j + 1)); } catch { return null; } }
  }
  return null;
}
function buscar(o, clave, res) {
  if (!o || typeof o !== 'object') return res;
  if (Array.isArray(o)) { for (const x of o) buscar(x, clave, res); return res; }
  for (const k in o) { if (k === clave) res.push(o[k]); else buscar(o[k], clave, res); }
  return res;
}
function texto(x) {
  if (!x) return '';
  if (x.simpleText) return x.simpleText;
  if (x.runs) return x.runs.map((r) => r.text || '').join('');
  return '';
}
