# Práctica - Matplotlib

## Nivel básico

1. **Gráfica lineal**
   Enunciado: Grafica $y=x^2$ para x de -5 a 5 con título, etiquetas y leyenda.
   Pista: Usa plt.plot().
   Criterio verificable: Gráfica correcta con todos los elementos.

2. **Scatter plot**
   Enunciado: Grafica scatter de dos características de Iris coloreado por target.
   Pista: Usa c=df['target'].
   Criterio verificable: Scatter con colores diferenciados por clase.

3. **Histograma**
   Enunciado: Histograma de una característica con bins apropiados.
   Pista: plt.hist(df[col], bins=20).
   Criterio verificable: Histograma con distribución visible.

## Nivel intermedio

4. **Subplots**
   Enunciado: Crea 2x2 subplots con 4 gráficas diferentes de Iris.
   Pista: fig, axes = plt.subplots(2,2).
   Criterio verificable: 4 gráficas organizadas correctamente.

5. **Boxplot**
   Enunciado: Boxplot por especie para comparar distribución.
   Pista: Usa datos agrupados.
   Criterio verificable: Boxplots comparativos correctos.

6. **Personalización**
   Enunciado: Personaliza colores, markers, linestyle, grid.
   Pista: Usa parámetros de plt.plot.
   Criterio verificable: Gráfica con personalizaciones aplicadas.

## Nivel desafío

7. **Curva de pérdida**
   Enunciado: Simula curva de pérdida decreciente y grafícala con etiquetas.
   Pista: Genera lista de pérdidas simuladas.
   Criterio verificable: Curva decreciente correcta.

8. **Comparación visual**
   Enunciado: Compara predicciones vs valores reales con scatter y línea ideal.
   Pista: Añade línea y=x.
   Criterio verificable: Gráfica comparativa clara.
