# Habilidades y responsabilidades

## Objetivo

Identificar las habilidades técnicas y blandas necesarias, así como las responsabilidades diarias de un Machine Learning Engineer.

## 1. Habilidades técnicas

| Área | Habilidades | Recursos a dominar |
| --- | --- | --- |
| Programación | Python, estructuras de datos, funciones, POO | Sintaxis, manejo de archivos, excepciones |
| Matemáticas | Álgebra lineal, cálculo, estadística, probabilidad | Vectores, gradientes, distribuciones, hipótesis |
| Datos | Limpieza, transformación, visualización | NumPy, pandas, Matplotlib, Seaborn |
| ML Clásico | Supervisado, no supervisado, validación | scikit-learn, métricas, regularización |
| Deep Learning | Redes neuronales, CNN, RNN | PyTorch o TensorFlow/Keras |
| Ingeniería | Git, APIs, testing, despliegue básico | Control de versiones, pipelines, monitoreo |

## 2. Responsabilidades típicas

- **Exploración**: Analizar datos y entender el problema de negocio.
- **Preparación**: Limpiar, transformar y crear características.
- **Modelado**: Probar algoritmos, ajustar hiperparámetros.
- **Evaluación**: Usar métricas correctas con validación rigurosa.
- **Despliegue**: Exponer modelo como API o integrarlo a sistema.
- **Monitoreo**: Detectar drift de datos o degradación del modelo.
- **Documentación**: Explicar decisiones, resultados y limitaciones.

## 3. Ejemplo práctico

```python
# Checklist de flujo ML reproducible
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
pipe = Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression(max_iter=200))])
pipe.fit(X_train, y_train)
print('Accuracy:', accuracy_score(y_test, pipe.predict(X_test)))
```

```python
# Validación simple con validación cruzada
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
clf = RandomForestClassifier(n_estimators=50, random_state=42)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
print('Media CV:', scores.mean())
```

## 4. Habilidades blandas

- Comunicación clara con perfiles técnicos y no técnicos.
- Pensamiento crítico y enfoque a negocio.
- Curiosidad para investigar errores.
- Gestión del tiempo y priorización.
- Ética en IA: sesgo, privacidad y transparencia.

## 5. Autoevaluación

1. ¿Qué pasos seguirías antes de entrenar un modelo?
2. ¿Por qué usar un Pipeline de scikit-learn?
3. ¿Qué es data drift y por qué es importante monitorearlo?
4. ¿Cuándo usar validación cruzada en lugar de solo train-test?
5. ¿Qué consideraciones éticas debes tener al trabajar con datos personales?

**Respuestas esperadas:**
1. Entender problema, revisar calidad de datos, limpiar, explorar, dividir correctamente y definir métrica.
2. Para encadenar transformaciones y modelo, evitar fuga de datos y garantizar reproducibilidad.
3. Cambio en distribución de datos con el tiempo que puede degradar el rendimiento del modelo.
4. Cuando el conjunto de datos es pequeño o se necesita estimación más robusta del rendimiento.
5. Cumplir normativas, anonimizar, evitar sesgo, garantizar transparencia y uso responsable.
