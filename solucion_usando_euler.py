#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Complete el código a continuación.
'''
from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt


condicion_inicial = [10, 0, 0, 0.3]

Jupiter = Planeta(condicion_inicial)

t_final =  3000.
numero_pasos = 10000
dt= t_final / (float)(numero_pasos)
t_values = np.linspace(0,t_final,numero_pasos)
x = np.zeros(numero_pasos)
y = np.zeros(numero_pasos)
vx = np.zeros(numero_pasos)
vy = np.zeros(numero_pasos)

energia = np.zeros(numero_pasos)

[x[0],y[0],vx[0],vy[0]] = condicion_inicial
energia[0] = Jupiter.energia_total()
for i in range (1,numero_pasos):
    #pdb.set_trace()
    Jupiter.avanza_euler(dt)
    resultados = Jupiter.y_actual
    x[i] = resultados[0]
    y[i] = resultados[1]
    vx[i] = resultados[2]
    vy[i] = resultados[3]
    energia[i] = Jupiter.energia_total()

fig=plt.figure(1)
plt.subplot(2, 1, 1)
fig.subplots_adjust(hspace=.5)
plt.plot(x , y)
plt.axis('equal')
plt.title(' 'u'Ó''rbita descrita por planeta, m'u'é''todo de Euler')
plt.xlabel("x [m]")
plt.ylabel("y [m]")

plt.subplot(2, 1, 2)
plt.plot(t_values, energia)
plt.axis('equal')
plt.title('Energia a trav'u'é''s del tiempo')
plt.xlabel("Tiempo [s]")
plt.ylabel("Energia [J]")
plt.show()
