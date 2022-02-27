# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:22:51 2022

@author: hongo
"""

def factorial(n):
    res=1
    for i in range(2, n+1):
        res*=i
    return res
num=5
print("Ene toonii factorial=", factorial(num))