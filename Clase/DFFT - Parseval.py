import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft

# %% """ DFFT --> Transformada rapida de Fourier """
# %% DEFINICION DE MI FUNCIONES
def mi_funcion_sen(frecuencia, nn, amplitud = 1, offset = 0, fase = 0, fs = 2): # Si lo igualo a algo es opcional, entonces si no le paso nada el programa me lo hace cero
     # Los obligatorios van al principio del parentesis y los opcionales al final    

    Ts = 1/fs # Es el tiempo en el cual se toma cada muestra

    tt = np.arange(start = 0, stop= N*Ts, step = Ts)

    xx = amplitud * np.sin(2 * np.pi * frecuencia * tt + fase) + offset

    return tt, xx

# %% DEFINO MIS VARIABLES
# Resolucion espectral unitaria --> N = fs
N = 1000
fs = N
df = fs/N # Resolucion temporal 
# --> la frecuencia siempre se mide en Hz, pero por como lo pongo me lo va a calcular en N° muestras 
# --> entonces para que N/4 este en Hz, lo multiplico por el df
ts = 1/fs # Tiempo de sampling, muestreo

# %% CALCULOS
# Las x en minuscula es porque estan en el espectro del tiempo
t1,x1 = mi_funcion_sen(frecuencia = N/4 * df, nn = N, fs = fs)
t2,x2 = mi_funcion_sen(frecuencia = ((N/4) + 0.5) * df, nn = N, fs = fs)
t3,x3 = mi_funcion_sen(frecuencia = ((N/4) + 1) * df, nn = N, fs = fs)

# CALCULO LA DFFT
# Las X en mayuscula son en el espectro de frecuencias, transformadas
X1 = fft(x1)
X2 = fft(x2)
X3 = fft(x3)

# La respuesta de la fft es una secuencia de numeros complejos --> tiene su parte real y su parte imaginaria
# Si le calculo el angulo es la fase de la fft --> le calculo en angulo y el modulo para verlo de manera polar que a nosotros nos sirve mas
modulo_X1 = np.abs(X1)
angulo_X1 = np.angle(X1)

modulo_X2 = np.abs(X2)
angulo_X2 = np.angle(X2)

modulo_X3 = np.abs(X3)
angulo_X3 = np.angle(X3)

# %% GRAFICOS
ff = np.arange(N) * df # Es un arange de N que necesito para graficar
# Es un eje en frecuencias (resolucion espectral), va de 0 a N
# Es mi eje x, y se mide en Hz

plt.figure()  # Tamaño de la figura (ancho, alto)
# plt.clf --> me borra los graficos cuando tengo muchos y los voy cerrando

# Grafico X1
plt.subplot(1,3,1)

plt.title("Modulo de la DFFT con frecuencia = N/4")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|x|')
plt.xlim([0, N/2]) # Una tuppla
# plt.plot(ff, np.log10(modulo_X1) * 20, 'o', label = 'X1 abs en db') # En este caso es un db de tension
plt.plot(ff, modulo_X1, 'o-', label = 'X1 abs')
plt.legend()
 
# Grafico X2
plt.subplot(1,3,2)

plt.title("Modulo de la DFFT con frecuencia = (N/4) + 0.5")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|x|')
plt.xlim([0, N/2]) # Una tuppla
# plt.plot(ff, np.log10(modulo_X2), 'o', label = 'X2 abs')
plt.plot(ff, modulo_X2, 'o-', label = 'X2 abs')
plt.legend()

# Grafico X3
plt.subplot(1,3,3)

plt.title("Modulo de la DFFT con frecuencia = (N/4) + 1")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|x|')
plt.xlim([0, N/2]) # Una tuppla
# plt.plot(ff, np.log10(modulo_X3), 'o', label = 'X3 abs')
plt.plot(ff, modulo_X3, 'o-', label = 'X3 abs')
plt.legend()

plt.show()

# %% GRAFICOS EN db
plt.figure()  # Tamaño de la figura (ancho, alto)
# plt.clf --> me borra los graficos cuando tengo muchos y los voy cerrando

# Grafico X1 en db
# plt.subplot(1,3,1)

plt.title("Modulo de la DFFT")

# plt.title("Modulo de la DFFT con frecuencia = (N/4)")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|x|')
plt.xlim([0, fs/2]) # En este caso fs = N, pero pongo fs para saber que va eso y no va siempre N
plt.plot(ff, np.log10(modulo_X1) * 20, 'o', label = 'X1 abs en db') # En este caso es un db de tension
plt.legend()
 
# Grafico X2
# plt.subplot(1,3,2)

# plt.title("Modulo de la DFFT con frecuencia = (N/4) + 0.5")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|x|')
plt.xlim([0, fs/2]) # Una tuppla
plt.plot(ff, np.log10(modulo_X2) * 20, 'x', label = 'X2 abs en db')
plt.legend()

# Grafico X3
# plt.subplot(1,3,3)

# plt.title("Modulo de la DFFT con frecuencia = (N/4) + 1")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|x|')
plt.xlim([0, fs/2]) # Una tuppla, por eso los corchetes, puede ser tambien entre parentesis 
plt.plot(ff, np.log10(modulo_X3) * 20, '+', label = 'X3 abs en db')
plt.legend()

plt.show()
# %% """ PARSEVAL """
# %% ITEM 1 - Identifico que la varianza de una senoidal es 1
# (sigma^2 = 1)
tt, xx = mi_funcion_sen(frecuencia = (N/4) * df, nn = N, amplitud = np.sqrt(2), fs = fs) # Sinusoidal con varianza unitaria ==> amp = raiz de 2

varianza = np.var(xx)
media = np.mean(xx)
desviacion_estandar = np.std(xx)

print(f"Varianza = {varianza:.5f}")
print(f"Media = {media:.5f}")
print(f"Desviacion estandar = {desviacion_estandar:.5f}")
# %% ITEM 2 - Calcular la densidad espectral de potencia
# (|x|^2 --> si lo pongo en db tengo que hacer lo de 10*log(|x|^2)))
XX = fft(xx)
modulo_XX = np.abs(XX)
potencia_espectral = (modulo_XX) ** 2
 
# Grafico
plt.figure()
plt.title("Densidad espectral de potencia en db")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('|x|')
# plt.xlim([0, fs/2]) # En este caso fs = N, pero pongo fs para saber que va eso y no va siempre N
plt.plot(ff, np.log10(potencia_espectral) * 10, 'o') # En este caso es un db de potencia --> en el log multiplico por 10
# El eje x es el mismo que use antes (ff = np.arange(N) * df)

plt.show()

# %% ITEM 3 - Verificar la identidad de Parseval
# --> integrar todo el espectro, y toda el area de la densidad espectral de potencia tiene que dar 1 (sum |x|^2 = 1)
modulo_xx = np.abs(xx)

energia_tiempo = np.sum(modulo_xx**2) # Es la energia en tiempo
energia_frecuencia = np.sum(modulo_XX**2 * (1/N)) # Es la energia en frecuencias

print(f"Energia en el tiempo = {energia_tiempo:.5f}")
print(f"Energia en frecuencias = {energia_frecuencia:.5f}")

# %% ZERO PADDING
# El zero padding es una forma de interpolar la resolcuion espectral

z = np.zeros(10*N) # Le paddeo 9N para que haya 10 muestras

Ff=np.arange(N)*df # Mi eje x en Hz

x1p = np.concat((x1, z))

X1p = fft(x1p)
X1Pabs = np.abs(X1p)
X1pang = np.angle(X1p)

df = fs / (10 * N) # Resolucion espectral = [[1/(s*muestras)]
FfP=np.arange((10*N))*df # Mi eje x en Hz

plt.figure()
plt.title('Zero Padding')
plt.plot(Ff, 20*np.log10(modulo_X1), label='X N/4 abs en dB')
plt.plot(FfP, 20*np.log10(X1Pabs), label='X N/4 abs en dB con padding')
plt.legend()

plt.show()

# %% OBSERVACIONES
# 1. np.var --> varianza
# 2. np.mean --> media
# 3. np.std --> el desvio estandar, que es la raiz de la varianza 
# 4. np.sum --> sumatoria
# %% TEORIA
# El modulo de x nos interesaba representarlo en db 
# db == desiveles
# MODULO EN db
# |x|db = 20 * log(|x|) --> es una definicion, y es logaitmo en base 10
# |x|^2 == densidad espectral de potencia --> [Watt]/[Hz]
# |x|^2 db = 10 * log(|x|) 
# El 0db representa 1Watt o 1V, dependiendo de que cosa estamos expresando en db --> medidas referenciales
# Si tengo 0db significa que mi medicion vale 1 (log(1) = 0)
# POTENCIA
# 0db ==> 1Watt
# Entonces... 10db ==> 10Wats
#             20db ==> 100Wats
# Estamos conviertiendo una medida que tiende exponencialmente en algo lineal...
# ... entonces si corres en potencia 10db, corres un orden de magnitud
# Si duplico en potencia (si duplico lo que esta adentro del  logaritmo) --> sumo 3db
# En Watts --> si estoy en -20dbWatts tengo 0.01
# TENSION
# Ahi esta el 20
# 10 * log(|x|^2) --> 20 * log(|x|) --> en tension
# 0db ==> 1V
# Entonces... 10db ==> 3,11V
#             20db ==> 10V
#             40db ==> 100V
# Es decir que cada vez que pasamos 20db estamos subiendo un orden de magnitud
# Si sumo 20db, multiplicamos por 10 en veces
# Si resto 20db, dividimos por 10 --> quitamos un orden de magnitud
# Entonces pensar en -40db --> estamos pensando en dos ordenes de magnitud abajo del 0db
# En volts --> si estoy en 1dbVolt tengo 0.01

# RANGO DINAMICO
# Su definicion se hace en db --> es un ratio
# Es un ratio entre el valor mas grande y el valor mas chico que se puede tener en un sistema presentes a la vez
# Un sistema que tiene un rango dinamico elevado significa que va a tener valores muy grandes de medicion al mismo tiempo que valores muy chicos
# Te expresa la variabilidad del rango que se percibe, la cantidad de ordenes de magnitud entre la medicion mas grande y la medicion mas chica
# Para expandir el rango dinamico (que se vea lo mismo pero mas a lo largo, mas claro), hago lo del logaritmo en el eje 
# La funcion logaritmo me 