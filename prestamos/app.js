/* Simulador de préstamos y ahorro de Simplelife. Todo se calcula en el navegador. */
(function () {
  "use strict";
  var $ = function (id) { return document.getElementById(id); };
  var MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","setiembre","octubre","noviembre","diciembre"];

  function num(v) {
    var t = String(v || "").trim().replace(/\s|S\/?|%/gi, "");
    if (!t) return null;
    if (/,\d{1,2}$/.test(t)) t = t.replace(/\./g, "").replace(",", "."); else t = t.replace(/,/g, "");
    var n = Number(t);
    return isFinite(n) ? n : null;
  }
  function soles(x, dec) { if (dec === undefined) dec = 2; return "S/ " + x.toLocaleString("es-PE", { minimumFractionDigits: dec, maximumFractionDigits: dec }); }
  function pct(x, dec) { return (x * 100).toLocaleString("es-PE", { minimumFractionDigits: dec, maximumFractionDigits: dec }) + " %"; }
  function plazoTxt(m) {
    if (m % 12 === 0) { var a = m / 12; return a + (a === 1 ? " año" : " años"); }
    return m + (m === 1 ? " mes" : " meses");
  }
  function tem(tea) { return Math.pow(1 + tea, 1 / 12) - 1; }
  function mensaje(id, txt) { $(id).innerHTML = '<span class="error">' + txt + "</span>"; }

  /* ---------- Pestañas ---------- */
  var modo = "p";
  function pestana(m, guardar) {
    modo = m;
    ["p", "a"].forEach(function (k) {
      $("tab-" + k).setAttribute("aria-selected", String(k === m));
      $("panel-" + k).classList.toggle("hidden", k !== m);
    });
    if (m === "p") calcP(guardar); else calcA(guardar);
  }
  $("tab-p").addEventListener("click", function () { pestana("p", true); });
  $("tab-a").addEventListener("click", function () { pestana("a", true); });

  function guardarURL(params) {
    var q = Object.keys(params).map(function (k) { return k + "=" + encodeURIComponent(params[k]); }).join("&");
    try { history.replaceState(null, "", "?" + q); } catch (e) {}
  }

  /* ---------- Préstamo ---------- */
  function cronograma(P, i, n, tipo, seg, com, extra) {
    var filas = [], S = P, R = i === 0 ? P / n : P * i / (1 - Math.pow(1 + i, -n)), A = P / n;
    for (var t = 1; t <= n && S > 0.005; t++) {
      var interes = S * i, amort = tipo === "a" ? A : R - interes;
      amort = t === n ? S : Math.min(S, amort + (extra || 0));
      var otros = S * seg + com;
      filas.push({ t: t, ini: S, interes: interes, amort: amort, otros: otros, cuota: interes + amort + otros });
      S = S - amort;
    }
    return filas;
  }
  function suma(filas, k) { return filas.reduce(function (s, f) { return s + f[k]; }, 0); }
  function tirMensual(P, pagos) {
    // Busca r tal que P = Σ pagos_t / (1+r)^t (bisección).
    var lo = 0, hi = 1;
    function vp(r) { var v = 0; for (var t = 0; t < pagos.length; t++) v += pagos[t] / Math.pow(1 + r, t + 1); return v; }
    if (vp(0) <= P) return 0;
    for (var k = 0; k < 200; k++) { var m = (lo + hi) / 2; if (vp(m) > P) lo = m; else hi = m; }
    return (lo + hi) / 2;
  }

  var ultimoCrono = [];
  function calcP(guardar) {
    var P = num($("p-monto").value), tea = num($("p-tea").value), n = Math.round(Number($("p-plazo").value));
    var tipo = $("p-tipo").value, seg = (num($("p-seg").value) || 0) / 100, com = num($("p-com").value) || 0, extra = num($("p-extra").value) || 0;
    if (P === null || P <= 0) return mensaje("p-frase", "Escribe un monto válido, por ejemplo 10000 o 10500.50.");
    if (tea === null || tea < 0 || tea > 1000) return mensaje("p-frase", "Escribe la TEA en porcentaje, por ejemplo 35 o 18.5.");
    if (!(n >= 1 && n <= 360)) return mensaje("p-frase", "El plazo debe estar entre 1 y 360 meses.");
    if (seg < 0 || com < 0 || extra < 0) return mensaje("p-frase", "El seguro, la comisión y el pago extra no pueden ser negativos.");
    var i = tem(tea / 100);
    var filas = cronograma(P, i, n, tipo, seg, com, extra);
    var base = cronograma(P, i, n, tipo, seg, com, 0);
    ultimoCrono = filas;
    var intereses = suma(filas, "interes"), otros = suma(filas, "otros"), total = suma(filas, "cuota");
    var r = tirMensual(P, filas.map(function (f) { return f.cuota; })), tcea = Math.pow(1 + r, 12) - 1;

    $("p-frase").textContent = tipo === "a" ? "Tu primera cuota sería (luego baja cada mes):" : (seg > 0 || com > 0 ? "Tu cuota mensual, con seguro y comisión, sería de unos:" : "Tu cuota mensual sería:");
    $("p-cifra").textContent = soles(filas[0].cuota) + (extra > 0 ? " + " + soles(extra, 0) + " extra" : "");
    $("p-s-int").textContent = soles(intereses);
    $("p-s-tot").textContent = soles(total);
    $("p-s-tem").textContent = pct(i, 2);
    $("p-s-tcea").textContent = pct(tcea, 2);

    var bar = $("p-prop").children, sum = P + intereses + otros;
    bar[0].style.width = (P / sum * 100) + "%"; bar[1].style.width = (intereses / sum * 100) + "%"; bar[2].style.width = (otros / sum * 100) + "%";
    $("p-ley").innerHTML = '<span><i style="background:var(--cap)"></i>Lo que te prestaron: ' + soles(P, 0) + '</span><span><i style="background:var(--int)"></i>Intereses: ' + soles(intereses, 0) + "</span>" +
      (otros > 0 ? '<span><i style="background:var(--warm)"></i>Seguro y comisiones: ' + soles(otros, 0) + "</span>" : "");

    var exp = "Por cada S/ 100 que te prestan devuelves " + soles(total / P * 100) + ". ";
    if (extra > 0) {
      var ahorro = suma(base, "interes") + suma(base, "otros") - intereses - otros;
      exp += "Con el pago extra de " + soles(extra, 0) + " al mes terminas en " + plazoTxt(filas.length) + " en lugar de " + plazoTxt(n) + " y te ahorras " + soles(ahorro) + " en intereses y seguros.";
    } else if (tipo === "a") {
      exp += "La última cuota sería de " + soles(filas[filas.length - 1].cuota) + ".";
    } else {
      exp += "La TEM de " + pct(i, 2) + " es la que se aplica cada mes sobre lo que aún debes.";
    }
    if (tcea - tea / 100 > 0.0005) exp += " El seguro y las comisiones suben el costo real de " + pct(tea / 100, 2) + " a " + pct(tcea, 2) + " al año.";
    $("p-explica").textContent = exp;

    graficoP(filas);
    comparar(P, i, tipo);
    tablaP(filas);
    if (guardar) guardarURL({ m: "p", monto: P, tea: tea, n: n, tipo: tipo, seg: seg * 100, com: com, extra: extra });
  }

  function graficoP(filas) {
    // Agrupa por año si hay más de 36 meses.
    var porAnio = filas.length > 36, grupos = [];
    filas.forEach(function (f) {
      var g = porAnio ? Math.ceil(f.t / 12) - 1 : f.t - 1;
      if (!grupos[g]) grupos[g] = { cap: 0, int: 0, et: porAnio ? "Año " + (g + 1) : String(f.t) };
      grupos[g].cap += f.amort; grupos[g].int += f.interes;
    });
    var W = 860, H = 260, L = 64, R = 10, T = 12, B = 30;
    var max = Math.max.apply(null, grupos.map(function (g) { return g.cap + g.int; })) * 1.05;
    var y = function (v) { return T + (1 - v / max) * (H - T - B); };
    var bw = (W - L - R) / grupos.length;
    var s = '<svg viewBox="0 0 ' + W + " " + H + '" xmlns="http://www.w3.org/2000/svg">';
    for (var k = 0; k <= 4; k++) {
      var v = max / 4 * k;
      s += '<line class="eje" x1="' + L + '" x2="' + (W - R) + '" y1="' + y(v).toFixed(1) + '" y2="' + y(v).toFixed(1) + '"/>';
      s += '<text x="' + (L - 6) + '" y="' + (y(v) + 4).toFixed(1) + '" text-anchor="end">' + Math.round(v).toLocaleString("es-PE") + "</text>";
    }
    var cada = Math.ceil(grupos.length / 14);
    grupos.forEach(function (g, idx) {
      var x = L + idx * bw + bw * 0.12, w = Math.max(1, bw * 0.76);
      var yc = y(g.cap), yi = y(g.cap + g.int);
      s += '<g><title>' + (porAnio ? g.et : "Mes " + g.et) + ": capital " + soles(g.cap) + ", intereses " + soles(g.int) + "</title>";
      s += '<rect x="' + x.toFixed(1) + '" y="' + yc.toFixed(1) + '" width="' + w.toFixed(1) + '" height="' + (H - B - yc).toFixed(1) + '" fill="var(--cap)"/>';
      s += '<rect x="' + x.toFixed(1) + '" y="' + yi.toFixed(1) + '" width="' + w.toFixed(1) + '" height="' + (yc - yi).toFixed(1) + '" fill="var(--int)"/></g>';
      if (idx % cada === 0 || idx === grupos.length - 1) s += '<text x="' + (x + w / 2).toFixed(1) + '" y="' + (H - B + 16) + '" text-anchor="middle">' + (porAnio ? "A" + (idx + 1) : g.et) + "</text>";
    });
    s += "</svg>";
    $("p-graf").innerHTML = s;
    $("p-g-txt").textContent = (porAnio ? "Cada barra es un año de pagos. " : "Cada barra es una cuota. ") + "Al inicio una buena parte se va en intereses; al final, casi todo baja tu deuda.";
  }

  function comparar(P, i, tipo) {
    var n0 = Math.round(Number($("p-plazo").value));
    var plazos = [6, 12, 18, 24, 36, 48, 60, 120, 240];
    if (plazos.indexOf(n0) < 0) { plazos.push(n0); plazos.sort(function (a, b) { return a - b; }); }
    $("p-comp").innerHTML = plazos.map(function (n) {
      var f = cronograma(P, i, n, tipo, 0, 0, 0), it = suma(f, "interes");
      var c = tipo === "a" ? soles(f[0].cuota) + " → " + soles(f[f.length - 1].cuota, 0) : soles(f[0].cuota);
      return '<tr' + (n === n0 ? ' class="marca"' : "") + "><td>" + plazoTxt(n) + (n === n0 ? " (tu plazo)" : "") + "</td><td>" + c + "</td><td>" + soles(it) + "</td><td>" + soles(it / P * 100) + "</td></tr>";
    }).join("");
  }

  function tablaP(filas) {
    var html = filas.map(function (f) {
      return "<tr><td>" + f.t + "</td><td>" + soles(f.ini) + "</td><td>" + soles(f.interes) + "</td><td>" + soles(f.amort) + "</td><td>" + soles(f.otros) + "</td><td>" + soles(f.cuota) + "</td><td>" + soles(Math.max(0, f.ini - f.amort)) + "</td></tr>";
    }).join("");
    html += '<tr class="marca"><td>Total</td><td></td><td>' + soles(suma(filas, "interes")) + "</td><td>" + soles(suma(filas, "amort")) + "</td><td>" + soles(suma(filas, "otros")) + "</td><td>" + soles(suma(filas, "cuota")) + "</td><td></td></tr>";
    $("p-crono").innerHTML = html;
  }

  $("p-csv").addEventListener("click", function () {
    var f2 = function (x) { return x.toFixed(2).replace(".", ","); };
    var lineas = ["Mes;Deuda al inicio;Interés;Capital;Seguro y comisión;Cuota total;Deuda al final"];
    ultimoCrono.forEach(function (f) { lineas.push([f.t, f2(f.ini), f2(f.interes), f2(f.amort), f2(f.otros), f2(f.cuota), f2(Math.max(0, f.ini - f.amort))].join(";")); });
    var blob = new Blob(["﻿" + lineas.join("\r\n")], { type: "text/csv;charset=utf-8" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = "cronograma-simplelife.csv";
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
  });

  /* ---------- Ahorro ---------- */
  function calcA(guardar) {
    var C0 = num($("a-ini").value) || 0, A = num($("a-apo").value) || 0, tea = num($("a-tea").value), n = Math.round(Number($("a-plazo").value));
    var inf = num($("a-inf").value), meta = num($("a-meta").value);
    if (C0 < 0 || A < 0) return mensaje("a-frase", "Los montos no pueden ser negativos.");
    if (C0 === 0 && A === 0) return mensaje("a-frase", "Escribe un monto inicial o un aporte mensual.");
    if (tea === null || tea < 0 || tea > 200) return mensaje("a-frase", "Escribe la TEA en porcentaje, por ejemplo 5 o 6.5.");
    if (!(n >= 1 && n <= 600)) return mensaje("a-frase", "El plazo debe estar entre 1 y 600 meses.");
    if (inf === null || inf <= -50) inf = 0;
    var i = tem(tea / 100), pi = inf / 100;
    var S = C0, filas = [];
    for (var t = 1; t <= n; t++) {
      S = S * (1 + i) + A;
      var puesto = C0 + A * t;
      if (t % 12 === 0 || t === n) filas.push({ t: t, puesto: puesto, saldo: S, real: S / Math.pow(1 + pi, t / 12) });
    }
    var puestoT = C0 + A * n, interes = S - puestoT, real = S / Math.pow(1 + pi, n / 12), tr = (1 + tea / 100) / (1 + pi) - 1;
    $("a-frase").textContent = "En " + plazoTxt(n) + " tendrías:";
    $("a-cifra").textContent = soles(S);
    $("a-s-apo").textContent = soles(puestoT);
    $("a-s-int").textContent = soles(interes);
    $("a-s-real").textContent = soles(real);
    $("a-s-tr").textContent = pct(tr, 2);
    var exp = "Los intereses son el " + pct(puestoT > 0 ? interes / puestoT : 0, 1) + " de lo que pusiste. ";
    if (tr < 0) exp += "Ojo: la TEA es menor que la inflación esperada, así que tu dinero pierde poder de compra aunque el saldo suba.";
    else exp += "Descontando una inflación de " + pct(pi, 1) + " al año, con ese saldo podrías comprar lo que hoy cuesta " + soles(real, 0) + ".";
    $("a-explica").textContent = exp;

    var mt = $("a-meta-txt");
    if (meta && meta > 0) {
      var fv0 = C0 * Math.pow(1 + i, n), fac = i === 0 ? n : (Math.pow(1 + i, n) - 1) / i, falta = meta - fv0;
      mt.classList.remove("hidden");
      if (falta <= 0) mt.textContent = "Con tu monto inicial ya llegas a tu meta de " + soles(meta, 0) + " sin aportar más.";
      else mt.textContent = "Para llegar a " + soles(meta, 0) + " en " + plazoTxt(n) + " necesitas ahorrar " + soles(falta / fac) + " cada mes" + (A > 0 ? " (hoy pones " + soles(A, 0) + ")." : ".");
    } else mt.classList.add("hidden");

    graficoA(C0, A, i, n);
    $("a-tabla").innerHTML = filas.map(function (f) {
      return "<tr><td>" + plazoTxt(f.t) + "</td><td>" + soles(f.puesto) + "</td><td>" + soles(f.saldo - f.puesto) + "</td><td>" + soles(f.saldo) + "</td><td>" + soles(f.real) + "</td></tr>";
    }).join("");
    if (guardar) guardarURL({ m: "a", ini: C0, apo: A, tea: tea, n: n, inf: inf, meta: meta || "" });
  }

  function graficoA(C0, A, i, n) {
    var W = 860, H = 260, L = 70, R = 10, T = 12, B = 30, pts = [], S = C0;
    pts.push({ t: 0, s: C0, p: C0 });
    for (var t = 1; t <= n; t++) { S = S * (1 + i) + A; pts.push({ t: t, s: S, p: C0 + A * t }); }
    var max = S * 1.05 || 1;
    var x = function (t) { return L + t / n * (W - L - R); }, y = function (v) { return T + (1 - v / max) * (H - T - B); };
    var s = '<svg viewBox="0 0 ' + W + " " + H + '" xmlns="http://www.w3.org/2000/svg">';
    for (var k = 0; k <= 4; k++) {
      var v = max / 4 * k;
      s += '<line class="eje" x1="' + L + '" x2="' + (W - R) + '" y1="' + y(v).toFixed(1) + '" y2="' + y(v).toFixed(1) + '"/>';
      s += '<text x="' + (L - 6) + '" y="' + (y(v) + 4).toFixed(1) + '" text-anchor="end">' + Math.round(v).toLocaleString("es-PE") + "</text>";
    }
    var arriba = pts.map(function (p) { return x(p.t).toFixed(1) + "," + y(p.s).toFixed(1); }).join(" ");
    var medio = pts.map(function (p) { return x(p.t).toFixed(1) + "," + y(p.p).toFixed(1); }).join(" ");
    var abajo = x(n).toFixed(1) + "," + y(0) + " " + x(0).toFixed(1) + "," + y(0);
    var medioRev = pts.slice().reverse().map(function (p) { return x(p.t).toFixed(1) + "," + y(p.p).toFixed(1); }).join(" ");
    s += '<polygon points="' + arriba + " " + medioRev + '" fill="var(--int)" opacity=".85"/>';
    s += '<polygon points="' + medio + " " + abajo + '" fill="var(--apo)"/>';
    s += '<polyline points="' + arriba + '" fill="none" stroke="var(--int)" stroke-width="2"/>';
    var paso = n > 24 ? 12 * Math.ceil(n / 12 / 10) : Math.max(1, Math.ceil(n / 12));
    for (var m = 0; m <= n; m += paso) s += '<text x="' + x(m).toFixed(1) + '" y="' + (H - B + 16) + '" text-anchor="middle">' + (n > 24 ? (m / 12) + (m === 0 ? "" : "a") : m + "m") + "</text>";
    s += "</svg>";
    $("a-graf").innerHTML = s;
  }

  /* ---------- Atajos, enlaces y arranque ---------- */
  function chip(cont, texto, fn) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "chip"; b.textContent = texto;
    b.addEventListener("click", fn); $(cont).appendChild(b);
  }
  function ponerP(m, tea, n) { $("p-monto").value = m; $("p-tea").value = tea; $("p-plazo").value = n; calcP(true); }
  chip("atajos-p", "Consumo: S/ 10 000 al 35 % en 2 años", function () { ponerP(10000, 35, 24); });
  chip("atajos-p", "Auto: S/ 60 000 al 14 % en 5 años", function () { ponerP(60000, 14, 60); });
  chip("atajos-p", "Vivienda: S/ 300 000 al 9 % en 20 años", function () { ponerP(300000, 9, 240); });
  chip("atajos-p", "Tarjeta: S/ 2 000 al 80 % en 12 meses", function () { ponerP(2000, 80, 12); });
  function ponerA(ini, apo, tea, n) { $("a-ini").value = ini; $("a-apo").value = apo; $("a-tea").value = tea; $("a-plazo").value = n; calcA(true); }
  chip("atajos-a", "Depósito a plazo: S/ 10 000 al 5 % por 1 año", function () { ponerA(10000, 0, 5, 12); });
  chip("atajos-a", "S/ 300 al mes al 4 % por 5 años", function () { ponerA(0, 300, 4, 60); });
  chip("atajos-a", "Fondo de emergencia: S/ 150 al mes por 2 años", function () { ponerA(0, 150, 3.5, 24); });

  ["p-monto", "p-tea", "p-plazo", "p-seg", "p-com", "p-extra"].forEach(function (id) { $(id).addEventListener("input", function () { calcP(true); }); });
  $("p-tipo").addEventListener("change", function () { calcP(true); });
  ["a-ini", "a-apo", "a-tea", "a-plazo", "a-inf", "a-meta"].forEach(function (id) { $(id).addEventListener("input", function () { calcA(true); }); });

  document.querySelectorAll("[data-copiar]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var url = location.href, txt = btn.textContent;
      function ok() { btn.textContent = "¡Enlace copiado!"; setTimeout(function () { btn.textContent = txt; }, 2000); }
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(ok, function () { prompt("Copia este enlace:", url); });
      else prompt("Copia este enlace:", url);
    });
  });

  // Lee un cálculo compartido por enlace.
  var q = new URLSearchParams(location.search);
  function desde(param, id) { if (q.get(param) !== null && q.get(param) !== "") $(id).value = q.get(param); }
  if (q.get("m") === "a") {
    desde("ini", "a-ini"); desde("apo", "a-apo"); desde("tea", "a-tea"); desde("n", "a-plazo"); desde("inf", "a-inf"); desde("meta", "a-meta");
  } else if (q.get("m") === "p") {
    desde("monto", "p-monto"); desde("tea", "p-tea"); desde("n", "p-plazo"); desde("seg", "p-seg"); desde("com", "p-com"); desde("extra", "p-extra");
    if (q.get("tipo") === "a") $("p-tipo").value = "a";
    if ((num(q.get("seg")) || 0) > 0 || (num(q.get("com")) || 0) > 0 || (num(q.get("extra")) || 0) > 0 || q.get("tipo") === "a") $("p-mas").open = true;
  }
  if (location.hash === "#ahorro" && !q.get("m")) q.set("m", "a");
  // Calcula las dos pestañas para que ambas estén listas.
  calcA(false); calcP(false);
  pestana(q.get("m") === "a" ? "a" : "p", false);

  // Tasas de referencia del BCRP (las actualiza el robot del glosario cada día).
  fetch("../glosario/cifras.json", { cache: "no-cache" }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (d) {
    var c = d.cifras || {};
    function mes(f) { var p = String(f || "").split("-"); return p.length >= 2 ? MESES[Number(p[1]) - 1] + " de " + p[0] : ""; }
    function poner(id, k, txtFecha) {
      if (!c[k]) return;
      $(id).innerHTML = '<a href="' + c[k].enlace + '" rel="noopener" target="_blank">' + c[k].valor.toLocaleString("es-PE", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " %</a>";
      return mes(c[k].fecha);
    }
    var f1 = poner("r-tamn", "tamn"); poner("r-tipmn", "tipmn"); var f3 = poner("r-inf", "inflacion12");
    var rv = String(d.revisado || "").split("-");
    $("r-fecha").textContent = "Tasas de " + (f1 || "el último mes") + "; inflación a " + (f3 || "el último mes") + ". Revisado el " + (rv.length === 3 ? Number(rv[2]) + " de " + MESES[Number(rv[1]) - 1] + " de " + rv[0] : "") + " (fuente: BCRP).";
  }).catch(function () {
    ["r-tamn", "r-tipmn", "r-inf"].forEach(function (id) { $(id).textContent = "—"; });
    $("r-fecha").textContent = "No pudimos cargar las tasas del BCRP. Vuelve a intentarlo más tarde.";
  });
})();
