# Práctica - 04-monit

## Nivel básico
1. **Monitoreo de recursos** (criterio de terminado: demostrable)
   Enunciado: Usa `top`, `htop` (si disponible), `free -h`, `df -h` para revisar CPU, memoria, disco y procesos.
   Pista: Ejecuta en Linux/servidor y toma nota de valores.
   Criterio verificable: Documenta al menos 5 métricas con valores actuales.

2. **Revisión de logs** (criterio de terminado: demostrable)
   Enunciado: Revisa logs con `journalctl` y archivos en `/var/log/` (ej. auth.log, syslog).
   Pista: Usa `journalctl -n 20` y `tail -n 20`.
   Criterio verificable: Identifica al menos 3 entradas de log relevantes.

## Nivel intermedio
3. **Estado de servicios** (criterio de terminado: demostrable)
   Enunciado: Verifica estado de un servicio con `systemctl status <servicio>`.
   Pista: Prueba con nginx/apache o cualquier servicio instalado.
   Criterio verificable: Muestra estado, uptime del servicio y logs recientes.

4. **Uptime y carga** (criterio de terminado: demostrable)
   Enunciado: Revisa `uptime`, `load average` y explica qué significa.
   Pista: Compara con número de CPUs (`nproc`).
   Criterio verificable: Explicación escrita con relación entre carga y CPUs.

## Nivel desafío
5. **Alerta y reinicio automático** (criterio de terminado: demostrable)
   Enunciado: Configura o documenta monitoreo básico con umbrales (CPU>80%, disco>90%) y reinicio automático con systemd/PM2.
   Pista: Usa `systemctl enable` y revisa configuración.
   Criterio verificable: Checklist con métricas, umbrales, alerta y procedimiento de reinicio documentado.
