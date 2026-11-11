/*
  Barra de navegación de Simplelife (la misma en todas las páginas).
  Para agregar una herramienta nueva, súmala a la lista HERRAMIENTAS.
  Cada página la carga con <script src="nav.js"></script> (o "../nav.js")
  justo después de <body>; la barra aparece en ese mismo lugar.
*/
(function () {
  var HERRAMIENTAS = [
    { href: 'transcriptor/', texto: 'Transcriptor' },
    { href: 'tramites/', texto: 'Trámites' },
    { href: 'quehagohoy/', texto: '¿Qué hago hoy?' },
    { href: 'intercambio/', texto: 'Intercambio' },
    { href: 'inflacion/', texto: 'Inflación' }
  ];
  var EXTRA = [
    { href: 'acerca.html', texto: 'Acerca de' },
    { href: 'contacto.html', texto: 'Contacto' },
    { href: 'privacidad.html', texto: 'Privacidad' }
  ];

  var yo = document.currentScript;
  if (!yo) return;
  var base = new URL('./', yo.src);
  var ruta = location.pathname;
  var enInicio = ruta === base.pathname || ruta === base.pathname + 'index.html';

  var css = '' +
    '.sl-nav{--sl-bg:#ffffff;--sl-text:#1d1d1b;--sl-muted:#5e5c56;--sl-line:#dedbd2;--sl-accent:#1f6f5c;--sl-soft:#e7f1ed;' +
    'background:var(--sl-bg);border-bottom:1px solid var(--sl-line);font:15px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--sl-text);}' +
    '@media (prefers-color-scheme:dark){.sl-nav{--sl-bg:#1e1f1d;--sl-text:#ecebe6;--sl-muted:#a3a19a;--sl-line:#34352f;--sl-accent:#4fb596;--sl-soft:#1f2d28;}}' +
    '.sl-nav *{box-sizing:border-box;}' +
    '.sl-in{max-width:1100px;margin:0 auto;padding:8px 16px;display:flex;align-items:center;gap:6px 14px;}' +
    '.sl-logo{display:inline-flex;align-items:center;gap:7px;text-decoration:none;color:var(--sl-text);font-weight:700;font-size:17px;}' +
    '.sl-logo img{width:28px;height:28px;}' +
    '.sl-logo b{color:var(--sl-accent);}' +
    '.sl-home{margin-left:auto;display:inline-flex;align-items:center;gap:6px;padding:7px 12px;border-radius:99px;background:var(--sl-accent);color:#fff;text-decoration:none;font-weight:600;font-size:14px;white-space:nowrap;}' +
    '@media (prefers-color-scheme:dark){.sl-home{color:#0d1a15;}}' +
    '.sl-home svg{width:16px;height:16px;}' +
    '.sl-links{flex:1 1 auto;min-width:0;display:flex;gap:2px;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch;margin:0;padding:0;list-style:none;}' +
    '.sl-links::-webkit-scrollbar{display:none;}' +
    '.sl-links a{display:block;padding:6px 10px;border-radius:99px;color:var(--sl-muted);text-decoration:none;white-space:nowrap;font-size:14px;}' +
    '.sl-links a:hover,.sl-links a:focus-visible{background:var(--sl-soft);color:var(--sl-text);}' +
    '.sl-links a[aria-current]{background:var(--sl-soft);color:var(--sl-accent);font-weight:600;}' +
    '.sl-sep{width:1px;background:var(--sl-line);margin:4px 2px;}' +
    '.sl-logo,.sl-home{flex:0 0 auto;}' +
    '@media (max-width:860px){.sl-in{flex-wrap:wrap;}.sl-links{order:3;flex-basis:100%;margin:0 -16px;padding:0 12px 2px;width:calc(100% + 32px);flex-basis:calc(100% + 32px);-webkit-mask-image:linear-gradient(90deg,#000 85%,transparent);mask-image:linear-gradient(90deg,#000 85%,transparent);}}';

  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  function enlace(item) {
    var url = new URL(item.href, base);
    var a = document.createElement('a');
    a.href = url.href;
    a.textContent = item.texto;
    if (ruta.indexOf(url.pathname) === 0) a.setAttribute('aria-current', 'page');
    var li = document.createElement('li');
    li.appendChild(a);
    return li;
  }

  var nav = document.createElement('nav');
  nav.className = 'sl-nav';
  nav.setAttribute('aria-label', 'Simplelife');
  var dentro = document.createElement('div');
  dentro.className = 'sl-in';

  var logo = document.createElement('a');
  logo.className = 'sl-logo';
  logo.href = base.href;
  logo.title = 'Ir al inicio de Simplelife';
  logo.innerHTML = '<img src="' + new URL('logo.svg', base).href + '" alt="" width="28" height="28"><span>Simple<b>life</b></span>';
  dentro.appendChild(logo);

  var lista = document.createElement('ul');
  lista.className = 'sl-links';
  HERRAMIENTAS.forEach(function (h) { lista.appendChild(enlace(h)); });
  var sep = document.createElement('li');
  sep.className = 'sl-sep';
  sep.setAttribute('aria-hidden', 'true');
  lista.appendChild(sep);
  EXTRA.forEach(function (h) { lista.appendChild(enlace(h)); });
  dentro.appendChild(lista);

  if (!enInicio) {
    var casa = document.createElement('a');
    casa.className = 'sl-home';
    casa.href = base.href;
    casa.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>Volver al inicio';
    dentro.appendChild(casa);
  }

  nav.appendChild(dentro);
  yo.parentNode.insertBefore(nav, yo.nextSibling);
})();
