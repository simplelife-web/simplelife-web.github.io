// Achica un poco las fórmulas que no caben en pantallas pequeñas (celulares).
// Si aun así no caben, se pueden deslizar de lado.
(function () {
  function ajustar() {
    document.querySelectorAll('.ecuacion').forEach(function (caja) {
      var k = caja.querySelector('.katex-display > .katex');
      if (!k) return;
      k.style.fontSize = '';
      var ancho = caja.clientWidth, real = caja.scrollWidth;
      if (real > ancho + 1) k.style.fontSize = Math.max(0.5, ancho / real * 0.98) * 1.12 + 'em';
    });
  }
  ajustar();
  var t;
  window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(ajustar, 150); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(ajustar);
})();
