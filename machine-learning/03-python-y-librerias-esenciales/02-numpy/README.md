# 2. NumPy para Machine Learning

## 1. ¿Qué es y para qué sirve?

NumPy proporciona arreglos multidimensionales eficientes y operaciones vectorizadas. Es la base para pandas, scikit-learn y muchas librerías científicas.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Permite realizar operaciones matriciales rápidas, fundamentales para álgebra lineal, cálculos estadísticos y preparación de datos.

## 3. Conceptos clave

- **ndarray**: Arreglo N-dimensional eficiente.
- **Shape/dtype**: Dimensiones y tipo de datos.
- **Indexado y slicing**: Acceso a elementos.
- **Broadcasting**: Operaciones entre arreglos de formas compatibles.
- **Vectorización**: Operaciones sin bucles explícitos.
- **Funciones universales**: np.sin, np.exp, etc.
- **Álgebra lineal**: np.dot, np.linalg.

## 4. Ejemplos de código en Python

```python
import numpy as np
a = np.array([1,2,3,4])
print(a*2, a**2)
print(a.mean(), a.std())
```

```python
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A @ B)
print(np.linalg.det(A))
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Usar listas en lugar de arrays. **Buena práctica**: Usar np.array para cálculos numéricos.
- **Error común**: Copia vs vista. **Buena práctica**: Usar .copy() cuando se necesita copia independiente.
- **Error común**: Bucles lentos. **Buena práctica**: Vectorizar operaciones.
- **Error común**: Errores de broadcasting. **Buena práctica**: Verificar shapes.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Ventaja de ndarray sobre lista Python?  
   **Respuesta orientativa:** Más eficiente en memoria y operaciones vectorizadas más rápidas.

2. **Pregunta:** ¿Qué es broadcasting?  
   **Respuesta orientativa:** Regla para operar arreglos de diferentes formas expandiendo dimensiones compatibles.

3. **Pregunta:** ¿Diferencia entre * y @ en NumPy?  
   **Respuesta orientativa:** * es elemento a elemento; @ es producto matricial.

4. **Pregunta:** ¿Cuándo usar np.arange vs np.linspace?  
   **Respuesta orientativa:** arange por paso; linspace por número de puntos equiespaciados.

5. **Pregunta:** ¿Por qué es importante evitar bucles en NumPy?  
   **Respuesta orientativa:** Vectorización es mucho más eficiente y código más conciso.
