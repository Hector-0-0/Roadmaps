# 06-npm

## 1. Qué es y para qué sirve
npm (Node Package Manager, gestor de paquetes de Node) es el gestor de paquetes por defecto para Node.js. Sirve para instalar, actualizar y gestionar librerías (bibliotecas) y herramientas de terceros.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Permite reutilizar código, usar herramientas como bundlers (empaquetadores) o linters (analizadores), y gestionar dependencias. Se conecta con JavaScript y con proyectos más grandes.

## 3. Conceptos clave

### package.json
Archivo que describe el proyecto: nombre, versión, dependencias, scripts.
```json
{
  "name": "mi-proyecto",
  "version": "1.0.0",
  "scripts": {
    "dev": "node app.js"
  },
  "dependencies": {
    "lodash": "^4.17.21"
  }
}
```

### Dependencias
- dependencies (dependencias de producción)
- devDependencies (dependencias de desarrollo)

### Comandos básicos
```bash
npm init -y        # inicializar
npm install <pkg>  # instalar paquete
npm install        # instalar todas las dependencias
npm run <script>   # ejecutar script
```

### node_modules
Carpeta con paquetes instalados. No debe commitearse normalmente.

### package-lock.json
Bloquea versiones exactas para instalaciones reproducibles.

## 4. Ejemplos de código comentados, correctos y ejecutables

```bash
mkdir mi-proyecto && cd mi-proyecto
npm init -y
npm install dayjs
```

```javascript
// app.js
const dayjs = require('dayjs');
console.log(dayjs().format('YYYY-MM-DD'));
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Commitear node_modules.
- No usar .gitignore.
- Instalar todo global sin razón.
- Confundir dependencies/devDependencies.

Buenas prácticas:
- Usar .gitignore con node_modules.
- Usar scripts en package.json.
- Revisar paquetes antes de instalar.
- Mantener package-lock.json.

## 6. Autoevaluación

1. ¿Qué es npm?
2. ¿Qué diferencia hay entre dependencies y devDependencies?
3. ¿Para qué sirve package.json?
4. ¿Debemos commitear node_modules?
5. ¿Qué hace npm install?

Respuestas orientativas:
1. Gestor de paquetes para Node.js.
2. Producción vs desarrollo.
3. Describe proyecto y dependencias/scripts.
4. No, es muy grande; se instala con npm install.
5. Instala dependencias según package.json.
