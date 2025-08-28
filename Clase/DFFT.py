# DFFT --> Transformada rapida de Fourier

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft

def mi_funcion_sen(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, fs = 1000):
    """
    - amplitud: es la amplitud maxima. [amplitud] = [V]
    - offset: es mi amplitud media. [offset] = [V]
    - frecuencia: es la frecuencia de la señal. [frecuencia] = [Hz]
    - fase: es la fase inicial. [fase] = [rad]
    - N: es la cantidad de muestras a generar
    - fs: es la frecuencia de muestreo del ADC. [fs] = [Hz]
    """
    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    return tt, xx

# Resolucion espectral unitaria --> N = fs
N = 1000
t1,x1 = mi_funcion_sen(1, 0, N/4, 0, N, N)

xdfft1 = fft(x1)

modulo_xdfft1 = np.abs(xdfft1)

plt.figure()  # Tamaño de la figura (ancho, alto)
plt.subplot(1,3,1)

plt.title("Modulo de la DFFT con frecuencia = N/4")

# Grafico la señal senoidal de 2KHz
plt.xlabel('Tiempo [s]')
plt.ylabel('|x|')
plt.plot(modulo_xdfft1, 'o--')
plt.show()



t2,x2 = mi_funcion_sen(1, 0, (N/4) + 0.5, 0, N, N)

xdfft2 = fft(x2)

modulo_xdfft2 = np.abs(xdfft2)

plt.subplot(1,3,2)

plt.title("Modulo de la DFFT con frecuencia = (N/4) + 0.5")

# Grafico la señal senoidal de 2KHz
plt.xlabel('Tiempo [s]')
plt.ylabel('|x|')
plt.plot(modulo_xdfft2, 'o--')
plt.show()



t3,x3 = mi_funcion_sen(1, 0, (N/4) + 1, 0, N, N)

xdfft3 = fft(x3)

modulo_xdfft3 = np.abs(xdfft3)

plt.subplot(1,3,3)

plt.title("Modulo de la DFFT con frecuencia = (N/4) + 1")

# Grafico la señal senoidal de 2KHz
plt.xlabel('Tiempo [s]')
plt.ylabel('|x|')
plt.plot(modulo_xdfft3, 'o--')
plt.show()

