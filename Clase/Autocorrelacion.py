import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

M = 8

x = np.zeros(M)
y = np.zeros(M)

x[0:2] = 1 # Es lo mismo que poner x[:2], va de cero a 2
y[5] = 1

rxx = sig.correlate(x,y)
# convxy = sig.convolve(x, y)

plt.figure(1)
plt.clf()
plt.plot(x, 'x:', label = 'x')
plt.plot(y, 'x:', label = 'y')
plt.plot(rxx, 'o:', label = 'rxx')
# plt.plot(convxy, 'o:', label = 'convolusion')
plt.legend()
plt.show







