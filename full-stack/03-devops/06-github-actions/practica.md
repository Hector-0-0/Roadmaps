# Práctica - 06-github-actions

## Nivel básico

1. **Workflow hola mundo**
   Enunciado: Crea `.github/workflows/hello.yml`. Configura trigger `on: push`. Crea job con runs-on `ubuntu-latest` y step que imprima "Hola desde GitHub Actions".
   Pista: Los workflows van en `.github/workflows/` con extensión `.yml` o `.yaml`. Sube el archivo y revisa pestaña Actions.
   Criterio verificable: Workflow aparece en Actions, se ejecuta en push y muestra el mensaje correctamente.

2. **Tests con Node.js**
   Enunciado: En repo con package.json, crea workflow que use `actions/checkout@v4` y `actions/setup-node@v4` con node-version `20`. Ejecuta `npm ci` y `npm test --if-present`.
   Pista: Usa `npm ci` en CI para instalaciones reproducibles. setup-node configura la versión correcta de Node.
   Criterio verificable: Workflow instala dependencias, ejecuta tests y finaliza con éxito.

3. **Matrix de versiones Node**
   Enunciado: Modifica workflow para usar `strategy.matrix` con node-version `[18, 20, 22]`. Usa `${{ matrix.node-version }}` en setup-node. Ejecuta tests en todas las versiones.
   Pista: Matrix ejecuta jobs en paralelo para cada combinación. Útil para asegurar compatibilidad entre versiones.
   Criterio verificable: Se ejecutan 3 jobs paralelos, uno por versión de Node, todos exitosos.

## Nivel intermedio

4. **Caché de dependencias npm**
   Enunciado: Añade caché con `actions/cache@v4` para `~/.npm` o usa `cache: 'npm'` en setup-node. Mide y documenta la diferencia de tiempo entre ejecuciones con y sin caché.
   Pista: setup-node soporta `cache: 'npm'` directamente. El caché acelera instalaciones en ejecuciones posteriores.
   Criterio verificable: Workflow usa caché correctamente, logs muestran cache hit/miss, instalación más rápida.

5. **Secrets y variables de entorno**
   Enunciado: Añade secret en GitHub Settings > Secrets. Usa `${{ secrets.MI_SECRETO }}` en env del step. Añade variable con `env:` y úsala. Nunca imprimas el valor completo del secret.
   Pista: Los secrets se enmascaran en logs. Usa variables para configuración no sensible, secrets para datos sensibles.
   Criterio verificable: Secret disponible en workflow sin exponerse en logs, variable de entorno usada correctamente.

6. **Artefactos de build**
   Enunciado: Genera archivos de build con script npm. Usa `actions/upload-artifact@v4` para guardar artefactos. Descarga con `actions/download-artifact@v4` o verifica en interfaz.
   Pista: Los artefactos persisten tras ejecución del job. Útiles para pasar archivos entre jobs o guardar resultados.
   Criterio verificable: Artefacto subido correctamente, visible en ejecución con archivos generados.

## Nivel desafío

7. **Despliegue condicionado a main con environments**
   Enunciado: Crea job de deploy con `needs: [test, build]`. Usa `if: github.ref == 'refs/heads/main'`. Configura environment en GitHub con protection rules. Usa secrets del environment.
   Pista: Environments permiten aprobaciones y secrets específicos. `needs` asegura que tests y build pasen antes de deploy.
   Criterio verificable: Deploy solo corre en push a main tras jobs exitosos, usa environment correcto, respeta condiciones.

8. **Workflow programado con cron**
   Enunciado: Crea workflow con `on.schedule` usando expresión cron (ej. `0 0 * * 1` para lunes a medianoche). Añade `workflow_dispatch` para ejecución manual. Documenta expresión cron.
   Pista: Cron usa formato UTC. `workflow_dispatch` permite probar manualmente. Verifica sintaxis con documentación GitHub.
   Criterio verificable: Workflow tiene trigger schedule y workflow_dispatch, sintaxis cron correcta, se puede ejecutar manualmente.
