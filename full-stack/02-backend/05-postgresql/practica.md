# Práctica - 02-backend/05-postgresql

## Nivel básico

1. **Conectar y crear base de datos**
   Enunciado: Conecta a PostgreSQL con `psql` o una herramienta gráfica. Crea una base de datos `practica_db` y conéctate a ella. Verifica las bases de datos existentes con `\l`.
   Pista: Usa `CREATE DATABASE practica_db;` y `\c practica_db`. En psql los comandos internos empiezan con backslash.
   Criterio verificable: La base de datos existe, la conexión es exitosa y se muestra en el listado con `\l`.

2. **Crear tabla con constraints**
   Enunciado: Crea una tabla `usuarios` con campos `id` (SERIAL PRIMARY KEY), `nombre` (VARCHAR(100) NOT NULL), `email` (VARCHAR(100) UNIQUE NOT NULL), `fecha_registro` (TIMESTAMP DEFAULT NOW()).
   Pista: Usa `CREATE TABLE` con los constraints indicados. Verifica la estructura con `\d usuarios`.
   Criterio verificable: La tabla se crea correctamente, muestra estructura con `\d usuarios` y aplica constraints al insertar datos.

3. **CRUD básico con SQL**
   Enunciado: Inserta al menos 3 usuarios con `INSERT`. Consulta todos con `SELECT * FROM usuarios`. Actualiza un usuario con `UPDATE ... WHERE`. Elimina un usuario con `DELETE ... WHERE`.
   Pista: Siempre usa `WHERE` en UPDATE y DELETE para evitar afectar todos los registros. Verifica con SELECT después de cada operación.
   Criterio verificable: Cada operación CRUD funciona correctamente, verificable con consultas SELECT mostrando los cambios.

## Nivel intermedio

4. **Relaciones con claves foráneas**
   Enunciado: Crea tabla `posts` con `id` SERIAL PRIMARY KEY, `usuario_id` INTEGER REFERENCES usuarios(id) ON DELETE CASCADE, `titulo` VARCHAR(200) NOT NULL, `contenido` TEXT. Inserta posts relacionados a usuarios existentes.
   Pista: La clave foránea debe apuntar a una clave primaria existente. ON DELETE CASCADE elimina posts al borrar usuario.
   Criterio verificable: La relación se crea correctamente, se pueden insertar posts con usuario_id válido y falla con usuario_id inexistente.

5. **Consultas con JOIN**
   Enunciado: Usa `INNER JOIN` para obtener usuarios con sus posts. Usa `LEFT JOIN` para obtener todos los usuarios aunque no tengan posts. Muestra nombre del usuario y título del post.
   Pista: Especifica las tablas con alias. Usa `ON usuarios.id = posts.usuario_id`. Ordena resultados con `ORDER BY`.
   Criterio verificable: Ambas consultas retornan resultados correctos mostrando la relación entre tablas con JOIN apropiado.

6. **Filtros, ordenamiento y agregación**
   Enunciado: Usa `WHERE`, `ORDER BY`, `LIMIT`. Usa funciones de agregación `COUNT()`, `GROUP BY` para contar posts por usuario. Usa `HAVING` para filtrar grupos.
   Pista: `GROUP BY` agrupa filas, `HAVING` filtra grupos (diferente de WHERE). Combina con JOIN para obtener nombres.
   Criterio verificable: Las consultas con filtros, agrupación y agregación retornan resultados correctos verificables con datos de prueba.

## Nivel desafío

7. **Transacciones**
   Enunciado: Usa `BEGIN`, `COMMIT` y `ROLLBACK`. Realiza dos operaciones relacionadas (ej. crear usuario y post) dentro de una transacción. Prueba rollback para revertir cambios.
   Pista: Si hay error en alguna operación, usa ROLLBACK para mantener integridad. COMMIT solo si todo es exitoso.
   Criterio verificable: Con COMMIT los cambios persisten, con ROLLBACK los cambios se revierten completamente.

8. **Consultas avanzadas con subconsultas**
   Enunciado: Crea un índice con `CREATE INDEX` sobre una columna usada en filtros o joins (ej. posts.usuario_id). Ejecuta una consulta con `EXPLAIN ANALYZE` antes y después de crear el índice y compara el plan de ejecución. También escribe una consulta con subconsulta usando `EXISTS` o `IN` para encontrar usuarios que tengan más de un post.
   Pista: Una subconsulta puede ir en WHERE. `EXISTS` verifica existencia. Practica con los datos creados.
   Criterio verificable: La subconsulta retorna correctamente los usuarios que cumplen la condición, con resultados verificables.
