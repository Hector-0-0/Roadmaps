# Checkpoint - Fundamentos matemáticos

## Objetivo

Consolidar conocimientos de cálculo, álgebra lineal, estadística, probabilidad y matemática discreta mediante proyectos integradores aplicados a Machine Learning.

## Conocimientos que consolida

- Cálculo: derivadas, gradiente, regla de la cadena, optimización con descenso por gradiente.
- Álgebra lineal: vectores, matrices, autovalores, autovectores, SVD y reducción dimensional.
- Estadística: descriptiva, inferencial, intervalos de confianza y pruebas de hipótesis.
- Probabilidad: Bayes, distribuciones, simulación y razonamiento bajo incertidumbre.
- Matemática discreta: combinatoria, conjuntos, grafos y conteo.

## Proyectos

### Proyecto 1: Gradiente descendente desde cero (Dificultad: Básico)

**Descripción:** Implementar descenso por gradiente para ajustar una recta $y = wx + b$ minimizando el error cuadrático medio usando derivadas parciales.

**Requisitos funcionales:**
- Generar datos sintéticos con $y=2x+1+ruido$ usando numpy
- Implementar función MSE y sus gradientes
- Actualizar parámetros con descenso por gradiente
- Graficar pérdida por iteración
- Comparar parámetros estimados con valores reales

**Habilidades que practica:** Cálculo, optimización, NumPy, Matplotlib

**Criterios de aceptación:**
- Código ejecutable sin errores
- Pérdida disminuye con iteraciones
- $w \in [1.5, 2.5]$ y $b \in [0.5, 1.5]$
- Gráfica de pérdida generada correctamente

**Mejoras opcionales:**
- Añadir learning rate adaptativo
- Implementar mini-batch gradient descent
- Añadir regularización L2

### Proyecto 2: Análisis estadístico completo del dataset Iris (Dificultad: Intermedio)

**Descripción:** Realizar análisis estadístico completo del dataset Iris aplicando estadística descriptiva, correlación, intervalos de confianza y prueba t.

**Requisitos funcionales:**
- Calcular media, mediana, varianza, desviación estándar por clase
- Generar matriz de correlación y visualizar con heatmap
- Calcular intervalo de confianza del 95% para una característica
- Realizar prueba t entre dos especies
- Redactar interpretación estadística

**Habilidades que practica:** Estadística descriptiva e inferencial, pandas, Seaborn, SciPy

**Criterios de aceptación:**
- Medidas descriptivas correctas
- Matriz de correlación con valores válidos
- Intervalo de confianza calculado con scipy.stats
- Prueba t con p-valor reportado e interpretación
- Visualizaciones con etiquetas correctas

**Mejoras opcionales:**
- Aplicar ANOVA entre tres especies
- Implementar bootstrapping
- Analizar outliers con boxplots

### Proyecto 3: PCA desde cero con álgebra lineal (Dificultad: Desafío)

**Descripción:** Implementar Análisis de Componentes Principales desde cero usando matriz de covarianza, autovalores, autovectores y proyección. Comparar con sklearn.

**Requisitos funcionales:**
- Estandarizar datos del dataset Iris
- Calcular matriz de covarianza
- Obtener autovalores y autovectores con np.linalg.eig
- Ordenar por autovalor descendente
- Proyectar a 2 componentes principales y visualizar
- Calcular varianza explicada por componente
- Comparar con sklearn.decomposition.PCA

**Habilidades que practica:** Álgebra lineal, SVD/autovalores, reducción dimensional, visualización

**Criterios de aceptación:**
- Estandarización correcta
- Autovalores/autovectores calculados correctamente
- Proyección a 2D funcional
- Varianza explicada calculada numéricamente
- Comparación con sklearn realizada
- Código bien documentado y ejecutable

**Mejoras opcionales:**
- Implementar con SVD usando np.linalg.svd
- Calcular varianza explicada acumulada
- Aplicar a dataset Wine
