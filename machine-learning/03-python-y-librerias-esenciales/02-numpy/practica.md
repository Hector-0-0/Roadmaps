# Práctica - NumPy

## Nivel básico

1. **Crear arrays**
   Enunciado: Crea arrays con np.array, np.zeros, np.ones, np.arange, np.linspace.
   Pista: Verifica shape y dtype.
   Criterio verificable: 5 arrays creados con formas correctas.

2. **Indexado y slicing**
   Enunciado: Extrae submatriz 2x2 de matriz 4x4 usando slicing.
   Pista: Usa arr[0:2, 0:2].
   Criterio verificable: Submatriz extraída correctamente.

3. **Operaciones vectorizadas**
   Enunciado: Suma, multiplica elemento a elemento y calcula potencia sin bucles.
   Pista: Usa operadores +, *, **.
   Criterio verificable: Todas las operaciones vectorizadas correctas.

## Nivel intermedio

4. **Broadcasting**
   Enunciado: Suma vector fila a cada fila de matriz usando broadcasting.
   Pista: Verifica shapes compatibles.
   Criterio verificable: Resultado correcto con broadcasting.

5. **Estadísticas con NumPy**
   Enunciado: Calcula media, mediana, std, min, max por columna con Iris.
   Pista: Usa axis=0.
   Criterio verificable: Estadísticos calculados correctamente por columna.

6. **Álgebra lineal**
   Enunciado: Multiplica matrices, inversa, determinante, autovalores.
   Pista: Usa np.linalg.
   Criterio verificable: Todas las operaciones correctas con verificación.

## Nivel desafío

7. **Normalización**
   Enunciado: Normaliza datos con z-score usando NumPy vectorizado.
   Pista: (x - mean)/std con axis correcto.
   Criterio verificable: Media ~0 y std ~1 tras normalización.

8. **Producto externo**
   Enunciado: Calcula producto externo entre dos vectores con np.outer.
   Pista: Compara con reshape y multiplicación.
   Criterio verificable: Matriz resultado correcta.
