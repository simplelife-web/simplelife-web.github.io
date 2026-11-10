# Guía: activar "Yo te enseño, tú me enseñas" (todo gratis)

La página ya funciona y muestra **ofertas de ejemplo**. Para recibir ofertas reales hay que crear dos formularios y dos hojas en tu Google. Un script lo hace todo por ti: solo lo pegas y pulsas un botón. Toma unos 5 minutos.

## Paso 1. Ejecutar el script (una sola vez)

1. Entra a https://script.google.com con tu Gmail y pulsa **Nuevo proyecto**.
2. Borra lo que aparece en el editor y pega **todo** el archivo [`crear-formularios.gs`](crear-formularios.gs).
3. Guarda con el ícono del disquete 💾.
4. Arriba, en la lista de funciones, elige **crearTodo** y pulsa **▶ Ejecutar**.
5. Google pedirá permiso. Pulsa **Revisar permisos**, elige tu cuenta y luego **Configuración avanzada → Ir a Proyecto sin título (no seguro) → Permitir**.
   El aviso "no seguro" sale porque el script es tuyo y Google no lo revisó. Solo trabaja dentro de tu cuenta.
6. Espera a que diga "Ejecución completada". Te llegará un correo **"Tus 3 enlaces de Yo te enseño, tú me enseñas"**.
7. Pásale esos 3 enlaces a Claude y él los pondrá en la página.

## Qué crea el script

| Qué | Para qué | ¿Pública? |
|---|---|---|
| Formulario "publicar mi oferta" | Para que la gente publique lo que enseña | Sí |
| Formulario "quiero contactar" | Para escribirle a la persona de una oferta | Sí |
| Hoja "respuestas (PRIVADO)" | Todas las respuestas, con correos y teléfonos | **No. No la compartas nunca.** |
| Hoja "ofertas publicadas (PÚBLICO)" | Solo las ofertas que apruebes, sin correos ni teléfonos | Sí, solo lectura |

## Tu trabajo del día a día

**Cuando llega una oferta**, te llega un correo "Nueva oferta para revisar". Ábrela en la hoja privada (pestaña **Ofertas**). Si está bien (sin cobros, sin datos privados en el texto, sin cosas raras), elige **Sí** en la columna **Aprobado**. En unos minutos aparece en la página.

**Cuando alguien quiere contactar**, te llega un correo "Alguien quiere aprender" con el mensaje y los correos de las dos personas. Si el mensaje está bien, envía **un solo correo** a la persona de la oferta, con copia a quien escribió, por ejemplo:

> Hola, Rosa: Diego vio tu oferta de cocina criolla en Yo te enseño, tú me enseñas y quiere aprender contigo. Su mensaje: "…". Pueden responder a este correo para ponerse de acuerdo. Recuerden los consejos de seguridad: la primera reunión por videollamada o en un lugar público. ¡Que disfruten el intercambio! Equipo Simplelife.

**Para quitar una oferta**, cambia **Sí** por **No** en la columna Aprobado (o borra la fila).

## Si algo falla

- Si perdiste el correo con los enlaces: en el mismo script elige la función **enviarmeLosEnlaces** y pulsa **Ejecutar**.
- No cambies el orden de las preguntas de los formularios ni agregues preguntas nuevas, porque el script cuenta las columnas.

---

**Costo total: S/ 0.** GitHub Pages, Google Forms, Google Sheets y Apps Script son gratis.
