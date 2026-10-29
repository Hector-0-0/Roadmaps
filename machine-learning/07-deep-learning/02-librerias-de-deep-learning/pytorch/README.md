# PyTorch

## 1. ¿Qué es y para qué sirve?

PyTorch es un tema fundamental en Machine Learning que permite preparar, analizar y modelar datos correctamente para obtener resultados confiables.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Este tema se conecta con las etapas anteriores y posteriores, proporcionando bases necesarias para el modelado, evaluación y despliegue de modelos.

## 3. Conceptos clave

- **Concepto fundamental**: Idea central con aplicación práctica en ML usando datasets públicos.
- **Métodos y técnicas**: Enfoques utilizados para resolver problemas relacionados.
- **Aplicaciones**: Casos de uso reales en proyectos de ML.
- **Consideraciones**: Puntos importantes a tener en cuenta.
- **Mejores prácticas**: Recomendaciones para aplicación correcta.

## 4. Ejemplos de código en Python

```python
# ejemplo unico para pytorch
import numpy as np
from sklearn.datasets import load_wine
X = load_wine().data
print(X.shape)
```

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target)
clf = LogisticRegression(max_iter=200)
clf.fit(X_train, y_train)
print(accuracy_score(y_test, clf.predict(X_test)))
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Aplicar técnicas sin entender datos. **Buena práctica**: Analizar datos antes de transformar.
- **Error común**: Fuga de datos. **Buena práctica**: Aplicar transformaciones solo con datos de entrenamiento.
- **Error común**: Usar parámetros por defecto sin justificación. **Buena práctica**: Entender efectos de parámetros.
- **Error común**: No validar resultados. **Buena práctica**: Verificar con métricas apropiadas.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Cuál es el objetivo principal de PyTorch?  
   **Respuesta orientativa:** Aplicar técnicas correctas para resolver el problema planteado con enfoque reproducible.

2. **Pregunta:** ¿Cómo se integra en un pipeline de ML?  
   **Respuesta orientativa:** Se ubica en el paso correspondiente con validación adecuada para evitar fuga de datos.

3. **Pregunta:** ¿Qué métricas usar para validar?  
   **Respuesta orientativa:** Depende del problema, usar métricas correctas y validación cruzada.

4. **Pregunta:** ¿Qué librerías son apropiadas?  
   **Respuesta orientativa:** NumPy, pandas, scikit-learn según el caso de uso.

5. **Pregunta:** ¿Cómo garantizar reproducibilidad?  
   **Respuesta orientativa:** Fijar semillas, usar pipelines y documentar pasos.
