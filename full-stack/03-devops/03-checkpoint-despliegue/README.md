# Checkpoint 03 - Despliegue

## Objetivo del checkpoint
Desplegar aplicación frontend o backend en nube.

## Conocimientos que consolida
- [01-linux-basico](../01-linux-basico/README.md)
- [02-servicios-basicos-aws](../02-servicios-basicos-aws/README.md)

## 3 ideas de proyecto de dificultad creciente

### 1. Proyecto 1: Sitio estático en S3 (Dificultad: básica)
**Descripción:** Desplegar HTML/CSS/JS en S3.

**Requisitos funcionales:**
- Subir archivos.
- Habilitar static hosting.
- Acceso público controlado.
- Verificar URL.

**Habilidades que practica:**
- S3, permisos.

**Criterios de aceptación:**
- Sitio accesible.
- Archivos correctos.

**Mejoras opcionales:**
- CloudFront básico.

### 2. Proyecto 2: App Node.js en EC2 (Dificultad: intermedia)
**Descripción:** Desplegar API en EC2 con PM2.

**Requisitos funcionales:**
- Instalar Node.js en EC2.
- Clonar repo.
- Ejecutar con PM2.
- Abrir puerto en security group.

**Habilidades que practica:**
- EC2, SSH, Linux, PM2.

**Criterios de aceptación:**
- API responde desde IP pública.
- Proceso corriendo con PM2.

**Mejoras opcionales:**
- Nginx como reverse proxy.

### 3. Proyecto 3: Despliegue con dominio (Dificultad: intermedia)
**Descripción:** Apuntar dominio con Route 53.

**Requisitos funcionales:**
- Configurar registro DNS.
- Apuntar a recurso (conceptual).
- Verificar resolución.

**Habilidades que practica:**
- DNS, Route 53.

**Criterios de aceptación:**
- Dominio resuelve.
- Documentar pasos.

**Mejoras opcionales:**
- HTTPS con certificados.
