# Checkpoint - Fundamentos matemáticos

## Objetivo

Consolidar conocimientos de cálculo, álgebra lineal, estadística, probabilidad y matemática discreta mediante proyectos integradores aplicados a Machine Learning.

## Conocimientos que consolida

- Cálculo: derivadas, gradiente, regla de la cadena
- Álgebra lineal: vectores, matrices, autovalores, SVD
- Estadística: descriptiva, inferencial, pruebas básicas
- Probabilidad: distribuciones, Bayes, variables aleatorias
- Matemática discreta: lógica y conjuntos aplicados

## Proyectos

### Proyecto 1: Gradiente descendente desde cero (Dificultad: Básico)

**Descripción:** Implementar descenso por gradiente para ajustar una recta $y = wx + b$ minimizando error cuadrático medio.

**Requisitos funcionales:**
- Generar datos sintéticos con ruido
- Inicializar parámetros w, b
- Calcular gradientes y actualizar parámetros
- Graficar pérdida por iteración
- Comparar con solución analítica o sklearn

**Habilidades que practica:** Cálculo, optimización, NumPy, Matplotlib

**Criterios de aceptación:**
- Código ejecutable sin errores
- Pérdida disminuye con iteraciones
- Parámetros convergen a valores razonables
- Gráficas correctas

**Mejoras opcionales:**
- Añadir learning rate adaptativo
- Implementar mini-batch gradient descent
- Añadir regularización

### Proyecto 2: Análisis estadístico de dataset Iris (Dificultad: Intermedio)

**Descripción:** Realizar análisis estadístico completo del dataset Iris usando conceptos de estadística descriptiva e inferencial.

**Requisitos funcionales:**
- Estadísticos descriptivos por clase
- Matriz de correlación
- Pruebas de hipótesis básicas
- Visualizaciones con Seaborn
- Interpretación de resultados

**Habilidades que practica:** Estadística, pandas, Seaborn, inferencia

**Criterios de aceptación:**
- Cálculos correctos verificados
- Visualizaciones con etiquetas
- Interpretación estadística coherente
- Código reproducible

**Mejoras opcionales:**
- Pruebas ANOVA
- Intervalos de confianza
- Análisis por pares

### Proyecto 3: PCA desde cero con álgebra lineal (Dificultad: Desafío)

**Descripción:** Implementar Análisis de Componentes Principales desde cero usando autovalores, autovectores y proyección.

**Requisitos funcionales:**
- Estandarizar datos
- Calcular matriz de covarianza
- Obtener autovalores y autovectores
- Seleccionar componentes principales
- Proyectar datos a 2D y visualizar
- Comparar con sklearn.decomposition.PCA

**Habilidades que practica:** Álgebra lineal, SVD/autovalores, reducción dimensional, visualización

**Criterios de aceptación:**
- Implementación correcta con NumPy puro
- Varianza explicada calculada correctamente
- Proyección visualizable
- Coincide razonablemente con sklearn
- Código bien documentado

**Mejoras opcionales:**
- Implementar con SVD
- Calcular varianza acumulada
- Aplicar a dataset Wine
