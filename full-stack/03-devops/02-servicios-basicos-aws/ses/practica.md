# Práctica - 03-devops/02-servicios-basicos-aws/ses

## Nivel básico

1. **Verificar identidad de correo en SES**
   Enunciado: En AWS SES en modo sandbox, verifica una dirección de correo electrónico propia como identidad. Revisa el correo de verificación y confirma la identidad desde la consola.
   Pista: Usa AWS Free Tier con precaución. Solo podrás enviar a direcciones verificadas mientras estés en sandbox. Configura una alerta de facturación antes de empezar.
   Criterio verificable: La identidad aparece como "Verified" en SES. Se documenta el correo usado y la fecha de verificación. Al terminar, elimina la identidad si es de prueba.

2. **Verificar destinatario en sandbox**
   Enunciado: Verifica una segunda dirección de correo (destinatario) para poder enviarle correos en modo sandbox. Confirma la verificación desde ambos correos.
   Pista: En modo sandbox ambos remitente y destinatario deben estar verificados. Guarda evidencia de las verificaciones.
   Criterio verificable: Ambas identidades aparecen verificadas en SES y se pueden usar para pruebas. Se documenta el proceso.

## Nivel intermedio

3. **Enviar correo de prueba desde consola**
   Enunciado: Desde la consola de SES, envía un correo de prueba entre las dos direcciones verificadas. Verifica recepción en bandeja de entrada (revisa spam si es necesario).
   Pista: Usa un asunto y cuerpo claros. Revisa los límites de sandbox. No envíes a direcciones no verificadas.
   Criterio verificable: El correo llega a la bandeja de entrada del destinatario verificado. Se documenta remitente, destinatario, asunto y resultado.

4. **Publicar registros DKIM y verificar con dig**
   Enunciado: Habilita Easy DKIM para la identidad verificada. AWS generará registros CNAME para DKIM. Publica esos registros CNAME en tu zona DNS (Route 53 o tu proveedor). Usa `dig` o `nslookup` para verificar que los registros DKIM resuelven correctamente.
   Pista: Usa `dig <registro-dkim> CNAME` o `nslookup -type=CNAME <registro-dkim>`. Espera propagación DNS (puede tardar minutos). SPF/DKIM mejoran entregabilidad.
   Criterio verificable: Los registros DKIM aparecen como publicados en SES, y `dig`/`nslookup` muestran los registros CNAME correctos resolviéndose.

## Nivel desafío

5. **Configurar SPF y verificar**
   Enunciado: Añade un registro TXT SPF en tu zona DNS para autorizar a SES a enviar desde tu dominio o desde amazonses.com según tu configuración. Verifica con `dig` que el registro TXT SPF resuelve correctamente.
   Pista: Ejemplo SPF puede ser `v=spf1 include:amazonses.com ~all`. Usa `dig TXT <dominio>` para verificar. Documenta el registro exacto publicado.
   Criterio verificable: El registro SPF TXT está publicado y `dig TXT` muestra el registro correcto resolviéndose.

6. **Prueba completa de autenticación**
   Enunciado: Con DKIM y SPF configurados, envía otro correo de prueba. Documenta el estado de autenticación (DKIM/SPF) visible en los headers del correo recibido si es posible.
   Pista: Revisa headers completos del correo recibido para ver resultados de autenticación. Compara con el envío sin DKIM/SPF.
   Criterio verificable: Se documenta configuración DNS (DKIM CNAME + SPF TXT), verificación con dig/nslookup, envío exitoso y análisis de autenticación.

7. **Entender sandbox vs producción**
   Enunciado: Documenta diferencias entre sandbox y producción, límites actuales, proceso para solicitar producción. No solicites producción innecesariamente, solo documenta el proceso completo.
   Pista: Lee la documentación de SES sobre moving out of sandbox. Entiende requisitos y riesgos.
   Criterio verificable: Documento completo con diferencias, límites, requisitos para salir de sandbox y pasos detallados.

8. **Limpieza obligatoria**
   Enunciado: Elimina las identidades de correo verificadas en SES. Elimina los registros DNS creados para pruebas (DKIM CNAME, SPF TXT). Verifica que no queden identidades activas y documenta la limpieza.
   Pista: Usa AWS Free Tier con precaución. Verifica en consola SES que no hay identidades de prueba.
   Criterio verificable: No quedan identidades verificadas de prueba en SES, registros DNS de prueba eliminados, checklist de limpieza completado.
