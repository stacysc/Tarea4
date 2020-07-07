# Tarea 4
Procesos aleatorios 

## Descripción: 
En el archivo bits10k.csv se encuentran 10.000 bits (actualizado) generados a partir de una fuente binaria equiprobable. El objetivo es hacer una modulación digital para "transmitir" estos datos por un canal ruidoso. La modulación se hace con una frecuencia en la portadora de f = 5000 Hz y con un período de símbolo igual a un período completo de la onda portadora.

### Resultados
> Parte 1: Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

La modulación BPSK o "Binary Phase Shift Keying", es la modulación por desplazamiento de fase que emplea dos símbolos, con un bit de información cada uno. Esta modulación consiste en enviar una onda sinusoidal, cuando el bit es uno, y enviar una señal sinusoidal inversa, cuando el bit es cero. 

Para resolver esta parte, primero se extrajeron los datos del archivo csv, con ayuda de `pandas`. Además se definieron varias variables, como la frecuencia, periodo, puntos de muestreo, el valor escogido fue de 50, porque con esa cantidad la señal sinusoidal se grafica de buena forma, y además, al haber 10000 bits, si se escogía un valor muy grande el programa podría durar demasiado. 
En este caso, la señal portadora es de tipo sinusoidal, por lo que se creó esta forma de onda con ayuda de `numpy`, con una frecuencia de <img src="https://latex.codecogs.com/gif.latex?f&space;=&space;5000&space;Hz" title="f = 5000 Hz" />. Esta se muestra en la siguiente figura:

<p align="center">
  <img src="https://github.com/stacysc/Tarea4/blob/master/Se%C3%B1al_portadora.png">
</p> 
<p align="center">Señal portadora.<p align="center">

Después de esto se definieron la frecuencia de muestreo y los puntos en el tiempo para la totalidad de la señal, se definió que cada periodo iba a tener cincuenta puntos, que es el muestreo que se definió anteriormente. Además se graficó la señal moduladora, que es la que muestra los bits, con una amplitud de uno, si el bit es uno, y de cero si el bit es cero. Esta señal, de los primeros siete bits, se muestra en la siguiete figura:

<p align="center">
  <img src="https://github.com/stacysc/Tarea4/blob/master/Se%C3%B1al_moduladora.png">
</p> 
<p align="center">Señal moduladora.<p align="center">

Finalmente, se creó la señal modulada BPSK, y por medio de un `for` se recorrieron todos los bits, y con ayuda de un `if`, se definió que si el bit es de uno, la onda durante ese periodo es igual a seno, y si el bit es de cero, la onda en ese periodo es igual a -seno. La siguiente gráfica muestra la onda modulada de los siete primeros bits:

<p align="center">
  <img src="https://github.com/stacysc/Tarea4/blob/master/Se%C3%B1al_modulada.png">
</p> 
<p align="center">Señal modulada<p align="center">

Adicionalmente, se graficaron la señal moduladora y la modulada para poder observar mejor los efectos de la modulación BPSK:

<p align="center">
  <img src="https://github.com/stacysc/Tarea4/blob/master/comparacion_se%C3%B1ales.png">
</p>
<p align="center">Comparación entre las señales moduladora y modulada<p align="center">
 
Como se puede observar, el primer bit es de cero, por lo que la señal modulada empieza con -seno, los siguientes bits son 1, 0, 1, 0, por lo que la señal varía entre seno y -seno, y los bits 6 y 7 corresponden a 1, por lo que la señal es seno durante dos periodos seguidos. En la siguiente tabla se resume el comportamiento obtenido de los primeros siete bits:

| Número de bit  | Valor | Señal modulada | 
|     :----:     |:----: |    :----:      |
|       0        |   0   |    -seno       |
|       1        |   1   |     seno       |
|       2        |   0   |    -seno       |
|       3        |   1   |     seno       |
|       4        |   0   |    -seno       |
|       5        |   1   |     seno       |
|       6        |   1   |     seno       |

***

> Parte 2: Calcular la potencia promedio de la señal modulada generada.

La potencia promedio de un proceso estocástico se calcula como:

<p align="center">
 <img src="https://latex.codecogs.com/gif.latex?\frac{1}{2T}\int_{-T}^{T}x^{2}(t)dt&space;=&space;\frac{1}{2T}\int_{-T}^{T}E\left[X^{2}(t)\right]dt&space;=&space;A\left\{E\left[X^{2}(t)\right]\right\}" title="\frac{1}{2T}\int_{-T}^{T}x^{2}(t)dt = \frac{1}{2T}\int_{-T}^{T}E\left[X^{2}(t)\right]dt = A\left\{E\left[X^{2}(t)\right]\right\}" />
</p> 

Entonces, primero se calculó la potencia instantánea, que corresponde a cada punto de la señal modulada al cuadrado, y luego se calculó la potencia promedio con la ayuda de la función `integrate.trapz`, que calcula una integral utilizando la regla del trapecio. Resultó una potencia promedio de:

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P(T)&space;=&space;0.49&space;\&space;W" title="P(T) = 0.49 \ W" />
</p>

***

> Parte 3: Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.

Para crear el canal ruidoso es necesario conocer su potencia, la cual podemos calcula por medio de la relación señal a ruido, que tiene la fórmula:

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?SNR_{dB}&space;=&space;10\log_{10}\left(\frac{P_S}{P_N}\right&space;)" title="SNR_{dB} = 10\log_{10}\left(\frac{P_S}{P_N}\right )" />
</p>

Entonces, la potencia del ruido es:

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?P_N&space;=&space;\frac{P_S}{10^{\left(\frac{SNR_{dB}}{10}\right)}}" title="P_N = \frac{P_S}{10^{\left(\frac{SNR_{dB}}{10}\right)}}" />
</p>

En este caso la relación señal a ruido corresponde al intervalo:

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?SNR&space;=&space;[-2,&space;-1,&space;0,&space;1,&space;2,&space;3]" title="SNR = [-2, -1, 0, 1, 2, 3]" />
</p>

Seguidamente se calculó el sigma de la señal ruidosa por medio de la raíz cuadrada de su potencia, y para crear el ruido se utilizó la función `random.normal`, que crea muestras aleatorias de una distribución gaussiana, con el sigma anteriormente calculado y del tamaño de la señal modulada. Finalmente se creó la señal ruidosa por medio de la suma de la señal modulada más el ruido creado. Como la relación señal a ruido tiene varios valores, entonces se crean diferentes señales ruidosas, dependiendo del valor de SNR, por lo que se utilizó un `for`, para recorrer cada valor del SNR, dentro de este for se desarrollan esta parte, además de las partes 4 y 5, ya que también dependen del valor de la señal con ruido que se haya generado según el valor del SNR. La gráfica de la señal modulada ruidosa, con todos los canales ruidosos sobrepuestos corresponde a:

<p align="center">
  <img src="https://github.com/stacysc/Tarea4/blob/master/Se%C3%B1al_modulada_ruidosa.png">
</p> 
<p align="center">Señal modulada ruidosa<p align="center">

***

> Parte 4: Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.

Para calcular la densidad espectral de potencia de la señal tanto antes como después del canal ruidoso se utilizó la función `signal.welch`, que precisamente calcula la densidad espectral de potencia por medio del método de Welch, el cual realiza una estimación de la densidad dividiendo los datos en segmentos superpuestos, calcula un periodograma modificado para cada segmento y promedia los periodogramas. 

La gráfica de la densidad espectral de la señal antes del canal ruidoso corresponde a: 

<p align="center">
  <img src="https://github.com/stacysc/Tarea4/blob/master/Densidad_espectral_antes.png">
</p> 
<p align="center">Densidad espectral de potencia de la señal antes del canal ruidoso<p align="center">

Y como se tienen varias señales ruidosas, entonces se tienen varias densidades espectrales después del canal ruidoso, por lo que la gráfica con la superposición de las mismas es:

<p align="center">
  <img src="https://github.com/stacysc/Tarea4/blob/master/Densidad_espectral_despues.png">
</p> 
<p align="center">Densidad espectral de potencia de la señal después del canal ruidoso<p align="center">

***

> Parte 5: Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.

Para resolver esta parte, primero se calculó la pseudo-energía de la señal modulada sin ruido, llamada así porque se calculó por medio de una sumatoria en lugar de una integral, y luego se realizó la decodificación por medio del cálculo de la energía de la señal ruidosa, la cual se calculó como la sumatoria de cada periodo de la señal multiplicado por la función seno, este método es utilizado para mejorar la detección de los bits y tener una tasa de error menor, por medio de la aproximación de la señal ruidosa por medio de la original y se deriva del producto interno entre dos señales, el cual se calcula por medio de:

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?\left\langle&space;s(t),&space;r(t)&space;\right\rangle&space;=&space;\int_{0}^{T}s(t)r(t)dt" title="\left\langle s(t), r(t) \right\rangle = \int_{0}^{T}s(t)r(t)dt" />
</p> 

Seguidamente se recorrieron todos los periodos de la energía de la señal ruidosa calculados y se compararon con los de la energía de la señal original, si la energía de la señal ruidosa es menor a la energía de la señal original, el bit corresponde a un cero, y si es mayor a un uno. Además se calculó la cantidad de errores obtenidos por medio del calculo del valor absoluto de la resta entre cada uno de los bits originales y los decodificados de la señal ruidosa. Con la cantidad de errores calculados se pudo calcula el BER o  el bit error rate, por medio de la división de la cantidad de errores entre el número total de bits. Para esta parte también se tienen varios resultados de BER, al tener distintos niveles de SNR. Los resultados del BER, de una de las simulaciones (porque al ruido crearse de manera aleatoria estos valores siempre cambian) se resumen en la tabla siguiente:

| Nivel de SNR   | Cantidad de errores |  BER | 
|     :----:     |       :----:        |:----:|
|      -2        |        77           |0.0077|
|      -1        |        33           |0.0033|
|       0        |        7            | 0.007|
|       1        |        6            | 0.006|
|       2        |        1            | 0.001|
|       3        |        1            | 0.001|

***

> Parte 6: Graficar BER versus SNR.

La gráfica de BER vs SNR se muestra en la siguiente figura:

<p align="center">
  <img src="https://github.com/stacysc/Tarea4/blob/master/Densidad_espectral_despues.png">
</p> 
<p align="center">BER vs SNR<p align="center">


