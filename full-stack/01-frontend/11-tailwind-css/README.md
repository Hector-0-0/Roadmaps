# 11-tailwind-css

## 1. Qué es y para qué sirve
Tailwind CSS es un framework CSS utility-first (basado en clases utilitarias). En lugar de escribir CSS personalizado para cada componente, se aplican clases utilitarias directamente en el HTML para estilizar rápidamente.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Permite prototipar y construir interfaces con rapidez manteniendo consistencia. Se conecta con CSS (es importante entenderlo primero) y con frameworks como React. Según el roadmap original se revisa tras Backend.

## 3. Conceptos clave
- **Utility-first**: usar clases pequeñas y reutilizables (p-4, text-center).
- **Responsive design**: prefijos como sm:, md:, lg:, xl:, 2xl:.
- **Estados (states)**: hover:, focus:, active:, disabled:.
- **Dark mode**: soporte con dark: (según configuración).
- **Flexbox/Grid con utilidades**: flex, grid, gap, justify-content.
- **Espaciado y tipografía**: padding/margin, text, font.
- **Componentes**: extraer componentes repetidos en lugar de duplicar clases.
- **Configuración**: tailwind.config.js para personalizar tema.

## 4. Ejemplos de código comentados, correctos y ejecutables

### Ejemplo 1: Tarjeta con utilidades
```html
<div class="max-w-sm rounded overflow-hidden shadow-lg p-6 bg-white">
  <h2 class="font-bold text-xl mb-2">Título</h2>
  <p class="text-gray-700 text-base">
    Texto de ejemplo usando Tailwind CSS.
  </p>
  <button class="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
    Botón
  </button>
</div>
```

### Ejemplo 2: Responsive y estados
```html
<div class="p-4 md:p-8 bg-gray-100">
  <h1 class="text-2xl md:text-4xl font-bold hover:text-blue-600">Responsive</h1>
  <button class="mt-2 px-4 py-2 bg-green-500 text-white focus:outline-none focus:ring-2 focus:ring-green-300">
    Con foco
  </button>
</div>
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Usar Tailwind sin entender CSS base.
- Duplicar largas cadenas de clases sin extraer componentes.
- Abusar de estilos inline cuando conviene componente.
- No aprovechar responsive breakpoints.
- Sobreescribir demasiado con CSS propio sin razón.

Buenas prácticas:
- Aprender CSS primero.
- Extraer componentes para clases repetidas.
- Usar breakpoints mobile-first.
- Aprovechar @apply solo cuando justificado.
- Personalizar tema en config si hay diseño consistente.
- Mantener legible agrupando clases.

## 6. Autoevaluación

1. ¿Qué significa utility-first?
2. ¿Cómo hacer diseño responsive con Tailwind?
3. ¿Cómo aplicar estilos en hover y focus?
4. ¿Cuándo conviene extraer un componente en lugar de repetir clases?
5. ¿Es necesario saber CSS para usar Tailwind?

Respuestas esperadas (orientativas):
1. Usar clases pequeñas que aplican una propiedad CSS.
2. Con prefijos de breakpoint (sm:, md:, lg:, etc.) siguiendo mobile-first.
3. Con prefijos hover:, focus:, active:.
4. Cuando el mismo patrón de clases se repite en varios lugares.
5. Sí, es recomendable entender CSS base para aprovecharlo mejor.
