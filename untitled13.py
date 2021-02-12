# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:37:48 2021

@author: Jordy
"""

flag="while"
a, b, c, d=2, 1, 0, 3
if a==b or b!=3:
    flag="yellow"
    if b**d+c < c+a+d**a:
        flag="red"
        if d%2==d-a: 
            flag="black"
        else: 
            flag="brown"
    else:
            flag="blue"
            print(flag)
            