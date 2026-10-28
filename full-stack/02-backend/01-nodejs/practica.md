# Práctica - 01-nodejs

## Nivel básico

1. **Servidor HTTP con http nativo**
   Enunciado: Crea un servidor usando el módulo `http`. Debe escuchar en el puerto 3000 y responder con texto plano "Hola desde Node.js" en la ruta `/`.
   Pista: Usa `http.createServer`, configura `res.writeHead` con código 200 y Content-Type correcto, finaliza con `res.end`. Ejecuta con `node server.js`.
   Criterio verificable: Al hacer `curl http://localhost:3000` se recibe el texto exacto con código de estado 200.

2. **Manejo de rutas básicas**
   Enunciado: Amplía el servidor para manejar rutas `/`, `/about` y devolver 404 para cualquier otra ruta. Cada ruta debe tener un mensaje distinto.
   Pista: Revisa `req.url` y usa condicionales. Para 404 usa código de estado 404 y un mensaje claro.
   Criterio verificable: `/` responde 200, `/about` responde 200 con contenido distinto, ruta inexistente responde 404.

3. **Servir HTML desde archivo**
   Enunciado: Crea un archivo `index.html` con contenido básico. Usa el módulo `fs` para leerlo y servirlo cuando se acceda a `/`.
   Pista: Usa `fs.readFile` con ruta correcta. Configura Content-Type como `text/html`. Maneja errores básicos.
   Criterio verificable: Al acceder a `/` se muestra el HTML correctamente en el navegador sin errores.

## Nivel intermedio

4. **Módulos propios**
   Enunciado: Separa la lógica en módulos propios. Crea `utils.js` con funciones y expórtalas con `module.exports`. Impórtalas en `server.js` con `require`.
   Pista: Organiza el código para reutilización. Usa rutas relativas al importar módulos propios.
   Criterio verificable: El servidor funciona usando funciones importadas desde módulo propio, código organizado en archivos separados.

5. **Parámetros y query strings**
   Enunciado: Crea una ruta que acepte query strings (ej. `/saludo?nombre=Ana`) y responda con un saludo personalizado.
   Pista: Usa el módulo `url` para parsear la URL y obtener `query`. También puedes usar `new URL(req.url, 'http://localhost:3000')`.
   Criterio verificable: Con diferentes valores en query string se obtienen saludos personalizados correctos.

6. **CLI con process.argv**
   Enunciado: Crea un CLI que tome argumentos desde `process.argv`. Debe soportar al menos dos comandos (ej. `add` y `list`) con argumentos.
   Pista: `process.argv` incluye node y archivo, empieza desde índice 2. Valida argumentos y muestra mensajes de error si faltan.
   Criterio verificable: Ejecutando `node cli.js add tarea1` y `node cli.js list` se obtienen comportamientos distintos y correctos.

## Nivel desafío

7. **API con datos en memoria**
   Enunciado: Crea una API REST con rutas GET/POST usando http nativo. Almacena datos en un array en memoria. GET debe listar, POST debe agregar con validación básica.
   Pista: Para POST necesitas leer el body con eventos `data` y `end`. Usa `JSON.parse` y valida campos obligatorios.
   Criterio verificable: GET `/items` retorna array con código 200, POST `/items` agrega elemento y retorna 201, POST con datos inválidos retorna 400.

8. **Servidor completo con rutas y manejo de errores**
   Enunciado: Crea un servidor con enrutamiento modular, manejo de errores, códigos de estado correctos y headers apropiados. Sirve archivos estáticos básicos.
   Pista: Organiza rutas por archivos/modulos. Usa try/catch donde aplique. Configura Content-Type correcto para cada tipo de archivo.
   Criterio verificable: Todas las rutas funcionan correctamente, errores devuelven códigos apropiados, archivos estáticos se sirven correctamente.
