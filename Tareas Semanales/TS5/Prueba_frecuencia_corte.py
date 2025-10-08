import numpy as np
from scipy import signal as sig
import matplotlib.pyplot as plt

# Parámetros
fs_ecg = 1000  # Hz
ecg = np.load('ecg_sin_ruido.npy').astype(float)

# Quitar componente DC
ecg = ecg - np.mean(ecg)

# Welch
cant_promedio = 10
nperseg = len(ecg) // cant_promedio
f, Pxx = sig.welch(ecg, fs=fs_ecg, window='hann', nperseg=nperseg)

# Quitar el bin de 0 Hz (para evitar que el DC distorsione la energía acumulada)
f = f[1:]
Pxx = Pxx[1:]

# Cálculo de energía acumulada real
df = f[1] - f[0]
energia_acum = np.cumsum(Pxx) * df
energia_acum_normal = energia_acum / energia_acum[-1]

# Frecuencia de corte (98% de la energía)
indice_corte = np.argmax(energia_acum_normal >= 0.98)
frecuencia_corte = f[indice_corte]

print(f"Frecuencia de corte ≈ {frecuencia_corte:.2f} Hz")

# Gráficos
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(f, Pxx)
plt.axvline(frecuencia_corte, color='orange', linestyle='--', label=f'fc = {frecuencia_corte:.2f} Hz')
plt.xlim(0, 50)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("PSD (V²/Hz)")
plt.title("ECG sin ruido por Método de Welch")
plt.legend()

plt.subplot(1,2,2)
plt.plot(f, energia_acum_normal)
plt.axvline(frecuencia_corte, color='orange', linestyle='--')
plt.axhline(0.98, color='gray', linestyle=':')
plt.xlim(0, 50)
plt.ylim(0, 1.02)
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Energía acumulada normalizada")
plt.title("Energía acumulada (98%)")

plt.tight_layout()
plt.show()

