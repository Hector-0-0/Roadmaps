# Checkpoint 07 - Paquetes externos

## Objetivo del checkpoint
Consolidar el uso de paquetes externos de npm (Node Package Manager) instalados desde el registro (registry), gestionando package.json, scripts y versiones para integrar funcionalidades en una aplicación frontend o Node.js.

## Conocimientos que consolida
- [04-javascript](../04-javascript/README.md): lógica, DOM y eventos.
- [06-npm](../06-npm/README.md): inicialización, dependencias, devDependencies, scripts y package-lock.json.

## 3 ideas de proyecto de dificultad creciente

### 1. Proyecto 1: Generador de fechas con dayjs (Dificultad: básica)
**Descripción:** Crear una página o script que muestre fechas formateadas usando un paquete externo como dayjs.

**Requisitos funcionales:**
- Inicializar proyecto con npm (`npm init -y`).
- Instalar `dayjs` como dependencia.
- Crear script para mostrar fecha/hora actual con al menos dos formatos distintos.
- Usar un script definido en `package.json` para ejecutar el programa.

**Habilidades que practica:**
- Gestión de dependencias, import/require de paquetes externos, uso de scripts npm.

**Criterios de aceptación:**
- Existe `package.json` con la dependencia registrada.
- Existe `package-lock.json` tras instalar.
- Al ejecutar el script (`npm run ...`) se muestran fechas formateadas correctamente.
- No se commitea `node_modules`.

**Mejoras opcionales:**
- Agregar `dayjs/plugin/relativeTime` para mostrar tiempo relativo.
- Permitir pasar un idioma distinto.

### 2. Proyecto 2: Validador de formularios con validator.js (Dificultad: intermedia)
**Descripción:** Crear un formulario HTML con validación usando el paquete `validator` (validator.js) para validar correo, URL o contraseñas.

**Requisitos funcionales:**
- Proyecto npm con `package.json`.
- Instalar `validator` como dependencia.
- Crear formulario con campos (correo, URL o teléfono) y botón de validar.
- Validar con funciones de `validator` y mostrar mensajes de error/acierto en el DOM.
- Ejecutar con un script (puede usar bundler ligero o solo Node; si es navegador, usar herramienta que permita importar el paquete).

**Habilidades que practica:**
- Integración de paquetes externos con lógica de validación, manipulación DOM, gestión de versiones.

**Criterios de aceptación:**
- Se instala y usa `validator` correctamente.
- Se validan al menos dos tipos distintos de dato.
- Se muestran mensajes claros al usuario.
- `package.json` lista correctamente la dependencia usada.

**Mejoras opcionales:**
- Agregar sanitización con funciones de `validator`.
- Mostrar validación en tiempo real con eventos.

### 3. Proyecto 3: Generador de PDFs o reportes con pdf-lib (Dificultad: intermedia-avanzada)
**Descripción:** Crear un script Node.js que use `pdf-lib` para generar un PDF con información desde un objeto/array, demostrando uso avanzado de paquetes externos.

**Requisitos funcionales:**
- Inicializar proyecto npm, crear `package.json` con scripts.
- Instalar `pdf-lib` como dependencia.
- Generar un PDF con al menos título, contenido y una lista.
- Guardar el archivo en disco usando `fs`.
- Añadir script `generate` en `package.json` para ejecutar la generación.

**Habilidades que practica:**
- Uso de API de paquete externo, trabajo con archivos, automatización con scripts npm, control de versiones de dependencias.

**Criterios de aceptación:**
- `pdf-lib` aparece en dependencies de `package.json`.
- Al ejecutar `npm run generate` se crea un archivo PDF válido.
- El código usa la API del paquete (no se genera el PDF manualmente).
- Se incluye un breve README o comentarios que indiquen el paquete usado y su versión.

**Mejoras opcionales:**
- Agregar imágenes o fuentes.
- Leer datos desde un archivo JSON y generar PDF dinámicamente.
