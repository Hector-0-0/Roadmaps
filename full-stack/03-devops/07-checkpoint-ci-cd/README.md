# Checkpoint 07 - CI/CD

## Objetivo del checkpoint
Crear pipeline CI/CD básico con GitHub Actions integrando pruebas y despliegue.

## Conocimientos que consolida
- [08-git-y-github](../../01-frontend/08-git-y-github/README.md): ramas, commits, push.
- [06-github-actions](../06-github-actions/README.md): workflows, jobs, secrets, despliegue.

## 3 ideas de proyecto de dificultad creciente

### 1. Proyecto 1: CI para tests (Dificultad: básica)
**Descripción:** Crear workflow que ejecute tests en cada push/PR.

**Requisitos funcionales:**
- Workflow en .github/workflows/ci.yml.
- Trigger push y pull_request.
- Instalar dependencias y ejecutar tests.
- Mostrar resultado.

**Habilidades que practica:**
- YAML, GitHub Actions, CI.

**Criterios de aceptación:**
- Workflow corre correctamente.
- Tests se ejecutan.
- Falla si tests fallan.

**Mejoras opcionales:**
- Badge en README.
- Ejecutar en múltiples Node versions.

### 2. Proyecto 2: Build y artifacts (Dificultad: intermedia)
**Descripción:** Generar build y guardar artifacts.

**Requisitos funcionales:**
- Job de build.
- Generar archivos de build.
- Guardar con actions/upload-artifact.
- Descargar/verificar artifact.

**Habilidades que practica:**
- Build, artifacts, caché.

**Criterios de aceptación:**
- Build exitoso.
- Artifact disponible.
- Caché configurado si aplica.

**Mejoras opcionales:**
- Cacheo de node_modules.
- Linting.

### 3. Proyecto 3: Despliegue automático (Dificultad: intermedia-avanzada)
**Descripción:** Desplegar a S3 con GitHub Actions usando secrets.

**Requisitos funcionales:**
- Pipeline con test -> build -> deploy.
- Usar secrets (AWS keys).
- Desplegar solo en main.
- Verificar sitio desplegado.

**Habilidades que practica:**
- CD, secrets, despliegue cloud.

**Criterios de aceptación:**
- Solo despliega si tests pasan.
- Usa secrets correctamente.
- Sitio accesible tras despliegue.

**Mejoras opcionales:**
- Invalidación CloudFront.
- Ambientes (staging/production).
