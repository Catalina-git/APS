# Primero importo la libreria numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Defino mis funciones
# Funcion de una señal sinusoidal
def mi_funcion_sen(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, frecADC = 1000):
    """
    - amplitud: es la amplitud maxima. [amplitud] = [V]
    - offset: es mi amplitud media. [offset] = [V]
    - frecuencia: es la frecuencia de la señal. [frecuencia] = [Hz]
    - fase: es la fase inicial. [fase] = [rad]
    - N: es la cantidad de muestras a generar
    - frecADC: es la frecuencia de muestreo del ADC. [frecADC] = [Hz]
    """
    Ts = 1/frecADC # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    return tt, xx

# Funcion del coseno
def mi_funcion_cos(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, frecADC = 1000):
    
    Ts = 1/frecADC # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.cos(2 * np.pi * frecuencia * tt + fase) + offset

    return tt, xx

# Funcion de una señal sinusoidal modulada en amplitud por otra señal sinusoidal de la mitad de frecuencia
def mi_funcion_sen_modulada(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, frecADC = 1000):
   
    Ts = 1/frecADC # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) * np.sin(2 * np.pi * frecuencia/2 * tt + fase) + offset

    return tt, xx

# Funcion para redcortar una funcion al 75% de su amplitud
def mi_funcion_sen_recortada(amplitud = 1, offset = 0, frecuencia = 1, fase = 0, N = 1000, frecADC = 1000):
    
    Ts = 1/frecADC # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    valor_corte = amplitud * 0.75 # es el 75% de la amplitud
    
    xx = np.clip(xx, - valor_corte, valor_corte) # Funcion de numpy que me recorta la señal
    
    return tt, xx

# Funcion para una señal cuadrada
def mi_funcion_cuadrada (frecuencia, frecADC, N, offset, fase):
    Ts = 1/frecADC # Es el tiempo en el cual se toma cada muestra

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
    
    print(x)
    
    return x

#Funcion para calcular ortogonalidad entre dos señales
def mi_funcion_ortogonalidad (f,g):
    productoInterno = np.dot(f,g)
    
    if (productoInterno == 0):
        return True
    else: 
        return False

def mi_funcion_propiedad(a,b):
    _,xa = mi_funcion_sen(frecuencia = a)
    _,xaa = mi_funcion_sen(frecuencia = b)
    
    f = 2 * xa * xaa
    
    _,xb = mi_funcion_cos(frecuencia = a - b)
    _,xbb = mi_funcion_cos(frecuencia = a + b)
    
    g = xb - xbb
    
    return f, g
    
    
    
    
    