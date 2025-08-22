# Primero importo la libreria numpy
import numpy as np
import matplotlib.pyplot as plt

N = 8
n = np.arange(N)
X = np.zeros(N, dtype = np.complex128)
x = 4 + 3 * np.sin(n * np.pi / 2)

for k in range(N):
    for m in range(N):
        X[k] += x[m] * np.exp(-1j * k * 2 * (np.pi / N) * m)

print(X)

X_modulo = np.abs(np.fft.fftshift(X))

plt.figure(1)

plt.subplot(1,2,1)
plt.title("Modulo de la DFT de x[n]")
plt.xlabel('k')
plt.ylabel('|X[k]|')
plt.plot(np.arange(N), X_modulo, color = 'orange')
plt.grid()


n = np.arange(N)
Y = np.zeros(N, dtype = np.complex128)
y = np.flip(x)

for k in range(N):
    for m in range(N):
        Y[k] += y[m] * np.exp(-1j * k * 2 * (np.pi / N) * m)

print(Y)

Y_modulo = np.abs(np.fft.fftshift(Y))

plt.subplot(1,2,2)
plt.title("Modulo de la DFT de y[n] = x[-n]")
plt.xlabel('k')
plt.ylabel('|Y[k]|')
plt.plot(np.arange(N), Y_modulo)
plt.grid()

plt.tight_layout()
plt.show
