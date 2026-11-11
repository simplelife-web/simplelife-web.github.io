import { readFileSync } from "node:fs";
const UA = "SimplelifeBot/1.0 (+https://simplelife-web.github.io/quehagohoy/)";
const w = (ms) => new Promise((r) => setTimeout(r, ms));
const { lugares } = JSON.parse(readFileSync("quehagohoy/lugares.json", "utf8"));
const LIMA = ["Ancón","Ate","Barranco","Breña","Carabayllo","Chaclacayo","Chorrillos","Cieneguilla","Comas","El Agustino","Independencia","Jesús María","La Molina","La Victoria","Lince","Los Olivos","Lurigancho","Lurín","Magdalena del Mar","Miraflores","Pachacámac","Pucusana","Pueblo Libre","Puente Piedra","Punta Hermosa","Punta Negra","Rímac","San Bartolo","San Borja","San Isidro","San Juan de Lurigancho","San Juan de Miraflores","San Luis","San Martín de Porres","San Miguel","Santa Anita","Santa María del Mar","Santa Rosa","Santiago de Surco","Surquillo","Villa El Salvador","Villa María del Triunfo"];
const CALLAO = ["Callao","Bellavista","Carmen de la Legua Reynoso","La Perla","La Punta","Ventanilla","Mi Perú"];
async function geo(q) {
  try {
    const r = await fetch(`https://nominatim.openstreetmap.org/search?format=json&limit=1&countrycodes=pe&q=${encodeURIComponent(q)}`, { headers: { "User-Agent": UA }, signal: AbortSignal.timeout(15000) });
    const j = await r.json();
    return j[0] ? [(+j[0].lat).toFixed(4), (+j[0].lon).toFixed(4), j[0].display_name.slice(0, 70)] : null;
  } catch (e) { return null; }
}
for (const l of lugares.filter((l) => l.lat == null)) {
  const g = await geo(`${l.osm}, Perú`);
  console.log("LUGAR", l.id, JSON.stringify(g)); await w(1200);
  try { const r = await fetch(l.url, { headers: { "User-Agent": UA }, redirect: "follow", signal: AbortSignal.timeout(15000) }); console.log("URL", r.status, l.url, "->", r.url); }
  catch (e) { console.log("URL ERR", l.url, e.cause?.code || e.message); }
}
for (const [prov, lista] of [["Lima", LIMA], ["Callao", CALLAO]]) for (const d of lista) {
  let g = await geo(`Distrito de ${d}, Provincia de ${prov}, Perú`); await w(1200);
  if (!g) { g = await geo(`${d}, ${prov}, Perú`); await w(1200); }
  console.log("DIST", prov, d, JSON.stringify(g));
}
