# Práctica - Probabilidad para Machine Learning

## Nivel básico

1. **Probabilidad básica**
   Enunciado: Calcula probabilidades con reglas de suma y producto para dos eventos independientes.
   Pista: Usa ejemplos numéricos concretos.
   Criterio verificable: Cálculos correctos con fórmulas aplicadas correctamente.

2. **Simulación**
   Enunciado: Simula 10000 lanzamientos de moneda con numpy.random y estima P(cara).
   Pista: Usa np.random.choice o randint.
   Criterio verificable: Estimación cercana a 0.5 con convergencia demostrada.

3. **Distribución Normal**
   Enunciado: Genera N(0,1), calcula P(-1 < Z < 1) empíricamente y teóricamente.
   Pista: Usa stats.norm.cdf.
   Criterio verificable: Valores empírico y teórico (~0.6827) comparados.

## Nivel intermedio

4. **Teorema de Bayes numérico**
   Enunciado: Resuelve problema diagnóstico: prevalencia 1%, sensibilidad 99%, especificidad 95%. Calcula P(enfermo|positivo).
   Pista: Aplica fórmula paso a paso.
   Criterio verificable: Resultado numérico correcto (~0.166) con pasos documentados.

5. **Naive Bayes conceptual práctico**
   Enunciado: Implementa clasificador Naive Bayes simple con conteos para datos categóricos pequeños.
   Pista: Asume independencia condicional. Usa Bayes por clase.
   Criterio verificable: Predicción correcta con probabilidades calculadas.

6. **Variables aleatorias**
   Enunciado: Simula Binomial(n=10,p=0.3), calcula media/varianza empírica y teórica.
   Pista: Teórica: E[X]=np, Var(X)=np(1-p).
   Criterio verificable: Valores empíricos cercanos a teóricos.

## Nivel desafío

7. **Monte Carlo**
   Enunciado: Estima π usando método Monte Carlo con 100000 puntos.
   Pista: Puntos dentro círculo unitario / total * 4.
   Criterio verificable: Estimación de π entre 3.13 y 3.15 con código correcto.

8. **Clasificación probabilística**
   Enunciado: Con datos de Iris usa probabilidades de LogisticRegression (predict_proba) y analiza calibración básica.
   Pista: Usa sklearn. Compara probabilidades con frecuencias.
   Criterio verificable: Probabilidades extraídas, análisis con valores numéricos.
