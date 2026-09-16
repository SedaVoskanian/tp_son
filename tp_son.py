
import numpy as np
import matplotlib as plt
from IPython.display import Audio, display
from scipy.io import wavfile

rate=44100
LA=440
DO = 523.25

#1. Il faut 44100 échantillons dans notre tableau pour une durée de 1 seconde
#2.équation mathématique qui donne la position de la membrane en fonction du temps $t$ sur l'intervalle $[0, 1]$ pour une fréquence $\phi$

def f(t,phi):
    return np.sin(phi*t*2*np.pi)

#3.
x=np.linspace(0,1,rate)
son=f(x,440)

plt.plot(x[1:2205],son[1:2205],label="son 0.05s")
plt.legend()
#plt.show()



#display(Audio(signal,rate))


