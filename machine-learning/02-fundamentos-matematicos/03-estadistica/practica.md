# Práctica - Estadística para Machine Learning

## Nivel básico

1. **Medidas descriptivas**
   Enunciado: Con dataset Iris calcula media, mediana, varianza, desviación estándar y rango por característica.
   Pista: Usa numpy con ddof=1 para varianza muestral.
   Criterio verificable: Todas las medidas calculadas numéricamente para las 4 características.

2. **Gráficos descriptivos**
   Enunciado: Genera histograma y boxplot para una característica de Iris con matplotlib/seaborn.
   Pista: Usa plt.hist y sns.boxplot con etiquetas.
   Criterio verificable: Gráficas generadas con títulos y etiquetas correctas.

3. **Matriz de correlación**
   Enunciado: Calcula matriz de correlación de Pearson para Iris e identifica pares con mayor correlación.
   Pista: Usa np.corrcoef o pandas corr().
   Criterio verificable: Matriz mostrada numéricamente con valores entre -1 y 1.

## Nivel intermedio

4. **Intervalo de confianza**
   Enunciado: Calcula intervalo de confianza del 95% para media de sépalo con scipy.stats.t.interval.
   Pista: Usa stats.sem para error estándar.
   Criterio verificable: Intervalo con dos valores numéricos, nivel de confianza correcto.

5. **Prueba de hipótesis**
   Enunciado: Realiza prueba t entre dos especies de Iris para una característica y interpreta p-valor.
   Pista: Usa scipy.stats.ttest_ind.
   Criterio verificable: t-statistic, p-valor reportados con interpretación clara.

6. **Análisis por grupos**
   Enunciado: Agrupa por especie y calcula media y desviación para todas las características.
   Pista: Usa pandas groupby.
   Criterio verificable: Tabla con medias/desviaciones por especie correcta.

## Nivel desafío

7. **Bootstrapping**
   Enunciado: Implementa bootstrap para estimar intervalo de confianza de la mediana con 1000 muestras.
   Pista: Muestreo con reemplazo, calcula percentiles 2.5 y 97.5.
   Criterio verificable: Intervalo numérico calculado con 1000 iteraciones.

8. **Análisis completo Iris**
   Enunciado: Realiza análisis estadístico completo: descriptivas, correlaciones, visualización e interpretación.
   Pista: Integra todos los conceptos del tema.
   Criterio verificable: Reporte con 5 hallazgos numéricamente respaldados.
