# 5. Matemática discreta para Machine Learning

## 1. ¿Qué es y para qué sirve?

La matemática discreta estudia estructuras finitas o contables: conjuntos, lógica, combinatoria y grafos. Es útil para conteo, complejidad, árboles de decisión, grafos en ML y razonamiento.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Apoya comprensión de árboles de decisión, espacio de búsqueda, conteo de features, teoría de grafos en embeddings y análisis de algoritmos.

## 3. Conceptos clave

- **Conjuntos**: Colección de elementos $A \cup B, A \cap B, A^c$.
- **Lógica proposicional**: AND, OR, NOT, implicación.
- **Combinatoria**: Permutaciones $P(n,r)=\frac{n!}{(n-r)!}$, combinaciones $C(n,r)=\frac{n!}{r!(n-r)!}$.
- **Principio de conteo**: Regla multiplicativa.
- **Grafos**: $G=(V,E)$ con vértices y aristas.
- **Caminos y conectividad**: Conceptos básicos.
- **Recursión**: Definiciones recursivas.
- **Complejidad**: Notación básica $O(n)$.

## 4. Ejemplos de código en Python

```python
from itertools import combinations, permutations
items = ['a','b','c']
print(list(combinations(items, 2)))
print(list(permutations(items, 2)))
```

```python
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bfs(grafo, inicio):
    visitados = set([inicio])
    cola = [inicio]
    i = 0
    while i < len(cola):
        actual = cola[i]
        i += 1
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return visitados

print(bfs(grafo, 'A'))
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Confundir permutación y combinación. **Buena práctica**: Preguntar si importa el orden.
- **Error común**: Doble conteo. **Buena práctica**: Usar principio correcto o diagramas.
- **Error común**: Ignorar casos base. **Buena práctica**: Definir base en recursión.
- **Error común**: Representar grafos mal. **Buena práctica**: Elegir estructura adecuada.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Diferencia entre permutación y combinación?  
   **Respuesta orientativa:** Permutación importa orden; combinación no importa orden.

2. **Pregunta:** Calcula $C(5,2)$  
   **Respuesta orientativa:** $10$.

3. **Pregunta:** ¿Qué es un grafo no dirigido?  
   **Respuesta orientativa:** Grafo donde aristas no tienen dirección, $A-B$ significa conexión bidireccional.

4. **Pregunta:** ¿Para qué usar BFS?  
   **Respuesta orientativa:** Para encontrar camino más corto en grafos no ponderados.

5. **Pregunta:** ¿Aplicación de combinatoria en ML?  
   **Respuesta orientativa:** Conteo de características, espacios de hiperparámetros, validación cruzada.
