# Práctica - Matemática discreta para Machine Learning

## Nivel básico

1. **Conjuntos**
   Enunciado: Dados A={1,2,3,4}, B={3,4,5,6} calcula unión, intersección, diferencia A-B y simétrica.
   Pista: Usa sets en Python.
   Criterio verificable: Los 4 resultados correctos con tipos set/list apropiados.

2. **Combinatoria**
   Enunciado: Calcula permutaciones y combinaciones de 4 elementos tomados de 2 con itertools.
   Pista: Usa permutations y combinations.
   Criterio verificable: Conteos correctos (P(4,2)=12, C(4,2)=6) y listas generadas.

3. **Conteo manual**
   Enunciado: ¿Cuántas formas de elegir 3 características de 10? Calcula y verifica con fórmula.
   Pista: $C(10,3)=120$.
   Criterio verificable: Resultado numérico 120 con cálculo correcto.

## Nivel intermedio

4. **Grafo básico**
   Enunciado: Crea grafo no dirigido, implementa BFS desde un nodo mostrando orden de visita.
   Pista: Usa cola con índice o collections.deque.
   Criterio verificable: BFS retorna nodos visitados en orden correcto.

5. **DFS**
   Enunciado: Implementa DFS recursivo para el mismo grafo y compara con BFS.
   Pista: Usa set para visitados.
   Criterio verificable: DFS funciona, diferencias con BFS documentadas.

6. **Árbol de decisión simple**
   Enunciado: Modela árbol binario simple con diccionarios y recorrelo con DFS.
   Pista: Nodo con valor, izquierda, derecha.
   Criterio verificable: Recorrido inorden/preorden funciona correctamente.

## Nivel desafío

7. **Subconjuntos**
   Enunciado: Genera todos los subconjuntos de {a,b,c} usando itertools o recursión.
   Pista: Total 2^3=8.
   Criterio verificable: 8 subconjuntos generados correctamente incluyendo vacío.

8. **Aplicación a ML**
   Enunciado: Cuenta espacios de búsqueda para grid de hiperparámetros simple y analiza complejidad.
   Pista: Si 3 params con 4 valores cada uno: 4^3=64 combinaciones.
   Criterio verificable: Conteo correcto con notación O y explicación de crecimiento exponencial.
