# Práctica - vpc

## Nivel básico
1. **Crear VPC** (criterio de terminado: demostrable)
   Enunciado: Crea una VPC con CIDR 10.0.0.0/16.
   Pista: Usa VPC Wizard o manual. Documenta CIDR elegido.
   Advertencia de costos: En Free Tier usualmente sin cargo por VPC; gateways sí pueden generar costo. Usa NAT Gateway con cuidado.

2. **Subredes** (criterio de terminado: demostrable)
   Enunciado: Crea una subred pública y una privada en distintas AZs.
   Pista: Asigna CIDR distintos, sin solapamiento.
   Advertencia de costos: Sin costo mayor. Eliminar al terminar.

## Nivel intermedio
3. **Internet Gateway y rutas** (criterio de terminado: demostrable)
   Enunciado: Adjunta IGW a VPC y configura route table de subred pública hacia IGW.
   Pista: Asocia route table a subred pública.
   Advertencia de costos: IGW sin costo, pero tráfico sí; practica controlado.

4. **NAT Gateway (conceptual/práctico)** (criterio de terminado: demostrable)
   Enunciado: Crea NAT Gateway en subred pública y ruta desde subred privada. Entiende diferencia con IGW.
   Pista: NAT Gateway genera costo por hora/uso; si no es necesario, solo documenta configuración.
   Advertencia de costos: NAT Gateway tiene cargo en Free Tier contexto; recomienda simular o destruir inmediatamente. Configura alerta de facturación.

## Nivel desafío
5. **Seguridad SG vs NACL** (criterio de terminado: demostrable)
   Enunciado: Configura Security Group permisivo solo necesario y NACL con reglas básicas. Prueba concepto stateful/stateless.
   Pista: Documenta diferencia con ejemplo.
   Advertencia de costos: Eliminar VPC, subredes, IGW, NAT Gateway al terminar. Verificar recursos huérfanos.
