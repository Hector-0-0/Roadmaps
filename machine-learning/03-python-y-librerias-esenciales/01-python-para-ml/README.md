# 1. Python para Machine Learning

## 1. ¿Qué es y para qué sirve?

Python es el lenguaje más usado en Machine Learning por su sintaxis clara, gran ecosistema y facilidad para prototipar. Conocer lo esencial de Python permite escribir código limpio, reutilizable y eficiente para análisis y modelado.

## 2. ¿Por qué importa y cómo se conecta con el resto del roadmap?

Todo el trabajo con NumPy, pandas, scikit-learn y PyTorch se hace en Python. Dominar tipos, estructuras, funciones y POO es fundamental para crear pipelines reproducibles.

## 3. Conceptos clave

- **Tipos básicos**: int, float, str, bool, None.
- **Estructuras**: list, tuple, dict, set.
- **Condicionales y bucles**: if/elif/else, for, while, list comprehensions.
- **Funciones**: def, argumentos, return, docstrings.
- **Excepciones**: try/except/else/finally.
- **Módulos**: import, from.
- **POO básico**: clases, objetos, __init__.
- **Built-ins útiles**: len, range, enumerate, zip, map.

## 4. Ejemplos de código en Python

```python
datos = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in datos if x % 2 == 0]
print(cuadrados)
```

```python
class DatasetLoader:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def cargar(self):
        return {"nombre": self.nombre, "filas": 100}

loader = DatasetLoader("iris")
print(loader.cargar())
```

## 5. Errores comunes y buenas prácticas

- **Error común**: Mutar listas inesperadamente. **Buena práctica**: Usar copy() cuando sea necesario.
- **Error común**: Ignorar excepciones. **Buena práctica**: Manejar errores específicos.
- **Error común**: Código repetitivo. **Buena práctica**: Usar funciones y list comprehensions legibles.
- **Error común**: Nombres poco claros. **Buena práctica**: Usar nombres descriptivos.

## 6. Autoevaluación con 5 preguntas específicas del tema y sus respuestas orientativas

1. **Pregunta:** ¿Diferencia entre lista y tupla?  
   **Respuesta orientativa:** Lista mutable, tupla inmutable. Usar tupla para datos fijos.

2. **Pregunta:** ¿Cuándo usar diccionario vs lista?  
   **Respuesta orientativa:** Diccionario para búsquedas por clave; lista para colecciones ordenadas por índice.

3. **Pregunta:** ¿Qué es list comprehension y cuándo usarlo?  
   **Respuesta orientativa:** Forma concisa para crear listas; usarlo cuando mejora legibilidad.

4. **Pregunta:** ¿Para qué sirve try/except?  
   **Respuesta orientativa:** Para manejar errores y evitar que el programa falle inesperadamente.

5. **Pregunta:** ¿Ventaja de usar clases para organizar código ML?  
   **Respuesta orientativa:** Encapsula datos y lógica, facilita reutilización y mantenimiento.
