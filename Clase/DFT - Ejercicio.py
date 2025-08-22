# Primero importo la libreria numpy
import numpy as np
import matplotlib.pyplot as plt

N = 8
n = np.arange(N)
X = np.zeros(N, dtype = np.complex128)
x = 4 + 3 * np.sin(n * np.pi / 2)

for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-1j * k * 2 * (np.pi / N) * n)

print(X)

X_modulo = np.abs(X)

plt.figure(1)

plt.subplot(1,2,1)
plt.title("Modulo de la DFT de x[n]")
plt.xlabel('k')
plt.ylabel('|X[k]|')
plt.plot(np.arange(N), X_modulo, color = 'orange')
plt.grid()


n = np.arange(N)
Y = np.zeros(N, dtype = np.complex128)
y = np.roll(x[::-1], 1)   # x[-n] (mod N)

for k in range(N):
    for n in range(N):
        Y[k] += y[n] * np.exp(-1j * k * 2 * (np.pi / N) * n)

print(Y)

Y_modulo = np.abs(Y)

plt.subplot(1,2,2)
plt.title("Modulo de la DFT de y[n] = x[-n]")
plt.xlabel('k')
plt.ylabel('|Y[k]|')
plt.plot(np.arange(N), Y_modulo)
plt.grid()

plt.tight_layout()
plt.show


# Genero otra figura para ver las diferencias entre x e y, ya que en modulo son iguales
plt.figure()

plt.subplot(1,2,1)
plt.title("Fase de X[k]")
plt.stem(np.arange(N), np.angle(X))
plt.xlabel("k"); plt.ylabel("∠X[k]")

plt.subplot(1,2,2)
plt.title("Fase de Y[k]")
plt.stem(np.arange(N), np.angle(Y))
plt.xlabel("k"); plt.ylabel("∠Y[k]")

plt.tight_layout()
plt.show()
