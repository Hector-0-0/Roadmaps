# 4. Aprendizaje no supervisado

## 1. ¿Qué es y para qué sirve?

El aprendizaje no supervisado encuentra patrones en datos sin etiquetas, como agrupamiento y reducción dimensional.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Es útil para exploración, segmentación y reducción de dimensionalidad antes de modelado supervisado.

## 3. Conceptos clave

- **Clustering**: Agrupamiento de datos similares.
- **PCA**: Reducción dimensional preservando varianza.
- **Tipos de clustering**: K-means, jerárquico, etc.
- **Métricas**: Silhouette score.
- **Aplicaciones**: Segmentación, compresión.

## 4. Ejemplos de código en Python

```python
# clustering
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
X = load_iris().data
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
print(kmeans.fit_predict(X)[:10])
```

```python
# pca
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
X = load_iris().data
pca = PCA(n_components=2)
X2 = pca.fit_transform(X)
print(X2.shape)
```

## 5. Errores comunes y buenas prácticas

- **Error común**: No escalar datos. **Buena práctica**: Estandarizar antes de clustering/PCA.
- **Error común**: Elegir k arbitrariamente. **Buena práctica**: Usar elbow method.
- **Error común**: Interpretar mal. **Buena práctica**: Validar con métricas.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Diferencia entre supervisado y no supervisado?  
   **Respuesta orientativa:** Supervisado usa etiquetas; no supervisado busca patrones sin etiquetas.

2. **Pregunta:** ¿Para qué usar PCA?  
   **Respuesta orientativa:** Reducir dimensionalidad manteniendo varianza.

3. **Pregunta:** ¿Cuándo usar K-means?  
   **Respuesta orientativa:** Para clustering con clusters esféricos y número conocido.

4. **Pregunta:** ¿Por qué escalar antes de clustering?  
   **Respuesta orientativa:** Distancias son sensibles a escala de variables.

5. **Pregunta:** ¿Qué es silhouette score?  
   **Respuesta orientativa:** Métrica para evaluar calidad de clustering.
