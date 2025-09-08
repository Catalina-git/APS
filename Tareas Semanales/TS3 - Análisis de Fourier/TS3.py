import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import Funciones3 as ts3

# %% DATOS DEL PROBLEMA
"""
- Senoidal de frecuencia: f0 = k0 * fs / N = k0 * Δf
- Potencia normalizada, es decir energ[ia (o varianza) unitaria.
                                       
"""
# %% ------------------------------- EJERCICIO a -------------------------------
"""
Sea k0: 
    - N / 4
    - N / 4 + 0.25
    - N / 4 + 0.5
 
Notar que a cada senoidal se le agrega una pequeña desintonía respecto a  Δf
Graficar las tres densidades espectrales de potencia (PDS's) y discutir cuál es el efecto de dicha desintonía en el espectro visualizado.

"""
# %% DEFINO LAS VARIABLES
N = 1000
fs = N
df = fs/N # Resolucion temporal

# %% CALCULOS
# Las x en minuscula es porque estan en el espectro del tiempo
k0 = N / 4
t1,x1 = ts3.mi_funcion_sen(frecuencia = k0 * df, nn = N, fs = fs)

k0 = N / 4 + 0.25
t2,x2 = ts3.mi_funcion_sen(frecuencia = k0 * df, nn = N, fs = fs)

k0 = N / 4 + 0.5
t3,x3 = ts3.mi_funcion_sen(frecuencia = k0 * df, nn = N, fs = fs)

# CALCULO LA DFFT
# Las X en mayuscula son en el espectro de frecuencias, transformadas
X1 = fft(x1)
X2 = fft(x2)
X3 = fft(x3)

PDS1 = np.abs(X1)**2
PDS2 = np.abs(X2)**2
PDS3 = np.abs(X3)**2

# %% GRAFICOS EN db
ff = np.arange(N) * df # Es un arange de N que necesito para graficar

plt.figure()  # Tamaño de la figura (ancho, alto)
# plt.clf --> me borra los graficos cuando tengo muchos y los voy cerrando

# Grafico X1 en db
# plt.subplot(1,3,1)

plt.title("Densidadesespectrales de potencia (PDS) en db")

# plt.title("Modulo de la DFFT con frecuencia = (N/4)")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.xlim([0, fs/2]) # En este caso fs = N, pero pongo fs para saber que va eso y no va siempre N
plt.plot(ff, np.log10(PDS1) * 10, 'o', label = 'frecuencia = N / 4') # En este caso es un db de tension
plt.legend()
 
# Grafico X2
# plt.subplot(1,3,2)

# plt.title("Modulo de la DFFT con frecuencia = (N/4) + 0.5")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.xlim([0, fs/2]) # Una tuppla
plt.plot(ff, np.log10(PDS2) * 10, 'x', label = 'frecuencia = N / 4 + 0.25')
plt.legend()

# Grafico X3
# plt.subplot(1,3,3)

# plt.title("Modulo de la DFFT con frecuencia = (N/4) + 1")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.xlim([0, fs/2]) # Una tuppla, por eso los corchetes, puede ser tambien entre parentesis 
plt.plot(ff, np.log10(PDS3) * 10, '+', label = 'frecuencia = N / 4 + 0.5')
plt.legend()

plt.show()

# %% ANALISIS
# - Cuando la frecuencia es exactamente múltiplo de Δf (como N/4), 
#   la energía se concentra en un solo bin de la FFT → pico muy definido.
# - Al desintonar ligeramente (N/4 + 0.25 o N/4 + 0.5), 
#   la energía se distribuye entre varios bins → el pico se ensancha y pierde definición.
# - Esto se debe a que la frecuencia ya no coincide exactamente con un bin de la FFT, 
#   lo que genera fugas espectrales (leakage).

# %% ------------------------------- EJERCICIO b -------------------------------
""" 
Verificar la potencia unitaria de cada PSD, puede usar la identidad de Parseval. En base a la teoría estudiada. 
Discuta la razón por la cual una señal senoidal tiene un espectro tan diferente respecto a otra de muy pocos Hertz de diferencia.

"""

t1, x1 = ts3.mi_funcion_sen(frecuencia = (N/4) * df, nn = N, amplitud = np.sqrt(2), fs = fs) # Sinusoidal con varianza unitaria ==> amp = raiz de 2

varianza = np.var(x1)
# media = np.mean(x1)
# desviacion_estandar = np.std(x1)

print(f"Varianza = {varianza:.5f}")
# print(f"Media = {media:.5f}")
# print(f"Desviacion estandar = {desviacion_estandar:.5f}")

t3, x3 = ts3.mi_funcion_sen(frecuencia = (N/4 + 0.25) * df, nn = N, amplitud = np.sqrt(2), fs = fs) # Sinusoidal con varianza unitaria ==> amp = raiz de 2

varianza = np.var(x2)
# media = np.mean(x2)
# desviacion_estandar = np.std(x2)

print(f"Varianza = {varianza:.5f}")
# print(f"Media = {media:.5f}")
# print(f"Desviacion estandar = {desviacion_estandar:.5f}")

t3, x3 = ts3.mi_funcion_sen(frecuencia = (N/4 + 0.5) * df, nn = N, amplitud = np.sqrt(2), fs = fs) # Sinusoidal con varianza unitaria ==> amp = raiz de 2

varianza = np.var(x3)
# media = np.mean(x3)
# desviacion_estandar = np.std(x3)

print(f"Varianza = {varianza:.5f}")
# print(f"Media = {media:.5f}")
# print(f"Desviacion estandar = {desviacion_estandar:.5f}")

# %% ANALISIS
# - Todas las señales tienen potencia unitaria (varianza = 1), 
#   y eso se verifica tanto en tiempo como en frecuencia gracias a Parseval.
# - Aunque la energía total es la misma, cómo se distribuye en el espectro cambia drásticamente:
# - La senoidal con frecuencia exacta (N/4) concentra toda la energía en un solo bin → espectro “filoso”.
# - Las desintonadas (N/4 + 0.25 y N/4 + 0.5) dispersan la energía → espectros más “anchos” y menos definidos.
# - Esto se debe al leakage espectral: cuando la frecuencia no coincide con un bin de la FFT, la energía se reparte entre varios.

# %% ------------------------------- EJERCICIO c -------------------------------
""" 
Repetir el experimento mediante la técnica de zero padding. 
Dicha técnica consiste en agregar ceros al final de la señal para aumentar Δf de forma ficticia.
Probar agregando un vector de 9*N ceros al final. Discuta los resultados obtenidos.

"""

zp = np.zeros(9 * N)

x1p = np.concatenate((x1, zp))
x2p = np.concatenate((x2, zp))
x3p = np.concatenate((x3, zp))

# Calculo la FFT
X1p = fft(x1p)
X2p = fft(x2p)
X3p = fft(x3p)

# Ejes de frecuencia
Npadding = len(x1p)
df_padding = fs / Npadding
ff_padding = np.arange(Npadding) * df_padding

# Grafico en db
plt.figure()
plt.title("PDS con Zero Padding (en db)")

plt.plot(ff_padding, 10 * np.log10(np.abs(X1p)**2), 'o', label = 'frecuencia = N / 4')
plt.plot(ff_padding, 10 * np.log10(np.abs(X2p)**2), 'x', label = 'frecuencia = N / 4 + 0.25')
plt.plot(ff_padding, 10 * np.log10(np.abs(X2p)**2), '+', label = 'frecuencia = N / 4 + 0.5')

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("PDS [db]")
plt.legend()
plt.tight_layout()
plt.show()

# %% ANALISIS
# - El zero padding no cambia la energía ni la forma de la señal, 
#   pero interpela el espectro → más puntos entre bins.
# - Mejora la resolución visual del espectro: 
#   los picos se ven más definidos, especialmente en las señales desintonadas.
# - No elimina el leakage, pero permite verlo con más detalle y distinguir mejor las diferencias entre frecuencias cercanas.





