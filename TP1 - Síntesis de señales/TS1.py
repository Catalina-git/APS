# Primero importo la libreria numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import Funciones as ts1
from scipy.io import wavfile # Libreria que uso para el ejercicio 5

# ------------------------------- EJERCICIO 1 -------------------------------
"""
1) Sintetizar y graficar: --> uso funciones de numpy
    a. Una señal sinusoidal de 2KHz
    b. Misma señal amplificada y desfazada en pi/2
    c. Señal anterior modulada en amplitud por otra señal sinusoidal de la mitad de frecuencia. --> modular es multiplicar por otra señal, en este caso va a ser de 1kHz --> sen(2*t) * sen(t) --> reemplazo A (amplitud) por la funcion que modula
    d. Señal anterior recortada al 75% de su amplitud --> potencia = A**2 / 2 --> despues se hace con una funcion de numpy --> la salida es recta arriba y abajo --> recorto todo lo que supere el 75% de la potencia
    --> las funciones con las que trabajamos no son periodicas (vemos N-muestras) --> vamos a calcular energias --> tomamos potencia como energia
    --> tengo que recortar la amplitud al valor del 75% de la potencia de la señal
    --> una manera es ir recorriendo el vector, y cuando llego a un valor que es mayor que el 75% de la potencia, lo cambio por el valor corte = treasure = 75% de la potencia
    --> otra manera, busco la funcion de numpy --> np.clip
    e. Una señal cuadrada de 4KHz
    f. Un pulso rectangular de 10ms
    g. En cada caso indique tiempo entre muestras, numero de mustras y potencia
"""
    
""" ITEM a """
# ------------------------------- Señal sinusoidal de 2kHz -------------------------------
# Llamo a mi funcion
_,fa = ts1.mi_funcion_sen(1, 0, 2000, 0, 100, 40000) # Pongo frecADC > 2 * frecuencia --> Teorema de Nyquist-Shannon

# Genero otra ventana para los graficos
plt.figure()  # Tamaño de la figura (ancho, alto)
plt.subplot(2,2,1)

plt.title("Señal Sinusoidal")

# Grafico la señal senoidal de 2KHz
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(_,fa, 'o--',  label = 'Sinusoidal de 2kHz')
plt.legend()

# Calculo la potenacia
x = ts1.calcular_potencia(fa)
print("Potencia de la señal fa: ", x)

""" ITEM b """
# ------------------------------- Señal sinusoidal de 2kHz, amplificada y desfazada en pi/2 -------------------------------
_,fb = ts1.mi_funcion_sen(2, 0, 2000, np.pi/2, 100, 40000) 

# Grafico la señal senoidal de 2KHz, pero amplificada y desfazada en pi/2
plt.subplot(2,2,2)
plt.title("Señal Sinusoidal")

# Grafico la señal senoidal de 2KHz
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(_,fa, 'o--',  label = 'Sinusoidal de 2kHz')
plt.legend()

plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(_,fb, 'x:', label = '2kHz, amplificada y desfazada en pi/2')
plt.legend()

# Calculo la potenacia
x = ts1.calcular_potencia(fb)
print("Potencia de la señal fb: ", x)

""" ITEM c """
# ------------------------------- Señal sinusoidal modulada por otra señal sinusoidal de 1kHz -------------------------------
_,fc = ts1.mi_funcion_sen_modulada(1, 0, 1000, 0, 100, 40000)

# Grafico la señal senoidal de 2KHz, pero modulada por otra señal de la mitad de la frecuencia
plt.subplot(2,2,3)
plt.title("Señal Sinusoidal")

# Grafico la señal senoidal de 2KHz
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(_,fa, 'o--',  label = 'Sinusoidal de 2kHz')
plt.legend()

plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(_, fc, 'x:', label = 'Señal modulada') # Genero el grafico de la señal
plt.legend()

# Calculo la potenacia
x = ts1.calcular_potencia(fc)
print("Potencia de la señal fc: ", x)

""" ITEM d """
# ------------------------------- Misma señal pero recortada al 75% de su potencia -------------------------------
_,fd = ts1.mi_funcion_sen_recortada(1, 0, 2000, 0, 100, 40000)

plt.subplot(2,2,4)
plt.title("Señal Sinusoidal")

# Grafico la señal senoidal de 2KHz
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(_,fa, 'o--',  label = 'Sinusoidal de 2kHz')
plt.legend()

# Grafico la señal recortada
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(_,fd, '*--', label = 'Señal recortada al 75%')
plt.legend()

# Calculo la potenacia
x = ts1.calcular_potencia(fd)
print("Potencia de la señal fd: ", x)

""" ITEM e """
# ------------------------------- Señal cuadrada de 4kHz -------------------------------
# Llamo a mi funcion
_,fe = ts1.mi_funcion_cuadrada(4000, 80000, 100, 0, 0)

# Grafico la señal cuadrada
plt.figure()
plt.subplot(1,2,1)
plt.title('Señal cuadrada de 4kHz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(_,fe, 'o--', label = 'Señal cuadrada de 4Hz')
plt.legend()

# Calculo la potenacia
x = ts1.calcular_potencia(fe)
print("Potencia de la señal fe: ", x)

""" ITEM f """
# ------------------------------- Pulso rectangular de 10ms -------------------------------
ff = ts1.mi_funcion_pulso(1, 11, 100, 1)

# Grafico
plt.subplot(1,2,2)
plt.title('Pulso rectangular de 10ms')
plt.plot(ff, 'o--', label = 'Pulso rectangular de 10ms')
# otra manera de graficar el pulso: 
# plt.stem(x)
plt.xlabel('Tiempo[ms]')
plt.ylabel('Amplitud [V]')
plt.axis([-2,15,0,1.5]) #Limites del grafico ([Xmin,Xmax,Ymin,Ymax]), si no se agrega este plt (axis) el programa por default busca mostrar todo el grafico completo
plt.legend()
plt.show()

# Calculo la energia
x = ts1.calcular_energia(ff)
print("Energia de la señal ff: ", x)


# ------------------------------- EJERCICIO 2 -------------------------------
"""
2) Verificar ortogonalidad entre la primera señal y las demas --> multiplicar matricialmente, filas por columnas, y tiene que dar cero
--> hago el producto interno entre vectores, si es cero son ortogonales --> hay funciones en numpy para calcularlo --> inner_product
"""

print("\nORTOGONALIDAD ENTRE SEÑALES")

# Verifico ortogonalidad
if (ts1.mi_funcion_ortogonalidad(fa, fb)):
    print("La funcion del item a y del item b son ortogonales\n")
else:
    print("La funcion del item a y del item b NO son ortogonales\n")
    
if (ts1.mi_funcion_ortogonalidad(fa, fc)):
  print("La funcion del item a y del item c son ortogonales\n")
else:
  print("La funcion del item a y del item c NO son ortogonales\n")
        
if (ts1.mi_funcion_ortogonalidad(fa, fd)):
   print("La funcion del item a y del item d son ortogonales\n")
else:
   print("La funcion del item a y del item d NO son ortogonales\n")
            
if (ts1.mi_funcion_ortogonalidad(fa, fe)):
  print("La funcion del item a y del item e son ortogonales\n")
else:
  print("La funcion del item a y del item e NO son ortogonales\n")
  
if (ts1.mi_funcion_ortogonalidad(fa, ff)):
    print("La funcion del item a y del item f son ortogonales\n")
else:
    print("La funcion del item a y del item f NO son ortogonales\n")

# ------------------------------- EJERCICIO 3 -------------------------------
"""
3) Graficar la autocorrelacion de la primera señal y la correlacion entre esta y las demas. 
    Autocorrelacion --> similitud lineal, similitud consigomismo
    scipy tiene una funcion que te hace la correlacion
"""

# ------------------------------- Correlacion -------------------------------
rxx1 = signal.correlate(fa,fa)

rxx2 = signal.correlate(fa,fb)

rxx3 = signal.correlate(fa,fc)

rxx4 = signal.correlate(fa,fd)

rxx5 = signal.correlate(fa,fe)

rxx6 = signal.correlate(fa,ff)

# Grafico de las correlaciones
plt.figure()

plt.subplot(2,3,1)
plt.title('Autocorrelacion de fa')
plt.plot(rxx1, 'o:')
plt.xlabel('Retardo [muestras]')
plt.ylabel('Valor de la autocorrelación')

plt.subplot(2,3,2)
plt.title('Correlacion entre fa y fb')
plt.plot(rxx2, 'o:')
plt.xlabel('Retardo [muestras]')
plt.ylabel('Valor de correlación')

plt.subplot(2,3,3)
plt.title('Correlacion entre fa y fc')
plt.plot(rxx3, 'o:')
plt.xlabel('Retardo [muestras]')
plt.ylabel('Valor de correlación')

plt.subplot(2,3,4)
plt.title('Correlacion entre fa y fd')
plt.plot(rxx4, 'o:')
plt.xlabel('Retardo [muestras]')
plt.ylabel('Valor de correlación')

plt.subplot(2,3,5)
plt.title('Correlacion entre fa y fe')
plt.plot(rxx5, 'o:')
plt.xlabel('Retardo [muestras]')
plt.ylabel('Valor de correlación')

plt.subplot(2,3,6)
plt.title('Correlacion entre fa y ff')
plt.plot(rxx6, 'o:')
plt.xlabel('Retardo [muestras]')
plt.ylabel('Valor de correlación')

plt.show()


# ------------------------------- EJERCICIO 4 -------------------------------
"""
4) Dada la siguiente propiedad trigonometrica
    2 * sin(alfa) * sin (beta) = cos(alfa - beta) - cos(alfa + beta)
    - Demostrar la igualdad
    - Mostrar que la igualdad se cumple con señales sinusoidales, considerando alfa = w * t, el doble de beta (use la frecuencia que desee).
"""

f,_ = ts1.mi_funcion_propiedad(np.pi, np.pi/2) 
_,g = ts1.mi_funcion_propiedad(np.pi, np.pi/2) 


plt.figure()

plt.subplot(1,3,1)
plt.title('Primer lado de la igualdad')
plt.plot(f, 'o:')
plt.xlabel('Muestras')   
plt.ylabel('Amplitud [V]')

plt.subplot(1,3,2)
plt.title('Segundo lado de la igualdad')
plt.plot(g,'o:')
plt.xlabel('Muestras') 
plt.ylabel('Amplitud [V]')

plt.subplot(1,3,3)
plt.title('Superposicion')
plt.plot(f, 'o:')
plt.plot(g,'o:')
plt.xlabel('Muestras')  
plt.ylabel('Amplitud [V]')

plt.show()


# ------------------------------- EJERCICIO 5 -------------------------------
"""
BONUS
5) Bajar un wav de freesoung.org, graficarlo y calcular la energia
"""

# Cargo el archivo .wav
fs, data = wavfile.read('sonido.wav') # fs es la frecuencia de muestreo

# Una señal ESTEREO tiene dos canales, uno para el lado izquierdo y uno para el derecho
# Se usa para que un sonido venga de muchos lugares
# Una señal MONO es una señal que sale toda por el mismo canal, sin distinguir entre izquierda y derecha
# Uso mono porque para analizar señales es mas simple
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

# Calculo la energia
energia = np.sum(data**2) # La energia es la suma del cuadrado de las muestras, me da "cuan intensa" es la señal
print(f"\nEnergía total: {energia:.2f}")

