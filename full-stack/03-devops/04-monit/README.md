# 04-monit

## 1. Qué es y para qué sirve
Monitoreo (monitoring) consiste en observar el estado, rendimiento y disponibilidad de aplicaciones y servidores. Permite detectar problemas antes de que afecten a usuarios.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Tras desplegar, es necesario vigilar recursos y logs. Se conecta con Linux, despliegue en EC2 y buenas prácticas de producción.

## 3. Conceptos clave
- **Métricas**: CPU, memoria RAM, disco, red, carga del sistema.
- **Logs (registros)**: eventos del sistema/aplicación (/var/log, journalctl).
- **Uptime (tiempo activo)**: disponibilidad del servicio.
- **Checks (comprobaciones)**: verificación de puertos/procesos.
- **Alertas**: notificaciones ante umbrales críticos.
- **Reinicio automático**: reiniciar servicio si falla (systemd, PM2).
- **Herramientas**: top/htop, journalctl, netstat/ss, Prometheus, Grafana (conceptos).

## 4. Ejemplos de código comentados, correctos y ejecutables

### Ejemplo 1: Comandos de monitoreo
```bash
# Uso de CPU/memoria
top
# o
htop

# Espacio en disco
df -h

# Memoria
free -h

# Procesos
ps aux | head -20
```

### Ejemplo 2: Revisar logs y servicio con systemd
```bash
# Logs del sistema
journalctl -u nginx --since -1h

# Estado de servicio
systemctl status nginx

# Reiniciar servicio
sudo systemctl restart nginx
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- No revisar logs al fallar servicio.
- Alertas sin umbrales definidos.
- Ignorar uso de disco/memoria.
- No tener forma de reinicio automático.

Buenas prácticas:
- Definir métricas clave.
- Revisar logs sistemáticamente.
- Configurar alertas básicas.
- Usar systemd o PM2 para reinicio automático.
- Documentar procedimientos de respuesta.

## 6. Autoevaluación

1. ¿Qué es monitoreo?
2. ¿Diferencia entre métrica y log?
3. ¿Para qué sirve journalctl?
4. ¿Qué es uptime?
5. ¿Cuándo reiniciar un servicio automáticamente?

Respuestas esperadas (orientativas):
1. Observar salud y rendimiento de sistemas/aplicaciones.
2. Métrica es valor numérico, log es registro de evento.
3. Ver logs de systemd/journald.
4. Porcentaje/tiempo que servicio está disponible.
5. Ante fallos recurrentes o caídas, con monitoreo y umbrales.
