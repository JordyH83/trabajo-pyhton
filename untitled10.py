# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:23:22 2021

@author: Jordy
"""
def fib(n):
    a, b=0,1
    while a<n:
        print(a, end='')
        c=a+b
        a=b
        b=c
        print()
        fib(50)
