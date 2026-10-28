# 05-postgresql

## 1. Qué es y para qué sirve
PostgreSQL (sistema de gestión de bases de datos relacionales, RDBMS) es una base de datos relacional open source (código abierto), potente y confiable. Sirve para almacenar datos estructurados con integridad.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Necesario para persistir datos en aplicaciones reales. Se conecta con APIs, autenticación y aplicación completa.

## 3. Conceptos clave

### SQL (Structured Query Language, lenguaje de consulta estructurado)
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO users (name, email) VALUES ('Ana', 'ana@example.com');
SELECT * FROM users;
UPDATE users SET name = 'Ana Maria' WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

### Conceptos
- Tablas, columnas, filas
- Primary Key (clave primaria)
- Foreign Key (clave foránea)
- Relaciones (1:1, 1:N, N:M)
- Normalización básica
- JOIN (uniones)

## 4. Ejemplos
```sql
-- Relación
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  title VARCHAR(200) NOT NULL
);

SELECT users.name, posts.title
FROM users
JOIN posts ON users.id = posts.user_id;
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- No usar claves primarias.
- Guardar datos redundantes.
- No usar constraints (restricciones).
- SQL injection (inyección SQL) sin parametrizar.

Buenas prácticas:
- Usar PRIMARY KEY/FOREIGN KEY.
- Normalizar cuando convenga.
- Usar consultas parametrizadas.
- Hacer respaldos conceptualmente.
- Nombrar tablas/columnas claros.

## 6. Autoevaluación

1. ¿Qué es PostgreSQL?
2. ¿Diferencia entre SQL y NoSQL?
3. ¿Qué es una clave foránea?
4. ¿Para qué sirve JOIN?
5. ¿Qué es normalización?

Respuestas orientativas:
1. Base de datos relacional open source.
2. SQL relacional vs NoSQL no relacional.
3. Relaciona tablas con clave primaria otra tabla.
4. Combinar datos de tablas relacionadas.
5. Reducir redundancia de datos.
