# Práctica - 02-css

## Nivel básico

1. **Selectores de elemento, clase e ID**
   Enunciado: Crea un archivo HTML con tres elementos distintos. Aplica estilos usando selector de elemento, selector de clase y selector de ID en un archivo CSS externo enlazado con `link`.
   Pista: Usa nombres de clases descriptivos y un ID único. Recuerda que los ID deben usarse con moderación y las clases son reutilizables.
   Criterio verificable: Los tres elementos muestran estilos diferentes aplicados desde CSS externo, visible al abrir el HTML en el navegador.

2. **Box Model práctico**
   Enunciado: Crea una caja con `width`, `padding`, `border` y `margin`. Experimenta con `box-sizing: content-box` y `box-sizing: border-box` y documenta la diferencia observada.
   Pista: Usa las herramientas de desarrollador del navegador para inspeccionar el Box Model y ver cómo se calcula el tamaño total.
   Criterio verificable: Se visualiza correctamente el padding, border y margin, y puedes explicar la diferencia entre ambos valores de box-sizing.

3. **Colores, tipografía y unidades**
   Enunciado: Aplica colores con valores hexadecimales o RGB, usa al menos dos familias tipográficas y combina unidades absolutas (`px`) y relativas (`em`, `rem`).
   Pista: Usa `font-family` con fuentes web seguras o Google Fonts. Prueba cómo se comportan `em` y `rem` al cambiar el tamaño base.
   Criterio verificable: Se observan diferencias claras entre las unidades usadas y los estilos tipográficos aplicados correctamente.

## Nivel intermedio

4. **Flexbox: alineación y distribución**
   Enunciado: Crea un contenedor con `display: flex` que contenga tres elementos. Usa `justify-content` para distribuirlos horizontalmente y `align-items` para centrarlos verticalmente. Haz que sean responsivos con `flex-wrap`.
   Pista: Prueba diferentes valores de `justify-content` (space-between, center, space-around). Usa `gap` para espaciado entre elementos.
   Criterio verificable: Los elementos se alinean correctamente con Flexbox, se centran vertical y horizontalmente y se ajustan al cambiar el tamaño de ventana.

5. **Posicionamiento y display**
   Enunciado: Crea un elemento con `position: relative` que contenga un elemento hijo con `position: absolute`. Usa también ejemplos de `display: block`, `inline` e `inline-block`.
   Pista: Recuerda que un elemento con position absolute se posiciona respecto al ancestro posicionado más cercano.
   Criterio verificable: El elemento absoluto se posiciona correctamente respecto a su contenedor relativo, y se observan las diferencias entre los valores de display.

6. **Media queries responsive**
   Enunciado: Crea un layout de dos columnas en pantallas grandes (mayores a 768px) que pase a una sola columna en pantallas pequeñas (menores o iguales a 768px) usando `@media`.
   Pista: Usa `flex-direction: column` o `grid-template-columns: 1fr` en el media query. Aplica enfoque mobile-first si lo prefieres.
   Criterio verificable: Al redimensionar la ventana, el layout cambia correctamente entre dos columnas y una columna en el breakpoint definido.

## Nivel desafío

7. **Tarjeta completa con Flexbox**
   Enunciado: Diseña una tarjeta con imagen, título, descripción, etiquetas y botón. Usa Flexbox para organizar el contenido, aplica sombras, bordes redondeados y espaciado consistente.
   Pista: Usa `display: flex; flex-direction: column` para el contenedor de tarjeta. Alinea el botón al final con `margin-top: auto` si es necesario.
   Criterio verificable: La tarjeta tiene diseño profesional, buen espaciado, es responsive y todos los elementos están correctamente alineados con Flexbox.

8. **Página responsive completa**
   Enunciado: Crea una página con header, navegación, contenido principal con sidebar, y footer usando Flexbox o CSS Grid. Hazla completamente responsive con al menos dos breakpoints usando media queries.
   Pista: En móvil, apila los elementos verticalmente. En tablet/escritorio, usa layout horizontal. Usa unidades relativas para mayor flexibilidad.
   Criterio verificable: La página se adapta correctamente en móvil, tablet y escritorio, mantiene legibilidad y usa media queries efectivamente.
