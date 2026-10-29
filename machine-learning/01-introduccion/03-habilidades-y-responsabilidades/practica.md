# Práctica

## Nivel básico

1. **Identificar el rol**
   Enunciado: Define con tus palabras qué es un Machine Learning Engineer y menciona tres responsabilidades clave.
   Pista: Usa la definición del README y diferencia entre entrenamiento y despliegue.
   Criterio verificable: Se menciona entrenamiento, evaluación, despliegue y al menos tres responsabilidades correctas.

2. **Comparar roles**
   Enunciado: Completa una tabla comparando ML Engineer y AI Engineer con al menos 4 aspectos.
   Pista: Considera enfoque, herramientas, datos y tipo de modelos.
   Criterio verificable: Tabla con 4 aspectos distintos y diferencias correctas para ambos roles.

3. **Explorar dataset Iris**
   Enunciado: Carga el dataset Iris con scikit-learn, imprime forma, nombres de características y nombres de clases.
   Pista: Usa load_iris() de sklearn.datasets. Accede a data, feature_names y target_names.
   Criterio verificable: Código ejecutable que imprime shape, feature_names y target_names correctamente.

## Nivel intermedio

4. **Entrenamiento rápido**
   Enunciado: Divide Iris en train/test con test_size=0.2, entrena LogisticRegression y calcula accuracy.
   Pista: Usa train_test_split con random_state para reproducibilidad. Usa accuracy_score.
   Criterio verificable: Accuracy calculado, código ejecutable, división correcta.

5. **Pipeline reproducible**
   Enunciado: Crea un Pipeline con StandardScaler y LogisticRegression, entrena y evalúa en test.
   Pista: Pipeline evita fuga de datos. Aplica fit solo en train.
   Criterio verificable: Pipeline implementado correctamente, evaluación en conjunto de test.

6. **Validación cruzada**
   Enunciado: Usa cross_val_score con cv=5 sobre RandomForestClassifier y muestra media y desviación.
   Pista: Usa numpy para calcular mean y std.
   Criterio verificable: Scores de 5 folds mostrados, media y desviación calculadas.

## Nivel desafío

7. **Analizar flujo completo**
   Enunciado: Documenta un flujo ML completo para un caso de uso (detección de fraude) con todas las etapas.
   Pista: Incluye datos, limpieza, features, validación, métricas, despliegue y monitoreo.
   Criterio verificable: Documento con todas las etapas, métricas apropiadas y consideraciones de negocio.

8. **Reflexión ética**
   Enunciado: Identifica tres riesgos éticos al usar datos personales y propone una mitigación para cada uno.
   Pista: Considera sesgo, privacidad, transparencia y consentimiento.
   Criterio verificable: Tres riesgos con mitigaciones concretas y aplicables.
