# Checkpoint - Python y librerías esenciales

## Objetivo

Consolidar Python, NumPy, pandas, Matplotlib y Seaborn mediante proyectos integradores con datasets clásicos.

## Conocimientos que consolida

- Python: estructuras, funciones, POO
- NumPy: arrays, vectorización, álgebra lineal
- pandas: carga, limpieza, transformación, agregación
- Matplotlib: visualización básica y personalizada
- Seaborn: visualización estadística

## Proyectos

### Proyecto 1: Análisis exploratorio con pandas y NumPy (Dificultad: Básico)

**Descripción:** Realizar EDA completo del dataset Iris usando pandas y NumPy.

**Requisitos funcionales:**
- Cargar Iris con sklearn o crear DataFrame
- Estadísticas descriptivas con NumPy/pandas
- Detectar tipos y estructura
- Filtrado y agrupación por especie
- Resumen con hallazgos

**Habilidades que practica:** pandas, NumPy, análisis de datos

**Criterios de aceptación:**
- DataFrame correctamente cargado
- Estadísticas por especie calculadas
- Filtros y agrupaciones correctas
- Resumen documentado

**Mejoras opcionales:**
- Añadir métricas adicionales
- Exportar a CSV

### Proyecto 2: Visualización comparativa (Dificultad: Intermedio)

**Descripción:** Crear dashboard visual con Matplotlib y Seaborn para comparar clases del dataset Iris.

**Requisitos funcionales:**
- Scatter plots por pares
- Histogramas por característica
- Boxplots y violinplots por especie
- Matriz de correlación con heatmap
- Subplots organizados

**Habilidades que practica:** Matplotlib, Seaborn, visualización

**Criterios de aceptación:**
- Mínimo 6 visualizaciones
- Uso correcto de hue por especie
- Gráficas con títulos y etiquetas
- Heatmap con anotaciones

**Mejoras opcionales:**
- Guardar figuras
- Añadir pairplot
- Personalizar paletas

### Proyecto 3: Pipeline de preparación de datos (Dificultad: Desafío)

**Descripción:** Crear pipeline completo de preparación usando todas las librerías, listo para scikit-learn.

**Requisitos funcionales:**
- Carga con pandas
- Limpieza y validación
- Normalización con NumPy
- Análisis visual con Seaborn
- Separación X,y
- División train/test
- Código reproducible

**Habilidades que practica:** Integración de librerías, preparación, reproducibilidad

**Criterios de aceptación:**
- Datos limpios sin valores faltantes
- Features normalizados correctamente
- X,y separados correctamente
- División estratificada funcional
- Todo con código ejecutable

**Mejoras opcionales:**
- Crear clase Pipeline
- Añadir validación cruzada
- Documentar decisiones
