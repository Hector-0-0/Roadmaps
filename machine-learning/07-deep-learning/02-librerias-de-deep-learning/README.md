# 2. Librerías de Deep Learning

## 1. ¿Qué es y para qué sirve?

Esta sección presenta las principales librerías para Deep Learning: TensorFlow/Keras y PyTorch. Permite elegir herramientas adecuadas según el proyecto.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Conocer ambas librerías es útil para entender diferentes ecosistemas y aplicar redes neuronales en problemas reales.

## 3. Conceptos clave

- **TensorFlow/Keras**: Framework de alto nivel para construir y entrenar redes neuronales.
- **PyTorch**: Framework con enfoque dinámico, muy usado en investigación.
- **Diferencias**: Paradigmas, debugging, ecosistema.
- **Cuándo usar cada uno**: Consideraciones prácticas.

## 4. Ejemplos de código en Python

```python
# concepto general
import numpy as np
print(np.array([1,2,3]))
```

```python
# flujo básico
from sklearn.datasets import load_iris
X = load_iris().data
print(X.shape)
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Elegir sin entender necesidades. **Buena práctica**: Probar ambos conceptos.
- **Error común**: Ignorar GPU. **Buena práctica**: Considerar recursos disponibles.
- **Error común**: Código poco reproducible. **Buena práctica**: Fijar semillas.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Diferencia principal entre Keras y PyTorch?  
   **Respuesta orientativa:** Keras más declarativo/alto nivel; PyTorch más imperativo y flexible.

2. **Pregunta:** ¿Cuándo usar TensorFlow?  
   **Respuesta orientativa:** Para despliegue en producción con ecosistema completo.

3. **Pregunta:** ¿Cuándo usar PyTorch?  
   **Respuesta orientativa:** Para investigación, prototipado rápido y debugging intuitivo.

4. **Pregunta:** ¿Qué son tensores?  
   **Respuesta orientativa:** Arreglos multidimensionales, equivalentes a arrays de NumPy con soporte GPU.

5. **Pregunta:** ¿Importancia de reproducibilidad?  
   **Respuesta orientativa:** Fundamental para comparar experimentos correctamente.
'''
cat > /home/hector0-0/Documents/Roadmaps/machine-learning/07-deep-learning/02-librerias-de-deep-learning/practica.md << 'EOF'
# Práctica - Librerías de Deep Learning

## Nivel básico

1. **Comparación**
   Enunciado: Compara TensorFlow/Keras y PyTorch en 5 aspectos con tabla.
   Pista: Incluye sintaxis, debugging, despliegue, curva aprendizaje.
   Criterio verificable: Tabla completa con diferencias correctas.

2. **Tensores conceptuales**
   Enunciado: Explica qué son tensores y relación con NumPy arrays.
   Pista: Menciona dimensiones, operaciones, GPU.
   Criterio verificable: Explicación correcta con ejemplos.

3. **Entorno**
   Enunciado: Verifica instalación de bibliotecas disponibles con imports.
   Pista: Usa try/except para verificar disponibilidad.
   Criterio verificable: Verificación ejecutable sin errores.

## Nivel intermedio

4. **Flujo general**
   Enunciado: Describe flujo típico: datos, modelo, pérdida, optimizador, entrenamiento.
   Pista: Aplica a ambos frameworks conceptualmente.
   Criterio verificable: Flujo completo documentado.

5. **Casos de uso**
   Enunciado: Propón framework para 3 casos diferentes justificando elección.
   Pista: Considera producción vs investigación.
   Criterio verificable: Justificación correcta por caso.

6. **Recursos**
   Enunciado: Identifica recursos oficiales de ambos frameworks.
   Pista: Usa URLs oficiales verificables.
   Criterio verificable: Lista con recursos correctos.

## Nivel desafío

7. **Decisión justificada**
   Enunciado: Para proyecto específico elige framework con análisis completo.
   Pista: Incluye equipo, despliegue, tiempo, recursos.
   Criterio verificable: Análisis con criterios objetivos.

8. **Plan de aprendizaje**
   Enunciado: Crea plan para aprender uno de los frameworks con ejercicios.
   Pista: Secuencial y práctico.
   Criterio verificable: Plan con pasos concretos y medibles.
