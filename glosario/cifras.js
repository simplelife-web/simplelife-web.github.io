// "Cifra oficial al día": muestra las cifras vigentes (tipo de cambio, tasa de referencia,
// inflación, UIT...) que un robot actualiza cada día en cifras.json. No cambia las
// definiciones: solo agrega un recuadro debajo de la frase inicial del término.
(function () {
  if (window.__cifrasAlDia) return;
  window.__cifrasAlDia = true;

  var MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'setiembre', 'octubre', 'noviembre', 'diciembre'];
  var NB = ' ';

  function miles(n) {
    var s = String(n);
    return s.replace('-', '').length >= 5 ? s.replace(/\B(?=(\d{3})+(?!\d))/g, NB) : s;
  }
  function dec(v, d) {
    var s = Math.abs(v).toFixed(d), p = s.split('.');
    return (v < 0 ? '−' : '') + miles(p[0]) + (p[1] ? '.' + p[1] : '');
  }
  function valor(c) {
    var v = c.valor;
    switch (c.formato) {
      case 'tc': return 'S/' + NB + v.toFixed(3) + ' por dólar';
      case 'pct2': return dec(v, 2) + NB + '%';
      case 'pct1': return dec(v, 1) + NB + '%';
      case 'millones': return 'US$' + NB + dec(v, 0) + ' millones';
      case 'cobre': return 'US$' + NB + dec(v / 100, 2) + ' por libra';
      case 'oro': return 'US$' + NB + dec(v, 0) + ' por onza troy';
      case 'entero': return dec(v, 0) + NB + 'puntos básicos';
      case 'soles': return 'S/' + NB + dec(v, 0) + (c.unidad ? ' ' + c.unidad : '');
      default: return dec(v, 2);
    }
  }
  function fecha(c) {
    var f = String(c.fecha).split('-');
    if (f.length === 3) return (c.desde ? 'vigente desde el ' : 'dato del ') + Number(f[2]) + ' de ' + MESES[Number(f[1]) - 1] + ' de ' + f[0];
    if (f.length === 2) return 'dato de ' + MESES[Number(f[1]) - 1] + ' de ' + f[0];
    return 'vigente en ' + f[0];
  }
  function hoyTexto(iso) {
    var f = iso.split('-');
    return Number(f[2]) + ' de ' + MESES[Number(f[1]) - 1] + ' de ' + f[0];
  }
  function el(tag, cls, txt) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (txt) e.textContent = txt;
    return e;
  }

  function pintar(D) {
    var pag = (location.pathname.split('/').pop() || 'index.html').replace(/\.html$/, '');
    var esPortada = pag === '' || pag === 'index';
    var claves = esPortada ? D.portada : D.terminos[pag];
    if (!claves || !claves.length) return;
    var lead = document.querySelector('main .lead');
    if (!lead || document.getElementById('cifras-al-dia')) return;

    var caja = el('aside', 'card cifras');
    caja.id = 'cifras-al-dia';
    caja.setAttribute('aria-label', 'Cifras oficiales al día');
    caja.appendChild(el('h2', '', claves.length > 1 ? 'Cifras oficiales al día' : 'Cifra oficial al día'));
    var ul = el('ul');
    claves.forEach(function (k) {
      var c = D.cifras[k];
      if (!c) return;
      var li = el('li');
      li.appendChild(el('span', 'n', c.nombre + (c.unidad && c.formato.indexOf('pct') === 0 ? ' (' + c.unidad + ')' : '')));
      li.appendChild(el('strong', '', valor(c)));
      var s = el('small', '', fecha(c) + ' · ');
      var a = el('a', '', c.fuente);
      a.href = c.enlace; a.target = '_blank'; a.rel = 'noopener';
      s.appendChild(a);
      li.appendChild(s);
      if (c.proximo) {
        var f = String(c.proximo.desde).split('-');
        li.appendChild(el('small', 'prox', 'Sube a ' + valor({ valor: c.proximo.valor, formato: c.formato, unidad: c.unidad }) +
          ' desde el ' + Number(f[2]) + ' de ' + MESES[Number(f[1]) - 1] + ' de ' + f[0] + '.'));
      }
      ul.appendChild(li);
    });
    caja.appendChild(ul);
    caja.appendChild(el('p', 'rev', 'Actualizado el ' + hoyTexto(D.revisado) +
      '. Un robot de Simplelife revisa las fuentes oficiales todos los días: los datos diarios cambian cada día hábil y los mensuales, cuando la entidad publica el mes nuevo.'));
    lead.parentNode.insertBefore(caja, lead.nextSibling);
  }

  function cargar() {
    fetch('cifras.json', { cache: 'no-cache' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (D) { if (D) pintar(D); })
      .catch(function () {});
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', cargar);
  else cargar();
})();
