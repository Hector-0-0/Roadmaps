# Checkpoint 08 - App completa

## Objetivo del checkpoint
Integrar Node.js, APIs RESTful, PostgreSQL, Redis, autenticación JWT en una app completa.

## Conocimientos que consolida
- [01-nodejs](../01-nodejs/README.md)
- [03-apis-restful](../03-apis-restful/README.md)
- [05-postgresql](../05-postgresql/README.md)
- [06-redis](../06-redis/README.md)
- [07-autenticacion-jwt](../07-autenticacion-jwt/README.md)

## 3 ideas de proyecto de dificultad creciente

### 1. Proyecto 1: API de blog con autenticación (Dificultad: intermedia)
**Descripción:** Blog con usuarios, posts, auth JWT.

**Requisitos funcionales:**
- Registro/login.
- CRUD posts (solo autor o admin).
- Posts públicos.
- Validación.

**Habilidades que practica:**
- Auth, relaciones, autorización.

**Criterios de aceptación:**
- Auth funcional.
- Autorización por propietario.
- Datos persistidos.

**Mejoras opcionales:**
- Comentarios.
- Categorías.

### 2. Proyecto 2: API de e-commerce básica (Dificultad: intermedia-avanzada)
**Descripción:** Productos, carrito, órdenes con auth.

**Requisitos funcionales:**
- Productos CRUD.
- Carrito por usuario.
- Crear orden.
- Protección de rutas.

**Habilidades que practica:**
- Relaciones complejas, lógica negocio.

**Criterios de aceptación:**
- Carrito funcional.
- Orden se crea correctamente.
- Validación stock básica.

**Mejoras opcionales:**
- Roles (admin/user).
- Historial órdenes.

### 3. Proyecto 3: App completa con caché (Dificultad: avanzada)
**Descripción:** App con PostgreSQL + Redis para caché.

**Requisitos funcionales:**
- Auth JWT.
- CRUD principal.
- Caché con Redis en lecturas frecuentes.
- Invalidación de caché.
- Estructura modular.

**Habilidades que practica:**
- Integración completa, rendimiento.

**Criterios de aceptación:**
- Caché funciona (verificar).
- Invalidación correcta.
- Código organizado.

**Mejoras opcionales:**
- Rate limiting con Redis.
- Logs básicos.
