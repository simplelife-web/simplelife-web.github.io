// Arma prestamos/index.html desde plantilla.html, dibujando las fórmulas con KaTeX.
// Uso: npm i katex@0.16.11 (en cualquier carpeta) y luego
//   NODE_PATH=<carpeta>/node_modules node .github/prestamos/generar.mjs
import { readFileSync, writeFileSync } from "node:fs";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const katex = require("katex");
const aqui = new URL(".", import.meta.url);
let html = readFileSync(new URL("plantilla.html", aqui), "utf8");
html = html.replace(/<!--D:([\s\S]*?)-->/g, (_, tex) => '<div class="ecuacion">' + katex.renderToString(tex, { displayMode: true, output: "htmlAndMathml" }) + "</div>");
html = html.replace(/<!--I:([\s\S]*?)-->/g, (_, tex) => katex.renderToString(tex, { output: "htmlAndMathml" }));
writeFileSync(new URL("../../prestamos/index.html", aqui), html);
console.log("prestamos/index.html listo");
