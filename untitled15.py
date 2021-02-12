# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:50:58 2021

@author: Jordy
"""

filas=int(input("introduce el numero de filas: "))
columnas=int(input("introduce el numero de columnas: "))
matriz=[]
for i in range (filas):
    matriz.append([0]*columnas)
    for i in range(filas):
       for j in range(columnas):
           matriz[i][j]= float(input("Fila {} : ".format(i+1, j+1)))