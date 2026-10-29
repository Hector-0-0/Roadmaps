# Práctica - 03-devops/02-servicios-basicos-aws/vpc

## Nivel básico

1. **Crear VPC con CIDR correcto**
   Enunciado: En AWS VPC, crea una VPC con CIDR block `10.0.0.0/16`. Habilita DNS hostnames y DNS resolution. Documenta la configuración.
   Pista: Usa AWS Free Tier. La VPC en sí no tiene costo significativo, pero presta atención a gateways. Configura alerta de facturación.
   Criterio verificable: VPC creada con CIDR correcto, DNS hostnames y resolution habilitados, visible en consola VPC.

2. **Crear subred pública y privada**
   Enunciado: Crea una subred pública `10.0.1.0/24` y una subred privada `10.0.2.0/24` en diferentes zonas de disponibilidad. Asigna nombres descriptivos.
   Pista: Asegúrate de que los rangos CIDR no se solapen. Usa diferentes AZ para práctica de alta disponibilidad.
   Criterio verificable: Ambas subredes creadas en AZs distintas con rangos correctos y mapeadas a la VPC.

## Nivel intermedio

3. **Internet Gateway y rutas para subred pública**
   Enunciado: Crea un Internet Gateway, adjúntalo a la VPC. Crea/edita la tabla de rutas de la subred pública para enrutar `0.0.0.0/0` al Internet Gateway. Asocia la tabla de rutas a la subred pública.
   Pista: La subred pública necesita ruta al IGW para tener acceso a internet. Verifica la asociación de tabla de rutas.
   Criterio verificable: IGW adjuntado, ruta 0.0.0.0/0 hacia IGW en tabla de rutas, subred pública asociada correctamente.

4. **Crear NAT Gateway y enrutar subred privada**
   Enunciado: En la subred pública, crea un NAT Gateway asignando una Elastic IP nueva. En la tabla de rutas de la subred privada, añade ruta `0.0.0.0/0` hacia el NAT Gateway. 
   Pista: ADVERTENCIA: NAT Gateway tiene costo por hora y por GB procesado. Usa solo para esta práctica, elimínalo inmediatamente después. Configura alerta de facturación.
   Criterio verificable: NAT Gateway en estado Available, Elastic IP asociada, ruta hacia NAT Gateway en tabla de rutas de subred privada.

5. **Verificar conectividad desde instancia privada**
   Enunciado: Lanza una instancia EC2 en la subred privada (sin IP pública). Lanza otra instancia EC2 en la subred pública con clave SSH. Desde la instancia pública conéctate por SSH a la instancia privada usando su IP privada. Desde la instancia privada prueba salida a internet con `curl -I https://www.google.com`.
   Pista: Configura Security Groups correctamente para permitir SSH entre instancias. Usa clave SSH desde instancia bastión.
   Criterio verificable: SSH desde bastión a instancia privada funciona, curl desde instancia privada recibe respuesta exitosa demostrando salida a internet vía NAT Gateway.

## Nivel desafío

6. **Configurar Security Groups y NACLs**
   Enunciado: Configura Security Groups con reglas mínimas necesarias (SSH solo desde origenes permitidos). Crea/configura NACLs para la subred privada con reglas explícitas. Documenta diferencias stateful vs stateless.
   Pista: Security Groups son stateful, NACLs stateless. Ambos se aplican, NACLs a nivel subred, SGs a nivel instancia.
   Criterio verificable: Reglas aplicadas correctamente, pruebas de conectividad demuestran funcionamiento, documentación clara de diferencias.

7. **Probar aislamiento de subred privada**
   Enunciado: Desde internet intenta conectar directamente a la instancia en subred privada por SSH. Desde internet intenta conectar a instancia en subred pública. Documenta resultados.
   Pista: Instancia privada no debe tener ruta directa desde internet. Solo debe ser accesible vía bastión.
   Criterio verificable: Conexión directa a instancia privada falla desde internet, conexión a instancia pública funciona según reglas de SG, aislamiento verificado.

8. **Limpieza obligatoria**
   Enunciado: Elimina en orden correcto: instancias EC2, NAT Gateway (espera a que se elimine), Elastic IP, Internet Gateway (desasociar primero), subredes, tablas de rutas, Security Groups, NACLs personalizados, finalmente VPC. Verifica que no queden recursos.
   Pista: Algunos recursos dependen de otros. Elimina NAT Gateway primero entre gateways, espera su eliminación completa. Verifica en todas las regiones si es necesario.
   Criterio verificable: Lista de verificación de limpieza completada, no quedan recursos activos en VPC, NAT Gateway eliminado (verifica facturación), todo documentado.
