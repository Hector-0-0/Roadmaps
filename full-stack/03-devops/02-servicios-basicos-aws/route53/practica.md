# Práctica - 03-devops/02-servicios-basicos-aws/route53

## Nivel básico

1. **Crear zona alojada y entender costos**
   Enunciado: En Route 53 crea una hosted zone pública para un dominio de prueba (si no tienes dominio propio, documenta con dominio ficticio). Anota los nameservers NS asignados. Elimina la zona al final.
   Pista: ADVERTENCIA: Hosted zones tienen costo mensual en AWS. Usa solo para práctica corta y elimina inmediatamente. Configura alerta de facturación.
   Criterio verificable: Zona alojada creada, nameservers documentados, recordatorios de costo y eliminación anotados.

2. **Registro A hacia instancia EC2**
   Enunciado: Lanza una instancia EC2 con IP pública (o usa Elastic IP). Crea un registro A en Route 53 apuntando tu dominio/subdominio a la IP pública. Espera propagación DNS.
   Pista: Usa Elastic IP para evitar cambio de IP al stop/start. TTL razonable como 300 segundos.
   Criterio verificable: Registro A creado, resolución con `dig +short <dominio>` o `nslookup` muestra IP correcta.

3. **CNAME y efecto del TTL**
   Enunciado: Crea un registro CNAME para `www` apuntando al dominio raíz. Cambia TTL de un registro y observa propagación. Usa `dig` para verificar TTL.
   Pista: CNAME apunta a otro nombre DNS, no a IP. TTL determina tiempo de cacheo en resolutores DNS.
   Criterio verificable: CNAME resuelve correctamente, `dig` muestra TTL del registro, diferencias entre TTLs documentadas.

## Nivel intermedio

4. **Registro TXT y MX**
   Enunciado: Crea un registro TXT para verificación (ej. texto de prueba). Crea un registro MX con prioridad para simular configuración de correo. Verifica ambos con `dig`.
   Pista: TXT se usa para verificaciones, MX define servidores de correo con prioridad numérica menor = mayor prioridad.
   Criterio verificable: Registros TXT y MX creados, `dig TXT` y `dig MX` muestran valores correctos.

5. **Enrutamiento ponderado entre dos registros**
   Enunciado: Crea dos registros A con mismo nombre pero diferente peso (weighted routing). Usa dos IPs diferentes. Documenta comportamiento de distribución.
   Pista: Weighted routing distribuye tráfico según peso asignado. Suma de pesos determina proporción.
   Criterio verificable: Dos registros con routing policy weighted creados con pesos diferentes, configuración documentada.

## Nivel desafío

6. **Zona privada asociada a VPC**
   Enunciado: Crea una hosted zone privada y asóciala a tu VPC. Crea un registro A interno apuntando a IP privada de EC2. Desde instancia en la misma VPC resuelve el nombre con `nslookup` o `dig`.
   Pista: Las zonas privadas solo resuelven desde VPC asociada. No son accesibles desde internet.
   Criterio verificable: Zona privada asociada a VPC, registro interno resuelve desde instancia dentro de VPC, no resuelve desde fuera.

7. **Pruebas DNS con herramientas**
   Enunciado: Usa `dig`, `nslookup`, `host` para resolver registros creados. Compara resultados desde diferentes perspectivas. Documenta tiempos de propagación.
   Pista: `dig` muestra información detallada, `nslookup` interactivo, `host` simple. Verifica desde terminal local.
   Criterio verificable: Las tres herramientas muestran resolución correcta, se documentan diferencias y tiempos.

8. **Limpieza obligatoria**
   Enunciado: Elimina todos los registros DNS creados. Elimina la hosted zone pública (y privada si creada). Verifica eliminación completa. Documenta costos asociados.
   Pista: Las hosted zones tienen cargo mientras existan. Elimina todos los registros antes de eliminar la zona.
   Criterio verificable: Zona alojada eliminada, sin registros restantes, checklist de limpieza completado.
