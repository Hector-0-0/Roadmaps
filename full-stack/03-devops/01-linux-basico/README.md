# 01-linux-basico

## 1. Qué es y para qué sirve
Linux es un sistema operativo (Operating System) de código abierto, tipo Unix. Es ampliamente usado en servidores, contenedores, nube y dispositivos embebidos. Conocerlo es fundamental para DevOps y despliegue.

## 2. Por qué importa dentro del roadmap y cómo se conecta
La gran mayoría de servidores usan Linux. Se conecta con SSH, despliegue en EC2, automatización con Ansible y monitoreo.

## 3. Conceptos clave
- **Sistema de archivos (Filesystem)**: estructura jerárquica, / (raíz), /home, /etc, /var, /usr, /tmp.
- **Navegación y archivos**: pwd, ls, cd, find, cat, less, head, tail, touch, cp, mv, rm, mkdir, rmdir.
- **Permisos (permissions)**: lectura(r), escritura(w), ejecución(x), usuario/grupo/otros, chmod, chown, chgrp.
- **Usuarios y sudo (superuser do)**: usuarios, grupos, privilegios, sudoers.
- **Procesos (processes)**: ps, top, htop, kill, jobs, systemctl (systemd).
- **Redirecciones y pipes (pipes)**: >, >>, <, |, stdin/stdout/stderr.
- **Gestor de paquetes (package manager)**: apt (Debian/Ubuntu), yum/dnf (RHEL/Amazon Linux).
- **SSH (Secure Shell)**: conexión remota segura, claves públicas/privadas, puerto 22.
- **systemd**: sistema de inicialización y gestión de servicios.

## 4. Ejemplos de código comentados, correctos y ejecutables

### Ejemplo 1: Navegación y permisos
```bash
# Ver directorio actual
pwd

# Listar con detalles
ls -la

# Crear archivo y cambiar permisos
touch script.sh
chmod +x script.sh
ls -l script.sh
```

### Ejemplo 2: Redirecciones, pipes y procesos
```bash
# Guardar salida
echo "hola" > archivo.txt
cat archivo.txt

# Pipe: filtrar
ps aux | grep nginx

# Ver logs recientes
tail -n 20 /var/log/syslog 2>/dev/null || tail -n 20 /var/log/messages 2>/dev/null
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Usar `rm -rf /` o rutas peligrosas.
- Ejecutar comandos como root sin necesidad.
- Permisos incorrectos en claves SSH (debe ser 400/600).
- Modificar archivos del sistema sin entender.
- No verificar ruta antes de borrar.

Buenas prácticas:
- Usar `sudo` solo cuando necesario.
- Aprender rutas absolutas/relativas.
- Proteger claves SSH con permisos correctos.
- Usar man pages: `man <comando>`.
- Hacer backup conceptual antes de cambios críticos.
- Entender diferencia entre stop/disable en systemd.

## 6. Autoevaluación

1. ¿Qué es Linux y por qué se usa en servidores?
2. ¿Diferencia entre ruta absoluta y relativa?
3. ¿Qué significan permisos r,w,x?
4. ¿Para qué sirve sudo?
5. ¿Qué diferencia hay entre redirección > y pipe |?

Respuestas esperadas (orientativas):
1. Sistema operativo open source tipo Unix, estable y seguro para servidores.
2. Absoluta desde raíz (/), relativa desde directorio actual.
3. Lectura, escritura, ejecución para usuario/grupo/otros.
4. Ejecutar comando con privilegios elevados de forma controlada.
5. > redirige salida a archivo, | pasa salida como entrada a otro comando.
