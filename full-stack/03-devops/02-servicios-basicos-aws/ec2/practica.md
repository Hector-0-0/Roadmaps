# Práctica - 03-devops/02-servicios-basicos-aws/ec2

## Nivel básico

1. **Lanzar instancia Free Tier con key pair**
   Enunciado: En AWS EC2 (Free Tier), lanza instancia t3.micro con AMI Amazon Linux 2023 o Ubuntu. Crea o selecciona key pair. Configura Security Group básico.
   Pista: ADVERTENCIA: Usa solo Free Tier. Configura alerta de facturación. Guarda el archivo .pem de forma segura.
   Criterio verificable: Instancia en estado running, key pair asociado, tipo t3.micro confirmado en consola.

2. **Conectarse por SSH con permisos correctos**
   Enunciado: Desde terminal aplica `chmod 400 mi-clave.pem`. Conéctate con `ssh -i mi-clave.pem ec2-user@<IP_PUBLICA>` (ajusta usuario según AMI). Verifica conexión exitosa.
   Pista: Si permisos son incorrectos SSH rechaza la clave. Usa el usuario correcto: ec2-user para Amazon Linux, ubuntu para Ubuntu.
   Criterio verificable: Conexión SSH exitosa, prompt de instancia visible, comando `whoami` muestra usuario correcto.

3. **Security Group con restricciones**
   Enunciado: Modifica Security Group para permitir SSH solo desde tu IP pública. Abre puerto 80 para HTTP desde internet si vas a servir web. Documenta reglas aplicadas.
   Pista: Obtén tu IP pública con `curl ifconfig.me`. Nunca abras SSH a 0.0.0.0/0 en producción.
   Criterio verificable: Reglas de SG configuradas correctamente, SSH solo desde IP autorizada, puerto 80 abierto según necesidad.

## Nivel intermedio

4. **Instalar nginx con User Data**
   Enunciado: Lanza nueva instancia con User Data script que instale y inicie nginx automáticamente. Accede con curl o navegador a IP pública.
   Pista: User Data se ejecuta al primer arranque. Script para Amazon Linux: `yum install -y nginx && systemctl start nginx && systemctl enable nginx`.
   Criterio verificable: nginx instalado y corriendo sin intervención manual, `curl http://<IP_PUBLICA>` retorna página por defecto de nginx.

5. **Asociar IP elástica**
   Enunciado: Asigna una Elastic IP a tu instancia. Verifica que persiste tras stop/start. Documenta diferencia con IP pública dinámica.
   Pista: ADVERTENCIA: Elastic IP asociada tiene costo en algunos casos, pero con instancia running suele estar cubierto en Free Tier. Libérala al terminar.
   Criterio verificable: Elastic IP asociada, IP permanece tras stop/start, instancia accesible por IP elástica.

6. **Crear AMI y lanzar copia**
   Enunciado: Crea una AMI desde tu instancia configurada con nginx. Lanza nueva instancia desde esa AMI. Verifica que nginx funciona sin instalarlo manualmente.
   Pista: La AMI captura estado del volumen. Al lanzar desde AMI se replica configuración.
   Criterio verificable: AMI creada exitosamente, nueva instancia lanzada, nginx funciona sin instalación manual.

## Nivel desafío

7. **Desplegar app Node.js con systemd**
   Enunciado: Instala Node.js en instancia. Sube app Node.js simple. Crea servicio systemd para ejecutarla automáticamente. Configura para reinicio automático.
   Pista: Crea archivo en `/etc/systemd/system/app.service`. Usa `systemctl daemon-reload`, `enable`, `start`. Abre puerto en SG.
   Criterio verificable: App responde por puerto configurado, servicio systemd corriendo, se reinicia tras stop manual.

8. **Limpiar recursos completamente**
   Enunciado: Termina todas las instancias EC2. Libera Elastic IPs. Elimina AMIs y snapshots asociados. Elimina key pairs de prueba. Verifica limpieza.
   Pista: Terminar instancia no siempre elimina volúmenes según configuración. Revisa volúmenes EBS huérfanos. Usa Free Tier con precaución.
   Criterio verificable: Sin instancias corriendo, Elastic IPs liberadas, AMIs eliminadas, sin volúmenes huérfanos, checklist completado.
