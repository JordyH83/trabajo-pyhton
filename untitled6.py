# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:09:41 2021

@author: Jordy
"""

nombres=input("ingrese el nombre: ")
apellidos=input("ingrese el apellido: ")
nota1= int(input("ingrese la nota 1: "))
nota2= int(input("ingrese la nota 2: "))
nota3= int(input("ingrese la nota 3: "))
promedio=(nota1+nota2+nota3)/3
print("el promedio para: ", nombres,apellidos, "es: ","{:.4f}".format(promedio))