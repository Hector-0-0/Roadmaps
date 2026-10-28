# Práctica - route53

## Nivel básico
1. **Entender zonas alojadas** (criterio de terminado: demostrable)
   Enunciado: Crea una hosted zone para un dominio de prueba (o simulado). Observa nameservers.
   Pista: Documenta NS records.
   Advertencia de costos: Registro de dominio tiene costo; puedes usar dominio propio o solo zona alojada de prueba. Verifica Free Tier.

2. **Registros básicos** (criterio de terminado: demostrable)
   Enunciado: Crea registro A apuntando a IP de EC2 (usar Elastic IP recomendado).
   Pista: Usa TTL razonable (300).
   Advertencia de costos: Consultas DNS pequeñas suelen baratas; elimina registros no usados.

## Nivel intermedio
3. **CNAME y TXT** (criterio de terminado: demostrable)
   Enunciado: Crea CNAME para www y registro TXT para verificación.
   Pista: Diferencia uso.
   Advertencia de costos: Sin costo significativo.

4. **Propagación** (criterio de terminado: demostrable)
   Enunciado: Verifica con nslookup/dig desde terminal.
   Pista: `dig +short ejemplo.com` o `nslookup`.
   Advertencia de costos: Herramientas locales sin costo.

## Nivel desafío
5. **Apuntar dominio a instancia** (criterio de terminado: demostrable)
   Enunciado: Apunta dominio a EC2 (con Elastic IP) usando registro A o Alias. Documenta pasos y propagación.
   Pista: Usa Elastic IP para evitar cambio de IP al stop/start.
   Advertencia de costos: OBLIGATORIO eliminar hosted zone/records si son de prueba. Cuidado con registro de dominio.
