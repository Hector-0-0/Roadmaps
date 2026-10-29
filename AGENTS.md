# AGENTES.md - Convenciones del repositorio Roadmaps

## Identidad Git y reglas de commit/push
- Nombre: Héctor David Flores Sánchez
- Correo: floressanchezhectordavid@gmail.com
- Todos los commits y pushes deben salir a este nombre.
- No agregar trailers `Co-authored-by` ni mencionar IA, OpenCode, Claude o herramientas similares en los mensajes de commit.
- Nunca usar `force push`. Si el push falla por autenticación, detenerse y avisar, sin cambiar credenciales.

## Estructura general
- Cada roadmap es una carpeta en la raíz, nombre en kebab-case y sin tildes.
- Raíz:
  - `README.md`: índice con tabla de roadmaps (nombre, descripción corta, estado) y cómo usar el repo.
  - `AGENTS.md`: este archivo.
- Dentro de cada roadmap:
  - `README.md`: objetivo, público objetivo, mapa de etapas con enlaces, cómo estudiar, roadmaps relacionados y atribución.
  - `PROGRESO.md`: checklist con casillas por tema y checkpoint.
  - Carpetas de etapa numeradas (ej. `01-frontend`, `02-backend`, `03-devops`), cada una con su `README.md`.
  - Dentro de cada etapa, carpetas numeradas por tema o checkpoint en orden de aprendizaje. Numeración continua dentro de la etapa.

## Plantilla de carpeta de tema (ej. `01-html/`)
- `README.md`: teoría completa según reglas.
- `practica.md`: ejercicios progresivos.
- `recursos.md`: recursos sin enlaces inventados.

Si un tema agrupa varios sub-temas, crear subcarpeta por sub-tema con la misma plantilla.

## Plantilla de carpeta de checkpoint
- `README.md`: objetivo, conocimientos que consolida (enlazando a temas previos), 3 ideas de proyecto de dificultad creciente (descripción, requisitos funcionales, habilidades que practica, criterios de aceptación, mejoras opcionales).
- `proyectos/`: carpeta con `.gitkeep`.

## Reglas de contenido
- Idioma: español. Términos técnicos en inglés la primera vez que aparezcan, acompañados de su equivalente en español.
- Sin placeholders, TODO, lorem ipsum o secciones vacías. Todo contenido debe ser real y útil.
- Recursos: si no se puede verificar una URL, indicar nombre del sitio y sección a buscar marcado como `(verificar enlace)`.
- Atribución obligatoria: en `README.md` de cada roadmap indicar que está basado en el roadmap correspondiente de [roadmap.sh](https://roadmap.sh) y que el contenido educativo es propio. No copiar ni commitear PDFs originales.

## Estilo de escritura
- No usar guiones largos (—) ni "--" como inciso. Usar comas o reestructurar la oración.

## Agregar un roadmap nuevo
1. Crear carpeta en raíz con nombre en kebab-case sin tildes.
2. Actualizar README índice con nueva fila en tabla.
3. Seguir las mismas plantillas de tema y checkpoint.
4. Mantener atribución a roadmap.sh correspondiente.

## Verificación

Antes de dar por terminada cualquier tarea hay que ejecutar `python3 scripts/verificar.py` (y con `--urls` cuando haya internet) y dejar 0 errores. El formato obligatorio de cada ejercicio de practica.md es:

N. **Título**
   Enunciado: pasos concretos y accionables.
   Pista: al menos una oración útil de 6 o más palabras.
   Criterio verificable: algo observable y comprobable.
