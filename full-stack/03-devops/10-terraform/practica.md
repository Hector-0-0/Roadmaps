# Práctica - 10-terraform

## Nivel básico

1. **Inicializar proyecto Terraform**
   Enunciado: Crea un directorio `terraform-practica`. Crea `main.tf` con el proveedor AWS configurado para región `us-east-1`. Ejecuta `terraform init` y verifica que se crea `.terraform/`.
   Pista: Usa `terraform init` para descargar providers. Añade `.terraform/` y `*.tfstate*` a `.gitignore`. Nunca commitees archivos de estado.
   Criterio verificable: `terraform init` finaliza sin errores, existe directorio `.terraform/` con provider aws descargado.

2. **Validar y planificar configuración**
   Enunciado: Usa `terraform validate` para comprobar sintaxis. Crea una configuración mínima con `terraform plan` y revisa la salida mostrando recursos a crear.
   Pista: `terraform validate` verifica sintaxis sin conectarse a AWS. `terraform plan` muestra cambios propuestos antes de aplicar.
   Criterio verificable: `terraform validate` retorna éxito, `terraform plan` muestra plan con recursos identificados sin aplicar cambios.

3. **Crear bucket S3 con variables**
   Enunciado: Usa `variables.tf` para definir variable `bucket_name`. Usa `terraform.tfvars` para asignar valor. Crea bucket S3 con `aws_s3_bucket`. Ejecuta `terraform apply`.
   Pista: Usa nombres únicos globalmente para buckets S3. Marca variables sensibles si aplica. Usa `var.nombre_variable` para referenciarlas.
   Criterio verificable: Bucket creado en AWS, visible con nombre desde variable, apply ejecutado correctamente.

## Nivel intermedio

4. **Outputs y EC2 con Security Group**
   Enunciado: Crea `aws_security_group` permitiendo SSH desde tu IP. Crea instancia `aws_instance` t3.micro (Free Tier). Añade `outputs.tf` mostrando IP pública. Ejecuta `terraform apply`.
   Pista: Usa `aws_ami` data source o AMI válida para tu región. Restringe SSH a tu IP con `cidr_blocks`. Siempre usar Free Tier.
   Criterio verificable: Instancia y SG creados, output muestra IP pública, SSH funciona con restricciones correctas.

5. **Inspeccionar estado con terraform state**
   Enunciado: Usa `terraform state list` para ver recursos en estado. Usa `terraform state show aws_instance.<nombre>` para detalles. Entiende relación entre código y estado.
   Pista: El archivo `terraform.tfstate` mapea configuración a recursos reales. Nunca lo edites manualmente.
   Criterio verificable: `terraform state list` muestra recursos creados, `terraform state show` muestra atributos correctos.

6. **Módulo reutilizable**
   Enunciado: Crea un módulo en `modules/s3_bucket/` con `main.tf`, `variables.tf`, `outputs.tf`. Usa el módulo desde raíz para crear bucket. Ejecuta `terraform init` y `apply`.
   Pista: Llama módulo con `module "nombre" { source = "./modules/s3_bucket" ... }`. Los módulos permiten reutilizar código.
   Criterio verificable: Módulo creado y usado correctamente, bucket creado vía módulo, estructura organizada.

## Nivel desafío

7. **Detectar drift con terraform plan**
   Enunciado: Con recursos creados por Terraform, modifica manualmente un tag desde consola AWS. Ejecuta `terraform plan` y observa drift detectado. Corrige con `terraform apply` para volver al estado deseado.
   Pista: Terraform detecta diferencias entre estado y configuración real. `terraform plan` muestra cambios para alinear.
   Criterio verificable: Plan muestra cambios para revertir modificación manual, apply restaura configuración definida en código.

8. **Destruir toda la infraestructura**
   Enunciado: Revisa recursos con `terraform plan -destroy`. Ejecuta `terraform destroy` para eliminar todos los recursos creados. Verifica en consola AWS que no queden recursos.
   Pista: Siempre destruye recursos de práctica para evitar costos. Usa `terraform destroy -auto-approve` con precaución o confirma interactivamente.
   Criterio verificable: `terraform destroy` finaliza exitosamente, no quedan recursos creados en AWS, archivos de estado actualizados.
