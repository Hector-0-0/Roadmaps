# 06-redis

## 1. Qué es y para qué sirve
Redis (Remote Dictionary Server) es una base de datos en memoria (in-memory), clave-valor, de código abierto. Es extremadamente rápido y se usa comúnmente para caché, almacenamiento de sesiones, colas y contadores.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Mejora el rendimiento de APIs al cachear datos frecuentes. Se conecta con Node.js, PostgreSQL y la aplicación completa.

## 3. Conceptos clave
- **Clave-valor (key-value)**: estructura simple clave -> valor.
- **Estructuras de datos**: strings, hashes, lists, sets, sorted sets.
- **TTL (Time To Live)**: tiempo de expiración de una clave.
- **Caché**: almacenar resultado para evitar consultas repetidas.
- **Patrón cache-aside**: verificar caché, si no existe consultar BD y guardar en caché.
- **Sesiones**: almacenar sesiones de usuario.
- **Persistencia**: RDB (snapshot) y AOF (Append Only File).
- **Uso desde Node.js**: cliente como `ioredis` o `redis`.

## 4. Ejemplos de código comentados, correctos y ejecutables

### Ejemplo 1: Comandos básicos
```bash
# Conectar con redis-cli
redis-cli

# Operaciones básicas
SET usuario:1 "Ana"
GET usuario:1
EXPIRE usuario:1 60
TTL usuario:1
```

### Ejemplo 2: Cache-aside con Node.js (conceptual, correcto)
```javascript
const redis = require('redis');
const client = redis.createClient();

async function obtenerUsuario(id) {
  const clave = `usuario:${id}`;
  // Intentar obtener de caché
  const cacheado = await client.get(clave);
  if (cacheado) {
    return JSON.parse(cacheado);
  }
  // Si no existe, consultar BD (simulado)
  const usuario = { id, nombre: 'Ana' };
  // Guardar en caché por 60 segundos
  await client.setEx(clave, 60, JSON.stringify(usuario));
  return usuario;
}
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Usar Redis como única base de datos sin entender persistencia.
- No usar TTL en datos temporales.
- Almacenar objetos grandes innecesariamente.
- Olvidar invalidar caché al actualizar datos.

Buenas prácticas:
- Usar para datos frecuentes o costosos de calcular.
- Definir TTL adecuado.
- Invalidar caché en escrituras (update/delete).
- Entender RDB/AOF según necesidad.
- Proteger instancia Redis en producción.

## 6. Autoevaluación

1. ¿Qué es Redis?
2. ¿Diferencia entre Redis y PostgreSQL?
3. ¿Qué es TTL?
4. ¿En qué consiste el patrón cache-aside?
5. ¿Diferencia entre RDB y AOF?

Respuestas esperadas (orientativas):
1. Base de datos en memoria clave-valor.
2. Redis en memoria (rápido), PostgreSQL relacional en disco.
3. Tiempo de vida/expiración de una clave.
4. Verificar caché, si falla consultar BD y guardar en caché.
5. RDB hace snapshots periódicos, AOF guarda cada operación.
