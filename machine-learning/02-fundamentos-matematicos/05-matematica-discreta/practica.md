# Práctica - Matemática discreta para Machine Learning

## Nivel básico

1. **Conjuntos**
   Enunciado: Dados A={1,2,3,4}, B={3,4,5,6} calcula unión, intersección, diferencia A-B y diferencia simétrica.
   Pista: Usa la clase set de Python con operadores |, &, -, ^ o métodos union/intersection/difference/symmetric_difference.
   Criterio verificable: Los 4 resultados son correctos (union {1..6}, intersección {3,4}, A-B {1,2}, simétrica {1,2,5,6}).

2. **Combinatoria**
   Enunciado: Usa itertools.permutations y itertools.combinations para obtener P(4,2) y C(4,2) mostrando las listas generadas.
   Pista: Recuerda que permutations importa el orden y combinations no lo importa, por lo que los conteos difieren.
   Criterio verificable: Se obtienen 12 permutaciones y 6 combinaciones, con conteos numéricos correctos.

3. **Conteo manual**
   Enunciado: Calcula C(10,3) usando la fórmula $C(n,r)=\frac{n!}{r!(n-r)!}$ con Python y verifica con math.comb o itertools.combinations.
   Pista: Usa math.comb o math.factorial para calcular la fórmula y compara con el conteo real de combinaciones.
   Criterio verificable: Resultado numérico es 120 y coincide con la longitud de la lista de combinaciones.

## Nivel intermedio

4. **Grafo básico**
   Enunciado: Crea grafo no dirigido, implementa BFS desde un nodo mostrando orden de visita.
   Pista: Usa cola con índice o collections.deque.
   Criterio verificable: BFS retorna nodos visitados en orden correcto.

5. **DFS**
   Enunciado: Implementa DFS recursivo para el mismo grafo usando un conjunto de visitados para evitar ciclos.
   Pista: Define la función recursiva que marca como visitado y recorre vecinos, controlando el caso de nodos ya visitados.
   Criterio verificable: DFS recorre todos los nodos alcanzables, no repite nodos y se documentan diferencias con BFS.

6. **Árbol de decisión simple**
   Enunciado: Modela un árbol binario simple con diccionarios (valor, izquierda, derecha) y realiza recorrido preorden con DFS recursivo.
   Pista: Usa recursión definiendo caso base cuando el nodo es None y visitando raíz, izquierda, derecha en ese orden.
   Criterio verificable: El recorrido preorden produce la secuencia correcta para el árbol definido.

## Nivel desafío

7. **Subconjuntos**
   Enunciado: Genera todos los subconjuntos de {a,b,c} usando recursión o itertools.chain, incluyendo el conjunto vacío.
   Pista: Usa el principio de que para cada elemento puedes incluirlo o excluirlo, resultando en 2^n subconjuntos totales.
   Criterio verificable: Se generan exactamente 8 subconjuntos incluyendo el vacío y todos son distintos.

8. **Aplicación a ML**
   Enunciado: Cuenta espacios de búsqueda para grid de hiperparámetros simple y analiza complejidad.
   Pista: Si 3 params con 4 valores cada uno: 4^3=64 combinaciones.
   Criterio verificable: Conteo correcto con notación O y explicación de crecimiento exponencial.
