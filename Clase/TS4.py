import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft
import scipy.signal as sp
# Modelo de señal, modelo asitivo
# x(k) = a0 * sen(omega1 * n) + na(n) = S de la cajita de modelo aditivo
# a0 = raiz de 2
# Cuando a una senoidal la contamino con una señal aleatoria que tiene una distribucion normal y pontencia sigma n al cuadrado
# --> x no es mas una se;al pura, es una señal a ruido
# señal a ruido es la relacion entre ...
# Para obtener sigma cuadrado lo despejo de de la formula de SNRdB = -10*log(sigma^2), el valor de SNRdB es un valor que nos dan

# %% VARIABLES
N = 1000
fs = N
df = fs/N # Resolucion temporal
a0 = np.sqrt(2)
realizaciones = 200 # Sirve para parametrizar la cantidad de realizaciones de sampling, de muestras que vamos a tomar de la frecuencia
omega_0 = np.pi / 2 # fs/4
fr = np.random.uniform(-2,2,realizaciones)
omega_1 = omega_0 + fr * 2 * np.pi / N
SNR = 10 # En dB
amplitud_0 = np.sqrt(2) # En Volts
nn = np.arange(N) # Vector dimensional de muestras
ff = np.arange(N) # Vector en frecuencia al escalar las muestras por la resolucion espectral

# %% FUNCION SENOIDAL
def mi_funcion_sen(frecuencia, nn, amplitud = 1, offset = 0, fase = 0, fs = 2): # Si lo igualo a algo es opcional, entonces si no le paso nada el programa me lo hace cero
     # Los obligatorios van al principio del parentesis y los opcionales al final    

    N = np.arange(nn)
    
    t = N / fs

    x = amplitud * np.sin(2 * np.pi * frecuencia * t + fase) + offset

    return t, x


k0 = (N / 4)
t1,s1 = mi_funcion_sen(frecuencia = k0 * df, nn = N, fs = fs, amplitud = amplitud_0) # Funcion senoidal de mitad de banda digital

# %% Calculo las potencias para ver que machean

pot_ruido = amplitud_0**2 / (2*10**(SNR/10))
print(f"Potencia del SNR -> {pot_ruido:.3f}")
ruido = np.random.normal(0, np.sqrt(pot_ruido), N) # Vector
var_ruido = np.var(ruido)
print(f"Potencia de ruido -> {var_ruido:.3f}")

x1 = s1 + ruido  # Modelo de señal --> señal limpia + ruido

# %% CALCULO LAS DFT
S1 = (1/N)*fft(s1)
# modulo_S1 = np.abs(S1)**2

RUIDO = (1/N)*fft(ruido)
# modulo_R = np.abs(R)**2

# Calculo la FFT
X1 = (1/N)*fft(x1) # Multiplico por 1/N para calibrarlo --> llevar el piso de ruido a cero
# modulo_X1 = np.abs(X1)**2

# %% GRAFICO
plt.figure()  # Tamaño de la figura (ancho, alto)
# plt.clf --> me borra los graficos cuando tengo muchos y los voy cerrando

# Grafico X1 en db
# plt.subplot(1,3,1)

plt.title("Densidades espectrales de potencia (PDS) en db")

# plt.title("Modulo de la DFFT con frecuencia = (N/4)")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.xlim([0, fs/2]) # En este caso fs = N, pero pongo fs para saber que va eso y no va siempre N
# plt.plot(ff, np.log10(np.abs(S1)**2) * 10, label = 'S1') # En este caso es un db de tension
# plt.plot(ff, np.log10(np.abs(R)**2) * 10, label = 'Ruido')
plt.plot(ff, np.log10(2*np.abs(X1)**2) * 10, label = 'X1')  # Densidad espectral de potencia
plt.legend()

plt.show()

# En ruido es poco entonces se "tapa", no me juega en la suma
# Estar 250dB por debajo, es estar 25 ordenes de potencia por debajo
# Todo el piso de ruido es tapado por la energia, al ser esta tan tan grande (casi infinitamente mas grande), lo tapa al ruido.

# %% Vamos a hacer una funcion seno para poder pasarle matrices

t = np.arange(N).reshape(-1,1) / fs # reshape para que las columnas sean tiempo
t_mat = np.tile(t, (1, realizaciones)) # (1000, 200)


# Repetir fr en filas (mismo valor de frecuencias por columna)
frecuencias = (k0 + fr) * df # en Hz
f_mat = np.tile(frecuencias, (N, 1))  # (1000, 200)


# Matriz de senoidales
s_mat = amplitud_0 * np.sin(2 * np.pi * f_mat * t_mat) # (1000, 200)

# RUIDO
pot_ruido = amplitud_0**2 / (2 * 10**(SNR / 10))
ruido_mat = np.random.normal(0, np.sqrt(pot_ruido), size = (N, realizaciones))  # (1000, 1)

x_mat = s_mat + ruido_mat

# Calculo la FFT normalizada a lo largo del eje del tiempo (filas)
X_mat = (1/N) * fft(x_mat, axis=0)

plt.figure()

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.plot(ff, np.log10(2*np.abs(X_mat)**2) * 10)  # Densidad espectral de potencia
plt.xlim([0, fs/2])

plt.show()



""" 
def add_noise_with_snr(senoidal, snr_db):
    signal_power = np.mean(senoidal**2)
    snr_linear = 10**(snr_db / 10)
    noise_power = signal_power / snr_linear
    noise = np.random.normal(0, np.sqrt(noise_power), senoidal.shape)
    return senoidal + noise

# Aplico la función a la señal
snr_deseado = 0.5  # en decibeles
noisy_signal = add_noise_with_snr(senoidal, snr_deseado)

# 4. Graficar la señal original y la señal con ruido
plt.figure(figsize=(10, 4))
plt.plot(t1, senoidal, label='Señal original')
plt.plot(t1, noisy_signal, label=f'Señal con ruido (SNR={snr_deseado} dB)', alpha=0.7)
plt.legend()
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.title('Señal con y sin ruido')
"""


