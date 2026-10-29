# Tipos De Machine Learning

## 1. ¿Qué es y para qué sirve?

Tipos de ML es un tema fundamental en Machine Learning que permite preparar, analizar y modelar datos correctamente para obtener resultados confiables.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Este tema se conecta con las etapas anteriores y posteriores, proporcionando bases necesarias para el modelado, evaluación y despliegue de modelos.

## 3. Conceptos clave

- **Concepto fundamental**: Idea central con aplicación práctica en ML.
- **Métodos y técnicas**: Enfoques utilizados para resolver problemas relacionados.
- **Aplicaciones**: Casos de uso reales en proyectos de ML.
- **Consideraciones**: Puntos importantes a tener en cuenta.
- **Mejores prácticas**: Recomendaciones para aplicación correcta.

## 4. Ejemplos de código en Python

```python
from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()
X = iris.data
print(X.shape, np.mean(X, axis=0))
```

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape)
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Aplicar técnicas sin entender datos. **Buena práctica**: Analizar datos antes de transformar.
- **Error común**: Fuga de datos. **Buena práctica**: Aplicar transformaciones solo con datos de entrenamiento.
- **Error común**: Usar parámetros por defecto sin justificación. **Buena práctica**: Entender efectos de parámetros.
- **Error común**: No validar resultados. **Buena práctica**: Verificar con métricas apropiadas.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Cuál es el objetivo principal de este tema?  
   **Respuesta orientativa:** Aplicar técnicas correctas para preparar o modelar datos con fines predictivos.

2. **Pregunta:** ¿Cómo se aplica a un proyecto de ML?  
   **Respuesta orientativa:** Se integra en el pipeline desde preprocesamiento hasta evaluación.

3. **Pregunta:** ¿Qué errores evitar?  
   **Respuesta orientativa:** Fuga de datos, transformación incorrecta y falta de validación.

4. **Pregunta:** ¿Qué herramientas usar?  
   **Respuesta orientativa:** NumPy, pandas, scikit-learn según corresponda al tema.

5. **Pregunta:** ¿Cómo verificar que es correcto?  
   **Respuesta orientativa:** Usar validación cruzada y métricas apropiadas al problema.
