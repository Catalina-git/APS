# Primero importo la libreria numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.o import wavfile

"""
BONUS
5) Bajar un wav de freesoung.org, graficarlo y calcular la energia
"""

# Cargo el archivo .wav
fs, data = wavfile.read('archivo.wav') # fs es la frecuencia de muestreo

# Si es estereo, lo convierto a mono
if data.ndim > 1:
    data = data.mean(axis = 1)
    
t = np.arange(len(data)) / fs # Creo el eje del tiempo

# Grafico
plt.figure()
plt.plot(t, data)
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.title('Forma de onda del audio .wav')
plt.grid()
plt.show()


