# CODIGO COMPLETO con FIR

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sig
# from matplotlib import patches
from pytc2.sistemas_lineales import plot_plantilla

# Plantilla de diseño 
# Pasabanda digital 

fs = 1000 # [Hz]
wp = (0.8, 35) # Comienzo y fin banda de paso
ws = (0.1, 40)  # Banda de stop [Hz]
# Banda de transicion de pocos hz implica orden mas elevado del polinomio 

# Divido por dos porque paso dos veces por el filtro 
alpha_p = 1/2 # Atenuacion maxima a la wp, alpha max o pérdidas en banda de paso (dB)
alpha_s = 40/2 # Atenuacion minima a la ws, alpha min o minima atenuacion requerida en banda de paso (dB)

# Aprox módulo 
f_aprox = 'butter'
mi_sos_butt = sig.iirdesign(wp = wp, ws = ws, gpass = alpha_p, gstop = alpha_s, analog = False, ftype = f_aprox, output = 'sos', fs = fs)

f_aprox = 'cauer'
mi_sos_cauer = sig.iirdesign(wp = wp, ws = ws, gpass = alpha_p, gstop = alpha_s, analog = False, ftype = f_aprox, output = 'sos', fs = fs)
# Devuelve coeficientes del polinomio 

f_aprox = 'cheby1'
mi_sos_cheb1 = sig.iirdesign(wp = wp, ws = ws, gpass = alpha_p, gstop = alpha_s, analog = False, ftype = f_aprox, output = 'sos', fs = fs)

f_aprox = 'cheby2'
mi_sos_cheb2 = sig.iirdesign(wp = wp, ws = ws, gpass = alpha_p, gstop = alpha_s, analog = False, ftype = f_aprox, output = 'sos', fs = fs)

#%%

mi_sos = mi_sos_cauer

# --- Respuesta en frecuencia ---
w, h = sig.freqz_sos(mi_sos, worN = np.logspace(-2, 1.9, 1000), fs = fs) # 10Hz a 1Hz calcula rta en frq del filtro, devuelve w y vector de salida (h es numero complejo)

# --- Cálculo de fase y retardo de grupo ---

fase = np.unwrap(np.angle(h)) # unwrap hace grafico continuo

w_rad = w / (fs / 2) * np.pi
gd = -np.diff(fase) / np.diff(w_rad) # Retardo de grupo [rad/rad]


# -- Gráficos --
plt.figure(figsize=(12,10))

# Magnitud
plt.subplot(3,1,1)
plt.plot(w, 20*np.log10(abs(h)), label=f_aprox)
plt.title('Respuesta en Magnitud')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|H(ω)| [dB]')
plt.grid(True, which='both', ls=':')
plt.legend()

# Fase
plt.subplot(3,1,2)
plt.plot(w, fase, label=f_aprox)
plt.title('Fase')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.grid(True, which='both', ls=':')
plt.legend()

# Retardo de grupo
plt.subplot(3,1,3)
plt.plot(w[1:], gd, label=f_aprox)  # Asumiendo que gd es el retardo de grupo
plt.title('Retardo de Grupo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('τg [# muestras]')
plt.grid(True, which='both', ls=':')
plt.legend()

# # --- Polos y ceros ---

# z, p, k = sig.sos2zpk(mi_sos) # Ubicacion de polos y ceros, z=ubicacion de ceros(=0), p=ubicacion polos, k

# # Diagrama de polos y ceros
# plt.figure(figsize=(10,10))
# plt.plot(np.real(p), np.imag(p), 'x', markersize=10, label=f'{f_aprox} Polos')

# axes_hdl = plt.gca()

# if len(z) > 0:
#     plt.plot(np.real(z), np.imag(z), 'o', markersize=10, fillstyle='none', label=f'{f_aprox} Ceros')
# plt.axhline(0, color='k', lw=0.5)
# plt.axvline(0, color='k', lw=0.5)

# unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='gray', ls='dotted', lw=2)
# axes_hdl.add_patch(unit_circle)

# plt.axis([-1.1, 1.1, -1.1, 1.1])
# plt.title('Diagrama de Polos y Ceros (plano Z)')
# plt.xlabel(r'$\Re(z)$')
# plt.ylabel(r'$\Im(z)$')
# plt.legend()
# plt.grid(True)
# plt.legend()

# plt.tight_layout()
# plt.show()

#%% Diseño de filtro FIR

wp = (0.8, 35) # Comienzo y fin banda de paso
ws = (0.1, 35.7)  # Banda de stop [Hz]

frecuencias = np.array([0, 0.1, 0.8, 35, 35.7, fs/2])
deseado = [0, 0, 1, 1, 0, 0] # Respuesta deseada del filtro en esa frecuencia, quiero que valga 1, que deje pasar en ese sector

cant_coef = 1000 # numtaps es coeficientes, no confundir con orden
retardo = (cant_coef - 1)//2
# fir_win_hamming = sig.firwin2(numtaps = cant_coef, freq = frecuencias, gain = deseado, fs = fs,nfreqs = int((np.ceil(np.sqrt(cant_coef)*2)**2)-1)) # hamming es la predeterminada
fir_win_rectangular = sig.firwin2(numtaps = cant_coef, freq = frecuencias, gain = deseado, window = 'boxcar', fs = fs, nfreqs = int((np.ceil(np.sqrt(cant_coef)*2)**2)-1)) # hamming es la predeterminada
# Ese fir me grafica la respuesta al impulso del filtro --> los coeficientes b --> filtro simetrico de tipo 2 --> cero topologico en pi --> nos sirve para el pasabanda
# firwin2 nos devuelve los coeficientes b --> no tenemos un output de matriz SOS porque es un sistema finito 
# Si a0 = 1 --> es un filtro recursivo --> condicion necesaria para que sea un filtro FIR
# Defino fs para que sepa que vamos a trabajar de forma desnormalizada
# nfreqs = (np.ceil(np.sqrt(cant_coef)*2)**2-1 todo este quilombo habría que revisarlo. es la mesh, la grilla, pero ni idea como la fabricó
# Igual no sirvió de nada aumentar la grilla con la ventana incorrecta. Con la rectangular sí
# Si cambio fs --> hago que la transicion tenga el doble de pendiente

cant_coeficientes = 2000
if cant_coeficientes % 2 == 0:
    cant_coeficientes += 1  # lo hace impar

fir_win_ls = sig.firls(numtaps = cant_coeficientes, bands = frecuencias, desired = deseado, fs = fs)
#%%
# mi_sos = mi_sos_cauer
# w, h = sig.freqz(b = fir_win_hamming, worN = np.logspace(-2,2, 1000),  fs = fs)
w, h = sig.freqz(b = fir_win_rectangular, worN = np.logspace(-2,2, 1000),  fs = fs)
w_ls, h_ls = sig.freqz(b = fir_win_ls, worN = np.logspace(-2,2, 1000),  fs = fs)
# --- Cálculo de fase y retardo de grupo ---

fase = np.unwrap(np.angle(h)) # unwrap hace grafico continuo
fase_ls = np.unwrap(np.angle(h_ls))

w_rad = w / (fs / 2) * np.pi
gd = -np.diff(fase) / np.diff(w_rad) # Retardo de grupo [rad/rad]

w_rad_ls = w_ls / (fs / 2) * np.pi
gd_ls = -np.diff(fase_ls) / np.diff(w_rad_ls)

# -- Gráficos --
plt.figure(figsize=(12,10))

# Magnitud
plt.subplot(3,1,1)
plt.plot(w, 20*np.log10(abs(h)), label = f_aprox)
plt.title('Respuesta en Magnitud')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|H(ω)| [dB]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# Fase
plt.subplot(3,1,2)
plt.plot(w, fase, label = f_aprox)
plt.title('Fase')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# Retardo de grupo
plt.subplot(3,1,3)
plt.plot(w[1:], gd, label = f_aprox)  # Asumiendo que gd es el retardo de grupo
plt.title('Retardo de Grupo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('τg [# muestras]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()


# Graficos de firls
plt.figure(figsize=(12,10))

# Magnitud
plt.subplot(3,1,1)
plt.plot(w_ls, 20*np.log10(abs(h_ls)), label = f_aprox)
plt.title('Respuesta en Magnitud')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|H(ω)| [dB]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# Fase
plt.subplot(3,1,2)
plt.plot(w_ls, fase_ls, label = f_aprox)
plt.title('Fase')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# Retardo de grupo
plt.subplot(3,1,3)
plt.plot(w_ls[1:], gd_ls, label = f_aprox)  # Asumiendo que gd es el retardo de grupo
plt.title('Retardo de Grupo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('τg [# muestras]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# # --- Polos y ceros ---

# z, p, k = sig.sos2zpk(sig.tf2sis(b = fir_win_hamming, a = 1)) # Ubicacion de polos y ceros, z = ubicacion de ceros(= 0), p = ubicacion polos, k
# # Primero lo pasa a sos para que lo entienda como analógico

# # Diagrama de polos y ceros
# plt.figure(figsize = (10,10))
# plt.plot(np.real(p), np.imag(p), 'x', markersize=10, label=f'{f_aprox} Polos')

# axes_hdl = plt.gca()

# if len(z) > 0:
#     plt.plot(np.real(z), np.imag(z), 'o', markersize=10, fillstyle='none', label=f'{f_aprox} Ceros')
# plt.axhline(0, color='k', lw=0.5)
# plt.axvline(0, color='k', lw=0.5)

# unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='gray', ls='dotted', lw=2)
# axes_hdl.add_patch(unit_circle)

# plt.axis([-1.1, 1.1, -1.1, 1.1])
# plt.title('Diagrama de Polos y Ceros (plano Z)')
# plt.xlabel(r'$\Re(z)$')
# plt.ylabel(r'$\Im(z)$')
# plt.legend()
# plt.grid(True)
# plt.legend()

# plt.tight_layout()
# plt.show()

#%% GRAFICOS 
# Graficos de firwin2
plt.figure(figsize=(12,10))

# Magnitud
plt.subplot(3,1,1)
plt.plot(w, 20*np.log10(abs(h)), label=f_aprox)
# plot_plantilla(filter_type='lowpass', fpass=wp, ripple=alpha_p*2, fstop=wp, attenuation=alpha_s*2, fs=fs)
plot_plantilla(filter_type = 'bandpass', fpass = wp, ripple = alpha_p*2, fstop = ws, attenuation = alpha_s*2, fs = fs)
# Banda de paso: tupla (f1, f2)
# Banda de stop: tupla (f1, f2)

plt.title('Respuesta en Magnitud')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|H(ω)| [dB]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# Fase
plt.subplot(3,1,2)
plt.plot(w, fase, label = f_aprox)
plt.title('Fase')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# Retardo de grupo
plt.subplot(3,1,3)
plt.plot(w[1:], gd, label = f_aprox)  # Asumiendo que gd es el retardo de grupo
plt.title('Retardo de Grupo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('τg [# muestras]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# Graficos de firls
plt.figure(figsize=(12,10))

# Magnitud
plt.subplot(3,1,1)
plt.plot(w_ls, 20*np.log10(abs(h_ls)), label = f_aprox)
# plot_plantilla(filter_type='lowpass', fpass=wp, ripple=alpha_p*2, fstop=wp, attenuation=alpha_s*2, fs=fs)
plot_plantilla(filter_type = 'bandpass', fpass = wp, ripple = alpha_p*2, fstop = ws, attenuation = alpha_s*2, fs = fs)
# Banda de paso: tupla (f1, f2)
# Banda de stop: tupla (f1, f2)
plt.title('Respuesta en Magnitud')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|H(ω)| [dB]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# Fase
plt.subplot(3,1,2)
plt.plot(w_ls, fase_ls, label = f_aprox)
plt.title('Fase')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()

# Retardo de grupo
plt.subplot(3,1,3)
plt.plot(w_ls[1:], gd_ls, label = f_aprox)  # Asumiendo que gd es el retardo de grupo
plt.title('Retardo de Grupo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('τg [# muestras]')
plt.grid(True, which = 'both', ls = ':')
plt.legend()
#%%
import scipy.io as sio
#          Lectura de ECG          #

fs_ecg = 1000 #Hz

#          ECG con ruido          #

# Para listar las variables que hay en el archivo
# sio.whosmat('ECG_TP4.mat')

mat_struct=sio.loadmat('./ECG_TP4.mat')
ecg_one_lead=mat_struct['ecg_lead'].flatten()
N=len(ecg_one_lead)
cant_muestras=N


ecg_filt_butt=sig.sosfiltfilt(mi_sos_butt, ecg_one_lead)
# ecg_filt_cauer=sig.sosfiltfilt(mi_sos_cauer, ecg_one_lead)
# ecg_filt_cheb1=sig.sosfiltfilt(mi_sos_cheb1, ecg_one_lead)
# ecg_filt_cheb2=sig.sosfiltfilt(mi_sos_cheb2, ecg_one_lead)

ecg_filt_win=sig.lfilter(b=fir_win_rectangular, a=1, x= ecg_one_lead)
#%%
plt.figure()
plt.plot(ecg_one_lead, label= 'ecg raw')
plt.plot(ecg_filt_butt, label='butt')
# plt.plot(ecg_filt_win, label='window')
# plt.plot(ecg_filt_cauer[:50000], label= 'cauer')
# plt.plot(ecg_filt_cbeb1[:50000], label= 'cheb1')
# plt.plot(ecg_filt_cheb2[:50000], label= 'cheb2')

plt. legend()

# Regiones de interés sin ruido #
regs_interes = (
        [4000, 5500], # Muestras
        [10e3, 11e3], # Muestras
        )
 
for ii in regs_interes:
   
    # Intervalo limitado de 0 a cant_muestras
    zoom_region = np.arange(np.max([0, ii[0]]), np.min([cant_muestras, ii[1]]), dtype='uint')
   
    plt.figure()
    plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', linewidth=2)
    plt.plot(zoom_region, ecg_filt_butt[zoom_region], label='Butterworth')
    plt.plot(zoom_region, ecg_filt_win[zoom_region + retardo], label='FIR Window')
   
    plt.title('ECG sin ruido desde' + str(ii[0]) + ' to ' + str(ii[1]) )
    plt.ylabel('Adimensional')
    plt.xlabel('Muestras (#)')
   
    axes_hdl = plt.gca()
    axes_hdl.legend()
    axes_hdl.set_yticks(())
           
    plt.show()
 

#  Regiones de interés con ruido  #
regs_interes = (
        np.array([5, 5.2]) *60*fs, # Minutos a muestras
        np.array([12, 12.4]) *60*fs, # Minutos a muestras
        np.array([15, 15.2]) *60*fs, # Minutos a muestras
        )
 
for ii in regs_interes:
   
    # Intervalo limitado de 0 a cant_muestras
    zoom_region = np.arange(np.max([0, ii[0]]), np.min([cant_muestras, ii[1]]), dtype='uint')
   
    plt.figure()
    plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', linewidth=2)
    plt.plot(zoom_region, ecg_filt_butt[zoom_region], label='Butterworth')
    plt.plot(zoom_region, ecg_filt_win[zoom_region + retardo], label='FIR Window')
   
    plt.title('ECG con ruido desde ' + str(ii[0]) + ' to ' + str(ii[1]) )
    plt.ylabel('Adimensional')
    plt.xlabel('Muestras (#)')
   
    axes_hdl = plt.gca()
    axes_hdl.legend()
    axes_hdl.set_yticks(())
           
    plt.show()

