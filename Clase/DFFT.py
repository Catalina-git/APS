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
t,x = mi_funcion_sen(1, 0, N/4, 0, N, N)

xdfft = np.fft(x, n=None, axis=-1, norm=None, out=None)

plt.figure()  # Tamaño de la figura (ancho, alto)

plt.title("DFFT")

# Grafico la señal senoidal de 2KHz
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(xdfft, 'o--')
plt.show()


