# Checkpoint 05 - Monitoreo

## Objetivo del checkpoint
Consolidar monitoreo básico aplicando conceptos de Linux y monitoreo a una aplicación o servidor.

## Conocimientos que consolida
- [01-linux-basico](../01-linux-basico/README.md): comandos, procesos, logs, systemd.
- [04-monit](../04-monit/README.md): métricas, logs, alertas, reinicio automático.

## 3 ideas de proyecto de dificultad creciente

### 1. Proyecto 1: Checklist de monitoreo (Dificultad: básica)
**Descripción:** Crear checklist completo para monitorear servidor Linux.

**Requisitos funcionales:**
- Listar métricas (CPU, memoria, disco, red).
- Comandos para revisar cada métrica.
- Umbrales sugeridos.
- Procedimiento básico de revisión.

**Habilidades que practica:**
- Identificación de métricas, documentación.

**Criterios de aceptación:**
- Checklist accionable.
- Comandos correctos para el sistema.
- Umbrales razonables.

**Mejoras opcionales:**
- Plantilla para incidentes.
- Checklist diario/semanal.

### 2. Proyecto 2: Monitoreo de servicio (Dificultad: intermedia)
**Descripción:** Monitorear un servicio (nginx/node) con systemd y logs.

**Requisitos funcionales:**
- Verificar estado con systemctl.
- Revisar logs con journalctl.
- Detectar caída y documentar pasos.
- Configurar reinicio automático si aplica.

**Habilidades que practica:**
- systemd, logs, diagnóstico.

**Criterios de aceptación:**
- Detecta estado correcto/incorrecto.
- Usa comandos correctos.
- Documenta procedimiento de recuperación.

**Mejoras opcionales:**
- Script simple de chequeo.
- Alertas por correo (conceptual).

### 3. Proyecto 3: Dashboard básico de monitoreo (Dificultad: intermedia-avanzada)
**Descripción:** Crear documento/plan con métricas, alertas y respuesta ante incidentes.

**Requisitos funcionales:**
- Definir métricas clave.
- Configurar umbrales de alerta.
- Plan de respuesta (escalado/reinicio).
- Monitoreo de logs críticos.

**Habilidades que practica:**
- Planificación, observabilidad básica.

**Criterios de aceptación:**
- Plan completo y aplicable.
- Umbrales justificados.
- Procedimientos claros.

**Mejoras opcionales:**
- Integrar con herramientas (Prometheus/Grafana conceptos).
- Métricas de aplicación.
