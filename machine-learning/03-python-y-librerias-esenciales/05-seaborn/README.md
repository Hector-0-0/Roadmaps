# 5. Seaborn para Machine Learning

## 1. ¿Qué es y para qué sirve?

Seaborn es una librería basada en Matplotlib para visualizaciones estadísticas atractivas. Simplifica creación de gráficos complejos con menos código.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Ideal para análisis exploratorio, visualización de correlaciones, distribuciones y comparación entre grupos en datasets como Iris, Wine, Titanic.

## 3. Conceptos clave

- **Relacionales**: scatterplot, lineplot.
- **Distribucionales**: histplot, kdeplot, boxplot, violinplot.
- **Categorical**: barplot, countplot, boxplot.
- **Matrices**: heatmap, clustermap.
- **Paletas**: color palettes.
- **Themes**: set_theme.
- **pairplot**: Exploración multivariable.

## 4. Ejemplos de código en Python

```python
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = [iris.target_names[t] for t in iris.target]
sns.pairplot(df, hue='species')
plt.show()
```

```python
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Usar muchos colores. **Buena práctica**: Elegir paletas adecuadas.
- **Error común**: Gráficas sobrecargadas. **Buena práctica**: Elegir gráfico según pregunta.
- **Error común**: Olvidar tema. **Buena práctica**: Usar sns.set_theme() para consistencia.
- **Error común**: Interpretar mal correlación. **Buena práctica**: Recordar correlación no implica causalidad.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Ventaja de Seaborn sobre Matplotlib puro?  
   **Respuesta orientativa:** Menos código, mejor aspecto por defecto, funciones estadísticas integradas.

2. **Pregunta:** ¿Cuándo usar pairplot?  
   **Respuesta orientativa:** Para exploración rápida de relaciones entre todas las variables con distinción por clase.

3. **Pregunta:** ¿Para qué usar heatmap?  
   **Respuesta orientativa:** Visualizar matriz de correlación o datos tabulares con colores.

4. **Pregunta:** ¿Diferencia entre boxplot y violinplot?  
   **Respuesta orientativa:** Boxplot muestra cuartiles; violinplot muestra distribución completa (densidad).

5. **Pregunta:** ¿Cuándo usar hue en Seaborn?  
   **Respuesta orientativa:** Para colorear por variable categórica y comparar grupos.
