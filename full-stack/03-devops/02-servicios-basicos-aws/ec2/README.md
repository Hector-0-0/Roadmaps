# ec2 (Elastic Compute Cloud)

## 1. Qué es y para qué sirve
EC2 (Elastic Compute Cloud, nube de computación elástica) es un servicio de AWS que permite alquilar máquinas virtuales (instancias) en la nube. Sirve para ejecutar aplicaciones, servidores web, APIs y cualquier carga de trabajo sin necesidad de hardware físico propio.

## 2. Por qué importa dentro del roadmap y cómo se conecta
EC2 es la base para desplegar aplicaciones backend. Se conecta con Linux básico (conexión SSH), VPC (red), seguridad y despliegue en el checkpoint de despliegue.

## 3. Conceptos clave
- **AMI (Amazon Machine Image, imagen de máquina de Amazon)**: plantilla con sistema operativo y software.
- **Instance type (tipo de instancia)**: define CPU, memoria, red (ej. t3.micro en Free Tier).
- **Key pair (par de claves)**: par público/privado para autenticación SSH.
- **Security Groups (grupos de seguridad)**: firewall virtual a nivel de instancia (reglas de entrada/salida).
- **Elastic IP (IP elástica)**: dirección IP pública estática asociable a instancia.
- **Ciclo de vida**: pending, running, stopping, stopped, terminated. Stop conserva volumen EBS, terminate elimina instancia y volumenes según configuración.

## 4. Ejemplos de código comentados, correctos y ejecutables

### Conexión SSH (ejemplo)
```bash
# Dar permisos a clave (Linux/macOS)
chmod 400 mi-clave.pem

# Conectar
ssh -i mi-clave.pem ec2-user@<IP_PUBLICA>
```

### Comandos básicos tras conexión
```bash
# Actualizar paquetes (Amazon Linux/Ubuntu según AMI)
sudo yum update -y  # Amazon Linux
# sudo apt update && sudo apt upgrade -y  # Ubuntu
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Olvidar abrir puerto 22 en Security Group para SSH.
- Usar permisos incorrectos en archivo .pem.
- Dejar instancias corriendo innecesariamente.
- Conectarse con usuario equivocado según AMI.

Buenas prácticas:
- Usar solo instancias Free Tier (t3.micro) mientras aprendes.
- Restringir Security Group a tu IP para SSH.
- Usar claves distintas por entorno.
- Terminar/stop recursos al finalizar práctica.
- Configurar alertas de facturación en AWS Billing.

## 6. Autoevaluación

1. ¿Qué es EC2?
2. ¿Qué es una AMI?
3. ¿Para qué sirve un Security Group?
4. ¿Cuál es la diferencia entre stop y terminate?
5. ¿Por qué usar chmod 400 en el archivo .pem?

Respuestas esperadas (orientativas):
1. Servicio de máquinas virtuales elásticas en AWS.
2. Plantilla con SO y software para lanzar instancias.
3. Firewall virtual que controla tráfico a la instancia.
4. stop detiene y conserva disco, terminate elimina instancia.
5. Restringir permisos para que SSH acepte la clave privada.
