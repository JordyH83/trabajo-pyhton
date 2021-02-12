# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:29:40 2021

@author: Jordy
"""

x=10
y=7
z=x%y
result="0"
if x==z:
    result+="1"
elif x<z:
    result+="2"
elif y>z:
    result+="3"
elif x==z:
    result+="4"
else:
    result+="5"
    print(result)