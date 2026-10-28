# Práctica - 06-github-actions

## Nivel básico
1. **Primer workflow** (criterio de terminado: demostrable)
   Enunciado: Crea `.github/workflows/ci.yml` que se ejecute en push a main y muestre mensaje.
   Pista: Usa evento `on: push` y step con `run: echo`.
   Criterio verificable: Workflow aparece en Actions y corre exitosamente.

2. **Checkout y setup** (criterio de terminado: demostrable)
   Enunciado: Agrega `actions/checkout@v4` y `actions/setup-node@v4` si es Node.
   Pista: Revisa sintaxis YAML.
   Criterio verificable: Steps se ejecutan en orden sin errores.

## Nivel intermedio
3. **Tests con npm** (criterio de terminado: demostrable)
   Enunciado: Ejecuta `npm ci` y `npm test  if-present`.
   Pista: Usa proyecto con package.json.
   Criterio verificable: Workflow instala deps y ejecuta tests.

4. **Secrets** (criterio de terminado: demostrable)
   Enunciado: Configura un secret en Settings > Secrets y úsalo con `${{ secrets.NOMBRE }}`.
   Pista: Nunca imprimas el valor completo.
   Criterio verificable: Se accede al secret sin exponerlo en logs.

## Nivel desafío
5. **Pipeline completo test+deploy** (criterio de terminado: demostrable)
   Enunciado: Crea pipeline con job test y job deploy con `needs: test`, usando secrets.
   Pista: Deploy puede ser echo simulado si no hay destino real.
   Criterio verificable: Deploy solo corre si test pasa y en branch correcto.
