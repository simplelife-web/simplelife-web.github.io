// Botones A− / A+ para cambiar el tamaño de la letra (se recuerda en este navegador)
(function () {
  var MIN = 16, MAX = 28, root = document.documentElement;
  function leer() { try { return parseInt(localStorage.getItem('tf-letra'), 10) || 0; } catch (e) { return 0; } }
  function poner(px) {
    if (px) root.style.setProperty('--base', px + 'px');
    try { localStorage.setItem('tf-letra', px); } catch (e) {}
  }
  var guardado = leer();
  if (guardado) root.style.setProperty('--base', guardado + 'px');
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest('[data-letra]');
    if (!b) return;
    var actual = parseFloat(getComputedStyle(root).fontSize) || 19;
    var nuevo = Math.min(MAX, Math.max(MIN, Math.round(actual + 2 * Number(b.dataset.letra))));
    poner(nuevo);
  });
})();
