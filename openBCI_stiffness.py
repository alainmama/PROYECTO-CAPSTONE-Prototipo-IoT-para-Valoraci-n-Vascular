# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:37:54 2022

@author: alain
"""

import serial
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal

#Configura el puerto serial con un baudrate de 115200, settings por default, puerto:COM8  
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM8'
state = ser.open()
#Set all channels to default
ser.write(b'd')
#Cadena de retorno si no hay streaming
data = ser.read(39)
print(data) 
#Llamada a comando y configura analog mode
ser.write(b'///2')
#Cadena de retorno 
data = ser.read(36)
print(data) 
#Despliega configuración de frecuencia de muestreo
ser.write(b'~~')
#Cadena de retorno 
data = ser.read(32)
print(data)
#Consigue frecuencia de muestreo
fs = int(data[24:27])
#print(fs)
#Configuración del canal 1
ser.write(b'x1060110X')
#Cadena de retorno 
data = ser.read(29)
print(data)
#Activa canal 1
ser.write(b'!')

#Inicia streaming de datos
ser.write(b'b')
N_points = 1000
data_PPG_1 = np.zeros(N_points)
data_PPG_2 = np.zeros(N_points)
data_ECG = np.zeros(N_points)
for i in range(0,N_points):
    #Consigue un paquete de datos
    data = ser.read(33)
    #print(data) 
    ############PPG###########
    #Lee localidades donde se encuentra la medición del pulse sensor 1
    byte_H = data[26]
    byte_L = data[27]
    #Concatena bytes
    word = (byte_H << 8) + byte_L
    #print(word)
    #Amacena medición en un arreglo
    data_PPG_1[i] = int(word)
    #Lee localidades donde se encuentra la medición del pulse sensor 2
    byte_H = data[28]
    byte_L = data[29]
    #Concatena bytes
    word = (byte_H << 8) + byte_L
    #print(word)
    #Amacena medición en un arreglo
    data_PPG_2[i] = int(word)
    ######## ECG ###########
    byte_1 = data[2]
    byte_2 = data[3]
    byte_3 = data[4]
    #Concatena datos de medición
    word = (byte_1 << 8) + byte_2
    word = (word << 8) + byte_3
    data_ECG[i] = word

#Gráfica de la señal fotopletismográfica
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(data_PPG_1)
plt.title('SEÑAL FOTOPLETISMOGRÁFICA (EXTREMIDAD IZQUIERDA)')
plt.xlabel('Número de Muestras')
plt.subplot(2,1,2)
plt.plot(data_PPG_2)
plt.title('SEÑAL FOTOPLETISMOGRÁFICA (EXTREMIDAD DERECHA)')
plt.xlabel('Número de Muestras')
#Gráfica de la señal de ECG
plt.figure(3)
plt.subplot(211)
plt.plot(data_ECG[1:])
plt.title("SEÑAL DE ELECTROCARDIOGRAFÍA")
plt.xlabel('Número de Muestras')
#Comando de stop streaming
ser.write(b's')
#Guarda datos en archivo csv    
df = pd.DataFrame(data_PPG_1)
df.to_csv('example_ppg_1.csv')
df = pd.DataFrame(data_PPG_2)
df.to_csv('example_ppg_2.csv')
df = pd.DataFrame(data_ECG[1:])
df.to_csv('example_ecg.csv')
#Cierra puerto UART
ser.close()


#Abre archivos
data_csv = pd.read_csv('example_ppg_1.csv', header=None, skiprows=1)
data_csv_2 = pd.read_csv('example_ppg_2.csv', header=None, skiprows=1)
data_csv_3 = pd.read_csv('example_ecg.csv', header=None, skiprows=1)
#Extrae la señal fotopletismografica
data_val = data_csv.values[:,1]
data_val_2 = data_csv_2.values[:,1]
#Gráfica de la señal
plt.figure(2)
plt.subplot(411)
plt.plot(data_val)
plt.title('SEÑAL FOTOPLETISMOGRÁFICA (CANAL IZQUIERDO)')
plt.subplot(413)
plt.plot(data_val_2)
plt.title('SEÑAL FOTOPLETISMOGRÁFICA (CANAL DERECHO)')
###############################################################################
#                   ANÁLISIS DE LA SEÑAL FOTOPLETISMOGRÁFICA
#Periodo de muestreo
ts = 1/fs
#Tamaño de la señal (-1 para no considerar el último dato de la señal de ECG)
N = len(data_val)-1
#Arreglo para almacenar la derivada
derivative = np.zeros(N-1)
derivative_2 = np.zeros(N-1)
#Derivadas canal 1 y 2
for i in range(1,N):
    derivative[i-1] = (data_val[i] - data_val[i-1])
    derivative_2[i-1] = (data_val_2[i] - data_val_2[i-1])
#Gráfica de la señal
plt.figure(2)
plt.subplot(412)
plt.plot(derivative)
plt.title('PRIMERA DERIVADA DE LA SEÑAL FOTOPLETISMOGRÁFICA PURA Y FILTRADA (CANAL IZQUIERDO)')
plt.subplot(414)
plt.plot(derivative_2)
plt.title('PRIMERA DERIVADA DE LA SEÑAL FOTOPLETISMOGRÁFICA PURA Y FILTRADA (CANAL DERECHO)')
#Filtrado de la señal canal 1 y 2
deriva_filt = np.zeros(N-1)
deriva_filt_2 = np.zeros(N-1)
a = 0.1
y_1 = 0
y_2 = 0
for i in range(0,N-1):
    deriva_filt[i] = a*derivative[i] + (1-a)*y_1
    y_1 = deriva_filt[i]
    deriva_filt_2[i] = a*derivative_2[i] + (1-a)*y_2
    y_2 = deriva_filt_2[i]
    
#Gráfica de la señal
plt.figure(2)
plt.subplot(412)
plt.plot(deriva_filt,'r')
plt.subplot(414)
plt.plot(deriva_filt_2,'r')
plt.xlabel('Número de Muestras')


#Máximos de la señal
maximos = []
maximos_val = []
maximos_2 = []
maximos_val_2 = []
for i in range(0,N-2):
    if deriva_filt[i] >= 0:
        if deriva_filt[i+1] <= 0:
            maximos.append(i)
            maximos_val.append(data_val[i])
            plt.subplot(411)
            plt.plot(i,data_val[i],'.r')
    if deriva_filt_2[i] >= 0:
        if deriva_filt_2[i+1] <= 0:
            maximos_2.append(i)
            maximos_val_2.append(data_val_2[i])
            plt.subplot(413)
            plt.plot(i,data_val_2[i],'.r')
           
#Busqueda de los dos máximos (principal y dicrótico) Canal 1
M = len(maximos)
maxi_dic = []
maxi_max = []
for i in range(1,M-1):
    if maximos_val[i-1] < maximos_val[i] and maximos_val[i] > maximos_val[i+1]:
        maxi_max.append(maximos[i])
        maxi_dic.append(maximos[i+1])
        plt.subplot(411)
        plt.plot(maximos[i],maximos_val[i],'.k')
        plt.plot(maximos[i+1],maximos_val[i+1],'.k')
#Busqueda de los dos máximos (principal y dicrótico) Canal 2
M = len(maximos_2)
maxi_dic_2 = []
maxi_max_2 = []
for i in range(1,M-1):
    if maximos_val_2[i-1] < maximos_val_2[i] and maximos_val_2[i] > maximos_val_2[i+1]:
        maxi_max_2.append(maximos_2[i])
        maxi_dic_2.append(maximos_2[i+1])
        plt.subplot(413)
        plt.plot(maximos_2[i],maximos_val_2[i],'.k')
        plt.plot(maximos_2[i+1],maximos_val_2[i+1],'.k')


#Obtiene diferencia de tiempo entre máximo principal y dicrótico canal 1
diff_time = maxi_dic[0]*ts - maxi_max[0]*ts
print("Output: Tiempo entre máximo principal y máximo de nodo dicrótico, Canal Izquierdo: ", diff_time,"seg.")
#Obtiene diferencia de tiempo entre máximo principal y dicrótico canal 2
diff_time_2 = maxi_dic_2[0]*ts - maxi_max_2[0]*ts
print("Output: Tiempo entre máximo principal y máximo de nodo dicrótico, Canal Derecho: ", diff_time_2,"seg.")
#Se establece la altura del sujeto o paciente
altura = 1.71
print("Input: Altura del paciente: ", altura,"mts.")
#Cálculo del índice de rigidez canal 1 y 2
stiffness_index = altura/diff_time
stiffness_index_2 = altura/diff_time_2
print("Output: Indice de Rigidez  Extremidad Izquierda: ",stiffness_index,"m/s")
print("Output: Indice de Rigidez Extremidad Derecha: ",stiffness_index_2,"m/s")
#Diferencia entre máximos principales
diff = maxi_max[1]*ts - maxi_max[0]*ts
diff_2 = maxi_max_2[1]*ts - maxi_max_2[0]*ts
#Cálculo frecuencia cardíaca
fc = (1/diff)*60
fc_2 = (1/diff_2)*60
print("Output: Frecuencia Cardíaca con Canal Izquierdo: ",fc,"ppm")    
print("Output: Frecuencia Cardíaca con Canal Derecho: ",fc_2, "ppm")     

###############################################################################
#           ANÁLISIS DE LA SEÑAL DE ECG (VELOCIDAD DE ONDA DE PULSO)

N = N-1
#Extrae la señal de ECG
data_val_ecg = data_csv_3.values[0:N,1]
#Normalización de la señal de ECG
data_val_ecg = (data_val_ecg - np.mean(data_val_ecg))/np.std(data_val_ecg)
#Gráfica de la señal
plt.figure(3)
plt.subplot(212)
plt.plot(data_val_ecg)
#Aplica Filtro Pasa Bajas con frecuencia de corte de 100 Hz
fc = 100
# Frecuencia digital
Fc = fc/fs
#Frecuencia en radianes
Oc = 2*np.pi*Fc
#Constante C
C = np.tan(0.5*Oc)
#numerador de Hz
num = [C,C]
#denominador de Hz
den = [C+1, C-1]
#Respuesta en frecuencia del filtro digital
wz, Hwz = signal.freqz(num,den)
#Convierte wz a frecuencia digital o normalizada
F = wz/(2*np.pi)
#Convierte frecuencia digital a Hertz
f = F*fs
#Se obtiene el mÃ³dulo de Hwz
Hwzm = np.abs(Hwz)
#GrÃ¡fico
plt.figure(4)
plt.plot(f,Hwzm)
#Aplica filtro a la señal
data_ecg_filt = signal.lfilter(num,den,data_val_ecg)

#Aplica filtro Rechazo de Banda con Frecuencia central de 60 Hertz
fo = 60.0
#Frecuencia central normalizada
Fo = 2*np.pi*fo/fs
#Ancho de Banda
Q = 50
df = fo/Q 
#Ancho de banda normalizado
Df = 2*np.pi*df/fs
#Constante C
C = np.tan(0.5*Df)
#Constante beta
B = np.cos(Fo) 
#Numerador de la funciÃ³n de transferencia de H(z)
numz = [1,-2*B,1]
#Denominador de la funciÃ³n de transferencia de H(z)
denz = [C+1,-2*B,1-C]
#Respuesta en frecuencia del filtro digital
wz, Hwz = signal.freqz(numz,denz)
#Convierte wz a frecuencia digital o normalizada
F = wz/(2*np.pi)
#Convierte frecuencia digital a Hertz
f = F*fs
#Se obtiene el mÃ³dulo de Hwz
Hwzm = np.abs(Hwz)
#GrÃ¡fico
plt.figure(4)
plt.plot(f,Hwzm)
plt.title('RESPUESTA EN FRECUENCIA DE LOS FILTROS DIGITALES')
plt.xlabel('Frecuencia en Hertz')
#Aplica filtro a la señal
data_ecg_filt = signal.lfilter(numz,denz,data_ecg_filt)
#Gráfica de la señal
plt.figure(3)
plt.subplot(212)
plt.plot(data_ecg_filt)

#Arreglo para almacenar la derivada de la señal de PPG 1
derivative_ppg_1 = np.zeros(N-1)
derivative_ppg_2 = np.zeros(N-1)
#Derivada
for i in range(1,N):
    derivative_ppg_1[i-1] = (data_val[i] - data_val[i-1])
    derivative_ppg_2[i-1] = (data_val_2[i] - data_val_2[i-1])
    
#Aplica filtro Pasa Bajas a las señales PPG con frecuencia de corte de 30 Hz
fc = 30
# Frecuencia digital
Fc = fc/fs
#Frecuencia en radianes
Oc = 2*np.pi*Fc
#Constante C
C = np.tan(0.5*Oc)
#numerador de Hz
num = [C,C]
#denominador de Hz
den = [C+1, C-1]
#Aplica filtro a las señales
derivative_ppg_1 = signal.lfilter(num,den,derivative_ppg_1)
derivative_ppg_2 = signal.lfilter(num,den,derivative_ppg_2)
#Media de la señal fotopletismográfica
mean_ppg = np.mean(data_val)
mean_ppg_2 = np.mean(data_val_2)
#Gráfica de la señal
plt.figure(5)
plt.subplot(411)
plt.plot(data_val)
plt.plot(derivative_ppg_1*10 + mean_ppg)
plt.title('SEÑAL FOTOPLETISMOGRÁFICA CANAL IZQUIERDO')    
plt.subplot(413)
plt.plot(data_val_2)
plt.plot(derivative_ppg_2*10 + mean_ppg_2)    
plt.title('SEÑAL FOTOPLETISMOGRÁFICA CANAL DERECHO') 
    
#Máximos de la señal PPG 1
maximos_ppg = []
maximos_val_ppg = []
for i in range(0,N-2):
    if derivative_ppg_1[i] >= 0:
        if derivative_ppg_1[i+1] <= 0:
            maximos_ppg.append(i)
            maximos_val_ppg.append(data_val[i])
            plt.figure(5)
            plt.subplot(411)
            plt.plot(i,data_val[i],'.r')    
    
#Máximos de la señal PPG 2
maximos_ppg_2 = []
maximos_val_ppg_2 = []
for i in range(0,N-2):
    if derivative_ppg_2[i] >= 0:
        if derivative_ppg_2[i+1] <= 0:
            maximos_ppg_2.append(i)
            maximos_val_ppg_2.append(data_val_2[i])
            plt.figure(5)
            plt.subplot(413)
            plt.plot(i,data_val_2[i],'.r')      
    
#Busqueda de los máximos globales en la señal PPG 1
M = len(maximos_ppg)
maxi_maxi = []
for i in range(1,M-1):
    if maximos_val_ppg[i-1] < maximos_val_ppg[i] and maximos_val_ppg[i] > maximos_val_ppg[i+1]:
        maxi_maxi.append(maximos_ppg[i])
        plt.figure(5)
        plt.subplot(411)
        plt.plot(maximos_ppg[i],maximos_val_ppg[i],'.k')    
    
#Busqueda de los máximos globales en la señal PPG 2
M = len(maximos_ppg_2)
maxi_maxi_2 = []
for i in range(1,M-1):
    if maximos_val_ppg_2[i-1] < maximos_val_ppg_2[i] and maximos_val_ppg_2[i] > maximos_val_ppg_2[i+1]:
        maxi_maxi_2.append(maximos_ppg_2[i])
        plt.figure(5)
        plt.subplot(413)
        plt.plot(maximos_ppg_2[i],maximos_val_ppg_2[i],'.k')        
    
#Filtrado de la señal de ECG
ecg_filt = np.zeros(N-1)
a = 0.05
y_1 = 0
for i in range(0,N-1):
    ecg_filt[i] = a*data_ecg_filt[i] + (1-a)*y_1
    y_1 = ecg_filt[i]
    
#Filtro Tracking DC
ecg_filt = data_ecg_filt[0:N-1] - ecg_filt

#Gráfica de la señal
plt.figure(3)
plt.subplot(212)
plt.plot(ecg_filt,'k')   
plt.title('SEÑAL DE ECG FILTRADA') 
plt.xlabel('Número de Muestras')
plt.figure(5)
plt.subplot(412)
plt.plot(ecg_filt,'k') 
plt.title('SEÑAL DE ECG (DETECCIÓN DE COMPLEJO QRS)') 
plt.xlabel('Número de Muestras')
plt.subplot(414)
plt.plot(ecg_filt,'k') 
plt.title('SEÑAL DE ECG (DETECCIÓN DE COMPLEJO QRS)') 
plt.xlabel('Número de Muestras')
    
#Máximo de la señal de ECG
umbral = np.max(ecg_filt)/2
#print("Umbral: ",umbral)
#Busqueda de máximo global en señal de ecg
max_ecg = []
val = 0
ind = 0
for i in range(0,N-1):
    if ecg_filt[i] >= umbral:
        if ecg_filt[i] > val:  
            val = ecg_filt[i]
    else:
        if ecg_filt[i-1] >= umbral:
            max_ecg.append(i)
            #Gráfica de la señal
            plt.figure(5)
            plt.subplot(412)
            plt.plot(i,ecg_filt[i],'.r')
            plt.subplot(414)
            plt.plot(i,ecg_filt[i],'.r')
        val = 0    
  
#Encuentra diferencia de Tiempo entre máximos globales de las señales ECG y PPG 1
N1 = len(maxi_maxi)
N2 = len(max_ecg)
if N1 >= N2:
    MN = N1
    var = True
else:
    MN = N2
    var = False
i = 0
j = 0
bo = False
while i < MN:
    if var == True:
        for j in range(0,MN):
            if max_ecg[i] < maxi_maxi[j]: 
                dt = (maxi_maxi[j] - max_ecg[i])*ts
                bo = True
                break
                
            
    if var == False:
        for j in range(0,N2):
            if max_ecg[i] < maxi_maxi[j]: 
                dt = (maxi_maxi[j] - max_ecg[i])*ts
                bo = True
                break  
    if bo == False:            
        i += 1
    else:
        break
            
print("Output: Diferencia de Tiempo entre Máximos de PPG Canal Izquierdo y ECG: ",dt,"seg.")
distancia = 0.98
print('Input: Distancia del corazón a la Extremidad Izquierda', distancia,"mts")
vop = distancia/dt
print("Output: Velocidad de onda de Pulso Extremidad Izquierda: ",vop,"m/s")    
    
    
#Encuentra diferencia de Tiempo entre máximos globales de las señales ECG y PPG 2
N1 = len(maxi_maxi_2)
N2 = len(max_ecg)
if N1 >= N2:
    MN = N1
    var = True
else:
    MN = N2
    var = False
i = 0
j = 0
bo = False
while i < MN:
    if var == True:
        for j in range(0,MN):
            if max_ecg[i] < maxi_maxi_2[j]: 
                dt_2 = (maxi_maxi_2[j] - max_ecg[i])*ts
                bo = True
                break
                
            
    if var == False:
        for j in range(0,N2):
            if max_ecg[i] < maxi_maxi_2[j]: 
                dt_2 = (maxi_maxi_2[j] - max_ecg[i])*ts
                bo = True
                break  
    if bo == False:            
        i += 1
    else:
        break
            
print("Output: Diferencia de Tiempo entre Máximos de PPG Canal Izquierdo y ECG: ",dt_2,"seg.")
distancia_2 = 1.12
print('Input: Distancia del corazón a la Extremidad Derecha', distancia_2,"mts")
vop_2 = distancia_2/dt_2
print("Output: Velocidad de onda de Pulso Extremidad Derecha: ",vop_2,"m/s")        
    

plt.figure(1)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.figure(2)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.figure(3)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.figure(4)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.figure(5)
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
plt.show() 
plt.figure(1)
plt.savefig("Señales PPG.jpg", bbox_inches='tight')   
plt.figure(2)
plt.savefig("Señales PPG y Derivada.jpg", bbox_inches='tight') 
plt.figure(3)
plt.savefig("Señal de ECG.jpg", bbox_inches='tight') 
plt.figure(4)
plt.savefig("Respuesta en Frecuencia.jpg", bbox_inches='tight') 
plt.figure(5)
plt.savefig("Señales PPG y ECG.jpg", bbox_inches='tight') 
    
    
    
    
    