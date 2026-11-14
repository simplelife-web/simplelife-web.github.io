# Simplelife

Herramientas gratuitas para hacer la vida más simple. La página principal (`index.html`) es la portada con un cuadro por herramienta. Para agregar una herramienta nueva, crea su carpeta, copia uno de los bloques `<li>` de `index.html` con su enlace y súmala a `sitemap.xml`.

| Carpeta | Herramienta |
|---|---|
| `transcriptor/` | Transcriptor gratuito de audio |
| `tramites/` | Trámite fácil Perú |
| `youtube/` | Transcribir videos de YouTube (usa el modelo de `transcriptor/`; `intercambio/` solo redirige aquí) |
| `quehagohoy/` | ¿Qué hago hoy? (planes gratis en Lima, en un mapa) |
| `inflacion/` | Calculadora de inflación Perú (IPC de Lima del BCRP) |
| `glosario/` | Glosario económico explicado en simple |

## ¿Qué hago hoy? (`/quehagohoy/`)

Mapa de planes gratis o económicos en Lima (OpenStreetMap con Leaflet, copiado en `quehagohoy/lib/`, sin claves ni pagos).

- `quehagohoy/lugares.json`: lugares fijos (museos, parques, paseos) con su enlace oficial.
- `quehagohoy/fuentes.json`: páginas oficiales que revisa el robot.
- `quehagohoy/distritos.json`: los 43 distritos de Lima y los 7 del Callao con su centro aproximado. Si un distrito aún no tiene lugares, la página muestra los más cercanos.
- `quehagohoy/eventos.json`: lo escribe solo el robot. No se edita a mano.
- Robot: `.github/robot/buscar-eventos.mjs`, lanzado por `.github/workflows/quehagohoy.yml` cada día a las 6:00 a. m. de Lima (GitHub Actions, gratis). Lee la agenda solo si la página la publica en formato abierto (calendario de WordPress o RSS) y respeta su `robots.txt`. Cada evento enlaza a su publicación oficial; los vencidos se ocultan solos.
- El primer domingo de cada mes (Museos Abiertos, Ley 30599) lo calcula la propia página.
- `.github/robot/revisar-lugares.mjs` (opcional, a mano): comprueba los enlaces oficiales y compara los puntos del mapa con OpenStreetMap.

## Transcriptor gratuito de audio (`/transcriptor/`)

Página web que convierte audio o video en texto. Todo ocurre en el navegador de quien la usa:

- **Gratis para siempre**: no hay servidor que pagar; la página es estática.
- **Sin límite de duración**: el audio se lee de 10 en 10 minutos y se transcribe en tramos de unos 28 segundos, cortados en silencios para no partir palabras.
- **Privada**: el archivo nunca se sube a internet.
- **Modelo**: Whisper (código abierto), mediante Transformers.js. Usa la tarjeta gráfica (WebGPU) si el navegador lo permite; si no, el procesador.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `transcriptor/index.html` | La página y su lógica (lectura del audio, cortes, botones). |
| `transcriptor/worker.js` | Carga Whisper y transcribe en segundo plano. |
| `transcriptor/lib/ort-*` | ONNX Runtime Web (motor de IA). Transformers.js 4.3.1 se carga desde jsDelivr. |
| `transcriptor/lib/ffmpeg/` | FFmpeg.wasm 0.12 (lee cualquier formato y audios largos por partes). |

## Publicarla gratis

**Opción A, la más fácil (Netlify Drop):** entra a https://app.netlify.com/drop, crea una cuenta gratis y arrastra la carpeta `transcriptor-web` completa. Te da un enlace al instante.

**Opción B (GitHub Pages):** sube esta carpeta a un repositorio y activa *Settings → Pages → Deploy from a branch → main / (root)*. Ojo: la web de GitHub no deja subir archivos de más de 25 MB arrastrándolos, y dos archivos de `lib/` pesan más; hay que subirlos con `git push` (o con GitHub Desktop).

Para probarla en tu computadora sin publicarla: en esta carpeta ejecuta `python -m http.server` y abre http://localhost:8000 (abrir `index.html` con doble clic no funciona).

## Licencias

Transformers.js y ONNX Runtime: Apache 2.0 y MIT. `@ffmpeg/ffmpeg`: MIT. `@ffmpeg/core` (FFmpeg compilado a WebAssembly): GPL 2.0 o posterior; su código fuente está en https://github.com/ffmpegwasm/ffmpeg.wasm. Modelos Whisper: MIT (OpenAI), descargados desde Hugging Face (onnx-community).

## Trámite fácil Perú (`/tramites/`)

Guías sencillas de trámites del Perú (RENIEC, SUNAT, municipalidades y otras entidades), con letra grande y enlaces oficiales. Son páginas HTML estáticas en la carpeta `tramites/`, con un estilo común (`estilo.css`) y botones para agrandar la letra (`letra.js`). Cada guía indica la fecha de revisión y su fuente: los costos cambian, así que conviene revisarlos cada cierto tiempo. La portada tiene buscador y cuadros por tema; cada tema tiene su propia página (`seccion-*.html`, lista `SECC` en el generador) y cada guía muestra la barra de temas, la ruta «Trámites › Tema» y «Más trámites de este tema». Todas las páginas se generan con `.github/tramites/generar.py` (los datos de cada guía están ahí): edita ese archivo y ejecuta `python3 .github/tramites/generar.py tramites`.

## Glosario económico (`/glosario/`)

Conceptos de economía y finanzas explicados con palabras sencillas, con ejemplos del Perú y fórmulas. Hay una página por término (por ejemplo, `glosario/inflacion.html`) y una portada con buscador y filtros por tema.

- El contenido está en `.github/glosario/terminos1.py` y `terminos2.py`. No edites a mano las páginas de `glosario/`: se generan solas.
- Para agregar o corregir un término, cambia esos archivos y ejecuta, desde la raíz:
  `npm i --prefix /tmp/kt katex@0.16.11` (solo la primera vez) y luego `KATEX=/tmp/kt/node_modules/katex python3 .github/glosario/generar.py`.
  Eso rehace las páginas y actualiza `sitemap.xml`.
- Las fórmulas se dibujan con KaTeX (licencia MIT) al generar las páginas; en `glosario/katex/` están su hoja de estilo y sus letras.

## Barra de navegación (`nav.js`)

La barra de arriba (logo, herramientas, Acerca, Privacidad y "Volver al inicio") sale de un solo archivo, `nav.js`, que cargan todas las páginas. Para sumar una herramienta nueva a la barra, agrégala a la lista `HERRAMIENTAS` de ese archivo, y en su página pon `<script src="../nav.js"></script>` justo después de `<body>`.

## Calculadora de inflación Perú (`/inflacion/`)

Calcula cuánto valen hoy soles de una fecha pasada con el IPC de Lima Metropolitana (serie PN38705PM del BCRP, índice dic. 2021 = 100, desde enero de 1991).

- `inflacion/ipc.json`: un número por mes desde `desde`. Lo escribe solo el robot; no se edita a mano.
- Robot: `.github/robot/actualizar-ipc.mjs`, lanzado por `.github/workflows/inflacion.yml` del 1 al 15 de cada mes a las 7:30 a. m. de Lima. Si el BCRP no responde o los datos vienen con huecos, no guarda nada.
