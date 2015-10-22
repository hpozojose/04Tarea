#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
G=1
M=1
class Planeta(object):


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
        self.y_actual = np.array(condicion_inicial)
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
        a=self.alpha
        cos_r = x/radio
        sen_r = y/radio
        f = G * M * ((2.*a/(radio**4)) - 1/(radio**3))
        fx = x*f
        fy = y*f


        return np.array([vx, vy, fx, fy])

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''

        self.y_anterior = self.y_actual
        self.y_actual = self.y_anterior + dt * (self.ecuacion_de_movimiento())
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
        x_n1 = 2*self.y_actual[0] - self.y_anterior[0] + (dt**2)*der_y_n[2]
        y_n1 = 2*self.y_actual[1] - self.y_anterior[1] + (dt**2)*der_y_n[3]
        dx_n1 = (x_n1 - self.y_actual[0])/dt
        dy_n1 = (y_n1 - self.y_actual[1])/dt

        self.y_anterior = y_init
        self.y_actual = np.concatenate((x_n1 ,y_n1 ,dx_n1 ,dy_n1))
        self.t_actual += dt

        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        Y = self.y_actual
        r = np.sqrt(Y[0]**2 + Y[1]**2)
        K = (Y[2]**2 + Y[3]**2)/2.
        U = -G*M*(1/r + self.alpha/r**2)
        return (K + U)*self.m
