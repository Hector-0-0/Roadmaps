# Algebra Lineal

## Objetivo

Desarrollar los fundamentos matemáticos necesarios para comprender algoritmos de Machine Learning.

## 1. Introducción

Los fundamentos matemáticos permiten entender cómo funcionan los algoritmos, la optimización y la generalización en Machine Learning.

## 2. Conceptos clave

En este tema se estudian los conceptos fundamentales con enfoque práctico y aplicación directa a Machine Learning.

## 3. Ejemplos con Python

```python
import numpy as np
x = np.array([1.0, 2.0, 3.0, 4.0])
print(np.mean(x))
print(np.std(x))
```

```python
import numpy as np
A = np.array([[1, 2],[3, 4]])
print(np.linalg.det(A))
```

## 4. Aplicación a Machine Learning

Estos conceptos se aplican en regresión, descenso por gradiente, regularización, reducción dimensional y evaluación de modelos.

## 5. Errores comunes

- Confundir escalares, vectores, matrices y tensores.
- Aplicar fórmulas sin interpretar su significado geométrico.
- Olvidar supuestos estadísticos al hacer inferencias.

## 6. Autoevaluación

1. ¿Por qué son importantes las matemáticas en Machine Learning?
2. ¿Qué papel tiene la optimización en el entrenamiento de modelos?
3. ¿Cuál es la diferencia entre estadística descriptiva e inferencial?
4. ¿Por qué es importante entender álgebra lineal para trabajar con datos?
5. ¿Cómo se relaciona la probabilidad con la incertidumbre en predicciones?

**Respuestas esperadas:**
1. Permiten entender algoritmos, seleccionar modelos, optimizar y interpretar resultados correctamente.
2. Busca minimizar una función de pérdida ajustando parámetros mediante técnicas como descenso por gradiente.
3. La descriptiva resume datos observados; la inferencial generaliza conclusiones a partir de una muestra.
4. Muchos datos se representan como vectores y matrices, y operaciones lineales son fundamentales.
5. Permite cuantificar incertidumbre, usar modelos probabilísticos y aplicar teorema de Bayes.
