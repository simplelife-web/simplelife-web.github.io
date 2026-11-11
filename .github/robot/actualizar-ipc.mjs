// Robot de la "Calculadora de inflación Perú"
// Descarga del BCRP (Banco Central de Reserva del Perú) la serie oficial
// PN01270PM: Índice de Precios al Consumidor de Lima Metropolitana
// (índice, base diciembre 2021 = 100, fuente INEI) y la guarda en inflacion/ipc.json.
// La calculadora del sitio solo lee ese archivo; no se conecta al BCRP.
// Uso: node .github/robot/actualizar-ipc.mjs   (Node 20 o más, sin instalar nada)

import { readFileSync, writeFileSync, existsSync } from "node:fs";

const RAIZ = new URL("../../", import.meta.url);
const ARCHIVO = new URL("inflacion/ipc.json", RAIZ);
const SERIE = "PN01270PM";
const UA = "SimplelifeBot/1.0 (+https://simplelife-web.github.io/inflacion/)";
const MES = { ene: 1, feb: 2, mar: 3, abr: 4, may: 5, jun: 6, jul: 7, ago: 8, sep: 9, set: 9, oct: 10, nov: 11, dic: 12 };

const hoy = new Date();
const url = `https://estadisticas.bcrp.gob.pe/estadisticas/series/api/${SERIE}/json/1949-1/${hoy.getUTCFullYear()}-12/esp`;

async function traer() {
  for (let intento = 1; intento <= 4; intento++) {
    try {
      const r = await fetch(url, { headers: { "User-Agent": UA, Accept: "application/json" }, signal: AbortSignal.timeout(60000) });
      if (r.ok) return JSON.parse((await r.text()).replace(/^﻿/, ""));
      console.log(`Intento ${intento}: el BCRP respondió ${r.status}`);
    } catch (e) { console.log(`Intento ${intento}: ${e.cause?.code || e.message}`); }
    await new Promise((ok) => setTimeout(ok, 5000 * intento));
  }
  throw new Error("No se pudo descargar la serie del BCRP");
}

const datos = await traer();
const meses = [];
for (const p of datos.periods || []) {
  const m = /^([A-Za-z]{3})\.?\s*(\d{4})$/.exec(String(p.name).trim());
  const v = Number(String(p.values?.[0]).replace(",", "."));
  if (!m || !MES[m[1].toLowerCase()] || !Number.isFinite(v) || v <= 0) continue;
  meses.push([`${m[2]}-${String(MES[m[1].toLowerCase()]).padStart(2, "0")}`, v]);
}
meses.sort((a, b) => a[0].localeCompare(b[0]));

// Controles para no guardar datos rotos: meses seguidos, sin huecos, y suficientes.
if (meses.length < 120) throw new Error(`Muy pocos meses (${meses.length}); no se guarda nada`);
for (let i = 1; i < meses.length; i++) {
  const [a, ma] = meses[i - 1][0].split("-").map(Number);
  const [b, mb] = meses[i][0].split("-").map(Number);
  if ((b * 12 + mb) - (a * 12 + ma) !== 1) throw new Error(`Hueco entre ${meses[i - 1][0]} y ${meses[i][0]}`);
}

const salida = {
  serie: SERIE,
  titulo: "Índice de precios al consumidor de Lima Metropolitana (índice dic. 2021 = 100)",
  fuente: "BCRP, Estadísticas (con datos del INEI)",
  enlace: `https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/${SERIE}/html`,
  desde: meses[0][0],
  hasta: meses[meses.length - 1][0],
  revisado: hoy.toISOString().slice(0, 10),
  // Un número por mes, empezando en "desde".
  indice: meses.map(([, v]) => v)
};

if (existsSync(ARCHIVO)) {
  const antes = JSON.parse(readFileSync(ARCHIVO, "utf8"));
  if (antes.hasta === salida.hasta && JSON.stringify(antes.indice) === JSON.stringify(salida.indice)) {
    console.log(`Sin cambios: el último dato sigue siendo ${salida.hasta}.`);
    process.exit(0);
  }
}
writeFileSync(ARCHIVO, JSON.stringify(salida) + "\n");
console.log(`Guardado: ${meses.length} meses, de ${salida.desde} a ${salida.hasta}.`);
