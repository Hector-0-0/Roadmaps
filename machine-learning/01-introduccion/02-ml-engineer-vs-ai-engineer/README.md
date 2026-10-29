# 2. ML Engineer vs AI Engineer

## 1. ¿Qué es y para qué sirve?

Comparar ML Engineer y AI Engineer sirve para entender diferencias de enfoque, herramientas y responsabilidades. Esto ayuda a elegir el camino de aprendizaje más acorde a objetivos concretos.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Conocer ambos roles permite entender cuándo conviene entrenar un modelo propio (ML Engineer) y cuándo conviene integrar modelos existentes en aplicaciones (AI Engineer). Ambos requieren fundamentos sólidos de datos y evaluación cubiertos en este roadmap.

## 3. Conceptos clave

- **Modelo propio**: Algoritmo entrenado o afinado con datos propios para un problema específico.
- **Modelo preentrenado**: Modelo ya entrenado por terceros, usado vía API o localmente.
- **RAG (Retrieval Augmented Generation)**: Técnica que combina recuperación de información con un modelo generativo para dar respuestas con contexto.
- **Pipeline de ML**: Enfoque centrado en datos, entrenamiento, validación y despliegue de modelos.
- **Aplicación con IA**: Enfoque centrado en orquestación, prompts, herramientas y experiencia de usuario.
- **Solapamiento**: Muchos equipos requieren habilidades de ambos perfiles.

## 4. Ejemplos de código en Python

```python
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=123, stratify=iris.target)
clf = RandomForestClassifier(n_estimators=100, random_state=123)
clf.fit(X_train, y_train)
print(classification_report(y_test, clf.predict(X_test), target_names=iris.target_names))
```

```text
Enfoque AI Engineer (patrón conceptual):
1. Recibir consulta
2. Recuperar documentos relevantes
3. Construir prompt con contexto
4. Enviar a LLM
5. Filtrar y retornar respuesta
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Pensar que son roles idénticos. **Buena práctica**: Entender enfoque (entrenar vs integrar).
- **Error común**: Usar LLM para todo sin evaluar. **Buena práctica**: Probar solución con ML clásico primero si es más simple y eficiente.
- **Error común**: Ignorar costos. **Buena práctica**: Considerar costo de inferencia, latencia y mantenimiento.
- **Error común**: Falta de evaluación. **Buena práctica**: Definir métrica objetiva para ambos enfoques.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Qué prioriza un ML Engineer frente a un AI Engineer?  
   **Respuesta orientativa:** El ML Engineer prioriza entrenar, optimizar y desplegar modelos propios; el AI Engineer prioriza orquestar e integrar modelos existentes.

2. **Pregunta:** ¿Qué es RAG y para qué se usa?  
   **Respuesta orientativa:** Retrieval Augmented Generation combina búsqueda de documentos relevantes con un modelo generativo para responder con información contextual.

3. **Pregunta:** ¿Cuándo es mejor usar un modelo entrenado desde cero?  
   **Respuesta orientativa:** Cuando hay datos propios suficientes, problema muy específico, o restricciones de costos/privacidad que justifican entrenar.

4. **Pregunta:** ¿Qué habilidades comparten ambos roles?  
   **Respuesta orientativa:** Python, comprensión de datos, evaluación con métricas, pensamiento crítico y enfoque a resolver problemas.

5. **Pregunta:** ¿Por qué el solapamiento entre roles es común?  
   **Respuesta orientativa:** En la práctica se necesitan ambos enfoques; proyectos reales suelen combinar entrenamiento, integración, despliegue y monitoreo.
