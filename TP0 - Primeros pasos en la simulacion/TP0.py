# -*- coding: utf-8 -*-

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


# Defino mis variables
amplitud = 2
offset = 1
frecuencia = 5
fase = np.pi/4
N = 1000
frecADC = 1000

# Llamo a mi funcion
tt, xx = mi_funcion_sen(amplitud, offset, frecuencia, fase, N, frecADC)

# Grafico la señal
plt.title("Señal Senoidal Generada")
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tt, xx, linestyle = '-', color = 'r' ) # Genero el grafico de la señal con linea 'continua' de color 'rojo'

