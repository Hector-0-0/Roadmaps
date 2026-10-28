# Práctica - 03-devops/01-linux-basico

## Nivel básico

1. **Navegación y exploración del sistema**
   Enunciado: Abre una terminal Linux. Usa `pwd` para ver directorio actual, `ls -la` para listar con detalles, `cd` para navegar entre directorios. Explora `/home`, `/etc`, `/var/log`.
   Pista: Usa rutas absolutas y relativas. `..` sube un nivel, `.` directorio actual, `~` directorio home.
   Criterio verificable: Ejecuta los comandos y documenta la salida mostrando al menos 3 directorios diferentes con sus permisos.

2. **Crear, copiar, mover y eliminar archivos**
   Enunciado: Crea un directorio `practica-linux`. Dentro crea archivos con `touch`. Copia con `cp`, mueve/renombra con `mv`, elimina con `rm`. Usa `cat` para visualizar contenido.
   Pista: Usa `mkdir -p` si necesitas crear rutas. Ten cuidado con `rm -rf`. Usa `ls` para verificar cada operación.
   Criterio verificable: Se demuestra cada operación (crear, copiar, mover, renombrar, eliminar) con comandos y sus resultados verificables.

3. **Permisos con chmod y chown**
   Enunciado: Crea un archivo `script.sh` con contenido `echo "Hola"`. Dale permisos de ejecución con `chmod +x`. Cambia permisos numéricos (ej. 644, 755). Experimenta con `chown` si tienes permisos.
   Pista: Permisos: r=4, w=2, x=1. 755 = rwxr-xr-x, 644 = rw-r--r--. Usa `ls -l` para verificar.
   Criterio verificable: `ls -l script.sh` muestra permisos correctos después de cada cambio y el script se ejecuta con `./script.sh`.

## Nivel intermedio

4. **Usuarios, grupos y sudo**
   Enunciado: Verifica usuario actual con `whoami`, grupos con `groups`. Usa `sudo` para ejecutar comando con privilegios. Entiende la diferencia entre usuario normal y root.
   Pista: Usa `id` para ver UID/GID. Solo usa sudo cuando necesario. Nunca uses root para operaciones diarias.
   Criterio verificable: Se documenta usuario, grupos y se ejecuta un comando con sudo mostrando el comportamiento correcto.

5. **Procesos, redirecciones y pipes**
   Enunciado: Lista procesos con `ps aux`. Usa `top` o `htop` para monitorear. Usa redirección `>` y `>>` para guardar salida. Usa pipe `|` para filtrar (ej. `ps aux | grep bash`).
   Pista: `>` sobrescribe, `>>` añade. `|` pasa salida de un comando como entrada a otro. Combina comandos para filtrar.
   Criterio verificable: Se demuestra redirección (archivo creado con contenido), pipe (filtrado funcional) y monitoreo de procesos.

6. **SSH, claves y conexión remota**
   Enunciado: Genera par de claves SSH con `ssh-keygen`. Configura permisos correctos en `~/.ssh` (700) y archivos clave (600). Documenta cómo conectarse con `ssh usuario@host`.
   Pista: Usa `chmod 700 ~/.ssh && chmod 600 ~/.ssh/*`. Nunca compartas la clave privada. Usa `ssh -i` para especificar clave.
   Criterio verificable: Claves generadas, permisos correctos verificados con `ls -la ~/.ssh/`, y se documenta el comando SSH correcto.

## Nivel desafío

7. **Gestor de paquetes y servicios con systemd**
   Enunciado: Actualiza repositorios con el gestor de paquetes de tu distro (apt update o yum check-update). Instala un paquete (ej. curl). Usa `systemctl` para verificar estado de un servicio, iniciar/detener si es posible.
   Pista: Usa `systemctl status <servicio>`, `systemctl start/stop/restart`. Algunos comandos requieren sudo.
   Criterio verificable: Paquete instalado verificado con `which` o `dpkg -l`/`rpm -q`, servicio gestionado con systemctl mostrando estados correctos.

8. **Script bash automatizado**
   Enunciado: Crea un script `backup.sh` que haga copia de archivos con fecha en nombre, use variables, condicionales y registre log. Dale permisos de ejecución y pruébalo.
   Pista: Usa `date +%Y%m%d`, variables `$VAR`, `if [ -f archivo ]`, redirección para log. Usa `#!/bin/bash` en primera línea.
   Criterio verificable: Script se ejecuta correctamente, crea copia con fecha, genera log, usa variables y condicionales funcionando.
