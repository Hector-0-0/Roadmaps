# Práctica - 10-terraform

## Nivel básico
1. **Estructura inicial** (criterio de terminado: demostrable)
   Enunciado: Crea archivos main.tf, variables.tf, outputs.tf con provider AWS.
   Pista: Usa región válida.
   Criterio verificable: Estructura correcta y sintaxis válida.

2. **Init y plan** (criterio de terminado: demostrable)
   Enunciado: Ejecuta `terraform init` y `terraform plan`, revisa salida.
   Pista: Lee plan antes de apply.
   Criterio verificable: Init exitoso, plan muestra recursos a crear.

## Nivel intermedio
3. **Crear bucket S3** (criterio de terminado: demostrable)
   Enunciado: Crea bucket S3 con nombre único usando resource.
   Pista: Nombre global único.
   Criterio verificable: Bucket creado tras apply.

4. **Variables y outputs** (criterio de terminado: demostrable)
   Enunciado: Usa variables para región/instancia y outputs para IP.
   Pista: Parametriza valores.
   Criterio verificable: Variables usadas, outputs muestran valores.

## Nivel desafío
5. **EC2 + S3 y destroy** (criterio de terminado: demostrable)
   Enunciado: Crea instancia EC2 (Free Tier) y bucket S3, luego ejecuta `terraform destroy` eliminando todo.
   Pista: Siempre destruir en práctica.
   Criterio verificable: Recursos creados y completamente destruidos, sin recursos huérfanos.
