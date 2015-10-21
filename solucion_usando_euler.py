#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Complete el código a continuación.
'''
from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt

#Solucion a trayectoria
condicion_inicial = [10, 0, 0, 0.3]

Jupiter = Planeta(condicion_inicial)
x_value = []
y_value = []
E = []
dt=0.1
pasos=1000
t_values = np.array(range(pasos))*dt

for i in range(pasos):
    x_value.append(Jupiter.y_actual[0])
    y_value.append(Jupiter.y_actual[1])
    E.append(Jupiter.energia_total())
    Jupiter.avanza_euler(dt)

x_value = np.array(x_pos)
y_value = np.array(y_pos)
energia = np.array(energia)

fig=plt.figure(1)
plt.subplot(2, 1, 1)
fig.subplots_adjust(hspace=.5)
plt.plot(x_value , y_value)
plt.title(' 'u'Ó''rbita descrita por planeta (m'u'é''todo de Euler)')
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.savefig('Orbita_Euler.eps')
plt.show()



plt.subplot(2, 1, 2)
plt.plot(t_values, Energia)
plt.title("Energia a traves del tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Energia [J]")

plt.savefig("Energia_Euler.eps")
plt.show()
