# Práctica - 11-tailwind-css (opcional)

## Nivel básico

1. **Configurar Tailwind con Vite**
   Enunciado: Crea un proyecto con Vite (o usa uno existente), instala Tailwind CSS siguiendo la guía oficial para Vite e importa los estilos en `main.jsx` o `index.css`. Verifica que las clases de Tailwind funcionan.
   Pista: Sigue los pasos exactos de la documentación para Vite. Asegúrate de importar el archivo CSS que contiene las directivas de Tailwind en el punto de entrada.
   Criterio verificable: Al aplicar una clase como `bg-blue-500 text-white` a un elemento, se aplican los estilos correctamente en el navegador.

2. **Maquetar una tarjeta**
   Enunciado: Usando solo clases utilitarias de Tailwind, crea una tarjeta con imagen, título, descripción y un botón. Usa padding, bordes redondeados, sombra y espaciado.
   Pista: Combina clases como `rounded`, `shadow`, `p-4`, `mt-2`, `bg-white`. Usa `flex` o `block` según la estructura.
   Criterio verificable: La tarjeta se ve correctamente con todos los elementos alineados, con espaciado y estilos aplicados únicamente con clases de Tailwind.

3. **Tipografía y colores**
   Enunciado: Crea una sección con un título, subtítulo y párrafo. Aplica diferentes tamaños de fuente, pesos, colores de texto y colores de fondo usando utilidades de Tailwind.
   Pista: Usa `text-2xl`, `font-bold`, `text-gray-700`, `bg-gray-100`. Prueba al menos tres combinaciones distintas.
   Criterio verificable: Se observan diferencias visuales claras entre título, subtítulo y párrafo usando únicamente clases utilitarias.

## Nivel intermedio

4. **Barra de navegación responsive**
   Enunciado: Crea una barra de navegación con logo y enlaces. En pantallas pequeñas debe mostrarse en columna o con menú simplificado, y en pantallas medianas o mayores debe mostrarse en fila horizontal usando breakpoints de Tailwind.
   Pista: Usa prefijos responsive como `md:flex`, `md:flex-row`, `hidden md:block`. Piensa mobile-first: define estilos para móvil y añade breakpoints para pantallas mayores.
   Criterio verificable: Al redimensionar la ventana, la navegación cambia de layout entre móvil y escritorio usando breakpoints de Tailwind.

5. **Estados hover, focus y active**
   Enunciado: Crea un botón con estilos para estado normal, `hover`, `focus` y `active`. Asegúrate de que el foco sea visible para accesibilidad.
   Pista: Usa prefijos `hover:`, `focus:`, `active:`. Añade `focus:outline-none focus:ring-2` para un foco visible.
   Criterio verificable: Al pasar el ratón, enfocar con tab o hacer clic, el botón muestra estilos distintos para cada estado.

6. **Formulario con estilos utilitarios**
   Enunciado: Maqueta un formulario con campos de nombre, correo y mensaje. Aplica estilos a inputs, labels, botón y añade validación visual con estados focus.
   Pista: Usa `border`, `rounded`, `px-3`, `py-2`, `focus:border-blue-500`. Agrupa con `flex flex-col` para cada campo.
   Criterio verificable: El formulario tiene buen espaciado, es legible y los inputs muestran estilo al enfocar con teclado o ratón.

## Nivel desafío

7. **Dark mode**
   Enunciado: Configura dark mode en Tailwind y crea una tarjeta que cambie de estilos entre modo claro y oscuro. Usa el prefijo `dark:` para aplicar estilos en modo oscuro.
   Pista: Revisa la configuración de dark mode en Tailwind (class strategy es común). Añade la clase `dark` al elemento html/body para probar.
   Criterio verificable: Al alternar la clase `dark` en el html, la tarjeta cambia colores correctamente usando únicamente clases con prefijo `dark:`.

8. **Componente reutilizable con extracción**
   Enunciado: Identifica clases repetidas en una tarjeta o botón y extráelas creando un componente reutilizable en React (o una clase con `@apply` justificado). Usa el componente al menos dos veces con props para personalizar texto.
   Pista: Si usas React, crea `Button.jsx` que acepte `children` y `className`. Solo usa `@apply` si realmente hay muchas utilidades repetidas y justifica su uso.
   Criterio verificable: El componente reutilizable funciona en dos instancias con contenido distinto, hay menos duplicación de clases largas y la UI se mantiene consistente.
