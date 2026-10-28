# 10-terraform

## 1. Qué es y para qué sirve
Terraform es una herramienta de IaC (Infrastructure as Code, infraestructura como código) de HashiCorp. Permite definir, aprovisionar y gestionar infraestructura con archivos declarativos en HCL (HashiCorp Configuration Language).

## 2. Por qué importa dentro del roadmap y cómo se conecta
Permite automatizar creación de infraestructura (VPC, EC2, S3) de forma reproducible. Se conecta con AWS, Ansible y CI/CD.

## 3. Conceptos clave
- **IaC**: infraestructura definida como código, versionable.
- **Provider (proveedor)**: plugin para interactuar con API (aws, azurerm).
- **Resource (recurso)**: componente de infraestructura a crear.
- **Data source**: leer recursos existentes.
- **Variables (variables)**: parametrizar configuración.
- **Outputs (salidas)**: mostrar información tras apply.
- **State (estado)**: archivo terraform.tfstate que mapea config a recursos reales.
- **Modules (módulos)**: contenedores reutilizables de configuración.
- **Ciclo**: init, plan, apply, destroy.

## 4. Ejemplos de código comentados, correctos y ejecutables

### Ejemplo 1: Crear bucket S3
```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "mi_bucket" {
  bucket = "mi-bucket-unico-12345"
  tags = {
    Name        = "MiBucket"
    Environment = "Dev"
  }
}
```

### Ejemplo 2: Crear instancia EC2 con variables
```hcl
# variables.tf
variable "ami_id" {
  type    = string
  default = "ami-0c55b159cbfafe1f0" # ejemplo, usar AMI válida en región
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

# main.tf
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name = "web-server"
  }
}

# outputs.tf
output "ip_publica" {
  value = aws_instance.web.public_ip
}
```

Comandos:
```bash
terraform init
terraform plan
terraform apply
terraform destroy
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Commitear terraform.tfstate.
- Usar nombres de bucket S3 no únicos.
- No usar variables/outputs.
- Aplicar sin revisar plan.
- Olvidar destroy en prácticas.

Buenas prácticas:
- Usar .gitignore (terraform.tfstate, .terraform/).
- Usar variables para valores reutilizables.
- Revisar plan antes de apply.
- Usar módulos para reutilización.
- Siempre destruir recursos de práctica.
- Cuidar credenciales AWS.

## 6. Autoevaluación

1. ¿Qué es IaC?
2. ¿Qué es Terraform?
3. ¿Diferencia entre init, plan, apply, destroy?
4. ¿Para qué sirve el archivo state?
5. ¿Ventaja de usar variables?

Respuestas esperadas (orientativas):
1. Infraestructura definida y gestionada con código.
2. Herramienta IaC declarativa multi-cloud.
3. init inicializa, plan muestra cambios, apply aplica, destroy elimina.
4. Rastrea recursos reales creados por Terraform.
5. Parametrizar y reutilizar configuración.
