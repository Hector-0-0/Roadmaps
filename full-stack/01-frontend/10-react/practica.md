# Práctica - 10-react (opcional)

## Nivel básico

1. **Crear app con Vite** 
   Enunciado: Crea un proyecto React con Vite usando `npm create vite@latest`, selecciona React y JavaScript. Instala dependencias con `npm install` y ejecuta el servidor con `npm run dev`. Verifica que se muestre la página por defecto en el navegador.
   Pista: Si el comando falla, asegúrate de tener Node.js actualizado. Usa la opción correcta al prompt y revisa la salida para confirmar que el servidor inició en el puerto indicado.
   Criterio verificable: Existe la carpeta del proyecto con `package.json`, `node_modules` instalado (o listo para instalar), y al ejecutar `npm run dev` la app carga correctamente mostrando contenido en el navegador.

2. **Componente funcional con props**
   Enunciado: Crea un componente `Saludo.jsx` que reciba una prop `nombre` y muestre un mensaje. Importa y usa ese componente dos veces desde `App.jsx` pasando nombres distintos.
   Pista: Usa PascalCase para el nombre del componente. Recuerda exportarlo con `export default` e importarlo correctamente desde App.
   Criterio verificable: Al renderizar la app se muestran dos saludos distintos con los nombres pasados como props, sin errores en consola.

3. **useState para contador**
   Enunciado: Crea un componente `Contador.jsx` con un botón que aumente un contador usando el hook `useState`. Muestra el valor actual del contador en pantalla.
   Pista: Importa `useState` desde `react`. No modifiques el estado directamente; usa siempre la función setter que devuelve useState.
   Criterio verificable: Al hacer clic en el botón, el número mostrado incrementa correctamente en cada clic.

## Nivel intermedio

4. **useEffect y llamada a API**
   Enunciado: Usando `useEffect`, haz una llamada a `https://jsonplaceholder.typicode.com/users` al montar el componente y muestra en una lista los nombres de los usuarios obtenidos.
   Pista: Usa `fetch` con `async/await` dentro de un `useEffect` con array de dependencias vacío para ejecutar solo al montar. Guarda los datos en estado con `useState`.
   Criterio verificable: Al cargar el componente se muestra una lista con al menos 3 nombres obtenidos de la API, sin errores de red en consola.

5. **Listas con key**
   Enunciado: Modifica el ejercicio anterior para renderizar la lista usando `.map()`, asignando un `key` único a cada elemento (usa el `id` del usuario). Añade un campo extra como el correo electrónico.
   Pista: Evita usar el índice del array como key si los elementos pueden reordenarse. Usa una propiedad única e inmutable como el id.
   Criterio verificable: La lista se renderiza correctamente con keys únicos (sin warning de keys en consola) y muestra nombre y correo de cada usuario.

6. **Eventos y formulario controlado**
   Enunciado: Crea un formulario controlado con un campo de texto para nombre y otro para correo. Guarda los valores en estado con `useState`. Al enviar el formulario, muestra los valores capturados debajo sin recargar la página.
   Pista: Usa `value` y `onChange` para controlar los inputs. Prevén el comportamiento por defecto con `event.preventDefault()` en el submit.
   Criterio verificable: Al escribir en los campos y enviar, se muestran los valores exactos capturados sin recarga de página.

## Nivel desafío

7. **Composición de componentes**
   Enunciado: Divide la lógica en componentes: crea `ListaUsuarios.jsx` que reciba un array por props y lo renderice, y `App.jsx` que gestione el estado y la llamada a API. Pásale los datos mediante props.
   Pista: Piensa en separación de responsabilidades: el componente padre gestiona datos y efectos, el hijo se encarga solo de presentar.
   Criterio verificable: La app funciona igual que el ejercicio 4, pero con componentes separados comunicándose por props, sin lógica de fetch dentro del componente de presentación.

8. **Buscar usuarios con filtro**
   Enunciado: Añade un campo de búsqueda al listado de usuarios. Filtra los usuarios por nombre en tiempo real conforme el usuario escribe, sin hacer nuevas llamadas a la API.
   Pista: Guarda la lista completa en un estado y el término de búsqueda en otro. Usa `.filter()` sobre la lista completa para mostrar los resultados filtrados.
   Criterio verificable: Al escribir en el buscador, la lista se filtra dinámicamente mostrando solo usuarios cuyo nombre coincida con el texto ingresado, manteniendo los datos originales en estado.
