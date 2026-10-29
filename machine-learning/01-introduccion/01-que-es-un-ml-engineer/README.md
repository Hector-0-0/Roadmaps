# ¿Qué es un Machine Learning Engineer?

## Objetivo

Comprender el rol del Machine Learning Engineer, sus responsabilidades, su ámbito de trabajo y cómo se diferencia de otros roles relacionados con inteligencia artificial.

## 1. Definición

Un Machine Learning Engineer es un profesional que diseña, construye, entrena, evalúa y despliega modelos de Machine Learning para resolver problemas del mundo real. Combina conocimientos de ingeniería de software, matemáticas, estadísticas y datos para llevar modelos desde prototipos hasta sistemas en producción.

## 2. ¿Qué tareas realiza?

- Recopilar, limpiar y preparar datos para entrenamiento.
- Seleccionar algoritmos adecuados según el problema.
- Entrenar, ajustar hiperparámetros y evaluar modelos.
- Implementar pipelines reproducibles y escalables.
- Desplegar modelos y monitorear su rendimiento en producción.
- Colaborar con científicos de datos, ingenieros de datos y producto.

## 3. Ejemplo práctico

```python
# Ejemplo simple: cargar dataset Iris con scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = LogisticRegression(max_iter=200)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(accuracy_score(y_test, y_pred))
```

```python
# Ejemplo: ver forma de datos
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data.shape)
print(iris.target_names)
```

## 4. Habilidades clave del rol

- Programación en Python.
- Conocimientos de álgebra lineal, cálculo, estadística y probabilidad.
- Manejo de librerías como NumPy, pandas, scikit-learn.
- Comprensión de evaluación de modelos y validación.
- Conocimientos básicos de ingeniería: versionado, testing y despliegue.

## 5. Casos de uso comunes

- Sistemas de recomendación.
- Detección de fraude.
- Clasificación de imágenes o texto.
- Predicción de demanda.
- Detección de anomalías.

## 6. Autoevaluación

1. ¿Cuál es la diferencia entre entrenar un modelo y desplegarlo en producción?
2. ¿Qué responsabilidades comparte un ML Engineer con un Data Scientist?
3. ¿Por qué es importante la reproducibilidad al trabajar con modelos?
4. ¿Qué métricas usarías para un problema de clasificación binaria?
5. ¿Por qué se requiere conocimiento de ingeniería de software en este rol?

**Respuestas esperadas:**
1. Entrenar es ajustar parámetros con datos; desplegar es integrar el modelo en un sistema accesible para usuarios o servicios.
2. Ambos analizan datos y construyen modelos, pero el ML Engineer pone mayor énfasis en escalabilidad, despliegue y mantenimiento.
3. Para poder replicar resultados, depurar errores y garantizar consistencia entre entornos.
4. Accuracy, precision, recall, F1-score y ROC-AUC, considerando el balance de clases.
5. Porque hay que escribir código mantenible, automatizar pipelines, manejar dependencias y asegurar integración con sistemas existentes.
