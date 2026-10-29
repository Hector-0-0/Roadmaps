# 1. ¿Qué es un Machine Learning Engineer?

## 1. ¿Qué es y para qué sirve?

Un Machine Learning Engineer es un profesional que diseña, entrena, evalúa y despliega modelos de Machine Learning para resolver problemas concretos. Sirve para transformar datos en sistemas predictivos que funcionan de forma confiable en producción.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Este rol conecta matemáticas, programación, datos y despliegue. Los fundamentos matemáticos permiten entender algoritmos, Python y librerías permiten implementarlos, y la evaluación garantiza resultados correctos antes de integrar modelos a sistemas reales.

## 3. Conceptos clave

- **Modelo**: Función parametrizada que aprende una relación a partir de datos. $f_\theta: X \rightarrow Y$.
- **Entrenamiento**: Proceso de ajustar parámetros $\theta$ minimizando una función de pérdida $L(\theta)$.
- **Inferencia**: Uso del modelo entrenado para generar predicciones sobre datos nuevos.
- **Pipeline**: Secuencia reproducible de pasos desde datos hasta predicción.
- **Reproducibilidad**: Capacidad de obtener los mismos resultados con los mismos datos y código.

## 4. Ejemplos de código en Python

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
clf = LogisticRegression(max_iter=200)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(accuracy_score(y_test, y_pred))
```

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target
print(X.shape, np.unique(y))
print(iris.feature_names, iris.target_names)
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Entrenar y evaluar con los mismos datos. **Buena práctica**: Usar división train/test o validación cruzada.
- **Error común**: Ignorar el tipo de problema. **Buena práctica**: Elegir métrica acorde al objetivo.
- **Error común**: Código no reproducible. **Buena práctica**: Fijar semillas y usar pipelines.
- **Error común**: Saltarse limpieza. **Buena práctica**: Validar calidad de datos antes de modelar.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Qué diferencia hay entre entrenamiento e inferencia?  
   **Respuesta orientativa:** El entrenamiento ajusta parámetros con datos conocidos; la inferencia usa el modelo ajustado para predecir datos nuevos.

2. **Pregunta:** ¿Por qué es importante dividir datos en train y test?  
   **Respuesta orientativa:** Para estimar el rendimiento en datos no vistos y detectar sobreajuste.

3. **Pregunta:** ¿Qué es un pipeline en Machine Learning?  
   **Respuesta orientativa:** Una secuencia encadenada de transformaciones y modelo que garantiza reproducibilidad y evita fuga de datos.

4. **Pregunta:** ¿Por qué usar stratify al dividir un dataset balanceado o desbalanceado?  
   **Respuesta orientativa:** Mantiene la proporción de clases en train y test, lo cual es importante para evaluación correcta.

5. **Pregunta:** ¿Qué papel juega la función de pérdida $L(\theta)$?  
   **Respuesta orientativa:** Mide qué tan mal predice el modelo; el objetivo es minimizarla ajustando $\theta$.
