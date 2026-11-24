// Robot de la "Calculadora de sueldo neto Perú" (prueba de lectura de la SBS).
const URL_SBS = "https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx";
const UA = "Mozilla/5.0 (compatible; SimplelifeBot/1.0; +https://simplelife-web.github.io/sueldo/)";
const r = await fetch(URL_SBS, { headers: { "User-Agent": UA } });
console.log("HTTP", r.status);
const html = await r.text();
const texto = html.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/gi, " ")
  .replace(/<\/(td|th)>/gi, " | ").replace(/<\/tr>/gi, "\n").replace(/<[^>]+>/g, " ")
  .replace(/&nbsp;/g, " ").replace(/[ \t]+/g, " ").replace(/\n\s+/g, "\n");
console.log(texto.slice(0, 12000));
