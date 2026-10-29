# Práctica - Seaborn

## Nivel básico

1. **Configuración**
   Enunciado: Configura tema con sns.set_theme() y grafica con estilo mejorado.
   Pista: sns.set_theme(style="whitegrid").
   Criterio verificable: Gráfica con tema aplicado.

2. **Relacionales**
   Enunciado: Crea scatterplot con hue por especie en Iris.
   Pista: sns.scatterplot(data=df, x=..., y=..., hue='species').
   Criterio verificable: Scatter con colores por especie.

3. **Distribucionales**
   Enunciado: histplot, kdeplot para distribución de una característica.
   Pista: Usa bins y kde=True.
   Criterio verificable: Histogramas y densidad mostrados correctamente.

## Nivel intermedio

4. **Categorical**
   Enunciado: boxplot y violinplot por especie para todas las características.
   Pista: Usa múltiples gráficas o subplots.
   Criterio verificable: Comparaciones por especie correctas.

5. **Pairplot**
   Enunciado: Genera pairplot completo con hue por especie.
   Pista: sns.pairplot(df, hue='species').
   Criterio verificable: Matriz de relaciones con colores por clase.

6. **Heatmap de correlación**
   Enunciado: Calcula correlación y visualiza con heatmap anotado.
   Pista: df.corr(), sns.heatmap(corr, annot=True).
   Criterio verificable: Heatmap con valores anotados.

## Nivel desafío

7. **Análisis exploratorio completo**
   Enunciado: Realiza EDA visual completo de Iris con Seaborn.
   Pista: Combina pairplot, heatmap, boxplots.
   Criterio verificable: EDA con 5+ visualizaciones y hallazgos.

8. **Comparación visual de clases**
   Enunciado: Identifica qué características separan mejor las clases visualmente.
   Pista: Usa scatterplots de pares con mayor separación.
   Criterio verificable: Análisis con evidencia visual.
