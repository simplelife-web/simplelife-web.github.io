# Guía: activar "Yo te enseño, tú me enseñas" (todo gratis)

La página ya funciona y muestra **ofertas de ejemplo**. Para que reciba ofertas reales solo necesitas tu cuenta de Google (Gmail). Son unos 20 minutos.

Al final tendrás 3 enlaces que pegarás en el archivo `intercambio/config.js`.

---

## Paso 1. Formulario "Publicar mi oferta"

1. Entra a https://forms.google.com y crea un formulario en blanco llamado **Yo te enseño, tú me enseñas: publicar mi oferta**.
2. Agrega estas preguntas **en este orden** y con estos títulos (la página reconoce las columnas por sus palabras):

| N.° | Título de la pregunta | Tipo | Obligatoria | ¿Se publica? |
|---|---|---|---|---|
| 1 | Tu nombre o apodo | Respuesta corta | Sí | Sí |
| 2 | Tu generación | Varias opciones: *Menos de 30 años*, *30 a 59 años*, *60 años o más* | Sí | Sí |
| 3 | Distrito y ciudad | Respuesta corta | Sí | Sí |
| 4 | ¿Qué puedes enseñar? | Respuesta corta | Sí | Sí |
| 5 | Categoría de lo que enseñas | Desplegable: *Tecnología y celular*, *Cocina*, *Costura y tejido*, *Jardinería y plantas*, *Oficios y reparaciones*, *Idiomas*, *Música y arte*, *Estudios y finanzas*, *Otros* | Sí | Sí |
| 6 | ¿Qué te gustaría aprender? | Respuesta corta | Sí | Sí |
| 7 | Modalidad | Varias opciones: *Presencial*, *Virtual*, *Ambas* | Sí | Sí |
| 8 | Cuéntanos un poco de ti (opcional) | Párrafo | No | Sí |
| 9 | Correo electrónico (privado, no se publica) | Respuesta corta | Sí | **No** |
| 10 | WhatsApp o teléfono (opcional, privado) | Respuesta corta | No | **No** |
| 11 | Acepto la política de privacidad: https://simplelife-web.github.io/intercambio/privacidad.html | Casillas: *Acepto* | Sí | **No** |

> Escribe las categorías **exactamente** como están arriba, para que funcione el filtro de la página.
> No actives "Recopilar correos electrónicos" en Configuración, porque cambia el orden de las columnas.

3. Pestaña **Respuestas** → **Vincular con Hojas de cálculo** → **Crear una hoja de cálculo nueva**.
4. Botón **Enviar** → ícono de enlace 🔗 → **Copiar**. Este es tu **enlace 1** (`formPublicar`).

## Paso 2. Hoja que revisa y publica

Abre la hoja de cálculo que se creó. La primera pestaña se llama **Respuestas de formulario 1**.

1. En la primera fila vacía a la derecha (columna **M**) escribe el título **Aprobado**.
2. Cada vez que llegue una oferta, léela. Si está bien (sin datos privados en el texto, sin cobros, sin cosas raras), escribe **Sí** en su columna M.
3. Crea una pestaña nueva (botón **+** abajo) y llámala **Publicadas**.
4. En la celda **A1** de Publicadas pega esta fórmula:

```
=QUERY('Respuestas de formulario 1'!A:M, "select A,B,C,D,E,F,G,H,I where M = 'Sí'", 1)
```

Si sale error, cambia las comas `,` que separan las partes por punto y coma `;`.

Así la pestaña Publicadas **solo** tiene columnas públicas (A a I). El correo y el teléfono (J y K) se quedan escondidos.

5. **Archivo → Compartir → Publicar en la web**. Elige la pestaña **Publicadas** (¡no "Todo el documento"!) y el formato **Valores separados por comas (.csv)**. Pulsa **Publicar** y copia el enlace. Este es tu **enlace 3** (`hojaCSV`).

> Importante: nunca publiques la pestaña "Respuestas de formulario 1", porque ahí están los correos.
> Los cambios pueden tardar unos 5 minutos en verse en la página.

## Paso 3. Formulario "Quiero contactar"

1. Crea otro formulario: **Yo te enseño, tú me enseñas: quiero contactar**.
2. Preguntas:
   1. Oferta que te interesa (Respuesta corta, obligatoria)
   2. Tu nombre (Respuesta corta, obligatoria)
   3. Tu correo electrónico (Respuesta corta, obligatoria)
   4. Tu mensaje: preséntate y cuenta qué puedes enseñar a cambio (Párrafo, obligatoria)
   5. Acepto que Simplelife envíe mi mensaje y mi correo a la persona de la oferta (Casillas: *Acepto*, obligatoria)
3. Menú de los tres puntos ⋮ → **Obtener enlace prellenado**. En "Oferta que te interesa" escribe **OFERTA** (en mayúsculas) y pulsa **Obtener enlace** → **Copiar enlace**. Este es tu **enlace 2** (`formContacto`).
4. En la pestaña **Respuestas** → ⋮ → activa **Recibir notificaciones por correo electrónico**, para enterarte cuando alguien escriba.

## Paso 4. Pegar los enlaces

Abre `intercambio/config.js` en GitHub (ícono del lápiz ✏️), pega cada enlace entre las comillas y guarda con **Commit changes**. O pásamelos y lo hago yo.

## Paso 5. Presentar a las personas (cada vez que llegue un contacto)

1. Te llega un aviso al correo. Mira qué oferta eligió la persona.
2. Busca esa oferta en tu hoja (por nombre y fecha) y copia su correo (columna J).
3. Envía **un solo correo** a la persona de la oferta, con copia a quien quiere aprender, por ejemplo:

> Hola, Rosa: Diego vio tu oferta de cocina criolla en Yo te enseño, tú me enseñas y quiere aprender contigo. Su mensaje: "…". Pueden responder a este correo para ponerse de acuerdo. Recuerden los consejos de seguridad: primera reunión por videollamada o en un lugar público. ¡Que disfruten el intercambio! Equipo Simplelife.

## Borrar una oferta

Si alguien lo pide, borra su fila en **Respuestas de formulario 1** (o cambia "Sí" por "No" en la columna M). Desaparece de la página en unos minutos.

---

**Costo total: S/ 0.** GitHub Pages, Google Forms y Google Sheets son gratis. Google Forms no tiene límite práctico de respuestas para este uso.
