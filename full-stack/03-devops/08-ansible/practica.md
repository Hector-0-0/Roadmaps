# Práctica - 08-ansible

## Nivel básico
1. **Inventory** (criterio de terminado: demostrable)
   Enunciado: Crea `inventory.ini` con grupo [web] y variables ansible_host/ansible_user.
   Pista: Usa IP de prueba o localhost según entorno.
   Criterio verificable: Inventory válido, parseable por ansible.

2. **Ad-hoc ping** (criterio de terminado: demostrable)
   Enunciado: Ejecuta `ansible all -i inventory.ini -m ping`.
   Pista: Requiere SSH configurado.
   Criterio verificable: Respuesta pong de hosts alcanzables.

## Nivel intermedio
3. **Playbook instalar paquete** (criterio de terminado: demostrable)
   Enunciado: Crea playbook para instalar nginx con apt/yum usando `become: true`.
   Pista: Usa módulo correcto según SO.
   Criterio verificable: Playbook idempotente (correr 2 veces sin cambios innecesarios).

4. **Handlers** (criterio de terminado: demostrable)
   Enunciado: Copia archivo de config y reinicia servicio con handler al cambiar archivo.
   Pista: Usa `notify` y `handlers`.
   Criterio verificable: Servicio reinicia solo si hay cambio.

## Nivel desafío
5. **Playbook completo comentado** (criterio de terminado: demostrable)
   Enunciado: Crea playbook completo: actualizar cache, instalar nginx, copiar index, iniciar servicio, con variables y handlers.
   Pista: Comenta cada task.
   Criterio verificable: Ejecuta correctamente, idempotente, bien estructurado.
