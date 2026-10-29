# Práctica - Habilidades y responsabilidades

## Nivel básico

1. **Mapa de habilidades**
   Enunciado: Crea un mapa con 3 habilidades técnicas y 3 blandas necesarias para un ML Engineer con descripción.
   Pista: Técnicas: Python, matemáticas, datos. Blandas: comunicación, pensamiento crítico, ética.
   Criterio verificable: 6 habilidades con descripción concreta y aplicable al rol.

2. **Flujo reproducible**
   Enunciado: Lista los pasos de un flujo ML reproducible desde problema hasta monitoreo.
   Pista: Incluye definición, datos, limpieza, modelado, evaluación, despliegue, monitoreo.
   Criterio verificable: Al menos 7 pasos ordenados con descripción breve.

3. **Pipeline práctico**
   Enunciado: Implementa Pipeline con StandardScaler y RandomForestClassifier para Iris con split estratificado.
   Pista: Usa sklearn.pipeline.Pipeline y evalúa con accuracy_score.
   Criterio verificable: Pipeline funcional, evaluación en test con valor numérico de accuracy.

## Nivel intermedio

4. **Validación cruzada completa**
   Enunciado: Con Pipeline anterior usa cross_val_score con cv=5, muestra scores, media y desviación.
   Pista: Usa numpy.mean y numpy.std.
   Criterio verificable: 5 scores numéricos, media y desviación calculados correctamente.

5. **Detectar fuga de datos**
   Enunciado: Explica por qué escalar antes del split causa fuga de datos y cómo evitarlo con Pipeline.
   Pista: fit_transform en todo filtra información del test al entrenamiento.
   Criterio verificable: Explicación correcta con ejemplo de implementación correcta usando Pipeline.

6. **Checklist de despliegue**
   Enunciado: Crea checklist con 8 ítems para llevar un modelo a producción.
   Pista: Incluye versionado, pruebas, monitoreo, rollback, seguridad.
   Criterio verificable: 8 ítems con criterio verificable para cada uno.

## Nivel desafío

7. **Plan de monitoreo**
   Enunciado: Diseña plan de monitoreo para modelo en producción (métricas, alertas, drift).
   Pista: Define métricas técnicas, métricas de negocio, umbrales y acciones.
   Criterio verificable: Plan con métricas, frecuencia, umbrales numéricos y plan de respuesta.

8. **Análisis ético**
   Enunciado: Analiza un caso hipotético con datos sensibles, identifica 3 riesgos y propone mitigaciones con código o proceso.
   Pista: Considera anonimización, fairness, explicabilidad.
   Criterio verificable: 3 riesgos con mitigaciones concretas, medibles y aplicables.
