import numpy as np
import matplotlib.pyplot as plt
import Funciones2 as ts2

# %% Parámetros de simulación

fs = 40000  # Frecuencia de muestreo en Hz
T = 1 / fs
N = 100


# %% ------------------------------- EJERCICIO 1 -------------------------------

"""
1) Dada la siguiente ecuacion en diferencias que modela un sistema LTI:
    y[n] = 0,03 * x[n] + 0,005 *x[n - 1] + 0,03 * x[n - 2] + 1,5 * y[n - 1] - 0,5 * y[n - 2]
    
    a. Graficar la señal de salida para cada una de las señales de entrada que generó en el TS1. 
    Considere que las mismas son causales.
    b. Hallar la respuesta al impulso y usando la misma, repetir la generacion de la señal de salida 
    para alguna de las señales de entrada consideradas en el punto anterior.
    
    - En cada caso, indique la frecuencia de muestreo, el tiempo de simulacion 
    y la potencia o energía de la señal de salida. 

"""

# %% Coeficientes del sistema (ecuacion de diferencias dada en el enunciado)

b = [0.03, 0.05, 0.03]  # Coeficientes de entrada x[n]
a = [1, -1.5, 0.5]        # Coeficientes de salida y[n]. El signo inverido es para lfilter

# %% """ ITEM a """

# Graficos de las señales de salida de cada una de las señales generadas en el TS1

# Llamo a mis funciones del TS1
# Señales del TS1
t1, x1 = ts2.mi_funcion_sen(1, 0, 2000, 0, 100, fs) # Funcion senoidal original del TS1
t2, x2 = ts2.mi_funcion_sen(2, 0, 2000, np.pi/2, 100, fs) # Misma funcion amplificada y desfazada en pi/2
t3, x3 = ts2.mi_funcion_sen_modulada(1, 0, 2000, 0, 100, fs) # Funcion senoidal original modulada por otra
t4, x4 = ts2.mi_funcion_sen_recortada(1, 0, 2000, 0, 100, fs) # Funcion original recortada al 75% de su amplitud
t5, x5 = ts2.mi_funcion_cuadrada(4000, fs, 100, 0, 0) # Funcion cuadrada creada con SciPy
x6 = ts2.mi_funcion_pulso(1, 11, 100, 1) # Funcion pulso de 10ms

# Paso a mis funciones del TS1 por la ecuacion en diferencias
# Simulaciones

y1 = ts2.simular(x1)
y2 = ts2.simular(x2)
y3 = ts2.simular(x3)
y4 = ts2.simular(x4)
y5 = ts2.simular(x5)
y6 = ts2.simular(x6)

# Grafico la señal de salida de cada una se las funciones del TS1
plt.figure()

# Señal sinusoidal de 2kHz
plt.subplot(2, 3, 1)
plt.plot(t1, x1, 'o-', label = 'Entrada')
plt.plot(t1, y1, 'o-', label = 'Salida')
plt.title('Salida del sistema de la señal senoidal de 2kHz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.tight_layout()

# Señal amplificada y desfazada
plt.subplot(2, 3, 2)
plt.plot(t2, x2, 'o-', label = 'Entrada')
plt.plot(t2, y2, 'o-', label = 'Salida')
plt.title('Salida del sistema de la señal amplificada y desfazada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.tight_layout()

# Señal modulada
plt.subplot(2, 3, 3)
plt.plot(t3, x3, 'o-', label = 'Entrada')
plt.plot(t3, y3, 'o-', label = 'Salida')
plt.title('Salida del sistema de la señal modulada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.tight_layout()

# Señal recortada al 75%
plt.subplot(2, 3, 4)
plt.plot(t4, x4, 'o-', label = 'Entrada')
plt.plot(t4, y4, 'o-', label = 'Salida')
plt.title('Salida del sistema de la señal recortada al 75%')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.tight_layout()

# Señal cuadrada de 4kHz
plt.subplot(2, 3, 5)
plt.plot(t5, x5, 'o-', label = 'Entrada')
plt.plot(t5, y5, 'o-', label = 'Salida')
plt.title('Salida del sistema de la señal cuadrada de 4kHz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.tight_layout()

# Pulso rectangular de 10ms
plt.subplot(2, 3, 6)
plt.plot(x6, 'o-', label = 'Entrada')
plt.plot(y6, 'o-', label = 'Salida')
plt.title('Salida del sistema del pulso rectangular de 10ms')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.tight_layout()

plt.show()

# CALCULO  LA POTENCIA 
print("\nPOTENCIAS Y ENERGIAS DEL EJERCICIO 1 (ITEM a)\n")

# Calculo la potenacia
p1 = ts2.calcular_potencia(y1)
print("Potencia de la salida generada por la señal fa: ", p1)

p2 = ts2.calcular_potencia(y2)
print("Potencia de la salida generada por la señal fb: ", p2)

p3 = ts2.calcular_potencia(y3)
print("Potencia de la salida generada por la señal fc: ", p3)

p4 = ts2.calcular_potencia(y4)
print("Potencia de la salida generada por la señal fd: ", p4)

p5 = ts2.calcular_potencia(y5)
print("Potencia de la salida generada por la señal fe: ", p5)

p6 = ts2.calcular_potencia(y6)
print("Potencia de la salida generada por la señal ff: ", p6)
# %% """ ITEM b """
# Respuesta al impulso h[n]

# Hago la convolucion entre la señal y el impulso --> y eso me genera la nueva salida y[n]

# Llamo a mi funcion impulso
h = ts2.respuesta_impulso(a, b)

yy1 = np.convolve(x1, h)
yy2 = np.convolve(x2, h)
yy3 = np.convolve(x3, h)
yy4 = np.convolve(x4, h)
yy5 = np.convolve(x5, h)
yy6 = np.convolve(x6, h)

# Vector de tiempo para convolución (mismo fs, pero puede tener más muestras)
t_conv1 = np.arange(len(yy1)) / fs
t_conv2 = np.arange(len(yy2)) / fs
t_conv3 = np.arange(len(yy3)) / fs
t_conv4 = np.arange(len(yy4)) / fs
t_conv5 = np.arange(len(yy5)) / fs
dt = 1/fs
t_yy6 = np.arange(len(yy6)) * dt
t_x6 = np.arange(len(x6)) * dt

# Grafico --> deberia darme igual que lo calculado a traves de la ecuacion en diferencias
plt.figure()

plt.subplot(2, 3, 1)
plt.plot(t_conv1, yy1, 'x-', label='Salida')
plt.plot(t1, x1, 'o-', label='Entrada')
plt.title('Salida de la funcion senoidal calculada con convolucion')
plt.xlabel('Tiempo [s]')
plt.xlim(0, max(t1))
plt.legend()
plt.tight_layout()

plt.subplot(2, 3, 2)
plt.plot(t_conv2, yy2, 'x-', label = 'Salida')
plt.plot(t2,x2, 'o-', label = 'Entrada')
plt.title('Salida calculada indirectamente de la señal amplificada y desfazada')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.xlim(0, max(t2))
plt.legend()
plt.tight_layout()

plt.subplot(2, 3, 3)
plt.plot(t_conv3, yy3, 'x-', label = 'Salida')
plt.plot(t3, x3, 'o-', label = 'Entrada')
plt.title('Salida de la funcion modulada calculada con convolucion')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.xlim(0, max(t3))
plt.legend()
plt.tight_layout()

plt.subplot(2, 3, 4)
plt.plot(t_conv4, yy4, 'x-', label = 'Salida')
plt.plot(t4, x4, 'o-', label = 'Entrada')
plt.title('Salida de la funcion recortada calculada con convolucion')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.xlim(0, max(t4))
plt.legend()
plt.tight_layout()

plt.subplot(2, 3, 5)
plt.plot(t_conv5, yy5, 'x-', label = 'Salida')
plt.plot(t5, x5, 'o-', label = 'Entrada')
plt.title('Salida de la funcion cuadrada calculada con convolucion')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.xlim(0, max(t5))
plt.legend()
plt.tight_layout()

plt.subplot(2, 3, 6)
plt.plot(t_yy6, yy6, 'x-', label = 'Salida')
plt.plot(t_x6, x6, 'o-', label = 'Entrada')
plt.title('Salida del pulso rectangular calculada con convolucion')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.xlim(0, max(t_x6))
plt.legend()
plt.tight_layout()

plt.show()

# CALCULO LA POTENCIA
print("\n\nPOTENCIAS DEL EJERCICIO 1 (ITEM b)\n")

# Calculo la potenacia
p1 = ts2.calcular_potencia(yy1)
print("Potencia de la salida generada por la señal fa: ", p1)

p2 = ts2.calcular_potencia(yy2)
print("Potencia de la salida generada por la señal fb: ", p2)

p3 = ts2.calcular_potencia(yy3)
print("Potencia de la salida generada por la señal fc: ", p3)

p4 = ts2.calcular_potencia(yy4)
print("Potencia de la salida generada por la señal fd: ", p4)

p5 = ts2.calcular_potencia(yy5)
print("Potencia de la salida generada por la señal fe: ", p5)

p6 = ts2.calcular_potencia(yy6)
print("Potencia de la salida generada por la señal ff: ", p6)
# %% ------------------------------- EJERCICIO 2 -------------------------------
"""
2) Hallar la respuesta al impulso y la salida correspondiente a una señal de entrada senoidal en los sistemas definidos mediante las siguientes ecuaciones en diferencias:
    - y[n] = x[n] + 3 * x[n - 10]
    - y[n] = x[n] + 3 * y[n - 10]
"""

# Defino los parametros del ejercicio
# Voy a usar la misma funcion seno definida en el ejercicio anterior (x1)

# Coeficientes de las ecuaciones en diferencias dadas
# Ecuacion 1
b1 = [1,0,0,0,0,0,0,0,0,0,3] # Coeficientes de entrada x[n]
a1 = [1.0]
#Ecuacion 2
b2 = [1.0] # Coeficientes de entrada x[n]
a2 = [1,0,0,0,0,0,0,0,0,0,-3] # Coeficientes de salida y[n]

# Calculo la respuesta al impulso

# Ecuacion 1
h1 = ts2.respuesta_impulso(a1, b1)

# Ecuacion 2
h2 = ts2.respuesta_impulso(a2, b2)

# Respuesta al impulso de ambos sistemas
plt.figure(figsize=(20,20))

# Ecuación 1
plt.subplot(1, 2, 1)
plt.plot(h1, 'o-')
plt.title("Respuesta al impulso - Ecuación 1")
plt.xlabel("n")
plt.ylabel("h1[n]")

# Ecuación 2
plt.subplot(1, 2, 2)
plt.plot(h2, 'o-')  # muestro primeras 100 muestras
plt.title("Respuesta al impulso - Ecuación 2")
plt.xlabel("n")
plt.ylabel("h2[n]")

plt.tight_layout()
plt.show()

# Llamo a mis funciones
# Para la ecuacion 1
y1 = np.convolve(x1, h1)

# Para la ecuacion 2
y2 = np.convolve(x1, h2)

# Vector de tiempo para convolución (mismo fs, pero puede tener más muestras)
t_conv1 = np.arange(len(y1)) / fs
t_conv2 = np.arange(len(y2)) / fs

# Grafico las soluciones
plt.figure()

# Ecuacion 1
plt.subplot(1, 2, 1)
plt.plot(t_conv1, y1, 'x-', label = 'Salida')
plt.plot(t1, x1, 'o-', label = 'Entrada')
plt.title('Salida de la primera ecuacion calculada a traves de h[n]')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.xlim(0, max(t1))
plt.legend()
plt.tight_layout()

# Ecuacion 2
plt.subplot(1, 2, 2)
plt.plot(t_conv2, y2, 'x-', label = 'Salida')
plt.plot(t1, x1, 'o-', label = 'Entrada')
plt.title('Salida de la segunda ecuacion calculada a traves de h[n]')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.xlim(0, max(t1))
plt.legend()
plt.tight_layout()

plt.show()

# CALCULO LA POTENCIA
print("\n\nPOTENCIAS DEL EJERCICIO 2\n")

# Calculo la potenacia
p1 = ts2.calcular_potencia(y1)
print("Potencia de la salida generada por la señal fa: ", p1)

p2 = ts2.calcular_potencia(y2)
print("Potencia de la salida generada por la señal fb: ", p2)

# %% ----------------------------- EJERCICIO BONUS -----------------------------
""" 
3) Discretizar la siguiente ecuacion diferencial 
   correspondiente al modelo de Windkessel que describe la dinamica presion-flujo del sistema sanguineo
       C * dP/dt + 1/R * P = Q
  Considere valores tipicos de Compliance y Resistencia vasuclar.
  
"""
