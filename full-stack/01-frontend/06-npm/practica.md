# Práctica - 06-npm

## Nivel básico

1. **Inicializar proyecto con npm**
   Enunciado: Crea una carpeta nueva, inicialízala con `npm init -y` y examina el archivo `package.json` generado. Añade una descripción y autor manualmente.
   Pista: Usa `npm init -y` para inicialización rápida. Luego edita `package.json` con un editor de texto.
   Criterio verificable: Existe `package.json` con nombre, versión, descripción, autor y main correctamente definidos.

2. **Instalar y usar un paquete**
   Enunciado: Instala el paquete `dayjs` como dependencia con `npm install dayjs`. Crea un archivo `app.js` que lo use para mostrar la fecha actual en formato `YYYY-MM-DD`.
   Pista: Usa `require('dayjs')` en CommonJS o `import` según configuración. Ejecuta con `node app.js`.
   Criterio verificable: Al ejecutar el script se muestra la fecha en formato correcto y `dayjs` aparece en dependencies de `package.json`.

3. **Dependencias de desarrollo**
   Enunciado: Instala `nodemon` como devDependency con `npm install --save-dev nodemon`. Añade un script `dev` en `package.json` que ejecute tu archivo con nodemon.
   Pista: Las devDependencies son para herramientas de desarrollo. Usa `--save-dev` o `-D`.
   Criterio verificable: `nodemon` aparece en devDependencies, el script `dev` existe en package.json y `npm run dev` reinicia al guardar cambios.

## Nivel intermedio

4. **Scripts personalizados**
   Enunciado: Crea al menos tres scripts en `package.json`: `start`, `dev` y `test` (con un comando simple como echo). Ejecuta cada uno con `npm run`.
   Pista: Los scripts pueden encadenar comandos con `&&`. Usa `npm run <nombre>` para ejecutarlos.
   Criterio verificable: Los tres scripts existen y se ejecutan correctamente mostrando la salida esperada.

5. **package-lock.json y node_modules**
   Enunciado: Observa `package-lock.json` y `node_modules`. Crea un `.gitignore` con `node_modules/`. Verifica con `git status` que node_modules no esté trackeado.
   Pista: `package-lock.json` debe commitearse para reproducibilidad. `node_modules` nunca debe commitearse.
   Criterio verificable: Existe `.gitignore` con `node_modules/`, `node_modules` no aparece en staging de git, `package-lock.json` existe.

6. **Instalar desde package.json**
   Enunciado: Elimina la carpeta `node_modules` con `rm -rf node_modules`. Ejecuta `npm install` para reinstalar todas las dependencias desde `package.json` y `package-lock.json`.
   Pista: Esto simula clonar un repo y restaurar dependencias. Debe reinstalar exactamente las versiones del lock file.
   Criterio verificable: Tras `npm install`, `node_modules` se recrea con los paquetes correctos y la app funciona igual que antes.

## Nivel desafío

7. **Proyecto con dos paquetes externos**
   Enunciado: Instala dos paquetes externos (ej. `dayjs` y `chalk`). Crea un script que use ambos: formatea una fecha con dayjs y muestra el resultado con colores usando chalk.
   Pista: Revisa la API de cada paquete en su documentación. Usa `require` o `import` según corresponda.
   Criterio verificable: Al ejecutar el script se muestra la fecha formateada con colores en terminal, ambos paquetes en package.json.

8. **Proyecto completo con scripts y estructura**
   Enunciado: Crea un proyecto completo con estructura organizada (src/, package.json, .gitignore), scripts para dev y start, al menos una dependencia y una devDependency. Documenta comandos en un README breve.
   Pista: Organiza código en `src/app.js`. Usa scripts para ejecutar desde `src/`.
   Criterio verificable: Proyecto funcional con estructura correcta, scripts ejecutables, dependencias registradas, `.gitignore` correcto y sin `node_modules` commiteado.
