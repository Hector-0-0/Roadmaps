# 2. Álgebra lineal para Machine Learning

## 1. ¿Qué es y para qué sirve?

El álgebra lineal permite representar y manipular datos como vectores, matrices y tensores. Es esencial para comprender regresión lineal, PCA, SVD, embeddings y redes neuronales.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Casi todos los algoritmos de ML operan con operaciones matriciales. PCA usa autovalores/autovectores, regresión usa sistemas lineales y deep learning usa multiplicación tensorial.

## 3. Conceptos clave

- **Escalar**: Un solo número $x \in \mathbb{R}$.
- **Vector**: Arreglo ordenado $v \in \mathbb{R}^n$.
- **Matriz**: Arreglo bidimensional $A \in \mathbb{R}^{m\times n}$.
- **Tensor**: Arreglo multidimensional general.
- **Producto escalar**: $v^T w = \sum v_i w_i$.
- **Producto matricial**: $(AB)_{ij}=\sum_k A_{ik}B_{kj}$.
- **Determinante**: $\det(A)$ mide invertibilidad.
- **Matriz inversa**: $A^{-1}$ tal que $AA^{-1}=I$.
- **Autovalores/autovectores**: $Av = \lambda v$.
- **Diagonalización**: $A = Q\Lambda Q^{-1}$.
- **SVD**: $A = U\Sigma V^T$ con valores singulares.

## 4. Ejemplos de código en Python

```python
import numpy as np

v = np.array([1, 2, 3])
w = np.array([4, 5, 6])
print(np.dot(v, w))
print(np.linalg.norm(v))
```

```python
import numpy as np

A = np.array([[1, 2],[3, 4]])
print(np.linalg.det(A))
print(np.linalg.inv(A))
u, s, vh = np.linalg.svd(A)
print(s)
A_rec = (u[:, :2] @ np.diag(s) @ vh[:2, :])
print(A_rec)
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Multiplicar matrices con dimensiones incorrectas. **Buena práctica**: Verificar formas con `.shape`.
- **Error común**: Usar inversa cuando hay solución numérica mejor. **Buena práctica**: Considerar `np.linalg.solve` o pseudoinversa.
- **Error común**: Confundir producto elemento a elemento con producto matricial. **Buena práctica**: Usar `*` vs `@`.
- **Error común**: Olvidar centrado para PCA. **Buena práctica**: Estandarizar/centrar antes de SVD.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Cuál es la diferencia entre producto escalar y producto matricial?  
   **Respuesta orientativa:** Producto escalar da un escalar entre vectores; producto matricial combina filas/columnas para obtener nueva matriz.

2. **Pregunta:** ¿Cuándo una matriz es invertible?  
   **Respuesta orientativa:** Cuando es cuadrada, determinante distinto de cero y columnas linealmente independientes.

3. **Pregunta:** ¿Qué representan autovalores y autovectores?  
   **Respuesta orientativa:** Direcciones que solo se escalan ($Av=\lambda v$) bajo transformación lineal.

4. **Pregunta:** ¿Para qué sirve la SVD en ML?  
   **Respuesta orientativa:** Para reducción dimensional, compresión, recomendaciones y aproximaciones de rango bajo.

5. **Pregunta:** ¿Por qué verificar dimensiones al multiplicar matrices?  
   **Respuesta orientativa:** $(m\times n)(n\times p)$ requiere que columnas de primera igualen filas de segunda.
