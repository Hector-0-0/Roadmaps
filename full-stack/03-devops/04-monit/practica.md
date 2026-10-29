# Práctica - 04-monit

## Nivel básico

1. **Monitoreo de recursos del sistema**
   Enunciado: En un sistema Linux, ejecuta `top`, `free -h` y `df -h`. Documenta el uso de CPU, memoria RAM y espacio en disco con valores numéricos.
   Pista: Usa `htop` si está disponible para una vista más clara. Compara el uso con `nproc` para entender la carga relativa al número de CPUs.
   Criterio verificable: Se documenta salida de los tres comandos con valores concretos, identificando uso total, usado y disponible.

2. **Revisión de logs con journalctl**
   Enunciado: Usa `journalctl -n 20` y `journalctl -u <servicio> --since -1h` para revisar logs. Identifica al menos tres entradas con timestamp y mensaje.
   Pista: Si no hay servicio específico, usa journalctl general. Los logs muestran eventos del sistema que ayudan a diagnosticar problemas.
   Criterio verificable: Se muestran al menos 3 entradas de log con timestamp, unidad o servicio y mensaje descriptivo.

3. **Estado y gestión de servicios con systemd**
   Enunciado: Verifica el estado de un servicio con `systemctl status <servicio>`. Si está disponible, practica `start`, `stop`, `restart` y `enable/disable`.
   Pista: Usa `sudo` para acciones que modifiquen estado. `enabled` significa que inicia con el sistema.
   Criterio verificable: Se muestra estado antes y después de cada acción, con evidencia del comando y su salida.

## Nivel intermedio

4. **Análisis de carga del sistema**
   Enunciado: Ejecuta `uptime` y relaciona la carga promedio con el número de CPUs obtenido con `nproc`. Explica si la carga es alta o baja.
   Pista: La carga promedio se compara con el número de núcleos. Una carga menor al número de CPUs generalmente indica buen rendimiento.
   Criterio verificable: Se documenta uptime, load average, número de CPUs y análisis con justificación.

5. **Detección y diagnóstico de problemas**
   Enunciado: Simula o identifica un servicio caído. Usa `systemctl status`, `journalctl -u <servicio> -n 30` para diagnosticar. Documenta pasos de solución.
   Pista: Revisa logs recientes para ver errores. Usa `systemctl restart` tras corregir si es necesario.
   Criterio verificable: Se identifica el problema, se revisan logs, se aplica solución y se verifica que el servicio vuelve a activo.

6. **Configuración de reinicio automático**
   Enunciado: Configura o documenta reinicio automático con systemd usando `Restart=` en la unidad del servicio. Verifica con `systemctl daemon-reload` y pruebas.
   Pista: Opciones comunes: `Restart=always` o `on-failure`. Siempre recarga daemon tras cambios en unit files.
   Criterio verificable: Se muestra configuración de Restart, daemon-reload ejecutado, y comportamiento documentado.

## Nivel desafío

7. **Plan de monitoreo con umbrales**
   Enunciado: Crea un plan de monitoreo con métricas (CPU, memoria, disco, servicios), umbrales de alerta (ej. CPU > 80%, disco > 90%), y procedimientos de respuesta.
   Pista: Define acciones concretas para cada umbral. Incluye comandos para verificar cada métrica.
   Criterio verificable: Plan documentado con métricas, umbrales numéricos, comandos verificables y procedimientos de respuesta claros.

8. **Monitoreo integral verificable**
   Enunciado: Ejecuta un chequeo integral: verifica 3 servicios, revisa uso de recursos, analiza logs recientes y genera un reporte con hallazgos y recomendaciones.
   Pista: Usa todos los comandos aprendidos. Estructura el reporte con fecha, métricas, estado de servicios y acciones.
   Criterio verificable: Reporte completo con evidencia de comandos ejecutados, resultados y conclusiones accionables.
