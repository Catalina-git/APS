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

# Primero hay que ponerle un SNR a x
N = 1000
fs = N
df = fs/N # Resolucion temporal
a0 = np.sqrt(2)
# omega0 = np.pi / 2
# fr = np.random.uniforme()
# omega1 = omega0 + fr * 2 * np.pi / N
# na = np.random.normal(0)

# Funcion senoidal
def mi_funcion_sen(frecuencia, nn, amplitud = 1, offset = 0, fase = 0, fs = 2): # Si lo igualo a algo es opcional, entonces si no le paso nada el programa me lo hace cero
     # Los obligatorios van al principio del parentesis y los opcionales al final    

    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= nn*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    return tt, xx

SNR = 10 # En dB
amplitud_0 = np.sqrt(2) # En Volts
nn = np.arange(N) # Vector dimensional de muestras
ff = np.arange(N) # Vector en frecuencia al escalar las muestras por la resolucion espectral

k0 = N / 4
t1,s1 = mi_funcion_sen(frecuencia = k0 * df, nn = N, fs = fs, amplitud = amplitud_0) # Funcion senoidal de mitad de banda digital

# Calculo las potencias para ver que machean
pot_ruido = amplitud_0**2 / (2*10**(SNR/10))
print(f"Potencia del SNR -> {pot_ruido:.3f}")
ruido = np.random.normal(0, np.sqrt(pot_ruido), N) # Vector
var_ruido = np.var(ruido)
print(f"Potencia de ruido -> {var_ruido:.3f}")

x1 = s1 + ruido  # Modelo de señal --> señal + ruido

S1 = fft(s1)
modulo_S1 = np.abs(S1)**2

R = fft(ruido)
modulo_R = np.abs(R)**2

# Calculo la FFT
X1 = fft(x1)
modulo_X1 = np.abs(X1)**2



plt.figure()  # Tamaño de la figura (ancho, alto)
# plt.clf --> me borra los graficos cuando tengo muchos y los voy cerrando

# Grafico X1 en db
# plt.subplot(1,3,1)

plt.title("Densidades espectrales de potencia (PDS) en db")

# plt.title("Modulo de la DFFT con frecuencia = (N/4)")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.xlim([0, fs/2]) # En este caso fs = N, pero pongo fs para saber que va eso y no va siempre N
plt.plot(ff, np.log10(np.abs(S1)**2) * 10, label = 'S1') # En este caso es un db de tension
plt.plot(ff, np.log10(np.abs(R)**2) * 10, label = 'Ruido')
plt.plot(ff, np.log10(np.abs(X1)**2) * 10, label = 'X1')
plt.legend()

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


