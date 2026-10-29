# 3. pandas para Machine Learning

## 1. ¿Qué es y para qué sirve?

pandas permite manipular datos tabulares con Series y DataFrames. Es esencial para limpieza, transformación, agregación y exploración de datos.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Casi todos los proyectos de ML empiezan cargando datos con pandas, limpiándolos y preparándolos para scikit-learn.

## 3. Conceptos clave

- **Series**: Arreglo unidimensional etiquetado.
- **DataFrame**: Estructura tabular 2D con columnas.
- **Index**: Etiquetas de filas/columnas.
- **Lectura/escritura**: read_csv, read_json, to_csv.
- **Selección**: loc, iloc, filtrado booleano.
- **Agrupación**: groupby, agregaciones.
- **Limpieza**: dropna, fillna, isna.
- **Transformación**: apply, map, astype.

## 4. Ejemplos de código en Python

```python
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.head())
print(df.describe())
```

```python
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.groupby('target').mean())
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Modificar vista sin copiar. **Buena práctica**: Usar .copy().
- **Error común**: Encadenamiento confuso. **Buena práctica**: Usar operaciones claras.
- **Error común**: Tipos incorrectos. **Buena práctica**: Verificar con .dtypes.
- **Error común**: NaN no manejados. **Buena práctica**: Identificar y tratar valores faltantes.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Diferencia entre Series y DataFrame?  
   **Respuesta orientativa:** Series 1D, DataFrame 2D con múltiples columnas.

2. **Pregunta:** ¿Diferencia entre loc e iloc?  
   **Respuesta orientativa:** loc por etiquetas, iloc por índices numéricos.

3. **Pregunta:** ¿Para qué usar groupby?  
   **Respuesta orientativa:** Agrupar por clave y aplicar agregaciones por grupo.

4. **Pregunta:** ¿Cómo detectar valores faltantes?  
   **Respuesta orientativa:** Usar .isna(), .isnull(), .info().

5. **Pregunta:** ¿Por qué usar copy() al filtrar?  
   **Respuesta orientativa:** Evita SettingWithCopyWarning y asegura copia independiente.


## 7. Aplicaciones en Machine Learning

pandas es fundamental para cargar datasets, explorar, limpiar, crear features y preparar datos para modelado. Permite integrar con scikit-learn sin problemas.

## 8. Checklist de aprendizaje

- [ ] Crear y manipular DataFrames
- [ ] Filtrar y seleccionar datos
- [ ] Agrupar y agregar
- [ ] Manejar valores faltantes
- [ ] Preparar datos para entrenamiento
