# Práctica - s3

## Nivel básico
1. **Crear bucket** (criterio de terminado: demostrable)
   Enunciado: Crea bucket con nombre único global.
   Pista: Revisar reglas de nombres.
   Advertencia de costos: Free Tier limitado; eliminar bucket.

2. **Subir archivos** (criterio de terminado: demostrable)
   Enunciado: Sube index.html y assets.
   Pista: Estructura correcta.
   Advertencia de costos: Almacenamiento pequeño sin costo mayor.

## Nivel intermedio
3. **Static website hosting** (criterio de terminado: demostrable)
   Enunciado: Habilita hosting estático y accede por endpoint.
   Pista: Configurar index/error document.
   Advertencia de costos: Tráfico pequeño; eliminar recursos.

4. **Permisos y políticas** (criterio de terminado: demostrable)
   Enunciado: Entiende Block Public Access y bucket policy. Hazlo solo si necesario y reversible.
   Pista: Mejor usar con cuidado, documentar.
   Advertencia de costos: Revisar permisos.

## Nivel desafío
5. **Versionado y limpieza** (criterio de terminado: demostrable)
   Enunciado: Habilita versionado, sube nueva versión, luego deshabilita/limpia y elimina bucket y objetos.
   Pista: Eliminar todas las versiones.
   Advertencia de costos: OBLIGATORIO eliminar bucket vacío o con objetos/versiones. Verificar no queden recursos.
