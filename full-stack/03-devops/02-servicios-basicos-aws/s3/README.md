# s3 (Simple Storage Service)

## 1. Qué es y para qué sirve
S3 (Simple Storage Service) es almacenamiento de objetos escalable. Permite guardar archivos (objetos) en buckets con alta durabilidad.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Ideal para hosting estático, archivos, backups. Se conecta con despliegue y CI/CD.

## 3. Conceptos clave
- **Bucket**: contenedor único a nivel global para objetos.
- **Objeto**: archivo + metadatos almacenados en bucket.
- **Clases de almacenamiento**: Standard, IA, Glacier (conceptos).
- **Versionado**: mantiene versiones de objetos.
- **Políticas de bucket**: controlan acceso.
- **Static website hosting**: servir sitio estático directamente desde S3.
- **Block Public Access**: bloquea acceso público por defecto.

## 4. Ejemplos de código comentados, correctos y ejecutables
Conceptual:
```text
Bucket: mi-sitio-estatico-123
Subir index.html, styles.css
Habilitar static website hosting
Configurar bucket policy si necesario (con cuidado)
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Hacer bucket público sin necesidad.
- Olvidar Block Public Access.
- Nombres de bucket no únicos globalmente.
- No eliminar objetos/buckets.

Buenas prácticas:
- Principio de menor privilegio.
- Usar políticas restrictivas.
- Versionado si hay cambios frecuentes.
- Eliminar recursos al terminar práctica.
- Usar Free Tier.

## 6. Autoevaluación

1. ¿Qué es S3?
2. ¿Diferencia entre bucket y objeto?
3. ¿Para qué sirve static website hosting?
4. ¿Qué es versionado?
5. ¿Por qué tener cuidado con acceso público?

Respuestas esperadas (orientativas):
1. Almacenamiento de objetos escalable.
2. Bucket contenedor, objeto archivo almacenado.
3. Servir HTML/CSS/JS como sitio web estático.
4. Guardar versiones anteriores de objetos.
5. Puede exponer datos públicamente si mal configurado.
