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

## Cómo funciona solo

1. **Llega una oferta.** Te llega un correo "Nueva oferta para verificar" con un enlace directo a su fila. Si el script ve algo sospechoso (enlaces, correos o teléfonos en el texto, precios o cobros), el asunto empieza con ⚠️.
2. **Tú la verificas.** Si está bien, elige **Sí** en la columna **Aprobado**. La oferta se publica en unos minutos y la persona recibe solo un correo "Tu oferta ya está publicada".
3. **Alguien quiere aprender.** El script envía solo **un correo de presentación** a las dos personas, con los consejos de seguridad, y tú recibes una copia oculta. Si el mensaje parece sospechoso, no lo envía y te lo manda a ti para que decidas.

**Para quitar una oferta**, elige **No** en la columna Aprobado (o borra la fila).

**Si actualizas el script:** pega la versión nueva, guarda, elige la función **actualizar** y pulsa **Ejecutar** (una sola vez).

## Si algo falla

- Si perdiste el correo con los enlaces: en el mismo script elige la función **enviarmeLosEnlaces** y pulsa **Ejecutar**.
- No cambies el orden de las preguntas de los formularios ni agregues preguntas nuevas, porque el script cuenta las columnas.

---

**Costo total: S/ 0.** GitHub Pages, Google Forms, Google Sheets y Apps Script son gratis.
