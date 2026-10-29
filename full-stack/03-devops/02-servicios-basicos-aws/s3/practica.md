# Práctica - 03-devops/02-servicios-basicos-aws/s3

## Nivel básico

1. **Crear bucket S3 y subir objetos**
   Enunciado: En AWS S3 (Free Tier), crea un bucket con nombre único global. Sube al menos dos archivos usando la consola. Lista los objetos del bucket con AWS CLI usando `aws s3 ls s3://nombre-bucket/`.
   Pista: Los nombres de bucket son únicos a nivel global. Usa AWS CLI configurado con credenciales válidas. Verifica que la región sea correcta.
   Criterio verificable: Bucket creado, archivos subidos visibles en consola, comando AWS CLI muestra los objetos listados correctamente.

2. **Activar versionado y recuperar objeto borrado**
   Enunciado: Activa versionado en el bucket. Sube un archivo, modifica y vuelve a subir (nueva versión). Elimina el archivo y recupera una versión anterior desde la consola o CLI.
   Pista: Con versionado activado, objetos eliminados quedan marcados con delete marker. Puedes restaurar versiones anteriores.
   Criterio verificable: Versionado habilitado, múltiples versiones visibles, archivo recuperado correctamente tras eliminación.

3. **Block Public Access y permisos**
   Enunciado: Intenta hacer público un objeto con Block Public Access activado. Observa el error 403. Configura bucket policy o permisos correctamente entendiendo las restricciones. Documenta el comportamiento.
   Pista: Block Public Access bloquea acceso público por defecto por seguridad. Usa con precaución y solo para hosting estático si es necesario.
   Criterio verificable: Se demuestra bloqueo con error 403, se entiende configuración de Block Public Access, política aplicada correctamente solo si justificado.

## Nivel intermedio

4. **Hosting estático completo**
   Enunciado: Sube `index.html`, `style.css` y opcionalmente `app.js`. Habilita Static website hosting con documento index `index.html`. Accede por la URL del endpoint y verifica que CSS se carga correctamente.
   Pista: Los archivos deben tener nombres correctos. Configura permisos adecuadamente. Usa rutas relativas en HTML/CSS.
   Criterio verificable: Sitio accesible por endpoint S3, HTML y CSS se cargan correctamente, navegación funciona sin errores.

5. **Regla de ciclo de vida**
   Enunciado: Crea una regla de ciclo de vida para mover objetos a clase de almacenamiento más económica (ej. Standard-IA) tras 30 días, o para eliminar versiones antiguas. Prueba la configuración.
   Pista: Las reglas de ciclo de vida automatizan transición entre clases para ahorrar costos. Documenta la regla creada.
   Criterio verificable: Regla de ciclo de vida configurada correctamente, visible en configuración del bucket con condiciones y acciones definidas.

6. **URL prefirmada con expiración**
   Enunciado: Genera una URL prefirmada para un objeto privado usando AWS CLI `aws s3 presign` con tiempo de expiración (ej. 3600 segundos). Prueba acceso con la URL y tras expiración.
   Pista: Las URLs prefirmadas permiten acceso temporal sin hacer público el objeto. El tiempo de expiración es configurable.
   Criterio verificable: URL prefirmada funciona dentro del tiempo, deja de funcionar tras expiración, objeto permanece privado.

## Nivel desafío

7. **Subir archivo desde Node.js con AWS SDK v3**
   Enunciado: Instala `@aws-sdk/client-s3`. Crea script Node.js para subir archivo a S3 usando credenciales configuradas. Lista objetos tras subida con script.
   Pista: Usa AWS SDK v3 con comandos. Configura credenciales con AWS CLI o variables de entorno. Maneja errores correctamente.
   Criterio verificable: Script sube archivo correctamente, aparece en bucket, listado desde SDK muestra el archivo.

8. **Vaciar y eliminar bucket (limpieza obligatoria)**
   Enunciado: Vacía el bucket eliminando todos los objetos y versiones (si hay versionado). Elimina el bucket completamente. Verifica desde consola que no existe. Usa AWS CLI para automatizar si es posible.
   Pista: ADVERTENCIA: Usa AWS Free Tier con precaución. Un bucket con objetos o versiones no se puede eliminar hasta vaciarlo completamente. Documenta pasos de limpieza.
   Criterio verificable: Bucket vacío y eliminado exitosamente, no aparece en listado de buckets, checklist de limpieza completado.
