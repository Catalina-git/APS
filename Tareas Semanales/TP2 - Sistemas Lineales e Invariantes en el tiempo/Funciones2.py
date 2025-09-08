import numpy as np
from scipy.signal import lfilter, unit_impulse
from scipy import signal

# %% Parametros del sistema

N = 100
# Coeficientes del sistema
b = [0.03, 0.05, 0.03]  # Coeficientes de entrada x[n]
a = [1, -1.5, 0.5]      # Coeficientes de salida y[n]. El signo inverido es para lfilter

# %% FUNCIONES
# Funcion para simular el sistema 
# Uso lfilter porque me permite poner condiciones iniciales. 
# Le paso los coeficientes y me devuelve la salida. 
def simular(x):
    """
    Simula el sistema LTI
    
    Parámetros:
        - x: señal de entrada
    
    Retorna:
        - y: señal de salida
    """
    y = np.zeros(N) # Armo mi array solucion y lo inicializo en cero
    
    # Es la implementacion del 0 padding
    # Funciones de numpy para concatenar dos vectores: v h stack cat concat
    # Pongo un prefijo y un subfijo de ceros --> xz(n) = [np.zeros(N), x, np.zeros(N)]
    # Demore a mi funcion N-muestras
    # Si quiero extraer solamente x --> xz[N, -N]
    # Todas las funciones utilizadas las consideramos causales
    # Mi entrada y mi salida son causales --> para todo n < 0 mi array vale 0
    for n in range(len(x)):
        x_n = x[n] if n >= 0 else 0
        x_n1 = x[n - 1] if n >= 0 else 0
        x_n2 = x[n - 2] if n >= 0 else 0
        y_n1 = y[n - 1] if n >= 0 else 0
        y_n2 = y[n - 2] if n >= 0 else 0
        
        y[n] = (0.03 * x_n + 0.05 * x_n1 + 0.03 * x_n2 + 1.5 * y_n1 - 0.5 * y_n2)
    
    return y

# Funcion para hallar la respuesta al impulso
def respuesta_impulso(a, b):
    delta = unit_impulse(N)
    h = lfilter(b, a, delta)
    
    return h

# FUNCIONES DE LAS SEÑALES DEL TS1
# Funcion de una señal sinusoidal
def mi_funcion_sen(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, fs = 1000):
    """
    - amplitud: es la amplitud maxima. [amplitud] = [V]
    - offset: es mi amplitud media. [offset] = [V]
    - frecuencia: es la frecuencia de la señal. [frecuencia] = [Hz]
    - fase: es la fase inicial. [fase] = [rad]
    - N: es la cantidad de muestras a generar
    - fs: es la frecuencia de muestreo del ADC. [fs] = [Hz]
    """
    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    return tt, xx

# Funcion de una señal sinusoidal modulada en amplitud por otra señal sinusoidal de la mitad de frecuencia
def mi_funcion_sen_modulada(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, fs = 1000):
   
    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) * np.sin(2 * np.pi * frecuencia/2 * tt + fase) + offset

    return tt, xx

# Funcion para redcortar una funcion al 75% de su amplitud
def mi_funcion_sen_recortada(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, fs = 1000):
    
    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    valor_corte = amplitud * 0.75 # es el 75% de la amplitud
    
    xx = np.clip(xx, - valor_corte, valor_corte) # Funcion de numpy que me recorta la señal
    
    return tt, xx

# Funcion para una señal cuadrada
def mi_funcion_cuadrada (frecuencia, fs, N, offset, fase):
    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    ttc = np.arange(start = 0, stop= N*Ts, step = Ts)

    xxc = signal.square(2 * np.pi * frecuencia * ttc + fase) + offset

    return ttc, xxc

# Funcion para un pulso
def mi_funcion_pulso (t0, tf, N, h):
    """
    t0: tiempo donde empieza el pulso
    tf: hasta donde 
    N: cantidad de muestras
    h: altura

    """
    
    x = np.zeros(N)
    x[t0:tf] = h
    
    return x

# Funcion para calcular la potencia de una señal
def calcular_potencia(x):
    return np.mean(x**2)

# Funcion para calcular la energia de una señal
def calcular_energia(x):
    return np.sum(x**2)
    
    