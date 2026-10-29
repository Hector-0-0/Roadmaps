# Práctica - Python para Machine Learning

## Nivel básico

1. **Tipos y estructuras**
   Enunciado: Crea lista, tupla, diccionario y set con datos relacionados a ML y muestra sus diferencias.
   Pista: Prueba métodos como append (lista) vs intentar modificar tupla.
   Criterio verificable: Se muestran las 4 estructuras con ejemplos y diferencias correctas.

2. **List comprehensions**
   Enunciado: Filtra números pares y eleva al cuadrado usando list comprehension.
   Pista: Sintaxis [expr for x in lista if condicion].
   Criterio verificable: Resultado correcto con list comprehension.

3. **Funciones**
   Enunciado: Crea función que calcule media, mínimo y máximo de una lista retornando diccionario.
   Pista: Usa sum(), len(), min(), max().
   Criterio verificable: Función retorna diccionario con las 3 claves correctas.

## Nivel intermedio

4. **Manejo de errores**
   Enunciado: Lee archivo con try/except manejando FileNotFoundError y muestra mensaje apropiado.
   Pista: Usa open() en bloque try.
   Criterio verificable: Manejo correcto del error con mensaje claro.

5. **POO para Dataset**
   Enunciado: Crea clase Dataset con métodos cargar, info y shape usando datos dummy.
   Pista: Usa __init__ para atributos.
   Criterio verificable: Clase funcional con los 3 métodos operativos.

6. **Trabajar con zip y enumerate**
   Enunciado: Combina dos listas con zip y enuméralos con enumerate imprimiendo pares.
   Pista: for i,(a,b) in enumerate(zip(lista1,lista2)).
   Criterio verificable: Salida correcta con índices y pares.

## Nivel desafío

7. **Pipeline simple**
   Enunciado: Implementa clase Pipeline con métodos add_step y run para encadenar funciones.
   Pista: Almacena funciones en lista y aplícalas secuencialmente.
   Criterio verificable: Pipeline ejecuta pasos en orden y retorna resultado correcto.

8. **Análisis con Python puro**
   Enunciado: Procesa lista de valores calculando estadísticos básicos sin usar numpy/pandas.
   Pista: Implementa media, varianza, desviación.
   Criterio verificable: Cálculos correctos comparados con valores esperados.
