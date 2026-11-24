// Robot de la "Calculadora de sueldo neto Perú"
// Lee en la SBS (Superintendencia de Banca, Seguros y AFP) la tabla oficial de
// comisiones, prima de seguros, aporte obligatorio y remuneración máxima asegurable
// de cada AFP, y la guarda en sueldo/afp.json. La calculadora solo lee ese archivo.
// Uso: node .github/robot/actualizar-afp.mjs   (Node 20 o más, sin instalar nada)

import { writeFileSync, readFileSync, existsSync } from "node:fs";

const RAIZ = new URL("../../", import.meta.url);
const ARCHIVO = new URL("sueldo/afp.json", RAIZ);
const URL_SBS = "https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx";
const UA = "Mozilla/5.0 (compatible; SimplelifeBot/1.0; +https://simplelife-web.github.io/sueldo/)";
const AFPS = ["HABITAT", "INTEGRA", "PRIMA", "PROFUTURO"];

async function traer() {
  for (let intento = 1; intento <= 4; intento++) {
    try {
      const r = await fetch(URL_SBS, { headers: { "User-Agent": UA }, signal: AbortSignal.timeout(60000) });
      if (r.ok) return await r.text();
      console.log(`Intento ${intento}: la SBS respondió ${r.status}`);
    } catch (e) { console.log(`Intento ${intento}: ${e.cause?.code || e.message}`); }
    await new Promise((ok) => setTimeout(ok, 5000 * intento));
  }
  throw new Error("No se pudo descargar la tabla de la SBS");
}

const html = await traer();
const texto = html.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/gi, " ")
  .replace(/<\/(td|th)>/gi, " | ").replace(/<[^>]+>/g, " ")
  .replace(/&nbsp;/g, " ").replace(/\s+/g, " ");

const num = (s) => Number(s.replace(/\s/g, "").replace(/\./g, "").replace(",", "."));
const afp = {};
for (const n of AFPS) {
  const re = new RegExp(n + "\\s*\\|\\s*([\\d,]+)\\s*%\\s*\\|\\s*([\\d,]+)\\s*%\\s*\\|\\s*([\\d,]+)\\s*%\\s*\\|\\s*([\\d,]+)\\s*%\\s*\\|\\s*([\\d\\s.,]+?)\\s*\\|");
  const m = re.exec(texto);
  if (!m) throw new Error(`No se encontró la fila de ${n}`);
  afp[n.charAt(0) + n.slice(1).toLowerCase()] = {
    flujo: num(m[1]), saldo: num(m[2]), prima: num(m[3]), aporte: num(m[4]), tope: num(m[5])
  };
}

// Controles para no guardar datos rotos
for (const [n, a] of Object.entries(afp)) {
  const ok = a.flujo > 0 && a.flujo < 4 && a.saldo >= 0 && a.saldo < 3 && a.prima > 0.5 && a.prima < 3 &&
    a.aporte >= 8 && a.aporte <= 15 && a.tope > 5000 && a.tope < 40000;
  if (!ok) throw new Error(`Valores raros para ${n}: ${JSON.stringify(a)}`);
}
const mes = /Al mes de devengue\s*(\d{4}-\d{2})/.exec(texto)?.[1] || null;

const nuevo = {
  fuente: "Superintendencia de Banca, Seguros y AFP (SBS)",
  enlace: URL_SBS,
  mes,
  revisado: new Date().toISOString().slice(0, 10),
  nota: "Porcentajes sobre la remuneración bruta mensual. La prima de seguros se cobra hasta la remuneración máxima asegurable (tope, en soles).",
  afp
};
if (existsSync(ARCHIVO)) {
  const viejo = JSON.parse(readFileSync(ARCHIVO, "utf8"));
  if (JSON.stringify(viejo.afp) !== JSON.stringify(afp)) console.log("Cambiaron los valores de las AFP.");
}
writeFileSync(ARCHIVO, JSON.stringify(nuevo, null, 1) + "\n");
console.log(JSON.stringify(nuevo, null, 1));
