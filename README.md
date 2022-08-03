# PROYECTO-CAPSTONE-Prototipo-IoT-para-Valoración-Vascular Bilateral Multiestado
Con el avance de la edad es común que una persona acompañe su vida con diferentes factores de riesgo cardiovascular, como pueden ser el tabaquismo, sedentarismo, estrés, diabetes, entre otros. Estos factores de riesgo, por lo general, generan cambios fisiológicos en el aparato circulatorio de una persona, los cuales incluyen la disminución de la distensibilidad de la arteria aorta, la pérdida progresiva de la fuerza del músculo cardíaco, la disminución de la frecuencia cardíaca máxima, el incremento de la presión arterial sistólica, la disminución del gasto cardíaco y la reducción de las fibras musculares cardíacas. En la actualidad no hay un procedimiento que permita retardar la progresión del envejecimiento cardiovascular, por lo tanto, la población se conforma con recurrir al ejercicio y probablemente a la toma de algunos fármacos. Hoy en día se realiza investigación dirigida a la predicción del riesgo cardiovascular usando diferentes metodologías subclínicas. La valoración vascular es un mecanismo que tiene el objetivo de obtener diferentes parámetros o métricas que brinden información complementaria acerca de la estructura y funciones endoteliales de las arterias. En resumen, valorar el estado de la estructura y la función arterial posibilita a determinar, en sujetos sin enfermedad cardiovascular manifiesta, el riesgo de desarrollarla, la presencia de una enfermedad vascular, la severidad y extensión, y el riesgo de presentar complicaciones.

El objetivo de este proyecto es desarrollar un prototipo para hacer valoración vascular a partir de 3 métricas o índices de valoración, el índice de rígidez arterial (IRA), frecuencia cardíaca (FC) y la velocidad de onda de pulso (VOP). Para obtener estas 3 métricas se utilizan 2 sensores para pulso oximetría (los cuales se utilizan para obtener la señal fotopletismográfica) los cuales son colocados en 2 de las extremidades del paciente y además, se utilizan 3 electrodos para obtener la señal de electrocardiografía los cuales se pueden colocar en el pecho de la persona.

El sistema embebido para registro de las señales fisiológicas está basado en la plataforma de desarrollo Open BCI (Open source Brain-Computer Interfaces). Este sistema embebido es básicamente un sistema de adquisición de datos basado en el Cyton Biosensing Board el cual tiene 8 canales para hacer registros de la actividad eléctrica neuronal ECG/EEG/EMG y otras variables fisiológicas como la onda de volumen de pulso (señal Fotopletismográfica). Este dispositivo tiene la capacidad de comunicarse inalámbricamente con la computadora mediante comunicación Bluetooth 4.0 y Wifi (utilizando el módulo Wifi Shield). El cerebro de este sistema es un procesador de 32 bits el cual responde a comandos AT por vía comunicación serial y su frecuencia de muestreo de trabajo es de 250Hz. Los entornos de trabajo sobre el cual opera este sistema son Windows 7 o superior y Linux.

Por otra parte, el sistema embebido para procesamiento de las señales y obtención de las métricas vasculares está basado en la plataforma Raspberry Pi 3. Como fortaleza adicional, esta plataforma permitirá que se tenga conectividad vía internet y la gestión de bases de datos para la consulta y el almacenamiento de las métricas de valoración vascular del paciente. La idea principal es que vía internet el médico pueda hacer la valoración del paciente sin necesidad de que éste se desplace a un centro de salud. Además, el médico podrá consultar el histórico de las métricas del paciente en todo momento, pedirle al paciente que haga una nueva adquisición de las señales y finalmente, comparar resultados del histórico del paciente con datos almacenados en otros centros de salud.  

# INTEGRANTES:
Dr. Alain Manzo Martínez 

Ing. Jesús Manuel Muñoz Larguero

Ing. Oscar Beltrán Gómez

# MATERIAL
## Raspberry Pi 3
Imagen 1
<img src="https://user-images.githubusercontent.com/95665770/182489391-2ee927f3-27df-4f56-a381-23f5c9e4ce86.png" width="480" height="400">
## Cyton Biosensing Board
Imagen 2
<img src="https://user-images.githubusercontent.com/95665770/182492633-d595c1f7-4e3e-43d4-8337-10b2f2d65ec3.png" width="480" height="400">
## 3 Gold Cup Electrodes
Imagen 3
![image](https://user-images.githubusercontent.com/95665770/182493294-54a5fe42-15ef-4f93-87cc-63472f314919.png)
## 2 Pulse Sensors
Imagen 4
![image](https://user-images.githubusercontent.com/95665770/182493512-ed8fd25a-f396-49d0-90db-a2b360b9575b.png)
## Conductive Paste Ten20
Imagen 5
<img src="https://user-images.githubusercontent.com/95665770/182493926-c37eeeed-1aa0-478f-af85-e98a192564a0.png" width="280" height="320">

# Conexión de Sensores y Comunicación
## Cyton Biosensing Board
El sistema embebido para registro de las señales fisiológicas está basado en la plataforma de desarrollo Open BCI (Open source Brain-Computer Interfaces). Este sistema embebido es básicamente un sistema de adquisición de datos basado en el Cyton Biosensing Board el cual tiene 8 canales para hacer registros de la actividad eléctrica neuronal ECG/EEG/EMG y otras variables fisiológicas como la onda de volumen de pulso (señal Fotopletismográfica). Este dispositivo tiene la capacidad de comunicarse inalámbricamente con la computadora mediante comunicación Bluetooth 4.0 y Wifi (utilizando el módulo Wifi Shield). El cerebro de este sistema es un procesador de 32 bits el cual responde a comandos AT por vía comunicación serial y su frecuencia de muestreo de trabajo es de 250Hz. Los entornos de trabajo sobre el cual opera este sistema son Windows 7 o superior y Linux.

## Raspberry Pi 3 B+
El sistema embebido para recibir las señales y procesarlas, es la Raspberry Pi 3 B+, que cuenta con un GPIO de 40 pines, el cual permite el contacto con el mundo exterior, tanto por sensores como con actuadores,  el GPIO de Raspberry trabaja con un nivel de 3.3V, cuenta con puertos de comunicación I2C, SPI y UART. Además la Raspberry Pi 3B+ cuenta con conexiones tradicionales como son puertos USB, conector de red ethernet, Jack de 3.5mm, puerto HDMI, puerto para memoria microSD y un conector micro-usb para la alimentación. Tambien podemos destacar los puertos especiales para la cámara y la pantalla.

## ¿Como empezar?
Para comenzar con la lectura de las señales fisiológicas, tenemos primeramente que realizar las conexiones de los sensores que utilizaremos para las mediciones, en este caso utilizaremos dos sensores de medición de pulso cardiaco y electrodos. Los sensores deben de ir conectados de la siguiente manera:

### Conexion de los electrodos
Conectar los dos pines de señal de los electrodos, uno en el pin superior y otro en el pin inferior del puerto denominado NP1.

Conectar el tercer cable al pin inferior del puerto denominado BIAS.

<img src="https://user-images.githubusercontent.com/95665770/182494870-6eeb022e-3bd4-4ab9-98d1-e4781e61a514.png" width="280" height="320">

### Conexion de los sensores de medición pulso.
Luego de haber conectado los electrodos a nuestro sistema lo siguiente de conectar serán los sensores de pulso, cada sensor cuenta con tres pines, un pin para el voltaje, uno para la tierra y el pin que envía señal a la tablilla (señal analógica).

<img src="https://user-images.githubusercontent.com/95665770/182495121-aebf74bb-fff8-4847-8d65-f08fc3b74484.png" width="420" height="320">

### Conexion Para la Lectura y Envio de Datos
Una vez conectados los sensores a nuestra placa, lo siguiente será establecer la comunicación entre nuestra Raspberry y la tablilla CYTON, esto se logrará mediante nuestro OpenBCI Dongle, este dongle funciona mediante una señal de radiofrecuencia con la cual se comunica con la tablilla Cyton.

Para realizar el enlace de comunicación el dongle debe estar conectado a uno de los puertos USB de la Raspberry y este automáticamente detectara el dongle sin la necesidad de instalar Drivers adicionales.

<img src="https://user-images.githubusercontent.com/95665770/182495717-2713cd69-e8ac-4f3b-98d4-90017aeaf66f.png" width="280" height="320">

### Caracteristicas y datos Tecnicos del Hardware

#### Raspberry Pi 3B+ especificaciones tecnicas.

CPU + GPU: Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz
RAM: 1GB LPDDR2 SDRAM
Wi-Fi + Bluetooth: 2.4GHz y 5GHz IEEE 802.11.b/g/n/ac, Bluetooth 4.2, BLE
Ethernet: Gigabit Ethernet sobre USB 2.0 (300 Mbps)
GPIO de 40 pines
HDMI
4 puertos USB 2.0
Puerto CSI para conectar una cámara.
Puerto DSI para conectar una pantalla táctil
Salida de audio estéreo y vídeo compuesto
Micro-SD
Power-over-Ethernet (PoE)
Cyton Board especificaciones tecnicas.

#### OpenBCI 32bit Board:

    •    8 differential, high gain, low noise input channels
    •    Compatible with active and passive electrodes
    •    Texas Instruments ADS1299 ADC (link to datasheet)
    •    PIC32MX250F128B microcontroller w/chipKIT™ bootloader (50MHz)
    •    RFduino™ Low Power Bluetooth™ radio (Link to datasheet)
    •    24-bit channel data resolution 
    •    Programmable gain: 1, 2, 4, 6, 8, 12, 24
    •    3.3V digital operating voltage
    •    +/-2.5V analog operating voltage
    •    ~3.3-12V input voltage
    •    LIS3DH accelerometer (link to datasheet)
    •    Micro SD card slot
    •    5 GPIO pins, 3 of which can be Analog



#### OpenBCI Dongle especificaciones tecnicas.

    •    RFD22301 radio module from RFdigital™
    •    FT231X USB-to-serial converter from FTDI
    •    Can upload code to the OpenBCI board or the dongle
    •    Fully broken out and pin-compatible w/ RFduino form factor  

## Conexión al cuerpo para realizar mediciones
### Conexion de los Electrodos y Sensores para Monitoreo
Lo siguiente a realizar, será colocar los electrodos y sensores de pulso, al cuerpo de la persona o paciente a la que se le desee realizar el monitoreo, la manera de colocar estos sensores es la siguiente:

Conecte el electrodo que corresponde a la tierra (GND) a la parte central ósea del pecho llamada esternón.
Los electrodos restantes se colocarán en puntos opuestos del pecho, uno en el lado izquierdo y otro en el lado derecho, recuerde que estos dos electrodos son los que previamente se conectaron en el puerto NP1 de la tablilla CYTON.

Coloque uno de los dos sensores de medición de pulso en el dedo índice de la mano izquierda, el otro puede ir, ya sea, en el dedo índice de la mano derecha o incluso en el dedo pulgar ambos pies.

A continuacion se muestran los lugares aproximados en donde deben de ir los electrodos y sensores:

<img src="https://user-images.githubusercontent.com/95665770/182496697-ec9b1431-c4c4-4773-8c05-b541b1eb55da.png" width="480" height="420">

## Ejecución del Código en la Raspberry
Para ejecutar el código en la Raspberry primero hay que instalar las siguientes librerías

sudo apt-get install Python3-serial

pip3 install matplotlib

pip3 install numpy

sudo apt install python3-pandas

sudo apt install -y python3-scipy

Una vez instalado las librerías ejecute el código tal como se muestra en la siguiente figura

![WhatsApp Image 2022-07-27 at 10 51 49 AM](https://user-images.githubusercontent.com/95665770/182500038-ef05d493-681e-4da6-80d6-533862744d99.jpeg)

