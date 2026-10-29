# Práctica - Álgebra lineal para Machine Learning

## Nivel básico

1. **Vectores**
   Enunciado: Crea dos vectores en R^3, calcula producto escalar, suma, resta y norma euclidiana.
   Pista: Usa numpy arrays. Normas con np.linalg.norm.
   Criterio verificable: Producto escalar numérico correcto, normas calculadas correctamente.

2. **Matrices**
   Enunciado: Crea dos matrices 2x2, multiplica con @, calcula transpuesta, determinante e inversa.
   Pista: Verifica dimensiones antes de multiplicar.
   Criterio verificable: Producto matricial correcto, det e inv calculados con numpy.

3. **Sistema lineal**
   Enunciado: Resuelve $\begin{bmatrix}2&1\\1&3\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}=\begin{bmatrix}5\\10\end{bmatrix}$ con np.linalg.solve.
   Pista: Compara con multiplicación A*x para verificar.
   Criterio verificable: Solución numérica correcta verificada con A@x == b.

## Nivel intermedio

4. **Autovalores y autovectores**
   Enunciado: Calcula autovalores y autovectores de una matriz simétrica. Verifica $Av = \lambda v$.
   Pista: Usa np.linalg.eig. Verifica con producto matricial.
   Criterio verificable: Verificación numérica $||Av - \lambda v|| < 1e-8$ para al menos un par.

5. **SVD básico**
   Enunciado: Aplica SVD a matriz 3x2, reconstruye con top 1 y top 2 valores singulares.
   Pista: Usa np.linalg.svd. Calcula error de reconstrucción con Frobenius.
   Criterio verificable: Reconstrucción con rank completo igual a original (error numérico pequeño), aproximación con rank menor calculada.

6. **Proyección**
   Enunciado: Proyecta vector v sobre vector u calculando $proj_u v = \frac{v^T u}{u^T u}u$.
   Pista: Implementa fórmula y verifica geométricamente.
   Criterio verificable: Proyección correcta con valores numéricos verificables.

## Nivel desafío

7. **PCA desde cero**
   Enunciado: Con dataset Iris, centra datos, calcula covarianza, autovalores/autovectores, proyecta a 2D.
   Pista: Usa solo numpy. Ordena por autovalor descendente.
   Criterio verificable: Proyección 2D generada, varianza explicada calculada correctamente.

8. **SVD para compresión**
   Enunciado: Genera matriz aleatoria, comprime con SVD manteniendo 50% energía (suma valores singulares) y calcula error.
   Pista: Calcula energía acumulada = suma(s[0:k])/suma(s).
   Criterio verificable: k seleccionado correctamente, error de reconstrucción calculado numéricamente.
