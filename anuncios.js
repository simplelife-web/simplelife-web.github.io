/*
  Zonas de anuncios de Simplelife.

  Cada página marca dónde puede ir un anuncio con:
    <div class="sl-anuncio" data-zona="nombre"></div>
  Las zonas están siempre FUERA de las herramientas (debajo del resultado,
  entre secciones de texto o al final), lejos de botones, y como máximo dos
  por página. Mientras BLOQUE esté vacío, las zonas no ocupan espacio.

  Cuando AdSense apruebe el sitio:
  1. En AdSense → Anuncios → Por bloque de anuncios, crea un bloque
     «Anuncio de display» adaptable.
  2. Copia el número de data-ad-slot y pégalo en BLOQUE (entre comillas).

  Para ver dónde caen las zonas sin anuncios reales, abre cualquier página
  con ?zonas al final (ejemplo: /glosario/inflacion.html?zonas).
*/
(function () {
  var BLOQUE = '';
  var CLIENTE = 'ca-pub-9798339025422593';

  var zonas = document.querySelectorAll('.sl-anuncio');
  if (!zonas.length) return;
  var prueba = /[?&]zonas\b/.test(location.search);
  if (!BLOQUE && !prueba) return;

  var css =
    '.sl-anuncio{display:block;clear:both;margin:32px auto;max-width:100%;text-align:center;}' +
    '.sl-anuncio-et{display:block;margin:0 0 6px;font:12px/1.2 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;letter-spacing:.04em;text-transform:uppercase;opacity:.6;}' +
    // Espacio reservado para que el texto no salte cuando carga el anuncio
    '.sl-anuncio .adsbygoogle,.sl-anuncio-prueba{display:block;width:100%;min-height:280px;}' +
    '@media (min-width:768px){.sl-anuncio .adsbygoogle,.sl-anuncio-prueba{min-height:250px;}}' +
    // Si Google no tiene un anuncio para mostrar, la zona desaparece sin dejar hueco
    '.sl-anuncio:has(ins[data-ad-status="unfilled"]){display:none;}' +
    '.sl-anuncio-prueba{display:flex;align-items:center;justify-content:center;border:2px dashed currentColor;border-radius:12px;opacity:.45;font:600 14px/1.4 system-ui,sans-serif;}' +
    '@media print{.sl-anuncio{display:none !important;}}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  zonas.forEach(function (z) {
    z.setAttribute('role', 'complementary');
    z.setAttribute('aria-label', 'Publicidad');
    var et = '<span class="sl-anuncio-et">Publicidad</span>';
    if (!BLOQUE) {
      z.innerHTML = et + '<div class="sl-anuncio-prueba">Zona de anuncio: ' + (z.getAttribute('data-zona') || '') + '</div>';
      return;
    }
    z.innerHTML = et + '<ins class="adsbygoogle" data-ad-client="' + CLIENTE + '" data-ad-slot="' + BLOQUE +
      '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) { /* sin anuncio, sin problema */ }
  });
})();
