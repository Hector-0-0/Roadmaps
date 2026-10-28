# Práctica - 07-autenticacion-jwt

## Nivel básico
1. **Registro** (criterio: terminado)
   Enunciado: Endpoint de registro con hash de contraseña.
   Pista: bcrypt.

2. **Login** (criterio: terminado)
   Enunciado: Login que valide y genere JWT.
   Pista: jsonwebtoken.

## Nivel intermedio
3. **Middleware auth** (criterio: terminado)
   Enunciado: Middleware para proteger rutas.
   Pista: Verificar token en header.

4. **Ruta protegida** (criterio: terminado)
   Enunciado: Acceder solo con token válido.
   Pista: Retornar 401 si no válido.

## Nivel desafío
5. **Roles básicos** (criterio: terminado)
   Enunciado: Proteger ruta por rol (admin/user).
   Pista: Agregar rol en payload y verificar.
