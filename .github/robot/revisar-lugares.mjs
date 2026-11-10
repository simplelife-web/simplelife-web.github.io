// Revisión de los lugares fijos: comprueba que cada enlace oficial abra
// y compara la ubicación del mapa con OpenStreetMap (Nominatim).
// Uso: node .github/robot/revisar-lugares.mjs
import { readFileSync } from "node:fs";
const RAIZ = new URL("../../", import.meta.url);
const { lugares } = JSON.parse(readFileSync(new URL("quehagohoy/lugares.json", RAIZ), "utf8"));
const UA = "SimplelifeBot/1.0 (+https://simplelife-web.github.io/quehagohoy/)";
const espera = (ms) => new Promise((r) => setTimeout(r, ms));
const km = (a, b, c, d) => { const R = 6371, x = (c - a) * Math.PI / 180, y = (d - b) * Math.PI / 180; const h = Math.sin(x / 2) ** 2 + Math.cos(a * Math.PI / 180) * Math.cos(c * Math.PI / 180) * Math.sin(y / 2) ** 2; return 2 * R * Math.asin(Math.sqrt(h)); };

const urls = [...new Set(lugares.map((l) => l.url))];
for (const u of urls) {
  try { const r = await fetch(u, { headers: { "User-Agent": UA }, redirect: "follow", signal: AbortSignal.timeout(20000) }); console.log(`ENLACE ${r.status} ${u} -> ${r.url}`); }
  catch (e) { console.log(`ENLACE ERROR ${u} ${e.cause?.code || e.message}`); }
}
for (const l of lugares) {
  const q = l.osm ? `${l.osm}, Lima, Perú` : `${l.nombre.replace(/\(.*?\)/g, "")}, ${l.distrito}, Lima, Perú`;
  try {
    const r = await fetch(`https://nominatim.openstreetmap.org/search?format=json&limit=1&countrycodes=pe&q=${encodeURIComponent(q)}`, { headers: { "User-Agent": UA }, signal: AbortSignal.timeout(15000) });
    const j = await r.json();
    if (j[0]) console.log(`MAPA ${l.id} osm=${(+j[0].lat).toFixed(4)},${(+j[0].lon).toFixed(4)} actual=${l.lat},${l.lon} dif=${km(l.lat, l.lon, +j[0].lat, +j[0].lon).toFixed(2)}km  (${j[0].display_name.slice(0, 90)})`);
    else console.log(`MAPA ${l.id} sin resultado para "${q}"`);
  } catch (e) { console.log(`MAPA ${l.id} error ${e.message}`); }
  await espera(1200);
}
