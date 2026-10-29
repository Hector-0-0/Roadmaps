# Práctica - 02-backend/06-redis

## Nivel básico

1. **Conectar a Redis y operaciones básicas**
   Enunciado: Instala Redis localmente o usa una instancia. Conéctate con `redis-cli`. Usa `SET`, `GET`, `DEL` para crear, leer y eliminar una clave. Verifica con `KEYS *` o `EXISTS`.
   Pista: Asegúrate de que Redis esté corriendo con `redis-cli ping` (debe responder PONG). Usa claves descriptivas como `usuario:1`.
   Criterio verificable: `SET nombre "Ana"` seguido de `GET nombre` retorna `"Ana"`, `DEL nombre` elimina la clave y `GET nombre` retorna nil.

2. **TTL y expiración**
   Enunciado: Crea una clave con `SETEX` o `SET` + `EXPIRE`. Usa `TTL` para ver tiempo restante. Usa `PERSIST` para quitar expiración. Observa comportamiento al expirar.
   Pista: TTL negativo significa clave expirada o no existe. Usa valores en segundos para pruebas rápidas.
   Criterio verificable: Clave con TTL muestra tiempo decreciente con `TTL`, tras expirar `GET` retorna nil, `PERSIST` quita expiración correctamente.

3. **Estructuras de datos: Hash y List**
   Enunciado: Usa `HSET`, `HGET`, `HGETALL` para guardar un objeto usuario en un hash. Usa `LPUSH`, `RPUSH`, `LRANGE` para manejar una lista de tareas.
   Pista: Los hashes son ideales para objetos. Las listas permiten colas simples con LPUSH/RPOP.
   Criterio verificable: Hash guarda múltiples campos accesibles individualmente y con HGETALL, lista permite agregar y recuperar elementos con LRANGE correcto.

## Nivel intermedio

4. **Patrón cache-aside con Node.js**
   Enunciado: Crea un script Node.js que use cliente Redis. Implementa patrón cache-aside: si existe en caché retorna datos cacheados, si no consulta función simulada, guarda en caché con TTL y retorna.
   Pista: Usa `redis` o `ioredis`. Guarda JSON con `JSON.stringify`. Recupera con `JSON.parse`. Usa `setEx` con TTL apropiado.
   Criterio verificable: Primera llamada consulta origen, segunda llamada usa caché (verificable con log), datos correctos en ambos casos.

5. **Invalidación de caché**
   Enunciado: Al actualizar o eliminar datos, invalida la clave de caché correspondiente con `DEL`. Prueba que tras invalidación se consulta origen nuevamente.
   Pista: Mantén convención de claves coherente (ej. `usuario:123`). Invalida en operaciones de escritura.
   Criterio verificable: Tras actualización, siguiente lectura obtiene datos actualizados (no cacheados), caché invalidado correctamente con DEL.

6. **Sesiones con Redis**
   Enunciado: Implementa almacenamiento de sesión simple: guardar sessionId con datos de usuario en Redis con TTL. Crear, leer y eliminar sesión.
   Pista: Usa hash o string con JSON. TTL corto para sesiones (ej. 1800 segundos). Genera sessionId único.
   Criterio verificable: Sesión se guarda con TTL, se recupera correctamente, se elimina con DEL y expira automáticamente.

## Nivel desafío

7. **Rate limiting básico**
   Enunciado: Implementa rate limiting simple con Redis usando INCR y EXPIRE. Limita a 5 peticiones por IP cada 60 segundos. Retorna error si excede límite.
   Pista: Usa clave `ratelimit:<ip>`. Si INCR devuelve 1, establece EXPIRE. Si supera límite, rechaza.
   Criterio verificable: Primeras 5 peticiones permitidas, sexta retorna código 429 o error, contador se resetea tras expirar TTL.

8. **Persistencia RDB/AOF (práctico)**
   Enunciado: Configura Redis para habilitar RDB (guardar snapshots) y/o AOF (appendonly) editando `redis.conf`. Genera datos, fuerza guardado con `BGSAVE`. Detén y reinicia Redis, verifica que los datos persistan tras reinicio.
   Pista: Revisa `redis.conf` para `save`, `appendonly yes`. Usa `BGSAVE` para guardar sin bloquear. Documenta configuración aplicada.
   Criterio verificable: Configuración de persistencia aplicada, snapshot generado (archivo dump.rdb), comportamiento documentado con evidencia.
