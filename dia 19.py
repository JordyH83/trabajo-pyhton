# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:21:41 2021

@author: Jordy
"""

lista=['R1','R2','R3','S1',"S2",'S3','6','5','AP']
for a in lista:
    if "R" in a:
        print ("los ruters son: ",a)
    elif "s" in a: 
        print ("los switch son: ",a)
    else:
        print ("no son equipo de red",a)