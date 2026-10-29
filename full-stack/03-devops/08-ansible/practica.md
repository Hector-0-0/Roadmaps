# Práctica - 08-ansible

## Nivel básico

1. **Inventario y conexión SSH**
   Enunciado: Crea `inventory.ini` con un grupo `[web]` y al menos un host con `ansible_host` y `ansible_user`. Configura acceso SSH por clave. Verifica conectividad.
   Pista: Usa formato INI para inventory. Asegúrate de que la clave SSH tenga permisos correctos con `chmod 600`.
   Criterio verificable: Inventory válido, conexión SSH funcional al host objetivo.

2. **Ping con ansible ad-hoc**
   Enunciado: Ejecuta `ansible all -i inventory.ini -m ping`. Verifica respuesta `pong`. Prueba con grupo específico `[web]`.
   Pista: El módulo ping de Ansible verifica conectividad y Python disponible. Si falla, revisa SSH y permisos.
   Criterio verificable: Todos los hosts responden `pong` exitosamente, salida muestra success.

3. **Playbook idempotente para instalar nginx**
   Enunciado: Crea playbook `nginx.yml` con `become: true` para instalar nginx usando módulo `apt` (o `yum`). Ejecuta dos veces y compara cambios.
   Pista: Ansible es idempotente, segunda ejecución debe mostrar `changed=0` para tareas ya cumplidas. Usa `state: present`.
   Criterio verificable: Primera ejecución instala nginx, segunda ejecución muestra `changed=0`, nginx corriendo tras playbook.

## Nivel intermedio

4. **Variables y plantillas Jinja2**
   Enunciado: Usa variables en playbook. Crea plantilla `index.html.j2` con variable. Usa módulo `template` para copiarla a `/var/www/html/index.html`. Cambia variable y vuelve a ejecutar.
   Pista: Las plantillas Jinja2 usan `{{ variable }}`. El módulo template es idempotente.
   Criterio verificable: Página servida con contenido de plantilla, cambio de variable actualiza contenido correctamente.

5. **Handlers para reiniciar servicios**
   Enunciado: Modifica configuración o archivo con módulo `copy` o `template`. Usa `notify` para llamar handler que reinicie nginx con módulo `service`. Verifica que reinicia solo cuando hay cambios.
   Pista: Handlers se ejecutan al final si son notificados. Si no hay cambios, handler no se ejecuta.
   Criterio verificable: Al cambiar archivo se notifica y reinicia nginx, al ejecutar sin cambios handler no se ejecuta.

6. **Roles con ansible-galaxy**
   Enunciado: Crea rol con `ansible-galaxy init roles/nginx`. Organiza tasks, handlers, templates en estructura de rol. Usa rol en playbook con `roles:`.
   Pista: La estructura de roles sigue convenciones de Ansible. Los archivos se buscan automáticamente en directorios del rol.
   Criterio verificable: Rol creado con estructura correcta, playbook usa rol, nginx configurado correctamente.

## Nivel desafío

7. **Secretos con ansible-vault**
   Enunciado: Crea archivo cifrado con `ansible-vault create secrets.yml`. Guarda variable sensible. Usa en playbook con `vars_files`. Ejecuta con `--ask-vault-pass` o vault password file.
   Pista: Nunca commitees secretos sin cifrar. Usa `ansible-vault edit/view/encrypt/decrypt` según necesites.
   Criterio verificable: Archivo cifrado no muestra secretos en texto plano, playbook accede a variables correctamente con vault, ejecución exitosa.

8. **Modo check, diff y verificación completa**
   Enunciado: Ejecuta playbook con `--check --diff` para ver cambios propuestos sin aplicar. Aplica con normalidad. Verifica idempotencia ejecutando 3 veces.
   Pista: `--check` hace dry-run, `--diff` muestra diferencias. Útil para validar antes de aplicar cambios en producción.
   Criterio verificable: --check muestra cambios propuestos, ejecución normal aplica correctamente, tercera ejecución muestra changed=0 mayoritariamente confirmando idempotencia.
