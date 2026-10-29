# 4. Matplotlib para Machine Learning

## 1. ¿Qué es y para qué sirve?

Matplotlib permite crear visualizaciones estáticas para análisis exploratorio, diagnóstico de modelos y presentación de resultados.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Es fundamental para entender distribuciones, correlaciones, curvas de aprendizaje y evaluación de modelos.

## 3. Conceptos clave

- **Figure y Axes**: Figura contenedora y ejes para graficar.
- **plot/scatter/hist/bar**: Tipos básicos de gráficas.
- **Subplots**: Múltiples gráficas en una figura.
- **Personalización**: títulos, labels, leyendas, colores.
- **Estilos**: plt.style.
- **Guardar**: savefig.

## 4. Ejemplos de código en Python

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title('Seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
```

```python
from sklearn.datasets import load_iris
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
plt.scatter(df.iloc[:,0], df.iloc[:,1], c=df['target'])
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()
```

## 5. Errores comunes y buenas prácticas

- **Error común**: No etiquetar ejes. **Buena práctica**: Siempre añadir xlabel/ylabel/title.
- **Error común**: Gráficas confusas. **Buena práctica**: Usar colores/leyendas claros.
- **Error común**: Muchos elementos. **Buena práctica**: Usar subplots para organizar.
- **Error común**: No guardar figuras. **Buena práctica**: Usar savefig con dpi adecuado.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Diferencia entre Figure y Axes?  
   **Respuesta orientativa:** Figure es ventana completa, Axes es área donde se dibuja.

2. **Pregunta:** ¿Cuándo usar scatter vs plot?  
   **Respuesta orientativa:** scatter para puntos individuales, plot para líneas/series.

3. **Pregunta:** ¿Para qué usar subplots?  
   **Respuesta orientativa:** Comparar múltiples visualizaciones en una figura.

4. **Pregunta:** ¿Cómo guardar figura?  
   **Respuesta orientativa:** plt.savefig('nombre.png', dpi=300, bbox_inches='tight').

5. **Pregunta:** ¿Importancia de visualización en ML?  
   **Respuesta orientativa:** Detecta patrones, outliers, relaciones y valida resultados.
