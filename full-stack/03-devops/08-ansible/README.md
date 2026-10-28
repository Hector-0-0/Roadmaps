# 08-ansible

## 1. Qué es y para qué sirve
Ansible es herramienta de automatización (IT automation). Usa YAML, agentless (sin agente), para configurar servidores.

## 2. Conceptos clave
- Inventory (inventario)
- Playbook (libro de jugadas)
- Tasks, Modules
- Idempotencia (idempotente)
- SSH

```yaml
- hosts: web
  tasks:
    - name: Instalar nginx
      apt:
        name: nginx
        state: present
```

## 3. Recursos
- **Ansible Docs** (verificar enlace)

## 4. Autoevaluación
1. ¿Qué es Ansible?
2. ¿Qué significa agentless?
3. ¿Qué es un playbook?
4. ¿Qué es idempotencia?
5. ¿Cuándo usarlo?
