// Convierte fórmulas LaTeX en HTML con KaTeX (se usa al generar el glosario).
// Entrada (stdin): JSON [[tex, display], ...]. Salida (stdout): JSON [html, ...].
// Necesita KaTeX instalado: npm i katex@0.16.11 (ruta en la variable KATEX, opcional).
const katex = require(process.env.KATEX || 'katex');
let datos = '';
process.stdin.on('data', (c) => { datos += c; });
process.stdin.on('end', () => {
  const lista = JSON.parse(datos);
  const salida = lista.map(([tex, display]) =>
    katex.renderToString(tex, { displayMode: display, throwOnError: true, strict: 'ignore', output: 'htmlAndMathml' })
  );
  process.stdout.write(JSON.stringify(salida));
});
