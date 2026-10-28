# Práctica - 02-backend/03-apis-restful

## Nivel básico

1. **Configurar servidor Express básico**
   Enunciado: Instala `express` con npm. Crea un servidor que escuche en el puerto 3000 y responda con JSON `{"mensaje": "API funcionando"}` en la ruta `GET /`.
   Pista: Usa `express()`, `app.use(express.json())` si planeas recibir JSON, y `app.listen(3000)`. Ejecuta con `node app.js` y prueba con curl o navegador.
   Criterio verificable: Al hacer `curl -i http://localhost:3000/` se recibe código de estado 200 y el JSON exacto indicado.

2. **Rutas con métodos HTTP básicos**
   Enunciado: Crea rutas `GET /usuarios`, `POST /usuarios` que respondan con JSON. Para GET devuelve un array vacío o con datos de prueba, para POST recibe datos y responde con ellos.
   Pista: Usa `app.get()` y `app.post()`. Asegúrate de parsear JSON con `express.json()`. Prueba ambos métodos con curl.
   Criterio verificable: GET /usuarios retorna código 200 con JSON, POST /usuarios retorna código 201 o 200 con el cuerpo recibido.

3. **Códigos de estado HTTP correctos**
   Enunciado: Implementa respuestas con códigos correctos: 200 para éxito, 201 al crear, 400 para datos inválidos, 404 para recurso no encontrado.
   Pista: Usa `res.status(codigo).json({...})`. Valida que POST sin datos obligatorios retorne 400 con mensaje de error claro.
   Criterio verificable: Cada caso retorna el código de estado HTTP correcto al probarlo con curl -i.

## Nivel intermedio

4. **CRUD completo en memoria**
   Enunciado: Implementa CRUD completo para recurso `productos`: GET /productos (listar), GET /productos/:id (obtener uno), POST /productos (crear), PUT /productos/:id (actualizar), DELETE /productos/:id (eliminar). Usa un array en memoria con IDs únicos.
   Pista: Usa `req.params.id` para obtener el ID. Genera IDs con `Date.now()` o contador. Retorna 404 si el recurso no existe.
   Criterio verificable: Los 5 métodos funcionan correctamente, retornando códigos apropiados (200, 201, 404) al probar con curl.

5. **Validación de datos**
   Enunciado: Añade validación en POST y PUT. Verifica que campos obligatorios existan, tipos correctos y valores válidos. Retorna 400 con array de errores si hay fallos.
   Pista: Valida antes de guardar. Estructura errores como `{"errores": ["campo requerido"]}` para facilitar verificación.
   Criterio verificable: POST/PUT con datos inválidos retorna 400 con errores descriptivos, con datos válidos procede correctamente.

6. **Organización modular de rutas**
   Enunciado: Separa el código en carpetas `routes/`, `controllers/`. Mueve las rutas de productos a su propio archivo usando `express.Router()`. Monta el router en `app.js`.
   Pista: Usa `router.get()`, `router.post()` etc. Exporta el router con `module.exports = router` e impórtalo con `app.use('/productos', router)`.
   Criterio verificable: La API funciona igual que antes, el código está dividido en rutas y controladores sin lógica mezclada en app.js.

## Nivel desafío

7. **Filtros, búsqueda y paginación**
   Enunciado: Añade query params a GET /productos: `?categoria=...` para filtrar, `?q=...` para búsqueda por nombre, `?page=1&limit=10` para paginación. Retorna metadatos de paginación.
   Pista: Lee `req.query`. Filtra el array con `filter()`. Calcula `skip` y `limit` para paginar. Retorna `{"datos": [...], "pagina": 1, "total": 5}`.
   Criterio verificable: Los filtros funcionan correctamente, paginación devuelve el número correcto de elementos y metadatos adecuados.

8. **Manejo de errores centralizado**
   Enunciado: Crea un middleware de manejo de errores centralizado. Usa `next(error)` en controladores, maneja errores con middleware con 4 parámetros. Añade validación con mensajes claros y códigos apropiados.
   Pista: Middleware de errores debe tener firma `(err, req, res, next)`. Colócalo al final de todas las rutas en app.js.
   Criterio verificable: Errores lanzados con `next()` son capturados por el middleware centralizado y retornan formato JSON consistente con código de estado correcto.
