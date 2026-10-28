# Práctica - 01-html

## Nivel básico

1. **Estructura mínima válida**
   Enunciado: Crea un archivo `index.html` con la estructura mínima válida en español. Debe incluir `<!DOCTYPE html>`, elemento `html` con `lang="es"`, `head` con `meta charset="UTF-8"`, `meta name="viewport"`, `title` y `body`.
   Pista: Usa un editor de texto y guarda el archivo. Abre el archivo en el navegador para verificar que se carga sin errores.
   Criterio verificable: El archivo existe, tiene todas las etiquetas indicadas y al abrirlo en el navegador se muestra una página vacía sin errores en el inspector.

2. **Encabezados, párrafos y saltos**
   Enunciado: Añade un encabezado `h1`, un encabezado `h2`, al menos tres párrafos con texto real y usa `br` o estructura clara para separar contenido.
   Pista: Escribe contenido sobre un tema que conozcas. Asegúrate de cerrar correctamente todas las etiquetas.
   Criterio verificable: Se visualizan los encabezados en orden jerárquico y los párrafos correctamente separados en el navegador.

3. **Enlaces e imágenes con alt**
   Enunciado: Añade un enlace externo que abra en una nueva pestaña con `target="_blank"` y `rel="noopener noreferrer"`. Añade una imagen con atributo `alt` descriptivo.
   Pista: Usa una URL válida para el enlace. El atributo `alt` debe describir la imagen para accesibilidad.
   Criterio verificable: El enlace abre en nueva pestaña correctamente, la imagen se carga o muestra texto alternativo si falla, y ambos atributos están presentes.

## Nivel intermedio

4. **Listas ordenadas y no ordenadas**
   Enunciado: Crea una lista no ordenada con al menos 4 elementos y una lista ordenada con al menos 4 elementos. Usa contenido real relacionado con un tema.
   Pista: Usa `ul`/`li` para no ordenadas y `ol`/`li` para ordenadas. Anida correctamente las etiquetas.
   Criterio verificable: Ambas listas se renderizan correctamente en el navegador con sus viñetas o numeración.

5. **Tablas con encabezados**
   Enunciado: Crea una tabla con al menos 3 columnas, encabezados con `th`, al menos 3 filas de datos con `td`. Incluye `thead` y `tbody`.
   Pista: Estructura la tabla semánticamente. Usa datos reales como horarios o productos.
   Criterio verificable: La tabla muestra encabezados y datos correctamente, con estructura `thead`/`tbody` presente en el HTML.

6. **Formulario básico**
   Enunciado: Crea un formulario con campos `nombre` (text), `correo` (email), `mensaje` (textarea) y un botón de envío. Usa etiquetas `label` asociadas correctamente con `for` e `id`.
   Pista: Asocia cada label con su input usando atributos correctos. Usa tipos de input apropiados.
   Criterio verificable: El formulario muestra todos los campos, labels asociados correctamente y el botón es funcional en la estructura HTML.

## Nivel desafío

7. **Página semántica completa**
   Enunciado: Estructura una página usando etiquetas semánticas: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`. Incluye contenido real en cada sección.
   Pista: Usa `nav` para enlaces de navegación, `main` para contenido principal, `footer` para información final.
   Criterio verificable: Todas las etiquetas semánticas están presentes y correctamente anidadas, con contenido visible en el navegador.

8. **Página integrada HTML completo**
   Enunciado: Combina todos los elementos anteriores en una sola página coherente: estructura semántica, listas, tabla, formulario y navegación funcional entre secciones usando anclas `id` y enlaces.
   Pista: Usa `id` en secciones y `href="#id"` para navegación interna. Mantén el código ordenado e indentado.
   Criterio verificable: La página funciona completamente, la navegación interna funciona, todos los elementos están presentes y el HTML es válido estructuralmente.
