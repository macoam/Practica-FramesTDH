import wave 
import numpy as np
import matplotlib.pyplot as plt

#Cargar archivo wav en la variable 

Claps = wave.open('Claps.wav', 'r')
WaitAMinute = wave.open('WaitAMinute.wav', 'r')

#Obtener todos los frames del objeto wave

frames = Claps.readframes(-1)
frames_w = WaitAMinute.readframes(-1)

#Mostrar el resultado de frames
#print(frames [:10])

#Convierte el audio good morning de bytes a enteros

ondaconvertida = np.frombuffer(frames, dtype='int16')
ondaconvertida_w = np.frombuffer(frames_w, dtype='int16')

#Print

framerate_c = Claps.getframerate()
framerate_w = WaitAMinute.getframerate()

print(framerate_c)
print(framerate_w)

time_c = np.linspace(start = 0, stop = len(ondaconvertida ) /framerate_c, num= len(ondaconvertida))
time_w = np.linspace(start = 0, stop = len(ondaconvertida_w ) /framerate_w, num= len(ondaconvertida_w))

print(time_c[:10])
print(time_w[:10])

#Generar gráfica

plt.title('Audios')

#Nomre de secciones

plt.xlabel('Tiempo')
plt.ylabel('Amplitud')

#Información

plt.plot(time_c, Claps, label='Claps')
plt.plot(time_w, WaitAMinute, label='WaitAMinute', alpha = 0.5)

plt.legend()
plt.show()