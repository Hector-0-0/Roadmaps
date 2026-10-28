# vpc (Virtual Private Cloud)

## 1. Qué es y para qué sirve
VPC (Virtual Private Cloud, nube privada virtual) es una red virtual aislada dentro de AWS. Permite definir rangos IP, subredes, tablas de rutas, gateways y controlar el tráfico de red.

## 2. Por qué importa dentro del roadmap y cómo se conecta
VPC define la red donde corren EC2 y otros servicios. Es fundamental para entender seguridad de red y despliegue aislado.

## 3. Conceptos clave
- **CIDR (Classless Inter-Domain Routing)**: rango de direcciones IP (ej. 10.0.0.0/16).
- **Subnet (subred)**: segmento de red dentro de VPC, puede ser pública o privada.
- **Route Table (tabla de rutas)**: reglas que definen hacia dónde va el tráfico.
- **Internet Gateway (IGW)**: permite comunicación entre VPC e internet.
- **NAT Gateway (Network Address Translation Gateway)**: permite salida a internet desde subredes privadas sin exponerlas.
- **Security Groups (grupos de seguridad)**: firewall a nivel de instancia (stateful).
- **NACLs (Network Access Control Lists, listas de control de acceso de red)**: firewall a nivel de subred (stateless).

## 4. Ejemplos de código comentados, correctos y ejecutables
Conceptual:
```text
VPC: 10.0.0.0/16
  Public Subnet: 10.0.1.0/24 -> route to IGW
  Private Subnet: 10.0.2.0/24 -> route to NAT Gateway
```
Nota: usar rango no superpuesto con otras redes.

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Confundir Security Groups (stateful) con NACLs (stateless).
- Exponer subred privada directamente a internet.
- Usar rangos CIDR demasiado grandes o conflictivos.
- Olvidar tabla de rutas al crear subred.

Buenas prácticas:
- Separar públicas/privadas.
- Usar NACLs como capa extra, Security Groups como principal.
- Diseñar con principio de menor privilegio.
- Eliminar recursos VPC creados en práctica.

## 6. Autoevaluación

1. ¿Qué es una VPC?
2. ¿Diferencia entre subred pública y privada?
3. ¿Qué función tiene Internet Gateway?
4. ¿Diferencia entre Security Group y NACL?
5. ¿Para qué sirve NAT Gateway?

Respuestas esperadas (orientativas):
1. Red virtual aislada en AWS.
2. Pública tiene ruta a IGW, privada suele salir vía NAT o sin ruta directa.
3. Conecta VPC con internet.
4. SG stateful a nivel instancia, NACL stateless a nivel subred.
5. Permite salida a internet desde subredes privadas.
