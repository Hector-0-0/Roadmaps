# 07-autenticacion-jwt

## 1. Qué es y para qué sirve
Autenticación verifica la identidad del usuario. Autorización determina qué recursos puede acceder. JWT (JSON Web Token) es un token compacto y firmado usado para transmitir información de forma segura entre cliente y servidor.

## 2. Por qué importa dentro del roadmap y cómo se conecta
Fundamental para proteger rutas, manejar sesiones sin estado (stateless) y construir aplicaciones con usuarios. Se conecta con APIs RESTful, Node.js y la app completa.

## 3. Conceptos clave
- **Autenticación vs autorización**: identidad vs permisos.
- **JWT estructura**: header.payload.signature (Base64URL).
- **Firma (signature)**: garantiza integridad y autenticidad.
- **Expiración (exp)**: tiempo de validez del token.
- **Access token y refresh token**: corto y largo plazo.
- **Almacenamiento seguro**: evitar localStorage para tokens sensibles en ciertos casos; considerar httpOnly cookies.
- **Hash de contraseñas**: usar bcrypt para nunca guardar en texto plano.
- **Middleware de autenticación**: verificar token en rutas protegidas.
- **Vulnerabilidades comunes**: tokens robados, secretos débiles, no expirar, guardar datos sensibles en payload.

## 4. Ejemplos de código comentados, correctos y ejecutables

### Ejemplo 1: Generar y verificar JWT
```javascript
const jwt = require('jsonwebtoken');

// Generar token
function generarToken(usuario) {
  // payload con info mínima (no contraseña)
  const payload = { id: usuario.id, rol: usuario.rol };
  // firmar con secreto y expiración
  return jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '1h' });
}

// Verificar token
function verificarToken(token) {
  try {
    return jwt.verify(token, process.env.JWT_SECRET);
  } catch (error) {
    return null;
  }
}

module.exports = { generarToken, verificarToken };
```

### Ejemplo 2: Middleware de autenticación
```javascript
const { verificarToken } = require('./auth');

function authMiddleware(req, res, next) {
  const header = req.headers.authorization || '';
  const token = header.startsWith('Bearer ') ? header.slice(7) : null;
  if (!token) return res.status(401).json({ error: 'Token requerido' });
  const decoded = verificarToken(token);
  if (!decoded) return res.status(401).json({ error: 'Token inválido o expirado' });
  req.usuario = decoded;
  next();
}

module.exports = authMiddleware;
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Guardar contraseñas en texto plano.
- Poner datos sensibles en payload JWT.
- Usar secretos débiles o hardcodeados.
- No expirar tokens.
- Almacenar tokens de forma insegura.

Buenas prácticas:
- Usar bcrypt para hash de contraseñas.
- JWT_SECRET fuerte en variables de entorno.
- Access token corto, refresh token con rotación.
- Verificar token con middleware.
- Usar HTTPS en producción.
- Validar permisos por rol en autorización.

## 6. Autoevaluación

1. ¿Diferencia entre autenticación y autorización?
2. ¿Qué partes tiene un JWT?
3. ¿Por qué no guardar contraseñas en texto plano?
4. ¿Diferencia entre access token y refresh token?
5. ¿Cómo proteger rutas con JWT?

Respuestas esperadas (orientativas):
1. Autenticación identifica, autorización define permisos.
2. Header, payload, signature.
3. Si hay filtración, se exponen contraseñas; usar hash (bcrypt).
4. Access corto para acceso, refresh más largo para obtener nuevo access token.
5. Usar middleware que verifique token en header Authorization: Bearer.
