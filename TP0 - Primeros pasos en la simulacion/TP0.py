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
N = 1000 
amplitud = 2
offset = 1
frecuencia = N
fase = np.pi/4
frecADC = 1000

# Llamo a mi funcion
tt, xx = mi_funcion_sen(amplitud, offset, frecuencia, fase, N, frecADC)

# Grafico la señal
plt.title("Señal Senoidal Generada")
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tt, xx, linestyle = '-', color = 'r' ) # Genero el grafico de la señal con linea 'continua' de color 'rojo'

# EJERCICIO BONUS (SIGUIENDO EL TEOREMA DE NYQUIST-SHANNON)

# Genero otra ventana para los graficos
plt.figure(figsize=(10, 6))  # Tamaño de la figura (ancho, alto)

# Señal 500 Hz, es Nyquist
plt.subplot(2, 2, 1)
tt, xx = mi_funcion_sen(2, 0, 500, np.pi/4, 1000, 1000)
plt.plot(tt, xx, '-', color='blue')
plt.title("Señal Senoidal con 500 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.grid(True)

# Señal 999 Hz
plt.subplot(2, 2, 2)
tt, xx = mi_funcion_sen(2, 0, 999, np.pi/4, 1000, 1000)
plt.plot(tt, xx, '-', color='green')
plt.title("Señal Senoidal con 999 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.grid(True)

# Señal 1001 Hz
plt.subplot(2, 2, 3)
tt, xx = mi_funcion_sen(2, 0, 1001, np.pi/4, 1000, 1000)
plt.plot(tt, xx, '-', color='orange')
plt.title("Señal Senoidal con 1001 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.grid(True)

# Señal 2001 Hz
plt.subplot(2, 2, 4)
tt, xx = mi_funcion_sen(2, 0, 2001, np.pi/4, 1000, 1000)
plt.plot(tt, xx, '-', color='grey')
plt.title("Señal Senoidal con 2001 Hz")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.grid(True)

plt.tight_layout()  
plt.show()

# Grafico una señal cuadrada

from scipy.signal import sweep_poly

# Parámetros de la señal
amplitud = 1 # Volts
offset = 0 
frecuencia = 50 # Hz
fase = 0 # radianes
tiempo_total = 0.05 # segundos
frecADC = 5000 # Frecuencia de muestreo (Hz)
t = np.arange(0, tiempo_total, 1/frecADC)

# Definimos el polinomio que describe la frecuencia instantánea
# En este caso, una aproximación simple con una frecuencia constante
polinomio = np.poly1d([frecuencia])

# Generamos la señal utilizando sweep_poly
senal_senoidal = sweep_poly(t, polinomio)

# Aproximamos la señal cuadrada utilizando una combinación de senos
senal_cuadrada = np.sign(senal_senoidal)

# Graficamos la señal cuadrada generada
plt.figure(figsize=(10, 4))
plt.plot(t, senal_cuadrada, label='Señal Cuadrada Aproximada')
plt.title('Generación de Señal Cuadrada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()



