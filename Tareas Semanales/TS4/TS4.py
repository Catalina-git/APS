# %% Librerias + variables


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from numpy.fft import fft, fftshift
from scipy.signal import windows

# Declaracion de varibles

N = 1000 # Cantidad de muestras
fs = N # Frecuencia de muestreo
df = fs/N # Resolucion temporal
a0 = 2 # Amplitud
realizaciones = 200 # Sirve para parametrizar la cantidad de realizaciones de sampling ->muestras que vamos a tomar de la frecuencia
omega_0 = np.pi / 2 # fs/4 -> mitad de banda digital
fr = np.random.uniform(-2,2) # Variable aleatoria de distribucion normal para la frecuencia
omega_1 = omega_0 + fr * 2 * np.pi / N
nn = np.arange(N) # Vector dimensional de muestras
ff = np.arange(N) # Vector en frecuencia al escalar las muestras por la resolucion espectral

# Signal to noise ratio en dB segun pide la consigna
SNR3 = 3
SNR10 = 10


# %% FUNCION SENOIDAL
def mi_funcion_sen(frecuencia, nn, amplitud = 1, offset = 0, fase = 0, fs = 2):   

    N = np.arange(nn)
    
    t = N / fs

    x = amplitud * np.sin(2 * np.pi * frecuencia * t + fase) + offset

    return t, x

t1,s1 = mi_funcion_sen(frecuencia = omega_1, nn = N, fs = fs, amplitud = a0) # Funcion senoidal con frecuencia aleatoria

# %% GENERACION DE VENTANAS
ventana_rectangular = np.ones(N)
ventana_flattop = windows.flattop(N)
ventana_blackmanharris = windows.blackmanharris(N)
ventana_hann = signal.windows.hann(N)  # Ventana extra

# --------------- FFT normalizada ---------------
ventana_RECTANGULAR = fft(ventana_rectangular, 2**14) / (len(ventana_rectangular)/2.0)
ventana_FLATTOP = fft(ventana_flattop, 2**14) / (len(ventana_flattop)/2.0)
ventana_BLACKMANHARRIS = fft(ventana_blackmanharris, 2**14) / (len(ventana_blackmanharris)/2.0)
ventana_HANN = fft(ventana_hann, 2**14) / (len(ventana_hann)/2.0)

# Magnitud en dB
respuesta_rectangular = 20 * np.log10(np.abs(fftshift(ventana_RECTANGULAR / abs(ventana_RECTANGULAR).max())))
respuesta_flattop = 20 * np.log10(np.abs(fftshift(ventana_FLATTOP / abs(ventana_FLATTOP).max())))
respuesta_blackmanharris = 20 * np.log10(np.abs(fftshift(ventana_BLACKMANHARRIS / abs(ventana_BLACKMANHARRIS).max())))
respuesta_hann = 20 * np.log10(np.abs(fftshift(ventana_HANN / abs(ventana_HANN).max())))

freq = np.linspace(-np.pi, np.pi, 2**14)
plt.figure()

plt.plot(freq, respuesta_rectangular,color="red", label = 'Rectangular')
plt.plot(freq, respuesta_flattop, color="lime", label = 'Flattop')
plt.plot(freq, respuesta_blackmanharris, color="yellow", label = 'Blackmanharris')
plt.plot(freq, respuesta_hann,  color='dodgerblue', label = 'Hann')
plt.xlim(-np.pi, np.pi)
plt.ylim(-80, 10)
# ticks = [-N_fft//2, -N_fft//4, 0, N_fft//4, N_fft//2]
# labels = [r'$-\frac{N_{FFT}}{2}$', r'$-\frac{N_{FFT}}{4}$', '0', r'$\frac{N_{FFT}}{4}$', r'$\frac{N_{FFT}}{2}$']
# plt.xticks(ticks, labels)
plt.title("Ventanas en funcion de Δω")
plt.ylabel("$|W_N(\omega)|$ [dB]")
plt.xlabel("Frecuencia en múltiplos de Δω")
plt.legend()
plt.tight_layout()
plt.show()

# %% RUIDO

pot_ruido3 = a0**2 / (2*10**(SNR3/10)) # Aca es la amplitud elevada al cuadrado y 10 elevado a la SNR3/10
print(f"Potencia del SNR 3dB -> {pot_ruido3:.3f}")
ruido3 = np.random.normal(0, np.sqrt(pot_ruido3), N) # Vector
var_ruido3 = np.var(ruido3)
print(f"Potencia de ruido 3dB -> {var_ruido3:.3f}")

pot_ruido10 = a0**2 / (2*10**(SNR10/10))
print(f"Potencia del SNR 10dB-> {pot_ruido10:.3f}")
ruido10 = np.random.normal(0, np.sqrt(pot_ruido10), N) # Vector
var_ruido10 = np.var(ruido10)
print(f"Potencia de ruido 10dB -> {var_ruido10:.3f}")


# Modelo de señal --> señal limpia + ruido
x1 = s1 + ruido3  
x2 = s1 + ruido10  

plt.figure()
plt.plot(x1,'x',label = 'Señal + 3dB ruido')
plt.plot(x2,'o',label = 'Senal + 10dB ruido')
plt.legend()
plt.show()

# %%FFT

X1 = (1/N)*fft(x1) # Multiplico por 1/N para calibrarlo --> llevar el piso de ruido a cero

X2 = (1/N)*fft(x2)# Multiplico por 1/N para calibrarlo --> llevar el piso de ruido a cero


# GRAFICO
plt.figure(figsize=(20,20))

# Grafico X1 en db

plt.title("Densidades espectrales de potencia (PDS) en db")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.xlim([0, fs/2])
plt.plot(ff, np.log10(2*np.abs(X1)**2 * 10), label = 'X1')  # Densidad espectral de potencia
plt.plot(ff, np.log10(2*np.abs(X2)**2* 10), label = 'X2')
plt.legend()
plt.show()

# El ruido es poco entonces se "tapa", no me juega en la suma
# Estar 250dB por debajo, es estar 25 ordenes de potencia por debajo
# Todo el piso de ruido es tapado por la energia, al ser esta tan tan grande (casi infinitamente mas grande), lo tapa al ruido.

# %% Señales ventaneadas

x_vent_fla= ruido3 * (windows.flattop(N).reshape(-1,1))
x_vent_BM= ruido3 * (windows.blackman(N).reshape(-1,1))
x_vent_R= ruido3 * (windows.boxcar(N).reshape(-1,1))
x_vent_H= ruido3 * (windows.hamming(N).reshape(-1,1))

# Calculo la FFT normalizada a lo largo del eje del tiempo (filas)
X_mat_ft = (1/N) * fft(x_vent_fla, axis=0)
X_mat_BM = (1/N) * fft(x_vent_BM, axis=0)
X_mat_R = (1/N) * fft(x_vent_R, axis=0)
X_mat_H = (1/N) * fft(x_vent_H, axis=0)

# Graficos de la transformada de senales ventanadas con ruido
plt.figure()

plt.subplot(2,2,1)
plt.title('BLACKMAN')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.plot(ff, np.log10(2*np.abs(X_mat_BM)**2) * 10)  # Densidad espectral de potencia
plt.xlim([0, fs/2])

plt.subplot(2,2,2)
plt.title('RECTANGULAR')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.plot(ff, np.log10(2*np.abs(X_mat_R)**2) * 10)  # Densidad espectral de potencia
plt.xlim([0, fs/2])

plt.subplot(2,2,3)
plt.title('HAMMING')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.plot(ff, np.log10(2*np.abs(X_mat_H)**2) * 10)  # Densidad espectral de potencia
plt.xlim([0, fs/2])

plt.subplot(2,2,4)
plt.title('FLATOP')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.plot(ff, np.log10(2*np.abs(X_mat_ft)**2) * 10)  # Densidad espectral de potencia
plt.xlim([0, fs/2])

plt.tight_layout()
plt.show()