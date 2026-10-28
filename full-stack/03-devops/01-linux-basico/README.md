# 01-linux-basico

## 1. Qué es y para qué sirve
Linux es un sistema operativo (SO) open source. Conocerlo es fundamental para servidores, despliegue y DevOps.

## 2. Conceptos clave

### Comandos básicos
```bash
pwd        # directorio actual
ls         # listar
cd         # cambiar directorio
mkdir      # crear directorio
rm         # eliminar
cp         # copiar
mv         # mover/renombrar
cat        # ver archivo
nano/vim   # editar
```

### Permisos
```bash
chmod +x script.sh
chown usuario:grupo archivo
```

### Procesos y red
```bash
ps aux
top/htop
curl
ssh usuario@ip
```

### Archivos importantes
- /etc/ hosts, configuración
- /var/log/ logs
- ~/.bashrc

## 3. Práctica orientativa
Navegar sistema, crear archivos, permisos, conectar por SSH.

## 4. Errores comunes y buenas prácticas
- Cuidado con rm -rf
- Entender permisos
- Usar sudo con precaución
- Aprender paths absolutos/relativos

## 5. Autoevaluación
1. ¿Qué es Linux?
2. ¿Diferencia entre ruta absoluta y relativa?
3. ¿Para qué sirve chmod?
4. ¿Qué es SSH?
5. ¿Por qué es importante en DevOps?

Respuestas orientativas:
1. SO open source basado en Unix.
2. Absoluta desde raíz vs relativa desde actual.
3. Cambiar permisos.
4. Conexión remota segura.
5. La mayoría de servidores usan Linux.
