# ML Engineer vs AI Engineer

## Objetivo

Distinguir claramente las responsabilidades, habilidades y enfoques del Machine Learning Engineer y del AI Engineer.

## 1. Comparación general

| Aspecto | Machine Learning Engineer | AI Engineer |
| --- | --- | --- |
| Enfoque | Construir y desplegar modelos de ML clásicos y basados en datos. | Integrar sistemas de IA, incluyendo LLMs, agentes y APIs de IA. |
| Datos | Trabaja con datos estructurados y no estructurados para entrenar modelos. | Trabaja con prompts, contexto, herramientas y datos para aplicaciones con IA generativa. |
| Herramientas principales | scikit-learn, NumPy, pandas, PyTorch, ML pipelines. | LLMs, frameworks de agentes, RAG, APIs, vector stores. |
| Despliegue | Modelos propios entrenados o afinados, APIs de inferencia. | Aplicaciones que consumen modelos preentrenados o combinan múltiples componentes. |
| Matemáticas | Fuerte énfasis en estadísticas, álgebra lineal y optimización. | Importante, pero con mayor énfasis en sistemas, prompts y orquestación. |

## 2. Ejemplo práctico

```python
# Enfoque ML Engineer: entrenar modelo propio con Iris
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=123)
clf = RandomForestClassifier(n_estimators=100, random_state=123)
clf.fit(X_train, y_train)
print(classification_report(y_test, clf.predict(X_test), target_names=iris.target_names))
```

```text
# Enfoque AI Engineer: patrón típico de aplicación con LLM
# 1. Recibir consulta del usuario
# 2. Recuperar contexto relevante (RAG)
# 3. Construir prompt con instrucciones y contexto
# 4. Llamar a API del LLM
# 5. Validar y retornar respuesta al usuario
```

## 3. Cuándo elegir cada camino

- Elige Machine Learning Engineer si te interesa entender algoritmos, entrenamiento y optimización de modelos.
- Elige AI Engineer si te interesa construir aplicaciones con modelos existentes, agentes y sistemas con IA generativa.

## 4. Puntos en común

- Sólidos conocimientos de Python.
- Comprensión de datos y evaluación.
- Enfoque en resolver problemas reales.
- Importancia de seguridad, costos y monitoreo.

## 5. Autoevaluación

1. ¿Qué enfoque prioriza el entrenamiento de modelos propios?
2. ¿Qué es RAG y por qué es relevante para AI Engineers?
3. ¿Qué rol requiere mayor conocimiento de despliegue de modelos propios?
4. ¿Pueden solaparse ambos roles? Justifica.
5. ¿Qué habilidades compartidas son fundamentales para ambos?

**Respuestas esperadas:**
1. Machine Learning Engineer, con énfasis en datos, algoritmos y optimización.
2. Retrieval Augmented Generation: combina recuperación de información con generación para dar respuestas con contexto relevante.
3. Machine Learning Engineer, especialmente al llevar modelos a producción.
4. Sí, hay solapamiento. En equipos pequeños un mismo profesional puede cubrir ambos aspectos según necesidades.
5. Python, comprensión de datos, evaluación, pensamiento crítico y capacidad para resolver problemas.
