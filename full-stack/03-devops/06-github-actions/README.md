# 06-github-actions

## 1. Qué es y para qué sirve
GitHub Actions es CI/CD (Continuous Integration/Continuous Delivery, integración continua/entrega continua) integrado a GitHub. Automatiza tests, builds, despliegues.

## 2. Conceptos clave
- Workflow (flujo de trabajo)
- Jobs, Steps, Actions
- YAML
- Triggers (push, pull_request)
- Secrets

```yaml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: echo "tests"
```

## 3. Recursos
- **GitHub Actions Docs** (verificar enlace)

## 4. Autoevaluación
1. ¿Qué es CI/CD?
2. ¿Qué es GitHub Actions?
3. ¿Qué es un workflow?
4. ¿Para qué sirven secrets?
5. ¿Ventaja de automatizar?
