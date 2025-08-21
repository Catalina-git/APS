# Primero importo la libreria numpy
import numpy as np
import matplotlib.pyplot as plt

# Funcion de una señal sinusoidal
def mi_funcion_sen(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, fs = 1000):
    """
    - amplitud: es la amplitud maxima. [amplitud] = [V]
    - offset: es mi amplitud media. [offset] = [V]
    - frecuencia: es la frecuencia de la señal. [frecuencia] = [Hz]
    - fase: es la fase inicial. [fase] = [rad]
    - N: es la cantidad de muestras a generar
    - fs: es la frecuencia de muestreo del ADC. [frecADC] = [Hz]
    """
    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    return tt, xx

N = 1000
fs = 1000 

tt, xx = mi_funcion_sen(1, 0, 1, 0, N, fs)
X = np.zeros(N, dtype = np.complex128)

for k in range(N):
    for n in range(N):
        X += [xx[n] * np.exp(-1j * k * 2 * (np.pi / N) * n)]

print(X)

#Grafico la senoidal de 1Hz
plt.subplot(1,2,1)
plt.title("Funcion senoidal de 1Hz")
plt.xlabel('Tiempo [s]')
plt.ylabel('sen()')
plt.plot(tt, xx, linestyle = '-') # Genero el grafico de la señal con linea 'continua' de color 'rojo'
plt.plot(tt, xx, 'o--')

X_modulo = np.abs(X)
frecuencia = np.arange(N) * fs/N
# Grafico el modulo de la DFT del seno de 1Hz de frecuencia
plt.subplot(1,2,2)
plt.title("DFT")
plt.xlabel('Tiempo [s]')
plt.ylabel('Funcion transformada')
plt.plot(frecuencia, X_modulo, linestyle = '-') # Genero el grafico de la señal con linea 'continua' de color 'rojo'
plt.plot(frecuencia, X_modulo, 'o--')
plt.xlim(-fs/2, fs/2)
