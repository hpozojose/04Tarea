#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt


condicion_inicial = [10, 0, 0, 0.3]

Jupiter = Planeta(condicion_inicial)
x_value = []
y_value = []
E = []
dt=0.1
pasos=10000
t_values = np.array(range(pasos))*dt

for i in range(pasos):
    x_value.append(Jupiter.y_actual[0])
    y_value.append(Jupiter.y_actual[1])
    E.append(Jupiter.energia_total())
    Jupiter.avanza_verlet(dt)


x_value = np.array(x_value)
y_value = np.array(y_value)
energia = np.array(E)

fig=plt.figure(1)
plt.subplot(2, 1, 1)
fig.subplots_adjust(hspace=.5)
plt.plot(x_value , y_value)
plt.axis('equal')
plt.title(' 'u'Ó''rbita descrita por planeta, Verlet')
plt.xlabel("x [m]")
plt.ylabel("y [m]")

plt.subplot(2, 1, 2)
plt.plot(t_values, energia)
plt.axis('equal')
plt.title('Energia a trav'u'é''s del tiempo')
plt.xlabel("Tiempo [s]")
plt.ylabel("Energia [J]")
plt.show()
