# 4. Probabilidad para Machine Learning

## 1. ¿Qué es y para qué sirve?

La probabilidad cuantifica incertidumbre. Es fundamental para modelos probabilísticos, clasificación con probabilidades, teorema de Bayes, Naive Bayes y toma de decisiones bajo incertidumbre.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Se usa en clasificación probabilística, evaluación con métricas probabilísticas, regularización bayesiana y en comprensión de ruido en datos.

## 3. Conceptos clave

- **Espacio muestral**: Conjunto de resultados posibles $\Omega$.
- **Probabilidad**: $P(A)\in[0,1]$, $P(\Omega)=1$.
- **Independencia**: $P(A\cap B)=P(A)P(B)$.
- **Condicional**: $P(A|B)=\frac{P(A\cap B)}{P(B)}$
- **Teorema de Bayes**: $P(A|B)=\frac{P(B|A)P(A)}{P(B)}$
- **Variable aleatoria**: Función de $\Omega$ a valores reales.
- **PDF/PMF**: Función de densidad/probabilidad.
- **Distribuciones**: Bernoulli, Binomial, Normal, Poisson.
- **Esperanza**: $E[X]=\sum x P(x)$ o integral
- **Varianza**: $Var(X)=E[(X-E[X])^2]$

## 4. Ejemplos de código en Python

```python
# Teorema de Bayes numérico
P_enfermo = 0.01
P_pos_enfermo = 0.99
P_pos_sano = 0.05
P_pos = P_pos_enfermo*P_enfermo + P_pos_sano*(1-P_enfermo)
P_enfermo_pos = (P_pos_enfermo*P_enfermo)/P_pos
print(P_enfermo_pos)
```

```python
import numpy as np
from scipy import stats

np.random.seed(42)
x = np.random.normal(0, 1, 10000)
print(np.mean(x), np.std(x))
print(stats.norm.cdf(1.96), stats.norm.cdf(-1.96))
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Confundir $P(A|B)$ con $P(B|A)$. **Buena práctica**: Aplicar Bayes explícitamente.
- **Error común**: Asumir independencia sin justificar. **Buena práctica**: Verificar supuestos.
- **Error común**: Interpretar probabilidad frecuentemente vs bayesiana. **Buena práctica**: Conocer ambos enfoques.
- **Error común**: Ignorar probabilidades a priori. **Buena práctica**: Considerar $P(A)$ en Bayes.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** Enuncia teorema de Bayes y explica sus términos.  
   **Respuesta orientativa:** $P(H|E)=\frac{P(E|H)P(H)}{P(E)}$ donde $P(H)$ priori, $P(E|H)$ verosimilitud, $P(E)$ evidencia.

2. **Pregunta:** ¿Diferencia entre variable aleatoria discreta y continua?  
   **Respuesta orientativa:** Discreta toma valores contables (PMF); continua valores en intervalo (PDF).

3. **Pregunta:** ¿Cuándo usar distribución Normal?  
   **Respuesta orientativa:** Cuando datos son simétricos alrededor de media, muchos fenómenos naturales.

4. **Pregunta:** ¿Qué significa independencia entre eventos?  
   **Respuesta orientativa:** Ocurrencia de uno no afecta probabilidad del otro: $P(A|B)=P(A)$.

5. **Pregunta:** ¿Por qué es importante Bayes en diagnóstico médico?  
   **Respuesta orientativa:** Combina prevalencia (a priori) con sensibilidad/especificidad para obtener probabilidad real.
