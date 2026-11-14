const UA = "SimplelifeBot/1.0 (+https://simplelife-web.github.io/quehagohoy/)";
const g = async (u) => { try { const r = await fetch(u, { headers: { "User-Agent": UA, "Accept-Language": "es-PE,es" }, signal: AbortSignal.timeout(20000) }); return { s: r.status, t: await r.text(), url: r.url }; } catch (e) { return { s: "ERR " + (e.cause?.code || e.message), t: "" }; } };
const P = (...a) => console.log(...a);
// 1 Joinnus
let r = await g("https://www.joinnus.com/robots.txt"); P("JOINNUS ROBOTS TOP\n" + r.t.slice(0, 700));
r = await g("https://www.joinnus.com/sitemap.xml");
const locs = [...r.t.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]);
P("sitemap locs", locs.length, "lima:", locs.filter(u => /\/events\/[^/]+\/lima-/.test(u)).length, "cats:", [...new Set(locs.map(u => u.split("/")[4]))].join(","));
P(locs.filter(u => /\/lima-/.test(u)).slice(0, 8).join("\n"));
const home = await g("https://www.joinnus.com/");
P("hosts api en home:", [...new Set([...home.t.matchAll(/https?:\/\/[a-z0-9.-]*joinnus[a-z0-9.-]*/gi)].map(m => m[0]))].join(" "));
const ev = locs.find(u => /\/lima-/.test(u) && !/tour-estadio|parque-de-la-imag/.test(u));
r = await g(ev); P("\nEVENTO", ev, r.s, r.t.length);
const ld = [...r.t.matchAll(/<script[^>]*ld\+json[^>]*>([\s\S]*?)<\/script>/gi)].map(m => m[1]); P("LD:", ld.map(x => x.slice(0, 1500)).join("\n---\n"));
const nd = r.t.match(/<script id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/); 
if (nd) { const s = nd[1]; P("NEXT len", s.length); for (const k of ["price", "Price", "startDate", "dateStart", "latitude", "lat", "venue", "address", "currency", "min", "free"]) { const i = s.indexOf('"' + k); if (i > -1) P(k, "→", s.slice(i, i + 200)); } }
P("og:", [...r.t.matchAll(/<meta[^>]+property="og:[^"]+"[^>]*>/g)].map(m => m[0]).slice(0, 6).join("\n"));
P("S/:", (r.t.match(/S\/\.?\s?[\d.,]+/g) || []).slice(0, 10));
// 2 Teleticket
r = await g("https://teleticket.com.pe/sitemap.xml"); const tl = [...r.t.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]); P("\nTELETICKET sitemap", r.s, tl.length, tl.slice(0, 10).join("\n"));
r = await g("https://teleticket.com.pe/evento/AMU004"); P("TT evento", r.s, r.t.length);
const tld = [...r.t.matchAll(/<script[^>]*ld\+json[^>]*>([\s\S]*?)<\/script>/gi)].map(m => m[1]); P("LD:", tld.map(x => x.slice(0, 1500)).join("\n---\n"));
P("S/:", (r.t.match(/S\/\.?\s?[\d.,]+/g) || []).slice(0, 10));
P(r.t.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/gi, " ").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").slice(0, 1500));
// 3 Ticketmaster
r = await g("https://www.ticketmaster.pe/sitemap.xml"); P("\nTM sitemap", r.s, r.t.slice(0, 600));
// 4 gob.pe
for (const u of ["https://www.gob.pe/institucion/cultura/noticias.rss", "https://www.gob.pe/institucion/munlima/noticias", "https://www.gob.pe/institucion/munlima/noticias.rss", "https://www.gob.pe/institucion/cultura/campañas", "https://www.gob.pe/institucion/cultura/eventos"]) { r = await g(u); P("\nGOB", u, r.s, r.t.length, r.t.slice(0, 300).replace(/\s+/g, " ")); }
// 5 Fever
r = await g("https://feverup.com/robots.txt"); P("\nFEVER robots", r.s, r.t.slice(0, 900));
r = await g("https://feverup.com/es/lima-peru"); P("FEVER lima", r.s, r.t.length, "ld:", ([...r.t.matchAll(/ld\+json[^>]*>([\s\S]*?)<\/script>/g)].map(m => m[1].slice(0, 600))).join("\n--\n"));
// 6 El Peruano RSS
for (const u of ["https://elperuano.pe/rss", "https://elperuano.pe/robots.txt", "https://www.andina.pe/agencia/rss.aspx", "https://andina.pe/robots.txt"]) { r = await g(u); P("\n", u, r.s, r.t.slice(0, 500)); }
