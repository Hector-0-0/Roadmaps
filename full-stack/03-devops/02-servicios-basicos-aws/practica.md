# Práctica - 02-servicios-basicos-aws

## Nivel básico

1. **Crear bucket S3 para hosting estático**
   Enunciado: En la consola de AWS (Free Tier), crea un bucket S3 con nombre único global. Sube un archivo `index.html` simple. Habilita "Static website hosting" con documento de índice `index.html`. 
   Pista: Revisa "Block Public Access" antes de aplicar políticas públicas. Usa un nombre que no colisione con otros buckets. Siempre configura alerta de facturación.
   Criterio verificable: Existe el bucket, `index.html` subido, static website hosting habilitado y se documenta la URL del endpoint. Al terminar, el bucket y objetos se eliminarán.

2. **Lanzar instancia EC2 y conectar por SSH**
   Enunciado: Lanza una instancia EC2 con AMI Free Tier (t3.micro), crea o usa un key pair. Configura Security Group permitiendo SSH solo desde tu IP pública. Conéctate por SSH usando el archivo `.pem` con permisos correctos.
   Pista: Usa `chmod 400 mi-clave.pem` en Linux/macOS. Identifica el usuario correcto según AMI (ec2-user para Amazon Linux, ubuntu para Ubuntu). Restringe el origen a tu IP, no a 0.0.0.0/0.
   Criterio verificable: Conexión SSH exitosa desde terminal, se muestra prompt de la instancia. Se documenta IP pública y se elimina la instancia al finalizar.

## Nivel intermedio

3. **Servir página web desde EC2**
   Enunciado: Desde la instancia EC2 conectada, instala un servidor web (nginx o apache), crea un archivo HTML en el directorio correcto y ábrelo desde el navegador usando la IP pública de la instancia.
   Pista: Abre el puerto 80 en el Security Group desde tu IP o 0.0.0.0/0 solo para esta prueba. Usa `sudo systemctl start <servicio>` y verifica con `curl localhost`.
   Criterio verificable: Al acceder a `http://<IP_PUBLICA>` se muestra la página creada. Al terminar, detén/elimina la instancia y libera recursos.

4. **Crear VPC con subred pública y privada**
   Enunciado: Crea una VPC con CIDR `10.0.0.0/16`. Crea una subred pública (`10.0.1.0/24`) y una subred privada (`10.0.2.0/24`) en zonas de disponibilidad distintas. Adjunta un Internet Gateway a la VPC y configura la tabla de rutas de la subred pública hacia el IGW.
   Pista: Diferencia subred pública (ruta a IGW) de privada (sin ruta directa a internet). Documenta CIDR, route tables e asociaciones.
   Criterio verificable: Se documenta la topología creada (VPC, subredes, IGW, route tables) mostrando asociación correcta. Se entiende y documenta cómo verificar conectividad. Elimina VPC y recursos al terminar.

5. **Route 53: zona alojada y registro de prueba**
   Enunciado: En Route 53, crea una hosted zone para un dominio de prueba (o documenta con un dominio propio). Crea un registro A apuntando a la IP pública de tu instancia EC2 (usa Elastic IP si es posible). Verifica la resolución DNS con `dig` o `nslookup`.
   Pista: Usa Elastic IP para evitar cambios de IP. Ten en cuenta que registrar un dominio tiene costo; si no tienes dominio, solo crea la hosted zone y documenta los nameservers.
   Criterio verificable: Se documentan los records creados y el resultado de `dig +short <dominio>` o `nslookup`. Se eliminan zona alojada/records de prueba al finalizar.

## Nivel desafío

6. **SES: verificar identidad y enviar correo en sandbox**
   Enunciado: Verifica una dirección de correo como identidad en Amazon SES en modo sandbox. Verifica también un correo destinatario. Desde la consola SES, envía un correo de prueba a la dirección verificada. Documenta los pasos, límites de sandbox y proceso para solicitar acceso a producción.
   Pista: En sandbox solo se puede enviar a direcciones verificadas. Revisa los correos de verificación. Configurar SPF/DKIM es recomendable para entregabilidad.
   Criterio verificable: Se muestran las identidades verificadas en SES, el correo de prueba enviado exitosamente y un documento con diferencias sandbox/producción. Elimina identidades de prueba al terminar.

7. **Integrador: desplegar sitio estático con S3**
   Enunciado: Despliega un sitio estático completo (index.html, styles.css) en S3 con static website hosting. Asegúrate de que los enlaces relativos funcionen. Documenta permisos aplicados y elimina todos los objetos y el bucket al finalizar.
   Pista: Usa nombres de archivos correctos, revisa Content-Type. Ten cuidado con políticas públicas: aplica solo lo necesario y revísalo.
   Criterio verificable: El sitio es accesible por el endpoint de S3, se visualizan estilos correctamente. Se verifica la limpieza completa (bucket vacío y eliminado).

8. **Integrador con limpieza obligatoria**
   Enunciado: Realiza un mini despliegue usando EC2 + Security Group + página web. Documenta: recursos creados, costos estimados con Free Tier, y lista de verificación de limpieza (instancia terminada, key pair, Elastic IP liberada, Security Group revisado). Ejecuta la limpieza y verifica que no queden recursos activos.
   Pista: Usa la consola de Billing/Cost Explorer para revisar. Configura una alerta de facturación antes de empezar. No dejes IP elásticas sin asociar.
   Criterio verificable: Documento con checklist de limpieza completado y evidenciado (capturas o descripción), sin recursos activos tras la práctica.
