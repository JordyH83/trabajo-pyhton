# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:12:15 2021

@author: Jordy
"""

import random
while True:
    print("ingrese el numero mayor a 3 y menor que 40 ")
    tamaño = int(input())
    if tamaño>=4 and tamaño<=39:
        break
for i in range (0,tamaño):
    leer=random.randrange(0,1)
    rd=leer
    rd+=rd
    print("el valor acumulado es: ",rd)