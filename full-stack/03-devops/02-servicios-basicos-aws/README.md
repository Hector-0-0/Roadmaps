# 02-servicios-basicos-aws

## 1. Qué es y para qué sirve
AWS (Amazon Web Services) es una plataforma de computación en nube (cloud computing) que ofrece servicios bajo demanda. En este tema se estudian servicios básicos para comprender redes, cómputo, DNS, correo y almacenamiento.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Estos servicios permiten desplegar aplicaciones creadas en Backend. Se conectan con Linux básico, despliegue y con los checkpoints posteriores. La práctica debe hacerse siempre en AWS Free Tier con precaución sobre costos.

## 3. Conceptos clave
- **Región y Zona de disponibilidad (Availability Zone)**: ubicación física donde se despliegan recursos.
- **Free Tier (capa gratuita)**: recursos gratuitos con límites; revisar [aws.amazon.com/free](https://aws.amazon.com/free/).
- **Seguridad**: principio de menor privilegio, Security Groups, control de acceso.
- **Costos**: configurar alerta de facturación, eliminar recursos tras práctica.

## 4. Mapa de sub-temas
- [ec2](ec2/README.md): instancias, AMI, tipos, key pairs, Security Groups, Elastic IP, ciclo de vida.
- [vpc](vpc/README.md): subredes públicas/privadas, route tables, IGW, NAT Gateway, CIDR, SG vs NACLs.
- [route53](route53/README.md): zonas alojadas, registros A/AAAA/CNAME/MX/TXT, TTL, apuntar dominio.
- [ses](ses/README.md): identidades, sandbox, SMTP vs API, SPF/DKIM, límites y reputación.
- [s3](s3/README.md): buckets, objetos, clases, políticas, versionado, hosting estático.

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Dejar recursos corriendo sin supervisión.
- Abrir puertos a todo internet innecesariamente.
- Olvidar liberar Elastic IP o eliminar buckets.
- No configurar alerta de facturación.

Buenas prácticas:
- Usar Free Tier y calcular límites.
- Configurar Billing Alarm (alerta de facturación).
- Aplicar menor privilegio.
- Eliminar recursos al finalizar cada práctica.
- Documentar lo que se crea y lo que se elimina.

## 6. Autoevaluación

1. ¿Qué es AWS?
2. ¿Qué es Free Tier?
3. ¿Por qué es importante configurar una alerta de facturación?
4. ¿Cuándo usarías EC2 vs S3?
5. ¿Qué precaución tomar al usar NAT Gateway?

Respuestas esperadas (orientativas):
1. Plataforma de computación en nube con servicios bajo demanda.
2. Capa gratuita con límites para practicar.
3. Para evitar cargos inesperados.
4. EC2 para cómputo/servidores, S3 para almacenamiento de objetos/hosting estático.
5. Tiene costo por hora/uso; usar solo si necesario y eliminarlo.
