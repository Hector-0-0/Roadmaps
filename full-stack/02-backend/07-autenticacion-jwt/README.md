# 07-autenticacion-jwt

## 1. Qué es y para qué sirve
Autenticación (verificación de identidad) confirma quién es el usuario. Autorización (permiso) define qué puede hacer. JWT (JSON Web Token, token web JSON) es un estándar para transmitir información segura entre partes como token.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Esencial para apps con usuarios, roles y protección de rutas. Se conecta con APIs y aplicación completa.

## 3. Conceptos clave

### Flujo básico
1. Usuario envía credenciales
2. Servidor valida y genera JWT
3. Cliente envía JWT en header Authorization: Bearer <token>
4. Servidor verifica token

### Estructura JWT
Header.Payload.Signature

```javascript
// Ejemplo con jsonwebtoken (concepto)
const jwt = require('jsonwebtoken');
const token = jwt.sign({ id: user.id }, 'secret', { expiresIn: '1h' });
jwt.verify(token, 'secret');
```

### Seguridad básica
- Usar HTTPS en producción
- Secret (clave secreta) fuerte
- Expiración de tokens
- No guardar datos sensibles en payload
- Hash de contraseñas (bcrypt)

## 4. Errores comunes y buenas prácticas

Errores comunes:
- Guardar contraseña en texto plano.
- Usar secret débil.
- No expirar tokens.
- Confiar en payload sin verificar.

Buenas prácticas:
- Usar bcrypt para passwords.
- Tokens con expiración.
- Verificar en middleware.
- Considerar refresh tokens (avanzado).

## 5. Autoevaluación

1. ¿Diferencia entre autenticación y autorización?
2. ¿Qué es JWT?
3. ¿Cómo se envía JWT?
4. ¿Por qué hashear contraseñas?
5. ¿Qué pasa si alguien roba un JWT?

Respuestas orientativas:
1. Identidad vs permisos.
2. Token firmado para transmitir claims.
3. Header Authorization: Bearer token.
4. Proteger si hay filtración.
5. Podría usarse hasta expirar; por eso expiración + medidas.
