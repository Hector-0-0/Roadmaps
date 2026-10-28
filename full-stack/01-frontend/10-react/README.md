# 10-react

## 1. Qué es y para qué sirve
React es una biblioteca (library) de JavaScript para construir interfaces de usuario (User Interfaces). Permite crear componentes reutilizables que gestionan su propio estado y se actualizan eficientemente cuando los datos cambian.

## 2. Por qué importa dentro del roadmap y cómo se conecta
React es uno de los enfoques más usados para frontend moderno. Se conecta con HTML, CSS, JavaScript y se vuelve relevante tras dominar las bases. El roadmap original sugiere revisarlo después de Backend; aquí se deja preparado para ese momento.

## 3. Conceptos clave
- **Componente (component)**: pieza reutilizable de UI (funcional o de clase; se enfoca en funcionales).
- **JSX (JavaScript XML)**: sintaxis que permite escribir HTML dentro de JavaScript.
- **Props (properties, propiedades)**: datos que se pasan de padre a hijo.
- **State (estado)**: datos internos que cambian con el tiempo.
- **useState (hook de estado)**: hook para agregar estado a componentes funcionales.
- **useEffect (hook de efecto)**: hook para efectos secundarios (fetch, suscripciones).
- **Listas y keys (claves)**: renderizar arrays con clave única estable.
- **Eventos**: manejo de eventos en JSX.
- **Composición (composition)**: combinar componentes en lugar de herencia.
- **Vite (herramienta de build)**: herramienta rápida para crear proyectos React.

## 4. Ejemplos de código comentados, correctos y ejecutables

### Ejemplo 1: Componente funcional con props
```jsx
// Saludo.jsx
function Saludo({ nombre }) {
  // Recibe props y muestra nombre
  return <h1>Hola, {nombre}</h1>;
}

export default Saludo;
```

```jsx
// App.jsx
import Saludo from './Saludo';

function App() {
  return (
    <div>
      <Saludo nombre="Ana" />
      <Saludo nombre="Luis" />
    </div>
  );
}

export default App;
```

### Ejemplo 2: useState, eventos y useEffect
```jsx
import { useState, useEffect } from 'react';

function Contador() {
  const [contador, setContador] = useState(0);

  // Efecto que se ejecuta al montar
  useEffect(() => {
    console.log('Componente montado');
  }, []);

  function incrementar() {
    setContador(contador + 1);
  }

  return (
    <div>
      <p>Contador: {contador}</p>
      <button onClick={incrementar}>Incrementar</button>
    </div>
  );
}

export default Contador;
```

## 5. Errores comunes y buenas prácticas

Errores comunes:
- Mutar estado directamente (usar setter).
- Olvidar key en listas.
- Usar índices como key cuando lista cambia.
- Efectos sin dependencias correctas.
- Componentes muy grandes sin dividir.

Buenas prácticas:
- Componentes funcionales y hooks.
- Props inmutables.
- Keys estables y únicas.
- Extraer lógica en componentes pequeños.
- Usar Vite para proyectos nuevos.
- Nombrar componentes en PascalCase.

## 6. Autoevaluación

1. ¿Qué es un componente en React?
2. ¿Qué es JSX?
3. ¿Diferencia entre props y state?
4. ¿Para qué sirven useState y useEffect?
5. ¿Por qué son importantes las keys al renderizar listas?

Respuestas esperadas (orientativas):
1. Pieza reutilizable de UI que encapsula lógica y presentación.
2. Sintaxis que permite mezclar HTML con JavaScript.
3. Props son datos pasados desde padre, state es datos internos mutables.
4. useState gestiona estado, useEffect maneja efectos secundarios.
5. Ayudan a React a identificar elementos y actualizar eficientemente.
