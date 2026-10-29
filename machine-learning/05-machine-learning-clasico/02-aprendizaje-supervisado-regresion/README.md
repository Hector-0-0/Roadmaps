# 02 Aprendizaje Supervisado Regresion

## 1. ¿Qué es y para qué sirve?

Grupo temático que agrupa algoritmos relacionados con 02 aprendizaje supervisado regresion para resolver problemas específicos en Machine Learning.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Este grupo conecta con fundamentos matemáticos, preparación de datos y evaluación, permitiendo aplicar algoritmos apropiados según el tipo de problema.

## 3. Conceptos clave

- **Algoritmos del grupo**: Cada subtema cubre un algoritmo con fundamentos y aplicación.
- **Cuándo usar**: Criterios para elegir el algoritmo adecuado.
- **Ventajas y limitaciones**: Trade-offs de cada enfoque.
- **Métricas apropiadas**: Evaluación correcta por tipo de problema.
- **Pipeline correcto**: Integración sin fuga de datos.

## 4. Ejemplos de código en Python

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target)
print(X_train.shape, X_test.shape)
```

```python
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
X = load_wine().data
X_s = StandardScaler().fit_transform(X)
print(X_s.mean(axis=0)[:3])
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Elegir algoritmo incorrecto. **Buena práctica**: Analizar problema primero.
- **Error común**: Fuga de datos. **Buena práctica**: Usar Pipeline.
- **Error común**: Métricas incorrectas. **Buena práctica**: Elegir según tipo de problema.
- **Error común**: Sobreajuste. **Buena práctica**: Validación cruzada y regularización.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Cuándo usar algoritmos de este grupo?  
   **Respuesta orientativa:** Según tipo de problema y características de los datos.

2. **Pregunta:** ¿Qué subtemas cubrir?  
   **Respuesta orientativa:** Revisar subcarpetas con sus fundamentos y aplicaciones.

3. **Pregunta:** ¿Cómo validar correctamente?  
   **Respuesta orientativa:** Con train/test o validación cruzada usando métricas apropiadas.

4. **Pregunta:** ¿Por qué usar Pipeline?  
   **Respuesta orientativa:** Para evitar fuga de datos y garantizar reproducibilidad.

5. **Pregunta:** ¿Cómo comparar algoritmos?  
   **Respuesta orientativa:** Con misma validación cruzada y métricas objetivas.
