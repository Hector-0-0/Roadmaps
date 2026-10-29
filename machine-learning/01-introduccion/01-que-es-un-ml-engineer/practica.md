# Práctica - ¿Qué es un Machine Learning Engineer?

## Nivel básico

1. **Definir el rol**
   Enunciado: Escribe una definición propia de Machine Learning Engineer, mencionando entrenamiento, evaluación y despliegue.
   Pista: Usa la diferencia entre ajustar un modelo y usarlo para predecir datos nuevos.
   Criterio verificable: La respuesta incluye las tres acciones (entrenamiento, evaluación, despliegue) con descripción correcta.

2. **Explorar Iris**
   Enunciado: Carga el dataset Iris con scikit-learn y muestra forma, nombres de características y nombres de clases.
   Pista: Usa load_iris() de sklearn.datasets y accede a data, feature_names, target_names.
   Criterio verificable: Código ejecutable que imprime shape, feature_names y target_names sin errores.

3. **División estratificada**
   Enunciado: Divide Iris con train_test_split usando test_size=0.2, random_state=42 y stratify=y. Verifica proporciones.
   Pista: Calcula conteo de clases en y_train y y_test con np.bincount.
   Criterio verificable: Proporciones de clases en train y test son similares a las del dataset completo.

## Nivel intermedio

4. **Entrenar y evaluar**
   Enunciado: Entrena LogisticRegression(max_iter=200) en los datos divididos y calcula accuracy con accuracy_score.
   Pista: Ajusta solo con X_train,y_train. Evalúa con X_test,y_test.
   Criterio verificable: Se obtiene un valor numérico de accuracy entre 0 y 1, calculado correctamente.

5. **Pipeline básico**
   Enunciado: Crea un Pipeline con StandardScaler y LogisticRegression. Entrena y evalúa obteniendo accuracy.
   Pista: Usa sklearn.pipeline.Pipeline con lista de tuplas ('nombre', estimador).
   Criterio verificable: Pipeline definido correctamente, fit solo en train, accuracy calculado en test.

6. **Reproducibilidad**
   Enunciado: Ejecuta el mismo experimento dos veces con mismo random_state y muestra que los resultados son idénticos.
   Pista: Guarda accuracy en dos variables y verifica igualdad.
   Criterio verificable: Los dos valores de accuracy son exactamente iguales.

## Nivel desafío

7. **Comparar con y sin escalado**
   Enunciado: Compara accuracy de LogisticRegression con y sin StandardScaler usando mismo split estratificado.
   Pista: Usa Pipeline para el caso con escalado. Mantén random_state idéntico.
   Criterio verificable: Se reportan ambos valores numéricos, con explicación de la diferencia observada.

8. **Flujo completo documentado**
   Enunciado: Implementa un flujo completo para Iris: carga, división estratificada, pipeline, validación cruzada (cv=5) y reporte.
   Pista: Usa cross_val_score con el pipeline. Calcula media y desviación estándar.
   Criterio verificable: Código ejecutable que muestra scores de 5 folds, media y desviación estándar con valores numéricos.
