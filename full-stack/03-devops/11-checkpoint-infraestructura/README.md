# Checkpoint 11 - Infraestructura

## Objetivo del checkpoint
Aprovisionar infraestructura con Terraform.

## Conocimientos que consolida
- [02-servicios-basicos-aws](../02-servicios-basicos-aws/README.md): EC2, S3, conceptos AWS.
- [10-terraform](../10-terraform/README.md): IaC, providers, resources, state.

## 3 ideas de proyecto de dificultad creciente

### 1. Proyecto 1: Bucket S3 con Terraform (Dificultad: básica)
**Descripción:** Crear bucket S3 usando Terraform.

**Requisitos funcionales:**
- main.tf con provider AWS.
- resource aws_s3_bucket.
- terraform init/plan/apply.
- terraform destroy.

**Habilidades que practica:**
- Terraform básico, S3.

**Criterios de aceptación:**
- Bucket creado.
- Código versionado.
- Recursos destruidos.

**Mejoras opcionales:**
- Versionado.
- Tags.

### 2. Proyecto 2: Instancia EC2 con Terraform (Dificultad: intermedia)
**Descripción:** Crear instancia EC2 (Free Tier) con variables.

**Requisitos funcionales:**
- Variables para ami/instance_type.
- Security Group básico.
- Outputs con IP pública.
- Destroy al terminar.

**Habilidades que practica:**
- Variables, outputs, EC2.

**Criterios de aceptación:**
- Instancia creada.
- Variables usadas.
- IP visible en outputs.

**Mejoras opcionales:**
- Key pair.
- User data.

### 3. Proyecto 3: Infraestructura básica completa (Dificultad: intermedia-avanzada)
**Descripción:** Crear VPC, subnet, EC2, S3 con Terraform.

**Requisitos funcionales:**
- Estructura modular o organizada.
- Variables y outputs.
- terraform plan revisado.
- Destruir todo al finalizar.

**Habilidades que practica:**
- IaC completo, organización.

**Criterios de aceptación:**
- Recursos creados correctamente.
- Código reutilizable.
- Todo destruido.

**Mejoras opcionales:**
- Backend remoto (conceptual).
- Workspaces.
