"""
1) Sintetizar y graficar: --> uso funciones de numpy
    - Una señal sinusoidal de 2KHz
    - Misma señal amplificada y desfazada en pi/2
    - Señal anterior modulada en amplitud por otra señal sinusoidal de la mitad de frecuencia. --> modular es multiplicar por otra señal, en este caso va a ser de 1kHz --> sen(2*t) * sen(t) --> reemplazo A (amplitud) por la funcion que modula
    - Señal anterior recortada al 75% de su amplitud --> potencia = A**2 / 2 --> despues se hace con una funcion de numpy --> la salida es recta arriba y abajo --> recorto todo lo que supere el 75% de la potencia
    --> las funciones con las que trabajamos no son periodicas (vemos N-muestras) --> vamos a calcular energias --> tomamos potencia como energia
    --> tengo que recortar la amplitud al valor del 75% de la potencia de la señal
    --> una manera es ir recorriendo el vector, y cuando llego a un valor que es mayor que el 75% de la potencia, lo cambio por el valor corte = treasure = 75% de la potencia
    --> otra manera, busco la funcion de numpy --> np.clic
    - Una señal cuadrada de 4KHz
    - Un pulso rectangular de 10ms
    - En cada caso indique tiempo entre muestras, numero de mustras y potencia
    
2) Verificar ortogonalidad entre la primera señal y las demas --> multiplicar matricialmente, filas por columnas, y tiene que dar cero
--> hago el producto interno entre vectores, si es cero son ortogonales --> hay funciones en numpy para calcularlo --> inner_product

3) Graficar la autocorrelacion de la primera señal y la correlacion entre esta y las demas. 
    Autocorrelacion --> similitud lineal, similitud consigomismo
    scipy tiene una funcion que te hace la correlacion
    
4) Dada la siguiente propiedad geometrica
    2 * sin(alfa) * sin (beta) = cos(alfa - beta) - cos(alfa + beta)
    - Demostrar la igualdad
    - Mostrar que la igualdad se cumple con señales sinosoidales, considerando alfa = w * t, el doble de beta (use la frecuencia que desee).

BONUS
5) Graficar la temperatura del procesador de tu computadora en tiempo real
    - Suponiendo distancia entre muestras constante
    - Considerando el tiempo de la muestra tomada
    
6) Bajar un wav de freesoung.org, graficarlo y calcular la energia

"""

# Primero importo la libreria numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Defino mis funciones
# Funcion de una señal sinusoidal
def mi_funcion_sen(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, frecADC = 1000):
    """
    - amplitud: es la amplitud maxima. [amplitud] = [V]
    - offset: es mi amplitud media. [offset] = [V]
    - frecuencia: es la frecuencia de la señal. [frecuencia] = [Hz]
    - fase: es la fase inicial. [fase] = [rad]
    - N: es la cantidad de muestras a generar
    - frecADC: es la frecuencia de muestreo del ADC. [frecADC] = [Hz]
    """
    Ts = 1/frecADC # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    return tt, xx

# Funcion de una señal sinusoidal modulada en amplitud por otra señal sinusoidal de la mitad de frecuencia
def mi_funcion_sen_modulada(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, frecADC = 1000):
    """
    - amplitud: es la amplitud maxima. [amplitud] = [V]
    - offset: es mi amplitud media. [offset] = [V]
    - frecuencia: es la frecuencia de la señal. [frecuencia] = [Hz]
    - fase: es la fase inicial. [fase] = [rad]
    - N: es la cantidad de muestras a generar
    - frecADC: es la frecuencia de muestreo del ADC. [frecADC] = [Hz]
    """
    Ts = 1/frecADC # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) * np.sin(2 * np.pi * frecuencia/2 * tt + fase) + offset

    return tt, xx

# Funcion para redcortar una funcion al 75% de su amplitud
def mi_funcion_sen_recortada(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, frecADC = 1000):
    
    Ts = 1/frecADC # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    valor_corte = amplitud * 0.75 # es el 75% de la amplitud
    
    xx = np.clip(xx, - valor_corte, valor_corte) # Funcion de numpy que me recorta la señal
    
    return tt, xx

# Funcion para una señal cuadrada
def mi_funcion_cuadrada (frecuencia, frecADC, N, offset, fase):
    Ts = 1/frecADC # Es el tiempo en el cual se toma cada muestra

    ttc = np.arange(start = 0, stop= N*Ts, step = Ts)

    xxc = signal.square(2 * np.pi * frecuencia * ttc + fase) + offset

    return ttc, xxc

# ------------------------------- EJERCICIO 1 -------------------------------
# ------------------------------- Señal sinusoidal de 2kHz -------------------------------
# Llamo a mi funcion
tt, xx = mi_funcion_sen(1, 0, 2000, 0, 100, 40000) # Pongo frecADC > 2 * frecuencia --> Teorema de Nyquist-Shannon

# Genero otra ventana para los graficos
plt.figure(figsize=(10, 6))  # Tamaño de la figura (ancho, alto)
plt.subplot(2,2,1)

plt.title("Señal Sinusoidal")

# Grafico la señal senoidal de 2KHz
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tt, xx, linestyle = '-', label='Señal Sinusoidal de 2kHz') # Genero el grafico de la señal con linea 'continua' de color 'rojo'
plt.plot(tt, xx, 'o--')
plt.lenegd()

# ------------------------------- Señal sinusoidal de 2kHz, amplificada y desfazada en pi/2 -------------------------------
tt, xx = mi_funcion_sen(2, 0, 2000, np.pi/2, 100, 40000) 

# Grafico la señal senoidal de 2KHz, pero amplificada y desfazada en pi/2
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tt, xx, label='Señal Sinusoidal de 2kHz, amplificada y desfazada en pi/2') # Genero el grafico de la señal
plt.plot(tt, xx, 'o--')
plt.lenegd()

# ------------------------------- Señal sinusoidal modulada por otra señal sinusoidal de 1kHz -------------------------------
tt, xx = mi_funcion_sen_modulada(1, 0, 1000, np.pi/2, 100, 40000)

# Grafico la señal senoidal de 2KHz, pero modulada por otra señal de la mitad de la frecuencia
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tt, xx, linestyle = '-', label='Señal Sinusoidal modulada') # Genero el grafico de la señal
plt.plot(tt, xx, 'o--')
plt.lenegd()

# ------------------------------- Misma señal pero recortada al 75% de su potencia -------------------------------
tt, xx = mi_funcion_sen_recortada(1, 0, 2000, 0, 100, 40000)

# Grafico la señal recortada
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tt, xx, linestyle = '-', label='Señal Sinusoidal de 2kHz recortada al 75% de amplitud') # Genero el grafico de la señal con linea 'continua' de color 'rojo'
plt.plot(tt, xx, 'o--')
plt.lenegd()

# ------------------------------- Señal cuadrada de 4kHz -------------------------------

# Llamo a mi funcion
ttc, xxc = mi_funcion_cuadrada(4000, 80000, 100, 0, 0)

# Grafico la señal cuadrada
plt.subplot(2,2,2)
plt.title('Señal cuadrada de 4kHz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ttc, xxc, linestyle = '-', label='Señal Cuadrada de 4kHz') # Genero el grafico de la señal con linea 'continua' de color 'rojo'
plt.plot(ttc, xxc, 'o--')
plt.lenegd()

# ------------------------------- Pulso rectangular de 10ms -------------------------------
M = 8
x = np.zeros(M)

x[3:5] = 1 # Los elementos 4, 5 y 6 valen 1

print(x)

# Grafico
plt.subplot(2,2,3)
plt.plot(x)
# otra manera de graficar el pulso: plt.stem(x)


# ------------------------------- EJERCICIO 3 -------------------------------
# ------------------------------- Autocorrelacion -------------------------------
"""
Rxx = signal.correlate(x,x)

# Grafico
plt.subplot(2,2,4)
plt.stem(Rxx)

print(x)
 
Rxx = np.zeros(M)

for tau in range(M - 1):
    for i in range(M): # Tambien puedo poner in len(x)
        Rxx(i) = x[i] * x[i + tau]

"""
        
