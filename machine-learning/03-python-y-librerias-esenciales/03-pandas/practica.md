# Práctica - pandas

## Nivel básico

1. **Crear DataFrame**
   Enunciado: Crea DataFrame desde diccionario, lista de listas y desde dataset Iris.
   Pista: Usa pd.DataFrame().
   Criterio verificable: 3 formas diferentes funcionando correctamente.

2. **Exploración**
   Enunciado: Usa head(), tail(), info(), describe(), shape, columns.
   Pista: Explora dataset Iris completo.
   Criterio verificable: Todas las funciones usadas con salida correcta.

3. **Selección y filtrado**
   Enunciado: Selecciona columnas, filtra filas con condición booleana.
   Pista: Usa df['col'] o df[['col1','col2']].
   Criterio verificable: Selección y filtrado correctos.

## Nivel intermedio

4. **Limpieza**
   Enunciado: Crea DataFrame con NaN, usa dropna, fillna con media.
   Pista: df.fillna(df.mean()).
   Criterio verificable: Valores faltantes tratados correctamente.

5. **Agrupación**
   Enunciado: Agrupa Iris por target con mean, count, std.
   Pista: df.groupby('target').agg().
   Criterio verificable: Agregaciones correctas por grupo.

6. **Transformación**
   Enunciado: Crea nueva columna, aplica función con apply(), cambia tipos con astype().
   Pista: Usa lambda o función definida.
   Criterio verificable: Transformaciones aplicadas correctamente.

## Nivel desafío

7. **Análisis completo**
   Enunciado: Carga Iris, analiza por especie, crea resumen y ordena resultados.
   Pista: Combina groupby, sort_values.
   Criterio verificable: Resumen completo con hallazgos numéricos.

8. **Preparación para ML**
   Enunciado: Separa features/target, verifica dtypes, crea copia para modelado.
   Pista: X = df.drop('target', axis=1), y = df['target'].
   Criterio verificable: X,y correctos listos para train_test_split.
