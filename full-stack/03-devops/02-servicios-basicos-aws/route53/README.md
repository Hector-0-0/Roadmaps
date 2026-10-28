# route53 (Amazon Route 53)

## 1. Qué es y para qué sirve
Route 53 es el servicio DNS (Domain Name System, sistema de nombres de dominio) gestionado de AWS. Permite registrar dominios, gestionar zonas alojadas y enrutar tráfico a recursos AWS.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Permite exponer aplicaciones con nombre de dominio. Se conecta con EC2, S3 (static hosting), y despliegue.

## 3. Conceptos clave
- **Hosted zone (zona alojada)**: contenedor para registros DNS de un dominio.
- **Record types (tipos de registro)**: A (IPv4), AAAA (IPv6), CNAME (alias a nombre), MX (correo), TXT (texto/verificación).
- **TTL (Time To Live)**: tiempo en segundos que los resolvers cachean el registro.
- **Alias record**: registro especial AWS para apuntar a recursos AWS (sin costo extra de consulta en muchos casos).
- **Routing policies** (concepto): simple, weighted, latency, failover.

## 4. Ejemplos de código comentados, correctos y ejecutables
Conceptual:
```text
Registro A: ejemplo.com -> IP pública EC2
Registro CNAME: www.ejemplo.com -> ejemplo.com
Registro TXT: para verificación (ej. SES/otros)
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Usar CNAME en zona apex (raíz) cuando no es posible.
- TTL muy bajo/alto sin entender propagación.
- Olvidar actualizar registros al cambiar IP (usar Elastic IP o Alias).
- Dejar zonas alojadas sin uso.

Buenas prácticas:
- Usar Alias cuando apuntas a recursos AWS.
- Entender propagación DNS (puede tardar minutos).
- Eliminar zonas alojadas de práctica si no necesarias.
- Tener cuidado con registro de dominios (puede tener costo).

## 6. Autoevaluación

1. ¿Qué es Route 53?
2. ¿Diferencia entre registro A y CNAME?
3. ¿Qué es TTL?
4. ¿Cuándo usar Alias record?
5. ¿Qué es una hosted zone?

Respuestas esperadas (orientativas):
1. DNS gestionado de AWS.
2. A apunta a IP, CNAME apunta a otro nombre DNS.
3. Tiempo de cacheo del registro DNS.
4. Para apuntar a recursos AWS (ELB, CloudFront, S3) eficientemente.
5. Contenedor de registros DNS para un dominio.
