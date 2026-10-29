# Práctica - 02-backend/07-autenticacion-jwt

## Nivel básico

1. **Generar y decodificar un token JWT**
   Enunciado: Instala `jsonwebtoken`. Crea un script que genere un token con payload `{ id: 1, rol: 'usuario' }` usando una clave secreta. Decodifica el token con `jwt.decode` y verifica su estructura (header, payload).
   Pista: Usa `jwt.sign(payload, secreto, { expiresIn: '1h' })`. Recuerda que decode no verifica firma, solo lee el contenido.
   Criterio verificable: El script genera un token, lo decodifica y muestra header y payload correctamente sin errores.

2. **Verificar firma y rechazar token manipulado**
   Enunciado: Genera un token válido con `jwt.sign`. Modifica manualmente una parte del token (cambia un carácter). Usa `jwt.verify` con la misma clave secreta y comprueba que rechaza el token manipulado.
   Pista: Un token JWT tiene tres partes separadas por puntos. Si modificas cualquier parte, la firma deja de coincidir y verify debe lanzar error.
   Criterio verificable: Token original verificado correctamente, token manipulado lanzado como error y capturado con try/catch mostrando rechazo.

3. **Token expirado y respuesta 401**
   Enunciado: Genera un token con expiración muy corta `expiresIn: '1s'`. Espera 2 segundos y verifica con `jwt.verify`. Maneja el error `TokenExpiredError` y retorna lógica que simule respuesta 401.
   Pista: Usa `setTimeout` para esperar. Captura el error específico y verifica su nombre con `err.name`.
   Criterio verificable: Antes de expirar verify funciona, tras expirar lanza TokenExpiredError y se identifica correctamente.

## Nivel intermedio

4. **Hash de contraseñas con bcrypt**
   Enunciado: Instala `bcrypt`. Genera un hash de una contraseña con `bcrypt.hash(password, 10)`. Verifica con `bcrypt.compare` que la contraseña correcta coincide y una incorrecta no coincide.
   Pista: Nunca almacenes contraseñas en texto plano. Usa salt rounds entre 10 y 12. El hash generado es diferente cada vez pero compare funciona correctamente.
   Criterio verificable: Hash generado, compare con contraseña correcta retorna true, compare con incorrecta retorna false.

5. **Middleware de autenticación en Express**
   Enunciado: Crea una API con Express. Implementa ruta `POST /login` que genere token. Implementa middleware `auth` que verifique token en header `Authorization: Bearer <token>`. Protege ruta `GET /perfil` retornando 200 con datos si token válido, 401 sin token o con token inválido.
   Pista: Extrae el token con `req.headers.authorization.split(' ')[1]`. Usa el middleware antes del handler de la ruta protegida.
   Criterio verificable: Sin token retorna 401, con token válido retorna 200 con datos del usuario, con token inválido retorna 401.

6. **Access token y refresh token**
   Enunciado: Genera access token con expiración corta (15m) y refresh token con expiración larga (7d). Crea ruta para refrescar token usando refresh token válido. Rechaza refresh token expirado o inválido.
   Pista: Usa claves secretas distintas para access y refresh si es posible. Almacena lógica para validar refresh token.
   Criterio verificable: Login genera ambos tokens, endpoint /refresh devuelve nuevo access token con refresh válido, rechaza con 401 si refresh inválido o expirado.

## Nivel desafío

7. **Cookie httpOnly vs localStorage**
   Enunciado: Implementa dos formas: enviar token en respuesta JSON (simulando localStorage) y enviar token en cookie httpOnly con flags `httpOnly`, `secure`, `sameSite`. Documenta vulnerabilidades: XSS puede robar de localStorage, CSRF es riesgo de cookies.
   Pista: Usa `res.cookie()` de Express. httpOnly impide acceso desde JavaScript. Entiende tradeoffs de seguridad entre ambos enfoques.
   Criterio verificable: Ambas implementaciones funcionan, se documentan diferencias, riesgos y cuándo usar cada una.

8. **Secret débil y ataque alg none**
   Enunciado: Demuestra riesgo de secreto débil (intenta verificar con secreto vacío o común). Muestra por qué es peligroso no especificar algoritmo. Configura `jwt.verify` con algoritmo explícito y rechaza tokens con algoritmo none o inesperado.
   Pista: Usa `algorithms: ['HS256']` explícitamente en verify. Nunca aceptes algoritmo none. Usa secretos fuertes en variables de entorno.
   Criterio verificable: Con algoritmo explícito se rechaza token manipulado con alg none, se documenta vulnerabilidad y mitigación aplicada.
