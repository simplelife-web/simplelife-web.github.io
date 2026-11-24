// Cursor de los gráficos: al pasar el mouse o el dedo, muestra el mes y el valor exacto.
(function () {
  var MESES = ['ene.', 'feb.', 'mar.', 'abr.', 'may.', 'jun.', 'jul.', 'ago.', 'set.', 'oct.', 'nov.', 'dic.'];
  var NS = 'http://www.w3.org/2000/svg';
  function fmt(v, d) {
    var s = Math.abs(v).toFixed(d).split('.');
    if (s[0].length > 4) s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
    return (v < 0 ? '−' : '') + s.join('.');
  }
  function mes(x0, i) {
    var a = +x0.slice(0, 4), m = +x0.slice(5, 7) - 1 + i;
    return MESES[m % 12] + ' ' + (a + Math.floor(m / 12));
  }
  document.querySelectorAll('svg.graf[data-g]').forEach(function (svg) {
    var g;
    try { g = JSON.parse(svg.getAttribute('data-g')); } catch (e) { return; }
    var caja = svg.parentNode;
    var vb = svg.viewBox.baseVal;
    var linea = document.createElementNS(NS, 'line');
    linea.setAttribute('class', 'g-cursor');
    linea.setAttribute('y1', g.mt); linea.setAttribute('y2', g.mt + g.ph);
    var puntos = g.s.map(function (s) {
      var c = document.createElementNS(NS, 'circle');
      c.setAttribute('r', 5); c.setAttribute('class', 'g-cursor-p g-punto ' + s.c);
      return c;
    });
    var tip = document.createElement('div');
    tip.className = 'g-tip'; tip.hidden = true;
    caja.appendChild(tip);
    function ocultar() {
      tip.hidden = true;
      if (linea.parentNode) svg.removeChild(linea);
      puntos.forEach(function (c) { if (c.parentNode) svg.removeChild(c); });
    }
    function mover(ev) {
      var r = svg.getBoundingClientRect();
      var esc = r.width / vb.width;
      var x = (ev.clientX - r.left) / esc;
      var i = Math.round((x - g.ml) / g.pw * (g.n - 1));
      i = Math.max(0, Math.min(g.n - 1, i));
      var hay = g.s.some(function (s) { return s.v[i] != null; });
      if (!hay) { ocultar(); return; }
      var X = g.ml + g.pw * i / Math.max(g.n - 1, 1);
      linea.setAttribute('x1', X); linea.setAttribute('x2', X);
      svg.appendChild(linea);
      var html = '<b>' + mes(g.x0, i) + '</b>';
      g.s.forEach(function (s, k) {
        var v = s.v[i];
        if (v == null) { if (puntos[k].parentNode) svg.removeChild(puntos[k]); return; }
        puntos[k].setAttribute('cx', X);
        puntos[k].setAttribute('cy', g.mt + g.ph * (1 - (v - g.lo) / (g.hi - g.lo)));
        svg.appendChild(puntos[k]);
        html += '<span><i class="' + s.c + '"></i>' + (g.s.length > 1 ? s.n + ': ' : '') + fmt(v, g.d) + (g.u === '%' ? ' %' : '') + '</span><br>';
      });
      tip.innerHTML = html;
      tip.hidden = false;
      var px = X * esc, ancho = tip.offsetWidth;
      var izq = px + 12 + ancho > r.width ? px - 12 - ancho : px + 12;
      tip.style.left = Math.max(0, izq) + 'px';
      tip.style.top = (g.mt * esc) + 'px';
    }
    var toque = svg.querySelector('.g-toque');
    toque.addEventListener('pointermove', mover);
    toque.addEventListener('pointerdown', mover);
    toque.addEventListener('pointerleave', ocultar);
  });
})();
