# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:54:48 2021

@author: Jordy
"""

a= float(input("ingrese las horas actuales recorridas: "))
b= int(input("ingrese la velocidad de desplasamiento(km/h): "))
distancia= a*b
distanciafaltante= (334-distancia)
print("la distancia recorrida es ", distancia)
print("la distancia faltante es ", distanciafaltante)
tiempototal= (334/b)
tiempofaltante= (tiempototal-a)
print("el tiempo faltante para llegar el destino es: ", tiempofaltante)