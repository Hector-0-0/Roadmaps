# ses (Simple Email Service)

## 1. Qué es y para qué sirve
SES (Simple Email Service) es un servicio de envío de emails transaccionales y masivos de AWS. Permite enviar correos desde aplicaciones de forma escalable.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Necesario para notificaciones, verificación, recuperación de contraseña. Se conecta con backend y despliegue.

## 3. Conceptos clave
- **Identidad (Identity)**: dominio o dirección de correo verificada.
- **Sandbox (modo sandbox)**: modo inicial con límites, solo a direcciones verificadas.
- **Production access (acceso a producción)**: requiere solicitud para enviar a cualquier destinatario.
- **SMTP (Simple Mail Transfer Protocol)**: protocolo para enviar emails.
- **API**: envío programático vía AWS SDK.
- **SPF (Sender Policy Framework)**: registro DNS para autorizar servidores de envío.
- **DKIM (DomainKeys Identified Mail)**: firma digital para autenticación.
- **Reputación de envío**: importante para evitar spam.

## 4. Ejemplos de código comentados, correctos y ejecutables
Conceptual:
```text
1. Verificar email/dominio
2. En modo sandbox, verificar destinatario
3. Enviar vía SMTP o API
4. Configurar SPF/DKIM en DNS
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Intentar enviar a destinatarios no verificados en sandbox.
- No configurar SPF/DKIM.
- Usar credenciales SMTP incorrectas.
- Enviar spam o sin consentimiento.

Buenas prácticas:
- Empezar en sandbox y entender límites.
- Verificar identidades.
- Configurar autenticación DNS.
- Monitorear reputación.
- Eliminar identidades de prueba.

## 6. Autoevaluación

1. ¿Qué es Amazon SES?
2. ¿Diferencia entre sandbox y producción?
3. ¿Diferencia entre SMTP y API?
4. ¿Para qué sirven SPF y DKIM?
5. ¿Qué es una identidad en SES?

Respuestas esperadas (orientativas):
1. Servicio de envío de emails transaccional.
2. Sandbox limita a destinatarios verificados; producción requiere solicitud.
3. SMTP protocolo estándar, API más integrado con AWS SDK.
4. Autenticación para mejorar entregabilidad y evitar spoofing.
5. Dominio o email verificado para enviar desde ahí.
