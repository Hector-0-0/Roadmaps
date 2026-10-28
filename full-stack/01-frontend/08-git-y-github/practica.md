# Práctica - 08-git-y-github

## Nivel básico

1. **Configurar Git e inicializar repositorio**
   Enunciado: Configura `user.name` y `user.email` globalmente con los datos correctos. Crea una carpeta, inicializa repositorio con `git init`, crea un `README.md` y haz tu primer commit.
   Pista: Usa `git config --global user.name` y `git config --global user.email`. Verifica con `git config --list`.
   Criterio verificable: `git log --oneline` muestra al menos un commit con autor correcto y mensaje descriptivo.

2. **Staging, commits y .gitignore**
   Enunciado: Crea varios archivos, usa `git add` selectivamente y `git add .`. Crea `.gitignore` para ignorar `node_modules/` y un archivo `.env`. Verifica con `git status`.
   Pista: `git add -p` permite añadir cambios por trozos. Usa `.gitignore` antes de hacer commit de archivos sensibles.
   Criterio verificable: Solo los archivos correctos están en staging/commiteados, `node_modules` y `.env` aparecen ignorados en git status.

3. **Historial y diferencias**
   Enunciado: Haz al menos 3 commits con mensajes descriptivos. Usa `git log`, `git log --oneline`, `git diff` y `git diff --staged` para revisar cambios.
   Pista: Escribe mensajes claros que describan qué se hizo. Revisa diferencias antes de hacer commit.
   Criterio verificable: `git log --oneline` muestra 3 o más commits con mensajes descriptivos y `git diff` muestra cambios correctamente.

## Nivel intermedio

4. **Ramas: crear, cambiar y fusionar**
   Enunciado: Crea una rama `feature/nueva-funcionalidad`, cambia a ella, haz cambios y commits. Vuelve a `main` y fusiona la rama con `git merge`. Elimina la rama fusionada.
   Pista: Usa `git switch` o `git checkout`. Asegúrate de estar en la rama correcta antes de mergear.
   Criterio verificable: La funcionalidad aparece en main tras merge, la rama feature fue fusionada correctamente y puedes verificar con `git log --oneline --graph`.

5. **Repositorio remoto en GitHub**
   Enunciado: Crea un repositorio en GitHub, conéctalo con `git remote add origin <url>`, cambia rama a main si es necesario y sube con `git push -u origin main`.
   Pista: Usa HTTPS o SSH según tu configuración. Verifica con `git remote -v`.
   Criterio verificable: El repositorio remoto tiene los commits subidos y `git remote -v` muestra fetch/push correctos.

6. **Sincronización: pull y push**
   Enunciado: Simula cambios remotos (edita desde GitHub) y trae cambios con `git pull`. Haz cambios locales y sube con `git push`. Resuelve cualquier conflicto simple si ocurre.
   Pista: Siempre haz `git pull` antes de `git push` cuando trabajas con remoto. Usa `git status` para ver estado.
   Criterio verificable: Los cambios remotos aparecen localmente tras pull, los cambios locales aparecen en GitHub tras push.

## Nivel desafío

7. **Pull Request simulado con ramas**
   Enunciado: Crea rama feature, haz cambios significativos, sube la rama con `git push -u origin <rama>`. Documenta el proceso para crear un Pull Request en GitHub (descripción, reviewers conceptuales). Fusiona vía merge.
   Pista: Un PR permite revisión de código antes de fusionar. Documenta cambios, propósito y pruebas realizadas.
   Criterio verificable: Rama feature existe en remoto, hay commits distintos a main, y se documenta el flujo completo de PR con pasos claros.

8. **Resolución de conflictos**
   Enunciado: Crea un conflicto intencionalmente: modifica la misma línea en main y en una rama feature, intenta fusionar y resuelve el conflicto manualmente editando los marcadores `<<<<<<<`, `=======`, `>>>>>>>`. Completa el merge con commit.
   Pista: Lee cuidadosamente los marcadores. Elige qué cambios mantener o combina ambos. Elimina los marcadores tras resolver.
   Criterio verificable: El conflicto se resuelve correctamente, el archivo queda sin marcadores de conflicto, el merge commit se crea y el código funciona correctamente.
