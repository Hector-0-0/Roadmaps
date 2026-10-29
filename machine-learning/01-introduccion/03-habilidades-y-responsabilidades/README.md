# 3. Habilidades y responsabilidades

## 1. ¿Qué es y para qué sirve?

Conocer las habilidades y responsabilidades permite identificar qué aprender, cómo practicar y qué esperar en proyectos reales de Machine Learning. Sirve como hoja de ruta para desarrollar competencias técnicas y blandas.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Las habilidades cubiertas aquí se desarrollan a lo largo de todo el roadmap: matemáticas en etapa 2, Python y librerías en etapa 3, datos en etapa 4, modelado en etapas 5 y 6, y despliegue/monitoreo en etapas posteriores.

## 3. Conceptos clave

- **Habilidades técnicas**: Conocimientos prácticos en programación, matemáticas, datos y modelado.
- **Pipeline reproducible**: Conjunto de pasos automatizables y versionables.
- **Validación cruzada**: Técnica para estimar rendimiento usando múltiples particiones ($k$-fold).
- **Data drift**: Cambio en distribución de datos que puede degradar el modelo con el tiempo.
- **Monitoreo**: Seguimiento de métricas y comportamiento del modelo en producción.
- **Ética en IA**: Consideraciones sobre sesgo, privacidad, transparencia y uso responsable.

## 4. Ejemplos de código en Python

```python
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
print(accuracy_score(y_test, pipe.predict(X_test)))
```

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

iris = load_iris()
clf = RandomForestClassifier(n_estimators=50, random_state=42)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
print(np.mean(scores), np.std(scores))
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Saltar validación. **Buena práctica**: Usar train/test y validación cruzada.
- **Error común**: Fuga de datos. **Buena práctica**: Usar Pipeline para ajustar transformaciones solo en train.
- **Error común**: Ignorar monitoreo. **Buena práctica**: Planificar seguimiento tras despliegue.
- **Error común**: Descuidar ética. **Buena práctica**: Evaluar sesgo y proteger datos sensibles.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Qué pasos clave seguir antes de entrenar un modelo?  
   **Respuesta orientativa:** Entender problema, explorar datos, limpiar, dividir correctamente, definir métrica y verificar calidad.

2. **Pregunta:** ¿Por qué usar un Pipeline en lugar de aplicar transformaciones manualmente?  
   **Respuesta orientativa:** Evita fuga de datos, garantiza reproducibilidad y simplifica despliegue.

3. **Pregunta:** ¿Cuándo usar validación cruzada en lugar de un solo split?  
   **Respuesta orientativa:** Cuando el dataset es pequeño o se necesita una estimación más robusta del rendimiento.

4. **Pregunta:** ¿Qué es data drift y cómo afecta al modelo?  
   **Respuesta orientativa:** Es el cambio en la distribución de datos con el tiempo que puede reducir la precisión del modelo.

5. **Pregunta:** ¿Qué consideraciones éticas son importantes en ML?  
   **Respuesta orientativa:** Minimización de datos, evitar sesgo, consentimiento, transparencia, explicabilidad y uso responsable.
