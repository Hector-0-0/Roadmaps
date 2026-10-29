# Práctica - 07 Escalado Y Normalizacion

## Nivel básico

1. **Exploración**
   Enunciado: Carga dataset Iris con código y analiza características relevantes para 07 escalado y normalizacion.
   Pista: Usa pandas para explorar forma, tipos y estadísticas básicas del dataset completo.
   Criterio verificable: Se reporta shape, columnas y al menos 3 estadísticas numéricas correctas.

2. **Preparación**
   Enunciado: Aplica preparación adecuada para 07 escalado y normalizacion usando train_test_split con random_state=42 y estratificación.
   Pista: Usa sklearn.model_selection.train_test_split con stratify cuando hay variable objetivo categórica.
   Criterio verificable: División con tamaños correctos y proporciones estratificadas verificadas numéricamente.

3. **Implementación base**
   Enunciado: Implementa técnica base de 07 escalado y normalizacion con dataset Iris usando scikit-learn.
   Pista: Elige algoritmo apropiado, usa parámetros explícitos y evalúa correctamente.
   Criterio verificable: Implementación ejecutable con métrica numérica calculada en test.

## Nivel intermedio

4. **Integración en pipeline**
   Enunciado: Crea Pipeline que integre transformaciones y proceso sin fuga de datos usando sklearn.pipeline.Pipeline.
   Pista: Ajusta todas las transformaciones solo con datos de entrenamiento mediante fit_transform.
   Criterio verificable: Pipeline funcional con fit en train y predict en test sin errores.

5. **Validación cruzada**
   Enunciado: Valida con cross_val_score cv=5 calculando media y desviación estándar con numpy.
   Pista: Usa cross_val_score del pipeline o estimador con validación cruzada adecuada.
   Criterio verificable: 5 valores numéricos mostrados con media y desviación estándar calculadas correctamente.

6. **Comparación**
   Enunciado: Compara dos configuraciones distintas de 07 escalado y normalizacion con misma validación cruzada.
   Pista: Mantén condiciones idénticas para comparación objetiva y justa.
   Criterio verificable: Comparación con valores numéricos y conclusión justificada con evidencia.

## Nivel desafío

7. **Caso end to end**
   Enunciado: Desarrolla solución completa con preparación, aplicación, validación y evaluación en test.
   Pista: Documenta cada paso y justifica decisiones con evidencia numérica.
   Criterio verificable: Métricas numéricas calculadas en test con interpretación correcta.

8. **Análisis crítico**
   Enunciado: Identifica limitaciones y propone mejora medible cuantificando diferencia numérica.
   Pista: Implementa mejora propuesta y compara con línea base usando misma validación.
   Criterio verificable: Mejora cuantificada con diferencia numérica demostrada y justificada.
