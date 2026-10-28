# Práctica - 04-javascript

## Nivel básico

1. **Variables, tipos y typeof**
   Enunciado: Declara variables usando `let`, `const` y `var` con diferentes tipos de datos (string, number, boolean, null, undefined, array, objeto). Muestra el tipo de cada una con `typeof` usando `console.log`.
   Pista: Observa las diferencias entre `let`, `const` y `var` en cuanto a reasignación. `const` no permite reasignación pero los objetos/arrays sí pueden mutarse.
   Criterio verificable: Se muestran en consola los valores y tipos correctos de al menos 7 variables diferentes usando los tres tipos de declaración.

2. **Operadores y condicionales**
   Enunciado: Crea un programa que determine si un número es par o impar, si es positivo o negativo, y que use una estructura `if/else if/else`. También usa el operador ternario en al menos un caso.
   Pista: Usa el operador módulo `%` para verificar par/impar. Prueba con números positivos, negativos y cero.
   Criterio verificable: El programa muestra correctamente el resultado para al menos 3 números diferentes usando condicionales y operador ternario.

3. **Bucles y arrays**
   Enunciado: Crea un array con al menos 5 elementos. Usa un bucle `for`, un `for...of` y `forEach` para recorrerlo e imprimir cada elemento. Calcula la suma de números usando un bucle.
   Pista: `forEach` recibe callback con elemento, índice y array. Calcula suma acumulando en una variable.
   Criterio verificable: Se imprimen todos los elementos con los tres tipos de bucle y se muestra la suma correcta de los números.

## Nivel intermedio

4. **Funciones, arrow functions y scope**
   Enunciado: Crea funciones tradicionales, arrow functions y funciones que retornen valores. Demuestra scope con `let`/`const` en bloques. Usa parámetros con valores por defecto.
   Pista: Recuerda que las arrow functions no tienen su propio `this`. Los parámetros por defecto se asignan con `param = valor`.
   Criterio verificable: Se ejecutan correctamente al menos 3 tipos de funciones mostrando valores retornados y comportamiento de scope.

5. **Objetos y métodos**
   Enunciado: Crea un objeto con propiedades y métodos. Usa `this` correctamente. Añade, modifica y elimina propiedades con notación de punto y corchetes. Usa `Object.keys()`, `Object.values()` o `Object.entries()`.
   Pista: Los métodos son funciones dentro del objeto. Usa `this.propiedad` para acceder a propiedades del mismo objeto.
   Criterio verificable: Se manipulan las propiedades del objeto correctamente y se muestran las claves/valores usando métodos de Object.

6. **Manipulación del DOM**
   Enunciado: Selecciona elementos con `querySelector` y `getElementById`. Cambia texto con `textContent` o `innerHTML`, modifica estilos con `style` y añade/elimina clases con `classList`.
   Pista: Asegúrate de que el script se carga después del DOM o usa `DOMContentLoaded`. Usa `classList.add/remove/toggle`.
   Criterio verificable: Al ejecutar en navegador, el DOM se modifica visualmente (texto, colores, clases) sin errores en consola.

## Nivel desafío

7. **Lista de tareas con eventos**
   Enunciado: Crea una lista de tareas funcional. Permite agregar tareas desde un input, marcar como completadas (toggle de clase), eliminar tareas individualmente. Usa `addEventListener`, `createElement`, `appendChild` o `append`.
   Pista: Usa delegación de eventos si es necesario. Guarda referencias a elementos creados dinámicamente.
   Criterio verificable: Se pueden agregar, marcar como completadas y eliminar tareas. Los cambios son visibles inmediatamente sin recargar la página.

8. **Formulario con validación en JavaScript**
   Enunciado: Crea un formulario con validación. Verifica campos obligatorios, formato de email con expresión regular básica, longitud mínima de contraseña. Muestra mensajes de error específicos debajo de cada campo. No envíes si hay errores.
   Pista: Usa `event.preventDefault()`. Muestra/oculta mensajes de error manipulando el DOM. Usa una expresión regular para validar email.
   Criterio verificable: Con datos inválidos se muestran errores específicos, con datos válidos no se muestran errores y el formulario no se envía (o se simula envío mostrando datos).
