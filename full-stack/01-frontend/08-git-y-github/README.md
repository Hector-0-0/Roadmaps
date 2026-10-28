# 08-git-y-github

## 1. Qué es y para qué sirve
Git (sistema de control de versiones distribuido) es una herramienta para rastrear cambios en código. GitHub (plataforma para alojar repositorios Git) permite colaborar, revisar código y gestionar proyectos.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Esencial para trabajo colaborativo, historial de cambios y despliegue. Se usa en todo el roadmap.

## 3. Conceptos clave

### Comandos básicos
```bash
git init
git add .
git commit -m "mensaje"
git status
git log  oneline
git branch
git checkout -b rama
git merge rama
git push origin main
git pull origin main
```

### Flujo básico
1. Modificar archivos
2. `git add` (staging area, área de preparación)
3. `git commit` (guardar snapshot)
4. `git push` (subir a remoto)

### GitHub
- Repositorio remoto
- Pull Request (PR, solicitud de extracción)
- Issues (incidencias)
- Fork (bifurcación)

## 4. Ejemplos de código comentados, correctos y ejecutables

```bash
# Inicializar repo
git init
git config user.name "Nombre"
git config user.email "correo@ejemplo.com"
echo "# Mi proyecto" > README.md
git add README.md
git commit -m "docs: agrega README"
git branch -M main
git remote add origin https://github.com/usuario/repo.git
git push -u origin main
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Hacer commits con mensajes vagos.
- Commitear archivos sensibles.
- No usar .gitignore.
- Hacer push a main sin revisar.

Buenas prácticas:
- Mensajes descriptivos en español o siguiendo convención.
- Usar ramas para features.
- Hacer pull antes de push cuando hay colaboración.
- Revisar cambios con `git diff`.

## 6. Autoevaluación

1. ¿Diferencia entre Git y GitHub?
2. ¿Qué hace `git add`?
3. ¿Qué es un commit?
4. ¿Qué es una rama (branch)?
5. ¿Para qué sirve un Pull Request?

Respuestas orientativas:
1. Git es herramienta, GitHub es plataforma.
2. Pasa archivos al área de preparación.
3. Snapshot de cambios con mensaje.
4. Línea independiente de desarrollo.
5. Solicitar revisión e integración de cambios.
