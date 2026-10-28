# 04-javascript

## 1. Qué es y para qué sirve
JavaScript (JS, JavaScript) es un lenguaje de programación interpretado, multiparadigma y de alto nivel. Se ejecuta principalmente en el navegador (browser) para añadir interactividad a las páginas web, aunque también se usa en servidor con Node.js.

## 2. Por qué importa dentro del roadmap y cómo se conecta
JavaScript permite responder a acciones del usuario (eventos), manipular el DOM (Document Object Model, modelo de objetos del documento), validar formularios y comunicarse con servidores. Se conecta con HTML/CSS y es la base para aprender Node.js después.

## 3. Conceptos clave

### Variables y tipos
```javascript
let nombre = "Ana"; // string
const edad = 25;    // number
let activo = true;  // boolean
let datos = null;   // null
let sinDefinir;     // undefined
```

### Operadores, condicionales, bucles
```javascript
if (edad >= 18) {
  console.log("Mayor de edad");
}

for (let i = 0; i < 3; i++) {
  console.log(i);
}
```

### Funciones
```javascript
function sumar(a, b) {
  return a + b;
}
const restar = (a, b) => a - b;
```

### Arrays (arreglos) y objetos
```javascript
const frutas = ["manzana", "pera"];
const persona = { nombre: "Ana", edad: 25 };
```

### DOM (Document Object Model)
```javascript
const titulo = document.querySelector("#titulo");
titulo.textContent = "Nuevo título";
```

### Eventos
```javascript
const boton = document.querySelector("#btn");
boton.addEventListener("click", () => {
  alert("Botón clickeado");
});
```

## 4. Ejemplos de código comentados, correctos y ejecutables

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>JS Básico</title>
</head>
<body>
  <button id="btn">Cambiar color</button>
  <script src="app.js"></script>
</body>
</html>
```

```javascript
// app.js
const boton = document.querySelector("#btn");
boton.addEventListener("click", () => {
  document.body.style.backgroundColor = "#f0f0f0";
});
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Usar `var` en lugar de `let`/`const`.
- Comparar con `==` en lugar de `===`.
- Modificar DOM antes de que cargue (usar `DOMContentLoaded`).
- No manejar errores básicos.

Buenas prácticas:
- Usar `const` por defecto, `let` cuando cambie.
- Usar `===` para comparación estricta.
- Separar JS en archivo externo.
- Usar nombres descriptivos.
- Comentar solo cuando necesario, código claro.

## 6. Autoevaluación

1. ¿Cuál es la diferencia entre `let`, `const` y `var`?
2. ¿Qué es el DOM?
3. ¿Para qué sirve `addEventListener`?
4. ¿Cuál es la diferencia entre `==` y `===`?
5. ¿Qué hace `querySelector`?

Respuestas orientativas:
1. `const` no reasignable, `let` reasignable en bloque, `var` con alcance de función (evitar).
2. Representación del documento HTML como objetos manipulables.
3. Escuchar eventos (click, submit, etc.) y ejecutar funciones.
4. `==` compara con coerción, `===` comparación estricta sin coerción.
5. Selecciona el primer elemento que coincida con selector CSS.
