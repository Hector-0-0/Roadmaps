# 03-apis-restful

## 1. Qué es y para qué sirve
API (Application Programming Interface, interfaz de programación de aplicaciones) permite comunicación entre sistemas. REST (Representational State Transfer, transferencia de estado representacional) es un estilo arquitectónico para APIs web usando HTTP (HyperText Transfer Protocol).

## 2. Por qué importa dentro del roadmap y cómo se conecta
Permite separar frontend y backend, crear servicios reutilizables. Se conecta con Node.js, CRUD y autenticación.

## 3. Conceptos clave

### Métodos HTTP
- GET: obtener
- POST: crear
- PUT/PATCH: actualizar
- DELETE: eliminar

### Códigos de estado HTTP
- 200 OK, 201 Created
- 400 Bad Request, 401 Unauthorized, 404 Not Found
- 500 Internal Server Error

### Recursos y endpoints
```text
GET /users      -> listar
GET /users/:id  -> obtener uno
POST /users     -> crear
PUT /users/:id  -> actualizar
DELETE /users/:id -> eliminar
```

### JSON (JavaScript Object Notation)
Formato estándar para intercambio de datos.

## 4. Ejemplo con Express (introducción)
```javascript
const express = require('express');
const app = express();
app.use(express.json());

app.get('/users', (req, res) => {
  res.json([{ id: 1, name: 'Ana' }]);
});

app.listen(3000, () => console.log('API en 3000'));
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- No usar códigos correctos.
- Exponer datos sensibles.
- Rutas inconsistentes.
- No validar datos.

Buenas prácticas:
- Usar nombres de recursos en plural.
- Versionar API (/api/v1/).
- Validar entrada.
- Manejo centralizado de errores.

## 6. Autoevaluación

1. ¿Qué es una API RESTful?
2. ¿Diferencia entre PUT y PATCH?
3. ¿Cuándo usar 201 vs 200?
4. ¿Qué es JSON?
5. ¿Por qué usar verbos HTTP correctos?

Respuestas orientativas:
1. API siguiendo principios REST con HTTP.
2. PUT reemplaza completo, PATCH parcial.
3. 201 al crear recurso, 200 operación exitosa.
4. Formato ligero para intercambio de datos.
5. Semántica clara y estándar.
