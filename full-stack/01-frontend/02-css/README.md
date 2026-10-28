# 02-css

## 1. Qué es y para qué sirve
CSS (Cascading Style Sheets, hojas de estilo en cascada) es un lenguaje de hojas de estilo usado para describir la presentación de un documento HTML. Sirve para controlar colores, tipografías, espaciados, layout (diseño), posicionamiento y responsive design (diseño adaptable).

## 2. Por qué importa dentro del roadmap y cómo se conecta
Después de estructurar con HTML, CSS da estilo visual. Se conecta con HTML (selectores apuntan a elementos) y prepara el camino para JavaScript (que puede manipular estilos dinámicamente).

## 3. Conceptos clave

### Formas de aplicar CSS
- Inline (en línea): `<p style="color: red;">`
- Interno: `<style>` en `<head>`
- Externo: `<link rel="stylesheet" href="styles.css">` (recomendado)

### Selectores
- Elemento: `p { ... }`
- Clase: `.clase { ... }`
- ID: `#id { ... }`
- Combinadores y pseudoclases (pseudo-clases): `:hover`, `:nth-child()`

### Box Model (modelo de caja)
Todo elemento es una caja: content (contenido), padding (relleno), border (borde), margin (margen).
```css
.caja {
  width: 200px;
  padding: 10px;
  border: 1px solid black;
  margin: 20px;
}
```

### Layout básico
- Display: `block`, `inline`, `inline-block`, `flex`, `grid`
- Flexbox (caja flexible): para alineación y distribución unidimensional
- Grid (rejilla): para diseño bidimensional

### Unidades
- Absolutas: `px`
- Relativas: `%`, `em`, `rem`, `vw`, `vh`

## 4. Ejemplos de código comentados, correctos y ejecutables

HTML + CSS externo:
```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="styles.css">
  <title>Ejemplo CSS</title>
</head>
<body>
  <h1 class="titulo">Hola CSS</h1>
  <p id="intro">Aprendiendo estilos.</p>
</body>
</html>
```

```css
/* styles.css */
/* Selector por clase */
.titulo {
  color: #2c3e50;
  font-size: 2rem;
}

/* Selector por ID */
#intro {
  color: #34495e;
  line-height: 1.5;
}

/* Pseudoclase */
.titulo:hover {
  color: #e74c3c;
}
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Usar IDs para todo (mejor usar clases reutilizables).
- No considerar el Box Model al calcular anchos.
- Especificidad (especificidad) mal entendida.
- Valores fijos que rompen responsive design.

Buenas prácticas:
- CSS externo.
- Nombres de clases descriptivos (metodologías como BEM - Block Element Modifier, bloque elemento modificador, se puede revisar luego).
- Usar unidades relativas cuando convenga.
- Mobile-first (móvil primero) para diseño adaptable.
- Mantener código organizado.

## 6. Autoevaluación

1. ¿Cuál es la diferencia entre margin y padding?
2. ¿Qué es el Box Model?
3. ¿Cuándo usarías Flexbox vs Grid?
4. ¿Qué significa "cascada" en CSS?
5. Menciona dos formas de aplicar CSS y cuál es la recomendada.

Respuestas orientativas:
1. Margin es espacio fuera de la caja, padding dentro entre contenido y borde.
2. Conjunto de content, padding, border, margin.
3. Flexbox unidimensional, Grid bidimensional.
4. Prioridad de estilos según origen, especificidad y orden.
5. Inline, interno, externo; recomendado externo.
