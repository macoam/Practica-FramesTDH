import wave 
import numpy as np
import matplotlib.pyplot as plt

#Cargar archivo wav en la variable 

Claps = wave.open('Claps.wav', 'r')
WaitAMinute = wave.open('WaitAMinute.wav', 'r')

#Obtener todos los frames del objeto wave
frames_c = Claps.readframes(-1)
frames_w = WaitAMinute.readframes(-1)

#Mostrar el resultado de frames
#print(frames [:10])

#Convierte el audio good morning de bytes a enteros
ondaconvertida = np.frombuffer(frames_c, dtype='int16')
ondaconvertida_t = np.frombuffer(frames_w, dtype='int16')
#print(ondaconvertida [:10])

framerate_c = Claps.getframerate()
framerate_w = WaitAMinute.getframerate()

print(framerate_c)
print(framerate_w)

time_c = np.linspace(start = 0, stop = len(ondaconvertida ) /framerate_c, num= len(ondaconvertida))
time_w = np.linspace(start = 0, stop = len(ondaconvertida_t ) /framerate_w, num= len(ondaconvertida_t))

print(time_c[:10])
print(time_w[:10])

#Generación de la gráfica

plt.title('Audios')

#etiquetas de los ojos
plt.xlabel('Tiempo segundos')
plt.ylabel('Amplitud')

#Agregar la informacion
plt.plot(time_c, ondaconvertida, label='Claps')
plt.plot(time_w, ondaconvertida_t, label='Wait a Minute', alpha = 0.5)

plt.legend()
plt.show()