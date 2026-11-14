// Sondeo temporal: qué páginas se pueden leer y si traen datos de eventos (JSON-LD)
const UA = "SimplelifeBot/1.0 (+https://simplelife-web.github.io/quehagohoy/)";
const urls = process.argv.slice(2).length ? process.argv.slice(2) : `
https://www.joinnus.com/robots.txt
https://www.joinnus.com/
https://www.joinnus.com/explore
https://www.joinnus.com/sitemap.xml
https://teleticket.com.pe/robots.txt
https://teleticket.com.pe/
https://www.ticketmaster.pe/robots.txt
https://www.ticketmaster.pe/
https://www.eventbrite.com.pe/robots.txt
https://www.eventbrite.com.pe/d/peru--lima/events/
https://www.eventbrite.com.pe/d/peru--lima/free--events/
https://www.atrapalo.pe/robots.txt
https://www.atrapalo.pe/entradas/
https://www.passline.com/robots.txt
https://www.passline.com/
https://tuentrada.com.pe/
https://www.instagram.com/robots.txt
https://www.tiktok.com/robots.txt
https://www.facebook.com/robots.txt
https://x.com/robots.txt
https://www.youtube.com/robots.txt
https://www.youtube.com/@MinisteriodeCulturaPeru
https://www.youtube.com/@MunicipalidaddeLima
https://www.youtube.com/@granteatronacional
https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts?q=lima%20concierto&limit=5
https://www.reddit.com/r/lima/new.json?limit=5
https://www.gob.pe/robots.txt
https://www.gob.pe/institucion/cultura/noticias
https://www.gob.pe/busquedas?contenido[]=campanas&institucion[]=cultura
https://infoartes.pe/
https://www.cultura.gob.pe/
https://www.lima.gob.pe/
https://agendacultural.pe/
https://www.teatroperuano.com/
`.trim().split(/\s+/);
for (const u of urls) {
  try {
    const r = await fetch(u, { headers: { "User-Agent": UA, "Accept-Language": "es-PE,es" }, redirect: "follow", signal: AbortSignal.timeout(20000) });
    const t = await r.text();
    const ld = [...t.matchAll(/<script[^>]*application\/ld\+json[^>]*>([\s\S]*?)<\/script>/gi)].map(m => m[1]);
    const evLd = ld.filter(x => /"@type"\s*:\s*"(\w*Event|ItemList)"/.test(x)).length;
    const nextData = /__NEXT_DATA__|__NUXT__/.test(t);
    const precios = (t.match(/S\/\.?\s?\d+/g) || []).length;
    console.log(`\n### ${u}\n${r.status} ${r.url !== u ? "→ " + r.url : ""} bytes=${t.length} ld=${ld.length} ldEventos=${evLd} next=${nextData} preciosS/=${precios}`);
    if (u.endsWith("robots.txt")) console.log(t.slice(0, 1500));
    else if (u.includes("youtube.com/@")) console.log("channelId:", (t.match(/"channelId":"(UC[\w-]{22})"/) || [])[1], (t.match(/<link rel="alternate" type="application\/rss\+xml"[^>]*href="([^"]+)"/) || [])[1]);
    else if (/json|xrpc|sitemap/.test(u)) console.log(t.slice(0, 1200));
    else { console.log(t.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/gi, " ").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").slice(0, 600)); if (ld[0]) console.log("LD0:", ld.find(x=>/Event/.test(x))?.slice(0, 800) || ld[0].slice(0, 300)); }
  } catch (e) { console.log(`\n### ${u}\nERROR ${e.cause?.code || e.message}`); }
}
