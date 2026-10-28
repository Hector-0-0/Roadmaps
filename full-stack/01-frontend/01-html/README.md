# 01-html

## 1. Qué es y para qué sirve
HTML (HyperText Markup Language, lenguaje de marcado de hipertexto) es el lenguaje de marcado estándar para crear la estructura de páginas web. Sirve para definir elementos como encabezados, párrafos, listas, enlaces, imágenes, formularios y más. No es un lenguaje de programación, es un lenguaje de marcado.

## 2. Por qué importa dentro del roadmap y cómo se conecta
HTML es la base de cualquier sitio web. Todo lo que verás después (CSS, JavaScript) se aplica sobre la estructura que defines con HTML. Es el primer paso para entender cómo funciona la web.

## 3. Conceptos clave

### Estructura básica de un documento HTML
Todo documento HTML tiene una estructura mínima:
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi primera página</title>
</head>
<body>
  <h1>Hola mundo</h1>
</body>
</html>
```
- `<!DOCTYPE html>`: indica la versión de HTML.
- `<html lang="es">`: elemento raíz, idioma español.
- `<head>`: metadatos (información sobre la página).
- `<meta charset="UTF-8">`: codificación de caracteres.
- `<meta name="viewport">`: responsive (adaptable a dispositivos).
- `<title>`: título de la pestaña.
- `<body>`: contenido visible.

### Elementos (etiquetas) comunes
- Encabezados: `<h1>` a `<h6>`
- Párrafos: `<p>`
- Enlaces (hyperlinks, hipervínculos): `<a href="...">`
- Imágenes: `<img src="..." alt="...">`
- Listas: `<ul>`, `<ol>`, `<li>`
- Tablas: `<table>`, `<tr>`, `<th>`, `<td>`
- Formularios (forms, formularios): `<form>`, `<input>`, `<label>`, `<button>`

### Atributos
Los atributos proporcionan información adicional. Ejemplo: `href` en `<a>`, `src` y `alt` en `<img>`.

## 4. Ejemplos de código comentados, correctos y ejecutables

Ejemplo completo:
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Ejemplo HTML</title>
</head>
<body>
  <!-- Encabezado principal -->
  <h1>Bienvenido</h1>
  <!-- Párrafo -->
  <p>Este es un ejemplo básico de HTML.</p>
  <!-- Enlace -->
  <a href="https://www.w3.org">Sitio web oficial de W3C</a>
</body>
</html>
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Olvidar `alt` en imágenes (importante para accesibilidad).
- No cerrar etiquetas correctamente.
- Usar mayúsculas en etiquetas de forma inconsistente.
- Anidar elementos incorrectamente.

Buenas prácticas:
- Usar `<!DOCTYPE html>`.
- Especificar `lang`.
- Usar etiquetas semánticas (semantic HTML, HTML semántico) cuando sea posible: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`.
- Proporcionar texto alternativo en imágenes.
- Mantener estructura ordenada e indentada.

## 6. Autoevaluación

1. ¿HTML es un lenguaje de programación? Responde sí o no y por qué.
2. ¿Qué función tiene la etiqueta `<head>`?
3. ¿Para qué sirve el atributo `alt` en `<img>`?
4. Menciona tres etiquetas semánticas y su propósito.
5. ¿Cuál es la diferencia entre `<ul>` y `<ol>`?

Respuestas esperadas (orientativas):
1. No, es un lenguaje de marcado para estructurar contenido.
2. Contiene metadatos, no contenido visible.
3. Texto alternativo para accesibilidad y cuando la imagen no carga.
4. Ej: `<header>` (encabezado), `<nav>` (navegación), `<main>` (contenido principal).
5. `<ul>` lista no ordenada, `<ol>` lista ordenada.
