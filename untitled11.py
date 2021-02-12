# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:25:43 2021

@author: Jordy
"""

import math
def Serie(x,n):
    s=0
    for i in range(n):
        term=x**i/math.factorial(i)
        s= s + term
        return s
    a=1
    b=3
    print("resultado:", Serie(a,b))