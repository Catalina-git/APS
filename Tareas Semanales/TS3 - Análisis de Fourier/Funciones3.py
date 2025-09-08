import numpy as np


def mi_funcion_sen(frecuencia, nn, amplitud = 1, offset = 0, fase = 0, fs = 2): # Si lo igualo a algo es opcional, entonces si no le paso nada el programa me lo hace cero
     # Los obligatorios van al principio del parentesis y los opcionales al final    

    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= nn*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    return tt, xx




