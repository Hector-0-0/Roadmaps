# 08-ansible

## 1. Qué es y para qué sirve
Ansible es una herramienta de automatización IT (Infrastructure Automation) agentless (sin agente). Permite configurar servidores, desplegar aplicaciones y orquestar tareas usando archivos YAML.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Automatiza configuración repetitiva en múltiples servidores. Se conecta con Linux, SSH, despliegue y Terraform.

## 3. Conceptos clave
- **Inventory (inventario)**: lista de hosts/servidores a gestionar (INI/YAML).
- **Playbook (libro de jugadas)**: archivo YAML con plays y tasks.
- **Play**: asociación entre hosts y tasks.
- **Task**: acción a ejecutar.
- **Module (módulo)**: unidad reutilizable (apt, yum, copy, service).
- **Idempotencia**: ejecutar mismo playbook múltiples veces da mismo resultado.
- **Variables**: parametrizar playbooks.
- **Handlers**: tareas que se ejecutan solo si otra task notifica cambio.
- **Roles**: organizar playbooks en estructura reutilizable.
- **Ad-hoc commands**: comandos rápidos sin playbook.

## 4. Ejemplos de código comentados, correctos y ejecutables

### Ejemplo 1: Inventory
```ini
# inventory.ini
[web]
servidor1 ansible_host=192.168.1.10 ansible_user=ubuntu

[db]
servidor2 ansible_host=192.168.1.11 ansible_user=ubuntu
```

### Ejemplo 2: Playbook completo comentado
```yaml
# playbook-nginx.yml
---
- name: Instalar y configurar Nginx
  hosts: web
  become: true  # usar sudo
  vars:
    puerto: 80
  tasks:
    - name: Actualizar cache de apt
      apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Instalar nginx
      apt:
        name: nginx
        state: present

    - name: Copiar página de inicio
      copy:
        src: ./index.html
        dest: /var/www/html/index.html
        owner: www-data
        group: www-data
        mode: '0644'
      notify: Reiniciar nginx

    - name: Asegurar nginx iniciado
      service:
        name: nginx
        state: started
        enabled: true

  handlers:
    - name: Reiniciar nginx
      service:
        name: nginx
        state: restarted
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Olvidar `become: true` para tareas con privilegios.
- No probar en entorno de prueba.
- Usar rutas absolutas incorrectas.
- No entender idempotencia.
- Cometer secretos en playbooks.

Buenas prácticas:
- Usar inventory por entorno.
- Aprovechar idempotencia de módulos.
- Usar roles para proyectos grandes.
- Usar variables y vault para secretos.
- Probar con `--check` cuando sea posible.

## 6. Autoevaluación

1. ¿Qué es Ansible y qué significa agentless?
2. ¿Qué es un inventory?
3. ¿Diferencia entre task y handler?
4. ¿Qué es idempotencia?
5. ¿Cuándo usar roles?

Respuestas esperadas (orientativas):
1. Herramienta de automatización sin agentes en servidores remotos (usa SSH).
2. Lista de hosts a gestionar.
3. Task se ejecuta siempre, handler solo si hay cambio notificado.
4. Ejecutar múltiples veces produce mismo estado.
5. Para organizar y reutilizar playbooks complejos.
