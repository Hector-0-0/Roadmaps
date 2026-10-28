# 06-github-actions

## 1. Qué es y para qué sirve
GitHub Actions es una plataforma de CI/CD (Continuous Integration/Continuous Delivery) integrada a GitHub. Permite automatizar flujos de trabajo como pruebas, build y despliegue cada vez que ocurre un evento en el repositorio.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Automatiza validación de código y despliegues. Se conecta con Git, repositorio y despliegue a servicios como S3/EC2.

## 3. Conceptos clave
- **Workflow (flujo de trabajo)**: archivo YAML en .github/workflows/.
- **Events (eventos)**: disparadores (push, pull_request, schedule, workflow_dispatch).
- **Jobs (trabajos)**: conjunto de steps que corren en mismo runner.
- **Steps (pasos)**: acciones o comandos individuales.
- **Actions (acciones)**: piezas reutilizables (actions/checkout).
- **Runners (ejecutores)**: máquinas donde corren jobs (ubuntu-latest).
- **Secrets (secretos)**: variables sensibles (tokens, claves).
- **Matrix (matriz)**: ejecutar en múltiples versiones/sistemas.
- **Cache (caché)**: acelerar builds cacheando dependencias.

## 4. Ejemplos de código comentados, correctos y ejecutables

### Ejemplo 1: Workflow básico CI
```yaml
# .github/workflows/ci.yml
name: CI Basico

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout código
        uses: actions/checkout@v4
      - name: Ejecutar prueba simple
        run: echo "Ejecutando pruebas..."
```

### Ejemplo 2: Pipeline completo test y despliegue (conceptual)
```yaml
# .github/workflows/deploy.yml
name: Test y Despliegue

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Instalar Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      - name: Instalar dependencias
        run: npm ci
      - name: Ejecutar tests
        run: npm test --if-present

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Desplegar (ejemplo)
        run: echo "Desplegando..."
        env:
          DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Exponer secretos en logs.
- No usar `npm ci` en CI.
- Workflows muy largos sin dividir jobs.
- Olvidar `needs` para dependencias.
- No validar YAML.

Buenas prácticas:
- Usar secrets para datos sensibles.
- Cachear dependencias.
- Usar versiones fijas de actions.
- Ejecutar solo en branches relevantes.
- Mantener workflows simples y legibles.

## 6. Autoevaluación

1. ¿Qué es CI/CD?
2. ¿Qué es un workflow en GitHub Actions?
3. ¿Diferencia entre job y step?
4. ¿Para qué sirven los secrets?
5. ¿Qué hace `needs` en un job?

Respuestas esperadas (orientativas):
1. Integración continua/entrega continua automatizada.
2. Archivo YAML que define automatización ante eventos.
3. Job es conjunto de steps en un runner, step es acción/comando individual.
4. Almacenar datos sensibles de forma segura.
5. Define dependencia para ejecutar después de otro job.
