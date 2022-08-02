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
<img src="https://user-images.githubusercontent.com/95665770/182489391-2ee927f3-27df-4f56-a381-23f5c9e4ce86.png" width="480" height="400">
## Cyton Biosensing Board
<img src="https://user-images.githubusercontent.com/95665770/182492633-d595c1f7-4e3e-43d4-8337-10b2f2d65ec3.png" width="480" height="400">



