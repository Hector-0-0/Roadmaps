# Práctica - ec2

## Nivel básico
1. **Lanzar instancia Free Tier** (criterio de terminado: demostrable)
   Enunciado: Lanza una instancia EC2 con tipo t3.micro (Free Tier) usando Amazon Linux o Ubuntu.
   Pista: Selecciona AMI válida para Free Tier, crea/par usa key pair y revisa Security Group.
   Advertencia de costos: Usa solo Free Tier. Elimina la instancia al terminar la práctica.

2. **Conexión SSH** (criterio de terminado: demostrable)
   Enunciado: Conéctate por SSH desde tu terminal usando el archivo .pem.
   Pista: Aplica `chmod 400` al archivo y usa el usuario correcto según AMI (ec2-user/ubuntu).
   Advertencia de costos: Sin costo si Free Tier y recursos eliminados.

## Nivel intermedio
3. **Security Groups** (criterio de terminado: demostrable)
   Enunciado: Configura reglas: permite SSH solo desde tu IP, y HTTP/HTTPS si vas a servir web.
   Pista: Restringe origen a tu IP pública, no uses 0.0.0.0/0 para SSH.
   Advertencia de costos: Sin costo. Configura alertas de facturación.

4. **Elastic IP** (criterio de terminado: demostrable)
   Enunciado: Asigna una Elastic IP a tu instancia y verifica que persiste tras stop/start.
   Pista: Elastic IP tiene límite Free Tier; libera al terminar.
   Advertencia de costos: Elastic IP sin asociar puede generar cargos; siempre libera al finalizar.

## Nivel desafío
5. **Ciclo de vida completo** (criterio de terminado: demostrable)
   Enunciado: Practica stop, start, verifica IP (cambia si no es Elastic IP), luego terminate y elimina recursos asociados.
   Pista: Documenta diferencias entre stop/start/terminate.
   Advertencia de costos: OBLIGATORIO eliminar todos los recursos (instancia, Elastic IP si liberable, volúmenes). Configura alerta de facturación en AWS Billing y verifica en Free Tier.
