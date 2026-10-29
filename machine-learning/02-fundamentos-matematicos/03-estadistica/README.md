# 3. Estadística para Machine Learning

## 1. ¿Qué es y para qué sirve?

La estadística permite describir datos, cuantificar incertidumbre y tomar decisiones basadas en evidencia. Es fundamental para validación, intervalos de confianza y pruebas de hipótesis en ML.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Se usa en train/test split, validación cruzada, métricas, análisis exploratorio y para entender sesgo/varianza. Es esencial para evaluar modelos correctamente.

## 3. Conceptos clave

- **Estadística descriptiva**: Resume datos con medidas de tendencia central, dispersión y forma.
- **Media**: $\bar{x}=\frac{1}{n}\sum x_i$
- **Mediana**: Valor central ordenado
- **Varianza muestral**: $s^2=\frac{1}{n-1}\sum (x_i-\bar{x})^2$
- **Desviación estándar**: $s=\sqrt{s^2}$
- **Estadística inferencial**: Generaliza a partir de muestra
- **Intervalo de confianza**: Rango con nivel de confianza para parámetro
- **Prueba de hipótesis**: Evalúa afirmaciones con evidencia
- **Correlación**: Relación lineal entre variables

## 4. Ejemplos de código en Python

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data[:, 0]
print(np.mean(X), np.median(X), np.std(X))
```

```python
from scipy import stats
import numpy as np

np.random.seed(42)
data = np.random.normal(loc=5, scale=1, size=30)
conf = stats.t.interval(0.95, len(data)-1, loc=np.mean(data), scale=stats.sem(data))
print(conf)
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Usar varianza poblacional en muestras. **Buena práctica**: Usar $n-1$ para muestras.
- **Error común**: Confundir correlación con causalidad. **Buena práctica**: Correlación no implica causalidad.
- **Error común**: Interpretar intervalo incorrectamente. **Buena práctica**: Entender significado de confianza.
- **Error común**: Ignorar outliers. **Buena práctica**: Visualizar y analizar valores extremos.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Diferencia entre media y mediana?  
   **Respuesta orientativa:** Media es promedio; mediana es valor central resistente a outliers.

2. **Pregunta:** ¿Por qué usar $n-1$ en varianza muestral?  
   **Respuesta orientativa:** Para corregir sesgo y obtener estimador insesgado de varianza poblacional.

3. **Pregunta:** ¿Qué es un intervalo de confianza del 95%?  
   **Respuesta orientativa:** Rango que, con procedimiento repetido, contiene el parámetro poblacional en ~95% de casos.

4. **Pregunta:** ¿Cuándo usar prueba t vs z?  
   **Respuesta orientativa:** t cuando varianza poblacional desconocida y muestra pequeña; z con varianza conocida o muestra grande.

5. **Pregunta:** ¿Por qué visualizar datos antes de calcular estadísticas?  
   **Respuesta orientativa:** Para detectar outliers, formas, asimetría que pueden engañar resúmenes numéricos.
