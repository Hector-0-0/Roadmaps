# Práctica - Cálculo para Machine Learning

## Nivel básico

1. **Derivadas numéricas**
   Enunciado: Implementa derivada numérica hacia adelante para $f(x)=x^2+3x+1$ en $x=2$ y compara con derivada analítica $f'(x)=2x+3$.
   Pista: Usa fórmula $f'(x)\approx \frac{f(x+h)-f(x)}{h}$ con $h=1e-6$.
   Criterio verificable: Error absoluto menor a 1e-8 entre derivada numérica y analítica (valor esperado 7.0).

2. **Derivadas parciales**
   Enunciado: Para $f(x,y)=x^2+y^2+3xy$, calcula $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$ en (1,2) numéricamente.
   Pista: Usa derivada parcial numérica fijando la otra variable.
   Criterio verificable: Valores numéricos correctos (esperados: df/dx=8, df/dy=7 aproximadamente con alta precisión).

3. **Regla de la cadena**
   Enunciado: Implementa $h(x)=\sin(x^2)$ y calcula $h'(x)$ numéricamente en $x=1.0$ comparando con $\cos(x^2)*2x$.
   Pista: Usa $h'(x)\approx \frac{h(x+h)-h(x)}{h}$.
   Criterio verificable: Coincidencia con valor analítico $\cos(1)*2$ con error menor a 1e-7.

## Nivel intermedio

4. **Gradiente descendente unidimensional**
   Enunciado: Minimiza $f(x)=x^2$ con descenso por gradiente empezando en $x=5$, lr=0.1, 50 iteraciones.
   Pista: $x_{t+1}=x_t - lr*2*x_t$. Guarda historial de $f(x)$.
   Criterio verificable: $f(x)$ disminuye monótonamente y $|x|<0.01$ tras 50 iteraciones.

5. **Gradiente descendente bidimensional**
   Enunciado: Minimiza $f(x,y)=x^2+y^2$ con gradiente $[2x,2y]$ empezando en (3,4), lr=0.1, 30 iteraciones.
   Pista: Actualiza x,y simultáneamente.
   Criterio verificable: $f(x,y)<0.01$ tras 30 iteraciones con valores cercanos a (0,0).

6. **Efecto del learning rate**
   Enunciado: Prueba lr=0.01, 0.1, 0.5 para minimizar $f(x)=x^2$. Grafica convergencia conceptualmente mostrando comportamiento.
   Pista: Con lr muy grande puede divergir, con muy pequeño converge lento.
   Criterio verificable: Se observan y documentan los tres casos con valores numéricos.

## Nivel desafío

7. **Regresión lineal con gradiente descendente**
   Enunciado: Genera datos $y=2x+1+ruido$ con numpy, implementa descenso por gradiente para MSE y estima $w,b$.
   Pista: MSE = $(1/n)\sum (wx_i+b-y_i)^2$, gradientes w,b derivados correctamente.
   Criterio verificable: $w\in[1.5,2.5], b\in[0.5,1.5]$ tras convergencia.

8. **Jacobiano básico**
   Enunciado: Para $g(x,y)=[x^2+y, xy]^T$ calcula Jacobiano numéricamente en (1,2) y verifica forma correcta.
   Pista: Jacobiano es matriz 2x2 con derivadas parciales.
   Criterio verificable: Matriz Jacobiana con dimensiones 2x2 y valores numéricos correctos calculados.
