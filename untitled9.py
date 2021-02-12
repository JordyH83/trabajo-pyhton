# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:16:56 2021

@author: Jordy
"""

vector=[str() for i in range(10)]
print("ingrese tamaño del vector: ")
tamanovector= int(input())
for i in range (1,tamanovector+1):
    print("ingrese el nombre del estudiante ",i)
    nombre=input()
    vector[i-1]= nombre
    for j in range(1,tamanovector+1):
        for l in range(1,tamanovector):
            if vector[l-1]>vector[1]:
                auxiliar=vector[l-1]
                vector[l-1]= vector[1]
                vector[l]= auxiliar
                for k in range (1,tamanovector+1):
                    print(" el vector resultante es: ", vector[k-1])
            