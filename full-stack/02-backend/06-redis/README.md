# 06-redis

## 1. Qué es y para qué sirve
Redis (Remote Dictionary Server, servidor de diccionario remoto) es una base de datos en memoria (in-memory), clave-valor (key-value), usada para caché, sesiones y colas.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Mejora rendimiento cacheando datos frecuentes. Se conecta con APIs y aplicación completa.

## 3. Conceptos clave
- Clave-valor
- Tipos: strings, hashes, lists, sets
- TTL (Time To Live, tiempo de vida)
- Caché
- Persistencia básica

```bash
SET nombre "Ana"
GET nombre
EXPIRE nombre 60
```

## 4. Casos de uso
- Caché de consultas
- Almacenamiento de sesiones
- Rate limiting (límite de peticiones)
- Colas simples

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Usar Redis como única BD sin entender límites.
- No configurar TTL.
- Guardar datos grandes innecesarios.

Buenas prácticas:
- Usar para datos temporales/frecuentes.
- Definir TTL.
- Entender persistencia.
- Monitorear memoria.

## 6. Autoevaluación

1. ¿Qué es Redis?
2. ¿Diferencia con PostgreSQL?
3. ¿Qué es TTL?
4. ¿Casos de uso principales?
5. ¿Es persistente por defecto?

Respuestas orientativas:
1. BD en memoria clave-valor.
2. En memoria vs relacional en disco.
3. Tiempo de expiración de clave.
4. Caché, sesiones, colas.
5. Configurable; puede ser volátil.
