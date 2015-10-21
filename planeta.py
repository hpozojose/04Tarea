#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
class Planeta(object):

G=1
M=1
    '''
    La clase planeta contiene funciones para integrar el potencial usando Euler,
    Runge-Kutta y Verlet, tambien se calcular con esta clase la energia de un
     planeta cualquiera, dependera del delta tiempo, la masa del
    planeta que sufre la atraccion, la constante alpha y las condiciones iniciales
    dadas
    '''

    def __init__(self, condicion_inicial, alpha=0, masa=1):
        '''
        __init__ es un metodo especial que se usa para inicializar las
        instancias de una clase.
        '''

        self.y_anterior = np.array([])
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha
        self.m = masa

    def ecuacion_de_movimiento(self):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        x, y, vx, vy = self.y_actual
        radio = np.sqrt(x**2 + y**2)
        cos_r = x/radio
        sen_r = y/radio
        a = G * M * ((2*self.alpha/(radio**3)) - 1/(radio**2))
        fx = cos_r * a
        fy = sen_r * a

        return [vx, vy, fx, fy]

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        y_init = self.y_actual
        der_y_init = self.ecuacion_de_movimiento()
        self.y_anterior = y_init
        self.y_actual = y_init + dt * der_y_init
        self.t_actual += dt
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        y_init = self.y_actual
        K1 = self.ecuacion_de_movimiento()
        self.y_actual = y_init + dt*K1/2.
        K2 = self.ecuacion_de_movimiento()
        self.y_actual = y_init + dt*K2/2.
        K3 = self.ecuacion_de_movimiento()
        self.y_actual = y_init + dt*K3
        K4 = self.ecuacion_de_movimiento()

        self.y_anterior = y_init
        self.y_actual = y_init + (K1+2*K2+2*K3+K4)*dt/6.
        self.t_actual += dt
        pass

    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        y_init = self.y_actual
        der_y_n = self.ecuacion_de_movimiento()
        y_n1 = 2*self.y_actual[0:2] - self.y_anterior[0:2] + (dt**2)*der_y_n[2:]
        dy_n1 = (y_n1 - self.y_actual[0:2])/dt

        self.y_anterior = y_init
        self.y_actual = np.concatenate((y_n1,dy_n1))
        self.t_actual += dt

        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        x, y, vx, vy = self.y_actual
        radio = np.sqrt(x**2 + y**2)
        U = - G * M * self.m/radio  + (self.alpha * G * M * self.m /(radio**2))
        K = (vx**2 + vt**2) * self.m/2.
        Energia = K + U

        return Energia
