'''
Tarea 4: Modulacion BSPK
'''

#Importamos los paquetes necesarios
import pandas as pd
import numpy as np
from scipy import stats
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt 
plt.style.use('ggplot')

#Se extraen los datos de el archivo csv y se guardan en 'bits'
datos = pd.read_csv('bits10k.csv', header = None) 
datos.columns = ['bits']
bits = datos ['bits']


# Parte 1: Crear un esquema de modulación BPSK para los bits presentados. 
# esto implica asignar una forma de onda sinusoidal normalizada (amplitud 
# unitaria) para cada bit y luego una concatenación de todas estas formas
# de onda.

N = 10000 #Numero de bits
f = 5000 #Frecuencia, en Hz
T = 1/f #Duracion del periodo de cada símbolo, y por lo tanto el de la onda
p_m = 50 #Cantidad de puntos de muestreo
t_p = np.linspace(0, T, p_m) #Puntos de muestreo en el tiempo 

#Se crea la forma de onda de la portadora, que sería una sinusoidal
seno = np.sin(2*np.pi*f*t_p) 

#Y la graficamos
t_pg = t_p*1000 #Multiplicamos cada punto del eje del tiempo para que se vea mejor en la gráfica
plt.figure(0)
plt.title('Señal portadora \n') 
plt.xlabel('Tiempo [ms]') 
plt.ylabel('Seno')
plt.plot(t_pg, seno)
plt.show() 

#Definimos la frecuencia de muestreo y los puntos en el tiempo para la totalidad de la señal 
f_m = p_m/T #Frecuencia de muestreo
t_total = np.linspace(0, N*T, N*p_m) #Cada punto en el tiempo para cada uno de los bits

#Inicializamos las señales, moduladora y modulada, con ceros 
s_moduladora = np.zeros(N*p_m) #Señal moduladora, muestra cada uno de los bits que se tienen 
s_modulada = np.zeros(N*p_m) #Señal modulada, muestra la senal después de la modulación


#Creamos la señal moduladora, que ilustra los bits, con su amplitud de 1 0 0, según corresponda
for i, j in enumerate(bits):
    if j == 1:
        s_moduladora [i*p_m:(i+1)*p_m] = 1
        
    if j == 0:
        s_moduladora [i*p_m:(i+1)*p_m] = 0
        
#Visualizamos los 7 primeros bits de la señal moduladora
pb = 7
plt.figure(1)
plt.title('Señal moduladora \n') 
plt.xlabel('Periodo [en cantidad de puntos]') 
plt.ylabel('Amplitud')
plt.plot(s_moduladora[0:pb*p_m])
plt.show()        

#Creamos la señal modulada, cuando se tiene un bit de 1, se muestra la señal sinusoidal, y cuando hay un bit de 0, la señal siusoidal invertida 
for i, j in enumerate(bits):
    if j == 1:
        s_modulada [i*p_m:(i+1)*p_m] = seno
        
    if j == 0:
        s_modulada [i*p_m:(i+1)*p_m] = -seno
        
#Visualizamos los 7 primeros bits de la señal modulada 
pb = 7
plt.figure(2)
plt.title('Señal modulada \n') 
plt.xlabel('Periodo [en cantidad de puntos]') 
plt.ylabel('Amplitud')
plt.plot(s_modulada[0:pb*p_m])
plt.show() 

#Graficamos las señales modulada y moduladora juntas 
plt.subplot(2, 1, 1)
plt.title('Señal moduladora') 
plt.xlabel('Periodo [en cantidad de puntos]') 
plt.ylabel('Amplitud')
plt.plot(s_moduladora[0:pb*p_m])
plt.subplot(2, 1, 2)
plt.title('Señal modulada \n') 
plt.xlabel('Periodo [en cantidad de puntos]') 
plt.ylabel('Amplitud')
plt.plot(s_modulada[0:pb*p_m])
plt.tight_layout()
plt.show()

#---------------------------------------------------------------------------------------------------------------------------------------

# Parte 2: Calcular la potencia promedio de la señal modulada generada.

#La potencia promedio se calcula como de P = 1/2T * integral(x^2) dt 
#Si no integramos vamos a tener la potencia instantánea, o sea en cada punto, y x en este caso sería cada punto de la señal modulada
P_s = (s_modulada)**2 #Potencia instantanea 

#Ahora integramos la potencia instantánea para obtener la potencia promedio
Pprom = integrate.trapz(P_s, t_total) / (N*T) #Potencia promedio

print("La potencia promedio de la señal modulada generada es de ",Pprom, "W \n")

#-------------------------------------------------------------------------------------------------------------------------------------

# Parte 3: Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco 
# gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.

SNR = [-2, -1, 0, 1, 2, 3]
BER = np.zeros(6) 

#A partir de este punto se abre un for, que se utiliza para las partes 3, 4 y 5, ya que tenemos un SNR de 6 valores, por lo que la señal modulada tiene 6 fuentes de ruido blanco

for i in range(0, 6):
    
#Se calcula la potencia del ruido, van a haber varias, al haber más de un SNR
    P_n = P_s / (10**(SNR[i] / 10))
    
#Se calcula el sigma de la señal ruidosa, a partir de su potencia
    std = np.sqrt(P_n)

#Se crea el ruido blanco gaussiano, utilizando el sigma calculado, y el tamaño de la señal modulada
    noise = np.random.normal(0, std, s_modulada.shape)
    
#Se calcula la señal ruidosa, sumando la señal modulada y el ruido creado
    s_noisy = s_modulada + noise

#Se grafica la señal ruidosa, se muestran los primero 7 bits
    plt.figure(2)
    plt.title('Señal modulada con ruido blanco \n') 
    plt.xlabel('Periodo [en cantidad de puntos]') 
    plt.ylabel('Amplitud')
    plt.plot(s_noisy[0:pb*p_m])

#------------------------------------------------------------------------------------------------------------------------------------
    
#   Parte 4: Graficar la densidad espectral de potencia de la señal con el método
#   de Welch (SciPy), antes y después del canal ruidoso.    
    
#Se calcula con ayuda de la función signal.welch, se calcula primero la densidad espectral de potencia antes del canal ruidoso, con la señal modulada
    fw, PSD = signal.welch(s_modulada, f_m, nperseg=1024)
    plt.figure(3)
    plt.semilogy(fw, PSD)
    plt.title('Densidad espectral de potencia de \n la señal (Método de Welch) antes del canal ruidoso \n') 
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Densidad espectral de potencia [V**2/Hz]')

#Luego, se calcula la densidad espectral del potencia después del canal ruidoso, con la señal con ruido blanco
    fw, PSD = signal.welch(s_noisy, f_m, nperseg=1024)
    plt.figure(4)
    plt.semilogy(fw, PSD)
    plt.title('Densidad espectral de potencia \n de la señal (Método de Welch) antes del canal ruidoso \n') 
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Densidad espectral de potencia [V**2/Hz]')

#-----------------------------------------------------------------------------------------------------------------------------------

#Parte 5: Demodular y decodificar la señal y hacer un conteo de la tasa 
#de error de bits (BER, bit error rate) para cada nivel SNR. 

#Se inicializa el vector de los bits recibidos, con el mismo tamaño del vector de bits que queríamos transmitir
    bits_r = np.zeros(bits.shape) #Bits recibidos
    
#Se calcula la 'pseudo-energía' de la señal original
    Es = np.sum(seno**2) #Pseudoenergia de la señal original

#Se calcula la energía de la señal ruidosa, y se utiliza para saber si los bits recibidos de la señal ruidosa son 1 o 0
    for k, b in enumerate(bits):
        Ep = np.sum(s_noisy[k*p_m:(k+1)*p_m] * seno)
        
#Se establece un umbral de la mitad de la señal original, si es mayor, corresponde a un 1, y si es menor a un 0
        if Ep > Es*0.5:
            bits_r[k] = 1
        else:
            bits_r[k] = 0  

#Se calculan la cantidad de errores que hubieron en la detección de bits
    err = np.sum(np.abs(bits - bits_r))

#Y se calcula el BER (bit error rate) 
    BER[i] = err / N
    print('Cuando SNR es', SNR [i], 'la cantidad de errores es de', err, 'por lo que BER corresponde a:', BER[i])

#-----------------------------------------------------------------------------------------------------------------------------------

# Parte 6: Graficar SSNR vs BER
plt.figure(6)
plt.title('SSNR vs BER') 
plt.xlabel('SNR') 
plt.ylabel('BER')
plt.plot(SNR, BER)
plt.show() 
