"""
1) Sintetizar y graficar:
    - Una señal sinusoidal de 2KHz
    - Misma señal amplificada y desfazada en pi/2
    - Señal anterior modulada en amplitud por otra señal sinusoidal de la mitad de frecuencia
    - Señal anterior recortada al 75% de su potencia
    - Una señal cuadrada de 4KHz
    - Un pulso rectangular de 10ms
    - En cada caso indique tiempo entre muestras, numero de mustras y potencia
    
2) Verificar ortogonalidad entre la primera señal y las demas

3) Graficar la autocorrelacion de la primera señal y la correlacion entre esta y las demas
    
4) Dada la siguiente propiedad geometricaÑ
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

# Defino mi funcion
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

# Llamo a mi funcion
tt, xx = mi_funcion_sen(1, 0, 2, 0, 1000, 1000)

# Genero otra ventana para los graficos
plt.figure(figsize=(10, 6))  # Tamaño de la figura (ancho, alto)

# Grafico la señal senoidal de 2KHz
plt.subplot(2, 2, 1)
plt.title("Señal Senoidal de 2KHz")
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tt, xx, linestyle = '-', color = 'r' ) # Genero el grafico de la señal con linea 'continua' de color 'rojo'

tt, xx = mi_funcion_sen(5, 0, 2, np.pi/2, 1000, 1000)

# Grafico la señal senoidal de 2KHz, pero amplificada y desfazada en pi/2
plt.subplot(2, 2, 2)
plt.title("Señal Senoidal de 2KHz, amplificada y desfazada en pi/2")
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tt, xx, linestyle = '-' ) # Genero el grafico de la señal


