# 5. Aprendizaje por refuerzo

## 1. ¿Qué es y para qué sirve?

El aprendizaje por refuerzo aprende mediante interacción con ambiente, maximizando recompensa acumulada.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Es relevante para agentes, robótica y toma de decisiones secuenciales.

## 3. Conceptos clave

- **Agente y ambiente**: Interacción.
- **Estado, acción, recompensa**: Elementos básicos.
- **Política**: Mapa estado-acción.
- **Q-learning**: Aprendizaje de valores Q.
- **Exploración vs explotación**: Trade-off.

## 4. Ejemplos de código en Python

```python
# q table simple
import numpy as np
q = np.zeros((4,2))
q[0,1] = 1.0
print(q)
```

```python
# epsilon greedy
import random
epsilon = 0.1
if random.random() < epsilon:
    action = 0
else:
    action = 1
print(action)
```

## 5. Errores comunes y buenas prácticas

- **Error común**: No balancear exploración/explotación. **Buena práctica**: Usar epsilon decreciente.
- **Error común**: Recompensas mal diseñadas. **Buena práctica**: Diseñar recompensas cuidadosas.
- **Error común**: Convergencia lenta. **Buena práctica**: Ajustar hiperparámetros.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Qué es aprendizaje por refuerzo?  
   **Respuesta orientativa:** Aprendizaje por prueba y error maximizando recompensa.

2. **Pregunta:** ¿Diferencia con supervisado?  
   **Respuesta orientativa:** No hay etiquetas directas, hay recompensas.

3. **Pregunta:** ¿Qué es Q-learning?  
   **Respuesta orientativa:** Algoritmo off-policy para aprender función Q.

4. **Pregunta:** ¿Exploración vs explotación?  
   **Respuesta orientativa:** Probar acciones nuevas vs usar conocidas.

5. **Pregunta:** ¿Aplicaciones?  
   **Respuesta orientativa:** Juegos, robótica, recomendadores, trading.
