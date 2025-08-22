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

# ------------------------------------------- Transformada discreta de Fourier ---------------------------------------
for k in range(N):
    for n in range(N):
        X[k] += xx[n] * np.exp(-1j * k * 2 * (np.pi / N) * n)

print(X)

# ----------------------------------------------------- GRAFICOS -----------------------------------------------------
#Grafico la senoidal de 1Hz
plt.subplot(2,2,1)
plt.title("Funcion senoidal de 1Hz")
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
#plt.plot(tt, xx, linestyle = '-') # Genero el grafico de la señal con linea 'continua' de color 'rojo'
plt.plot(tt, xx, 'b-')
plt.grid()

frecuencia = np.linspace(-fs/2, (fs/2) - (fs/N), N) # Esto genera N puntos equiespaciados entre -fs/2 y ((fs/2) - (fs/N))
X_modulo = np.abs(np.fft.fftshift(X))

"""
La funcion "np.fft.fftshift(X)" reorganiza el array para que 
las frecuencias negativas aparezcan a la izquierda y las positivas a la derecha. 
Sin esto, el gráfico estaría desordenado, con el pico de 1 Hz en un extremo.

"""

# Grafico el modulo de la DFT del seno de 1Hz de frecuencia
plt.subplot(2,2,2)
plt.title("DFT (modulo)")
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|X[k]|')
#plt.plot(frecuencia, X_modulo, linestyle = '-') # Genero el grafico de la señal con linea 'continua' de color 'rojo'
plt.plot(frecuencia, X_modulo, 'r-')
plt.grid()

plt.tight_layout()
plt.show

N = 8
X = np.zeros(N, dtype = np.complex128)
x = 4 + 3 * np.sin(n * np.pi / 2)

for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-1j * k * 2 * (np.pi / N) * n)

print(X)

X_modulo = np.abs(np.fft.fftshift(X))

plt.subplot(2,2,1)
plt.title("DFT (modulo)")
plt.xlabel('k')
plt.ylabel('|X[k]|')
plt.plot(np.arange(N), X_modulo)
plt.grid()

plt.tight_layout()
plt.show
