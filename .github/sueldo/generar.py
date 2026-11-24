"""Genera sueldo/index.html desde .github/sueldo/plantilla.html.

Las fórmulas se escriben en la plantilla como {{TEX:...}} (en línea) o
{{TEXD:...}} (centradas) y se convierten en HTML con KaTeX, igual que el glosario,
para que la página no necesite JavaScript extra para mostrarlas.

Uso (desde la raíz del repositorio):
    npm i --prefix /tmp/kt katex@0.16.11      # solo la primera vez
    KATEX=/tmp/kt/node_modules/katex python3 .github/sueldo/generar.py
"""
import json, os, re, subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
plantilla = open(os.path.join(AQUI, "plantilla.html"), encoding="utf-8").read()
patron = re.compile(r"\{\{(TEXD?):(.+?)\}\}(?!\})", re.S)
pedidos = [[m.group(2).strip(), m.group(1) == "TEXD"] for m in patron.finditer(plantilla)]
res = subprocess.run(["node", os.path.join(RAIZ, ".github", "glosario", "katex-render.cjs")],
                     input=json.dumps(pedidos), capture_output=True, text=True, check=True)
htmls = iter(json.loads(res.stdout))
salida = patron.sub(lambda m: (('<div class="ecuacion">%s</div>' if m.group(1) == "TEXD" else "%s") % next(htmls)), plantilla)
open(os.path.join(RAIZ, "sueldo", "index.html"), "w", encoding="utf-8").write(salida)
print("sueldo/index.html listo con", len(pedidos), "fórmulas")
