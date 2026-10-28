# Checkpoint 09 - Automatización

## Objetivo del checkpoint
Automatizar configuración de servidores con Ansible.

## Conocimientos que consolida
- [01-linux-basico](../01-linux-basico/README.md): SSH, permisos, servicios.
- [08-ansible](../08-ansible/README.md): inventory, playbooks, handlers, roles.

## 3 ideas de proyecto de dificultad creciente

### 1. Proyecto 1: Configurar inventario (Dificultad: básica)
**Descripción:** Crear inventory y probar conectividad.

**Requisitos funcionales:**
- Inventory con hosts.
- Conexión SSH.
- Comando ad-hoc ping.
- Documentar resultados.

**Habilidades que practica:**
- Inventory, SSH, Ansible ad-hoc.

**Criterios de aceptación:**
- Todos los hosts responden pong.
- Configuración correcta.

**Mejoras opcionales:**
- Múltiples grupos.
- Variables por grupo.

### 2. Proyecto 2: Instalar y configurar Nginx (Dificultad: intermedia)
**Descripción:** Playbook para instalar nginx, copiar página, iniciar servicio.

**Requisitos funcionales:**
- Playbook con tasks.
- Uso de become.
- Handler para reinicio.
- Idempotencia verificada.

**Habilidades que practica:**
- Playbooks, módulos, handlers.

**Criterios de aceptación:**
- Nginx instalado y corriendo.
- Página servida.
- Playbook idempotente.

**Mejoras opcionales:**
- Plantillas con Jinja2.
- Firewall.

### 3. Proyecto 3: Automatización completa (Dificultad: intermedia-avanzada)
**Descripción:** Automatizar stack básico (usuario, paquetes, nginx, firewall).

**Requisitos funcionales:**
- Múltiples tasks organizadas.
- Variables.
- Handlers.
- Documentación.

**Habilidades que practica:**
- Automatización completa, organización.

**Criterios de aceptación:**
- Servidor configurado desde cero.
- Reproducible.
- Sin pasos manuales.

**Mejoras opcionales:**
- Usar roles.
- Ansible Vault.
