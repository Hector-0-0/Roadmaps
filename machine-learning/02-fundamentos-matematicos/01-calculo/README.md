# 1. Cálculo para Machine Learning

## 1. ¿Qué es y para qué sirve?

El cálculo permite entender cómo cambian las funciones y cómo optimizar parámetros. En Machine Learning es fundamental para comprender el descenso por gradiente, la regla de la cadena y la minimización de funciones de pérdida.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

El cálculo se conecta con optimización en regresión, entrenamiento de redes neuronales y regularización. Es la base para entender cómo los algoritmos ajustan pesos mediante derivadas.

## 3. Conceptos clave

- **Derivada**: Tasa de cambio instantánea. Para $f(x)$, $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$.
- **Derivadas parciales**: Para $f(x,y)$, $\frac{\partial f}{\partial x}$ mide cambio manteniendo otras variables constantes.
- **Regla de la cadena**: Si $z=g(f(x))$, entonces $\frac{dz}{dx}=g'(f(x))f'(x)$.
- **Gradiente**: Vector de derivadas parciales $\nabla f(x,y)=\left[\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right]^T$ indica dirección de máximo ascenso.
- **Jacobiano**: Matriz de derivadas parciales para funciones vectoriales.
- **Hessiano**: Matriz de segundas derivadas parciales $H_{ij}=\frac{\partial^2 f}{\partial x_i \partial x_j}$, útil para análisis de curvatura.

## 4. Ejemplos de código en Python

```python
import numpy as np

def f(x):
    return x**2 + 3*x + 1

def df(x):
    return 2*x + 3

x = 2.0
print(f(x))
print(df(x))
```

```python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def f(x, y):
    return x**2 + y**2

def grad_f(x, y):
    return np.array([2*x, 2*y])

x, y = 1.0, 1.0
lr = 0.1
history = []
for i in range(20):
    g = grad_f(x, y)
    x, y = x - lr*g[0], y - lr*g[1]
    history.append(f(x,y))
print(history[0], history[-1])
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Aplicar regla de cadena incorrectamente. **Buena práctica**: Descomponer funciones paso a paso.
- **Error común**: Usar learning rate muy grande. **Buena práctica**: Probar valores pequeños y observar convergencia.
- **Error común**: Olvidar que gradiente es vectorial. **Buena práctica**: Actualizar todas las variables simultáneamente.
- **Error común**: Confundir ascenso/descenso. **Buena práctica**: Usar $-\nabla f$ para minimizar.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Qué indica el gradiente de una función?  
   **Respuesta orientativa:** Indica la dirección de máximo ascenso; para minimizar se usa el negativo del gradiente.

2. **Pregunta:** Aplica regla de la cadena a $h(x)=\sin(x^2)$. ¿Cuál es $h'(x)$?  
   **Respuesta orientativa:** $h'(x)=\cos(x^2)\cdot 2x$.

3. **Pregunta:** ¿Cuál es la diferencia entre derivada parcial y derivada total?  
   **Respuesta orientativa:** Parcial considera otras variables constantes; total considera todas las dependencias.

4. **Pregunta:** ¿Por qué usar descenso por gradiente en lugar de búsqueda aleatoria?  
   **Respuesta orientativa:** Usa información direccional del gradiente para converger más eficientemente.

5. **Pregunta:** ¿Qué información proporciona el Hessiano?  
   **Respuesta orientativa:** Proporciona información sobre curvatura, útil para entender convergencia y optimizadores de segundo orden.
