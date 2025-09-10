import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
from scipy.signal import windows

# %% SEÑAL Y RUIDO (SNR)
# Defino mis variables 
noise_std = 0.5 # Es el desvio estandar del ruido
# 1. Crear una señal de ejemplo
t1 = np.linspace(0, 1, 1000)
senoidal = np.sin(2 * np.pi * 10 * t1)  # Señal senoidal de 10 Hz, y amplitud = 1

# Ruido Blanco Gaussiano
ruido = np.random.normal(0, noise_std, size=t1.shape)

# Señal con ruido
senoidal_ruido = senoidal + ruido

# Grafico
plt.figure()
plt.plot(t1, senoidal, color='black', label = 'Senoidal pura')
plt.plot(t1, senoidal_ruido, color='orange', label = 'Senoidal con ruido')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.title('Señal senoidal con ruido blanco')
plt.legend()
plt.tight_layout()
plt.show()


""" 

Otra manera de hacerlo...
# Defino la función para agregar ruido con SNR
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

# %% PRACTICA VENTANAS
# Defino las variables utilizadas
# Todos estos parametros sirven si no defino mi funcion, uso np.sin(2 * np.pi * fx * tiempo) directamente
N = 31 # Si pongo 31 queda igual al del holton, si pongo otro N se ve mas colapsado
# N es el tamaño de la ventana
# fs = 500 # Si mi fs != N, estoy cambiando mi relacion de 1/deltaf = N.Ts = 1 y cambio el tiempo.
fs = N   # Esto quiere decir que yo voy a tomar 1000 muestras por segundo. 

N_fft = 2048 # FFT larga para buena resolución espectral
# N_fft es la cantidad de puntos que uso para calcular la Transformada Rapida de Fpurier (FFT). 
# No tiene que coincidir con el tamaño de la señal o ventana original. 
# Se puede extender (zero padding) para obbtener mas puntos del espectro.
# Porque N_fft = 2048? Si uso pocos puntos, el espectro de ve "cuadrado", con pocos bins.
#                      Si uso muchos puntos el espectro se ve suave y detallado.
delta_omega = 2 * np.pi / N_fft
omega = np.linspace(-np.pi, np.pi, N_fft)
omega_delta = omega / delta_omega # Eje x en multiplos de Δω 
Ts = 1 / fs
# fx = 1000


# Ventanas
ventana_BH = windows.blackmanharris(N)

ventana_Hamming = windows.hamming(N)

ventana_Hann = windows.hann(N)

ventana_Rectangular = np.ones(N)

ventana_FT = windows.flattop(N)

# --------------- FFT normalizada ---------------
A = fft(ventana_BH, N_fft) / (len(ventana_BH)/2.0)
B = fft(ventana_Hamming, N_fft) / (len(ventana_Hamming)/2.0)
C = fft(ventana_Hann, N_fft) / (len(ventana_Hann)/2.0)
D = fft(ventana_Rectangular, N_fft) / (len(ventana_Rectangular)/2.0)
E = fft(ventana_FT, N_fft) / (len(ventana_FT)/2.0)

# Magnitud en dB
respuesta_BH = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
respuesta_Hamming = 20 * np.log10(np.abs(fftshift(B / abs(B).max())))
respuesta_Hann = 20 * np.log10(np.abs(fftshift(C / abs(C).max())))
respuesta_Rectangular = 20 * np.log10(np.abs(fftshift(D / abs(D).max())))
respuesta_FT = 20 * np.log10(np.abs(fftshift(E / abs(E).max())))

plt.figure()

plt.plot(omega_delta, respuesta_BH,color="red", label = 'Blackman Harris')
plt.plot(omega_delta, respuesta_Hamming, color="lime", label = 'Hamming')
plt.plot(omega_delta, respuesta_Hann, color="yellow", label = 'Hann')
plt.plot(omega_delta, respuesta_Rectangular,  color='dodgerblue', label = 'Rectangular')
plt.plot(omega_delta, respuesta_FT, color="brown",  label = 'Flattop')
plt.xlim(omega_delta[0], omega_delta[-1])
plt.ylim(-80, 0)
ticks = [-N_fft//2, -N_fft//4, 0, N_fft//4, N_fft//2]
labels = [r'$-\frac{N_{FFT}}{2}$', r'$-\frac{N_{FFT}}{4}$', '0', r'$\frac{N_{FFT}}{4}$', r'$\frac{N_{FFT}}{2}$']
plt.xticks(ticks, labels)
plt.title("Ventanas en funcion de Δω")
plt.ylabel("$|W_N(\omega)|$ [dB]")
plt.xlabel("Frecuencia en múltiplos de Δω")
plt.legend()
plt.tight_layout()
plt.show()

