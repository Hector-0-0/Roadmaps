# Práctica

## Nivel básico

1. **Exploración con Iris**
   Enunciado: Carga dataset Iris, explora forma, tipos y estadísticas básicas.
   Pista: Usa pandas y numpy para obtener resumen completo de los datos.
   Criterio verificable: Se muestran shape, dtypes, describe() con valores numéricos correctos.

2. **Preparación correcta**
   Enunciado: Divide datos en train/test con estratificación usando random_state=42.
   Pista: Usa train_test_split con stratify=y para mantener proporciones de clases.
   Criterio verificable: División con tamaños correctos y proporciones estratificadas verificadas.

3. **Implementación base**
   Enunciado: Implementa solución base con algoritmo apropiado y evalúa con métrica correcta.
   Pista: Elige métrica acorde al tipo de problema y evalúa solo en test.
   Criterio verificable: Métrica numérica calculada correctamente en conjunto de test.

## Nivel intermedio

4. **Pipeline sin fuga**
   Enunciado: Construye Pipeline con transformaciones y modelo, entrena y evalúa correctamente.
   Pista: Usa sklearn.pipeline.Pipeline para encadenar pasos evitando fuga de datos.
   Criterio verificable: Pipeline funcional con fit en train y predict en test.

5. **Validación cruzada**
   Enunciado: Usa cross_val_score con cv=5 y reporta media y desviación estándar.
   Pista: Usa numpy para calcular mean y std de los scores obtenidos.
   Criterio verificable: 5 scores mostrados, media y desviación calculadas numéricamente.

6. **Comparación objetiva**
   Enunciado: Compara al menos dos configuraciones con misma validación cruzada.
   Pista: Mantén mismo split/validación para comparación justa entre configuraciones.
   Criterio verificable: Comparación con valores numéricos y conclusión fundamentada.

## Nivel desafío

7. **Caso práctico completo**
   Enunciado: Resuelve caso end to end con limpieza, modelado, validación y evaluación.
   Pista: Documenta cada paso y justifica decisiones con evidencia numérica.
   Criterio verificable: Solución completa con métricas numéricas en test y explicación clara.

8. **Análisis crítico**
   Enunciado: Analiza limitaciones, posibles mejoras y propone siguiente paso con justificación.
   Pista: Considera sobreajuste, datos insuficientes o mejoras posibles.
   Criterio verificable: Análisis con al menos 3 limitaciones y 3 mejoras con justificación.
