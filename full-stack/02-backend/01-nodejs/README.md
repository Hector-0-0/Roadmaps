# 01-nodejs

## Nota sobre el lenguaje
Se puede elegir cualquier lenguaje de backend. Se recomienda Node.js por la familiaridad con JavaScript y porque es más fácil de aprender partiendo desde el frontend.

## 1. Qué es y para qué sirve
Node.js es un entorno de ejecución (runtime) de JavaScript basado en el motor V8 de Chrome. Permite ejecutar JavaScript en el servidor para crear APIs, servidores web, CLI y más.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Permite usar JavaScript en backend, compartir lógica, y crear APIs que consumirá el frontend. Se conecta con npm, APIs RESTful y bases de datos.

## 3. Conceptos clave

### Módulos (CommonJS/ESM)
```javascript
// CommonJS
const fs = require('fs');

// ES Modules (ESM)
import fs from 'fs';
```

### Servidor básico con http
```javascript
const http = require('http');
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hola desde Node.js');
});
server.listen(3000, () => console.log('Servidor en puerto 3000'));
```

### npm y package.json
Ya visto en frontend, aplica igual.

### fs, path, eventos básicos
Módulos nativos para trabajar con archivos, rutas y eventos.

## 4. Ejemplos de código comentados, correctos y ejecutables

```javascript
// server.js
const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h1>Inicio</h1>');
  } else {
    res.writeHead(404, { 'Content-Type': 'text/html' });
    res.end('<h1>404 No encontrado</h1>');
  }
});

server.listen(3000, () => {
  console.log('Servidor escuchando en http://localhost:3000');
});
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- No manejar rutas.
- Bloquear event loop con operaciones síncronas pesadas.
- Olvidar cerrar servidor en desarrollo.
- Mezclar CommonJS/ESM sin configurar.

Buenas prácticas:
- Usar nodemon (herramienta para reiniciar) en desarrollo.
- Organizar por rutas/controladores.
- Manejar errores.
- Usar variables de entorno (environment variables).

## 6. Autoevaluación

1. ¿Qué es Node.js?
2. ¿Diferencia entre frontend JS y Node.js?
3. ¿Qué módulo nativo usarías para crear servidor HTTP?
4. ¿Qué es el event loop (bucle de eventos)?
5. ¿Por qué usar Node.js en este roadmap?

Respuestas orientativas:
1. Entorno de ejecución JS en servidor.
2. Acceso a APIs del navegador vs sistema/servidor.
3. http.
4. Mecanismo que maneja operaciones asíncronas.
5. Familiaridad con JS y facilidad de aprendizaje.
