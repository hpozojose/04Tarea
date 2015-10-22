from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt


condicion_inicial = [10, 0, 0, 0.3]

Jupiter = Planeta(condicion_inicial)
x_value = []
y_value = []
E = []
dt=0.1
pasos=10500
t_values = np.array(range(pasos))*dt

for i in range(pasos):
    x_value.append(Jupiter.y_actual[0])
    y_value.append(Jupiter.y_actual[1])
    E.append(Jupiter.energia_total())
    Jupiter.avanza_rk4(dt)


x_value = np.array(x_value)
y_value = np.array(y_value)
energia = np.array(E)
print energia

fig=plt.figure(1)
plt.subplot(2, 1, 1)
fig.subplots_adjust(hspace=.5)
plt.plot(x_value , y_value)
plt.axis('equal')
plt.title('Orbita descrita por planeta,Runge-Kutta')
plt.xlabel("x [m]")
plt.ylabel("y [m]")

plt.subplot(2, 1, 2)
plt.plot(t_values, energia)
plt.axis('equal')
plt.title('Energia a traves del tiempo')
plt.xlabel("Tiempo [s]")
plt.ylabel("Energia [J]")
plt.show()
